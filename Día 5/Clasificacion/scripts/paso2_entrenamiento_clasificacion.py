"""
===============================================================================
MÓDULO DE CLASIFICACIÓN - PASO 2: ENTRENAMIENTO DEL MODELO BINARIO
Capacitación de IA - Servicio Nacional de Migración de Panamá (Día 5)
===============================================================================
OBJETIVO:
Entrenar un modelo de REGRESIÓN LOGÍSTICA para predecir si una jornada operativa
tendrá 'Operación Normal (0)' o 'Alerta de Congestión (1)', aplicando train_test_split (80/20).
===============================================================================
"""

import os
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score

plt.rcParams['font.sans-serif'] = 'Segoe UI'

print("\n" + "="*75)
print(" MÓDULO CLASIFICACIÓN - PASO 2: ENTRENAMIENTO DE MODELO BINARIO")
print(" (El detalle completo se muestra en la ventana gráfica)")
print("="*75 + "\n")

# 1. Rutas relativas
script_dir = os.path.dirname(os.path.abspath(__file__))
ruta_historia = os.path.join(script_dir, "..", "datos", "dataset_historia_clasificacion.csv")
ruta_modelo = os.path.join(script_dir, "..", "modelos", "modelo_clasificacion.joblib")

# 2. Cargar datos de historia
df_historia = pd.read_csv(ruta_historia)

X = df_historia[['pasajeros_proyectados', 'vuelos_simultaneos', 'inspectores_disponibles', 'porcentaje_escaneo']]
y = df_historia['alerta_congestion']

# 3. SPLIT PORCENTUAL AUTOMÁTICO (80% Entrenamiento / 20% Prueba Interna)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)

# 4. Crear y entrenar el modelo de Clasificación (Logistic Regression)
modelo_clasificacion = LogisticRegression(max_iter=1000)
modelo_clasificacion.fit(X_train, y_train)

# 5. Guardar artefacto en modelos/
os.makedirs(os.path.dirname(ruta_modelo), exist_ok=True)
joblib.dump(modelo_clasificacion, ruta_modelo)
print(f"Modelo guardado como 'modelo_clasificacion.joblib'. Entrenado con {len(X_train)} registros, validado con {len(X_test)}.")

# 6. Explicar coeficientes / impacto aprendido
nombres_var = ['Pasajeros\nProyectados', 'Vuelos\nSimultáneos', 'Inspectores\nDisponibles', '% Equipaje\nEscaneado']
coeficientes = modelo_clasificacion.coef_[0]

fig, (ax_coef, ax_val) = plt.subplots(1, 2, figsize=(11, 6.5))

colores_coef = ['#D9381E' if c >= 0 else '#2E7D32' for c in coeficientes]
barras_coef = ax_coef.barh(nombres_var, coeficientes, color=colores_coef, height=0.5)
ax_coef.axvline(0, color='#666666', linestyle='--')
ax_coef.set_title('Impacto Aprendido por la IA en el Riesgo', fontsize=11.5, fontweight='bold')
ax_coef.set_xlabel('Coeficiente Logístico (Rojo = Aumenta riesgo, Verde = Reduce riesgo)')

# 7. Validación preliminar rápida
y_pred_test = modelo_clasificacion.predict(X_test)
acc_test = accuracy_score(y_test, y_pred_test)
rec_test = recall_score(y_test, y_pred_test)

ax_val.bar(['Exactitud Global\n(Accuracy)', 'Detección de Alertas\n(Recall)'], 
            [acc_test * 100, rec_test * 100], color=['#00529B', '#D9381E'], width=0.45)

for b, val in zip(ax_val.patches, [acc_test * 100, rec_test * 100]):
    ax_val.text(b.get_x() + b.get_width()/2, b.get_height() + 2, f'{val:.1f}%', ha='center', fontsize=11, fontweight='bold')

ax_val.set_ylim(0, 115)
ax_val.set_title(f'Validación Interna Preliminar\n(Entrenado con {len(X_train)} filas, probado con {len(X_test)})', fontsize=11.5, fontweight='bold')
ax_val.set_ylabel('Porcentaje (%)')

fig.suptitle('Paso 2: Entrenamiento del Modelo de Clasificación (Regresión Logística)', fontsize=13, fontweight='bold', y=0.98)

plt.figtext(0.5, 0.88,
            "¿Por qué Regresión Logística y no Lineal (Módulo 1)? La Regresión Lineal puede devolver cualquier número,\n"
            "pero una probabilidad solo tiene sentido entre 0% y 100%. La Logística convierte el resultado en una probabilidad\n"
            "y aplica un umbral de decisión (50%): por encima predice Alerta, por debajo predice Normal, el mismo umbral\n"
            "que enciende el semáforo rojo/verde en el Paso 4.",
            ha='center', fontsize=9, bbox=dict(boxstyle='round,pad=0.5', facecolor='#eef4fb', edgecolor='#00529B'))

plt.figtext(0.5, 0.02,
            "Explicación de lo que aprendió la IA:\n"
            "Coeficiente positivo (rojo): factores como más pasajeros o vuelos aumentan la probabilidad de Alerta.\n"
            "Coeficiente negativo (verde): contar con más inspectores reduce sensiblemente el riesgo de congestión.",
            ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8f9fa', edgecolor='#cccccc'))

fig.tight_layout(rect=[0, 0.16, 1, 0.80])

plt.show()

print("¡PASO 2 COMPLETADO! Listo para ejecutar 'paso3_evaluacion_clasificacion.py'.\n")
