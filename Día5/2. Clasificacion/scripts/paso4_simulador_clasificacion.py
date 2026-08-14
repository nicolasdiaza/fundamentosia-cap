# Paso 4: simulador visual (semáforo de alertas) con el modelo entrenado

import os
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

plt.rcParams['font.sans-serif'] = 'Segoe UI'
plt.rcParams['axes.edgecolor'] = '#cccccc'

# Paso 1: cargar modelo y datos históricos
script_dir = os.path.dirname(os.path.abspath(__file__))
ruta_modelo = os.path.join(script_dir, "..", "modelos", "modelo_clasificacion.joblib")
ruta_historia = os.path.join(script_dir, "..", "datos", "dataset_historia_clasificacion.csv")

try:
    modelo_clasificacion = joblib.load(ruta_modelo)
    df_historia = pd.read_csv(ruta_historia)
except Exception as e:
    print(f"Error cargando modelo o dataset: {e}")
    exit()

# Paso 2: crear ventana principal
fig = plt.figure(figsize=(12, 8.5), facecolor='#f4f6f9')
fig.canvas.manager.set_window_title('Migración Panamá - Sistema de Alerta Temprana de Congestión')

# Encabezado Principal
plt.suptitle('Sistema de Alerta Temprana de Congestión Migratoria (IA)', 
             fontsize=15, fontweight='bold', color='#003366', y=0.96)

fig.text(0.5, 0.92, 
         'Ajusta las condiciones del turno en el panel izquierdo para evaluar el nivel de riesgo en tiempo real.',
         ha='center', fontsize=10.5, color='#444444')

# Paso 3: definir áreas de la interfaz
ax_semaforo = fig.add_axes([0.48, 0.26, 0.47, 0.60])
ax_tarjeta = fig.add_axes([0.48, 0.04, 0.47, 0.18])
ax_tarjeta.axis('off')

# Valores iniciales (Promedios)
init_pasajeros = int(df_historia['pasajeros_proyectados'].mean())
init_vuelos = int(df_historia['vuelos_simultaneos'].mean())
init_inspectores = int(df_historia['inspectores_disponibles'].mean())
init_escaneo = float(df_historia['porcentaje_escaneo'].mean())

# Paso 4: crear sliders/palancas
ax_s1 = fig.add_axes([0.08, 0.74, 0.32, 0.035], facecolor='#e6ecf5')
ax_s2 = fig.add_axes([0.08, 0.58, 0.32, 0.035], facecolor='#e6ecf5')
ax_s3 = fig.add_axes([0.08, 0.42, 0.32, 0.035], facecolor='#e6ecf5')
ax_s4 = fig.add_axes([0.08, 0.26, 0.32, 0.035], facecolor='#e6ecf5')

slider_pasajeros = Slider(ax_s1, '', 500, 3500, valinit=init_pasajeros, valstep=50, color='#00529B')
slider_vuelos = Slider(ax_s2, '', 2, 18, valinit=init_vuelos, valstep=1, color='#7B1FA2')
slider_inspectores = Slider(ax_s3, '', 5, 35, valinit=init_inspectores, valstep=1, color='#2E7D32')
slider_escaneo = Slider(ax_s4, '', 10, 90, valinit=init_escaneo, valstep=5, color='#D9381E')

# Etiquetas claras sobre los controles
fig.text(0.08, 0.79, 'Pasajeros Proyectados en Turno', fontsize=10.5, fontweight='bold', color='#00529B')
fig.text(0.08, 0.77, '(Volumen total de personas llegando a la terminal)', fontsize=8.5, color='#555555')

fig.text(0.08, 0.63, 'Vuelos Simultáneos', fontsize=10.5, fontweight='bold', color='#7B1FA2')
fig.text(0.08, 0.61, '(Cantidad de aviones desembarcando al mismo tiempo)', fontsize=8.5, color='#555555')

fig.text(0.08, 0.47, 'Inspectores Disponibles', fontsize=10.5, fontweight='bold', color='#2E7D32')
fig.text(0.08, 0.45, '(Ventanillas activas de control de entrada)', fontsize=8.5, color='#555555')

fig.text(0.08, 0.31, '% Equipaje Escaneado', fontsize=10.5, fontweight='bold', color='#D9381E')
fig.text(0.08, 0.29, '(Porcentaje de revisiones aduaneras/seguridad secundarias)', fontsize=8.5, color='#555555')

# Botón Reset
ax_boton = fig.add_axes([0.08, 0.10, 0.102, 0.05])
boton_reset = Button(ax_boton, 'Valores Promedio', color='#ffffff', hovercolor='#e2e8f0')
boton_reset.label.set_fontsize(8.5)

# Botones de Escenarios Preestablecidos (para explorar casos reales sin tocar sliders)
fig.text(0.08, 0.17, 'Escenarios Rápidos:', fontsize=9.5, fontweight='bold', color='#333333')

ax_esc1 = fig.add_axes([0.194, 0.10, 0.102, 0.05])
boton_tranquilo = Button(ax_esc1, 'Turno Tranquilo', color='#e8f5e9', hovercolor='#c8e6c9')
boton_tranquilo.label.set_fontsize(8.5)

ax_esc2 = fig.add_axes([0.308, 0.10, 0.102, 0.05])
boton_critico = Button(ax_esc2, 'Turno Crítico', color='#ffebee', hovercolor='#ffcdd2')
boton_critico.label.set_fontsize(8.5)

# Paso 5: función de actualización del semáforo y la predicción
def actualizar(val=None):
    pas = slider_pasajeros.val
    vue = slider_vuelos.val
    insp = slider_inspectores.val
    esc = slider_escaneo.val
    
    df_input = pd.DataFrame({
        'pasajeros_proyectados': [pas],
        'vuelos_simultaneos': [vue],
        'inspectores_disponibles': [insp],
        'porcentaje_escaneo': [esc]
    })
    
    # UMBRAL DE DECISIÓN: si la probabilidad supera 50%, el modelo predice Alerta (1).
    # Este mismo corte se explicó en el Paso 2 al pasar de Regresión Logística a decisión binaria.
    UMBRAL_DECISION = 50.0
    ZONA_INCERTIDUMBRE = 8.0  # +/- puntos alrededor del umbral considerados "zona gris"

    # Predecir probabilidad y derivar la clase del mismo umbral (evita que color y % se contradigan,
    # lo cual puede pasar si se compara .predict() con .predict_proba() por separado en algunos modelos)
    prob_congestion = modelo_clasificacion.predict_proba(df_input)[0][1] * 100
    pred_clase = 1 if prob_congestion >= UMBRAL_DECISION else 0
    en_zona_incertidumbre = abs(prob_congestion - UMBRAL_DECISION) <= ZONA_INCERTIDUMBRE

    # Limpiar panel
    ax_semaforo.clear()
    ax_semaforo.axis('off')

    # Dibujar Semáforo Visual
    if pred_clase == 1:
        color_fondo = '#ffebee'
        color_borde = '#d32f2f'
        titulo_estado = "ALERTA ROJA: RIESGO DE CONGESTIÓN MIGRATORIA"
        sub_estado = "Demanda supera la capacidad de atención en ventanillas."
        circulo_color = '#d32f2f'
    else:
        color_fondo = '#e8f5e9'
        color_borde = '#2e7d32'
        titulo_estado = "ESTADO VERDE: OPERACIÓN NORMAL"
        sub_estado = "Flujo de pasajeros dentro de la capacidad disponible."
        circulo_color = '#2e7d32'

    if en_zona_incertidumbre:
        color_borde = '#e6a700'
        circulo_color = '#e6a700'

    # Dibujar recuadro semafórico central usando FancyBboxPatch (bordes redondeados compatibles)
    from matplotlib.patches import FancyBboxPatch
    patch_semaforo = FancyBboxPatch((0.05, 0.1), 0.9, 0.8, boxstyle="round,pad=0.03,rounding_size=0.05",
                                     facecolor=color_fondo, edgecolor=color_borde, linewidth=3)
    ax_semaforo.add_patch(patch_semaforo)

    # Círculo semáforo
    ax_semaforo.plot(0.5, 0.65, marker='o', markersize=45, color=circulo_color)

    # Texto de Probabilidad + Umbral de decisión explícito
    ax_semaforo.text(0.5, 0.44, f'Probabilidad de Sobrecarga: {prob_congestion:.1f}%',
                     ha='center', va='center', fontsize=14, fontweight='bold', color=color_borde)
    ax_semaforo.text(0.5, 0.37, f'(Umbral de decisión de la IA: {UMBRAL_DECISION:.0f}%)',
                     ha='center', va='center', fontsize=9, color='#666666', style='italic')

    if en_zona_incertidumbre:
        ax_semaforo.text(0.5, 0.30, "ZONA DE INCERTIDUMBRE: valor muy cerca del umbral.\nConsidere reforzar personal por precaución.",
                         ha='center', va='center', fontsize=9, fontweight='bold', color='#8a6d00')
        titulo_estado = titulo_estado.replace("ALERTA ROJA", "ZONA GRIS (cercana a Alerta)").replace("ESTADO VERDE", "ZONA GRIS (cercana a Alerta)")

    ax_semaforo.text(0.5, 0.20, titulo_estado, ha='center', va='center', fontsize=11, fontweight='bold', color='#111111')
    ax_semaforo.text(0.5, 0.13, sub_estado, ha='center', va='center', fontsize=9, color='#444444')

    ax_semaforo.set_xlim(0, 1)
    ax_semaforo.set_ylim(0, 1)
    
    # Tarjeta explicativa e instrucciones operativas
    ax_tarjeta.clear()
    ax_tarjeta.axis('off')
    
    if pred_clase == 1:
        accion_recomendada = f"RECOMENDACIÓN IA: Habilitar {max(2, int((pas - insp*100)/100))} inspectores adicionales o reducir temporalmente % de escaneo."
    else:
        accion_recomendada = "RECOMENDACIÓN IA: Mantener la dotación actual de personal en el turno."
        
    texto_explicativo = (
        f"DIAGNÓSTICO DEL SISTEMA DE IA:\n"
        f"{accion_recomendada}\n"
        f"Con {int(pas)} pasajeros y {int(vue)} vuelos simultáneos, se requieren al menos {int(np.ceil(pas/105))} inspectores.\n"
        f"Actualmente tienes {int(insp)} inspectores asignados."
    )
    
    ax_tarjeta.text(0.02, 0.5, texto_explicativo, va='center', ha='left', fontsize=9.5,
                    bbox=dict(boxstyle='round,pad=0.6', facecolor='#ffffff', edgecolor='#00529B', linewidth=1.5))
    
    fig.canvas.draw_idle()

slider_pasajeros.on_changed(actualizar)
slider_vuelos.on_changed(actualizar)
slider_inspectores.on_changed(actualizar)
slider_escaneo.on_changed(actualizar)

def reset(event):
    slider_pasajeros.reset()
    slider_vuelos.reset()
    slider_inspectores.reset()
    slider_escaneo.reset()

def escenario_tranquilo(event):
    # Turno con baja demanda y buena dotación de personal: debería salir Verde con margen amplio.
    slider_pasajeros.set_val(900)
    slider_vuelos.set_val(3)
    slider_inspectores.set_val(25)
    slider_escaneo.set_val(30)

def escenario_critico(event):
    # Alta demanda, muchos vuelos simultáneos y poco personal: debería salir Rojo con margen amplio.
    slider_pasajeros.set_val(3200)
    slider_vuelos.set_val(15)
    slider_inspectores.set_val(8)
    slider_escaneo.set_val(75)

boton_reset.on_clicked(reset)
boton_tranquilo.on_clicked(escenario_tranquilo)
boton_critico.on_clicked(escenario_critico)

actualizar()

plt.show()
