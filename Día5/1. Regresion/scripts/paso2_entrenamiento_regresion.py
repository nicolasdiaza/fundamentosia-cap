# Paso 2: entrenamiento interactivo (elige test_size, escalado y algoritmo)

import os
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, r2_score

COLOR_ENTRENAMIENTO = '#2a78d6'
COLOR_PRUEBA = '#eb6834'
COLOR_POSITIVO = '#2a78d6'
COLOR_NEGATIVO = '#e34948'


def preguntar_opcion(mensaje, opciones, por_defecto):
    print(mensaje)
    for clave, texto in opciones.items():
        print(f"  {clave}. {texto}")
    eleccion = input(f"Elige una opción [Enter = {por_defecto}]: ").strip()
    return eleccion if eleccion in opciones else por_defecto


def preguntar_numero(mensaje, por_defecto, tipo=float, minimo=None):
    texto = input(f"{mensaje} [Enter = {por_defecto}]: ").strip()
    if texto == "":
        return por_defecto
    try:
        valor = tipo(texto)
        if minimo is not None and valor < minimo:
            raise ValueError
        return valor
    except ValueError:
        print(f"  Entrada no válida, se usará el valor por defecto ({por_defecto}).")
        return por_defecto


def preguntar_si_no(mensaje, por_defecto):
    etiqueta = 's' if por_defecto else 'n'
    texto = input(f"{mensaje} (s/n) [Enter = {etiqueta}]: ").strip().lower()
    if texto == "":
        return por_defecto
    if texto in ("s", "n"):
        return texto == "s"
    print(f"  Entrada no válida, se usará el valor por defecto ({'sí' if por_defecto else 'no'}).")
    return por_defecto


def preguntar_max_depth(mensaje, por_defecto=None):
    etiqueta_defecto = 'sin límite' if por_defecto is None else por_defecto
    texto = input(f"{mensaje} [Enter = {etiqueta_defecto}]: ").strip()
    if texto.isdigit() and int(texto) >= 1:
        return int(texto)
    if texto != "":
        print(f"  Entrada no válida, se usará el valor por defecto ({etiqueta_defecto}).")
    return por_defecto


def obtener_estimador_final(modelo):
    # Si es un Pipeline devuelve el último paso (el estimador real); si no, el modelo tal cual
    if hasattr(modelo, "named_steps"):
        return list(modelo.named_steps.values())[-1]
    return modelo


print("\n" + "="*75)
print(" MÓDULO REGRESIÓN - PASO 2: ENTRENAMIENTO CON TRAIN / TEST SPLIT")
print("="*75 + "\n")

# Paso 1: rutas relativas
script_dir = os.path.dirname(os.path.abspath(__file__))
ruta_historia = os.path.join(script_dir, "..", "datos", "dataset_historia_migracion.csv")
ruta_modelo = os.path.join(script_dir, "..", "modelos", "modelo_regresion.joblib")

# Paso 2: cargar historia
df_historia = pd.read_csv(ruta_historia)

X = df_historia[['inspectores_turno', 'presupuesto_usd', 'tiempo_espera_min']]
y = df_historia['tramites_procesados']

# Paso 3: configuración interactiva del entrenamiento
print("--- CONFIGURACIÓN DEL ENTRENAMIENTO ---")

opcion_test = preguntar_opcion(
    "\n¿Qué porcentaje de los datos reservamos para prueba interna?",
    {"1": "10%", "2": "20% (recomendado)", "3": "30%"}, "2")
PORCENTAJE_TEST = {"1": 0.10, "2": 0.20, "3": 0.30}[opcion_test]

usar_escalado = preguntar_si_no("\n¿Escalar variables con StandardScaler antes de entrenar?", False)

opcion_algo = preguntar_opcion(
    "\n¿Qué algoritmo de regresión quieres entrenar?",
    {
        "1": "Regresión Lineal (Linear Regression)",
        "2": "Ridge Regression",
        "3": "Lasso Regression",
        "4": "Árbol de Decisión (Decision Tree Regressor)",
        "5": "Bosque Aleatorio (Random Forest Regressor)",
        "6": "Gradient Boosting Regressor",
    }, "1")

if opcion_algo == "1":
    nombre_modelo = "Regresión Lineal"
    modelo_base = LinearRegression()
elif opcion_algo == "2":
    alpha = preguntar_numero("  Valor de alpha (regularización)", 1.0, minimo=0)
    nombre_modelo = "Ridge Regression"
    modelo_base = Ridge(alpha=alpha, random_state=42)
elif opcion_algo == "3":
    alpha = preguntar_numero("  Valor de alpha (regularización)", 1.0, minimo=0)
    nombre_modelo = "Lasso Regression"
    modelo_base = Lasso(alpha=alpha, random_state=42)
elif opcion_algo == "4":
    max_depth = preguntar_max_depth("  Profundidad máxima (max_depth)")
    nombre_modelo = "Árbol de Decisión"
    modelo_base = DecisionTreeRegressor(max_depth=max_depth, random_state=42)
elif opcion_algo == "5":
    n_estimators = int(preguntar_numero("  Cantidad de árboles (n_estimators)", 100, tipo=int, minimo=1))
    max_depth = preguntar_max_depth("  Profundidad máxima (max_depth)")
    nombre_modelo = "Random Forest"
    modelo_base = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
else:
    n_estimators = int(preguntar_numero("  Cantidad de árboles (n_estimators)", 100, tipo=int, minimo=1))
    learning_rate = preguntar_numero("  Tasa de aprendizaje (learning_rate)", 0.1, minimo=1e-4)
    max_depth = preguntar_max_depth("  Profundidad máxima (max_depth)", 3)
    nombre_modelo = "Gradient Boosting"
    modelo_base = GradientBoostingRegressor(n_estimators=n_estimators, learning_rate=learning_rate,
                                             max_depth=max_depth, random_state=42)

modelo_regresion = Pipeline([("escalador", StandardScaler()), ("modelo", modelo_base)]) if usar_escalado else modelo_base

print(f"\nModelo elegido: {nombre_modelo} | Escalado: {'Sí' if usar_escalado else 'No'} | Prueba: {PORCENTAJE_TEST*100:.0f}%\n")

# Paso 4: dividir en entrenamiento / prueba
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

# Paso 5: entrenar el modelo
modelo_regresion.fit(X_train, y_train)

# Paso 6: guardar modelo (o pipeline) en la carpeta modelos/
os.makedirs(os.path.dirname(ruta_modelo), exist_ok=True)
joblib.dump(modelo_regresion, ruta_modelo)

# Paso 7: mostrar qué aprendió el modelo (coeficientes o importancia de características)
nombres_variables = {
    'inspectores_turno': 'Un Inspector\nde turno más',
    'presupuesto_usd': 'Un USD más\nde presupuesto',
    'tiempo_espera_min': 'Un minuto más\nde espera',
}
estimador_final = obtener_estimador_final(modelo_regresion)

if hasattr(estimador_final, "coef_"):
    coef = np.array(estimador_final.coef_, dtype=float)
    intercept = estimador_final.intercept_

    # Si se escaló, los coeficientes están en desviaciones estándar: reconvertir a unidades originales
    escalador = modelo_regresion.named_steps.get("escalador") if hasattr(modelo_regresion, "named_steps") else None
    if escalador is not None and hasattr(escalador, "scale_"):
        coef = coef / escalador.scale_
        intercept = intercept - np.sum(coef * escalador.mean_)

    print("\n¿QUÉ APRENDIÓ LA IA? Mira el efecto de cada variable:")

    etiquetas_coef = [nombres_variables[col] for col in X.columns]
    valores_coef = list(coef)
    colores_coef = [COLOR_POSITIVO if v >= 0 else COLOR_NEGATIVO for v in valores_coef]

    fig, ax = plt.subplots(figsize=(9, 5.5))
    barras = ax.barh(etiquetas_coef, valores_coef, color=colores_coef, height=0.55)

    max_val = max([abs(v) for v in valores_coef])
    if max_val == 0:
        print("  Nota: todos los coeficientes son 0 (regularización muy fuerte); se usa un rango fijo para el gráfico.")
        max_val = 1.0
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
    ax.set_title(f'Paso 2: ¿Qué aprendió la IA? ({nombre_modelo})', fontsize=13, fontweight='bold', pad=15)
    ax.set_xlabel('Impacto directo en el número de trámites diarios', fontsize=10.5)

    plt.figtext(0.5, 0.02,
                f"[EXPLICACIÓN DE LO QUE APRENDIÓ EL MODELO]:\n"
                f"• Barras AZULES (+): Aumentan la capacidad de atención (ej: +1 inspector = +{valores_coef[0]:.1f} trámites).\n"
                f"• Barras ROJAS (-): Reducen la capacidad (ej: +1 min de espera = {valores_coef[2]:.1f} trámites).\n"
                f"• Punto de partida base (constante intercepto b): {intercept:.0f} trámites.",
                ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8f9fa', edgecolor='#cccccc'))

    fig.tight_layout(rect=[0, 0.16, 1, 0.95])
    print("\n(Cierra la ventana gráfica para continuar)")
    plt.show()

elif hasattr(estimador_final, "feature_importances_"):
    nombres_variables_imp = {
        'inspectores_turno': 'Inspectores\nde turno',
        'presupuesto_usd': 'Presupuesto\n(USD)',
        'tiempo_espera_min': 'Tiempo de\nespera',
    }
    print("\n¿QUÉ APRENDIÓ LA IA? Mira la importancia relativa de cada variable:")

    etiquetas_imp = [nombres_variables_imp[col] for col in X.columns]
    valores_imp = list(estimador_final.feature_importances_)

    fig, ax = plt.subplots(figsize=(9, 5.5))
    barras = ax.barh(etiquetas_imp, valores_imp, color=COLOR_ENTRENAMIENTO, height=0.55)
    for barra, valor in zip(barras, valores_imp):
        ax.text(barra.get_width() + max(valores_imp) * 0.03, barra.get_y() + barra.get_height() / 2,
                f'{valor*100:.1f}%', va='center', fontsize=10.5, fontweight='bold')
    ax.set_xlim(0, max(valores_imp) * 1.25)
    ax.set_title(f'Paso 2: ¿Qué aprendió la IA? ({nombre_modelo})', fontsize=13, fontweight='bold', pad=15)
    ax.set_xlabel('Importancia relativa en la predicción (todas suman 100%)', fontsize=10.5)

    plt.figtext(0.5, 0.02,
                "[EXPLICACIÓN DE LO QUE APRENDIÓ EL MODELO]:\n"
                "• Estas barras muestran cuánto usa el modelo cada variable para decidir, en términos relativos.\n"
                "• Una barra más ALTA significa que esa variable pesa más en las decisiones (no indica si el efecto es positivo o negativo).\n"
                "• A diferencia de la regresión lineal, este modelo no tiene una fórmula simple de '+1 unidad = X trámites'.",
                ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8f9fa', edgecolor='#cccccc'))

    fig.tight_layout(rect=[0, 0.16, 1, 0.95])
    print("\n(Cierra la ventana gráfica para continuar)")
    plt.show()

# Paso 8: evaluación preliminar en la muestra de prueba
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

fig.suptitle(f'Resultado de la Validación Interna (Subconjunto de Prueba {PORCENTAJE_TEST*100:.0f}%)', fontsize=13, fontweight='bold')

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
