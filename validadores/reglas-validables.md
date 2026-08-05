# Qué reglas del estándar son validables

Auditoría regla por regla de `base/` para decidir cuáles se pueden convertir en **validadores automáticos**. Fecha: **2026-08-05**. Alimenta el pendiente [01 · validadores + hooks](../pendientes/01-validadores-y-hooks.md). Es una foto: al agregar o cambiar reglas, se revisa.

## Criterio

> Si un script puede decir **sí/no sin opinar** → **validable**.
> Si dos personas pueden discutir si se cumplió → **se queda en el `.md`** (lo interpreta el agente).

Muchas reglas validables inspeccionan el **código/esquema/config del proyecto** o corren herramientas (linter, pruebas, audit de dependencias) → **necesitan un proyecto real con `proyectos/`**; no se pueden validar "en seco" sobre el estándar.

## Conteo

| Categoría | Cuántas |
|---|---|
| ✅ **Ya son validadores** | ~15 |
| 🟡 **Validables, faltan** | ~45 (casi todas necesitan un proyecto real) |
| 🔴 **No validables** (criterio humano) | ~93 |

---

## ✅ Ya son validadores (HECHAS)

| Regla | Validador | Comprueba |
|---|---|---|
| `G2` | `commits.py` | asunto con contenido, línea en blanco, idioma |
| `G3` | `versionado.py` | no versionar secretos/artefactos/config local |
| `G8` | `commits.py` | sin atribución de herramienta |
| `F13` | `sesion.py` | existe la carpeta `proyectos/` |
| `C18` | `sesion.py` | sync `CLAUDE.md` ↔ plantilla central |
| `F12.1/3/4/6/7/11/13` | `fases.py` | una fase = una HU · id único · nomenclatura · jerarquía · ruta física |
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
| `F12.2` | cada HU tiene ≥1 carpeta de fase | 🔶 |
| `F12.5` | consecutivo alfabético sin huecos/reinicios | 🔶 |
| `F12.12` | formato del nombre complementario (`D-B-EP-…`) por regex | 🔶 |
| `DOC1` | doc de cierre con secciones plan/pruebas/resultado | 🔶 |
| `DOC3` / `DOC11` | tabla de trazabilidad sin `❌` injustificados | 🔶 |
| `DOC7` | cruce bidireccional A↔B en §Historial cruzado | 🔶 |
| `DOC8` | cierre de análisis: tabla + banner + puntero en prompt vivo | 🔶 |
| `DOC10` | regla `P` numerada + banner si promovida + puntero de señal | 🔶 |
| `DOC12` | bloque de fase con campo ORIGEN (1 de 3) + réplica en el plan | 🔶 |
| `DOC13` | entradas de catálogo con campos mínimos | 🔶 |
| `DOC14` (formato) | link de 2 partes: texto=ruta absoluta, link=relativo `.md` | 🔶 |
| `DOC15` | README por carpeta del árbol · HU-NNN · sin placeholders `[…]` | 🔶 |
| `DOC16` | enlace bidireccional épica↔HU · toda HU con épica · EP-NNN | 🔶 |

### Código, datos, pruebas (`03`–`08`)

| Regla | Qué comprobaría | 🔶 |
|---|---|---|
| `03·D1` | columnas de auditoría + FK con política + índices/UNIQUE | 🔶 |
| `03·D2` | cada migración tiene `up` y `down` | 🔶 |
| `03·D3` | columna `NOT NULL` sin default en migración | 🔶 |
| `04·S3` | concatenación en SQL/shell, mass-assignment (regex/linter) | 🔶 |
| `04·S4` | `.env` en gitignore + plantilla + escaneo de secretos | 🔶 |
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
| `G4` | trabajo en rama ≠ principal, al día | 🔶 |
| `G6` | pipeline CI con pruebas + lint | 🔶 |
| `10·DEP2` | lockfile existe y está versionado | 🔶 |
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

Sobre el **estándar solo**, ya está prácticamente todo lo validable (las ~15 hechas). Para sumar las ~45 pendientes hace falta un **proyecto real con la estructura `proyectos/`** (agro-system o rni), porque validan artefactos del proyecto, no las plantillas base.
