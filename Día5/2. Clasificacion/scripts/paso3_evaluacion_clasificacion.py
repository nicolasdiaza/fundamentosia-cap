# Paso 3: evaluación final (matriz de confusión y métricas)

import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

plt.rcParams['font.sans-serif'] = 'Segoe UI'

print("\n" + "="*75)
print(" MÓDULO CLASIFICACIÓN - PASO 3: MATRIZ DE CONFUSIÓN Y EVALUACIÓN FINAL")
print(" (Los resultados completos se muestran en las 2 ventanas gráficas)")
print("="*75 + "\n")

# Paso 1: rutas relativas
script_dir = os.path.dirname(os.path.abspath(__file__))
ruta_eval = os.path.join(script_dir, "..", "datos", "dataset_evaluacion_clasificacion.csv")
ruta_modelo = os.path.join(script_dir, "..", "modelos", "modelo_clasificacion.joblib")

# Paso 2: cargar modelo y dataset de prueba independiente
modelo_clasificacion = joblib.load(ruta_modelo)
df_eval = pd.read_csv(ruta_eval)

X_eval = df_eval[['pasajeros_proyectados', 'vuelos_simultaneos', 'inspectores_disponibles', 'porcentaje_escaneo']]
y_eval = df_eval['alerta_congestion']

# Paso 3: predecir a ciegas
y_pred = modelo_clasificacion.predict(X_eval)

# Paso 4: matriz de confusión y métricas
cm = confusion_matrix(y_eval, y_pred)
tn, fp, fn, tp = cm.ravel()

acc = accuracy_score(y_eval, y_pred)
prec = precision_score(y_eval, y_pred)
rec = recall_score(y_eval, y_pred)
f1 = f1_score(y_eval, y_pred)

# Referencia: un modelo "tonto" que siempre predice la clase mayoritaria (sin IA)
acc_ingenuo = max(y_eval.mean(), 1 - y_eval.mean())

print(f"Evaluando modelo en {len(df_eval)} registros independientes de 'dataset_evaluacion_clasificacion.csv'...")

# Paso 5: gráfica de matriz de confusión
fig, ax_cm = plt.subplots(figsize=(7.5, 6))

# Matriz personalizada con anotaciones explicativas dentro de cada celda
matriz_textos = np.array([
    [f"Verdadero Normal\n(TN = {tn})\nCorrecto", f"Falsa Alarma\n(FP = {fp})\nGasto innecesario"],
    [f"No Detectado\n(FN = {fn})\nPeligro de colapso", f"Alerta a Tiempo\n(TP = {tp})\nPrevenido"]
])

sns.heatmap(cm, annot=matriz_textos, fmt="", cmap='YlOrRd', cbar=False, ax=ax_cm,
            annot_kws={"size": 11, "weight": "bold"}, linewidths=2, linecolor='white')

ax_cm.set_title('Paso 3: Matriz de Confusión 2x2 (Evaluación Ciega)', fontsize=13, fontweight='bold', pad=15)
ax_cm.set_xlabel('Predicción de la IA', fontsize=11, fontweight='bold')
ax_cm.set_ylabel('Realidad Operativa (Test CSV)', fontsize=11, fontweight='bold')
ax_cm.set_xticklabels(['Predijo Normal (0)', 'Predijo Alerta (1)'], fontsize=10.5)
ax_cm.set_yticklabels(['Fue Normal (0)', 'Fue Alerta (1)'], fontsize=10.5)

plt.figtext(0.5, 0.02,
            "Cómo leer la matriz de confusión:\n"
            "Diagonal principal (arriba-izq. y abajo-der.): aciertos reales de la IA.\n"
            "Abajo a la izquierda (Falsos Negativos): el error más grave. La IA dijo que todo estaba bien pero ocurrió congestión.",
            ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8f9fa', edgecolor='#cccccc'))

fig.tight_layout(rect=[0, 0.16, 1, 0.95])
print("\n(Cierra la ventana de la Matriz para ver las 4 Métricas)")
plt.show()

# Paso 6: gráfica de las 4 métricas clave
fig, ax_met = plt.subplots(figsize=(9.5, 5.5))

metricas_nombres = ['Exactitud Global\n(Accuracy)', 'Confiabilidad Alertas\n(Precision)', 'Cobertura de Riesgos\n(Recall)', 'Balance Global\n(F1-Score)']
metricas_valores = [acc * 100, prec * 100, rec * 100, f1 * 100]
colores_met = ['#00529B', '#2E7D32', '#D9381E', '#7B1FA2']

barras_m = ax_met.bar(metricas_nombres, metricas_valores, color=colores_met, width=0.45)
# Resaltar la barra de Recall (métrica prioritaria del negocio) con borde grueso
barras_m[2].set_edgecolor('#111111')
barras_m[2].set_linewidth(2.5)

for b, val in zip(barras_m, metricas_valores):
    ax_met.text(b.get_x() + b.get_width()/2, b.get_height() + 2, f'{val:.1f}%', ha='center', fontsize=11, fontweight='bold')

barra_recall = barras_m[2]
ax_met.text(barra_recall.get_x() + barra_recall.get_width()/2, barra_recall.get_height() + 11,
            'Métrica prioritaria\npara este sistema', ha='center', fontsize=8.5, color='#111111', fontweight='bold')

# Línea de referencia: lo que lograría un modelo "tonto" sin IA (solo aplica a Accuracy)
ax_met.axhline(acc_ingenuo * 100, color='#888888', linestyle='--', linewidth=1.3)
ax_met.text(3.42, acc_ingenuo * 100 + 2, f'Referencia sin IA: {acc_ingenuo*100:.0f}%',
            ha='right', fontsize=8.5, color='#555555', style='italic')

ax_met.set_ylim(0, 115)
ax_met.set_ylabel('Porcentaje de Calidad (%)', fontsize=10.5)
ax_met.set_title('Paso 3: Evaluación de Métricas Clave de Clasificación', fontsize=13, fontweight='bold', pad=15)
ax_met.grid(True, axis='y', linestyle='--', alpha=0.5)

plt.figtext(0.5, 0.02,
            "Resumen de las 4 métricas de clasificación:\n"
            f"Accuracy ({acc*100:.1f}%): aciertos globales totales (compárese con el {acc_ingenuo*100:.0f}% de un modelo sin IA).\n"
            f"Precision ({prec*100:.1f}%): cuando suena la alarma, ¿qué % de veces es real?\n"
            f"Recall ({rec*100:.1f}%): de todas las congestiones reales, ¿qué % logró prevenir la IA? Es la métrica más importante aquí,\n"
            f"porque perder una congestión real (Falso Negativo) es más grave que una falsa alarma.\n"
            f"F1-Score ({f1*100:.1f}%): promedio armónico general del desempeño.",
            ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8f9fa', edgecolor='#cccccc'))

fig.tight_layout(rect=[0, 0.18, 1, 0.95])
print("\n(Cierra la ventana gráfica para finalizar el Paso 3)")
plt.show()

print("\n¡PASO 3 COMPLETADO! Listo para ejecutar 'paso4_simulador_clasificacion.py'.\n")
