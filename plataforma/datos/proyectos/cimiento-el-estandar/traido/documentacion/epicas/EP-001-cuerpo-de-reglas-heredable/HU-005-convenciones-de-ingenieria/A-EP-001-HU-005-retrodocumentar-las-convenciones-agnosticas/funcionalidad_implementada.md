# Funcionalidad implementada — Fase `A-EP-001-HU-005-retrodocumentar-las-convenciones-agnosticas` (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

> **Escrito el 2026-08-28, seis días después de cerrar la fase.** Faltaba, y su ausencia era una de las que hacía que la historia contara como sin terminar. Se escribe con lo que dicen el [plan de trabajo](plan_trabajo.md) y el [resultado de pruebas](resultado_pruebas.md), **sin agregar nada que ellos no respalden**: lo que no quedó registrado entonces se dice como no registrado, no se reconstruye de memoria (`04·R4`).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-001-HU-005-retrodocumentar-las-convenciones-agnosticas` |
| **Módulo** | Cuerpo de reglas |
| **Especificación del módulo** | La redacción de los CA de la [HU-005](../HU-005-convenciones-de-ingenieria.md) es la especificación funcional (`02·F19`) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | HU-005 (CA-01, CA-02, CA-03) |
| **Fecha de cierre** | 2026-08-22 · **este documento, 2026-08-28** |
| **Versión del estándar al cerrar** | No quedó registrada en su momento. **No se inventa**: el `resultado_pruebas.md` no la anota, y deducirla del `CHANGELOG` daría una fecha, no un sello |
| **Commit** | No quedó registrado |

---

## 1. Qué se implementó — resumen

**Esta fase no construyó: comprobó.** Es retro-documentación (`13·DOC6`): las diecisiete —hoy más— convenciones de `base/` ya estaban escritas, y lo que faltaba era demostrar que **se pueden heredar sin tocarlas**.

Quedó demostrado con dos proyectos de lenguajes distintos, un barrido de las 84 reglas buscando tecnología nombrada, y la revisión de qué capítulos están marcados como opcionales.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem del especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 — una convención sirve igual en dos proyectos de lenguajes distintos | doc | Los capítulos de `base/`, sin cambios | ✅ | La misma regla cumplida con valores distintos en dos stacks, y **84 reglas sin una sola tecnología nombrada** |
| CA-02 — un tema no aparece en dos capítulos | doc | `base/20-meta-reglas/reglas/M2` | ✅ | Barrido de las 84 por pares de capítulos: **4 candidatos, 1 real**, ya derogado hacia su dueño |
| CA-03 — lo que solo sirve a cierto tipo de proyecto queda marcado opcional | doc | La marca `[CAPA 2 · opt-in]` en sus capítulos | ✅ | **Siete capítulos marcados**, y uno apagado de verdad por un proyecto real |

**Faltantes / diferimientos:** ninguno de los CA. Lo que quedó fuera estaba declarado como fuera de alcance desde el plan: reescribir convenciones, poner al día los checklists vencidos, darle punto de entrada a `metareglas.py`, y la capa del proyecto.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | Elegir los dos proyectos y las convenciones a probar | ✅ hecha | `plan_pruebas.md` | Dos stacks distintos |
| T-02 | Caso: la misma convención se cumple en los dos, y lo que cambia se declara en la capa del proyecto | ✅ hecha | `plan_pruebas.md` | `CA-01` |
| T-03 | Recorrer los capítulos buscando lenguaje, framework, motor, nube o herramienta | ✅ hecha | `resultado_pruebas.md` | **Cero apariciones en 84 reglas** |
| T-04 | Levantar la tabla tema → capítulo dueño | ✅ hecha | `analisis/` | La base del barrido de `CA-02` |
| T-05 | Caso: por cada tema con dos apariciones, ver si la segunda enlaza o repite | ✅ hecha | `plan_pruebas.md` | 4 candidatos |
| T-06 | Numerar como hallazgo cada repetición, **sin corregirla** | ✅ hecha | `resultado_pruebas.md` | 1 real, ya derogado |
| T-07 | Caso: los capítulos `opt-in` llevan su marca, y quien no los enciende no incumple | ✅ hecha | `plan_pruebas.md` | `CA-03` |
| T-08 | Revisar si algún capítulo sin marca solo sirve a cierto tipo de proyecto | ✅ hecha | `resultado_pruebas.md` | — |
| T-09 | Correr, escribir el resultado y cerrar la trazabilidad | **parcial** | — | El resultado quedó escrito; **este documento faltaba, y es parte de esa tarea** |

**Correspondencia con el plan:** 9 tareas en el plan, 9 acá.

**Tareas que no se hicieron:** ninguna. **La `T-09` quedó a medias**, y es precisamente lo que este documento cierra seis días después.

**Archivos tocados que el plan no declaraba:** ninguno registrado.

**Esfuerzo real contra estimado:** el plan estimaba 15,5 h. **El real no quedó registrado**, y no se estima ahora: un número inventado seis días después es peor que su ausencia.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple** |

- **Suites ejecutadas + resultado:** no aplica como suite de código. La comprobación fue **lectura sistemática de las 84 reglas** y su ejecución sobre dos proyectos reales.
- **Verificaciones manuales** (`08·T4`):
  - La misma convención cumplida con valores distintos en **dos stacks**.
  - Barrido de las 84 reglas por pares de capítulos: 4 candidatos de solape, **1 real**.
  - Un capítulo `opt-in` **apagado de verdad** por un proyecto real, comprobando que no queda incumpliendo.
- **Defectos abiertos que se aceptaron:** ninguno abierto. Los tres se cerraron dentro de la fase.

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

- **Punto de entrada:** ninguno propio. Lo que esta fase comprobó vive en los capítulos de `base/`, que llegan a cada proyecto por el instalador.
- **Permisos o datos base sembrados:** ninguno.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| **Una sola fase para los tres CA** | Se descartó partirlos: los tres se comprueban sobre el mismo cuerpo y con la misma lectura, y partirlos habría dado fases que existen para cumplir la nomenclatura | — |
| **Los solapes se anotan, no se corrigen** | Corregir una convención es otra fase (`02·F20`). Mezclarlo habría convertido una comprobación en una reescritura sin plan | — |
| **Se probó sobre dos proyectos reales, no sobre ejemplos** | Un ejemplo escrito para la prueba demuestra que la regla es escribible, no que sea heredable | — |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| **`D-03`: el barrido de solapes mira nombres, no exigencias.** Dos reglas que exijan lo mismo con títulos distintos se le escapan | No previsto | Quedó escrito en el `resultado_pruebas.md` §5.1 como lo que ese resultado **no** dice |
| **`D-01` y `D-02`: el plan afirmaba dos cosas que ya no eran ciertas** — daba por incorrible una comprobación construida cinco días antes, y contaba cinco capítulos `opt-in` cuando hoy son siete | No previsto | Cerrados dentro de la fase, al comprobarlos |

**Los dos primeros son el mismo aprendizaje:** un plan escrito sobre la línea base de hace cinco días afirma cosas que dejaron de ser ciertas. **Se corrigieron porque la ejecución volvió a mirar, en vez de citar el plan.**

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] Mapa de dependencias: no aplica; la fase no tocó código.
- [x] Catálogo de módulos: no se creó módulo.
- [x] Índice de la carpeta de docs.
- [x] Especificación del módulo: los CA de la HU, que no cambiaron al comprobar.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**No aplica.** La fase no cambió nada que se despliegue: comprobó lo que ya estaba escrito.
