# Paso 3: evaluación final ciega con datos que el modelo nunca vio

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print("\n" + "="*75)
print(" MÓDULO REGRESIÓN - PASO 3: EVALUACIÓN FINAL CIEGA (DATASET EVALUACIÓN)")
print("="*75 + "\n")

# Paso 1: definir rutas relativas
script_dir = os.path.dirname(os.path.abspath(__file__))
ruta_eval_final = os.path.join(script_dir, "..", "datos", "dataset_evaluacion_final.csv")
ruta_modelo = os.path.join(script_dir, "..", "modelos", "modelo_regresion.joblib")

# Paso 2: cargar modelo y dataset independiente de evaluación
modelo_regresion = joblib.load(ruta_modelo)
df_eval_final = pd.read_csv(ruta_eval_final)

X_eval = df_eval_final[['inspectores_turno', 'presupuesto_usd', 'tiempo_espera_min']]
y_eval = df_eval_final['tramites_procesados']

# Paso 3: predecir sobre los datos de evaluación final
y_pred = modelo_regresion.predict(X_eval)

# Paso 4: calcular métricas finales
mae = mean_absolute_error(y_eval, y_pred)
mse = mean_squared_error(y_eval, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_eval, y_pred)

print(f"Evaluando modelo en {len(df_eval_final)} registros del archivo: {os.path.basename(ruta_eval_final)}")
print("¿QUÉ TAN BIEN PREDICE LA IA CON DATOS QUE NUNCA VIO?")

COLOR_MODELO = '#2a78d6'
COLOR_BASE = '#eb6834'

# Comparación simple contra "adivinar siempre el promedio", sin usar IA
promedio_tramites = y_eval.mean()
mae_promedio = mean_absolute_error(y_eval, [promedio_tramites] * len(y_eval))
rmse_promedio = np.sqrt(mean_squared_error(y_eval, [promedio_tramites] * len(y_eval)))

fig, (ax_error, ax_r2) = plt.subplots(1, 2, figsize=(11, 5.5))

etiquetas_error = ['Sin IA\n(adivinando el\npromedio)', 'Con IA\n(MAE)', 'Con IA\n(RMSE)']
valores_error = [mae_promedio, mae, rmse]
colores_error = [COLOR_BASE, COLOR_MODELO, COLOR_MODELO]
barras = ax_error.bar(etiquetas_error, valores_error, color=colores_error, width=0.5)

for barra, valor in zip(barras, valores_error):
    ax_error.text(barra.get_x() + barra.get_width() / 2, barra.get_height() + max(valores_error) * 0.03,
                   f'{valor:.0f}', ha='center', fontsize=10.5, fontweight='bold')

ax_error.set_title('Comparativa de Error (¡Mientras menor sea el número, mejor!)', fontsize=11, fontweight='bold')
ax_error.set_ylabel('Diferencia en Trámites por día')
ax_error.set_ylim(0, max(valores_error) * 1.3)

ax_r2.bar(['Precisión (R²)'], [r2 * 100], color=COLOR_MODELO, width=0.45)
ax_r2.text(0, r2 * 100 + 2, f'{r2*100:.1f}%', ha='center', fontsize=11.5, fontweight='bold')
ax_r2.set_title('Calificación Global del Modelo (Ideal: 100%)', fontsize=11, fontweight='bold')
ax_r2.set_ylabel('Porcentaje (%)')
ax_r2.set_ylim(0, 115)

fig.suptitle('Paso 3: Evaluación Final en Datos Nuevos (dataset_evaluacion_final.csv)', fontsize=13, fontweight='bold')

plt.figtext(0.5, 0.02,
            "[EXPLICACIÓN DE MÉTRICAS]:\n"
            f"• Sin IA (Error: {mae_promedio:.0f}): Si simplemente adivináramos el promedio diario, nos equivocaríamos por ±{mae_promedio:.0f} trámites.\n"
            f"• Con IA (Error MAE: {mae:.0f}): Gracias al modelo, reducimos el error a solo ±{mae:.0f} trámites (¡Una gran mejora!).\n"
            "• RMSE es similar a MAE pero penaliza más fuerte los días atípicos o emergencias.",
            ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8f9fa', edgecolor='#cccccc'))

fig.tight_layout(rect=[0, 0.16, 1, 0.93])
print("\n(Cierra la ventana gráfica para continuar)")
plt.show()

# Paso 5: gráfica de comparación Real vs Predicho
fig, ax = plt.subplots(figsize=(9.5, 6.5))
ax.scatter(y_eval, y_pred, color='#00529B', alpha=0.8, edgecolors='black', s=85, label='Días de Evaluación (Test)')

# Línea ideal perfecta
min_val = min(min(y_eval), min(y_pred))
max_val = max(max(y_eval), max(y_pred))
ax.plot([min_val, max_val], [min_val, max_val], color='#d9381e', linestyle='--', linewidth=2.5, label='Predicción Perfecta (Ideal)')

ax.set_title('Paso 3: Evaluando la Precisión Día por Día (Real vs Predicho)', fontsize=13, fontweight='bold', pad=15)
ax.set_xlabel('Trámites REALES (Datos que la IA NUNCA vio)', fontsize=11, fontweight='bold')
ax.set_ylabel('Trámites PREDICHOS por la IA', fontsize=11, fontweight='bold')
ax.legend(fontsize=10.5, loc='upper left')
ax.grid(True, linestyle='--', alpha=0.6)

# Anotación explicativa dentro de la gráfica
plt.figtext(0.5, 0.02,
            "[¿CÓMO LEER ESTE GRÁFICO DE PUNTOS?]:\n"
            "• Cada punto azul representa 1 día de operación en Migración Panamá.\n"
            "• La línea roja discontinua es el escenario perfecto donde Predicción = Realidad.\n"
            "• Mientras más PEGADOS estén los puntos azules a la línea roja, MÁS PRECISA es la Inteligencia Artificial.",
            ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.6', facecolor='#f8f9fa', edgecolor='#cccccc'))

plt.tight_layout(rect=[0, 0.16, 1, 0.96])

print("\n(Cierra la ventana gráfica para finalizar el Paso 3)")
plt.show()

print("\n¡PASO 3 COMPLETADO! Listo para ejecutar 'paso4_simulador_regresion.py'.\n")
