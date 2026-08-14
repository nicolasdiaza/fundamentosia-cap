# Guía del Laboratorio: Regresión

**Objetivo:** practicar el flujo completo de un proyecto de Machine Learning de **regresión** (predecir un número, no una categoría) — en este caso, cuántos trámites migratorios se procesarán en un día según inspectores, presupuesto y tiempo de espera.

Se usan dos datasets: uno de **historia** (para entrenar y validar) y uno de **evaluación final** (datos que el modelo nunca vio, para comprobar si realmente aprendió a generalizar).

## Cómo ejecutar el laboratorio

1. `generar_datasets.py` — genera los datos de historia y evaluación (puedes elegir cuántos registros de cada uno).
2. `paso1_carga_y_exploracion.py` — explora los datos antes de entrenar.
3. `paso2_entrenamiento_regresion.py` — entrena el modelo; eliges el % de prueba interna, si se escalan los datos, y el algoritmo con sus hiperparámetros.
4. `paso3_evaluacion_regresion.py` — evalúa el modelo con el dataset de evaluación final.
5. `paso4_simulador_regresion.py` — simulador interactivo para probar predicciones moviendo los valores de entrada.

```bash
python "1. Regresion/scripts/generar_datasets.py"
python "1. Regresion/scripts/paso1_carga_y_exploracion.py"
python "1. Regresion/scripts/paso2_entrenamiento_regresion.py"
python "1. Regresion/scripts/paso3_evaluacion_regresion.py"
python "1. Regresion/scripts/paso4_simulador_regresion.py"
```

## Preguntas del Paso 2

**% de prueba interna (test_size):** qué parte de los datos de historia se aparta para validar el modelo apenas termina de entrenar (esos datos no se usan para entrenar). Con más %, la validación es más confiable pero el modelo aprende de menos datos; 20% es un balance típico.

## Algoritmos disponibles en el Paso 2

| Algoritmo | ¿Para qué sirve? | Hiperparámetro(s) |
|---|---|---|
| Regresión Lineal | Relación simple y directa entre las variables y el resultado. | — (no tiene) |
| Ridge | Como la lineal, pero evita que el modelo se ajuste demasiado al ruido de los datos. | `alpha` |
| Lasso | Igual que Ridge, pero además puede "apagar" variables poco útiles. | `alpha` |
| Árbol de Decisión | Aprende reglas tipo "si-entonces" a partir de los datos. | `max_depth` |
| Random Forest | Combina muchos árboles para predecir de forma más estable. | `n_estimators`, `max_depth` |
| Gradient Boosting | Combina árboles donde cada uno corrige los errores del anterior. | `n_estimators`, `learning_rate`, `max_depth` |

## Hiperparámetros explicados

| Hiperparámetro | ¿Qué controla? | Valor bajo | Valor alto |
|---|---|---|---|
| `alpha` (Ridge, Lasso) | Qué tanto se penaliza el tamaño de los coeficientes. | Cercano a 0: se comporta casi igual que Regresión Lineal normal. | Modelo más simple y conservador; si es demasiado alto puede perder precisión. |
| `max_depth` (Árbol, Random Forest, Gradient Boosting) | Cuántos niveles de preguntas puede encadenar cada árbol. | Reglas simples; puede no captar todos los patrones (subajuste). | Reglas muy específicas; riesgo de memorizar los datos en vez de aprender (sobreajuste). |
| `n_estimators` (Random Forest, Gradient Boosting) | Cuántos árboles se entrenan y combinan. | Entrena rápido, pero el resultado puede ser menos estable. | Predicciones más estables, pero tarda más en entrenar. |
| `learning_rate` (Gradient Boosting) | Qué tan grande es la corrección que aplica cada árbol nuevo sobre el error del anterior. | Aprende despacio y con cuidado (conviene subir `n_estimators` para compensar). | Aprende rápido, pero puede "pasarse" y perder precisión. |

**Escalado (StandardScaler):** pone todas las variables en una escala comparable antes de entrenar. No cambia lo que aprende una Regresión Lineal, pero sí afecta a Ridge y Lasso (porque penalizan el tamaño de los coeficientes).
