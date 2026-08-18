# Funcionalidad implementada — Fase A-EP-004-HU-006-retrodocumentar-la-comprobacion-de-la-estructura (módulo Comprobación automática)

> **Veredicto de la fase: [Cumple](resultado_pruebas.md#7-veredicto-de-la-fase).** Los tres criterios verificados, los dos transversales también, y quedó escrito por primera vez **qué parte de `F12` comprueba el programa y qué parte no**, con el motivo de cada exclusión.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-006-retrodocumentar-la-comprobacion-de-la-estructura` |
| **Módulo** | Comprobación automática — [`validadores/fases.py`](../../../../../validadores/fases.py) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / exigencias cubiertas** | HU-006: CA-01, CA-02, CA-03 y sus dos transversales |
| **Fecha de cierre** | 2026-08-17 · **Commit** pendiente de autorización |

---

## 1. Qué se implementó — resumen

**Nada de programa: la fase escribió el caso que faltaba y el documento que no existía.** `fases.py` ya comprobaba los tres criterios y tenía once pruebas. Lo que no había era el caso del CA-03 —que la fase incompleta **diga cuáles** documentos le faltan— ni ninguna constancia de qué parte de `F12` se comprueba.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| `F12.6` · nombre de la fase | programa | [`fases.py`](../../../../../validadores/fases.py) | ✅ Ya existía | CP-001 |
| `F12.1` · una fase, una HU | programa | El mismo | ✅ Ya existía | CP-001 |
| `F12.5` · consecutivo sin huecos ni repetidos | programa | El mismo | ✅ Ya existía | CP-002 |
| `F12.13` · los cinco documentos, **nombrando cuáles faltan** | programa | El mismo | ✅ Ya existía | CP-003 |
| Los tres bordes vacíos | programa | El mismo | ✅ Ya existía | Transversal |
| **Qué se comprueba de `F12` y qué no** | documentación | [`docs/fases.md`](../../../../../validadores/docs/fases.md) | ✅ **Escrito acá** | — |
| Los cinco casos, con red | pruebas | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `EstructuraYNomenclatura` | ✅ Escritas acá | 5 pruebas |

### Criterios de aceptación

| CA | Cómo quedó | Estado |
|---|---|---|
| CA-01 | Nombre mal armado y fase bajo la HU equivocada: falla. Complemento válido y ancho de números: no se reportan | ✅ |
| CA-02 | Hueco: aviso. Letra repetida: falla. Consecutivo contiguo: nada | ✅ |
| CA-03 | Se reporta **nombrando los cuatro** que faltan, sin nombrar el que está | ✅ |
| Transversal · Límites | Épica sin HU y HU sin fases avisan; árbol sin `epicas/` falla; ninguno revienta | ✅ |
| Transversal · No regresión | Tres fases cerradas siguen sin producir hallazgos | ✅ |

---

## 3. Lo que la fase midió

| Medición, 2026-08-17 | Valor |
|---|---|
| Avisos de `validar.py fases` cuando se escribió el plan | 54 |
| Al empezar a ejecutar | 53 |
| Al cerrar esta fase | **45** |
| De esos 45, cuántos son de documentos faltantes | **45** — todos |
| Fallas de estructura | **0** |

**El número bajó nueve mientras se medía**, porque nueve fases se ejecutaron esta sesión y estrenaron sus dos documentos. Queda anotado así, con los tres momentos: **no es una línea base estable, es un contador de trabajo pendiente**, y cada fase que cierra lo baja en uno. Escribirlo como cifra fija habría envejecido en horas.

---

## 4. Lo que quedó escrito, y por qué importa

Hasta hoy, qué comprueba `fases.py` de `F12` se sabía leyendo el programa. Ahora está en [`docs/fases.md`](../../../../../validadores/docs/fases.md), y lo que más valor tiene es **la lista de lo que no comprueba, con el motivo**:

| No se comprueba | Por qué |
|---|---|
| `F12.10` · que la fase sea trabajo real y no relleno de nomenclatura | Es criterio: dos personas pueden discutir si una fase «representa un trabajo real» |
| El **contenido** de los cinco documentos | Cada uno tiene su validador: `flujo`, `trazabilidad`, `plantilla` |
| Que las letras sigan el orden cronológico | La letra es consecutivo, no cronología |

Y por qué `F12.13` avisa en vez de fallar: **una fase en curso tiene que poder existir sin sus cinco documentos**, porque los dos últimos salen de ejecutarla. Reprobar por eso convertiría todo trabajo en marcha en un incumplimiento.

---

## 5. Decisiones y señales

| Decisión | Dónde quedó |
|---|---|
| La línea base se anota con **los tres momentos y el motivo del cambio**, no como una cifra fija | §3 de este documento y §3 del [resultado](resultado_pruebas.md) |
| El caso del CA-03 comprueba también **que no nombre el documento que sí está**: sin eso, una lista genérica pasaría igual | CP-003 |
| Los bordes se prueban con árboles de mentira, no tocando `documentacion/epicas/` | Clase `EstructuraYNomenclatura` |

---

## 6. Lo que no entró, y dónde sigue

| Qué | Dónde |
|---|---|
| Que la corrida cuente las HU sin fase | [HU-017](../../HU-017-inventario-de-hu-sin-fase/HU-017-inventario-de-hu-sin-fase.md) |
| Comparar los dos veredictos de una fase | [HU-014](../../HU-014-un-solo-veredicto-por-fase/HU-014-un-solo-veredicto-por-fase.md), ya cerrada |

**Lo que deja esta fase:** de las nueve ejecutadas hasta ahora, es la primera que cierra en «Cumple». Y no porque se le exigiera menos: porque lo que la HU pedía **ya estaba construido y bien**, y lo único que faltaba era probarlo y escribirlo.
