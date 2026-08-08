"""
===============================================================================
MÓDULO DE CLUSTERING - PASO 2: ENTRENAMIENTO K-MEANS Y NORMALIZACIÓN
Capacitación de IA - Servicio Nacional de Migración de Panamá (Día 5)
===============================================================================
OBJETIVO:
1. Normalizar las variables numéricas con StandardScaler (para que los dólares de 5000 USD
   no dominen sobre la frecuencia de 5 viajes al calcular distancias).
2. Entrenar el algoritmo K-Means con k=3 grupos.
3. Extraer e interpretar los Centroides (El Viajero Promedio de cada grupo).
4. Guardar los modelos 'modelo_kmeans.joblib' y 'escalador_scaler.joblib'.
===============================================================================
"""

import os
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from perfiles_clustering import PERFILES, mapear_clusters_a_perfiles

plt.rcParams['font.sans-serif'] = 'Segoe UI'

# 1. Rutas relativas
script_dir = os.path.dirname(os.path.abspath(__file__))
ruta_historia = os.path.join(script_dir, "..", "datos", "dataset_historia_clustering.csv")
ruta_kmeans = os.path.join(script_dir, "..", "modelos", "modelo_kmeans.joblib")
ruta_scaler = os.path.join(script_dir, "..", "modelos", "escalador_scaler.joblib")

# 2. Cargar datos
df_historia = pd.read_csv(ruta_historia)

# 3. Normalizar variables con StandardScaler (Imprescindible para K-Means)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_historia)

# 4. Entrenar K-Means con k=3 grupos
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X_scaled)

# Asignar la columna 'cluster' al dataframe
df_historia['cluster'] = kmeans.labels_

# 5. Guardar artefactos en la carpeta modelos/
os.makedirs(os.path.dirname(ruta_kmeans), exist_ok=True)
joblib.dump(kmeans, ruta_kmeans)
joblib.dump(scaler, ruta_scaler)

# 6. Extraer los Centroides Reales (Des-escalados a las unidades originales)
centroides_escalados = kmeans.cluster_centers_
centroides_reales = scaler.inverse_transform(centroides_escalados)

columnas_originales = df_historia.columns[:-1]
df_centroides = pd.DataFrame(centroides_reales, columns=columnas_originales)

# El ID de cluster (0,1,2) que asignó K-Means es arbitrario: se recalcula el perfil real
# de cada uno a partir de sus características, nunca asumiendo un orden fijo.
mapa_cluster_a_perfil = mapear_clusters_a_perfiles(centroides_reales, columnas_originales)

# 7. Visualización Gráfica: Resumen de Centroides (El viajero promedio de cada perfil)
fig, ax_tabla = plt.subplots(figsize=(12, 5.5))
ax_tabla.axis('off')

# Formatear la tabla para mostrar en pantalla
tabla_data = []
for idx in range(3):
    c = df_centroides.iloc[idx]
    perfil = PERFILES[mapa_cluster_a_perfil[idx]]
    tabla_data.append([
        f"Grupo #{idx}: {perfil['nombre']}",
        f"{c['frecuencia_viajes_ano']:.1f} viajes/año",
        f"{c['tiempo_estadia_dias']:.1f} días",
        f"${c['monto_declarado_usd']:,.0f} USD",
        f"{c['tiempo_tramite_min']:.1f} min"
    ])

columnas_headers = ['Perfil Descubierto por IA (Cluster)', 'Frecuencia Viajes', 'Tiempo Estadía', 'Monto Declarado', 'Tiempo Trámite']

tabla = ax_tabla.table(cellText=tabla_data, colLabels=columnas_headers, loc='center', cellLoc='center',
                        colWidths=[0.34, 0.16, 0.16, 0.17, 0.17])
tabla.auto_set_font_size(False)
tabla.set_fontsize(10.5)
tabla.scale(1.2, 2.2)

# Estilar cabecera y colorear cada fila según el perfil real (no la posición de la fila)
for (row, col), cell in tabla.get_celld().items():
    if row == 0:
        cell.set_facecolor('#00529B')
        cell.get_text().set_color('white')
        cell.get_text().set_weight('bold')
    else:
        idx = row - 1
        perfil = PERFILES[mapa_cluster_a_perfil[idx]]
        cell.set_facecolor(perfil['color_fondo'])

fig.suptitle('Paso 2: Centroides Descubiertos por K-Means (El Viajero Promedio de cada Grupo)', fontsize=14, fontweight='bold')

plt.figtext(0.5, 0.02,
            "[EXPLICACIÓN DE ESTE PASO]:\n"
            "• StandardScaler emparejó las variables para que los miles de dólares no opacaran a los viajes simples.\n"
            "• K-Means encontró de forma 100% automática estos 3 perfiles de viajeros analizando distancias numéricas.\n"
            "• El número 'Grupo #' es solo una etiqueta interna del algoritmo (puede cambiar si se re-entrena); el PERFIL es lo que importa.\n"
            "Siguiente paso -> ejecutar 'paso3_evaluacion_clustering.py'",
            ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8f9fa', edgecolor='#cccccc'))

fig.tight_layout(rect=[0, 0.16, 1, 0.93])

plt.show()
