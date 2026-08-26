# Funcionalidad implementada — Fase B-EP-004-HU-004-el-encuadre-de-la-plantilla-sobrevive-al-llenado   ·   `[CAPA 3]`

**Para qué sirve este documento.** Es el cierre de la fase: **qué quedó hecho, qué se probó, qué se decidió y qué deuda quedó**. El plan dice lo que se iba a hacer; esto dice lo que pasó, para poder comparar los dos.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-004-HU-004-el-encuadre-de-la-plantilla-sobrevive-al-llenado` |
| **Épica / HU** | [EP-004](../../epica.md) · [HU-004](../HU-004-forma-de-los-documentos.md) |
| **CA que cierra** | [CA-05](../HU-004-forma-de-los-documentos.md#ca-05--el-texto-fijo-de-la-plantilla-sobrevive-al-llenado) |
| **Fecha de cierre** | 2026-08-22 |
| **Veredicto** | [Cumple](resultado_pruebas.md#6-veredicto-de-la-fase) |

---

## 1. Qué se implementó — resumen

`validar.py plantilla` gana una quinta comprobación: **el texto que la plantilla fija antes de su primer separador tiene que sobrevivir al llenado**. Falla si el documento lo borró, y falla si lo reemplazó por una nota de procedencia, que es lo que se reconoce por traer una fecha que la plantilla no tiene ahí.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Exigencia | Dónde quedó | Prueba que lo cubre | Evidencia |
|---|---|---|---|
| [CA-05](../HU-004-forma-de-los-documentos.md#ca-05--el-texto-fijo-de-la-plantilla-sobrevive-al-llenado) | `plantillas.py`, comprobación 5 de `validar()` | CP-001, CP-002, CP-003, CP-005b | [resultado_pruebas.md](resultado_pruebas.md) §2 |
| RN-07 | `plantillas.bloque_fijo()` | CP-001, CP-004, CP-005c | Ídem |
| RN-08 | `_FECHA` y la segunda rama de la comprobación 5 | CP-003, CP-005 | Ídem |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué decía el plan | Qué se hizo |
|---|---|---|
| T-01 | Escribir `bloque_fijo(texto)` | Hecho. Con un ajuste que el plan no preveía: salta también las filas de tabla, o reprobaba 110 documentos |
| T-02 | Comprobar que el documento tenga bloque fijo si su plantilla lo tiene | Hecho |
| T-03 | Si la plantilla cita reglas ahí, exigir que el documento cite alguna | **Cambiado.** El criterio reprobaba un documento correcto, así que se sustituyó por la fecha en el bloque fijo. Medido antes de decidir: el solapamiento de vocabulario daba 31%, 17% y 11%, o sea que no separaba nada |
| T-04 | Escribir las pruebas | Hecho, y dos más que el plan no pedía: los dos defectos que la ejecución destapó |
| T-05 | Correr contra los documentos reales | Hecho. 650 revisados, 5 reprobados, ninguno por error del validador |
| T-06 | `CHANGELOG` y `VERSION` | Hecho, sobre `31.12.0`. El plan decía `31.10.0` y quedó viejo: otra sesión subió la versión a `31.11.0` mientras esta fase corría |

**Archivos tocados fuera de los que el plan declaraba:** ninguno, salvo `validadores/tests/test_plantillas_origen_regla.py`, que hubo que poner al día porque su fixture copiaba literal una línea del molde que la otra fase de la jornada cambió. Se anota acá porque [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md) pide que descubrir un archivo nuevo se reporte y no se edite en silencio.

---

## 3. Qué se probó  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Las dos suites que dependen de [`validadores/plantillas.py`](../../../../../validadores/plantillas.py), 14 pruebas, en verde. Más el barrido sobre los documentos reales del repositorio, que es lo que de verdad mide el riesgo de esta fase.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

```
python validadores/validar.py plantilla <documento.md>
python validadores/validar.py plantilla <documento.md> --contra plantillas/<molde>.md
```

La comprobación entra sola: no hay bandera que la active. Si el documento resuelve su plantilla y esa plantilla tiene texto fijo, se comprueba.

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md)

**El texto fijo se identifica por posición, no por su etiqueta.** La etiqueta cambió dos veces en un solo día: era «Encuadre para el agente» en el molde y quedó como «Para el agente» en el planteamiento de Cimiento. Un validador atado a una redacción reprueba lo que está bien apenas alguien corrige el molde.

**El criterio no es semántico, y se llegó a eso midiendo.** La primera idea era distinguir «instrucción de uso» de «nota de procedencia» por el vocabulario. Los tres casos reales dieron 31%, 17% y 11% de solapamiento con el molde: un umbral entre 11 y 17 es una moneda al aire. La fecha, en cambio, es mecánica, y en 650 documentos no dio un solo falso positivo.

**Lo que se comprueba es que esté y que no cuente procedencia, no que diga lo correcto.** Es el límite que el [pendiente 77](../../../../../pendientes/hecho/el-planteamiento-conserva-su-encuadre.md) se puso, y se respetó.

---

## 6. Deuda técnica y pendientes generados

| Qué queda | Dónde |
|---|---|
| Cinco planes de pruebas perdieron la línea fija de su molde | D-04 de [resultado_pruebas.md](resultado_pruebas.md) §4. Falta su pendiente |
| El molde del planteamiento todavía no declara su encuadre como texto fijo | [Fase C de EP-003 · HU-002](../../../EP-003-documentos-modelo-y-procedimientos/HU-002-modelos-del-encargo/C-EP-003-HU-002-el-planteamiento-se-reconstruye-igual/plan_trabajo.md), sin aprobar |
| La comprobación no se corre sola en ninguna batería: hay que invocarla por documento | Sin anotar. Es candidata a una fase de EP-004 · HU-008 |

---

## 7. Índices y mapas actualizados

- [HU-004](../HU-004-forma-de-los-documentos.md): CA-05, RN-07, RN-08 y la fila de esta fase en §8.
- El mapa del amarre de `validadores/` no se tocó, y su prueba ya fallaba antes de esta fase.

---

## 8. Despliegue — si aplica

No aplica. Es un validador que corre en la máquina de quien lo invoca.
