# Qué reglas del estándar son validables

Auditoría regla por regla de `base/` para decidir cuáles se pueden convertir en **validadores automáticos**. Fecha: **2026-08-05**. Alimenta el pendiente [01 · validadores de código de proyecto](../pendientes/01-validadores-de-codigo-de-proyecto.md) y su contraparte [hecho](../pendientes/hecho/validadores-y-hooks.md). Es una foto: al agregar o cambiar reglas, se revisa.

## Criterio

> Si un script puede decir **sí/no sin opinar** → **validable**.
> Si dos personas pueden discutir si se cumplió → **se queda en el `.md`** (lo interpreta el agente).

Muchas reglas validables inspeccionan el **código/esquema/config del proyecto** o corren herramientas (linter, pruebas, audit de dependencias) → **necesitan un proyecto real con `proyectos/`**; no se pueden validar "en seco" sobre el estándar.

## Conteo

| Categoría | Cuántas |
|---|---|
| ✅ **Ya son validadores** | ~23 |
| 🟡 **Validables, faltan** | ~37 (necesitan inspeccionar código/config del proyecto o correr herramientas) |
| 🔴 **No validables** (criterio humano) | ~93 |

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
| `G8` | `commits.py` | sin atribución de herramienta |
| `F13` | `sesion.py` | existe la carpeta `proyectos/` |
| `C18` | `sesion.py` | sync `CLAUDE.md` ↔ plantilla central |
| `F12.1/2/3/4/5/6/7/11/12/13` | `fases.py` | jerarquía épica→HU→fase · id único · nomenclatura · consecutivo sin huecos · ruta física |
| `DOC16` · `DOC12` · `DOC3/DOC11` | `trazabilidad.py` | enlace bidireccional épica↔HU · ORIGEN en el plan · tabla de cierre |
| `16·CQ1` | `plantillas.py` | completitud de `marco-normativo.md` |
| `DOC14` (resolución de enlaces) | `enlaces.py` | enlaces `.md` resuelven |
| **completitud de plantillas** | `plantillas.py` | marcadores sin llenar, secciones ausentes |
| **enlaces/índices** | `enlaces.py` | enlaces rotos, índices desactualizados |

---

## 🟡 Validables, faltan (PENDIENTE)

> Casi todas requieren un **proyecto real con `proyectos/`** (marcado 🔶). Las "en seco" (sobre el estándar) son escasas.

### Flujo y trazabilidad (`02`, `13·DOC`)

| Regla | Qué comprobaría el script | 🔶 |
|---|---|---|
| `F0` | existen brief/épica/HU/spec padres de cada fase | 🔶 |
| `F2` | ¿código de fase sin spec referenciado? | 🔶 |
| `F4` | `plan_pruebas` junto al `plan_trabajo` | 🔶 |
| `F4.1` | el `plan_trabajo` tiene las 13 secciones | 🔶 |
| `F4.3` | regex de marcas de incertidumbre (`TBD`, `(o similar)`, `?`, `~`) en el plan | 🔶 |
| `F4.4` | cada intervención del plan referencia un CA | 🔶 |
| `DOC1` | doc de cierre con secciones plan/pruebas/resultado | 🔶 |
| `DOC7` | cruce bidireccional A↔B en §Historial cruzado | 🔶 |
| `DOC8` | cierre de análisis: tabla + banner + puntero en prompt vivo | 🔶 |
| `DOC10` | regla `P` numerada + banner si promovida + puntero de señal | 🔶 |
| `DOC13` | entradas de catálogo con campos mínimos | 🔶 |
| `DOC14` (formato) | link de 2 partes: texto=ruta absoluta, link=relativo `.md` | 🔶 |
| `DOC15` | README por carpeta del árbol · HU-NNN · sin placeholders `[…]` | 🔶 |

### Código, datos, pruebas (`03`–`08`)

| Regla | Qué comprobaría | 🔶 |
|---|---|---|
| `03·D1` | columnas de auditoría + FK con política + índices/UNIQUE | 🔶 |
| `03·D2` | cada migración tiene `up` y `down` | 🔶 |
| `03·D3` | columna `NOT NULL` sin default en migración | 🔶 |
| `04·S3` | concatenación en SQL/shell, mass-assignment (regex/linter) | 🔶 |
| `04·S5` | flags `HttpOnly`/`Secure`/HTTPS/hashing en config | 🔶 |
| `04·S7` | audit de vulnerabilidades del ecosistema | 🔶 |
| `05·E1` | `catch` vacío (regex/linter) | 🔶 |
| `05·E5` | campos sensibles en llamadas de log (regex) | 🔶 |
| `06·R1` | heurística de consulta en bucle (N+1) | 🔶 |
| `06·R2` | `SELECT *` y listados sin paginar | 🔶 |
| `07·Q3` | longitud/complejidad de función (métrica) | 🔶 |
| `07·Q6` | linter + formateador sin advertencias | 🔶 |
| `08·T3` | suite en orden aleatorio + detectar rand/fecha/red | 🔶 |
| `08·T4` | config de pruebas apunta a BD efímera, no real | 🔶 |
| `08·T5` | corre la suite y reporta conteo | 🔶 |
| `14·EST1` | módulos en su ubicación según la convención declarada | 🔶 |
| `14·EST2` | nombres siguen convención/regex + límite de longitud | 🔶 |
| `15·IM2` | tres estados + campos de anulación en el esquema | 🔶 |
| `15·IM5` | permiso "anular" separado de "eliminar" en el catálogo | 🔶 |

### Git / CI / dependencias (`09`–`11`)

| Regla | Qué comprobaría | 🔶 |
|---|---|---|
| `G6` | pipeline CI con pruebas + lint | 🔶 |
| `10·DEP3` | audit de vulnerabilidades sin pendientes | 🔶 |
| `10·DEP4` | carpeta instalada no versionada | 🔶 |
| `11·CFG2` | `.env` real ignorado + plantilla sin valores | 🔶 |

---

## 🔴 No validables (se quedan en el `.md` — criterio humano)

- **`00`:** N1, N2, N3, N4, N5, N6.
- **`01`:** C1–C17 (todas menos C18).
- **`02`:** F1, F3, F4.2, F4.5, F5, F6, F7, F8, F9, F10, F11 · F12.8, F12.9, F12.10.
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
- **`13`:** DOC2, DOC4, DOC5, DOC6, DOC9.
- **`14`:** EST3.
- **`15`:** IM1, IM3, IM4.
- **`16`:** CQ2, CQ3, CQ4, Parte B.
- **`17`:** I1, I2, I3, I4, I5, I6.

---

## Conclusión

Sobre el **estándar solo** ya está todo lo validable. Lo demás vive en los proyectos: se empezó a validar contra código real — `S4`, `DEP2` y `G4` ya corren, y son multiproyecto (universales o por detección de stack). Las ~37 restantes son del mismo tipo (código/config/herramientas del proyecto) y se van sumando apuntando a un proyecto real; varias necesitan además correr una herramienta (linter, pruebas, audit) instalada en él.
