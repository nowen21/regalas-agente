# Resultado de pruebas — Fase A-EP-001-HU-008-retrodocumentar-la-derogacion

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-001-HU-008-retrodocumentar-la-derogacion` |
| **HU** | [HU-008](../HU-008-derogacion-sin-borrar.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-001-HU-008 v1.0 |
| **Ciclo** | 1 · **Fecha** 2026-08-17 · **Ejecutado por** el agente, con el plan aprobado ese día |
| **Ambiente y versión** | Este repositorio: las **ocho derogaciones** reales. Estándar 23.3.0 |

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 6 | 6 | 6 | 0 | 0 | 0 |

**Veredicto de la fase: Cumple** (§6). Las ocho derogaciones conservan su texto, dicen desde cuándo y por cuál, ningún identificador liberado volvió como regla vigente, y a ninguna se le reclama nada.

---

## 2. Ejecución caso por caso

| Caso | CA | Prioridad | Con qué se probó | Resultado | Evidencia |
|---|---|---|---|---|---|
| [CP-001](plan_pruebas.md) | CA-01 | Crítica | Las ocho derogaciones | Aprobado | EV-01 |
| [CP-002](plan_pruebas.md) | CA-01 | Alta | La marca de cada una, y su reemplazo | Aprobado | EV-01 |
| [CP-003](plan_pruebas.md) | CA-02 | Crítica | Las ocho contra las reglas vigentes | Aprobado | EV-01 |
| [CP-004](plan_pruebas.md) | CA-02 | Alta | El consecutivo de los capítulos | Aprobado | EV-02 |
| [CP-005](plan_pruebas.md) | CA-03 | Alta | La cuenta de incumplimientos | Aprobado | EV-01 |
| [CP-006](plan_pruebas.md) | — | Media | La suite entera | Aprobado | EV-03 |

---

### Detalle de CP-001 y CP-002 — Las ocho, con su marca y su reemplazo

| Desde | Derogada | Reemplazada por | ¿Su texto sigue? |
|---|---|---|---|
| `3.1.0` | `F4.1` | `F14` | Sí |
| `3.1.0` | `F4.2` | `F15` | Sí |
| `3.1.0` | `F4.3` | `F16` y `F17` | Sí |
| `3.1.0` | `F4.4` | `F18` | Sí |
| `3.1.0` | `F4.5` | `F19` y `F20` | Sí |
| `4.0.0` | `F6` | `13·DOC1` | Sí |
| `4.0.0` | `F7` | `13·DOC3` | Sí |
| `6.0.0` | `ID2` | `00·ID7` | Sí |

**Las ocho conservan su cuerpo**, y las ocho dicen **desde qué versión** y **por cuál**. Y se comprobó lo que suele faltar: **que el reemplazo exista**. Una derogación que remite a una regla inventada manda a buscar lo que no está, y se ve igual de bien escrita que una correcta.

**Por qué no se borran.** Las especificaciones, los commits y las fases cerradas citan las reglas por identificador. Borrar `F4.1` rompería toda cita a `F4.1` **sin dejar rastro**: el enlace deja de resolver y nadie sabe qué decía.

---

### Detalle de CP-003 y CP-004 — El identificador liberado no vuelve

**Ninguno de los ocho aparece además como regla vigente.** Y esto es más grave que borrar: si `F6` volviera como una regla nueva, toda cita vieja a `F6` **seguiría resolviendo** — a otra cosa. El enlace funcionaría, el documento se vería sano, y diría algo que nadie escribió.

**El consecutivo de cada capítulo tampoco los toma:** el capítulo de flujo va por `F23` y nunca reutilizó los cinco `F4.x` ni `F6` ni `F7`; el de identidad va más allá de `ID2`. Los huecos quedan como historia, que es lo que [`20·M11`](../../../../../base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md) manda.

---

### Detalle de CP-005 — La derogada no cuenta como incumplimiento

Se corrió el validador de meta-reglas y se buscó si alguna de las ocho aparece reclamada: **ninguna**. No se les exige checklist al día, ni clasificación de validable, ni molde.

**Es lo correcto:** una regla derogada no tiene que cumplir el procedimiento de las vigentes. Reclamárselo obligaría a mantener al día algo que ya no manda, y el ruido acabaría en que nadie lee los hallazgos.

---

### Detalle de CP-006 — Qué mitad la comprueba un programa que corre

**Es la salvedad que esta fase deja escrita**, y la pedía su tarea `T-06`:

| Qué se comprueba | Con qué | ¿Corre en el trabajo normal? |
|---|---|---|
| Que la derogada conserve su texto y su marca | Las pruebas de esta fase | **Sí**, con la suite |
| Que el identificador no vuelva | Las pruebas de esta fase | **Sí** |
| Que no se le reclame nada | `metareglas.py` | **No**: no tiene subcomando en `validar.py` |
| Que una derogación sin adoptar detenga la fase (`02·F22`) | `versiones.py` | Sí |

**La tercera fila es el hueco.** `metareglas.py` funciona y **no se ejecuta** salvo que alguien lo invoque desde Python — es el punto 2 del [pendiente 53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md), y el mismo que dejó en «No» el CA-03 de [`A-EP-004-HU-002`](../../../EP-004-comprobacion-automatica/HU-002-marca-de-comprobable-en-cada-regla/A-EP-004-HU-002-retrodocumentar-la-clasificacion-de-cada-regla/resultado_pruebas.md).

**Acá no deja el CA en «No»**, porque lo que el CA-03 pide —que no se cuente como incumplimiento— **se cumple**: la prueba de esta fase lo comprueba en cada corrida de la suite, que sí se ejecuta.

---

## 3. Verificaciones manuales

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Cuántas derogaciones hay | `version.derogaciones()` | **8** |
| 2 | Que las ocho conserven su texto | Buscándolas en `base/` | Las ocho |
| 3 | Que el reemplazo de cada una exista | Buscando el identificador que nombra | Los ocho existen |
| 4 | Que ninguna sin reemplazo | Recorriéndolas | **Ninguna**: el caso «sin reemplazo» no ha ocurrido nunca |
| 5 | Que la suite siga verde, con su número | `python validadores/pruebas.py` | **357 pruebas** · verde, con 7 fallos esperados |

---

## 4. Defectos encontrados

| ID | Severidad | Qué es | Dónde queda |
|---|---|---|---|
| D-01 | Baja | La vigilancia de que no se le reclame nada a una derogada vive en `metareglas.py`, que **no tiene punto de entrada** | Ya anotado: punto 2 del [pendiente 53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md). No deja el CA-03 en «No» porque la prueba de esta fase sí corre con la suite |
| D-02 | Baja | El plan de pruebas declara cobertura completa y **no le escribe caso a los dos transversales**. Se probaron igual | El plan aprobado no se modifica. Mismo defecto de molde de las 51 fases |

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-008-derogacion-sin-borrar.md#ca-01--una-regla-derogada-sigue-siendo-legible) | CP-001, CP-002 | Las ocho conservan su texto, dicen desde cuándo y por cuál, **y el reemplazo existe** | Sí |
| [CA-02](../HU-008-derogacion-sin-borrar.md#ca-02--un-identificador-liberado-no-se-reutiliza) | CP-003, CP-004 | Ninguno volvió como vigente; el consecutivo no los toma | Sí |
| [CA-03](../HU-008-derogacion-sin-borrar.md#ca-03--una-regla-derogada-no-se-cuenta-como-incumplimiento) | CP-005 | A ninguna se le reclama nada | Sí |
| Transversal · Límites | Verificación 4 | Las ocho tienen reemplazo. **El caso «sin reemplazo» no ha ocurrido**, y queda dicho en vez de darse por bueno | Sí, con la salvedad escrita |
| Transversal · No regresión | CP-006 | Las 357 pruebas en verde: derogar no reabrió nada | Sí |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Meta | Resultado | Cumple |
|---|---|---|---|
| Cobertura de exigencias | 100% | 100% de lo que el plan contó, más los dos transversales | Sí |
| Casos ejecutados | 6 de 6 | 6 de 6 | Sí |
| Derogaciones sin su texto | **0** | **0** de 8 | Sí |
| Identificadores derogados que vuelven | **0** | **0** | Sí |
| Pruebas de la suite, con su número | Las 246 más las nuevas | **357**, en verde | Sí |

---

## 6. Veredicto de la fase

**Concepto:** **Cumple.**

**Justificación:** los tres criterios quedaron verificados sobre las ocho derogaciones reales, y los dos transversales también. Lo que más valía comprobar es el CA-02, porque su incumplimiento sería **invisible**: si un identificador derogado volviera como regla vigente, toda cita vieja seguiría resolviendo —a otra cosa—, el enlace funcionaría y el documento se vería sano. Ninguno volvió.

Y se comprobó algo que el plan no pedía y que suele faltar: **que el reemplazo de cada derogación exista**. Una que remita a una regla inventada se ve igual de bien escrita que una correcta.

**Qué falta para que cumpla:** nada. Queda escrito, con la salvedad de que el caso «derogación sin reemplazo» **no ha ocurrido nunca** — se dice, en vez de darlo por resuelto.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Casos automatizados | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `DerogacionSinBorrar`: 5 pruebas, en verde |
| EV-02 | La tabla de las ocho | §2 de este documento |
| EV-03 | Corrida completa | `python validadores/pruebas.py` — **357 pruebas**, verde, 7 fallos esperados |

---

## 8. Ciclos anteriores

Ninguno: es el primero.
