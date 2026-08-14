# Paso 4: simulador visual (asignación de perfil en vivo) con el modelo entrenado

import os
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib.patches import FancyBboxPatch
from perfiles_clustering import PERFILES, mapear_clusters_a_perfiles, obtener_estimador_final, obtener_centroides

plt.rcParams['font.sans-serif'] = 'Segoe UI'
plt.rcParams['axes.edgecolor'] = '#cccccc'


# Paso 1: cargar modelo y datos de historia
script_dir = os.path.dirname(os.path.abspath(__file__))
ruta_modelo = os.path.join(script_dir, "..", "modelos", "modelo_clustering.joblib")
ruta_historia = os.path.join(script_dir, "..", "datos", "dataset_historia_clustering.csv")

try:
    modelo_clustering = joblib.load(ruta_modelo)
    df_historia = pd.read_csv(ruta_historia)
except Exception as e:
    print(f"Error cargando el modelo o datos: {e}")
    exit()

# El ID de cluster es arbitrario: se recalcula el perfil real de cada uno
# a partir de sus características, igual que en Pasos 2 y 3.
columnas_originales = list(df_historia.columns)
estimador_final = obtener_estimador_final(modelo_clustering)
centroides_finales = obtener_centroides(estimador_final)

escalador = modelo_clustering.named_steps.get("escalador") if hasattr(modelo_clustering, "named_steps") else None
centroides_reales_hist = escalador.inverse_transform(centroides_finales) if escalador is not None else centroides_finales

mapa_cluster_a_perfil = mapear_clusters_a_perfiles(centroides_reales_hist, columnas_originales)

# Paso 2: crear ventana principal
fig = plt.figure(figsize=(12, 8.5), facecolor='#f4f6f9')
fig.canvas.manager.set_window_title('Migración Panamá - Clasificador de Perfiles de Viajeros (Clustering)')

# Encabezado Principal
plt.suptitle('Sistema de Identificación de Perfiles de Viajeros con IA', 
             fontsize=15, fontweight='bold', color='#003366', y=0.96)

fig.text(0.5, 0.92, 
         'Ingresa las características de un pasajero que llega a la ventanilla para asignarlo a su perfil operativo.',
         ha='center', fontsize=10.5, color='#444444')

# Paso 3: definir áreas de la interfaz
ax_perfil = fig.add_axes([0.48, 0.26, 0.47, 0.60])
ax_tarjeta = fig.add_axes([0.48, 0.04, 0.47, 0.18])
ax_tarjeta.axis('off')

# Valores iniciales: el centroide del perfil MÁS COMÚN (no el promedio de todo el dataset).
# El promedio de las 400 historias mezcla los 3 perfiles y cae en una zona ambigua, sin
# parecerse de verdad a ningún viajero real; arrancar en un centroide da un primer ejemplo
# claro y con alta similitud, en vez de una lectura confusa al abrir el simulador.
cluster_mas_comun = pd.Series(modelo_clustering.predict(df_historia)).value_counts().idxmax()
centroide_inicial = centroides_reales_hist[cluster_mas_comun]
init_frec = int(round(centroide_inicial[0]))
init_estadia = float(round(centroide_inicial[1], 1))
init_monto = float(round(centroide_inicial[2], 2))
init_tramite = float(round(centroide_inicial[3], 1))

# Paso 4: crear sliders/palancas
ax_s1 = fig.add_axes([0.08, 0.74, 0.32, 0.035], facecolor='#e6ecf5')
ax_s2 = fig.add_axes([0.08, 0.58, 0.32, 0.035], facecolor='#e6ecf5')
ax_s3 = fig.add_axes([0.08, 0.42, 0.32, 0.035], facecolor='#e6ecf5')
ax_s4 = fig.add_axes([0.08, 0.26, 0.32, 0.035], facecolor='#e6ecf5')

slider_frec = Slider(ax_s1, '', 1, 40, valinit=init_frec, valstep=1, color='#00529B')
slider_estadia = Slider(ax_s2, '', 1, 90, valinit=init_estadia, valstep=1, color='#7B1FA2')
slider_monto = Slider(ax_s3, '', 500, 8000, valinit=init_monto, valstep=100, color='#2E7D32')
slider_tramite = Slider(ax_s4, '', 1, 30, valinit=init_tramite, valstep=0.5, color='#D9381E')

# Etiquetas sobre los controles
fig.text(0.08, 0.79, '[ Frecuencia de Viajes al Año ]', fontsize=10.5, fontweight='bold', color='#00529B')
fig.text(0.08, 0.77, '(Entradas/Salidas registradas en los últimos 12 meses)', fontsize=8.5, color='#555555')

fig.text(0.08, 0.63, '[ Tiempo de Estadía (Días) ]', fontsize=10.5, fontweight='bold', color='#7B1FA2')
fig.text(0.08, 0.61, '(Duración prevista de su permanencia en el país)', fontsize=8.5, color='#555555')

fig.text(0.08, 0.47, '[ Monto Declarado (USD) ]', fontsize=10.5, fontweight='bold', color='#2E7D32')
fig.text(0.08, 0.45, '(Fondos económicos o dinero reportado al ingresar)', fontsize=8.5, color='#555555')

fig.text(0.08, 0.31, '[ Tiempo de Trámite (Minutos) ]', fontsize=10.5, fontweight='bold', color='#D9381E')
fig.text(0.08, 0.29, '(Duración de la verificación en la taquilla migratoria)', fontsize=8.5, color='#555555')

# Botón Reset
ax_boton = fig.add_axes([0.15, 0.12, 0.18, 0.05])
boton_reset = Button(ax_boton, 'Restablecer Valores', color='#ffffff', hovercolor='#e2e8f0')

# Paso 5: función de actualización del identificador de perfil
def actualizar(val=None):
    frec = slider_frec.val
    est = slider_estadia.val
    mon = slider_monto.val
    tra = slider_tramite.val

    df_nuevo = pd.DataFrame({
        'frecuencia_viajes_ano': [frec],
        'tiempo_estadia_dias': [est],
        'monto_declarado_usd': [mon],
        'tiempo_tramite_min': [tra]
    })

    # Predecir cluster (el Pipeline escala internamente si corresponde)
    cluster_asignado = modelo_clustering.predict(df_nuevo)[0]

    # Distancia al centroide del cluster asignado, en el mismo espacio que usa el modelo
    entrada_transformada = escalador.transform(df_nuevo)[0] if escalador is not None else df_nuevo.iloc[0].to_numpy(dtype=float)
    distancia = np.linalg.norm(entrada_transformada - centroides_finales[cluster_asignado])
    
    # Limpiar panel derecho
    ax_perfil.clear()
    ax_perfil.axis('off')
    
    # Mapeo de estilos según el perfil real del cluster descubierto (no según el ID crudo)
    perfil = PERFILES[mapa_cluster_a_perfil[cluster_asignado]]
    color_fondo = perfil['color_fondo']
    color_borde = perfil['color']
    titulo_perfil = f"GRUPO #{cluster_asignado}: {perfil['nombre'].upper()}"
    desc_perfil = perfil['descripcion']
    rec_operativa = perfil['recomendacion']

    # Dibujar tarjeta de perfil visual
    patch_tarjeta = FancyBboxPatch((0.05, 0.1), 0.9, 0.8, boxstyle="round,pad=0.03,rounding_size=0.05",
                                    facecolor=color_fondo, edgecolor=color_borde, linewidth=3)
    ax_perfil.add_patch(patch_tarjeta)
    
    ax_perfil.plot(0.5, 0.68, marker='o', markersize=42, color=color_borde)
    ax_perfil.text(0.5, 0.68, str(cluster_asignado), ha='center', va='center', fontsize=18, fontweight='bold', color='white')
    
    ax_perfil.text(0.5, 0.44, titulo_perfil, ha='center', va='center', fontsize=11.5, fontweight='bold', color='#111111')
    ax_perfil.text(0.5, 0.32, desc_perfil, ha='center', va='center', fontsize=9.5, color='#444444')
    ax_perfil.text(0.5, 0.20, f'Similitud con el Perfil Promedio: {(1/(1+distancia))*100:.0f}%', 
                   ha='center', va='center', fontsize=10.5, fontweight='bold', color=color_borde)
    
    ax_perfil.set_xlim(0, 1)
    ax_perfil.set_ylim(0, 1)
    
    # Tarjeta explicativa abajo
    ax_tarjeta.clear()
    ax_tarjeta.axis('off')
    
    texto_explicativo = (
        f"DIAGNÓSTICO DEL SISTEMA DE CLUSTERING (IA NO SUPERVISADA):\n"
        f"-------------------------------------------------------------\n"
        f"• Recomendación Operativa: {rec_operativa}\n"
        f"• El pasajero ingresado (Frecuencia: {int(frec)}, Estadía: {int(est)} días, ${mon:,.0f} USD) ha sido asignado\n"
        f"  automáticamente al Grupo #{cluster_asignado} ({perfil['nombre']}) por cercanía matemática a su centroide."
    )

    ax_tarjeta.text(0.02, 0.5, texto_explicativo, va='center', ha='left', fontsize=9.5,
                    bbox=dict(boxstyle='round,pad=0.6', facecolor='#ffffff', edgecolor='#00529B', linewidth=1.5))

    fig.canvas.draw_idle()

slider_frec.on_changed(actualizar)
slider_estadia.on_changed(actualizar)
slider_monto.on_changed(actualizar)
slider_tramite.on_changed(actualizar)

def reset(event):
    slider_frec.reset()
    slider_estadia.reset()
    slider_monto.reset()
    slider_tramite.reset()

boton_reset.on_clicked(reset)

actualizar()

plt.show()
