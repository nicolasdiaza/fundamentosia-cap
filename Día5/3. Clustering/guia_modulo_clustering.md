# Guía del Laboratorio: Clustering

**Objetivo:** practicar el flujo de un proyecto de Machine Learning de **aprendizaje no supervisado** — descubrir perfiles de viajeros (sin decirle a la IA cuáles son de antemano) a partir de su frecuencia de viajes, estadía, monto declarado y tiempo de trámite.

A diferencia de Regresión y Clasificación, aquí la IA no recibe ninguna respuesta correcta durante el entrenamiento: agrupa los datos por similitud matemática (distancia entre puntos).

## Cómo ejecutar el laboratorio

1. `generar_datasets.py` — genera los datos de historia y evaluación con fórmulas independientes entre sí (para forzar que el modelo generalice); puedes elegir cuántos registros de cada uno.
2. `paso1_carga_y_exploracion.py` — explora los datos sin etiquetar antes de entrenar.
3. `paso2_entrenamiento_clustering.py` — entrena el modelo; eliges el algoritmo, cuántos grupos (`k`) buscar, y si se escalan los datos.
4. `paso3_evaluacion_clustering.py` — visualiza los clusters y centroides sobre datos que el modelo nunca vio.
5. `paso4_simulador_clustering.py` — simulador visual para ver a qué perfil se asigna un viajero nuevo.

```bash
python "3. Clustering/scripts/generar_datasets.py"
python "3. Clustering/scripts/paso1_carga_y_exploracion.py"
python "3. Clustering/scripts/paso2_entrenamiento_clustering.py"
python "3. Clustering/scripts/paso3_evaluacion_clustering.py"
python "3. Clustering/scripts/paso4_simulador_clustering.py"
```

## Algoritmos disponibles en el Paso 2

| Algoritmo | ¿Para qué sirve? | Hiperparámetro(s) |
|---|---|---|
| K-Means | Agrupa los datos en `k` grupos según cercanía a un centroide. El más simple y rápido. | `k` (ver abajo) |
| MiniBatch K-Means | Igual que K-Means, pero entrena por lotes — más rápido en datasets grandes, resultado similar. | `k`, `batch_size` |
| Gaussian Mixture | Agrupa asumiendo que cada grupo sigue una distribución normal, permitiendo formas más flexibles que un círculo. | `k`, `covariance_type` |

## Hiperparámetros explicados

| Hiperparámetro | ¿Qué controla? | Valor bajo | Valor alto |
|---|---|---|---|
| `k` (número de grupos, todos los algoritmos) | Cuántos perfiles distintos busca la IA. | Pocos grupos: perfiles más generales, pueden mezclar viajeros distintos. | Muchos grupos: perfiles más específicos, pero más difíciles de interpretar — y más fácil que dos grupos terminen con el mismo nombre de perfil. |
| `batch_size` (MiniBatch K-Means) | Cuántos registros mira antes de actualizar los centroides. | Actualiza más seguido; resultado un poco menos estable. | Se comporta más parecido a K-Means normal, pero más lento de entrenar. |

El laboratorio trae 3 perfiles ya descritos (ver abajo). Con `k` distinto de 3, es normal que algún perfil se repita o no aparezca, porque la IA sigue clasificando por características, no por una cantidad fija de nombres.

**Tipo de covarianza (solo si eliges Gaussian Mixture):** define qué forma pueden tener los grupos.

| Opción | ¿Qué forma le permite a cada grupo? |
|---|---|
| `full` (recomendado) | Cualquier forma y orientación — la más flexible. |
| `tied` | Todos los grupos comparten la misma forma, pero pueden estar en lugares distintos. |
| `diag` | Cada grupo tiene su propia forma, pero alineada a los ejes (sin inclinación). |
| `spherical` | Cada grupo es una esfera/círculo simple, sin inclinación ni alargamiento. |

**Escalado (StandardScaler):** indispensable aquí — estos algoritmos agrupan por distancia, y sin escalar, una variable como el monto declarado (cientos o miles de USD) dominaría sobre la frecuencia de viajes (unidades).

## Los perfiles descubiertos

El número de grupo (0, 1, 2...) que asigna el algoritmo es arbitrario y puede cambiar entre ejecuciones. Por eso el módulo traduce cada centroide a uno de estos perfiles según sus características, nunca por posición:

- **Viajero Frecuente / Negocios:** muchos viajes al año, estadía corta, trámite rápido.
- **Turista Estándar:** viajes ocasionales, estadía de 1-2 semanas.
- **Perfil Atípico / Revisión Especial:** estadía o tiempo de trámite inusualmente largos.
