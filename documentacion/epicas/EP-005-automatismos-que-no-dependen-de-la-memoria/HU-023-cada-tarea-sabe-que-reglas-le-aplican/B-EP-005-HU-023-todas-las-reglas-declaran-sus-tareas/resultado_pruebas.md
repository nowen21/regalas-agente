# Resultado de Pruebas · Fase `B-EP-005-HU-023-todas-las-reglas-declaran-sus-tareas`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra qué se ejecutó de verdad y con qué resultado, y de ahí sale el **veredicto** de la fase: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección *Qué se probó* del `funcionalidad_implementada.md`. El diseño de los casos vive en el `plan_pruebas.md` de esta misma fase, que no se modifica al ejecutar: se aprobó antes y así se queda.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-005-HU-023-todas-las-reglas-declaran-sus-tareas` |
| **HU** | [HU-023](../HU-023-cada-tarea-sabe-que-reglas-le-aplican.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md), versión 2.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-09-28 |
| **Ejecutado por** | El agente |
| **Ambiente y versión** | El repositorio del estándar, rama `main`, versión 39.3.0 sin commit; carpetas temporales para las pruebas que rompen algo a propósito |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 5 | 5 | 5 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

**CA-04 · CP-001, que el validador detecte lo que no cuadra**

**El problema que resuelve:** si nadie comprueba las líneas, una regla nueva entra sin tareas y el mapa envejece.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Prueba `test_la_regla_sin_tareas_falla` | Falla, nombrando la regla | Falla con «`07·Q1` no dice a qué tareas aplica» |
| 2 | Prueba `test_la_tarea_fuera_de_la_lista_falla` | Falla, nombrando la tarea | Falla con «nombra la tarea `bailar`» |
| 3 | Prueba `test_el_mapa_viejo_falla` | Falla, diciendo que el mapa quedó viejo | Falla con «el mapa no coincide con lo que dicen las reglas» |
| 4 | Prueba `test_la_regla_derogada_no_se_reporta` | No se reporta | No se reporta |
| 5 | Prueba `test_sin_lista_de_tareas_no_reporta_nada` | Nada | Nada |
| 6 | Buscar `tareas` en el `pre-push` de `instalar.py` y de `.githooks/pre-push` | Está en los dos | `for SUB in estandar versionado ejecutable tareas; do` en los dos; lo comprueba `test_el_pre_push_lo_corre` |

**Cómo se verificó que la pareja cumple:** los pasos 1 a 3 son los tres casos que pide la HU; el 4 y el 5, que no molesta donde no debe; el 6, que corre solo.

**CA-05 · CP-002, que todas las reglas declaren sus tareas**

**El problema que resuelve:** una regla sin tareas no le llega al agente por ningún lado.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr `python validadores/validar.py tareas` | 0 fallas | `OK: sin incumplimientos` |
| 2 | Contar las reglas del mapa y las vigentes | 252 y 252 | 252 reglas distintas en `base/mapa-de-tareas.md`; `metareglas.py` cuenta 252 vigentes |
| 3 | Correr `python validadores/validar.py metareglas`, y comparar los 99 archivos de `base/` tocados con los de `HEAD` quitándoles la línea | Sin sellos vencidos ni cuerpos cambiados | `OK: sin incumplimientos`; en los 99 archivos, lo único distinto es la línea `**Aplica a:**` |
| 4 | Mostrarle al usuario cuántas reglas quedaron en cada tarea | El usuario lo lee | `recibir-pedido` 18, `responder` 14, `escribir-documento` 51, `cambiar-codigo` 127, `correr-comando` 18, `tocar-git` 18, `tocar-datos` 18, `ir-afuera` 5, `cambiar-estandar` 25, `trabajar-cadena` 42. Se le muestra en el reporte de cierre |

**Cómo se verificó que la pareja cumple:** el paso 1 decide; el 2 confirma que no quedó ninguna fuera; el 3, que ninguna cambió qué exige.

**CA-06 · CP-003, que el amarre no se deje engañar**

**El problema que resuelve:** una frase que nombra un programa lo daba por clasificado y dejaba el mapa incompleto con el validador en verde.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Prueba `test_nombrarla_en_una_frase_no_la_clasifica` | Se reporta sin clasificar | Se reporta |
| 2 | Prueba `test_clasificarla_la_calla`, ahora con una fila de tabla | No se reporta | No se reporta |
| 3 | Prueba `test_la_linea_que_solo_lista_nombres_la_clasifica` | No se reporta | No se reporta |
| 4 | Correr `python validadores/validar.py amarre` | 0 fallas | `OK: sin incumplimientos`, 29 amarradas de 88 |
| 5 | Correr `python -m unittest test_el_mapa_del_amarre_no_envejece` | OK, sin las 3 fallas de la línea base | `Ran 14 tests`, OK |

**Cómo se verificó que la pareja cumple:** el paso 1 es el defecto de H-8; el 4 y el 5, que el mapa real quedó completo.

**CA-07 · CP-005, que el recuperador traiga las reglas de la tarea**

**El problema que resuelve:** el agente olvidaba las reglas porque no le llegaban en el momento de actuar.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Pasarle al enganche real «suba a git» | Trae `00·N2`, y las de todo mensaje | `00·N2` completa; `01·C28` e `ID8` a `ID12` en el bloque de todo mensaje |
| 2 | Pasarle «aplique las reglas de la caja de reglas de redacción al readme» | Trae `ID8`, `ID9`, `ID11` e `ID12` | `ID7`, `ID8`, `ID10`, `ID11` e `ID12` completas; `ID9` por su título en el bloque de todo mensaje, con la orden de leerla, porque completa no cabía (ver §4) |
| 3 | Pasarle «cree el pendiente del H2» | Trae `02·F23` y `01·C28` | `02·F23` completa; `01·C28` en el bloque de todo mensaje |
| 4 | Pasarle «hola» | Solo las de todo mensaje | Ninguna completa; las 31 de todo mensaje por su título |
| 5 | Medir lo que inyecta el enganche entero en los seis mensajes de prueba | Dentro de 10 KB, o lo que no cupo nombrado | Entre 2,9 y 9,4 KB, contando el recordatorio fijo del enganche |
| 6 | Correr los casos del recuperador de `validadores/pruebas.py` | OK | `Ran 21 tests`, OK |
| 7 | Abrir `.claude/settings.json` del estándar | `hook_reglas.py` en `UserPromptSubmit` | Está, después de `hook_checklist.py`, como lo pone `instalar.py` |

**Cómo se verificó que la pareja cumple:** los pasos 1 a 3 son los mensajes reales que fallaban; el 5 comprueba que lo inyectado no se corta; el 7, que corre en el estándar.

**RNF-01 y RNF-02 · CP-004, versionado y pruebas**

**El problema que resuelve:** un cambio sin versión no se rastrea, y lo que no tiene pruebas se rompe sin aviso.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Abrir `VERSION` | `39.3.0` | `39.3.0` |
| 2 | Abrir `CHANGELOG.md` | La entrada `39.3.0`, `**MENOR**`, en palabras llanas | Está; sus dos primeros párrafos no tienen rutas ni identificadores |
| 3 | Correr `validar.py versionado` y `test_la_entrada_del_registro_se_entiende` | 0 fallas y OK | `0 falla(s), 1 aviso(s)`, el de la 15.4.0 que ya estaba; OK |
| 4 | Correr las pruebas del mapa de tareas, del amarre, del instalador y del recuperador | OK | Mapa de tareas y amarre: 29, OK. Recuperador: 19, OK. Suite completa: ver §8 |

**Cómo se verificó que la pareja cumple:** los cuatro pasos dan lo esperado.

| Caso | CA | Prioridad (del plan) | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-04 | Crítica | 2026-09-28 | 7 pruebas del validador; `tareas` en los dos `pre-push` | Aprobado | EV-01 | — |
| CP-002 | CA-05 | Crítica | 2026-09-28 | `validar.py tareas` sin incumplimientos; 252 de 252 en el mapa; los 99 archivos sin otro cambio | Aprobado | EV-02 | DEF-01, DEF-04 |
| CP-003 | CA-06 | Crítica | 2026-09-28 | 3 pruebas nuevas; `amarre` sin fallas; 14 pruebas del amarre en OK | Aprobado | EV-03 | — |
| CP-004 | RNF-01, RNF-02 | Media | 2026-09-28 | `VERSION` en 39.3.0, entrada `**MENOR**`, pruebas en OK | Aprobado | EV-04 | — |
| CP-005 | CA-07 | Crítica | 2026-09-28 | El enganche real con seis mensajes de la sesión; 19 casos del recuperador en OK | Aprobado | EV-05 | DEF-02, DEF-03 |

**Correspondencia con el plan:** 5 casos en el plan, 5 aquí.

**Qué salió distinto de lo esperado:** en el CP-005, `ID9` llegó por su título y no completa en el pedido de redacción; es la mitigación que el plan aprobó para el riesgo B-03. En el CP-002, la lista de apoyo del guion rompió 79 enlaces (DEF-01).

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que las líneas quedaran dentro de su regla | Revisar a mano dos cambios: `base/03-datos.md` y la regla `F23` | Las dos van después del ejemplo y antes del separador |
| 2 | Que el enganche real no pase del tope de la herramienta | Correr `hook_reglas.py` como proceso, con la entrada en UTF-8, como lo corre la herramienta | Entre 2,9 y 9,4 KB en seis mensajes |

## 4. Defectos encontrados

| ID | Título | Caso que lo destapó | Severidad | Estado | Dónde quedó registrado |
|---|---|---|---|---|---|
| DEF-01 | La lista de apoyo del guion copió el cuerpo de las reglas con sus enlaces, que desde otra carpeta quedaban rotos: 79 fallas de `estandar` | CP-002 | Media | Verificado | Este documento; el guion deja ahora solo el texto de los enlaces |
| DEF-02 | Lo que el recuperador inyectaba pasaba de 10 KB: no contaba la lista de las que no cupieron ni el recordatorio del enganche | CP-005 | Alta | Verificado | Este documento; el recuperador mide el texto exacto y deja 1,5 KB para el enganche |
| DEF-03 | El orden ponía delante reglas que solo compartían «el», «del» o «reglas» con el pedido | CP-005 | Media | Verificado | Este documento; esas palabras no cuentan para el orden |
| DEF-05 | Ya conectado, el recuperador leyó como pedido lo que el editor agrega al mensaje: «qué sigue?» trajo reglas de documentos y de la cadena por la ruta del archivo abierto | Uso real, primer mensaje con el enganche puesto | Alta | Verificado | Este documento; se descarta lo que agrega el editor, con su prueba |
| DEF-06 | Las reglas de todo mensaje que no cabían completas salían dos veces: entre las que no cupieron y en su bloque | Uso real, el mismo mensaje | Baja | Verificado | Este documento; salen solo en su bloque, con su prueba |
| DEF-04 | El mapa copiaba los títulos de las reglas con su raya larga o su punto medio, que en una lista son marca de `00·ID8`: 11 marcas | CP-002 | Baja | Verificado | Este documento; `mapa_tareas.py` los escribe con coma, y el mapa quedó con 0 marcas |

**Defectos abiertos que se aceptan y por qué:** ninguno. El resultado de `ID9` en el paso 2 del CP-005 no es un defecto: es la mitigación aprobada del riesgo B-03. Solo cabría completa quitando la repetición del recordatorio fijo de `hook_reglas.py`, que el plan dejó fuera de alcance.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU (`CA-0N` · `RNF-0N`) | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-04 | CP-001 | Aprobado | Sí |
| CA-05 | CP-002 | Aprobado | Sí |
| CA-06 | CP-003 | Aprobado | Sí |
| CA-07 | CP-005 | Aprobado | Sí |
| RNF-01 | CP-004 | Aprobado | Sí |
| RNF-02 | CP-004 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias de la fase | Plan §12 | 100% | 6 de 6 con caso | Sí |
| Reglas vigentes sin tareas | Plan §12 | 0 | 0 | Sí |
| Fallas de `amarre`, `metareglas`, `estandar` y `versionado` | Plan §12 | 0 | 0, 0, 0 y 0 | Sí |

**Lo que no se cumplió:** nada.

## 6. Veredicto de la fase

**Concepto:** Cumple

**Justificación:** CA-04 a CA-07, RNF-01 y RNF-02 cumplen con sus casos ejecutados (§5). Los seis defectos se corrigieron dentro de la fase; dos de ellos salieron del primer mensaje real con el enganche puesto.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Pruebas y enganches | `validadores/tests/test_cada_tarea_sabe_que_reglas_le_aplican.py`, `validadores/instalar.py`, `.githooks/pre-push` |
| EV-02 | Archivos resultantes y guiones | Las líneas en `base/`, `base/mapa-de-tareas.md` y `historico-chat/scripts/2026-09-28/` |
| EV-03 | Programa, pruebas y mapa | `validadores/amarre.py`, `validadores/tests/test_el_mapa_del_amarre_no_envejece.py`, `anatomia/que-esta-amarrado-a-la-herramienta.md` |
| EV-04 | Archivos resultantes y pruebas | `VERSION`, `CHANGELOG.md` |
| EV-05 | Programa, pruebas, lista y enganche | `validadores/recuperar.py`, `validadores/pruebas.py`, `base/tareas.md`, `.claude/settings.json` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-09-28 | 5 | 0 | Primera ejecución |

**Suites de la fase (`02·F5`):** 191 pruebas de los módulos que la fase toca o que dependen de lo tocado (mapa de tareas, amarre, instalador y enganche de publicar, marcado de lo externo, y los que usan `metareglas.py`), en OK; y 21 casos del recuperador en `pruebas.py`, en OK. Se lanzó además la suite completa, que `02·F5` no pide; el usuario lo señaló y se detuvo sin resultado.
