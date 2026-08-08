# Guía General de Capacitación IA - Módulo 2: CLASIFICACIÓN BINARIA
**Organización:** Servicio Nacional de Migración de Panamá  
**Concepto Fundamental:** Algoritmos de Clasificación y Matriz de Confusión 2x2.

---

## 📊 ¿Qué es el Módulo de Clasificación y en qué se diferencia de la Regresión?

- **Regresión Lineal (Módulo 1):** Predecía una cantidad numérica continua (*ej. ¿Cuántos trámites procesaremos hoy?*).
- **Clasificación (Módulo 2):** Predice una **Categoría o Etiqueta** (*ej. ¿El turno estará en Estado Normal [0] o Alerta de Congestión [1]?*).

### 🔀 ¿Por qué no reutilizamos la Regresión Lineal para esto?

La Regresión Lineal puede devolver cualquier número (-30, 500, 1200…), pero una probabilidad
solo tiene sentido entre 0% y 100%. La **Regresión Logística** resuelve esto: convierte el
resultado en un número entre 0 y 1 (la probabilidad de Alerta) y luego aplica un
**umbral de decisión** (por defecto 50%) para convertir esa probabilidad en la etiqueta final:

- Probabilidad > 50% → predice **Alerta (1)**
- Probabilidad ≤ 50% → predice **Normal (0)**

Este mismo umbral es el que enciende el semáforo rojo/verde en el Paso 4, y por eso el
simulador ahora muestra explícitamente el % de probabilidad y el umbral usado.

---

## 📁 Estructura del Módulo de Clasificación

```text
Día 5/
│
└── 🛡️ Clasificacion/
    │
    ├── 📂 datos/
    │   ├── dataset_historia_clasificacion.csv    (400 filas: Para Entrenamiento + Test Interno)
    │   └── dataset_evaluacion_clasificacion.csv  (100 filas: Para Evaluación Final fuera de muestra)
    │
    ├── 📂 modelos/
    │   └── modelo_clasificacion.joblib           (Modelo binario de Regresión Logística)
    │
    └── 📂 scripts/
        ├── generar_datasets.py                   (Genera archivos CSV basados en PORCENTAJES)
        ├── paso1_carga_y_exploracion.py          (EDA, balance de clases y matriz de correlación)
        ├── paso2_entrenamiento_clasificacion.py  (Train_test_split 80/20, fit y exportación)
        ├── paso3_evaluacion_clasificacion.py     (Matriz de Confusión 2x2 + 4 Métricas Clave)
        └── paso4_simulador_clasificacion.py      (Simulador visual semafórico interactivo)
```

---

## 🧩 La Matriz de Confusión Explicada (Paso 3)

La **Matriz de Confusión** es la herramienta estándar para evaluar cualquier modelo de clasificación en la industria:

| | Predicho: NORMAL (0) | Predicho: ALERTA (1) |
|---|---|---|
| **Realidad: NORMAL (0)** | **Verdadero Negativo (TN)**<br>*(IA correcta: Todo fluido)* | **Falso Positivo (FP - Falsa Alarma)**<br>*(Gasto innecesario de recursos)* |
| **Realidad: ALERTA (1)** | **Falso Negativo (FN - ¡Peligro!)**<br>*(IA no detectó el colapso)* | **Verdadero Positivo (TP)**<br>*(IA acertó: Congestión prevenida)* |

### 📈 Las 4 Métricas Clave:
1. **Accuracy (Exactitud Global):** Porcentaje total de aciertos globales ($TN + TP / Total$).
2. **Precision (Confiabilidad de Alertas):** De las alarmas que sonó la IA, ¿cuántas eran reales? ($TP / (TP + FP)$).
3. **★ Recall / Sensibilidad (Cobertura de Riesgos) — MÉTRICA PRIORITARIA:** De todas las emergencias reales, ¿cuántas capturó la IA? ($TP / (TP + FN)$).
4. **F1-Score (Balance Global):** Media armónica balanceada entre Precision y Recall.

### ⚖️ ¿Por qué las clases están desbalanceadas (~70% Normal / 30% Alerta) y no 50/50?

Así funciona la realidad operativa: la mayoría de los turnos son normales, y la congestión es
el evento minoritario. Los datasets del Paso 1 se generan a propósito con este desbalance para
enseñar una trampa común: **un modelo "tonto" que siempre dijera "Normal" acertaría ~70% de las
veces sin analizar nada.** Por eso el Accuracy solo no es suficiente para validar un modelo, y
por eso el Paso 3 muestra la línea de referencia "sin IA" junto a las 4 métricas.

### 🎯 ¿Por qué Recall es la métrica prioritaria de este sistema?

En una Alerta Temprana, el costo de los dos tipos de error NO es igual:

- **Falso Positivo (Falsa Alarma):** se refuerza personal sin necesidad — cuesta recursos.
- **Falso Negativo (Peligro de Colapso):** no se detecta una congestión real — cuesta el colapso operativo.

Como el Falso Negativo es mucho más grave, priorizamos **Recall** (cobertura de riesgos reales)
por encima de Precision. Es una decisión de negocio, no solo estadística — vale la pena
discutirla en voz alta con el grupo.

---

## 🚀 Instrucciones de Ejecución para los Estudiantes

```bash
# 1. Generar los datos en la carpeta datos/
python Clasificacion/scripts/generar_datasets.py

# 2. Cargar y explorar la historia (EDA)
python Clasificacion/scripts/paso1_carga_y_exploracion.py

# 3. Entrenar el modelo de Regresión Logística
python Clasificacion/scripts/paso2_entrenamiento_clasificacion.py

# 4. Ver la Matriz de Confusión 2x2 y las 4 Métricas Clave
python Clasificacion/scripts/paso3_evaluacion_clasificacion.py

# 5. Probar el Simulador Visual Semafórico
python Clasificacion/scripts/paso4_simulador_clasificacion.py
```

---

## 📖 Vocabulario Visual (usar los mismos términos en Paso 3 y Paso 4)

| Término | Color | Significado Operativo |
|---|---|---|
| Verdadero Normal (TN) | 🟢 Verde | IA dijo Normal y fue Normal — correcto |
| Falsa Alarma (FP) | 🟠 Naranja | IA dijo Alerta pero fue Normal — gasto innecesario |
| Peligro de Colapso (FN) | 🔴 Rojo | IA dijo Normal pero hubo Alerta — el error más grave |
| Alerta a Tiempo (TP) | 🟢 Verde | IA dijo Alerta y hubo Alerta — colapso prevenido |
| Zona de Incertidumbre | 🟡 Amarillo | Probabilidad muy cerca del umbral (50% ± 8 pts) — reforzar por precaución |

Mantener esta misma paleta de colores en la Matriz de Confusión (Paso 3) y en el semáforo del
simulador (Paso 4) reduce la carga cognitiva para un público que ve estos conceptos por primera vez.

---

## ✅ Quiz Kinestésico de Cierre (antes de pasar al Módulo 3)

Antes de tocar el simulador, plantear estos 3 casos en voz alta y pedir al grupo que identifique
la celda de la Matriz de Confusión correspondiente:

1. *"La IA predijo Alerta. Al final del turno, efectivamente hubo congestión."* → **TP (Alerta a Tiempo)**
2. *"La IA predijo Normal. Al final del turno, hubo congestión y las filas colapsaron."* → **FN (Peligro de Colapso)**
3. *"La IA predijo Alerta. Al final del turno, el flujo fue normal y no pasó nada."* → **FP (Falsa Alarma)**

Este ejercicio verifica comprensión real sin necesidad de código, antes de continuar.

---

## 🌉 Puente hacia el Módulo 3: Clustering

Hasta ahora, en los Módulos 1 y 2, **tú le diste a la IA la respuesta correcta** durante el
entrenamiento (el número de trámites, o si hubo Alerta o no). Esto se llama **aprendizaje
supervisado**.

- **Módulo 1 (Regresión):** predecir un número.
- **Módulo 2 (Clasificación):** predecir sí/no.
- **Módulo 3 (Clustering):** la IA buscará **patrones y grupos ocultos en los datos SIN que le
  digamos la respuesta correcta** (*aprendizaje no supervisado*) — por ejemplo, agrupar turnos
  migratorios con comportamientos similares para descubrir perfiles operativos que ni siquiera
  sabíamos que existían.

Ese es el cambio de mentalidad más grande del curso: pasar de "enseñarle a la IA" a "dejar que
la IA descubra por sí sola".
