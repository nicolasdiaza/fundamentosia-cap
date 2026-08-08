"""
===============================================================================
MÓDULO DE CLASIFICACIÓN - PASO 1: CARGA Y EXPLORACIÓN DE DATOS (EDA)
Capacitación de IA - Servicio Nacional de Migración de Panamá (Día 5)
===============================================================================
OBJETIVO:
Cargar el dataset de historia en .csv, analizar las variables predictoras y 
comprender el balance de la variable objetivo binaria (Operación Normal vs Alerta).
===============================================================================
"""

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'Segoe UI'

print("\n" + "="*75)
print(" MÓDULO CLASIFICACIÓN - PASO 1: EXPLORACIÓN DE DATOS DE HISTORIA (.CSV)")
print(" (El detalle completo se muestra en la ventana gráfica)")
print("="*75 + "\n")

# 1. Ruta relativa al dataset
script_dir = os.path.dirname(os.path.abspath(__file__))
ruta_historia = os.path.join(script_dir, "..", "datos", "dataset_historia_clasificacion.csv")

df_historia = pd.read_csv(ruta_historia)

# Análisis del Balance de Clases (Target Binario)
conteo_alertas = df_historia['alerta_congestion'].value_counts()
pct_normal = (conteo_alertas.get(0, 0) / len(df_historia)) * 100
pct_alerta = (conteo_alertas.get(1, 0) / len(df_historia)) * 100

# Modelo "ingenuo": predecir siempre la clase mayoritaria, sin usar IA
pct_mayoritaria = max(pct_normal, pct_alerta)

# 5. Visualización Gráfica: Ficha Técnica, Distribución del Target y Matriz de Correlación
fig, (ax_ficha, ax_barras, ax_corr) = plt.subplots(1, 3, figsize=(16.5, 6), gridspec_kw={'width_ratios': [0.85, 1, 1.25]})

# Panel 0: Ficha Técnica estructurada del Dataset
ax_ficha.axis('off')
ficha_texto = (
    f"FICHA TÉCNICA DEL DATASET\n"
    f"------------------------------\n"
    f"Registros históricos: {len(df_historia)} días\n"
    f"Variables predictoras: {df_historia.shape[1] - 1}\n\n"
    f"Pasajeros/turno:\n"
    f"  Min: {df_historia['pasajeros_proyectados'].min():.0f} | Max: {df_historia['pasajeros_proyectados'].max():.0f}\n"
    f"  Promedio: {df_historia['pasajeros_proyectados'].mean():.0f}\n\n"
    f"Vuelos simultáneos:\n"
    f"  Min: {df_historia['vuelos_simultaneos'].min():.0f} | Max: {df_historia['vuelos_simultaneos'].max():.0f}\n"
    f"  Promedio: {df_historia['vuelos_simultaneos'].mean():.1f}\n\n"
    f"Inspectores disponibles:\n"
    f"  Min: {df_historia['inspectores_disponibles'].min():.0f} | Max: {df_historia['inspectores_disponibles'].max():.0f}\n"
    f"  Promedio: {df_historia['inspectores_disponibles'].mean():.1f}\n\n"
    f"% Equipaje escaneado:\n"
    f"  Min: {df_historia['porcentaje_escaneo'].min():.0f}% | Max: {df_historia['porcentaje_escaneo'].max():.0f}%\n"
    f"  Promedio: {df_historia['porcentaje_escaneo'].mean():.1f}%"
)
ax_ficha.text(0.02, 0.98, ficha_texto, va='top', ha='left', fontsize=9.5, family='monospace',
              bbox=dict(boxstyle='round,pad=0.6', facecolor='#f8f9fa', edgecolor='#00529B', linewidth=1.5))

# Gráfico 1: Conteo del Target (Normal vs Alerta)
etiquetas = ['Operación Normal (0)', 'Alerta Congestión (1)']
valores = [conteo_alertas.get(0, 0), conteo_alertas.get(1, 0)]
colores = ['#2E7D32', '#D9381E']

barras = ax_barras.bar(etiquetas, valores, color=colores, width=0.45)
for barra, val in zip(barras, valores):
    ax_barras.text(barra.get_x() + barra.get_width()/2, barra.get_height() + max(valores)*0.03,
                   f'{val} días\n({val/len(df_historia)*100:.1f}%)', ha='center', fontsize=10.5, fontweight='bold')

# Línea de referencia del modelo tonto sin IA
linea_mayoritaria = max(valores)
ax_barras.axhline(linea_mayoritaria, color='#555555', linestyle='--', linewidth=1.3)
ax_barras.text(0.5, linea_mayoritaria + max(valores)*0.04, f'Referencia sin IA: {pct_mayoritaria:.0f}% aciertos si siempre adivinamos "Normal"',
               ha='center', va='bottom', fontsize=8.5, color='#444444', style='italic')

ax_barras.set_title('Proporción de Días en la Historia', fontsize=12.5, fontweight='bold', pad=15)
ax_barras.set_ylabel('Cantidad de Días', fontsize=11)
ax_barras.set_ylim(0, max(valores) * 1.3)
ax_barras.tick_params(axis='both', labelsize=10)

# Gráfico 2: Matriz de Correlación
df_corr = df_historia.rename(columns={
    'pasajeros_proyectados': 'Pasajeros',
    'vuelos_simultaneos': 'Vuelos',
    'inspectores_disponibles': 'Inspectores',
    'porcentaje_escaneo': '% Escaneo',
    'alerta_congestion': 'Alerta (Target)'
}).corr()

sns.heatmap(df_corr, annot=True, cmap='YlOrRd', fmt=".2f", linewidths=1.2, ax=ax_corr,
            annot_kws={"size": 10.5, "weight": "bold"}, cbar_kws={'label': 'Intensidad de Relación'})

ax_corr.set_title('Relación de Variables con el Riesgo', fontsize=12.5, fontweight='bold', pad=15)
ax_corr.tick_params(axis='x', labelsize=10, rotation=15)
ax_corr.tick_params(axis='y', labelsize=10, rotation=0)

fig.suptitle('Paso 1: Análisis Exploratorio de Datos (Clasificación Migratoria)', fontsize=14.5, fontweight='bold')

plt.figtext(0.5, 0.02,
            "Guía de lectura de este paso:\n"
            "Panel 1 (Ficha): resumen numérico de la operación.  Panel 2: verificación de clases y comparación sin IA.\n"
            "Panel 3: correlación directa (rojo más intenso = mayor impacto en el riesgo de congestión).",
            ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8f9fa', edgecolor='#cccccc'))

fig.tight_layout(rect=[0, 0.14, 1, 0.94])

plt.show()

print("¡PASO 1 COMPLETADO! Listo para ejecutar 'paso2_entrenamiento_clasificacion.py'.\n")
