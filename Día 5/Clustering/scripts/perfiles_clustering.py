"""
===============================================================================
MÓDULO DE CLUSTERING - DEFINICIONES COMPARTIDAS DE PERFILES
Capacitación de IA - Servicio Nacional de Migración de Panamá (Día 5)
===============================================================================
El ID de cluster que asigna K-Means (0, 1, 2) es arbitrario: depende de cómo se
inicializa el algoritmo y NO representa un orden fijo ("Cluster 0" no siempre es
el mismo perfil). Este módulo traduce cada centroide entrenado a su perfil real
observando sus características, para que Pasos 2, 3 y 4 muestren siempre el
mismo nombre, color y recomendación sin importar qué ID interno le tocó a cada
grupo en esa ejecución.
===============================================================================
"""

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
