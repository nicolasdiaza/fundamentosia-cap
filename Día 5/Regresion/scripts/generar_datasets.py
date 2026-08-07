import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Semilla para reproducibilidad
np.random.seed(42)
TOTAL_REGISTROS = 500
PORCENTAJE_EVALUACION = 0.20 # 20% para evaluación final fuera de muestra (In-the-wild)

# 1. Generar datos operativos simulados
inspectores = np.random.randint(5, 35, size=TOTAL_REGISTROS)
presupuesto = inspectores * 160 + np.random.normal(600, 150, size=TOTAL_REGISTROS)
presupuesto = np.round(np.maximum(presupuesto, 800), 2)
tiempo_espera_prom_min = np.round(np.random.uniform(10, 60, size=TOTAL_REGISTROS), 1)

# Variable continua -> REGRESIÓN (Trámites procesados)
tramites = (inspectores * 42) + (presupuesto * 0.08) - (tiempo_espera_prom_min * 3) + np.random.normal(100, 50, size=TOTAL_REGISTROS)
tramites = np.maximum(tramites, 120).astype(int)

df_completo = pd.DataFrame({
    'inspectores_turno': inspectores,
    'presupuesto_usd': presupuesto,
    'tiempo_espera_min': tiempo_espera_prom_min,
    'tramites_procesados': tramites
})

# 2. División dinámica por PORCENTAJE usando train_test_split de Scikit-Learn
df_historia_entrenamiento, df_evaluacion_final = train_test_split(
    df_completo, 
    test_size=PORCENTAJE_EVALUACION, 
    random_state=42
)

# 3. Definir rutas relativas
script_dir = os.path.dirname(os.path.abspath(__file__))
dir_datos = os.path.join(script_dir, "..", "datos")
os.makedirs(dir_datos, exist_ok=True)

path_historia = os.path.join(dir_datos, "dataset_historia_migracion.csv")
path_eval = os.path.join(dir_datos, "dataset_evaluacion_final.csv")

# Guardar los 2 archivos CSV principales
df_historia_entrenamiento.to_csv(path_historia, index=False)
df_evaluacion_final.to_csv(path_eval, index=False)

print("="*75)
print(" GENERADOR DINÁMICO DE DATASETS (MÓDULO REGRESIÓN)")
print("="*75)
print(f" Total de registros simulados: {TOTAL_REGISTROS}")
print(f" -> Dataset Historia ({(1-PORCENTAJE_EVALUACION)*100:.0f}%): {len(df_historia_entrenamiento)} filas -> dataset_historia_migracion.csv")
print(f"    (Se usará en paso2 para split automático: Train 80% / Test 20%)")
print(f" -> Dataset Evaluación Final ({PORCENTAJE_EVALUACION*100:.0f}%): {len(df_evaluacion_final)} filas -> dataset_evaluacion_final.csv")
print(f"    (Se usará en paso3 para validación final ciega)")
print("="*75)
