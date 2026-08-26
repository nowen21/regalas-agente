# Funcionalidad implementada — Fase A-EP-007-HU-005-retrodocumentar-que-no-se-pisa-lo-escrito (módulo Instalación)

> **Veredicto de la fase: [Cumple](resultado_pruebas.md#6-veredicto-de-la-fase).** De los 15 archivos que la instalación deja, **13 conservan lo que la persona les escriba**. Los dos que no son los guiones de git: programa generado, y el plan avisa que los va a reescribir.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-007-HU-005-retrodocumentar-que-no-se-pisa-lo-escrito` |
| **Módulo** | Instalación — [`validadores/instalar.py`](../../../../../validadores/instalar.py) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / exigencias cubiertas** | HU-005: CA-01, CA-02 y sus dos transversales |
| **Fecha de cierre** | 2026-08-17 · **Commit** pendiente de autorización |

---

## 1. Qué se implementó — resumen

**Nada de programa: la fase levantó la lista que faltaba.** Que el instalador no pise lo escrito se sabía por partes —había casos sueltos del `CLAUDE.md` y del `.gitignore`—, pero **nadie había hecho la lista completa** de qué se conserva y qué se reemplaza.

Ahora está, y salió de marcar los quince archivos y reinstalar.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| No perder lo que la persona llenó | programa | [`instalar.py`](../../../../../validadores/instalar.py), en cada paso | ✅ Ya existía | CP-001 |
| Agregar lo nuevo sin tocar lo viejo | programa | `instalar_claude_md`, `instalar_gitignore` | ✅ Ya existía | CP-002 |
| Reemplazar lo que es programa generado | programa | `instalar_git` | ✅ Ya existía | CP-003 |
| Avisar de lo que se va a reescribir | programa | El plan distingue «ya estaba al día» de «escribir» | ✅ Ya existía | Transversal |
| El registro nombra la versión | programa | `instalar_registro` | ✅ Ya existía | CP-004 |
| **La lista de los quince** | documentación | §2 del [resultado_pruebas.md](resultado_pruebas.md) | ✅ **Escrita acá** | CP-003 |
| Las cuatro exigencias, con red | pruebas | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `NoPisarLoEscrito` | ✅ Escritas acá | 5 pruebas |

### Criterios de aceptación

| CA | Cómo quedó | Estado |
|---|---|---|
| CA-01 | 13 de 15 conservan lo propio, y entre ellos los cuatro que una persona llena | ✅ |
| CA-02 | Lo nuevo se agrega y lo viejo queda; el registro nombra la versión | ✅ |
| Transversal · Límites | Los dos generados se reemplazan, y el plan lo dice | ✅ con `D-01` |
| Transversal · Errores | No pisa lo que no puede regenerar | ✅ |

---

## 3. La lista, que es lo que la fase deja

| | Cuántos | Cuáles |
|---|---:|---|
| **Se conservan** | **13** | Los cuatro de `.agente/` llenados a mano, `stack-instalacion.md`, `.claude/settings.json`, `.gitignore`, `CLAUDE.md`, los tres del histórico y la memoria, y los dos de `documentacion/versiones/` |
| **Se reemplazan** | **2** | `.githooks/commit-msg` y `.githooks/pre-commit` |

**Los dos que se reemplazan son programa, no documento.** Corren al hacer un commit; nadie los llena, y una versión vieja del guion comprueba mal. **Los cuatro documentos que una persona llena a mano están entre los conservados**, que es lo único irreponible.

---

## 4. La observación que queda

El aviso existe y distingue: con el archivo intacto el plan dice «commit-msg ya estaba al día»; modificado, dice «escribir .githooks/commit-msg». **Lo que no distingue es escribir de pisar** — la palabra es la misma.

No es incumplimiento: el criterio pide avisar, y avisa. Queda como `D-01`.

> **Se estuvo a punto de anotarlo como defecto.** La primera medición buscó solo la línea del enganche en la salida y la encontró igual en los dos casos. Comparar las **dos corridas enteras** mostró que sí cambia. Medir una línea no es medir el comportamiento, y la diferencia entre las dos formas de mirar era un «No cumple» falso.

---

## 5. Decisiones y señales

| Decisión | Dónde quedó |
|---|---|
| Se marcan **los quince archivos**, no una muestra: la lista completa es lo que la fase venía a levantar, y una muestra habría dejado fuera justo los dos que se pierden | CP-001 del [resultado](resultado_pruebas.md) |
| Reemplazar los guiones de git **está bien** y se dice por qué: son programa, y uno viejo comprueba mal | §3 de este documento |
| El aviso se anota como observación, no como defecto: el criterio pide avisar, y avisa | `D-01` |

---

## 6. Lo que no entró, y dónde sigue

| Qué | Dónde |
|---|---|
| Que el aviso distinga escribir de pisar (`D-01`) | Sin destino. Es de redacción del plan, no de comportamiento |
| Que la simulación anuncie el registro de versión | `D-01` de [HU-002](../../HU-002-mostrar-antes-de-hacer/A-EP-007-HU-002-retrodocumentar-el-mostrar-antes-de-hacer/resultado_pruebas.md) |
| Poner al día lo ya instalado | [HU-006](../../HU-006-poner-al-dia/HU-006-poner-al-dia.md), ya cerrada |

**Lo que deja esta fase:** hasta hoy «el instalador no pisa lo escrito» era una afirmación con dos ejemplos. Ahora es una lista de quince filas donde se ve exactamente cuáles dos se pierden y por qué está bien que se pierdan.
