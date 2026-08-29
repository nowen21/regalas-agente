# Funcionalidad implementada — Fase `A-EP-003-HU-006-retrodocumentar-los-procedimientos-por-rol` (módulo Documentos modelo y procedimientos)   ·   `[CAPA 3]`

> **Escrito el 2026-08-28, seis días después de cerrar la fase.** Faltaba, y su ausencia era una de las que hacía que la historia contara como sin terminar. Se escribe con lo que dicen el [plan de trabajo](plan_trabajo.md) y el [resultado de pruebas](resultado_pruebas.md), **sin agregar nada que ellos no respalden** (`04·R4`).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-003-HU-006-retrodocumentar-los-procedimientos-por-rol` |
| **Módulo** | Documentos modelo y procedimientos |
| **Especificación del módulo** | `documentos-modelo/spec.md`, al que esta fase le agregó la tabla de roles (`T-02`) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | HU-006 (CA-01, CA-02, CA-03) |
| **Fecha de cierre** | 2026-08-22 · **este documento, 2026-08-28** |
| **Versión del estándar al cerrar** | No quedó registrada. **No se deduce ahora**: un sello reconstruido seis días después no dice bajo qué reglas se cerró, que es para lo que sirve |
| **Commit** | No quedó registrado |

---

## 1. Qué se implementó — resumen

**Quedó demostrado que cada procedimiento por rol declara qué recibe y qué entrega, y que sin esa entrada no arranca en vez de inventarla.**

Lo notable es con qué se comprobó: **no con casos escritos para la prueba, sino con once corridas reales del mismo encargo** — las once fases del 2026-08-22 en cinco épicas distintas. Once entregables de la misma forma, comparados a máquina.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem del especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 — cada rol declara su entrada y su salida | doc | `skills/`, los once procedimientos · la tabla en `documentos-modelo/spec.md` | ✅ | **Diez de once** las declaran |
| CA-02 — sin la entrada no arranca | doc | Los procedimientos mismos | ✅ | **Once fases detenidas cinco días** por falta de entrada, y arrancadas el día que llegó |
| CA-03 — el mismo encargo da el mismo tipo de resultado | doc | Los once entregables | ✅ | Comparados **a máquina** por `validar.py fases`, que rechazó dos por veredictos que no coincidían |
| La tabla rol → qué recibe → qué entrega | doc | `documentos-modelo/spec.md` | ✅ | `T-01`, `T-02` |

**Faltantes / diferimientos:** uno, y está abierto: **`usar-memoria` no declara entrada ni salida** (ver §6).

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | Levantar la tabla rol → qué recibe → qué entrega, leyendo los diez procedimientos | ✅ hecha | `resultado_pruebas.md` | La tabla |
| T-02 | Escribir el incremento en la especificación, con la tabla y el criterio de qué es un rol | ✅ hecha | `documentos-modelo/spec.md` | — |
| T-03 | Caso: invocar dos procedimientos sin su entrada y ver que **piden el dato en vez de inventarlo** | ✅ hecha | `plan_pruebas.md` | `CA-02` |
| T-04 | Caso: el mismo encargo corrido dos veces entrega el mismo tipo de documento | ✅ hecha | `plan_pruebas.md` | **Once corridas**, no dos |
| T-05 | Numerar los procedimientos a los que les falta declarar entrada o salida | ✅ hecha | `resultado_pruebas.md` | `D-01` |
| T-06 | Correr, escribir el resultado y cerrar la trazabilidad | **parcial** | — | El resultado quedó escrito; **este documento faltaba, y es parte de esa tarea** |

**Correspondencia con el plan:** 6 tareas en el plan, 6 acá.

**Tareas que no se hicieron:** ninguna. **La `T-06` quedó a medias**, y es lo que este documento cierra.

**Archivos tocados que el plan no declaraba:** ninguno registrado.

**Esfuerzo real contra estimado:** el plan estimaba 12 h. **El real no quedó registrado, y no se estima ahora.**

---

## 3. Qué se probó  ·  `08` / `02·F5`

| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple** |

- **Suites ejecutadas + resultado:** `validar.py fases` sobre los once entregables, que **rechazó dos** por veredictos que no coincidían. No es una suite de código: es la comparación a máquina de la forma de los once.
- **Verificaciones manuales** (`08·T4`):
  - Los once procedimientos leídos uno a uno para levantar la tabla.
  - **Once fases detenidas cinco días** por falta de entrada, y arrancadas el día que llegó: el `CA-02` no se simuló, ocurrió.
- **Defectos abiertos que se aceptaron:** **`D-01`**, ver §6.

**Lo que hace fuerte a este resultado es que no probó sobre ejemplos.** Once corridas reales del mismo encargo es más de lo que el criterio pedía, y por eso el `CA-03` se pudo comprobar a máquina en vez de a ojo.

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

- **Punto de entrada:** los procedimientos de `skills/`, que el agente invoca por su nombre.
- **Permisos o datos base sembrados:** ninguno.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| **Se comprobó con corridas reales, no con casos de laboratorio** | Un caso escrito para la prueba demuestra que el procedimiento es invocable, no que se comporte igual dos veces. Once corridas del mismo encargo sí | — |
| **Se comparó a máquina, no a ojo** | `validar.py fases` rechazó dos entregables por veredictos que no coincidían. Una lectura humana los habría dado por iguales | — |
| **Lo que falta se numera, no se corrige** | `D-01` y `D-02` quedaron anotados. Corregir un procedimiento es otra fase | — |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| **`D-01` · `usar-memoria` no declara entrada ni salida.** O es un rol y le faltan, o no es un rol y no debería contarse entre los procedimientos | No previsto | **Abierto.** La pregunta no es documental sino de definición, y por eso no se cerró de paso |
| **`D-02` · el procedimiento de ejecutar una fase no pide verificar la §2 del plan antes de arrancar**, y las once fases de ese día encontraron su línea base envejecida | No previsto | Anotado en el `resultado_pruebas.md` §3 |

**`D-02` es el hallazgo que deja esta fase, y vale más que su veredicto.** Declarar la entrada de un procedimiento no alcanza: **no obliga a comprobar que lo declarado siga siendo cierto.** Once fases arrancaron con una línea base de cinco días atrás, y lo descubrieron ejecutando.

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] Mapa de dependencias: no aplica; la fase no tocó código.
- [x] Catálogo de módulos: no se creó módulo.
- [x] Índice de la carpeta de docs.
- [x] **Especificación del módulo actualizada** con la tabla rol → entrada → salida (`T-02`).

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**No aplica.** Los procedimientos viajan a los proyectos con `skills/`, por el instalador.
