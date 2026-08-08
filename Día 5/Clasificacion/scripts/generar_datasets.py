import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Semilla para reproducibilidad
np.random.seed(42)
TOTAL_REGISTROS = 500
PORCENTAJE_EVALUACION = 0.20 # 20% para evaluación final independiente (out-of-sample)

# 1. Generar variables predictoras realistas para un Puesto Migratorio
pasajeros = np.random.randint(500, 3500, size=TOTAL_REGISTROS)
vuelos_simultaneos = np.random.randint(2, 18, size=TOTAL_REGISTROS)
inspectores_disponibles = np.random.randint(5, 35, size=TOTAL_REGISTROS)
porcentaje_escaneo = np.round(np.random.uniform(10, 90, size=TOTAL_REGISTROS), 1)

# 2. Generar Regla Operativa de Congestión con Ruido Realista
# Capacidad relativa por inspector: aprox 105 pasajeros por turno
# COLCHON_OPERATIVO: margen de infraestructura (pasillos, personal de apoyo) que
# hace que, en la mayoría de los turnos, el puesto opere de forma Normal.
# Esto refleja la realidad: la Alerta de Congestión es el evento MINORITARIO, no la norma.
COLCHON_OPERATIVO = 1400
capacidad_atencion = inspectores_disponibles * 105 - (vuelos_simultaneos * 40) - (porcentaje_escaneo * 5) + COLCHON_OPERATIVO
diferencia_demanda = pasajeros - capacidad_atencion

# Regla de Clasificación Binaria:
# 0 = Operación Normal (Capacidad suficiente)
# 1 = Alerta de Congestión (Demanda supera capacidad)
probabilidad_congestion = 1 / (1 + np.exp(-diferencia_demanda / 300))
estado_operacion = (np.random.rand(TOTAL_REGISTROS) < probabilidad_congestion).astype(int)

# Crear DataFrame principal
df_completo = pd.DataFrame({
    'pasajeros_proyectados': pasajeros,
    'vuelos_simultaneos': vuelos_simultaneos,
    'inspectores_disponibles': inspectores_disponibles,
    'porcentaje_escaneo': porcentaje_escaneo,
    'alerta_congestion': estado_operacion
})

# 3. División dinámica por PORCENTAJE usando train_test_split
df_historia, df_evaluacion = train_test_split(
    df_completo, 
    test_size=PORCENTAJE_EVALUACION, 
    random_state=42,
    stratify=df_completo['alerta_congestion'] # Mantener proporción balanceada de clases
)

# 4. Definir rutas relativas
script_dir = os.path.dirname(os.path.abspath(__file__))
dir_datos = os.path.join(script_dir, "..", "datos")
os.makedirs(dir_datos, exist_ok=True)

path_historia = os.path.join(dir_datos, "dataset_historia_clasificacion.csv")
path_eval = os.path.join(dir_datos, "dataset_evaluacion_clasificacion.csv")

# Guardar archivos CSV
df_historia.to_csv(path_historia, index=False)
df_evaluacion.to_csv(path_eval, index=False)

print("="*75)
print(f" Datasets generados: {len(df_historia)} filas (historia) + {len(df_evaluacion)} filas (evaluación)")
print(" -> Ejecuta 'paso1_carga_y_exploracion.py' para ver el detalle gráfico completo.")
print("="*75)
