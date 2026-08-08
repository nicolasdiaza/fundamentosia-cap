# Guía General de Capacitación IA - Módulo 1: REGRESIÓN LINEAL
**Organización:** Servicio Nacional de Migración de Panamá  
**Concepto Fundamental:** Flujo completo de Machine Learning con división dinámica porcentual de Datasets.

---

## 📊 Concepto Clave: Los 3 Datasets en Machine Learning

Para evitar trampas en la evaluación de la Inteligencia Artificial (como el sobreajuste o *overfitting*), utilizamos **3 subconjuntos de datos diferenciados**:

```text
 ┌──────────────────────────────────────────────────────────────────────────┐
 │                           500 REGISTROS TOTALES                          │
 └────────────────────────────────────┬─────────────────────────────────────┘
                                      │
                                      ▼
                 Generados dinámicamente por PORCENTAJE (80% / 20%)
                                      │
           ┌──────────────────────────┴──────────────────────────┐
           │                                                     │
           ▼                                                     ▼
 📜 1. DATASET HISTORIA (80% = 400 filas)          🎯 3. DATASET EVALUACIÓN FINAL (20% = 100 filas)
 (dataset_historia_migracion.csv)                  (dataset_evaluacion_final.csv)
           │                                                     │
           │ Se divide internamente en PASO 2                    │ Se evalúa a ciegas en PASO 3
           │ usando train_test_split (80% / 20%)                 │ como la "Prueba de Fuego en la Vida Real"
           │                                                     │
     ┌─────┴──────────────────┐                                  │
     ▼                        ▼                                  │
 🏋️ 1.1 ENTRENAMIENTO    🧪 1.2 TEST/VALIDACIÓN                  │
 (320 filas - 80%)       (80 filas - 20%)                        │
  La IA aprende los       Ajuste y validación                    │
  patrones numéricos.     interna durante el                     │
                          entrenamiento.                         │
                                                                 │
     │                        │                                  │
     └────────────────────────┴──────────────────────────────────┘
                                   │
                                   ▼
                       PROCESO DE EVALUACIÓN FINAL
```

---

## 📁 Estructura del Módulo de Regresión

```text
Día 5/
│
└── 📈 Regresion/
    │
    ├── 📂 datos/
    │   ├── dataset_historia_migracion.csv    (400 filas: Para Entrenamiento + Test Interno)
    │   └── dataset_evaluacion_final.csv      (100 filas: Para Evaluación Final fuera de muestra)
    │
    ├── 📂 modelos/
    │   └── modelo_regresion.joblib           (Modelo binario de Regresión guardado)
    │
    └── 📂 scripts/
        ├── generar_datasets.py               (Genera archivos CSV basados en PORCENTAJES)
        ├── paso1_carga_y_exploracion.py      (Exploración EDA de dataset_historia_migracion.csv)
        ├── paso2_entrenamiento_regresion.py  (División automática train_test_split 80/20 y fit)
        ├── paso3_evaluacion_regresion.py     (Evaluación a ciegas en dataset_evaluacion_final.csv)
        └── paso4_simulador_regresion.py      (Simulador interactivo en consola)
```

---

## 🧩 ¿Cómo se conecta esto con lo visto en clase?

Cada paso del laboratorio pone en práctica uno de los temas ya vistos en el curso:

| Tema visto en clase   | ¿Dónde se aplica en el laboratorio? |
|------------------------|--------------------------------------|
| Tipos de datos          | Al abrir los `.csv` en el **Paso 1**, vemos columnas numéricas (inspectores, presupuesto, tiempo de espera, trámites): ese es el tipo de dato que usa este modelo. |
| ¿Qué es Machine Learning? | Todo el laboratorio: la IA "aprende" un patrón a partir de datos históricos, en vez de que alguien le programe una fórmula fija. |
| Tipos de Machine Learning | Este caso es **Regresión**, porque lo que queremos predecir (trámites procesados) es un número que puede tomar cualquier valor, no una categoría. |
| Cómo se entrena          | **Paso 2**: la IA mira 320 días de historia y ajusta sus propias reglas internas (coeficientes) para acercarse lo más posible a los resultados reales. |
| Cómo se evalúa           | **Paso 3**: probamos la IA con 100 días que nunca vio, para saber qué tan bien predice en la vida real (no solo en los datos con los que practicó). |

---

## 🚀 Instrucciones para los Estudiantes

```bash
# 1. Generar los conjuntos de datos dinámicos (80% Historia / 20% Evaluación Final)
python Regresion/scripts/generar_datasets.py

# 2. Cargar y explorar los datos de historia
python Regresion/scripts/paso1_carga_y_exploracion.py

# 3. Entrenar el modelo con train_test_split (80% Train / 20% Test interno)
python Regresion/scripts/paso2_entrenamiento_regresion.py

# 4. Prueba de fuego: Evaluar en el dataset independiente de evaluación final
python Regresion/scripts/paso3_evaluacion_regresion.py

# 5. Probar el Simulador Interactivo
python Regresion/scripts/paso4_simulador_regresion.py
```
