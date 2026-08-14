# Definiciones compartidas de perfiles de clustering.
# El ID de cluster que asigna el algoritmo (0, 1, 2, ...) es arbitrario: no representa
# un orden fijo. Este módulo traduce cada centroide a su perfil real observando sus
# características, para que Pasos 2, 3 y 4 muestren siempre el mismo nombre y color
# sin importar qué ID interno le tocó a cada grupo en esa ejecución, ni cuántos grupos haya.

import pandas as pd

PERFILES = {
    'frecuente': {
        'nombre': 'Viajero Frecuente / Negocios',
        'color': '#2a78d6',
        'color_fondo': '#eef4fb',
        'descripcion': 'Viajes constantes al año, estadía corta, trámite muy rápido.',
        'recomendacion': '[OK] ATENCIÓN RÁPIDA / Carril de atención preferencial.',
    },
    'turista': {
        'nombre': 'Turista Estándar',
        'color': '#2E7D32',
        'color_fondo': '#e8f5e9',
        'descripcion': 'Viajes ocasionales, estadía de vacaciones (1-2 semanas), monto típico.',
        'recomendacion': '[OK] PROCESO ESTÁNDAR / Registro de estadía regular.',
    },
    'atipico': {
        'nombre': 'Perfil Atípico / Revisión Especial',
        'color': '#D9381E',
        'color_fondo': '#ffebee',
        'descripcion': 'Estadía prolongada o tiempo de trámite inusualmente elevado.',
        'recomendacion': '[!] REVISIÓN SECUNDARIA / Verificar hospedaje o fondos.',
    },
}


def identificar_tipo_perfil(centroide):
    """Clasifica un centroide (con frecuencia_viajes_ano y tiempo_estadia_dias) en una clave de PERFILES."""
    if centroide['tiempo_estadia_dias'] > 20:
        return 'atipico'
    elif centroide['frecuencia_viajes_ano'] > 10:
        return 'frecuente'
    else:
        return 'turista'


def mapear_clusters_a_perfiles(centroides_reales, columnas):
    """Dado el array de centroides des-escalados y los nombres de columnas originales,
    devuelve {cluster_id: tipo_perfil} calculado por características, nunca por posición fija."""
    df_centroides = pd.DataFrame(centroides_reales, columns=columnas)
    return {idx: identificar_tipo_perfil(row) for idx, row in df_centroides.iterrows()}


def obtener_estimador_final(modelo):
    # Si es un Pipeline devuelve el último paso (el estimador real); si no, el modelo tal cual
    if hasattr(modelo, "named_steps"):
        return list(modelo.named_steps.values())[-1]
    return modelo


def obtener_centroides(estimador):
    # KMeans/MiniBatchKMeans exponen cluster_centers_; GaussianMixture expone means_
    return estimador.cluster_centers_ if hasattr(estimador, "cluster_centers_") else estimador.means_
