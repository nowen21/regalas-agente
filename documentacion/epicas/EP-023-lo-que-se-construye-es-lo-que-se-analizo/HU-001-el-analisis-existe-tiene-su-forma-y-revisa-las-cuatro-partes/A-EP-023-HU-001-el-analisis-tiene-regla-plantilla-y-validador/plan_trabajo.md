# Plan de Trabajo · Fase `A-EP-023-HU-001-el-analisis-tiene-regla-plantilla-y-validador` (módulo Cuerpo de reglas, plantillas y validadores)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-023-HU-001-el-analisis-tiene-regla-plantilla-y-validador` |
| **Épica** | [EP-023](../../epica.md) |
| **HU** | [HU-001](../HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes.md), una sola (`F12.1`) |
| **Módulo** | Cuerpo de reglas, `plantillas/` y `validadores/` |
| **Especificación del módulo** | Las reglas de negocio RN-01 a RN-06 de la HU-001 |
| **Fecha apertura** | 2026-10-01 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): primera fase de la HU-001, que sale de los análisis 1, 2 y 4 del pendiente [Lo que se construye se aparta de lo aprobado](../../103-cada-documento-de-la-cadena-sale-del-anterior/pendiente.md).

**Carencias que cierra** (`02·F14` Q3): las que nombra el [pendiente](../../103-cada-documento-de-la-cadena-sale-del-anterior/pendiente.md): no hay un documento que fije el alcance antes de la HU. En esta fase, el análisis entra a la cadena con su regla, su plantilla y su validador.

**Versión 2, del [análisis 5](../../103-cada-documento-de-la-cadena-sale-del-anterior/analisis-5.md).** La versión 1 se aprobó el 2026-10-01 y se detuvo antes de la T-01 por el H-4: el CA-05 pedía una regla con dos exigencias. Esta versión parte esa regla en `DOC24` y `DOC25`, suma los dos archivos que faltaban y acorta `F0` y `F23`. El usuario la aprobó el 2026-10-01 (`02·F4`).

**Disparo** (`02·F15`, etapa 2): el usuario pidió escribir la especificación y el plan de la HU-001 el 2026-10-01, con «Escriba».

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-001 | Estado |
|---|---|
| CA-01 · `02·F0` lleva el análisis en cada punto de reparto | ☐ |
| CA-02 · Existe la plantilla del análisis | ☐ |
| CA-04 · El pendiente pasa por el análisis antes de la HU | ☐ |
| CA-05 · `13·DOC8` queda derogada y reemplazada por dos reglas | ☐ |
| CA-06 · El análisis sin una de las cuatro partes no cierra | ☐ |
| CA-07 · La versión 40.0.0 | ☐ |
| CA-16 · La plantilla del análisis pide la parte del problema de cada HU | ☐ |

Los demás criterios van en otras fases: CA-03 y CA-09 a CA-15, la herramienta que pasa la conversación, en la fase `B`; CA-08, el análisis principal de Cimiento, en la fase `C`.

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que el análisis exista en el estándar como eslabón de la cadena, con su regla, su plantilla y un validador que no deje cerrar uno al que le falten sus cuatro partes.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | `02·F0` pide el análisis en los tres puntos de reparto | Regla | Baja |
| CA-04 | `02·F23` pone el análisis entre el pendiente y la HU | Regla | Baja |
| CA-05 | `13·DOC8` derogada; `13·DOC24` y `13·DOC25` nuevas | Regla | Media |
| CA-02, CA-16 | La plantilla del análisis | Plantilla | Media |
| CA-06 | El validador de las cuatro partes | Validador | Media |
| CA-07 | Versión MAYOR con su CHANGELOG | Versionado | Baja |

**Fuera de alcance:**

- La herramienta que pasa la conversación al análisis y sus palabras (fase `B`).
- El análisis principal de Cimiento (fase `C`).
- Lo que reparten las HU 2 a 7.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-10-01:

- `02·F0` dice `planteamiento → épica → HU → especificación → plan → código`. Su ejemplo CORRECTO ya nombra un análisis antes de la épica, pero el cuerpo no.
- `02·F23` dice que el pendiente aprobado baja a una HU, sin análisis de por medio.
- `13·DOC8` pide un archivo de cierre aparte, con la plantilla `plantillas/cierre-analisis.md`, y congela el análisis original.
- La última regla del capítulo 13 es `DOC23`, así que las nuevas son `DOC24` y `DOC25`.
- El cuerpo de `F0` tiene 291 caracteres y el de `F23`, 320; la fila 10 del checklist admite hasta 320.
- `validadores/reglas-validables.md` registra si cada regla es validable y en su línea 65 nombra `DOC8`.
- `validadores/sitio.py` exige que cada validador esté en `anatomia/mapa-del-sitio.md`.
- Una regla derogada conserva su texto, lleva `[DEROGADA en X → ver Y]` en el título y una nota de por qué; el modelo es `00·ID2`.
- Citan `DOC8` o `cierre-analisis`: `validadores/plantillas.py`, `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md`, `base/02-flujo-de-trabajo/estructura-base.md`, `base/13-documentacion/base.md`, `base/13-documentacion/retrodocumentacion.md`, `base/glosario.md` y `base/mapa-de-tareas.md`.
- No hay plantilla del análisis. El punto de partida es el [borrador](../../103-cada-documento-de-la-cadena-sale-del-anterior/borrador-plantilla-analisis.md) (análisis 3, punto 3).
- `validadores/validar.py` registra cada validador como subcomando; no hay ninguno para el análisis.
- `VERSION` dice 39.6.0.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md` | Modificar | Estándar | El análisis en los tres puntos de reparto; se vuelve a sellar su checklist |
| `base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md` | Modificar | Estándar | El análisis entre el pendiente y la HU; se vuelve a sellar |
| `base/13-documentacion/reglas/DOC8-cierra-todo-analisis-con-su-tabla-de-decisiones.md` | Modificar | Estándar | Marca de derogada y nota; el texto se conserva (`20·M11`) |
| `base/13-documentacion/reglas/DOC24-cierra-el-analisis-en-su-mismo-archivo.md` | Nuevo | Estándar | El análisis individual cierra al final de su mismo archivo y no se reescribe |
| `base/13-documentacion/reglas/DOC25-reescribe-el-analisis-principal-con-su-lista-de-cambios.md` | Nuevo | Estándar | El análisis principal se reescribe y lleva su lista de cambios |
| `validadores/reglas-validables.md` | Modificar | Validador | Registra `DOC24` y `DOC25`, y cambia la mención de `DOC8` |
| `anatomia/mapa-del-sitio.md` | Modificar | Documentación | Dice qué hace `validadores/analisis.py` |
| `base/13-documentacion/base.md` | Modificar | Estándar | El índice del capítulo nombra `DOC24` y `DOC25`, y marca `DOC8` derogada |
| `base/02-flujo-de-trabajo/estructura-base.md`, `base/13-documentacion/retrodocumentacion.md`, `base/glosario.md` | Modificar | Estándar | Citan `DOC24` en lugar de `DOC8` |
| `plantillas/analisis.md` | Nuevo | Plantilla | Sale del borrador; su tabla de HU pide la parte del problema que resuelve cada una |
| `plantillas/cierre-analisis.md` | Modificar | Plantilla | Nota de que la regla que la pedía está derogada |
| `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` | Modificar | Plantilla | Cita `DOC24` en lugar de `DOC8` |
| `validadores/plantillas.py` | Modificar | Validador | Registra `plantillas/analisis.md` |
| `validadores/analisis.py` | Nuevo | Validador | Falla si un análisis aprobado no tiene sus cuatro secciones |
| `validadores/validar.py` | Modificar | Validador | Subcomando `analisis` |
| `validadores/tests/test_analisis.py` | Nuevo | Pruebas | Los casos del plan de pruebas |
| `base/reglas-por-tarea/` y `base/mapa-de-tareas.md` | Modificar | Estándar | Los vuelve a escribir `validadores/mapa_tareas.py` |
| `VERSION` y `CHANGELOG.md` | Modificar | Estándar | 40.0.0, MAYOR |
| Los documentos de esta fase, la HU-001 y el resumen de la sesión | Modificar | Documentación | Cierre |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Archivo | Cambio de contrato | Lo que depende | Dónde rompe |
|---|---|---|---|
| `13·DOC8` | Deja de regir | Las citas de la sección 2 y la de `reglas-validables.md` | Se cambian a `DOC24` o `DOC25` en esta fase |
| `validadores/plantillas.py` | Suma una plantilla | Sus pruebas | Se ajustan si cuentan plantillas |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| `DOC8` se deroga y nacen `DOC24` y `DOC25` | Reescribir `DOC8`, o una sola regla nueva con las dos partes | `20·M11`: las reglas se derogan; `20·M5`: una sola exigencia por regla (análisis 5) |
| El validador solo mira los `analisis-N.md` con la marca «Aprobado» | Mirar todo análisis | Uno abierto todavía se está llenando; el análisis de `analisis/` es de la forma vieja |
| `plantillas/cierre-analisis.md` se conserva con una nota | Borrarla | La citan fases y análisis cerrados |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| `02·F0` | Cadena sin análisis en el cuerpo | El análisis en los tres puntos de reparto | `20·M5`, `20·M12` |
| `02·F23` | El pendiente baja directo a la HU | El pendiente pasa por su análisis | `20·M5` |
| `13·DOC8` | Vigente | Derogada, con su texto conservado | `20·M11` |
| `13·DOC24` | No existe | El análisis individual cierra al final de su mismo archivo y no se reescribe | `20·M5`, `20·M7` |
| `13·DOC25` | No existe | El análisis principal se reescribe con su lista de cambios | `20·M5`, `20·M7` |
| `plantillas/analisis.md` | No existe | Plantilla del análisis | `13·DOC19`, `13·DOC21` |
| `validadores/analisis.py` | No existe | `revisar(raiz) -> list[str]`: devuelve las fallas de cada `analisis-N.md` aprobado al que le falte una de las cuatro secciones | `20·M9` |
| `validadores/validar.py` | Sin subcomando del análisis | Subcomando `analisis`, que llama a `analisis.revisar` | `20·M9` |
| `VERSION` | 39.6.0 | 40.0.0 | `20·M10` |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-01 · `02·F0` lleva el análisis en cada punto de reparto

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | Modificar el cuerpo: el análisis antes de las épicas, antes de las HU de cada épica y cada vez que entra un pendiente. Acortar el texto que ya tiene para que el cuerpo quepa en 320 caracteres, sin cambiar lo que exige. Volver a sellar su checklist | `base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md` | CA-01 | Cambia lo que pide la regla: se vuelve a escribir `base/reglas-por-tarea/` (T-08) | 0,5 h | Ninguna | CP-001 |

### CA-04 · El pendiente pasa por el análisis antes de la HU

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-02 | Modificar el cuerpo: el pendiente pasa por su análisis antes de bajar a la HU. Acortar el texto que ya tiene para que el cuerpo quepa en 320 caracteres, sin cambiar lo que exige. Volver a sellar su checklist | `base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md` | CA-04 | Igual que T-01 | 0,5 h | T-01 | CP-002 |

### CA-05 · `13·DOC8` queda derogada y reemplazada

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-03 | Crear las dos reglas con el molde de `20·M5` y su checklist: `DOC24`, el individual cierra al final de su mismo archivo y no se reescribe; `DOC25`, el principal se reescribe con su lista de cambios. Agregarlas al índice del capítulo y registrarlas en `reglas-validables.md` | `base/13-documentacion/reglas/DOC24-cierra-el-analisis-en-su-mismo-archivo.md`, `base/13-documentacion/reglas/DOC25-reescribe-el-analisis-principal-con-su-lista-de-cambios.md`, `base/13-documentacion/base.md` y `validadores/reglas-validables.md` | CA-05 | Reglas nuevas: entran a `base/reglas-por-tarea/` (T-08) | 1,5 h | Ninguna | CP-003 |
| T-04 | Marcar `DOC8` como derogada, con su nota y el texto original; cambiar sus citas a `DOC24` o `DOC25` | `DOC8`, `base/02-flujo-de-trabajo/estructura-base.md`, `base/13-documentacion/retrodocumentacion.md`, `base/glosario.md`, `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` y `plantillas/cierre-analisis.md` | CA-05 | Los proyectos que heredan dejan de tener `DOC8` vigente: aplica `02·F22` | 0,7 h | T-03 | CP-003 |

### CA-02 y CA-16 · La plantilla del análisis

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-05 | Crear la plantilla desde el borrador, con la columna «Parte del problema que resuelve» en la tabla de HU de la propuesta final; registrarla en el diccionario de plantillas | `plantillas/analisis.md` y `validadores/plantillas.py` | CA-02 y CA-16 | Las pruebas de `plantillas.py` pueden contar plantillas | 1 h | Ninguna | CP-004 |

### CA-06 · El análisis sin una de las cuatro partes no cierra

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-06 | Crear `revisar(raiz)`: busca los `analisis-N.md` con la marca «Aprobado» y devuelve una falla por cada sección de Cimiento, el proyecto, lo aprendido o el entorno que no esté. Sumar el subcomando `analisis` y describirlo en el mapa del sitio | `validadores/analisis.py`, `validadores/validar.py` y `anatomia/mapa-del-sitio.md` | CA-06 | Subcomando nuevo; no cambia los que existen | 1,5 h | T-05 | CP-005 |
| T-07 | Escribir los casos del CP-005 | `validadores/tests/test_analisis.py` | CA-06 | Ninguno | 1 h | T-06 | CP-005 |

### CA-07 · La versión 40.0.0

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-08 | Correr `mapa_tareas.py` para volver a escribir las reglas por tarea; subir la versión y escribir la entrada con «⚠ obliga a migrar», lo que cada proyecto tiene que hacer, `20·M10` y `02·F22` | `base/reglas-por-tarea/`, `base/mapa-de-tareas.md`, `VERSION` y `CHANGELOG.md` | CA-07 | Todo proyecto que actualice recibe la versión MAYOR | 0,7 h | T-01 a T-07 | CP-006 |

## 4. Secuencia de ejecución

T-01, T-02, T-03, T-04, T-05, T-06, T-07 y T-08. Al final, `validar.py estandar`, `plantillas`, `tareas`, `versionado` y `analisis`, más las pruebas que la fase toca (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Leer `F0` | CP-001 |
| CA-04 | Leer `F23` | CP-002 |
| CA-05 | Leer `DOC8`, `DOC24` y `DOC25`; buscar citas a `DOC8` fuera de la regla derogada | CP-003 |
| CA-02, CA-16 | Leer `plantillas/analisis.md` | CP-004 |
| CA-06 | Correr el validador sobre un análisis completo y uno al que le falta una sección | CP-005 |
| CA-07 | Leer `VERSION` y `CHANGELOG.md` | CP-006 |

## 6. Datos y ambiente de prueba

Local. Los análisis 1 a 4 del pendiente 103 como casos reales; copias en una carpeta temporal para los casos que fallan.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase. `DOC8` vuelve a regir porque su texto nunca se borra.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Los proyectos que heredan reciben la versión 40.0.0. Por `02·F22`, el que no la adopte no abre ni cierra fase. Nada se migra: los análisis viejos quedan como están.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`20·M5`, `20·M7`, `20·M10`, `20·M11`, `20·M12`, `02·F5`, `02·F8`, `02·F18`, `02·F22` y `00·ID8`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Una cita a `DOC8` que quede sin cambiar | La búsqueda del CP-003 |
| Que el validador marque los análisis 1 a 4 | El CP-005 los corre como caso real |

## 11. Definition of Done

- [ ] Los siete CA con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Las pruebas que la fase toca, en verde.
- [ ] `VERSION` y `CHANGELOG.md` al día.
- [ ] Aprobación del usuario.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Se llena al cerrar la fase.
