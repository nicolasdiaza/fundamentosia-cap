# Paso 2: entrenamiento interactivo (elige algoritmo, k y escalado)

import os
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn.mixture import GaussianMixture
from sklearn.pipeline import Pipeline
from perfiles_clustering import PERFILES, mapear_clusters_a_perfiles, obtener_estimador_final, obtener_centroides

plt.rcParams['font.sans-serif'] = 'Segoe UI'


def preguntar_opcion(mensaje, opciones, por_defecto):
    print(mensaje)
    for clave, texto in opciones.items():
        print(f"  {clave}. {texto}")
    eleccion = input(f"Elige una opción [Enter = {por_defecto}]: ").strip()
    return eleccion if eleccion in opciones else por_defecto


def preguntar_numero(mensaje, por_defecto, tipo=float, minimo=None):
    texto = input(f"{mensaje} [Enter = {por_defecto}]: ").strip()
    if texto == "":
        return por_defecto
    try:
        valor = tipo(texto)
        if minimo is not None and valor < minimo:
            raise ValueError
        return valor
    except ValueError:
        print(f"  Entrada no válida, se usará el valor por defecto ({por_defecto}).")
        return por_defecto


def preguntar_si_no(mensaje, por_defecto):
    etiqueta = 's' if por_defecto else 'n'
    texto = input(f"{mensaje} (s/n) [Enter = {etiqueta}]: ").strip().lower()
    if texto == "":
        return por_defecto
    if texto in ("s", "n"):
        return texto == "s"
    print(f"  Entrada no válida, se usará el valor por defecto ({'sí' if por_defecto else 'no'}).")
    return por_defecto


print("\n" + "="*75)
print(" MÓDULO CLUSTERING - PASO 2: ENTRENAMIENTO Y NORMALIZACIÓN")
print("="*75 + "\n")

# Paso 1: rutas relativas
script_dir = os.path.dirname(os.path.abspath(__file__))
ruta_historia = os.path.join(script_dir, "..", "datos", "dataset_historia_clustering.csv")
ruta_modelo = os.path.join(script_dir, "..", "modelos", "modelo_clustering.joblib")

# Paso 2: cargar datos
df_historia = pd.read_csv(ruta_historia)

# Paso 3: configuración interactiva del entrenamiento
print("--- CONFIGURACIÓN DEL ENTRENAMIENTO ---")

opcion_algo = preguntar_opcion(
    "\n¿Qué algoritmo de clustering quieres entrenar?",
    {"1": "K-Means", "2": "MiniBatch K-Means", "3": "Gaussian Mixture (Modelos de Mezcla)"}, "1")

n_clusters = int(preguntar_numero("\n¿Cuántos grupos (clusters) quieres identificar?", 3, tipo=int, minimo=1))
if n_clusters > len(df_historia):
    print(f"  n_clusters ({n_clusters}) supera el número de registros ({len(df_historia)}); se ajusta a {len(df_historia)}.")
    n_clusters = len(df_historia)

if opcion_algo == "1":
    nombre_modelo = "K-Means"
    modelo_base = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
elif opcion_algo == "2":
    batch_size = int(preguntar_numero("  Tamaño de lote (batch_size)", 100, tipo=int, minimo=1))
    nombre_modelo = "MiniBatch K-Means"
    modelo_base = MiniBatchKMeans(n_clusters=n_clusters, random_state=42, n_init=10, batch_size=batch_size)
else:
    opcion_cov = preguntar_opcion(
        "  Tipo de covarianza",
        {"1": "full (recomendado)", "2": "tied", "3": "diag", "4": "spherical"}, "1")
    covarianza_map = {"1": "full", "2": "tied", "3": "diag", "4": "spherical"}
    nombre_modelo = "Gaussian Mixture"
    modelo_base = GaussianMixture(n_components=n_clusters, covariance_type=covarianza_map[opcion_cov], random_state=42)

usar_escalado = preguntar_si_no("\n¿Escalar variables con StandardScaler antes de entrenar?", True)

modelo_clustering = Pipeline([("escalador", StandardScaler()), ("modelo", modelo_base)]) if usar_escalado else modelo_base

print(f"\nModelo elegido: {nombre_modelo} | Grupos (k): {n_clusters} | Escalado: {'Sí' if usar_escalado else 'No'}\n")

# Paso 4: entrenar el modelo (no hay train/test split: todo df_historia se usa para descubrir perfiles)
modelo_clustering.fit(df_historia)

# Paso 5: guardar artefacto único en modelos/
os.makedirs(os.path.dirname(ruta_modelo), exist_ok=True)
joblib.dump(modelo_clustering, ruta_modelo)
print(f"Modelo guardado como 'modelo_clustering.joblib'. Entrenado con {len(df_historia)} registros.")

# Paso 6: extraer centroides reales y mapear cada cluster a su perfil
estimador_final = obtener_estimador_final(modelo_clustering)
centroides_finales = obtener_centroides(estimador_final)

escalador = modelo_clustering.named_steps.get("escalador") if hasattr(modelo_clustering, "named_steps") else None
centroides_reales = escalador.inverse_transform(centroides_finales) if escalador is not None else centroides_finales

columnas_originales = df_historia.columns
df_centroides = pd.DataFrame(centroides_reales, columns=columnas_originales)

# El ID de cluster que asignó el algoritmo es arbitrario: se recalcula el perfil real
# de cada uno a partir de sus características, nunca asumiendo un orden fijo.
mapa_cluster_a_perfil = mapear_clusters_a_perfiles(centroides_reales, columnas_originales)

# Paso 7: visualización de la tabla de centroides (el viajero promedio de cada grupo)
fig, ax_tabla = plt.subplots(figsize=(12, 5.5))
ax_tabla.axis('off')

tabla_data = []
for idx in range(len(df_centroides)):
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

fig.suptitle(f'Paso 2: Centroides Descubiertos por {nombre_modelo} (El Viajero Promedio de cada Grupo)', fontsize=14, fontweight='bold')

plt.figtext(0.5, 0.02,
            "[EXPLICACIÓN DE ESTE PASO]:\n"
            "• StandardScaler (si se activó) emparejó las variables para que los miles de dólares no opacaran a los viajes simples.\n"
            f"• {nombre_modelo} encontró de forma 100% automática estos {len(df_centroides)} perfiles analizando distancias numéricas.\n"
            "• El número 'Grupo #' es solo una etiqueta interna del algoritmo (puede cambiar si se re-entrena); el PERFIL es lo que importa.\n"
            "• Con k distinto de 3, es normal que dos grupos compartan el mismo nombre de perfil si sus características son similares.\n"
            "Siguiente paso -> ejecutar 'paso3_evaluacion_clustering.py'",
            ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8f9fa', edgecolor='#cccccc'))

fig.tight_layout(rect=[0, 0.16, 1, 0.93])

plt.show()
