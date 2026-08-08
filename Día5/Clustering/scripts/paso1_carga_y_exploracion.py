"""
===============================================================================
MÓDULO DE CLUSTERING - PASO 1: CARGA Y EXPLORACIÓN DE DATOS (EDA)
Capacitación de IA - Servicio Nacional de Migración de Panamá (Día 5)
===============================================================================
OBJETIVO:
Cargar el dataset de viajeros en .csv y explorar las características de la población
ANTES de aplicar ningún algoritmo. Explicar por qué este problema NO TIENE ETIQUETA
(Aprendizaje No Supervisado).
===============================================================================
"""

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'Segoe UI'

# 1. Ruta relativa al dataset
script_dir = os.path.dirname(os.path.abspath(__file__))
ruta_historia = os.path.join(script_dir, "..", "datos", "dataset_historia_clustering.csv")

df_historia = pd.read_csv(ruta_historia)

# 2. Visualización Gráfica: Ficha Técnica + Diagramas de Dispersión
fig, (ax_ficha, ax_scatter) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [0.85, 1.25]})

# Panel 0: Ficha Técnica estructurada del Dataset sin etiquetas
ax_ficha.axis('off')
ficha_texto = (
    f"FICHA TÉCNICA (APRENDIZAJE NO SUPERVISADO)\n"
    f"────────────────────────────────────────────\n"
    f"Registros de viajeros: {len(df_historia)} personas\n"
    f"Variables de perfilamiento: {df_historia.shape[1]}\n"
    f"Etiquetas o clases previas: 0 (¡NINGUNA!)\n\n"
    f"Frecuencia viajes/año: {df_historia['frecuencia_viajes_ano'].min():.0f} - {df_historia['frecuencia_viajes_ano'].max():.0f}\n"
    f"  (promedio {df_historia['frecuencia_viajes_ano'].mean():.1f} viajes)\n\n"
    f"Tiempo de estadía: {df_historia['tiempo_estadia_dias'].min():.0f} - {df_historia['tiempo_estadia_dias'].max():.0f} días\n"
    f"  (promedio {df_historia['tiempo_estadia_dias'].mean():.1f} días)\n\n"
    f"Monto declarado: ${df_historia['monto_declarado_usd'].min():,.0f} - ${df_historia['monto_declarado_usd'].max():,.0f}\n"
    f"  (promedio ${df_historia['monto_declarado_usd'].mean():,.0f})\n\n"
    f"Tiempo de trámite: {df_historia['tiempo_tramite_min'].min():.1f} - {df_historia['tiempo_tramite_min'].max():.1f} min\n"
    f"  (promedio {df_historia['tiempo_tramite_min'].mean():.1f} min)"
)
ax_ficha.text(0.02, 0.98, ficha_texto, va='top', ha='left', fontsize=9.5, family='monospace',
              bbox=dict(boxstyle='round,pad=0.6', facecolor='#f8f9fa', edgecolor='#7B1FA2', linewidth=1.5))

# Gráfico de Dispersión sin agrupar (Todos los puntos del mismo color gris)
ax_scatter.scatter(df_historia['frecuencia_viajes_ano'], df_historia['tiempo_estadia_dias'], 
                   color='#666666', alpha=0.7, edgecolors='black', s=55)

ax_scatter.set_title('Datos de Viajeros SIN Clasificar (Puntos Grises)', fontsize=12.5, fontweight='bold', pad=15)
ax_scatter.set_xlabel('Frecuencia de Viajes al Año', fontsize=11, fontweight='bold')
ax_scatter.set_ylabel('Tiempo de Estadía (Días)', fontsize=11, fontweight='bold')
ax_scatter.grid(True, linestyle='--', alpha=0.5)

fig.suptitle('Paso 1: Exploración de Datos sin Etiquetar (Clustering Migratorio)', fontsize=14.5, fontweight='bold')

plt.figtext(0.5, 0.02,
            "[GUÍA DE LECTURA DE ESTE PASO]:\n"
            "• A diferencia del Módulo 1 y 2, aquí NO HAY una columna con la respuesta correcta (Target).\n"
            "• Todos los puntos se ven grises e iguales. El objetivo de la IA (K-Means) será encontrar los patrones y grupos ocultos.\n"
            "Siguiente paso -> ejecutar 'paso2_entrenamiento_clustering.py'",
            ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8f9fa', edgecolor='#cccccc'))

fig.tight_layout(rect=[0, 0.14, 1, 0.94])

plt.show()
