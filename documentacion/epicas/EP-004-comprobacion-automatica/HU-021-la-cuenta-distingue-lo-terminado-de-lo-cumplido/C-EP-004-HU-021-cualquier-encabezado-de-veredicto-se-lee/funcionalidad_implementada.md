# Funcionalidad implementada — Fase `C-EP-004-HU-021-cualquier-encabezado-de-veredicto-se-lee` (módulo Programas de comprobación)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-004-HU-021-cualquier-encabezado-de-veredicto-se-lee` |
| **Módulo** | Programas de comprobación |
| **Especificación del módulo** | No hay documento aparte. `02·F19`: la redacción del CA es la especificación funcional |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-27 |
| **HU / CA cubiertas** | [HU-021](../HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido.md): el `CA-03` |
| **Fecha de cierre** | 2026-08-27 |
| **Versión del estándar al cerrar** | `35.2.0` — **sin cambio**: no se toca `base/` ni `plantillas/` |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | `fce6e41` |

---

## 1. Qué se implementó — resumen

**La fase `B` dijo que el veredicto está escrito de tres formas y que 39 fases no lo dicen. Sin encabezado hay dos.**

Al enumerar los encabezados de los 130 resultados aparecieron **seis títulos distintos** que empiezan por «Veredicto», y uno más era el veredicto de la fase: `## N. Veredicto`, en quince de ellas.

| Antes | Ahora |
|---|---|
| `56 cumplen, 13 no cumplen, 15 no dicen` | `63 cumplen, 16 no cumplen, 5 no dicen` |

**Diez historias recuperadas, y tres de ellas dicen «No cumple»** — trabajo abierto que no se veía.

**Cómo se cometió el defecto, que es lo que enseña:** la fase `B` contó las formas **que el programa ya sabía buscar** y llamó «sin encabezado» a todo el resto, sin abrirlo. **Es `04·R4` incumplida en la fase que venía a hacerla cumplir.**

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem de la historia | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| `CA-03` lo ilegible se cuenta aparte | servicio | `_VEREDICTO_TITULO_SOLO` en [validadores/fases.py](../../../../../validadores/fases.py) | ✅ | CP-001 |
| `CA-03` **y solo** lo ilegible | servicio | El título exacto, con `\s*$` | ✅ | CP-002, sus cinco pasos |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · el patrón del título exacto | ✅ | CP-001 |
| T-02 · un caso por título que sí se lee | ✅ | 3 pruebas |
| T-03 · que **no** lea «por criterio de aceptación» | ✅ | El caso crítico, y el sabotaje 2 |
| T-04 · que **no** lea `final` ni los otros dos | ✅ | 3 pruebas |
| T-05 · medir y nombrar las diez | ✅ | §3 del resultado |
| T-06 · las 22 de `A` y `B`, sin tocarlas | ✅ | CP-003 |
| T-07 · sabotear | ✅ | Cuatro; el cuarto obligó a un segundo ciclo |

**Correspondencia:** 7 tareas, 7 con resultado. **Ninguna sin hacer.**

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, en el ciclo 2 |
| **Suites ejecutadas + resultado** | `python validadores/pruebas.py`: **434 verdes** |
| **Defectos abiertos que se aceptaron** | Ninguno. `DEF-01` y `DEF-02` corregidos |

**Los dos defectos fueron de la herramienta que juzga, no del código.** Uno de cobertura —faltaba una prueba, y lo destapó un sabotaje en verde— y otro peor: **la guardia del guion de sabotaje daba por buena una corrida con fallas**, porque buscaba «OK» en un texto que trae «OK: sin incumplimientos.».

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

```
python validadores/validar.py fases
```

Sin cambios en el uso. `veredicto_de` y `por_veredicto` **conservan su firma**; cambia cuántos encabezados saben leer.

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal |
|---|---|---|
| El título tiene que ser **exactamente** `Veredicto` | 70 encabezados empiezan por «Veredicto» y son la tabla criterio por criterio. Un patrón que los aceptara **hoy no fallaría** —van seguidos de tabla— y sería correcto por casualidad: el defecto de mañana | `S-058` |
| `Veredicto final` **no** entra, aunque suene a veredicto | Sus cuatro casos no van seguidos de la palabra suelta. Agregarlo «por si acaso» es el mismo error que se está corrigiendo | El plan §2.6 |
| Un patrón **aparte**, no ampliar el de la fase `B` | Aflojarlo arriesga los 91 que ya sirven. El sabotaje 3 lo demuestra: reemplazar en vez de sumar rompe nueve pruebas | `CP-003` |
| El criterio de parada exige **las tres «No cumple»**, no solo el total | Recuperar solo las siete que cumplen daría un número **mejor y más falso**, y se leería como éxito | `S-058` |
| La palabra tiene que ir **pegada** al encabezado | Lo pidió un sabotaje que pasó en verde. Sin eso, el lector se salta la prosa y toma una fila de criterio | `DEF-01` |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| **Los tres «No cumple» que aparecieron** | **Abiertos, y ahora visibles.** `EP-001·HU-007`, `EP-003·HU-002` y `EP-005·HU-001`. Es trabajo que ya existía y no se contaba |
| **Las cinco que de verdad no dicen si cumplen** | **Abierta.** Bajaron de 15, y las que quedan son reales. Cada una se resuelve escribiendo su veredicto |
| **Las 130 fases escriben el veredicto con seis títulos distintos** | **Abierta, y no se toca.** El molde fija uno para lo nuevo; reescribir lo cerrado borra el rastro |
| El andamio deja una fase contando como terminada antes de tener una línea (`S-053`) | **Abierta.** Esta fase lo demostró por **cuarta** vez: crear su carpeta sacó la `HU-021` de las terminadas antes de escribir nada. Es el [pendiente 88](../../../../../pendientes/hecho/el-molde-sin-llenar-no-cuenta-como-escrito.md) |
| Los guiones de sabotaje guardan su copia de restauración **fuera del repositorio** | **Abierta.** Resto de lo mismo que destapó `S-057`; anotado en el [pendiente 89](../../../../../pendientes/89-nada-hace-cumplir-que-los-guiones-queden-en-el-repositorio.md) |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El [README](../README.md) de la carpeta de la historia.
- [x] La señal `S-058`.
- [x] El README de [historico-chat/scripts/2026-08-27/](../../../../../historico-chat/scripts/2026-08-27/).
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**, no se toca `base/` ni `plantillas/`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna.
- **Qué cambia para quien ya tenía el estándar:** bajan sus «no dicen» y **suben las dos otras cuentas**. El trabajo abierto también estaba escondido, y esa mitad es la que importa.
- **Reversión:** se descarta el commit.
