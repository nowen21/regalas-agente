# Resultado de Pruebas — Fase B-EP-004-HU-004-el-encuadre-de-la-plantilla-sobrevive-al-llenado   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie. El plan de pruebas se queda como se aprobó; acá va lo que pasó al correrlo.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-004-HU-004-el-encuadre-de-la-plantilla-sobrevive-al-llenado` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), PP-B-EP-004-HU-004 v1.0 |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente |
| **Ambiente** | El repositorio, en la máquina del usuario. Sin datos reales |

---

## 1. Resumen de la ejecución

| Métrica | Meta del plan | Resultado |
|---|---|---|
| Exigencias con al menos un caso | 4 de 4 | 4 de 4 |
| Casos ejecutados | 7 de 7 | 9 de 9, dos más de los planeados |
| Casos en verde | 7 de 7 | 9 de 9 |
| Documentos reales reprobados estando bien | 0 | 0, después de dos correcciones |
| Pruebas que antes pasaban y ahora fallan | 0 | 0 en las suites que la fase toca |

**Los dos casos de más** salieron de los defectos que la ejecución destapó, y quedaron escritos como prueba para que no vuelvan: CP-005b y CP-005c en [`test_encuadre_de_la_plantilla.py`](../../../../../validadores/tests/test_encuadre_de_la_plantilla.py).

---

## 2. Ejecución caso por caso

| Caso | Qué se corrió | Qué salió | Concepto |
|---|---|---|---|
| CP-001 | Documento sin el bloque fijo, contra una plantilla que sí lo tiene | Una falla, con el texto que la plantilla pone ahí | Pasa |
| CP-002 | Encuadre reescrito, más corto, adaptado | Ninguna falla | Pasa |
| CP-003 | El caso real: nota de procedencia con fecha, fuentes y número de pendiente | Una falla, diciendo que ahí se contó de dónde salió el documento | Pasa |
| CP-004 | Plantilla sin bloque fijo | Ninguna falla | Pasa |
| CP-005 | Plantilla con bloque fijo que no cita reglas | Ninguna falla | Pasa |
| CP-005b | El encuadre de `planteamiento.md`, que deletrea la cadena en palabras | Ninguna falla | Pasa, después de corregir el criterio |
| CP-005c | Un documento con su tabla de ficha antes del separador | La tabla no se toma como texto fijo | Pasa, después de corregir `bloque_fijo` |
| CP-006 | Las dos suites que importan `plantillas`: 14 pruebas | Todas en verde | Pasa |
| CP-007 | Barrido sobre los documentos del repositorio que resuelven su plantilla | 650 revisados, 5 reprobados, ninguno por error | Pasa |

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Los 5 documentos que el CP-007 reprobó se abrieron uno por uno.** Los cinco son planes de pruebas a los que les falta de verdad la línea fija de su molde:

- `EP-002 · HU-002 · B` · plan_pruebas.md
- `EP-003 · HU-004 · B` · plan_pruebas.md
- `EP-003 · HU-010 · B` · plan_pruebas.md
- `EP-005 · HU-001 · B` · plan_pruebas.md
- `EP-005 · HU-011 · A` · plan_pruebas.md

Ninguno es un error del validador. Quedan como hallazgo en §4.

**Ningún dato real se tocó:** los casos escriben sus documentos en carpeta temporal, y el barrido solo lee.

---

## 4. Defectos encontrados

| ID | Caso | Severidad | Qué pasó | Estado |
|---|---|---|---|---|
| D-01 | CP-007 | Crítica | El criterio inicial, exigir que el bloque fijo citara una regla, reprobó [`planteamiento.md`](../../../../../planteamiento.md), que dice exactamente lo que debe decir pero deletrea la cadena en palabras | **Corregido.** Se midió el solapamiento de vocabulario como alternativa y dio 31%, 17% y 11% en los tres casos reales, o sea que no discrimina. El criterio pasó a ser la fecha en el bloque fijo |
| D-02 | CP-007 | Crítica | `bloque_fijo()` contaba las filas de la tabla de ficha, que trae una fila `Fecha`. Reprobaba 110 documentos | **Corregido.** La función salta las líneas que abren con `\|`. Queda cubierto por CP-005c |
| D-03 | CP-006 | Alta | `test_plantillas_origen_regla` falló: su fixture copia literal una línea del molde de la especificación, que la otra fase de esta jornada cambió | **Corregido.** El fixture se puso al día con el molde |
| D-04 | CP-007 | Media | Cinco planes de pruebas del repositorio perdieron la línea fija de su molde | **Abierto.** Es un hallazgo del validador, no un defecto suyo. Se anota y se corrige aparte |

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia | Casos | Concepto |
|---|---|---|
| [CA-05](../HU-004-forma-de-los-documentos.md#ca-05--el-texto-fijo-de-la-plantilla-sobrevive-al-llenado) | CP-001, CP-002, CP-003, CP-005b | Cumple |
| RN-07 | CP-001, CP-004 | Cumple |
| RN-08 | CP-003, CP-005 | Cumple |
| Transversal, no regresión | CP-006, CP-007, CP-005c | Cumple |

## 5.1 Lo que el plan exigía

El plan de trabajo §8 decía que si aparecía un documento reprobado estando bien, el defecto era del validador y se corregía antes de publicar. Apareció, y se corrigió: dos veces. Es la parte del plan que más sirvió.

**Lo que el plan no previó y hubo que decidir en marcha:** que el criterio del CA-05 tuviera que cambiar. El CA hablaba de exigir citas de regla; se cambió a exigir que no haya fecha, y el CA se reescribió con él. Queda dicho acá para que nadie compare el plan con lo hecho y crea que se ejecutó otra cosa a escondidas.

---

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** las cuatro exigencias del §5 quedaron en verde con al menos un caso cada una, los 9 casos pasaron, y los 3 defectos críticos y altos se cerraron dentro de la fase. Las dos suites que dependen de lo que la fase cambia quedaron en verde.

**Lo que queda abierto** es D-04, que no es un defecto de esta fase sino lo primero que encontró el validador que la fase construyó.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | El código | [`validadores/plantillas.py`](../../../../../validadores/plantillas.py), `bloque_fijo()` y la comprobación 5 de `validar()` |
| EV-02 | Las pruebas | [`validadores/tests/test_encuadre_de_la_plantilla.py`](../../../../../validadores/tests/test_encuadre_de_la_plantilla.py), 9 casos |
| EV-03 | El barrido | Este documento, §2 y §3 |
| EV-04 | Las suites que la fase toca | `test_encuadre_de_la_plantilla.py` (11) y `test_plantillas_origen_regla.py` (3), en verde |

---

## 8. Ciclos anteriores

Ninguno: es la primera ejecución de esta fase.
