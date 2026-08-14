# Guía del Laboratorio: Clasificación

**Objetivo:** practicar el flujo completo de un proyecto de Machine Learning de **clasificación binaria** (predecir una categoría, no un número) — en este caso, si un turno migratorio estará en **Operación Normal (0)** o **Alerta de Congestión (1)**.

Se usan dos datasets: uno de **historia** (para entrenar y validar) y uno de **evaluación final** (datos que el modelo nunca vio). Las clases están desbalanceadas a propósito (~70% Normal / 30% Alerta), como ocurre en la realidad operativa.

## Cómo ejecutar el laboratorio

1. `generar_datasets.py` — genera los datos de historia y evaluación (puedes elegir cuántos registros de cada uno).
2. `paso1_carga_y_exploracion.py` — explora los datos y el balance de clases antes de entrenar.
3. `paso2_entrenamiento_clasificacion.py` — entrena el modelo; eliges el % de prueba interna, si se escalan los datos, y el algoritmo con sus hiperparámetros.
4. `paso3_evaluacion_clasificacion.py` — evalúa el modelo con la Matriz de Confusión y 4 métricas (Accuracy, Precision, **Recall**, F1). Recall es la métrica prioritaria aquí: importa más detectar todas las alertas reales que evitar alguna falsa alarma.
5. `paso4_simulador_clasificacion.py` — simulador visual (semáforo) para probar predicciones moviendo los valores de entrada.

```bash
python "2. Clasificacion/scripts/generar_datasets.py"
python "2. Clasificacion/scripts/paso1_carga_y_exploracion.py"
python "2. Clasificacion/scripts/paso2_entrenamiento_clasificacion.py"
python "2. Clasificacion/scripts/paso3_evaluacion_clasificacion.py"
python "2. Clasificacion/scripts/paso4_simulador_clasificacion.py"
```

## Preguntas del Paso 2

**% de prueba interna (test_size):** qué parte de los datos de historia se aparta para validar el modelo apenas termina de entrenar (esos datos no se usan para entrenar). Con más %, la validación es más confiable pero el modelo aprende de menos datos; 20% es un balance típico.

## Algoritmos disponibles en el Paso 2

| Algoritmo | ¿Para qué sirve? | Hiperparámetro(s) |
|---|---|---|
| Regresión Logística | Calcula una probabilidad (0-100%) y aplica un umbral (50%) para decidir la clase. | `C` |
| Árbol de Decisión | Aprende reglas tipo "si-entonces" a partir de los datos. | `max_depth` |
| Random Forest | Combina muchos árboles para predecir de forma más estable. | `n_estimators`, `max_depth` |
| Gradient Boosting | Combina árboles donde cada uno corrige los errores del anterior. | `n_estimators`, `learning_rate`, `max_depth` |
| K-Vecinos Más Cercanos (KNN) | Clasifica un caso nuevo según la clase de sus vecinos más parecidos. | `n_neighbors` |
| SVM (SVC) | Busca la frontera que mejor separa ambas clases. | `C` |

## Hiperparámetros explicados

| Hiperparámetro | ¿Qué controla? | Valor bajo | Valor alto |
|---|---|---|---|
| `C` (Regresión Logística, SVM) | Qué tan flexible es el modelo (es lo inverso a la regularización). | Modelo más simple y conservador. | Se ajusta más a los datos de entrenamiento; riesgo de sobreajuste. |
| `max_depth` (Árbol, Random Forest, Gradient Boosting) | Cuántos niveles de preguntas puede encadenar cada árbol. | Reglas simples; puede no captar todos los patrones (subajuste). | Reglas muy específicas; riesgo de memorizar los datos en vez de aprender (sobreajuste). |
| `n_estimators` (Random Forest, Gradient Boosting) | Cuántos árboles se entrenan y combinan. | Entrena rápido, pero el resultado puede ser menos estable. | Predicciones más estables, pero tarda más en entrenar. |
| `learning_rate` (Gradient Boosting) | Qué tan grande es la corrección que aplica cada árbol nuevo sobre el error del anterior. | Aprende despacio y con cuidado (conviene subir `n_estimators` para compensar). | Aprende rápido, pero puede "pasarse" y perder precisión. |
| `n_neighbors` (KNN) | Cuántos vecinos más cercanos consulta para decidir la clase. | Muy sensible a casos individuales o ruido (ej. 1 vecino). | Decisión más "promediada"; puede perder detalle en los límites entre clases. |

**Escalado (StandardScaler):** pone todas las variables en una escala comparable antes de entrenar. Especialmente importante para KNN y SVM, que deciden por distancia entre puntos.
