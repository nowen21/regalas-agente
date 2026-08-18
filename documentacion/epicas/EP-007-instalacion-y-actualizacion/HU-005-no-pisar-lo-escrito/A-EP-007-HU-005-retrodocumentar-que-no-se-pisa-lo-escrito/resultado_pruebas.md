# Resultado de pruebas — Fase A-EP-007-HU-005-retrodocumentar-que-no-se-pisa-lo-escrito

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-007-HU-005-retrodocumentar-que-no-se-pisa-lo-escrito` |
| **HU** | [HU-005](../HU-005-no-pisar-lo-escrito.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-007-HU-005 v1.0 |
| **Ciclo** | 1 · **Fecha** 2026-08-17 · **Ejecutado por** el agente, con el plan aprobado ese día |
| **Ambiente y versión** | Proyectos temporales con git, instalados y reinstalados de verdad. Estándar 23.3.0 |

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Veredicto de la fase: Cumple** (§6). De los 15 archivos que la instalación deja, **13 conservan lo que la persona les escriba**. Los otros dos son programa generado, se reemplazan a propósito, y el plan lo avisa.

---

## 2. Ejecución caso por caso

| Caso | CA | Prioridad | Con qué se probó | Resultado | Evidencia |
|---|---|---|---|---|---|
| [CP-001](plan_pruebas.md) | CA-01 | Crítica | Los 15 archivos, marcados uno por uno | Aprobado | EV-02 |
| [CP-002](plan_pruebas.md) | CA-01 | Crítica | El `CLAUDE.md` con una regla propia | Aprobado | EV-01 |
| [CP-003](plan_pruebas.md) | CA-02 | Alta | La lista de qué se reemplaza y qué se conserva | Aprobado | EV-02 |
| [CP-004](plan_pruebas.md) | CA-02 | Alta | El registro de versión tras actualizar | Aprobado | EV-01 |

---

### Detalle de CP-001 y CP-003 — Qué se conserva y qué se reemplaza

**Se probó de la forma más dura que admitía el caso:** se instaló un proyecto, se le escribió una marca propia a **todos** sus archivos, y se volvió a instalar.

| Resultado | Cuántos | Cuáles |
|---|---:|---|
| **Conservan la marca propia** | **13** | `.agente/stack.md` · `dominio.md` · `mapeo-nombres.md` · `marco-normativo.md` · `stack-instalacion.md` · `.claude/settings.json` · `.gitignore` · `CLAUDE.md` · `historico-chat/README.md` · `resumenes/README.md` · `memory/memory.md` · `documentacion/versiones/README.md` y su registro |
| **La pierden** | **2** | `.githooks/commit-msg` · `.githooks/pre-commit` |

**Los dos que se reemplazan son programa, no documento.** Son los guiones que corren al hacer un commit: nadie los llena, y una versión vieja del guion es un guion que comprueba mal. Reemplazarlos es lo correcto, y es **comportamiento definido**, que es lo que el transversal de límites pide.

**El resultado que importa: los cuatro documentos de la capa de proyecto —los que una persona llena a mano— están entre los 13 que se conservan.** Son los únicos que, perdidos, no se pueden reponer.

---

### Detalle de CP-002 — El `CLAUDE.md` con texto propio sobrevive

Se le agregó una regla propia al `CLAUDE.md` de un proyecto instalado y se volvió a instalar: **la regla sigue ahí**.

Es el caso más importante de la HU. El `CLAUDE.md` es a la vez generado desde una plantilla **y** el sitio donde el proyecto escribe sus reglas propias; un instalador que lo regenerara entero borraría la capa 3 del proyecto en cada actualización.

---

### Detalle de CP-004 — El registro dice qué se actualizó

Tras instalar queda `documentacion/versiones/<fecha>-<version>.md`, y **nombra la versión del estándar** con la que se instaló. Es lo que permite responder «¿desde cuándo este proyecto cumple qué?» sin adivinar.

---

### El aviso, y lo que le falta

El transversal de límites pide que el archivo modificado que el estándar considera generado tenga **comportamiento definido y se avise**. Las dos cosas ocurren:

| Estado del archivo | Qué dice el plan |
|---|---|
| Intacto | `(simulado) commit-msg ya estaba al día` |
| Modificado a mano | `(simulado) escribir .githooks\commit-msg` |

**Se avisa:** quien lea el plan ve que ese archivo va a cambiar. **Lo que el aviso no distingue** es escribirlo por primera vez de pisar lo que alguien escribió — la palabra es la misma. Queda como observación `D-01`, no como incumplimiento: el criterio pide avisar, y avisa.

> **Se estuvo a punto de anotarlo como defecto.** La primera medición solo buscó la línea del enganche en la salida y la encontró igual; comparar las dos corridas enteras mostró que sí cambia. **Medir una línea no es medir el comportamiento.**

---

## 3. Verificaciones manuales

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Cuántos archivos conservan lo propio | Marcando **los 15** y reinstalando | **13 conservan · 2 no** |
| 2 | Que los dos que se pierden sean programa | Mirándolos | Los dos guiones de `.githooks/` |
| 3 | Que el plan distinga intacto de modificado | Comparando las dos simulaciones enteras | **Distingue** |
| 4 | Que la suite siga verde | `python validadores/pruebas.py` | 330 pruebas · verde, con 6 fallos esperados |

---

## 4. Defectos encontrados

| ID | Severidad | Qué es | Dónde queda |
|---|---|---|---|
| D-01 | Baja | El aviso de que se va a reemplazar un archivo **no distingue** «escribir por primera vez» de «pisar lo que escribiste»: la palabra es la misma | Anotado. No deja ningún CA en «No»: el criterio pide avisar, y avisa |
| D-02 | Baja | El plan de pruebas declara cobertura completa y **no le escribe caso a los dos transversales**. Se probaron igual, y por eso apareció `D-01` | El plan aprobado no se modifica. Mismo defecto de molde de las 51 fases |

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-005-no-pisar-lo-escrito.md#ca-01--un-documento-llenado-por-la-persona-no-se-pierde) | CP-001, CP-002 | **13 de 15** conservan lo propio, y entre ellos están los cuatro documentos que una persona llena | Sí |
| [CA-02](../HU-005-no-pisar-lo-escrito.md#ca-02--las-secciones-nuevas-se-agregan-sin-tocar-lo-viejo) | CP-003, CP-004 | Lo nuevo se agrega y lo viejo queda; el registro nombra la versión | Sí |
| Transversal · Límites | Verificaciones 1 a 3 | Los dos generados **se reemplazan** —comportamiento definido— y el plan lo dice | Sí, con `D-01` |
| Transversal · Errores | CP-001 | No pisa lo que no está seguro de poder regenerar: los 13 se conservan sin excepción | Sí |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Meta | Resultado | Cumple |
|---|---|---|---|
| Cobertura de exigencias | 100% | 100% de lo que el plan contó, más los dos transversales | Sí |
| Casos ejecutados | 4 de 4 | 4 de 4 | Sí |
| Documentos llenados por la persona que se pierdan | **0** | **0** | Sí |
| Lista de qué se reemplaza y qué se conserva | Escrita | Escrita, con los 15 | Sí |

---

## 6. Veredicto de la fase

**Concepto:** **Cumple.**

**Justificación:** los dos criterios quedaron verificados de la forma más dura que admitía la prueba —marcando **los quince archivos** y reinstalando— y los dos transversales también. De quince, trece conservan lo que la persona escriba, y los dos que no son los guiones de git: programa generado, donde una versión vieja comprueba mal. Los cuatro documentos de la capa de proyecto, que son los únicos irreponibles, están entre los conservados.

**Qué falta para que cumpla:** nada. Queda una observación (`D-01`): el aviso no distingue escribir de pisar.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Casos automatizados | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `NoPisarLoEscrito`: 5 pruebas, en verde |
| EV-02 | La lista de los quince | §2 de este documento |
| EV-03 | Corrida completa | `python validadores/pruebas.py` — 330 pruebas, verde, 6 fallos esperados |

---

## 8. Ciclos anteriores

Ninguno: es el primero.
