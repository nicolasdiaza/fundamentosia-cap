# 🇵🇦 PROJECT BRIEF
## Proyecto Integrador — Inteligencia Artificial aplicada a Migración Panamá

### Del aprendizaje a una solución real

Durante la capacitación hemos explorado diferentes tecnologías y conceptos de Inteligencia Artificial: Machine Learning, Deep Learning, NLP, LLMs, Prompt Engineering, Computer Vision, agentes, RAG, automatización e IA Responsable.

Ahora es momento de integrarlos.

---

# 1. 🎯 El reto

## Transformando un proceso migratorio con Inteligencia Artificial

Su equipo deberá **identificar un problema o proceso relacionado con migración** y diseñar una solución que utilice Inteligencia Artificial para mejorarlo.

La solución debe demostrar que el equipo puede:

- Identificar un problema real.
- Determinar dónde puede aportar valor la IA.
- Seleccionar la tecnología adecuada.
- Diseñar un flujo de solución.
- Construir un prototipo o Proof of Concept (PoC).
- Evaluar posibles errores y limitaciones.
- Incorporar supervisión humana.
- Considerar los principios de IA Responsable.
- Explicar el impacto esperado de la solución.

### ⚠️ Importante

El objetivo **no es utilizar la mayor cantidad posible de tecnologías**.

Una buena solución no es la que utiliza más IA, sino la que responde mejor a:

> **¿Por qué esta tecnología es apropiada para este problema?**

---

# 2. 🧩 Posibles desafíos

El equipo podrá seleccionar uno de los siguientes desafíos o proponer uno propio, previa validación del instructor.

### 🛂 Desafío 1 — Procesamiento inteligente de documentos

**Problema:** La revisión y extracción de información de documentos puede requerir tiempo y trabajo manual.

Diseñen una solución que pueda ayudar a:

- Analizar documentos.
- Extraer información.
- Detectar inconsistencias.
- Organizar información para el funcionario.

Posibles tecnologías:

**Computer Vision · OCR · Document Intelligence · LLM · Agentes**

Ejemplo de flujo:

```text
Documento
    ↓
Extracción de información
    ↓
Validación
    ↓
Identificación de inconsistencias
    ↓
Revisión humana
```

---

### 👤 Desafío 2 — Asistente inteligente para funcionarios

**Problema:** Los funcionarios pueden necesitar consultar rápidamente información, procedimientos o documentación.

Diseñen un asistente que permita:

- Realizar preguntas en lenguaje natural.
- Consultar información.
- Resumir documentos.
- Orientar al funcionario.
- Proporcionar respuestas fundamentadas.

Posibles tecnologías:

**LLM · Prompt Engineering · RAG · Agentes**

El equipo deberá considerar cómo reducir el riesgo de **alucinaciones**.

---

### 📊 Desafío 3 — Predicción y análisis con Machine Learning

**Problema:** Los datos históricos pueden contener patrones útiles para anticipar situaciones operativas.

Diseñen una solución para, por ejemplo:

- Predecir tiempos o cantidades.
- Clasificar solicitudes.
- Identificar casos que requieren atención.
- Descubrir perfiles o grupos de comportamiento.
- Anticipar congestión operativa.

Posibles tecnologías:

**Regresión · Clasificación · Clustering**

El equipo deberá justificar por qué eligió determinado tipo de Machine Learning.

---

### 🚨 Desafío 4 — Identificación y priorización de casos

**Problema:** No todos los casos requieren el mismo nivel de revisión.

Diseñen una solución que ayude a **priorizar casos para revisión humana**.

Por ejemplo:

```text
                 Solicitudes
                      ↓
                  Modelo IA
                      ↓
        ┌─────────────┼─────────────┐
        ↓             ↓             ↓
      Bajo          Medio          Alto
        ↓             ↓             ↓
   Flujo normal   Revisión       Revisión
                  adicional     especializada
```

El equipo deberá analizar especialmente los **falsos positivos y falsos negativos** y explicar qué tipo de error resulta más crítico.

---

### ⚙️ Desafío 5 — Automatización de un proceso

**Problema:** Existen procesos administrativos repetitivos que podrían ser asistidos o automatizados.

Diseñen un flujo que combine IA y automatización.

Ejemplo:

```text
Solicitud
    ↓
Leer documentos
    ↓
Extraer información
    ↓
Validar
    ↓
Consultar información
    ↓
Clasificar / recomendar
    ↓
👤 Funcionario
    ↓
Decisión
    ↓
Notificación / siguiente proceso
```

Posibles tecnologías:

**IA · Agentes · RPA · Power Apps · Power Automate**

---

# 3. 🤖 Requisitos de la solución

Cada equipo deberá utilizar **al menos tres capacidades de IA o automatización**, seleccionadas de acuerdo con el problema.

Algunas posibilidades:

| Tecnología | Posible aplicación |
|---|---|
| LLM / NLP | Comprensión y generación de lenguaje |
| Prompt Engineering | Control y estructuración de respuestas |
| RAG | Consulta de información contextual |
| Computer Vision | Análisis de documentos e imágenes |
| Machine Learning | Predicción y clasificación |
| Deep Learning | Reconocimiento de patrones complejos |
| Clustering | Descubrimiento de grupos |
| Agentes | Ejecución de tareas y uso de herramientas |
| RPA | Automatización de procesos |

### 👤 Human-in-the-loop

Toda solución deberá identificar al menos **un punto donde intervenga una persona**.

La IA puede:

- analizar,
- recomendar,
- clasificar,
- extraer,
- resumir,
- priorizar,

pero el equipo debe definir claramente **qué decisión permanece bajo responsabilidad humana**.

> **La solución debe apoyar al funcionario, no reemplazar automáticamente la decisión migratoria final.**

---

# 4. 🏗️ Qué debe construir el equipo

El resultado esperado es un **Proof of Concept (PoC)**.

No es necesario construir un sistema productivo completo.

El prototipo debe demostrar de forma clara:

### Entrada
¿Qué información recibe el sistema?

### Procesamiento
¿Qué hace la IA con esa información?

### Resultado
¿Qué produce?

### Acción
¿Qué ocurre después?

### Humano
¿Dónde interviene el funcionario?

El equipo deberá representar su solución mediante un diagrama de arquitectura o flujo.

Ejemplo:

```text
┌─────────────┐
│    Usuario  │
│ / Funcionario│
└──────┬──────┘
       ↓
┌─────────────┐
│ Aplicación  │
└──────┬──────┘
       ↓
┌─────────────────────┐
│     Capa de IA      │
│                     │
│ ML / LLM / CV / RAG │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ Recomendación /     │
│ resultado generado  │
└──────────┬──────────┘
           ↓
     👤 Funcionario
           ↓
        Decisión
```

---

# 5. 🧠 Demuestren lo aprendido

Durante la presentación deberán explicar **qué ocurre detrás de su solución**.

No basta con decir:

> “Utilizamos Machine Learning.”

Deben poder explicar:

- ¿Qué datos utiliza?
- ¿Qué tipo de Machine Learning es?
- ¿Qué está prediciendo?
- ¿Cómo se entrenó?
- ¿Cómo se evaluaría?
- ¿Qué errores puede cometer?

De igual forma, si utilizan un LLM deberán explicar aspectos como:

- ¿Qué modelo utilizan?
- ¿Qué información recibe?
- ¿Qué prompt utilizan?
- ¿Cómo controlan las respuestas?
- ¿Cómo reducen las alucinaciones?

Y si utilizan Computer Vision:

- ¿Qué información visual analiza?
- ¿Qué intenta extraer o identificar?
- ¿Qué puede hacer que falle?
- ¿Cómo se valida el resultado?

---

# 6. 🛡️ IA Responsable

Después de la charla de Ética de IA, cada equipo deberá realizar una revisión de riesgos sobre su solución.

Respondan:

### Bias
¿Podría el sistema favorecer o perjudicar injustamente a algún grupo?

### Privacidad
¿Qué información personal utiliza la solución?

### Precisión
¿Qué ocurre cuando la IA se equivoca?

### Explicabilidad
¿Podemos entender por qué produjo determinado resultado?

### Supervisión humana
¿Dónde debe intervenir una persona?

### Seguridad
¿Qué podría ocurrir si los datos o las entradas son manipulados?

### Impacto
¿Qué consecuencias tendría implementar esta solución incorrectamente?

Finalmente, deberán indicar:

> **¿Qué medidas incorporarían para reducir estos riesgos?**

La revisión ética no debe ser un apartado aislado: **si identifican un riesgo importante, deberán modificar su solución para mitigarlo.**

---

# 7. ⏱️ Tiempo disponible

El proyecto se desarrollará en tres momentos.

## Día 5 — 1 hora
### 🚀 Definición

Al finalizar deberán tener:

- Problema seleccionado.
- Usuario objetivo.
- Objetivo de la solución.
- Tecnologías seleccionadas.
- Primer diseño de arquitectura.

---

## Día 8 — 1 hora
### 🛡️ Revisión de IA Responsable

Después de la charla de Ética:

- Identificar riesgos.
- Revisar Bias.
- Revisar privacidad.
- Analizar errores.
- Definir Human-in-the-loop.
- Ajustar la arquitectura.

---

## Día 9 — 3 horas
### 🛠️ Construcción

**Hora 1:** Construcción del componente principal.

**Hora 2:** Integración y pruebas.

**Hora 3:** Preparación de la demo y presentación.

---

# 8. 🎤 Presentación final

La presentación será realizada durante el Día 10.

Cada equipo deberá realizar una presentación de aproximadamente **10 minutos**.

### Estructura

**1. El problema — 1 min**

¿Qué problema migratorio identificaron?

**2. La solución — 2 min**

¿Cómo lo resolverían utilizando IA?

**3. Demo — 3 min**

Mostrar el prototipo funcionando.

**4. ¿Qué hay detrás? — 2 min**

Explicar las tecnologías y conceptos de IA utilizados.

**5. IA Responsable — 1 min**

¿Qué riesgos identificaron y cómo los mitigaron?

**6. Impacto — 1 min**

¿Qué mejoraría si esta solución se implementara?

---

# 9. 📋 Evaluación

| Criterio | Peso |
|---|---:|
| Definición y comprensión del problema | 10% |
| Uso adecuado de Inteligencia Artificial | 20% |
| Implementación y demostración del PoC | 25% |
| Integración de conceptos aprendidos | 15% |
| IA Responsable y gestión de riesgos | 15% |
| Viabilidad e impacto | 10% |
| Presentación | 5% |
| **TOTAL** | **100%** |

### ⭐ Regla principal de evaluación

**No se evaluará cuántas tecnologías utilizaron.**

Se evaluará si fueron capaces de seleccionar **la tecnología adecuada para resolver el problema adecuado**.

---

# 10. 🏁 La pregunta final

Al finalizar la presentación, cada equipo deberá responder:

> ### **¿Por qué utilizar Inteligencia Artificial para resolver este problema y no simplemente una solución tradicional?**

Y una segunda pregunta:

> ### **¿Qué podría salir mal si implementamos nuestra solución sin supervisión humana?**

El objetivo de este proyecto no es demostrar que podemos poner IA en cualquier proceso.

Es demostrar que podemos **identificar dónde la IA aporta valor, elegir la tecnología adecuada, construir una solución y utilizarla de manera responsable.**

## 🚀 De los conceptos a una solución real

**Problema → Datos → IA → Automatización → Validación → Humano → Impacto**