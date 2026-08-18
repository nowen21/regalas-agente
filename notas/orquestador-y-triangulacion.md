# Pendientes: SDD Orquestador y triangulación de pruebas

> Notas de diseño sobre dos capacidades que el estándar **no** cubre todavía y qué haría falta para agregarlas. Ninguna requiere rehacer el estándar; son añadidos.

## Estado actual (qué ya está y qué no)

| Concepto | ¿Lo maneja hoy? | Dónde |
|---|---|---|
| Spec-driven development (SDD) | Sí, es el corazón | `02-flujo-de-trabajo` · F2 |
| Trazabilidad especificación → implementación | Sí | `13-documentacion` · DOC3 |
| Corner cases / casos límite | Sí, como principio | `08-pruebas` · T2 |
| **SDD Orquestador** | No | — |
| **Triangulación de pruebas** (método formal) | Parcial | `08-pruebas` (solo "cubrir casos límite/error") |

---

## 1. SDD Orquestador

Pasar de "el agente sigue una secuencia" a "un componente que **coordina y controla** las fases con puertas de paso".

### La línea de montaje (metáfora)

La **línea de montaje** es una metáfora de fábrica: el trabajo avanza por **estaciones**, una tras otra, y en cada una se hace una parte y se revisa antes de pasar a la siguiente. En una fábrica de autos: chasis → motor → pintura → control de calidad. Cada estación hace **una** cosa, y nada pasa a la siguiente sin cumplir lo suyo.

Aplicado al estándar, el orquestador es el flujo de `02` convertido en estaciones con **puerta de control** entre cada una:

```
Estación 1: SPEC         → puerta: ¿está aprobada?
Estación 2: PLAN         → puerta: ¿aprobado + plan de pruebas?
Estación 3: CÓDIGO       → puerta: ¿implementado según el plan?
Estación 4: PRUEBAS      → puerta: ¿todas verdes?
Estación 5: TRAZABILIDAD → puerta: ¿especificación cumplida ítem por ítem?
Estación 6: CIERRE       → listo
```

Idea central: **el trabajo no avanza a la siguiente estación si no pasa la puerta de la actual.** No se programa sin especificación aprobada; no se cierra con pruebas en rojo.

Diferencia con hoy: el estándar ya describe esas estaciones (en `02`), pero **como reglas que el agente sigue**. La línea de montaje real es el **orquestador** que las controla de forma explícita y bloquea el avance en cada puerta.

### Artefactos a crear
- **Skill `sdd-orchestrator`** (como `analizar-proyecto`) que ejecute el flujo de `02` como procedimiento **con puertas (gates)**: no avanza de fase si la anterior no cumple.
- **Archivo de estado** (en qué fase va, qué gate falta) — en `documentacion/` o `.agente/`.

### Decisiones a tomar
- Las **puertas** exactas: ¿especificación aprobada? → ¿plan aprobado? → ¿pruebas verdes? → ¿trazabilidad completa? Cada una bloquea el avance.
- Si se quiere **orquestación real con sub-agentes** (varios en paralelo por fase). Eso **depende de una capacidad del entorno** (los workflows / sub-agentes de Claude Code), no del estándar. Sin esa capacidad, el orquestador es secuencial.

### Esfuerzo
Medio. Un `SKILL.md` bien hecho + definir las puertas. La versión con sub-agentes en paralelo es más, y atada al entorno.

---

## 2. Triangulación de pruebas (corner cases)

Hoy `08` dice "cubrí casos límite y de error". Falta la **técnica formal** de cómo generarlos y cómo converger.

### Artefactos a crear
- **Regla nueva en `08-pruebas`** (ej. `T7 · Triangulación`) que defina los métodos concretos:
  - **Valores de frontera** (0, máximo, vacío, uno más / uno menos).
  - **Clases de equivalencia** (agrupar entradas que se comportan igual).
  - **Tablas de decisión** (combinaciones de condiciones).
  - **Casos negativos / adversariales** (entradas inválidas, ataques).
  - **Triangulación real:** derivar el resultado esperado desde **2–3 fuentes independientes** (la especificación, un cálculo manual, una propiedad invariante) y exigir que coincidan.
- Opcional: **skill `generar-casos-prueba`** que produzca la matriz de corner cases a partir de la especificación.

### Decisiones a tomar
- Cuántas fuentes independientes se exigen para dar algo por "triangulado" (2 o 3).
- Si la matriz de casos es obligatoria en toda fase o solo en lógica crítica.

### Esfuerzo
Bajo-medio. Es sobre todo **contenido** (una sección en `08`), y opcionalmente una skill.

---

## 3. Flujo de dependencias entre tareas (PENDIENTE)

Hoy solo hay orden **lineal** entre estaciones (1→7) y dependencias puntuales de datos (`03`·D3: catálogos antes que sus FK). Falta un **grafo de dependencias entre tareas**.

**Qué faltaría:**
- El **Planificador de tareas** produce un **grafo**: cada tarea con sus **prerrequisitos** ("esta necesita aquella antes"), no solo una lista.
- El **orquestador** lo usa para: (1) ejecutar en **orden topológico** (nunca una tarea antes que su prerrequisito) y (2) detectar tareas **independientes** → candidatas a ir en **paralelo** (si el entorno lo permite).
- **Detectar ciclos** (A depende de B y B de A) y bloquear como error de diseño.

**Esfuerzo:** medio; ligado al Planificador de tareas (ver [`roles-especializados.md`](roles-especializados.md)) y al orquestador.

## Resumen

- **Triangulación** → rápido, puro contenido (una sección en `08`).
- **Orquestador** → skill nueva; con sub-agentes en paralelo depende de las capacidades de Claude Code.
- **Grafo de dependencias entre tareas** → pendiente; parte del Planificador de tareas + el orquestador.
