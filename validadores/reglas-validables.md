# Qué reglas del estándar son validables

Auditoría regla por regla de `base/` para decidir cuáles se pueden convertir en **validadores automáticos**. Fecha: **2026-08-05**. Alimenta el pendiente [01 · validadores de código de proyecto](../pendientes/01-validadores-de-codigo-de-proyecto.md) y su contraparte [hecho](../pendientes/hecho/validadores-y-hooks.md). Es una foto: al agregar o cambiar reglas, se revisa.

## Criterio

> Si un script puede decir **sí/no sin opinar** → **validable**.
> Si dos personas pueden discutir si se cumplió → **se queda en el `.md`** (lo interpreta el agente).

Muchas reglas validables inspeccionan el **código/esquema/config del proyecto** o corren herramientas (linter, pruebas, audit de dependencias) → **necesitan un proyecto real con `proyectos/`**; no se pueden validar "en seco" sobre el estándar.

## Conteo

| Categoría | Cuántas |
|---|---|
| ✅ **Ya son validadores** | ~50 |
| 🟡 **Validables, faltan** | ~9 (4 fuzzy o pesadas: `F2`, `F18`, `DOC7`, `DOC14`; 5 necesitan que el proyecto declare su convención/dominio) |
| 🔴 **No validables** (criterio humano) | ~93 |

> Actualización 2026-08-07: el capítulo `02` pasó por el molde de `M5` y por el checklist. Ninguna regla `F` nació ni se derogó, así que este registro no cambia — pero los títulos sí: `F0` es ahora *"Recorre la cadena completa"*, `F3` *"Ejecuta seguido el plan aprobado"*, `F5` *"Corre solo las suites que la fase toca"*, `F13` *"Detente si el proyecto no tiene su estructura base"*. Los ID son los de siempre.
>
> Actualización 2026-08-05: se sumaron `F12.5` (consecutivo sin huecos) y, en `trazabilidad.py`, `DOC16` (enlace bidireccional épica↔HU), `DOC12` (ORIGEN en el plan) y `DOC3/DOC11` (tabla de cierre) — sobre el árbol `documentacion/epicas/`. Después, ya contra código real (agro-system), `04·S4` (`secretos.py`: secretos incrustados) y `10·DEP2` (`dependencias.py`: lockfile versionado).

---

## ✅ Ya son validadores (HECHAS)

| Regla | Validador | Comprueba |
|---|---|---|
| `G2` | `commits.py` | asunto con contenido, línea en blanco, idioma |
| `G3` | `versionado.py` | no versionar secretos/artefactos/config local (por nombre) |
| `04·S4` · `00·N6` | `secretos.py` | secretos incrustados en el código (claves, tokens, `password="…"`) |
| `10·DEP2` | `dependencias.py` | lockfile del ecosistema presente y versionado |
| `09·G4` | `rama.py` | rama dedicada (no la principal) y al día con ella |
| `03·D2` | `migraciones.py` | cada migración declara su reversión (multi-stack por detección) |
| `03·D1` (FK) · `03·D3` · `14·EST2` (longitud) | `esquema.py` | FK con política; `NOT NULL` nuevo sin default; identificador sobre el límite |
| `05·E1` · `05·E5` | `errores.py` | capturas de error vacías; secretos en logs (multi-lenguaje) |
| `06·R2` (`SELECT *`) · `06·R1` | `rendimiento.py` | traer solo lo necesario; consulta en bucle (N+1) |
| `04·S3` · `04·S5` | `seguridad.py` | concatenación SQL/shell; asignación masiva; flags de cookie |
| `07·Q3` | `calidad.py` | funciones demasiado largas |
| `08·T4` · `08·T3` | `aislamiento.py` | BD efímera; orden aleatorio; fuentes flaky |
| `09·G6` | `ci.py` | existe pipeline de CI que corre pruebas y linter |
| `10·DEP4` · `11·CFG2` | `versionado.py` | carpeta instalada no versionada; `.env` real ignorado + molde |
| `07·Q6` | `herramientas.py` (`linter`) | corre el linter/formateador del stack |
| `08·T5` | `herramientas.py` (`suite`) | corre la suite de pruebas del stack |
| `10·DEP3` · `04·S7` | `herramientas.py` (`audit`) | corre el audit de vulnerabilidades del stack (misma herramienta) |
| `G8` | `commits.py` | sin atribución de herramienta |
| `F13` | `sesion.py` | existe la carpeta `proyectos/` |
| `C18` | `sesion.py` | sync `CLAUDE.md` ↔ plantilla central |
| `C19` | `recuerdos.py` · `checklist.py` | la memoria vive en `historico-chat/memory/`; el almacén de la herramienta, vacío |
| `F12.1/2/3/4/5/6/7/11/12/13` | `fases.py` | jerarquía épica→HU→fase · id único · nomenclatura · consecutivo sin huecos · ruta física |
| `DOC16` · `DOC12` · `DOC3/DOC11` | `trazabilidad.py` | enlace bidireccional épica↔HU · ORIGEN en el plan · tabla de cierre |
| `F0` · `F14` · `F17` | `flujo.py` | cada fase tiene sus padres (épica/HU) · el plan trae las 13 preguntas · sin incertidumbre |
| `DOC1` · `DOC8` · `DOC10` · `DOC13` · `DOC15` | `plantillas.py` | completitud contra su plantilla (cierre, análisis, reglas, catálogo, HU) |
| `DOC17` | `enlaces.py` | cada carpeta del árbol lleva su `README.md` y lista lo que cuelga de ella |
| `16·CQ1` | `plantillas.py` | completitud de `marco-normativo.md` |
| `DOC14` (resolución de enlaces) | `enlaces.py` | enlaces `.md` resuelven |
| **completitud de plantillas** | `plantillas.py` | marcadores sin llenar, secciones ausentes |
| **enlaces/índices** | `enlaces.py` | enlaces rotos, índices desactualizados |

---

## 🟡 Validables, faltan (PENDIENTE)

> Casi todas requieren un **proyecto real con `proyectos/`** (marcado 🔶). Las "en seco" (sobre el estándar) son escasas.

### Flujo y trazabilidad (`02`, `13·DOC`)

| Regla | Qué comprobaría el script | Por qué falta |
|---|---|---|
| `F2` | ¿código de fase sin spec referenciado? | cruzar el código con su spec; es el más pesado |
| `F18` | cada intervención del plan referencia un CA | mapear intervención→CA dentro del plan (fuzzy) |
| `DOC7` | cruce bidireccional A↔B en §Historial cruzado | narrativa de complemento entre fases (fuzzy) |
| `DOC14` (formato) | link de 2 partes: texto=ruta absoluta | forzarlo marca los links de texto descriptivo (alto FP) |

### Meta-reglas (`20`) — se validan **en seco**, sobre el propio estándar

No necesitan proyecto: leen `base/`. Son las más rentables del conjunto y hoy no existe ninguna. Alimentan un validador `metareglas.py` pendiente.

| Regla | Qué comprobaría el script |
|---|---|
| `M3` | ninguna regla de `base/` nombra lenguaje, framework, motor, nube ni ruta de un proyecto real (lista negra + revisión de rutas) |
| `M4` | ID único, prefijo exclusivo del capítulo y registrado, consecutivo sin reutilizar |
| `M5` | encabezado `##`, marca de la lista cerrada, presencia del ejemplo, tamaño del cuerpo |
| `M7` | toda dependencia declarada apunta a un ID que existe · sin ciclos · ninguna de capa 2 sobre una `[BLINDADA]` |
| `M9` | toda regla de `base/` aparece clasificada en este archivo |
| `M10` | `CHANGELOG.md` y `VERSION` suben juntos — ya lo hace `version.py`, falta atarlo a la regla |
| `M14` | toda regla trae su bloque de checklist, con resultado y versión contra la que se aplicó |

`M14` es **parcial**: que la regla haya recorrido de verdad los nueve pasos no lo decide un script, pero la **presencia y el resultado** del bloque sí.

### Necesitan que el proyecto **declare** su convención o dominio

No son mecánicas "en seco": hace falta que el proyecto declare, en `.agente/`,
contra qué comparar (su convención de estructura/nombres, qué entidades son
inmutables, qué tablas llevan auditoría). Sin esa declaración, dos personas
pueden discutir si se cumplen → hoy las interpreta el agente.

| Regla | Qué comprobaría | Necesita |
|---|---|---|
| `03·D1` (resto) | columnas de auditoría + `UNIQUE` + índices en lo que se filtra | qué tablas son de dominio (no framework) |
| `14·EST1` | módulos en su ubicación | la convención de estructura declarada |
| `14·EST2` (resto) | nombres siguen la convención | la convención de nombres declarada |
| `15·IM2` | tres estados + campos de anulación en el esquema | qué entidades son inmutables |
| `15·IM5` | permiso "anular" separado de "eliminar" | qué entidades son inmutables |

---

## 🔴 No validables (se quedan en el `.md` — criterio humano)

- **`20` meta-reglas:** `M1`, `M2`, `M6`, `M8`, `M11`, `M12`, `M13` — enrutar, desempatar, decidir si una excepción está completa o si dos reglas dicen lo mismo es criterio: dos personas pueden discutir el resultado.
- **`00` identidad y rol:** ID1, ID2, ID3, ID4, ID5, ID6 — postura, registro y borde del rol: qué cuenta como "criterio de senior" o "sin adornos" lo discute una persona, no un script. `ID3` es la excepción parcial: sus cuatro condiciones ya las validan por separado `08·T5`, `02·F7` y `13·DOC1`; lo que no se valida es la conjunción.
- **`00` núcleo:** N1, N2, N3, N4, N5, N6.
- **`01`:** C1–C17 (todas menos C18).
- **`02`:** F1, F3, F5, F6, F7, F8, F9, F10, F11, F15, F16, F19, F20 · F12.8, F12.9, F12.10.
- **`03`:** D4, D5, D6, D7, D8.
- **`04`:** S1, S2, S6, S8, S9, S10, S11.
- **`05`:** E2, E3, E4.
- **`06`:** R3, R4, R5, R6.
- **`07`:** Q1, Q2, Q4, Q5, Q7.
- **`08`:** T1, T2, T6, T7.
- **`09`:** G1, G5, G7.
- **`10`:** DEP1, DEP5.
- **`11`:** CFG1, CFG3, CFG4.
- **`12`:** PR1, PR2, PR3, PR4, PR5 (toda la capa de privacidad es juicio).
- **`13`:** DOC2, DOC4, DOC5, DOC6, DOC9, DOC18 (que el mapa se haya actualizado **en el mismo cambio** exige leer el diff y entender qué cambió).
- **`14`:** EST3.
- **`15`:** IM1, IM3, IM4.
- **`16`:** CQ2, CQ3, CQ4, Parte B.
- **`17`:** I1, I2, I3, I4, I5, I6.

---

## Conclusión

Sobre el **estándar solo** ya está todo lo validable, y la mayor parte de lo que vive en los proyectos también — ~50 reglas, todo multiproyecto: leen el código, corren la herramienta del stack, o revisan la documentación de flujo (fases, plan, padres, completitud contra plantilla). Quedan **~9**: 4 son fuzzy o pesadas (`F2` cruzar código↔spec, `F4.4`, `DOC7`, `DOC14`), y 5 necesitan que el proyecto **declare su convención/dominio** en `.agente/` (`EST1`, resto de `EST2`, `D1`-resto, `IM2`, `IM5`) — sin esa declaración las interpreta el agente.
