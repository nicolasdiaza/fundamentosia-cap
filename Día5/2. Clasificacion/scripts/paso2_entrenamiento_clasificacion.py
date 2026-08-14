# Paso 2: entrenamiento interactivo (elige test_size, escalado y algoritmo)

import os
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, recall_score

plt.rcParams['font.sans-serif'] = 'Segoe UI'


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
print(" MÓDULO CLASIFICACIÓN - PASO 2: ENTRENAMIENTO DE MODELO BINARIO")
print(" (El detalle completo se muestra en la ventana gráfica)")
print("="*75 + "\n")

# Paso 1: rutas relativas
script_dir = os.path.dirname(os.path.abspath(__file__))
ruta_historia = os.path.join(script_dir, "..", "datos", "dataset_historia_clasificacion.csv")
ruta_modelo = os.path.join(script_dir, "..", "modelos", "modelo_clasificacion.joblib")

# Paso 2: cargar datos de historia
df_historia = pd.read_csv(ruta_historia)

X = df_historia[['pasajeros_proyectados', 'vuelos_simultaneos', 'inspectores_disponibles', 'porcentaje_escaneo']]
y = df_historia['alerta_congestion']

# Paso 3: configuración interactiva del entrenamiento
print("--- CONFIGURACIÓN DEL ENTRENAMIENTO ---")

opcion_test = preguntar_opcion(
    "\n¿Qué porcentaje de los datos reservamos para prueba interna?",
    {"1": "10%", "2": "20% (recomendado)", "3": "30%"}, "2")
PORCENTAJE_TEST = {"1": 0.10, "2": 0.20, "3": 0.30}[opcion_test]

usar_escalado = preguntar_si_no("\n¿Escalar variables con StandardScaler antes de entrenar?", False)

opcion_algo = preguntar_opcion(
    "\n¿Qué algoritmo de clasificación quieres entrenar?",
    {
        "1": "Regresión Logística (Logistic Regression)",
        "2": "Árbol de Decisión (Decision Tree Classifier)",
        "3": "Bosque Aleatorio (Random Forest Classifier)",
        "4": "Gradient Boosting Classifier",
        "5": "K-Vecinos Más Cercanos (K-Nearest Neighbors)",
        "6": "Máquina de Vectores de Soporte (SVC)",
    }, "1")

if opcion_algo == "1":
    C = preguntar_numero("  Inverso de la regularización (C)", 1.0, minimo=1e-4)
    nombre_modelo = "Regresión Logística"
    modelo_base = LogisticRegression(C=C, max_iter=1000, random_state=42)
elif opcion_algo == "2":
    max_depth = preguntar_max_depth("  Profundidad máxima (max_depth)")
    nombre_modelo = "Árbol de Decisión"
    modelo_base = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
elif opcion_algo == "3":
    n_estimators = int(preguntar_numero("  Cantidad de árboles (n_estimators)", 100, tipo=int, minimo=1))
    max_depth = preguntar_max_depth("  Profundidad máxima (max_depth)")
    nombre_modelo = "Random Forest"
    modelo_base = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
elif opcion_algo == "4":
    n_estimators = int(preguntar_numero("  Cantidad de árboles (n_estimators)", 100, tipo=int, minimo=1))
    learning_rate = preguntar_numero("  Tasa de aprendizaje (learning_rate)", 0.1, minimo=1e-4)
    max_depth = preguntar_max_depth("  Profundidad máxima (max_depth)", 3)
    nombre_modelo = "Gradient Boosting"
    modelo_base = GradientBoostingClassifier(n_estimators=n_estimators, learning_rate=learning_rate,
                                              max_depth=max_depth, random_state=42)
elif opcion_algo == "5":
    n_neighbors = int(preguntar_numero("  Cantidad de vecinos (n_neighbors)", 5, tipo=int, minimo=1))
    nombre_modelo = "K-Vecinos Más Cercanos"
    modelo_base = KNeighborsClassifier(n_neighbors=n_neighbors)
else:
    C = preguntar_numero("  Parámetro de regularización (C)", 1.0, minimo=1e-4)
    nombre_modelo = "SVM (SVC)"
    # probability=True es obligatorio: paso4 usa .predict_proba() para el semáforo
    modelo_base = SVC(C=C, kernel='rbf', probability=True, random_state=42)

modelo_clasificacion = Pipeline([("escalador", StandardScaler()), ("modelo", modelo_base)]) if usar_escalado else modelo_base

print(f"\nModelo elegido: {nombre_modelo} | Escalado: {'Sí' if usar_escalado else 'No'} | Prueba: {PORCENTAJE_TEST*100:.0f}%\n")

# Paso 4: dividir en entrenamiento / prueba, manteniendo la proporción de clases (stratify)
try:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=PORCENTAJE_TEST, random_state=42, stratify=y)
except ValueError:
    print("  No hay suficientes registros de la clase minoritaria para mantener las proporciones; "
          "se usará una división simple (sin stratify).")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=PORCENTAJE_TEST, random_state=42)

# KNN necesita al menos tantos vecinos como filas de entrenamiento tenga disponibles
if opcion_algo == "5" and n_neighbors > len(X_train):
    print(f"  n_neighbors ({n_neighbors}) supera el tamaño de entrenamiento ({len(X_train)}); se ajusta a {len(X_train)}.")
    n_neighbors = len(X_train)
    modelo_base.set_params(n_neighbors=n_neighbors)

# Paso 5: entrenar el modelo
modelo_clasificacion.fit(X_train, y_train)

# Paso 6: guardar artefacto en modelos/
os.makedirs(os.path.dirname(ruta_modelo), exist_ok=True)
joblib.dump(modelo_clasificacion, ruta_modelo)
print(f"Modelo guardado como 'modelo_clasificacion.joblib'. Entrenado con {len(X_train)} registros, validado con {len(X_test)}.")

# Paso 7: mostrar qué aprendió el modelo (coeficientes o importancia) + validación preliminar
nombres_var = ['Pasajeros\nProyectados', 'Vuelos\nSimultáneos', 'Inspectores\nDisponibles', '% Equipaje\nEscaneado']
estimador_final = obtener_estimador_final(modelo_clasificacion)

fig, (ax_izq, ax_val) = plt.subplots(1, 2, figsize=(11, 6.5))

if hasattr(estimador_final, "coef_"):
    # Regresión Logística binaria: coef_ e intercept_ tienen forma (1, n) y (1,)
    coef = np.array(estimador_final.coef_[0], dtype=float)

    # Si se escaló, los coeficientes están en desviaciones estándar: reconvertir a unidades originales
    escalador = modelo_clasificacion.named_steps.get("escalador") if hasattr(modelo_clasificacion, "named_steps") else None
    if escalador is not None and hasattr(escalador, "scale_"):
        coef = coef / escalador.scale_

    colores_coef = ['#D9381E' if c >= 0 else '#2E7D32' for c in coef]
    ax_izq.barh(nombres_var, coef, color=colores_coef, height=0.5)
    ax_izq.axvline(0, color='#666666', linestyle='--')
    ax_izq.set_title('Impacto Aprendido por la IA en el Riesgo', fontsize=11.5, fontweight='bold')
    ax_izq.set_xlabel('Coeficiente Logístico (Rojo = Aumenta riesgo, Verde = Reduce riesgo)')

elif hasattr(estimador_final, "feature_importances_"):
    importancias = list(estimador_final.feature_importances_)
    barras_imp = ax_izq.barh(nombres_var, importancias, color='#00529B', height=0.5)
    for barra, valor in zip(barras_imp, importancias):
        ax_izq.text(barra.get_width() + max(importancias) * 0.03, barra.get_y() + barra.get_height() / 2,
                    f'{valor*100:.1f}%', va='center', fontsize=9.5, fontweight='bold')
    ax_izq.set_xlim(0, max(importancias) * 1.25)
    ax_izq.set_title('Importancia Relativa de cada Variable', fontsize=11.5, fontweight='bold')
    ax_izq.set_xlabel('Peso relativo en la decisión de Alerta (todas suman 100%)')

else:
    ax_izq.axis('off')
    ax_izq.text(0.5, 0.5, f'El modelo "{nombre_modelo}" no expone\ncoeficientes ni importancias de variables.',
                ha='center', va='center', fontsize=11, color='#555555')

# Paso 8: validación preliminar rápida
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

fig.suptitle(f'Paso 2: Entrenamiento del Modelo de Clasificación ({nombre_modelo})', fontsize=13, fontweight='bold', y=0.98)

plt.figtext(0.5, 0.88,
            "¿Por qué un umbral de decisión? En clasificación binaria, la IA calcula una probabilidad (0%-100%)\n"
            "de que ocurra una Alerta de Congestión. Se aplica un umbral (50%): por encima predice Alerta, por debajo\n"
            "predice Normal — el mismo umbral que enciende el semáforo rojo/verde en el Paso 4.",
            ha='center', fontsize=9, bbox=dict(boxstyle='round,pad=0.5', facecolor='#eef4fb', edgecolor='#00529B'))

plt.figtext(0.5, 0.02,
            "Explicación de lo que aprendió la IA:\n"
            "Coeficiente positivo (rojo) o mayor importancia: factores que más influyen en la probabilidad de Alerta.\n"
            "Coeficiente negativo (verde): contar con más inspectores reduce sensiblemente el riesgo de congestión.",
            ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8f9fa', edgecolor='#cccccc'))

fig.tight_layout(rect=[0, 0.16, 1, 0.80])

plt.show()

print("¡PASO 2 COMPLETADO! Listo para ejecutar 'paso3_evaluacion_clasificacion.py'.\n")
