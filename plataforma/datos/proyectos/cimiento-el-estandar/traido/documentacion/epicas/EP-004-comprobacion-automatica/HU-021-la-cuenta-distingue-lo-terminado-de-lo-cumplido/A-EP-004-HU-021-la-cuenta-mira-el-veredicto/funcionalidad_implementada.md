# Funcionalidad implementada — Fase `A-EP-004-HU-021-la-cuenta-mira-el-veredicto` (módulo Programas de comprobación)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-021-la-cuenta-mira-el-veredicto` |
| **Módulo** | Programas de comprobación |
| **Especificación del módulo** | No hay documento aparte. `02·F19`: la redacción del CA es la especificación funcional |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-27 |
| **HU / CA cubiertas** | [HU-021](../HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido.md): `CA-01` a `CA-05`. Los cinco |
| **Fecha de cierre** | 2026-08-27 |
| **Versión del estándar al cerrar** | `35.2.0` |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | `735d00c` |

---

## 1. Qué se implementó — resumen

**El número que responde «cuánto falta» dejó de contar como hecho el trabajo que no cumplió.**

Antes decía `85 completas`. Ahora dice **`85 terminadas, de las cuales 51 cumplen, 11 no cumplen y 23 no dicen si cumplen`**.

**Estaba sobrestimado en un 40%** — más de lo que se estimó al planearlo.

**Y la causa no era descuido de nadie.** El molde del documento de cierre ofrecía `Cumple / Cumple con observaciones` y **no tenía forma de decir «No cumple»**: diecinueve fases tuvieron que escribirlo en prosa suelta, donde ningún programa lo lee.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem de la historia | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| `RN-01` el conteo distingue terminada de cumplida | servicio | `por_veredicto` en [validadores/fases.py](../../../../../validadores/fases.py) | ✅ | CP-001 |
| `RN-02` el veredicto se lee del resultado | servicio | `veredicto_de` | ✅ | El sabotaje 4, que lo cambia al cierre y rompe 5 pruebas |
| `RN-03` un solo vocabulario | documento | Los tres moldes | ✅ | CP-004 |
| `RN-04` el cierre gana forma de declarar «No cumple» | documento | El campo del molde `11` | ✅ | CP-004 paso 1 |
| `RN-05` una fase sí cierra con «No cumple» | documento | Los tres moldes, corregidos | ✅ | CP-004 paso 4 |
| `RN-06` lo ilegible se cuenta aparte | servicio | La tercera cuenta | ✅ | CP-003 |
| `RN-07` el programa avisa, no corrige | servicio | Solo lee y cuenta | ✅ | No escribe nada |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · el campo de veredicto en el molde del cierre | ✅ | CP-004 |
| T-02 · quitar de los tres moldes la prohibición | ✅ | CP-004 paso 4 |
| T-03 · leer el veredicto del resultado | ✅ | `veredicto_de` |
| T-04 · contar las tres | ✅ | `por_veredicto` |
| T-05 · que la línea las diga | ✅ | CP-001 |
| T-06 a T-09 · las pruebas | ✅ | 14 pruebas nuevas |
| T-10 · medir antes de escribir | ✅ | Los dos números en el `CHANGELOG` |
| T-11 a T-12 · versionar | ✅ | `35.2.0` |
| T-13 · sabotear | ✅ | Seis, seis cazados |

**Correspondencia:** 13 tareas, 13 con resultado. **Ninguna sin hacer.**

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, en el ciclo 2 |
| **Suites ejecutadas + resultado** | `python validadores/pruebas.py`: **417 de 417 verdes** |
| **Defectos abiertos que se aceptaron** | Ninguno. `DEF-01` corregido |

**El único defecto fue de cobertura, no de código**, y lo encontró un sabotaje: el `CA-04` no tenía comprobación automática.

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

```
python validadores/validar.py fases
```

La última línea dice el total, cuántas están sin terminar, y de las terminadas cuántas cumplen, cuántas no y cuántas no lo dicen.

- **Desde el código:** `fases.por_veredicto(proyecto)` da la terna; `fases.veredicto_de(ruta_fase)` da el veredicto de una fase o `None`.
- **`fases.inventario` no cambió:** sigue devolviendo total, terminadas e incompletas.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal |
|---|---|---|
| El veredicto se lee del **resultado**, no del cierre | Está en 103 de 128 contra 55 de 125, y es el documento que lo produce | `RN-02` |
| La cuenta nueva va en **otra función** | Diez pruebas dependen de la firma de `inventario`, y son otra pregunta. Cambiarla habría roto diez para no ganar nada | El plan §2.2 |
| Lo ilegible va a una **tercera cuenta** | Repartirlo haría que el número mintiera de una forma nueva | `S-038` |
| **Basta una fase que no cumpla** | Es la misma regla que `inventario` usa para «terminada»: cerrar la primera no cierra la historia | `CP-002` |
| El **molde del resultado manda** sobre el del cierre | Es quien produce el veredicto, y ya decía «no hay estado intermedio» | `RN-03` |
| Los moldes **dejan de prohibir** cerrar con un rojo | La regla decía lo contrario de lo que se hace, **y lo que se hace es lo correcto**: cerrar no es aprobar, y dejarlo abierto esconde la deuda | `RN-05` |
| **La caja no importa** para el veredicto, y sí para el estado | Un estado con otra caja abre la puerta a variantes; un veredicto no tiene variantes que abrir | `CP-005` |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| **Las 23 historias que no dicen si cumplen** | **Abierta, y ahora visible.** Antes estaban escondidas entre las completas. Cada una se resuelve al escribir su veredicto |
| **Las 11 que no cumplen** | **Abiertas, y ahora contadas aparte.** Es trabajo, y por primera vez se sabe cuánto |
| El andamio crea los cinco documentos vacíos, y con eso una fase recién abierta cuenta **terminada** | **Abierta.** Esta fase la hace inofensiva —cae en «no dice si cumple»— pero el conteo de terminadas sigue inflado. Es `S-053` |

**La tercera es la que queda viva**, y esta misma fase es su ejemplo: la historia que se creó para arreglar el conteo contaba como terminada antes de escribir una línea.

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] La épica [EP-004](../../epica.md): la `HU-021` en sus dos tablas.
- [x] El [README](../README.md) de la carpeta de la historia.
- [x] Los tres moldes de `plantillas/ciclo-vida-proyectos/`.
- [x] La señal `S-055`.
- [x] `VERSION` y `CHANGELOG.md`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna. **No hay nada que migrar**: los documentos siguen igual, y lo que cambia es qué se cuenta.
- **Qué cambia para quien ya tenía el estándar:** su número de trabajos completos **va a bajar**, y con él aparece el reparto. No perdió trabajo: antes se contaba de más.
- **Reversión:** se descarta el commit.
