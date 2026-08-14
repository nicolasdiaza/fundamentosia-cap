# Paso 4: simulador visual (medidor de capacidad) con el modelo entrenado

import os
import itertools
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from sklearn.metrics import mean_absolute_error

plt.rcParams['font.sans-serif'] = 'Segoe UI'
plt.rcParams['axes.edgecolor'] = '#cccccc'


def obtener_estimador_final(modelo):
    # Si es un Pipeline devuelve el último paso (el estimador real); si no, el modelo tal cual
    if hasattr(modelo, "named_steps"):
        return list(modelo.named_steps.values())[-1]
    return modelo


# Paso 1: cargar el modelo entrenado
script_dir = os.path.dirname(os.path.abspath(__file__))
ruta_modelo = os.path.join(script_dir, "..", "modelos", "modelo_regresion.joblib")
ruta_historia = os.path.join(script_dir, "..", "datos", "dataset_historia_migracion.csv")
ruta_eval_final = os.path.join(script_dir, "..", "datos", "dataset_evaluacion_final.csv")

try:
    modelo_regresion = joblib.load(ruta_modelo)
    df_historia = pd.read_csv(ruta_historia)
    df_eval_final = pd.read_csv(ruta_eval_final)
except Exception as e:
    print(f"Error cargando el modelo o datos: {e}")
    exit()

COLUMNAS_MODELO = ['inspectores_turno', 'presupuesto_usd', 'tiempo_espera_min']

# Margen de error real del modelo (el mismo cálculo que hace el Paso 3),
# en vez de un número fijo escrito a mano.
MAE_MODELO = mean_absolute_error(
    df_eval_final['tramites_procesados'],
    modelo_regresion.predict(df_eval_final[COLUMNAS_MODELO])
)

# Lo que la IA aprendió en el Paso 2, para mostrarlo junto a cada palanca
ESTIMADOR_FINAL = obtener_estimador_final(modelo_regresion)
TIENE_COEFICIENTES = hasattr(ESTIMADOR_FINAL, "coef_")
TIENE_IMPORTANCIAS = hasattr(ESTIMADOR_FINAL, "feature_importances_")

if TIENE_COEFICIENTES:
    coef = np.array(ESTIMADOR_FINAL.coef_, dtype=float)
    escalador = modelo_regresion.named_steps.get("escalador") if hasattr(modelo_regresion, "named_steps") else None
    if escalador is not None and hasattr(escalador, "scale_"):
        coef = coef / escalador.scale_  # volver a unidades originales, igual que en paso2
    COEF_INSPECTORES, COEF_PRESUPUESTO, COEF_ESPERA = coef
elif TIENE_IMPORTANCIAS:
    IMP_INSPECTORES, IMP_PRESUPUESTO, IMP_ESPERA = ESTIMADOR_FINAL.feature_importances_

# Paso 2: crear ventana principal
fig = plt.figure(figsize=(12, 8.5), facecolor='#f4f6f9')
fig.canvas.manager.set_window_title('Migración Panamá - Medidor de Capacidad con IA')

# Encabezado Principal
plt.suptitle('Simulador de Capacidad de Atención Migratoria (IA)', 
             fontsize=16, fontweight='bold', color='#003366', y=0.96)

fig.text(0.5, 0.92,
         'Mueve las palancas de la izquierda para ver cuántos trámites podrá atender la estación.',
         ha='center', fontsize=11, color='#444444')

# Título del medidor: se dibuja una sola vez en una posición fija de la figura
# (en vez de ax.set_title) para que nunca choque con la leyenda de zonas.
fig.text(0.715, 0.82, 'MEDIDOR DE CAPACIDAD DE ATENCIÓN EN TIEMPO REAL',
         ha='center', fontsize=12, fontweight='bold')

# Paso 3: definir áreas de la interfaz
ax_medidor = fig.add_axes([0.48, 0.24, 0.47, 0.54])
ax_tarjeta = fig.add_axes([0.48, 0.04, 0.47, 0.16])
ax_tarjeta.axis('off')

# Valores iniciales (Promedios)
init_inspectores = int(df_historia['inspectores_turno'].mean())
init_presupuesto = float(df_historia['presupuesto_usd'].mean())
init_espera = float(df_historia['tiempo_espera_min'].mean())

# Val min y max históricos para el medidor
MIN_HISTORICO = int(df_historia['tramites_procesados'].min())
MAX_HISTORICO = int(df_historia['tramites_procesados'].max())
PROMEDIO_HISTORICO = df_historia['tramites_procesados'].mean()

# Zonas Baja/Media/Alta calculadas desde los propios datos (terciles),
# en vez de números fijos.
ZONA_BAJA_MAX = df_historia['tramites_procesados'].quantile(0.33)
ZONA_MEDIA_MAX = df_historia['tramites_procesados'].quantile(0.66)

# Rangos de cada palanca (se reutilizan para los sliders y para calcular
# el máximo teórico que puede marcar el medidor, y así el eje nunca recorta la aguja)
RANGO_INSPECTORES = (5, 40)
RANGO_PRESUPUESTO = (800, 7000)
RANGO_ESPERA = (10, 60)

esquinas = pd.DataFrame(
    itertools.product(RANGO_INSPECTORES, RANGO_PRESUPUESTO, RANGO_ESPERA),
    columns=COLUMNAS_MODELO
)
PREDICCION_MAXIMA_TEORICA = modelo_regresion.predict(esquinas).max()
XLIM_MEDIDOR = max(MAX_HISTORICO, PREDICCION_MAXIMA_TEORICA) * 1.1

# Paso 4: crear sliders/palancas
ax_slider1 = fig.add_axes([0.08, 0.70, 0.32, 0.04], facecolor='#e6ecf5')
ax_slider2 = fig.add_axes([0.08, 0.50, 0.32, 0.04], facecolor='#e6ecf5')
ax_slider3 = fig.add_axes([0.08, 0.30, 0.32, 0.04], facecolor='#e6ecf5')

slider_inspectores = Slider(ax_slider1, '', *RANGO_INSPECTORES, valinit=init_inspectores, valstep=1, color='#00529B')
slider_presupuesto = Slider(ax_slider2, '', *RANGO_PRESUPUESTO, valinit=init_presupuesto, valstep=50, color='#2E7D32')
slider_espera = Slider(ax_slider3, '', *RANGO_ESPERA, valinit=init_espera, valstep=0.5, color='#D9381E')

# Texto de cada palanca: fórmula de coeficiente o % de importancia, según el modelo
if TIENE_COEFICIENTES:
    texto_insp = f'Lo que la IA aprendió: +1 inspector = {COEF_INSPECTORES:+.0f} trámites'
    texto_pres = f'Lo que la IA aprendió: +$1 USD = {COEF_PRESUPUESTO:+.2f} trámites'
    texto_esp = f'Lo que la IA aprendió: +1 minuto = {COEF_ESPERA:+.0f} trámites'
elif TIENE_IMPORTANCIAS:
    texto_insp = f'Lo que la IA aprendió: esta variable pesa {IMP_INSPECTORES*100:.0f}% en su decisión'
    texto_pres = f'Lo que la IA aprendió: esta variable pesa {IMP_PRESUPUESTO*100:.0f}% en su decisión'
    texto_esp = f'Lo que la IA aprendió: esta variable pesa {IMP_ESPERA*100:.0f}% en su decisión'
else:
    texto_insp = texto_pres = texto_esp = ''

# Textos sobre las palancas (sin emojis para evitar advertencias de tipografía)
fig.text(0.08, 0.76, '[ Inspectores de Turno ]', fontsize=11, fontweight='bold', color='#00529B')
fig.text(0.08, 0.74, '(Ventanillas abiertas atendiendo personas)', fontsize=9, color='#555555')
fig.text(0.08, 0.665, texto_insp, fontsize=8.5, color='#00529B', style='italic')

fig.text(0.08, 0.56, '[ Presupuesto Operativo (USD) ]', fontsize=11, fontweight='bold', color='#2E7D32')
fig.text(0.08, 0.54, '(Fondo diario para sistemas y horas extra)', fontsize=9, color='#555555')
fig.text(0.08, 0.465, texto_pres, fontsize=8.5, color='#2E7D32', style='italic')

fig.text(0.08, 0.36, '[ Tiempo de Espera (Minutos) ]', fontsize=11, fontweight='bold', color='#D9381E')
fig.text(0.08, 0.34, '(Tiempo que tarda cada persona en la fila)', fontsize=9, color='#555555')
fig.text(0.08, 0.265, texto_esp, fontsize=8.5, color='#D9381E', style='italic')

# Botón Reset
ax_boton = fig.add_axes([0.15, 0.14, 0.18, 0.05])
boton_reset = Button(ax_boton, 'Restablecer Valores', color='#ffffff', hovercolor='#e2e8f0')

# Paso 5: función de actualización del medidor de capacidad
def actualizar(val=None):
    insp = slider_inspectores.val
    pres = slider_presupuesto.val
    esp = slider_espera.val
    
    # Predicción IA
    df_input = pd.DataFrame({
        'inspectores_turno': [insp],
        'presupuesto_usd': [pres],
        'tiempo_espera_min': [esp]
    })
    
    prediccion = modelo_regresion.predict(df_input)[0]
    prediccion = max(0, int(round(prediccion)))
    
    # Calcular nivel porcentual de capacidad
    porcentaje_capacidad = (prediccion - MIN_HISTORICO) / (MAX_HISTORICO - MIN_HISTORICO) * 100
    porcentaje_capacidad = np.clip(porcentaje_capacidad, 0, 100)
    
    # Limpiar panel del medidor
    ax_medidor.clear()

    # Barra de fondo (Zonas de color calculadas desde los datos reales, por terciles)
    ax_medidor.barh([0], [ZONA_BAJA_MAX], color='#ffcdd2', height=0.5, label=f'Baja (<{ZONA_BAJA_MAX:.0f})')
    ax_medidor.barh([0], [ZONA_MEDIA_MAX - ZONA_BAJA_MAX], left=[ZONA_BAJA_MAX], color='#fff9c4', height=0.5,
                     label=f'Media ({ZONA_BAJA_MAX:.0f}-{ZONA_MEDIA_MAX:.0f})')
    ax_medidor.barh([0], [XLIM_MEDIDOR - ZONA_MEDIA_MAX], left=[ZONA_MEDIA_MAX], color='#c8e6c9', height=0.5,
                     label=f'Alta (>{ZONA_MEDIA_MAX:.0f})')

    # Marcador/Aguja de la IA
    color_aguja = '#d32f2f' if prediccion < ZONA_BAJA_MAX else ('#fbc02d' if prediccion < ZONA_MEDIA_MAX else '#388e3c')

    # Barra indicadora de la predicción real
    ax_medidor.barh([0], [prediccion], color=color_aguja, height=0.25, alpha=0.95)
    ax_medidor.plot(prediccion, 0, marker='o', markersize=14, color='black')

    # Texto con la predicción exacta dentro del gráfico
    ax_medidor.text(prediccion, 0.32, f'  {prediccion:,} Trámites\n  ({porcentaje_capacidad:.0f}% Capacidad)',
                    fontsize=12, fontweight='bold', color=color_aguja, ha='center', va='bottom',
                    bbox=dict(boxstyle='round,pad=0.4', facecolor='#ffffff', edgecolor=color_aguja, linewidth=2))

    # Línea del promedio histórico, para comparar la predicción contra "lo típico"
    ax_medidor.axvline(PROMEDIO_HISTORICO, color='#333333', linestyle=':', linewidth=2)
    ax_medidor.text(PROMEDIO_HISTORICO, -0.3, f'Promedio histórico\n{PROMEDIO_HISTORICO:.0f}',
                    fontsize=8, ha='center', va='top', color='#333333')

    # Formato del medidor (el eje se calcula una sola vez para que la aguja nunca se recorte)
    ax_medidor.set_xlim(0, XLIM_MEDIDOR)
    ax_medidor.set_ylim(-0.55, 0.7)
    ax_medidor.set_yticks([])
    ax_medidor.set_xlabel('Cantidad de Trámites Proyectados al Día', fontsize=11, fontweight='bold')
    ax_medidor.grid(True, axis='x', linestyle='--', alpha=0.5)
    ax_medidor.legend(loc='lower center', bbox_to_anchor=(0.5, 1.02), ncol=3, fontsize=8.3, frameon=False)

    # Tarjeta explicativa abajo
    ax_tarjeta.clear()
    ax_tarjeta.axis('off')

    if prediccion < ZONA_BAJA_MAX:
        estado_txt = "[!] CAPACIDAD BAJA (riesgo de demoras)"
    elif prediccion < ZONA_MEDIA_MAX:
        estado_txt = "[=] CAPACIDAD MEDIA (operación regular)"
    else:
        estado_txt = "[OK] CAPACIDAD ALTA (máximo rendimiento)"

    margen = round(MAE_MODELO)
    texto_explicativo = (
        f"PREDICCIÓN CON LA IA: {prediccion:,} TRÁMITES / DÍA\n"
        f"Estado: {estado_txt}\n"
        f"Insp.: {int(insp)}   |   Presupuesto: ${pres:,.0f}   |   Espera: {esp:.0f} min\n"
        f"Rango de confianza: entre {max(0, prediccion-margen):,} y {prediccion+margen:,} trámites al día."
    )
    
    ax_tarjeta.text(0.02, 0.5, texto_explicativo, va='center', ha='left', fontsize=9.5,
                    bbox=dict(boxstyle='round,pad=0.6', facecolor='#ffffff', edgecolor='#00529B', linewidth=1.5))
    
    fig.canvas.draw_idle()

slider_inspectores.on_changed(actualizar)
slider_presupuesto.on_changed(actualizar)
slider_espera.on_changed(actualizar)

def reset(event):
    slider_inspectores.reset()
    slider_presupuesto.reset()
    slider_espera.reset()

boton_reset.on_clicked(reset)

actualizar()

print("\nSimulador Gráfico tipo Medidor ejecutado correctamente.\n")
plt.show()
