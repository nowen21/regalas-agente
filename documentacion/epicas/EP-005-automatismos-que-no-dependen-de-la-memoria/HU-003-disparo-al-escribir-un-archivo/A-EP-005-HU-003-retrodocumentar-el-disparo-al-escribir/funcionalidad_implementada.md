# Funcionalidad implementada — Fase A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir (módulo Automatismos)

> **Veredicto de la fase: [No cumple](resultado_pruebas.md#6-veredicto-de-la-fase).** El disparo corre en el momento y calla con lo que no le toca. Falla el CA-03: pide que el hallazgo grave **detenga**, y hoy todo avisa.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir` |
| **Módulo** | Automatismos — [`validadores/hook_md.py`](../../../../../validadores/hook_md.py) |
| **Especificación del módulo** | [`documentacion/automatismos/spec.md`](../../../../automatismos/spec.md), §4.3 escrita en esta fase |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / exigencias cubiertas** | HU-003: CA-01, CA-02, CA-03 y sus tres transversales |
| **Fecha de cierre** | 2026-08-17 · **Commit** pendiente de autorización |

---

## 1. Qué se implementó — resumen

**Nada de programa: la fase escribió el incremento y probó el silencio.** El disparo existe desde hace versiones. Lo que faltaba era la prueba de que **callar no es lo mismo que no ejecutarse**, y la constancia de que el CA-03 nunca se construyó.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-23 · corre al escribir, en el momento | programa | [`hook_md.py`](../../../../../validadores/hook_md.py) | ✅ Ya existía | CP-001 |
| RN-24 · calla con lo que no le toca, y corre igual | programa | El mismo | ✅ Ya existía | CP-002 |
| RN-25 · el archivo que ya no está no lo revienta | programa | El mismo | ✅ Ya existía | Transversal |
| RN-26 · el disparo no se nota | programa | El mismo | ✅ Ya existía | Transversal |
| **Que el hallazgo grave detenga** | programa | No existe: todo avisa | ❌ **No existe** | CP-003 |
| Las cuatro reglas, escritas | documentación | [`automatismos/spec.md`](../../../../automatismos/spec.md) §4.3 | ✅ **Escrito acá** | — |
| Las exigencias, con red | pruebas | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `DisparoAlEscribirUnArchivo` | ✅ Escritas acá | 4 pruebas |

### Criterios de aceptación

| CA | Cómo quedó | Estado |
|---|---|---|
| CA-01 | Avisa en el momento y nombra el problema | ✅ |
| CA-02 | Calla, y se comprueba que corrió igual | ✅ |
| CA-03 | **Todo avisa. Nada detiene** | ❌ |
| Transversal · Rendimiento · Errores | Por debajo de 5 s; el archivo ausente no lo revienta | ✅ |
| Transversal · Reversibilidad | **No aplica hoy**: sin detención no hay archivo a medias | N/A |

---

## 3. La prueba del silencio, que es la que valía la pena

Que el enganche **calle** y que **no se haya ejecutado** se ven idénticos desde fuera: salida vacía en los dos casos.

El caso los separa mirando el **código de salida**: si no hubiera corrido, no habría código que mirar. Sin ese detalle, el CA-02 se podría dar por bueno con un enganche que ni siquiera está registrado.

---

## 4. Lo que no cumple, y por qué importa

El CA-03 dice «el hallazgo grave detiene; el resto avisa». Hoy **hace lo mismo con los dos: avisar**.

**Un aviso depende de que alguien lo lea.** Este repositorio tiene la constancia: `00·ID8` llegaba completa al abrir la sesión el 2026-08-14, y se incumplió durante toda la sesión igual. Lo que la HU quería es que un documento con un incumplimiento grave **no se pueda dejar así**.

**No se arregló acá:** `hook_md.py` no está en los archivos que §2.1 del plan declara.

---

## 5. Decisiones y señales

| Decisión | Dónde quedó |
|---|---|
| El silencio se prueba mirando el **código de salida**, no solo la salida vacía | §3 de este documento |
| El transversal de reversibilidad se marca **N/A con su motivo**, no se da por cumplido: sin detención no hay nada que revertir | §5 del [resultado](resultado_pruebas.md) |
| El incremento de la especificación dice también **lo que todavía no hace** | `automatismos/spec.md` §4.3, última nota |

---

## 6. Lo que no entró, y dónde sigue

| Qué | Dónde |
|---|---|
| Que el hallazgo grave detenga (`D-01`) | Fase `B-EP-005-HU-003`, propuesta |
| El formato del hallazgo y sus severidades | [EP-004 · HU-003](../../../EP-004-comprobacion-automatica/HU-003-formato-del-hallazgo/HU-003-formato-del-hallazgo.md) |

**La advertencia que deja esta fase:** el disparo hace bien la parte barata —avisar rápido— y le falta la cara: detener. Y detener es lo único que convierte una regla escrita en una regla que se cumple.
