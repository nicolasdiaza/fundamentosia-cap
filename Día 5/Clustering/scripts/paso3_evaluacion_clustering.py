"""
===============================================================================
MÓDULO DE CLUSTERING - PASO 3: VISUALIZACIÓN DE CLUSTERS Y CENTROIDES
Capacitación de IA - Servicio Nacional de Migración de Panamá (Día 5)
===============================================================================
OBJETIVO:
Visualizar en 2D la segmentación realizada por K-Means sobre el dataset de
evaluación independiente 'dataset_evaluacion_clustering.csv'.
===============================================================================
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import joblib
from perfiles_clustering import PERFILES, mapear_clusters_a_perfiles

plt.rcParams['font.sans-serif'] = 'Segoe UI'

# 1. Rutas relativas
script_dir = os.path.dirname(os.path.abspath(__file__))
ruta_eval = os.path.join(script_dir, "..", "datos", "dataset_evaluacion_clustering.csv")
ruta_kmeans = os.path.join(script_dir, "..", "modelos", "modelo_kmeans.joblib")
ruta_scaler = os.path.join(script_dir, "..", "modelos", "escalador_scaler.joblib")

# 2. Cargar modelos y datos de evaluación
kmeans = joblib.load(ruta_kmeans)
scaler = joblib.load(ruta_scaler)
df_eval = pd.read_csv(ruta_eval)

# 3. Asignar clusters a los datos nuevos que la IA nunca vio
X_scaled_eval = scaler.transform(df_eval)
df_eval['cluster'] = kmeans.predict(X_scaled_eval)

# 4. Extraer centroides en escala original
columnas_originales = [c for c in df_eval.columns if c != 'cluster']
centroides_reales = scaler.inverse_transform(kmeans.cluster_centers_)

# El ID de cluster (0,1,2) es arbitrario: se recalcula el perfil real de cada uno
# a partir de sus características, igual que en Paso 2, para que nombres y colores
# nunca queden desincronizados del algoritmo.
mapa_cluster_a_perfil = mapear_clusters_a_perfiles(centroides_reales, columnas_originales)

# 5. Visualización Gráfica en 2D: Mapa de Grupos de Viajeros
fig, ax = plt.subplots(figsize=(11, 6.5))

for c_id in range(3):
    perfil = PERFILES[mapa_cluster_a_perfil[c_id]]
    sub = df_eval[df_eval['cluster'] == c_id]
    ax.scatter(sub['frecuencia_viajes_ano'], sub['tiempo_estadia_dias'],
               color=perfil['color'], alpha=0.75, s=65, edgecolors='black',
               label=f"Grupo #{c_id}: {perfil['nombre']}")

# Dibujar Centroides de cada grupo (Marcador 'X' grande o estrella)
for c_id in range(3):
    c_x = centroides_reales[c_id, 0] # frecuencia
    c_y = centroides_reales[c_id, 1] # estadía
    ax.scatter(c_x, c_y, color='black', marker='X', s=250, linewidths=2.5, zorder=10)
    ax.text(c_x, c_y + 2.5, f'Centroide {c_id}', fontsize=10, fontweight='bold', ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#ffffff', edgecolor='black', alpha=0.85))

ax.set_title('Paso 3: Segmentación de Viajeros en 2D (K-Means en Datos Nuevos)', fontsize=13, fontweight='bold', pad=15)
ax.set_xlabel('Frecuencia de Viajes al Año', fontsize=11, fontweight='bold')
ax.set_ylabel('Tiempo de Estadía (Días)', fontsize=11, fontweight='bold')
ax.legend(fontsize=10, loc='upper right')
ax.grid(True, linestyle='--', alpha=0.5)

plt.figtext(0.5, 0.02,
            "[CÓMO INTERPRETAR LA GRÁFICA DE CLUSTERS]:\n"
            "• Cada punto coloreado representa a 1 pasajero evaluado por la IA en datos independientes.\n"
            "• Las marcas 'X' negras son los CENTROIDES (el centro de gravedad / pasajero promedio de cada perfil).\n"
            "• K-Means asigna automáticamente a cada viajero el grupo del centroide que le queda más cerca.\n"
            "• Este mapa solo muestra 2 de las 4 variables usadas para agrupar: puede haber puntos que se vean cerca\n"
            "  aquí pero pertenezcan a grupos distintos por diferencias en monto declarado o tiempo de trámite.\n"
            "Siguiente paso -> ejecutar 'paso4_simulador_clustering.py'",
            ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8f9fa', edgecolor='#cccccc'))

fig.tight_layout(rect=[0, 0.18, 1, 0.95])

plt.show()
