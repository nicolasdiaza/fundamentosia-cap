"""
===============================================================================
MÓDULO DE REGRESIÓN - PASO 2: ENTRENAMIENTO CON DIVISIÓN AUTOMÁTICA (SPLIT)
Capacitación de IA - Servicio Nacional de Migración de Panamá (Día 5)
===============================================================================
OBJETIVO:
Demostrar el flujo estándar de ML utilizando train_test_split para dividir 
el dataset de historia en:
  1. Entrenamiento (80%): Para que el modelo aprenda los patrones.
  2. Validación Interna / Prueba (20%): Para ajustar y validar antes de desplegar.
===============================================================================
"""

import os
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

COLOR_ENTRENAMIENTO = '#2a78d6'
COLOR_PRUEBA = '#eb6834'
COLOR_POSITIVO = '#2a78d6'
COLOR_NEGATIVO = '#e34948'

print("\n" + "="*75)
print(" MÓDULO REGRESIÓN - PASO 2: ENTRENAMIENTO CON TRAIN / TEST SPLIT (80% / 20%)")
print("="*75 + "\n")

# 1. Rutas relativas
script_dir = os.path.dirname(os.path.abspath(__file__))
ruta_historia = os.path.join(script_dir, "..", "datos", "dataset_historia_migracion.csv")
ruta_modelo = os.path.join(script_dir, "..", "modelos", "modelo_regresion.joblib")

# 2. Cargar historia
df_historia = pd.read_csv(ruta_historia)

X = df_historia[['inspectores_turno', 'presupuesto_usd', 'tiempo_espera_min']]
y = df_historia['tramites_procesados']

# 3. SPLIT PORCENTUAL AUTOMÁTICO CON SCIKIT-LEARN (80% Entrenamiento, 20% Prueba Interna)
PORCENTAJE_TEST = 0.20 # 20% para validación durante el entrenamiento
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=PORCENTAJE_TEST, random_state=42)

print(f"Cargados {len(df_historia)} registros de historia. Mira cómo se dividieron:")

etiquetas_split = ['Entrenamiento\n(la IA aprende aquí)', 'Prueba interna\n(para validar antes de usarla)']
valores_split = [len(X_train), len(X_test)]
colores_split = [COLOR_ENTRENAMIENTO, COLOR_PRUEBA]

fig, ax = plt.subplots(figsize=(7, 5))
barras = ax.bar(etiquetas_split, valores_split, color=colores_split)
for barra, valor in zip(barras, valores_split):
    porcentaje = valor / len(df_historia) * 100
    ax.text(barra.get_x() + barra.get_width() / 2, barra.get_height() + 5,
            f'{valor} días\n({porcentaje:.0f}%)', ha='center', fontsize=10, fontweight='bold')
ax.set_title('Así se dividió tu información', fontsize=13, fontweight='bold')
ax.set_ylabel('Cantidad de días')
ax.set_ylim(0, max(valores_split) * 1.25)
fig.tight_layout()
print("\n(Cierra la ventana gráfica para continuar)")
plt.show()

# 4. Entrenar el modelo de Regresión Lineal
modelo_regresion = LinearRegression()
modelo_regresion.fit(X_train, y_train)

# 5. Guardar modelo en la carpeta modelos/
os.makedirs(os.path.dirname(ruta_modelo), exist_ok=True)
joblib.dump(modelo_regresion, ruta_modelo)

# 5.1 Explicar en palabras simples qué aprendió el modelo
nombres_variables = {
    'inspectores_turno': 'Un Inspector\nde turno más',
    'presupuesto_usd': 'Un USD más\nde presupuesto',
    'tiempo_espera_min': 'Un minuto más\nde espera',
}
print("\n¿QUÉ APRENDIÓ LA IA? Mira el efecto de cada variable:")

etiquetas_coef = [nombres_variables[col] for col in X.columns]
valores_coef = list(modelo_regresion.coef_)
colores_coef = [COLOR_POSITIVO if v >= 0 else COLOR_NEGATIVO for v in valores_coef]

fig, ax = plt.subplots(figsize=(9, 5.5))
barras = ax.barh(etiquetas_coef, valores_coef, color=colores_coef, height=0.55)

# Ajustar límites del eje X para dar espacio a las etiquetas
max_val = max([abs(v) for v in valores_coef])
ax.set_xlim(-max_val * 1.4, max_val * 1.4)

for barra, valor in zip(barras, valores_coef):
    signo = '+' if valor >= 0 else ''
    desplazamiento = max_val * 0.05
    x_texto = barra.get_width() + (desplazamiento if valor >= 0 else -desplazamiento)
    ha_align = 'left' if valor >= 0 else 'right'
    
    ax.text(x_texto, barra.get_y() + barra.get_height() / 2, f'{signo}{valor:.2f} trámites',
            va='center', ha=ha_align, fontsize=10.5, fontweight='bold',
            color='#111111')

ax.axvline(0, color='#666666', linewidth=1.2, linestyle='--')
ax.set_title('Paso 2: ¿Qué aprendió la IA? (Efecto por cada unidad extra)', fontsize=13, fontweight='bold', pad=15)
ax.set_xlabel('Impacto directo en el número de trámites diarios', fontsize=10.5)

# Tarjeta explicativa abajo
plt.figtext(0.5, 0.02,
            f"[EXPLICACIÓN DE LO QUE APRENDIÓ EL MODELO]:\n"
            f"• Barras AZULES (+): Aumentan la capacidad de atención (ej: +1 inspector = +{valores_coef[0]:.1f} trámites).\n"
            f"• Barras ROJAS (-): Reducen la capacidad (ej: +1 min de espera = {valores_coef[2]:.1f} trámites).\n"
            f"• Punto de partida base (constante intercepto b): {modelo_regresion.intercept_:.0f} trámites.",
            ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8f9fa', edgecolor='#cccccc'))

fig.tight_layout(rect=[0, 0.16, 1, 0.95])
print("\n(Cierra la ventana gráfica para continuar)")
plt.show()

# 6. Evaluación preliminar en la muestra de prueba (Validation Test)
y_pred_test = modelo_regresion.predict(X_test)
mae_test = mean_absolute_error(y_test, y_pred_test)
r2_test = r2_score(y_test, y_pred_test)

print("\n¿CÓMO LE FUE A LA IA EN LA VALIDACIÓN INTERNA?")

fig, (ax_error, ax_precision) = plt.subplots(1, 2, figsize=(10, 5.5))

ax_error.bar(['Error promedio\n(MAE)'], [mae_test], color=COLOR_PRUEBA, width=0.45)
ax_error.text(0, mae_test + (mae_test * 0.05), f'±{mae_test:.0f} trámites', ha='center', fontsize=11, fontweight='bold')
ax_error.set_title('Margen de Error Promedio', fontsize=11.5, fontweight='bold')
ax_error.set_ylabel('Trámites de diferencia por día', fontsize=10)
ax_error.set_ylim(0, mae_test * 1.35)

ax_precision.bar(['Precisión\n(R²)'], [r2_test * 100], color=COLOR_ENTRENAMIENTO, width=0.45)
ax_precision.text(0, r2_test * 100 + 2, f'{r2_test*100:.1f}%', ha='center', fontsize=11, fontweight='bold')
ax_precision.set_title('Precisión General del Modelo', fontsize=11.5, fontweight='bold')
ax_precision.set_ylabel('Porcentaje (%)', fontsize=10)
ax_precision.set_ylim(0, 115)

fig.suptitle('Resultado de la Validación Interna (Subconjunto de Prueba 20%)', fontsize=13, fontweight='bold')

plt.figtext(0.5, 0.02,
            "[¿CÓMO INTERPRETAR ESTA VALIDACIÓN?]:\n"
            f"• Error MAE ({mae_test:.0f}): En promedio, la IA se equivoca por solo ±{mae_test:.0f} trámites al día.\n"
            f"• Precisión R² ({r2_test*100:.1f}%): El modelo logra explicar el {r2_test*100:.1f}% del comportamiento real de la estación.",
            ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8f9fa', edgecolor='#cccccc'))

fig.tight_layout(rect=[0, 0.16, 1, 0.93])
print("\n(Cierra la ventana gráfica para continuar)")
plt.show()

print(f"¡Modelo guardado como 'modelo_regresion.joblib' en carpeta modelos/!")

print("\n¡PASO 2 COMPLETADO! Listo para ejecutar 'paso3_evaluacion_regresion.py'.\n")
