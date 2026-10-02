# Plan de Trabajo · Fase `A-EP-023-HU-002-cada-punto-dice-de-donde-sale` (módulo cuerpo de reglas, `plantillas/` y `validadores/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-023-HU-002-cada-punto-dice-de-donde-sale` |
| **Épica** | [EP-023](../../epica.md) |
| **HU** | [HU-002](../HU-002-cada-documento-sale-del-anterior.md), una sola (`F12.1`) |
| **Módulo** | Cuerpo de reglas (`base/`), `plantillas/` y `validadores/` |
| **Especificación del módulo** | Las reglas de negocio RN-01 a RN-05 de la HU-002 |
| **Fecha apertura** | 2026-10-02 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva, la única fase de la HU-002. Sale de los puntos 4 y 5 de «Lo que se tiene que hacer» del [análisis 1](../../103-cada-documento-de-la-cadena-sale-del-anterior/analisis-1.md) del punto 1 del [análisis 4](../../103-cada-documento-de-la-cadena-sale-del-anterior/analisis-4.md) y de los puntos 1 y 2 del [análisis 7](../../103-cada-documento-de-la-cadena-sale-del-anterior/analisis-7.md). Depende de la HU-001, que ya cumple.

**Carencias que cierra** (`02·F14` Q3): nada obliga a que cada documento salga del anterior ([análisis 4](../../103-cada-documento-de-la-cadena-sale-del-anterior/analisis-4.md), conclusión 4).

**Versión 2, del análisis 7.** La versión 1 se escribió el 2026-10-02 y no se aprobó por el H-7: los criterios de la plantilla de la HU no tenían «Sale de». Esta versión suma ese campo al CA-03.

**Aprobación** (`02·F4`): el usuario aprobó este plan y el de pruebas el 2026-10-02.

**Disparo** (`02·F15`, etapa 2): el usuario pidió escribir esta fase el 2026-10-02 con «Escriba».

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-002 | Estado |
|---|---|
| CA-01 · Cada punto cita su origen, y un validador sigue la cadena | ☑ |
| CA-02 · El cambio se aplica donde nace y baja en orden | ☑ |
| CA-03 · La plantilla de la HU distingue de dónde sale su contexto, y cada criterio dice de dónde sale | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que ningún punto de un documento de la cadena entre sin decir de qué punto del anterior sale, que un programa lo compruebe, y que un cambio de la necesidad baje en orden desde donde nace.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | La regla exige «Sale de»; el validador pasa un documento con todos sus orígenes y detiene uno sin «Sale de» y uno que cita un punto que no existe | Regla y validador | Alta |
| CA-02 | Una regla dice que el cambio se aplica donde nace y baja en orden | Regla | Baja |
| CA-03 | La plantilla de la HU dice de dónde sale el contexto en los dos casos, y cada criterio lleva «Sale de» | Plantilla | Baja |

**Fuera de alcance:**

- Los puntos de «Lo que se tiene que hacer» que la propuesta final reparte a las otras HU.
- Cómo pasa el plan a su versión siguiente cuando el cambio llega hasta él: es el punto 18 del análisis 1, de la HU-004.
- La tarea del plan frente a su criterio: ya la exige `02·F18` y la comprueba `validar.py flujo`.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-10-02, sobre la versión 41.0.0:

- La última regla del capítulo 02 es `F26`; los números libres son `F27` y `F28`.
- `02·F18` exige que cada tarea del plan cuelgue de un criterio, y `validadores/flujo.py` lo comprueba. Ninguna regla exige «Sale de» en los otros eslabones.
- Ninguna regla de `base/` dice que el cambio se aplica donde nace y baja en orden. `02/base.md` dice que el plan aprobado no se modifica «para anotarle resultados», que es otro caso.
- Los documentos de EP-023 ya citan su origen, y todas las citas existen: las conclusiones de los análisis 1 a 6 citan turnos de su conversación, las filas de «Lo que se tiene que hacer» citan conclusiones, los 42 criterios de las siete HU citan puntos de «Lo que se tiene que hacer», y el pendiente cita hallazgos que están en sus resúmenes.
- La plantilla del análisis tiene la columna «Sale de»; la del pendiente, «De dónde sale»; la del plan, la columna «Por qué» con el criterio. Los criterios de `plantillas/ciclo-vida-proyectos/04-HU.md` no tienen «Sale de» (H-7, resuelto en el análisis 7). Ningún validador compara los campos de los criterios contra la plantilla.
- La sección 3 de `04-HU.md` dice solo: «Es el problema del pendiente que genera la HU, tal cual está».
- Las 160 HU de las épicas anteriores a EP-023 no llevan «Sale de», porque nacieron antes de la regla.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `base/02-flujo-de-trabajo/reglas/F27-cada-punto-dice-de-que-punto-del-anterior-sale.md` | Nuevo | Regla | «Sale de» en cada punto |
| `base/02-flujo-de-trabajo/reglas/F28-el-cambio-se-aplica-donde-nace-y-baja-en-orden.md` | Nuevo | Regla | El cambio baja en orden |
| `base/02-flujo-de-trabajo/base.md` | Modificar | Regla | El índice del capítulo nombra `F27` y `F28` |
| `plantillas/ciclo-vida-proyectos/04-HU.md` | Modificar | Plantilla | La sección 3, con los dos casos, y «Sale de» en cada criterio |
| `validadores/origen.py` | Nuevo | Validador | Sigue la cadena de «Sale de» |
| `validadores/validar.py` | Modificar | Validador | Subcomando `origen` |
| `validadores/tests/test_origen.py` | Nuevo | Pruebas | Los casos del plan de pruebas |
| `validadores/reglas-validables.md` | Modificar | Validador | `F27` validable con `origen.py`; `F28` no validable |
| `anatomia/mapa-del-sitio.md` y `anatomia/que-esta-amarrado-a-la-herramienta.md` | Modificar | Documentación | Dicen qué hace `origen.py` y que no está atado a la herramienta |
| `base/reglas-por-tarea/` y `base/mapa-de-tareas.md` | Modificar | Regla | Los vuelve a escribir `validadores/mapa_tareas.py` |
| `CHANGELOG.md` y `VERSION` | Modificar | Versión | 42.0.0 |
| Los documentos de esta fase, la HU-002 y el resumen de la sesión | Modificar | Documentación | Cierre |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

No aplica: no se cambia ningún contrato. `validar.py todo` corre el subcomando nuevo junto con los demás.

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| `F27` extiende a `02·F18`, y `F18` no se toca | Ampliar `F18` | Lo pide la RN-04 (análisis 1, conclusión 28) |
| `F28` extiende a `02·F0` | Que extienda a `F27` | `F0` es la cadena; `F28` dice cómo la recorre un cambio |
| El validador revisa las épicas que tienen un análisis (`analisis-N.md`) en la carpeta de un pendiente | Revisar todas las HU | Las 160 HU anteriores nacieron sin la regla, y un cambio de norma no reabre lo cerrado (`20·M10`) |
| El validador revisa tres eslabones: el pendiente frente a su hallazgo, la conclusión frente a su turno y la fila de «Lo que se tiene que hacer» frente a su conclusión, y el criterio de la HU frente a su punto | Revisar también la tarea frente a su criterio | Eso ya lo hace `flujo.py` por `F18`; repetirlo da dos avisos por la misma falla |
| Un punto sin origen, o con un origen que no existe, es falla y no aviso | Aviso | El criterio dice «lo detiene» |
| La versión sube a 42.0.0, MAYOR | MENOR | `F27` obliga a cada proyecto al día a citar el origen en sus documentos nuevos |

### 2.7 Dudas por resolver antes de codificar

Ninguna. El H-7 lo resolvió el análisis 7.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| `02·F27` | No existe | Cada punto dice con «Sale de» de qué punto del documento anterior sale; lo que no tiene origen no entra | `20·M5`, `20·M7` |
| `02·F28` | No existe | El cambio de la necesidad se escribe donde nace y baja en orden: épica, HU, especificación y plan | `20·M5`, `20·M7` |
| `validar.py origen` | No existe | Falla por cada punto sin «Sale de» o con un origen que no existe | `20·M9` |
| Sección 3 de `04-HU.md` | Solo el caso del pendiente | El caso del pendiente y el de la épica, con su enlace | `13·DOC15` |
| Criterios de `04-HU.md` | Escenario, «Cómo validarlo» y «Aprobado cuando» | Además, «Sale de» encima del escenario | `02·F27` |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-01 · Cada punto cita su origen, y un validador sigue la cadena

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | Crear `F27` con el molde de `20·M5`: una exigencia, cuerpo de hasta 320 caracteres, «(extiende `02·F18`)», ejemplo INCORRECTO/CORRECTO, «Aplica a» y checklist. Sumarla al índice del capítulo | `base/02-flujo-de-trabajo/reglas/F27-…`, `base/02-flujo-de-trabajo/base.md` | CA-01 | Rige desde 42.0.0 en todo proyecto | 1 h | Ninguna | CP-001 |
| T-02 | Crear `revisar(raiz)` y `validar(raiz)`: en cada épica con un `analisis-N.md`, una falla por cada criterio de HU sin «Sale de» o que cita un punto que no está en «Lo que se tiene que hacer» de ese análisis; por cada conclusión que cita un turno que no está en la conversación; por cada fila de «Lo que se tiene que hacer» que cita una conclusión que no existe; y por cada pendiente sin «De dónde sale» o que cita un hallazgo que no está en el resumen enlazado | `validadores/origen.py` | CA-01 | Ninguno fuera de las épicas con análisis | 3 h | T-01 | CP-002, CP-003 |
| T-03 | Sumar el subcomando `origen` | `validadores/validar.py` | CA-01 | `validar.py todo` lo corre | 0,3 h | T-02 | CP-003 |
| T-04 | Escribir los casos del CP-002 sobre una carpeta temporal | `validadores/tests/test_origen.py` | CA-01 | Ninguno | 1 h | T-02 | CP-002 |
| T-05 | Registrar `F27` como validable con `origen.py` y `F28` como no validable; describir `origen.py` en el mapa del sitio y en el mapa del amarre | `validadores/reglas-validables.md`, `anatomia/mapa-del-sitio.md`, `anatomia/que-esta-amarrado-a-la-herramienta.md` | CA-01 | Ninguno | 0,3 h | T-02, T-06 | CP-006 |

### CA-02 · El cambio se aplica donde nace y baja en orden

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-06 | Crear `F28` con el molde de `20·M5` y «(extiende `02·F0`)», su checklist, y sumarla al índice del capítulo | `base/02-flujo-de-trabajo/reglas/F28-…`, `base/02-flujo-de-trabajo/base.md` | CA-02 | Rige desde 42.0.0 en todo proyecto | 0,5 h | Ninguna | CP-004 |
| T-08 | Correr `mapa_tareas.py`; subir a 42.0.0 y escribir la entrada con «⚠ obliga a migrar» y lo que cada proyecto tiene que hacer (`20·M10`) | `base/mapa-de-tareas.md`, `base/reglas-por-tarea/`, `VERSION`, `CHANGELOG.md` | CA-01, CA-02 | Las reglas que llegan con cada mensaje cambian | 0,5 h | T-01, T-06 | CP-006 |

### CA-03 · La plantilla de la HU distingue de dónde sale su contexto, y cada criterio dice de dónde sale

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-07 | Cambiar la sección 3: si la HU sale directo de un pendiente, el contexto es el problema del pendiente; si sale de una épica, es la parte del problema de la épica que le toca, con el enlace a la épica | `plantillas/ciclo-vida-proyectos/04-HU.md` | CA-03 | Las HU nuevas | 0,3 h | Ninguna | CP-005 |
| T-09 | Agregar a cada criterio de ejemplo la línea «**Sale de:**», encima del escenario, con el punto de «Lo que se tiene que hacer» del análisis | `plantillas/ciclo-vida-proyectos/04-HU.md` | CA-03 | Las HU nuevas cumplen `F27` desde la plantilla | 0,2 h | T-07 | CP-005 |

## 4. Secuencia de ejecución

T-01, T-06, T-02, T-03, T-04, T-05, T-07, T-09 y T-08. Al final, los validadores, las pruebas y la medición de marcas (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Leer `F27`; correr el validador sobre los tres documentos de prueba y sobre el repositorio | CP-001 a CP-003 |
| CA-02 | Leer `F28` | CP-004 |
| CA-03 | Leer la sección 3 y los criterios de `04-HU.md` | CP-005 |

## 6. Datos y ambiente de prueba

El repositorio del estándar, y carpetas temporales con documentos de prueba para el validador.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Cada proyecto adopta la 42.0.0 con el instalador. Sus documentos ya cerrados no cambian (`20·M10`); el validador solo revisa las épicas que nacen de un análisis.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`20·M5`, `20·M7`, `20·M9`, `20·M10`, `20·M14`, `02·F0`, `02·F18`, `13·DOC15`, `00·ID8`, `02·F5`, `02·F8`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Que `F27` no quepa en 320 caracteres con los cuatro eslabones | Se mide al escribirla; si no cabe, la fase se detiene y vuelve al análisis |
| Que el validador detenga documentos que hoy están bien | La línea base midió que los de EP-023 citan orígenes que existen; el CP-003 lo vuelve a correr |

## 11. Definition of Done

- [ ] CA-01 a CA-03 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Los validadores y las pruebas sin fallas, y cero marcas nuevas.
- [ ] `VERSION` y `CHANGELOG.md` en 42.0.0.
- [ ] Aprobación del usuario.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Se llena al cerrar la fase.
