# Funcionalidad implementada — Fase `A-EP-004-HU-022-el-molde-sin-llenar-no-cuenta-como-escrito` (módulo Programas de comprobación)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-022-el-molde-sin-llenar-no-cuenta-como-escrito` |
| **Módulo** | Programas de comprobación |
| **Especificación del módulo** | No hay documento aparte. `02·F19`: la redacción del CA es la especificación funcional |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-27 |
| **HU / CA cubiertas** | [HU-022](../HU-022-un-documento-que-sigue-siendo-el-molde-no-cuenta.md): `CA-01` a `CA-05`. Los cinco |
| **Fecha de cierre** | 2026-08-27 |
| **Versión del estándar al cerrar** | `35.3.0` |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | `011754b` |

---

## 1. Qué se implementó — resumen

**Una fase recién abierta contaba como terminada.** El andamio crea sus cinco documentos vacíos, y el conteo miraba que existieran. **Cobró cuatro veces el 2026-08-27**, dos de ellas moviendo una medición en curso.

Ahora un documento que **sigue siendo su plantilla** no cuenta como escrito.

| Antes | Ahora |
|---|---|
| `32 sin terminar · 85 terminadas` | `40 sin terminar · 78 terminadas` |

**No se perdió trabajo: hay siete documentos que nunca se escribieron y hasta hoy contaban como escritos**, y el programa los nombra uno por uno.

**Cómo se distingue un documento escrito de un formulario.** No por **cuántos** marcadores tiene, sino por **cuántos son los de su plantilla**. `«Cumple»` es prosa de esta casa; `«2-4 líneas en lenguaje claro»` está en el molde y solo ahí.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem de la historia | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| `RN-01` un documento que sigue siendo su plantilla no cuenta escrito | servicio | `sigue_siendo_el_molde` en [validadores/fases.py](../../../../../validadores/fases.py) | ✅ | CP-001 |
| `RN-02` se compara contra la plantilla, no contra un umbral | servicio | El cruce con `marcadores_de_los_moldes` | ✅ | CP-002, y el sabotaje 2 |
| `RN-03` una fase con un documento así no está terminada | servicio | `_fase_terminada`, compartida por las dos cuentas | ✅ | CP-001 |
| `RN-04` el programa dice cuáles | servicio | `documentos_que_siguen_siendo_el_molde` | ✅ | CP-003, y el sabotaje 5 |
| `RN-05` avisa, no corrige | servicio | Solo lee | ✅ | CP-005 |
| `RN-06` los marcadores se leen del repositorio | servicio | `marcadores_de_los_moldes` | ✅ | CP-004, y el sabotaje 4 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-00 · el impacto sobre los árboles de prueba | ✅ | 2.299 literales, ninguno al corte |
| T-01 · leer las plantillas una vez | ✅ | `RNF-01` |
| T-02 · tres o más de los suyos | ✅ | CP-002 |
| T-03 · la fase no cuenta terminada | ✅ | CP-001 |
| T-04 · un aviso por documento | ✅ | CP-003 |
| T-05 · los cinco CA | ✅ | 16 pruebas |
| T-06 · medir y nombrar los siete | ✅ | §3 del resultado |
| T-07 · `CHANGELOG` y `VERSION` | ✅ | `35.3.0` |
| T-08 · sabotear | ✅ | Seis, cuatro defectos encontrados |

**Correspondencia:** 9 tareas, 9 con resultado. **Ninguna sin hacer.**

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, en el ciclo 2 |
| **Suites ejecutadas + resultado** | `python validadores/pruebas.py`: **450 verdes** |
| **Defectos abiertos que se aceptaron** | Ninguno. `DEF-01` a `DEF-04` corregidos |

**Los cuatro defectos fueron de las pruebas y del guion que las corre, no del código.** El más grave: **el guion de sabotaje se cayó entre romper el archivo y restaurarlo**, dejó el repositorio con el sabotaje puesto, y el fallo no se vio porque se lanzó con `| tail`. Está en `S-060`.

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

```
python validadores/validar.py fases
```

La línea dice el reparto de siempre, y ahora hay **un aviso por documento** que sigue siendo su plantilla, con el archivo y un marcador de ejemplo.

- **Desde el código:** `fases.marcadores_de_los_moldes(proyecto)` da lo que trae cada plantilla; `fases.moldes_sin_llenar(ruta_fase, de_cada_uno)` da los documentos de una fase que siguen en blanco.
- **`inventario` y `por_veredicto` no cambiaron de firma.** Cambia lo que devuelven.

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal |
|---|---|---|
| Se compara **contra la plantilla** | Un umbral por cantidad ya se probó y señaló tres documentos escritos el mismo día. La cuenta mide el estilo de la casa, no el formulario | `S-059` |
| **El corte no se eligió: lo dio el reparto** | 577 con ninguno, 80 con uno o dos, 7 con tres o más — **y nada entre 3 y 15**. Ajustar el umbral hasta que diera siete habría sido el error de siempre | El plan §2.2 |
| `Veredicto final` del caso análogo, y `Veredicto` a secas: **solo lo medido entra** | Es la misma regla que la fase `C` de la `HU-021`: el patrón se ajusta al hecho, no a lo que podría existir | `S-058` |
| Sin plantilla **no se afirma nada** de ese documento | `04·R4`. Suponer una lista de reserva sería inventar la regla desde el código | `CP-004`, sabotaje 4 |
| La `T-00` **antes** de tocar código | Once pruebas arman árboles con documentos de mentira. Descubrir al final que once rompen por algo que no es defecto cuesta el doble | El plan §4 |
| La línea base, medida **antes** de crear la carpeta | Es literalmente el defecto que esta fase arregla, y ya confundió una medición | El plan §2.0 |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| **Los cinco `plan_pruebas.md` que nunca se escribieron** | **Abierta, y ahora visible.** `B-EP-002-HU-003`, `B-EP-002-HU-004`, `B-EP-004-HU-011`, `B-EP-004-HU-012`, `B-EP-005-HU-002`. Son fases con código y pruebas: **nadie sabe con qué casos se comprobaron** |
| **Los dos `estado-fase.md` en blanco** | **Abierta.** `A-EP-004-HU-021` y `A-EP-007-HU-009` |
| Que el andamio deje de crear los cinco documentos de entrada | **Fuera de alcance por decisión del usuario.** Es la salida 2 del [pendiente 88](../../../../../pendientes/hecho/el-molde-sin-llenar-no-cuenta-como-escrito.md), y cambia cómo se abre una fase |
| Los guiones de sabotaje guardan su copia de restauración **fuera del repositorio** | **Abierta.** [Pendiente 89](../../../../../pendientes/hecho/los-guiones-de-apoyo-quedan-en-el-repositorio.md) |

**La primera es la que más vale**, y no se veía hasta hoy.

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] La épica [EP-004](../../epica.md): la `HU-022` en sus tablas.
- [x] El [README](../README.md) de la carpeta de la historia.
- [x] Las señales `S-059` y `S-060`.
- [x] El README de [historico-chat/scripts/2026-08-27/](../../../../../historico-chat/scripts/2026-08-27/).
- [x] `VERSION` en `35.3.0` y su entrada en el `CHANGELOG`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna. **No hay nada que migrar:** los documentos siguen igual, y lo que cambia es qué se cuenta.
- **Qué cambia para quien ya tenía el estándar:** su número de historias sin terminar **va a subir**. No perdió trabajo: **tiene documentos que nunca se escribieron y hasta hoy contaban como escritos**, y ahora el programa le dice cuáles son.
- **Reversión:** se descarta el commit y se baja `VERSION`.
