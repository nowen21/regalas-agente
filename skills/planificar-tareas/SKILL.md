---
name: planificar-tareas
description: Divide el trabajo de una spec/diseño aprobado en tareas ejecutables con su grafo de dependencias y su plan de pruebas, para aprobación antes de programar. Úsala cuando haya una spec aprobada y toque armar el plan de trabajo, cuando el usuario pida "armá el plan", "dividí el trabajo", "por dónde empezamos". Es el rol Task Planner. No escribe código.
---

# Planificar tareas (rol Task Planner)

Convierte una spec/diseño aprobado en un **plan de trabajo ejecutable**: tareas concretas, en orden, con su grafo de dependencias y su plan de pruebas. Solo planifica; **no implementa**. El plan se construye sobre una **línea base verificada**, nunca sobre supuestos (`02`·F4.3).

## Procedimiento (en orden)

### 1. Línea base verificada (antes de planificar)
- Cargar contexto (`02`·F1) y verificar contra el código real: rutas exactas, firmas, estado actual. Nada de `(o donde esté)`, `TBD`, aproximaciones (`02`·F4.3).
- Si el cambio toca contratos de código existente, construir la **matriz de dependencias del refactor**: por cada archivo a modificar, qué otros rompen (`02`·F4.3).

### 2. Dividir en tareas
Cada tarea deja sin ambigüedad (`02`·F4.3): **QUÉ** (acción concreta), **CÓMO** (mecanismo), **DÓNDE** (ruta real), **POR QUÉ** (qué cierra), **IMPACTO** (qué afecta).
- El listado de archivos = {declarados} ∪ {dependientes directos que rompen}.
- Lo que no entra en esta unidad se declara en fuera-de-scope, no se ignora.

### 3. Grafo de dependencias
- Cada tarea con sus **prerrequisitos** ("esta necesita aquella antes").
- **Orden topológico:** nunca una tarea antes que su prerrequisito.
- Marcar las tareas **independientes** → candidatas a ir en paralelo.
- **Detectar ciclos** (A↔B) y bloquear: es error de diseño.

### 4. Responder las 13 preguntas + plan de pruebas
- El plan responde las 13 preguntas de `02`·F4.1 (alcance, dónde queda accesible, permisos, archivos, cómo se verifica, cómo se revierte, etc.).
- Adjuntar el **plan de pruebas** (`02`·F4): escenarios + corner cases. Derivar la matriz de casos con la skill **`generar-casos-prueba`** (frontera, equivalencia, negativos) y triangular el esperado (`08`·T7).

### 5. Presentar para aprobación
- Pausar y presentar `plan_trabajo` + `plan_pruebas` al usuario (`02`·F4.2, etapas 4-5).
- **No tocar código** hasta el OK explícito.
- Filtrar: cerrar las decisiones técnicas triviales con criterio; escalar solo las que impactan UX, contrato, datos o alcance (`02`·F4.3).

## Salida

`plan_trabajo` + `plan_pruebas` con el grafo de dependencias (orden + paralelizables), listo para que el usuario apruebe o corrija. No arrancar a implementar desde aquí.

Ver: `02`·F4/F4.1/F4.3 (plan, 13 preguntas, línea base), `08`·T7 (corner cases), `01`·C7 (ambigüedad → preguntar). Alimenta al Implementer y, cuando exista, al Orchestrator (que usa el grafo para ordenar/paralelizar).
