import os
import pandas as pd
import numpy as np

# ===============================================================================
# DATASET DE HISTORIA (para que K-Means descubra los perfiles): 3 grupos generados
# con rangos enteros/uniformes "de manual operativo" (ej. frecuencia como conteo,
# estadía y trámite como rangos uniformes de referencia).
# ===============================================================================
np.random.seed(42)
TOTAL_HISTORIA = 400

num_grupo1 = int(TOTAL_HISTORIA * 0.40)  # 40% Viajeros Frecuentes / Negocios
num_grupo2 = int(TOTAL_HISTORIA * 0.45)  # 45% Turistas Estándar
num_grupo3 = TOTAL_HISTORIA - (num_grupo1 + num_grupo2)  # 15% Revisión Especial / Atípicos

# Grupo 0: Viajeros Frecuentes / Negocios
frecuencia_g0 = np.random.randint(12, 35, size=num_grupo1)
estadia_g0 = np.round(np.random.uniform(1, 5, size=num_grupo1), 1)
monto_g0 = np.round(np.random.normal(3500, 800, size=num_grupo1), 2)
tramite_g0 = np.round(np.random.uniform(2, 6, size=num_grupo1), 1)

# Grupo 1: Turistas Estándar
frecuencia_g1 = np.random.randint(1, 4, size=num_grupo2)
estadia_g1 = np.round(np.random.uniform(6, 18, size=num_grupo2), 1)
monto_g1 = np.round(np.random.normal(1800, 500, size=num_grupo2), 2)
tramite_g1 = np.round(np.random.uniform(4, 9, size=num_grupo2), 1)

# Grupo 2: Perfil Atípico / Revisión Especial
frecuencia_g2 = np.random.randint(1, 8, size=num_grupo3)
estadia_g2 = np.round(np.random.uniform(25, 90, size=num_grupo3), 1)
monto_g2 = np.round(np.random.normal(800, 400, size=num_grupo3), 2)
tramite_g2 = np.round(np.random.uniform(12, 30, size=num_grupo3), 1)

frecuencia = np.concatenate([frecuencia_g0, frecuencia_g1, frecuencia_g2])
estadia = np.concatenate([estadia_g0, estadia_g1, estadia_g2])
monto = np.maximum(500, np.concatenate([monto_g0, monto_g1, monto_g2]))
tramite = np.concatenate([tramite_g0, tramite_g1, tramite_g2])

indices = np.arange(TOTAL_HISTORIA)
np.random.shuffle(indices)

df_historia = pd.DataFrame({
    'frecuencia_viajes_ano': frecuencia[indices],
    'tiempo_estadia_dias': estadia[indices],
    'monto_declarado_usd': np.round(monto[indices], 2),
    'tiempo_tramite_min': tramite[indices]
})

# ===============================================================================
# DATASET DE EVALUACIÓN: cohorte de viajeros INDEPENDIENTE, no una porción de la
# misma tanda de historia. Se genera con una fórmula distinta a propósito:
# - distribuciones normales truncadas (variación suave y realista) en vez de
#   enteros/uniformes "de manual operativo",
# - proporciones de grupo distintas (turno con más turistas de lo habitual),
# - ruido de medición adicional en el monto declarado.
# Esto obliga a K-Means a generalizar sobre datos genuinamente nuevos, no solo a
# repetir un patrón que ya vio en el mismo lote de generación.
# ===============================================================================
np.random.seed(7)
TOTAL_EVALUACION = 100


def normal_truncada(media, desviacion, minimo, maximo, size):
    valores = np.random.normal(media, desviacion, size=size)
    return np.clip(valores, minimo, maximo)


num_eval1 = int(TOTAL_EVALUACION * 0.32)  # 32% Viajeros Frecuentes / Negocios
num_eval2 = int(TOTAL_EVALUACION * 0.53)  # 53% Turistas Estándar (cohorte con más turismo)
num_eval3 = TOTAL_EVALUACION - (num_eval1 + num_eval2)  # 15% Revisión Especial / Atípicos

# Grupo 0: Viajeros Frecuentes / Negocios
frecuencia_ev1 = np.round(normal_truncada(23, 6, 12, 38, num_eval1)).astype(int)
estadia_ev1 = np.round(normal_truncada(3, 1.3, 1, 6, num_eval1), 1)
monto_ev1 = np.round(normal_truncada(3500, 950, 500, 9000, num_eval1), 2)
tramite_ev1 = np.round(normal_truncada(4, 1.4, 1, 7, num_eval1), 1)

# Grupo 1: Turistas Estándar
frecuencia_ev2 = np.round(normal_truncada(2.3, 1.1, 1, 5, num_eval2)).astype(int)
estadia_ev2 = np.round(normal_truncada(12, 3.5, 5, 20, num_eval2), 1)
monto_ev2 = np.round(normal_truncada(1850, 550, 500, 4000, num_eval2), 2)
tramite_ev2 = np.round(normal_truncada(6.5, 1.8, 3, 10, num_eval2), 1)

# Grupo 2: Perfil Atípico / Revisión Especial
frecuencia_ev3 = np.round(normal_truncada(4.5, 2, 1, 9, num_eval3)).astype(int)
estadia_ev3 = np.round(normal_truncada(55, 17, 24, 95, num_eval3), 1)
monto_ev3 = np.round(normal_truncada(780, 380, 500, 2500, num_eval3), 2)
tramite_ev3 = np.round(normal_truncada(19, 6, 11, 32, num_eval3), 1)

frecuencia_eval = np.concatenate([frecuencia_ev1, frecuencia_ev2, frecuencia_ev3])
estadia_eval = np.concatenate([estadia_ev1, estadia_ev2, estadia_ev3])
monto_eval = np.concatenate([monto_ev1, monto_ev2, monto_ev3])
tramite_eval = np.concatenate([tramite_ev1, tramite_ev2, tramite_ev3])

# Ruido de medición adicional en el monto (p.ej. redondeos de aduana / tasas de cambio del día)
ruido_monto = np.random.normal(0, 60, size=TOTAL_EVALUACION)
monto_eval = np.maximum(500, monto_eval + ruido_monto)

indices_eval = np.arange(TOTAL_EVALUACION)
np.random.shuffle(indices_eval)

df_evaluacion = pd.DataFrame({
    'frecuencia_viajes_ano': frecuencia_eval[indices_eval],
    'tiempo_estadia_dias': estadia_eval[indices_eval],
    'monto_declarado_usd': np.round(monto_eval[indices_eval], 2),
    'tiempo_tramite_min': tramite_eval[indices_eval]
})

# Definir rutas relativas
script_dir = os.path.dirname(os.path.abspath(__file__))
dir_datos = os.path.join(script_dir, "..", "datos")
os.makedirs(dir_datos, exist_ok=True)

path_historia = os.path.join(dir_datos, "dataset_historia_clustering.csv")
path_eval = os.path.join(dir_datos, "dataset_evaluacion_clustering.csv")

# Guardar CSVs
df_historia.to_csv(path_historia, index=False)
df_evaluacion.to_csv(path_eval, index=False)
