# Funcionalidad implementada — Fase A-EP-004-HU-002-retrodocumentar-la-clasificacion-de-cada-regla (módulo Comprobación automática)

> **Veredicto de la fase: [No cumple](resultado_pruebas.md#6-veredicto-de-la-fase).** Cero reglas sin clasificar, cero rangos, y desde el registro se llega al programa. Pero **cuatro reglas escritas en `base/` no existen para el analizador**, y la clasificación **no detiene nada** ni corre en el trabajo normal.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-002-retrodocumentar-la-clasificacion-de-cada-regla` |
| **Módulo** | Comprobación automática — [`validadores/metareglas.py`](../../../../../validadores/metareglas.py) y [`validadores/reglas-validables.md`](../../../../../validadores/reglas-validables.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / exigencias cubiertas** | HU-002: CA-01, CA-02, CA-03 y sus dos transversales |
| **Fecha de cierre** | 2026-08-17 · **Commit** pendiente de autorización |

---

## 1. Qué se implementó — resumen

**Nada de programa: la fase escribió la prueba de la vuelta, que era la que faltaba.** El registro y su validador existen desde hace versiones, y `A-EP-001-HU-009` ya había bajado a cero las reglas sin clasificar. Lo que nadie había comprobado es **el otro sentido**: si el registro nombra cosas que el programa no reconoce.

Nombra nueve. Y ahí apareció el agujero.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| Registro con una fila por regla | documentación | [`reglas-validables.md`](../../../../../validadores/reglas-validables.md) — 205 entradas | ✅ Ya existía | CP-001 |
| Avisar la regla sin clasificar | programa | [`metareglas.py`](../../../../../validadores/metareglas.py) · `_fila18_clasificada` | ✅ Ya existía | CP-004 |
| La fila dice **qué programa** la comprueba | documentación | La tabla «Ya son validadores» | ✅ Ya existía | CP-003 |
| La derogada se conserva y no se le exige | programa | `_fila18_clasificada` salta las derogadas | ✅ Ya existía | Transversal |
| **Que el analizador vea todas las reglas** | programa | `reglas()` solo reconoce `## ` | ❌ **No existe** | CP-001 |
| **Que la clasificación detenga** | programa | Sale AVISO, y sin subcomando no corre | ❌ **No existe** | CP-004 |
| La comprobación en los dos sentidos | pruebas | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `ClasificacionDeCadaRegla` | ✅ Escrita acá | 8 pruebas |

### Criterios de aceptación

| CA | Cómo quedó | Estado |
|---|---|---|
| CA-01 | 0 sin clasificar y 0 rangos, **pero 4 reglas invisibles para el analizador** | ❌ |
| CA-02 | Las tres reglas probadas llegan a su programa leyendo solo el registro | ✅ |
| CA-03 | Avisa, no detiene, y no corre en el trabajo normal | ❌ |
| Transversal · Límites | La derogada se conserva marcada y no se le exige clasificación nueva | ✅ |
| Transversal · No regresión | La clasificación existente no se perdió al sumar reglas | ✅ |

---

## 3. Lo que la fase midió

| Medición, 2026-08-17 | Valor |
|---|---|
| Reglas que el analizador reconoce | **200** |
| Entradas del registro | **205** |
| Reglas sin clasificar | **0** |
| Entradas que nombran algo inexistente | **0** |
| Entradas que el analizador **no reconoce** | **9** — las 4 `CQ` del capítulo 16 y 5 sub-reglas de `F12` |
| Rangos en el registro | **0** |
| Subcomandos de `validar.py` | **24** — ninguno llama a `metareglas.py` |
| Módulos validadores que el registro no nombra | **10**, y ninguno es un hueco real |

---

## 4. El agujero, en una frase

**`metareglas.reglas()` solo reconoce lo que empieza por `## `.** Las cuatro reglas del capítulo 16 están escritas como `### CQ1 · …`, así que **no existen para el programa**: no se les aplica ninguna de las veinte filas del checklist —ni el molde, ni el identificador, ni las dependencias— y todo sale en verde.

Son justamente las reglas de **para quién se construye, seguridad por defecto y atributos de calidad**. Nunca han pasado por su propio procedimiento, y nadie lo notaría mirando la salida.

**No se arregló acá.** `metareglas.py` no está en los archivos que §2.1 del plan declara, y `02·F8` no deja salirse. Queda con su prueba en rojo esperado.

---

## 5. Decisiones y señales

| Decisión | Dónde quedó |
|---|---|
| La vuelta se comprueba **contra el texto de `base/`**, no contra lo que el analizador reconoce: si no, toda regla que el analizador no vea saldría como «inventada» y el defecto quedaría disfrazado de otra cosa | La prueba `test_el_registro_no_nombra_reglas_que_no_existan` |
| La regla de mentira del CA-03 se escribe **en una copia**: meterla en `base/` dejaría el repositorio con una regla que nadie aprobó | CP-004 del [resultado](resultado_pruebas.md) |
| Los diez módulos que el registro no nombra **se anotan y se distinguen**: no son huecos de clasificación, son programas que no comprueban reglas | §3 de este documento |

---

## 6. Lo que no entró, y dónde sigue

| Qué | Dónde |
|---|---|
| Que el analizador vea las reglas escritas con `###` y en viñeta (`D-01`) | Fase `B-EP-004-HU-002`, propuesta |
| Que `metareglas.py` tenga subcomando y que la regla sin clasificar sea falla (`D-02`) | La misma fase, que cierra el punto 2 del pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md) |
| El criterio de qué es comprobable | [HU-001](../../HU-001-criterio-de-lo-comprobable/HU-001-criterio-de-lo-comprobable.md) |

**La advertencia que deja esta fase:** el validador de las reglas lleva versiones diciendo «cero sin clasificar» y es cierto — de las que ve. Nadie había preguntado cuántas ve.
