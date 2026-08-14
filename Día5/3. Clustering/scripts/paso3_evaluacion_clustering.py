# Paso 3: visualización de clusters y centroides sobre datos de evaluación independientes

import os
import pandas as pd
import matplotlib.pyplot as plt
import joblib
from perfiles_clustering import PERFILES, mapear_clusters_a_perfiles, obtener_estimador_final, obtener_centroides

plt.rcParams['font.sans-serif'] = 'Segoe UI'

# Paso 1: rutas relativas
script_dir = os.path.dirname(os.path.abspath(__file__))
ruta_eval = os.path.join(script_dir, "..", "datos", "dataset_evaluacion_clustering.csv")
ruta_modelo = os.path.join(script_dir, "..", "modelos", "modelo_clustering.joblib")

# Paso 2: cargar modelo y datos de evaluación
modelo_clustering = joblib.load(ruta_modelo)
df_eval = pd.read_csv(ruta_eval)

# Paso 3: asignar clusters a los datos nuevos que la IA nunca vio (el Pipeline escala internamente)
df_eval['cluster'] = modelo_clustering.predict(df_eval)

# Paso 4: extraer centroides en escala original
columnas_originales = [c for c in df_eval.columns if c != 'cluster']
estimador_final = obtener_estimador_final(modelo_clustering)
centroides_finales = obtener_centroides(estimador_final)

escalador = modelo_clustering.named_steps.get("escalador") if hasattr(modelo_clustering, "named_steps") else None
centroides_reales = escalador.inverse_transform(centroides_finales) if escalador is not None else centroides_finales

n_clusters_reales = len(centroides_reales)

# El ID de cluster es arbitrario: se recalcula el perfil real de cada uno
# a partir de sus características, igual que en Paso 2, para que nombres y colores
# nunca queden desincronizados del algoritmo.
mapa_cluster_a_perfil = mapear_clusters_a_perfiles(centroides_reales, columnas_originales)

# Paso 5: visualización en 2D del mapa de grupos de viajeros
fig, ax = plt.subplots(figsize=(11, 6.5))

for c_id in range(n_clusters_reales):
    perfil = PERFILES[mapa_cluster_a_perfil[c_id]]
    sub = df_eval[df_eval['cluster'] == c_id]
    ax.scatter(sub['frecuencia_viajes_ano'], sub['tiempo_estadia_dias'],
               color=perfil['color'], alpha=0.75, s=65, edgecolors='black',
               label=f"Grupo #{c_id}: {perfil['nombre']}")

# Dibujar Centroides de cada grupo (Marcador 'X' grande o estrella)
for c_id in range(n_clusters_reales):
    c_x = centroides_reales[c_id, 0] # frecuencia
    c_y = centroides_reales[c_id, 1] # estadía
    ax.scatter(c_x, c_y, color='black', marker='X', s=250, linewidths=2.5, zorder=10)
    ax.text(c_x, c_y + 2.5, f'Centroide {c_id}', fontsize=10, fontweight='bold', ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#ffffff', edgecolor='black', alpha=0.85))

nombre_modelo = type(estimador_final).__name__
ax.set_title(f'Paso 3: Segmentación de Viajeros en 2D ({nombre_modelo} en Datos Nuevos)', fontsize=13, fontweight='bold', pad=15)
ax.set_xlabel('Frecuencia de Viajes al Año', fontsize=11, fontweight='bold')
ax.set_ylabel('Tiempo de Estadía (Días)', fontsize=11, fontweight='bold')
ax.legend(fontsize=10, loc='upper right')
ax.grid(True, linestyle='--', alpha=0.5)

plt.figtext(0.5, 0.02,
            "[CÓMO INTERPRETAR LA GRÁFICA DE CLUSTERS]:\n"
            "• Cada punto coloreado representa a 1 pasajero evaluado por la IA en datos independientes.\n"
            "• Las marcas 'X' negras son los CENTROIDES (el centro de gravedad / pasajero promedio de cada perfil).\n"
            f"• {nombre_modelo} asigna automáticamente a cada viajero el grupo del centroide que le queda más cerca.\n"
            "• Este mapa solo muestra 2 de las 4 variables usadas para agrupar: puede haber puntos que se vean cerca\n"
            "  aquí pero pertenezcan a grupos distintos por diferencias en monto declarado o tiempo de trámite.\n"
            "Siguiente paso -> ejecutar 'paso4_simulador_clustering.py'",
            ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8f9fa', edgecolor='#cccccc'))

fig.tight_layout(rect=[0, 0.18, 1, 0.95])

plt.show()
