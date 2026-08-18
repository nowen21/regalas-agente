# Funcionalidad implementada — Fase A-EP-005-HU-001-retrodocumentar-la-transcripcion-de-la-sesion (módulo Automatismos)

> **Veredicto de la fase: [No cumple](resultado_pruebas.md#6-veredicto-de-la-fase).** Los tres CA numerados verificados —nace sola, la hora sale del reloj, entra al índice—. Falla el transversal de privacidad: **nada enmascara**, y la transcripción se versiona.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-005-HU-001-retrodocumentar-la-transcripcion-de-la-sesion` |
| **Módulo** | Automatismos — [`validadores/hook_historico.py`](../../../../../validadores/hook_historico.py) y [`historico.py`](../../../../../validadores/historico.py) |
| **Especificación del módulo** | [`documentacion/automatismos/spec.md`](../../../../automatismos/spec.md), §4.2 escrita en esta fase |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / exigencias cubiertas** | HU-001: CA-01, CA-02, CA-03 y sus tres transversales |
| **Fecha de cierre** | 2026-08-17 · **Commit** pendiente de autorización |

---

## 1. Qué se implementó — resumen

**Nada de programa: la fase escribió el incremento de la especificación y probó lo que se daba por hecho.** La transcripción se escribe sola desde hace versiones. Lo que faltaba era la prueba de que **la hora sale del reloj y no del texto**, y las seis reglas del comportamiento, que vivían solo en el código.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-17 · la escribe el programa | programa | [`hook_historico.py`](../../../../../validadores/hook_historico.py) | ✅ Ya existía | CP-001 |
| RN-18 · la hora sale del reloj | programa | [`historico.py`](../../../../../validadores/historico.py) · `anotar_usuario` | ✅ Ya existía | CP-002 |
| RN-19 · nace con el primer mensaje | programa | El mismo | ✅ Ya existía | CP-001 |
| RN-20 · no duplica | programa | El mismo | ✅ Ya existía | CP-003 |
| RN-21 · entra al índice y sobrevive al renombrado | programa | `_indexar`, `renombrar`, `_reindexar` | ✅ Ya existía | CP-004 |
| RN-22 · un proyecto sin la carpeta no se afecta | programa | `_archivo` no la crea | ✅ Ya existía | CP-001 |
| **Enmascarar antes de escribir** | programa | No existe | ❌ **No existe** | §3 del resultado |
| Las seis reglas, escritas | documentación | [`automatismos/spec.md`](../../../../automatismos/spec.md) §4.2 | ✅ **Escrito acá** | — |
| Las exigencias, con red | pruebas | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `TranscripcionDeLaSesion` | ✅ Escritas acá | 3 pruebas |

### Criterios de aceptación

| CA | Cómo quedó | Estado |
|---|---|---|
| CA-01 | Nace con el primer mensaje, no duplica, y no toca un proyecto sin la carpeta | ✅ |
| CA-02 | La hora sale del reloj, probado con un mensaje que contiene una hora falsa | ✅ |
| CA-03 | Entra al índice y sobrevive al renombrado | ✅ |
| Transversal · Privacidad | **Nada enmascara** | ❌ |
| Transversal · Límites · Errores | Sin la carpeta no escribe; no revienta y termina en 0 | ✅ |

---

## 3. La prueba que está escrita al revés, y por qué

El transversal de privacidad no se puede comprobar: **no hay con qué enmascarar**. Así que la prueba **afirma lo contrario de lo que se querría**: comprueba que el texto se guarda literal.

Escrita así, **falla el día que se construya el enmascarado** y obliga a volver a este documento. Escrita como un salto, ese día nadie se enteraría.

---

## 4. Decisiones y señales

| Decisión | Dónde quedó |
|---|---|
| El caso de la hora se arma con un mensaje que **contiene** una hora falsa: un programa que copiara el texto pasaría cualquier otro caso | CP-002 del [resultado](resultado_pruebas.md) |
| La prueba de privacidad se escribe al revés en vez de saltarse | §3 de este documento |
| El incremento de la especificación dice también **lo que todavía no hace** | `automatismos/spec.md` §4.2, última nota |

---

## 5. Lo que no entró, y dónde sigue

| Qué | Dónde |
|---|---|
| Enmascarar la clave antes de escribirla | [HU-002](../../HU-002-enmascarar-claves/HU-002-enmascarar-claves.md) — **bloqueada por dos dudas del usuario** |
| Que el resumen de la sesión nazca solo | [HU-008](../../HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md), ya cerrada |

**La advertencia que deja esta fase:** la transcripción es lo más fiel que tiene el repositorio —la escribe un programa, con la hora del reloj— y es también donde una clave pegada en el chat queda escrita en claro y versionada. La misma fidelidad que la hace útil la hace peligrosa.
