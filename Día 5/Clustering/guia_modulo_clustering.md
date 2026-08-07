# Guía General de Capacitación IA - Módulo 3: CLUSTERING (APRENDIZAJE NO SUPERVISADO)
**Organización:** Servicio Nacional de Migración de Panamá  
**Concepto Fundamental:** Algoritmos de Agrupamiento K-Means, Normalización y Centroides.

---

## 📊 ¿Qué es el Módulo de Clustering y cómo se diferencia de Regresión y Clasificación?

- **Aprendizaje Supervisado (Módulos 1 y 2):** Nosotros le dábamos a la IA la respuesta correcta en el entrenamiento (*ej. el número exacto de trámites o la etiqueta 0/1 de Alerta*).
- **Aprendizaje No Supervisado (Módulo 3 - Clustering):** **La IA no recibe ninguna respuesta ni etiqueta previa.** Recibe un conjunto de datos a ciegas y busca por sí sola agrupaciones, patrones o **perfiles naturales** ocultos calculando distancias matemáticas.

---

## 📁 Estructura del Módulo de Clustering

```text
Día 5/
│
└── 🔀 Clustering/
    │
    ├── 📂 datos/
    │   ├── dataset_historia_clustering.csv    (400 filas: Para Descubrir Perfiles con K-Means)
    │   └── dataset_evaluacion_clustering.csv  (100 filas: Para Asignar Perfiles en Datos Nuevos)
    │
    ├── 📂 modelos/
    │   ├── modelo_kmeans.joblib               (Modelo K-Means con k=3 entrenado)
    │   └── escalador_scaler.joblib            (StandardScaler para igualar escalas)
    │
    └── 📂 scripts/
        ├── generar_datasets.py                (Genera historia y evaluación con fórmulas independientes entre sí)
        ├── perfiles_clustering.py             (Definiciones compartidas: traduce cada centroide a su perfil real)
        ├── paso1_carga_y_exploracion.py       (EDA de datos sin etiquetar)
        ├── paso2_entrenamiento_clustering.py  (StandardScaler + K-Means k=3 + Tabla de Centroides)
        ├── paso3_evaluacion_clustering.py      (Visualización de Clusters en 2D + Marcadores Centroides)
        └── paso4_simulador_clustering.py       (Simulador visual interactivo de asignación de perfiles)
```

---

## 🧠 Conceptos Clave de Aprendizaje:

1. **¿Por qué es indispensable la Normalización (`StandardScaler`) en K-Means?**
   - K-Means calcula distancias euclídeas entre puntos. Si no escalamos las variables, un campo como `monto_declarado_usd` (que va de $500 a $8,000 USD) dominaría completamente sobre `frecuencia_viajes_ano` (que va de 1 a 35 viajes), distorsionando los grupos.
   - `StandardScaler` transforma todas las variables a una escala común (promedio 0, desviación estándar 1).

2. **¿Qué es un Centroide?**
   - Es el "Pasajero Promedio" o centro de gravedad de un grupo. K-Means encuentra $k$ centroides ($k=3$) y asigna cada viajero al centroide más cercano.

3. **¿Por qué el número de Grupo (0, 1, 2) puede cambiar entre ejecuciones?**
   - K-Means asigna esos números de forma arbitraria según cómo inicializa el cálculo; no representan un orden fijo ("Grupo 0" no siempre es el mismo perfil). Por eso el Módulo recalcula en cada paso, a partir de las características reales del centroide, a qué perfil corresponde cada número — nunca lo asume por posición.

4. **Los 3 Perfiles Descubiertos por la IA:** (el número de Grupo que le toque a cada uno puede variar; el perfil no)
   - **Viajeros Frecuentes / Negocios:** Alta frecuencia de viajes, estadía corta y trámite muy rápido.
   - **Turistas Estándar:** Viajes ocasionales, estadía de 1 a 2 semanas y trámite estándar.
   - **Perfil Atípico / Revisión Especial:** Estadías inusualmente largas o tiempos de trámite elevados.

---

## 🚀 Instrucciones de Ejecución para los Estudiantes

```bash
# 1. Generar los conjuntos de datos de viajeros
python Clustering/scripts/generar_datasets.py

# 2. Cargar y explorar los datos sin etiquetar
python Clustering/scripts/paso1_carga_y_exploracion.py

# 3. Entrenar K-Means (k=3), escalar datos y calcular centroides
python Clustering/scripts/paso2_entrenamiento_clustering.py

# 4. Visualizar el mapa 2D de clusters y centroides
python Clustering/scripts/paso3_evaluacion_clustering.py

# 5. Probar el Clasificador de Perfiles Visual en tiempo real
python Clustering/scripts/paso4_simulador_clustering.py
```
