import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def preguntar_entero(mensaje, por_defecto):
    texto = input(f"{mensaje} [Enter = {por_defecto}]: ").strip()
    if texto == "":
        return por_defecto
    if texto.isdigit() and int(texto) > 0:
        return int(texto)
    print(f"  Entrada no válida, se usará el valor por defecto ({por_defecto}).")
    return por_defecto


np.random.seed(42)

# Paso 1: configuración interactiva del tamaño de los datasets
print("--- CONFIGURACIÓN DE LOS DATASETS ---")
N_HISTORIA = preguntar_entero("\n¿Cuántos registros para el dataset de entrenamiento (historia)?", 400)
N_EVALUACION = preguntar_entero("¿Cuántos registros para el dataset de evaluación final?", 100)
TOTAL_REGISTROS = N_HISTORIA + N_EVALUACION

# Paso 2: generar datos operativos simulados
inspectores = np.random.randint(5, 35, size=TOTAL_REGISTROS)
presupuesto = inspectores * 160 + np.random.normal(600, 150, size=TOTAL_REGISTROS)
presupuesto = np.round(np.maximum(presupuesto, 800), 2)
tiempo_espera_prom_min = np.round(np.random.uniform(10, 60, size=TOTAL_REGISTROS), 1)

tramites = (inspectores * 42) + (presupuesto * 0.08) - (tiempo_espera_prom_min * 3) + np.random.normal(100, 50, size=TOTAL_REGISTROS)
tramites = np.maximum(tramites, 120).astype(int)

df_completo = pd.DataFrame({
    'inspectores_turno': inspectores,
    'presupuesto_usd': presupuesto,
    'tiempo_espera_min': tiempo_espera_prom_min,
    'tramites_procesados': tramites
})

# Paso 3: dividir en historia (entrenamiento) y evaluación final
df_historia_entrenamiento, df_evaluacion_final = train_test_split(
    df_completo,
    train_size=N_HISTORIA,
    test_size=N_EVALUACION,
    random_state=42
)

# Paso 4: definir rutas y guardar los CSV
script_dir = os.path.dirname(os.path.abspath(__file__))
dir_datos = os.path.join(script_dir, "..", "datos")
os.makedirs(dir_datos, exist_ok=True)

path_historia = os.path.join(dir_datos, "dataset_historia_migracion.csv")
path_eval = os.path.join(dir_datos, "dataset_evaluacion_final.csv")

df_historia_entrenamiento.to_csv(path_historia, index=False)
df_evaluacion_final.to_csv(path_eval, index=False)

print("="*75)
print(" GENERADOR DINÁMICO DE DATASETS (MÓDULO REGRESIÓN)")
print("="*75)
print(f" Total de registros simulados: {TOTAL_REGISTROS}")
print(f" -> Dataset Historia: {len(df_historia_entrenamiento)} filas -> dataset_historia_migracion.csv")
print(f"    (Se usará en paso2 para el split de entrenamiento/prueba)")
print(f" -> Dataset Evaluación Final: {len(df_evaluacion_final)} filas -> dataset_evaluacion_final.csv")
print(f"    (Se usará en paso3 para validación final ciega)")
print("="*75)
