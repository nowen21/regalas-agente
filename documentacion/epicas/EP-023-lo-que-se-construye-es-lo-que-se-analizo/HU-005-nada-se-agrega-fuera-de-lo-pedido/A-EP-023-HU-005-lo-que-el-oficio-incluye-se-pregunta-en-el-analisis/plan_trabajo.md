# Plan de Trabajo · Fase `A-EP-023-HU-005-lo-que-el-oficio-incluye-se-pregunta-en-el-analisis` (módulo cuerpo de reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-023-HU-005-lo-que-el-oficio-incluye-se-pregunta-en-el-analisis` |
| **Épica** | [EP-023](../../epica.md) |
| **HU** | [HU-005](../HU-005-nada-se-agrega-fuera-de-lo-pedido.md), una sola (`F12.1`) |
| **Módulo** | Cuerpo de reglas (`base/`) y `historico-chat/memory/` |
| **Especificación del módulo** | Las reglas de negocio RN-01 a RN-05 de la HU-005 |
| **Fecha apertura** | 2026-10-02 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva, la única fase de la HU-005. Sale de los puntos 8, 22 y 28 de «Lo que se tiene que hacer» del [análisis 1](../../103-cada-documento-de-la-cadena-sale-del-anterior/analisis-1.md) y de los puntos 1 a 4 del [análisis 6](../../103-cada-documento-de-la-cadena-sale-del-anterior/analisis-6.md). Depende de la HU-001, que ya cumple.

**Versión 2, del análisis 6.** La versión 1 se escribió el 2026-10-02 y no se aprobó por el H-5: `01·C15` y `00·ID1` también se apoyaban en `01·C14`. Al revisarla salió además que el ejemplo de `02·F19` choca con `04·S1`. Esta versión suma `C15`, `ID1` y el ejemplo de `F19`.

**Carencias que cierra** (`02·F14` Q3): el agente agrega lo que no se pidió, porque `01·C14` se lo permite ([análisis 4](../../103-cada-documento-de-la-cadena-sale-del-anterior/analisis-4.md), conclusión 4).

**Aprobación** (`02·F4`): el usuario aprobó este plan y el de pruebas el 2026-10-02.

**Disparo** (`02·F15`, etapa 2): el usuario pidió escribir esta fase el 2026-10-02 con «Escriba», y la versión 2 con «Escriba» después de aprobar el análisis 6.

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-005 | Estado |
|---|---|
| CA-01 · La regla que reemplaza a `01·C14` y `02·F19` se complementan | ☑ |
| CA-02 · `01·C14` queda derogada y reemplazada, y `01·C25` y `01·C15` reubicadas | ☑ |
| CA-03 · Los recuerdos se ajustan al plan aprobado | ☑ |
| CA-04 · `00·ID1` rige dentro de lo pedido | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que ninguna regla ni recuerdo le permita al agente agregar lo que no se pidió. Lo pedido es el criterio de aceptación más lo que exigen las reglas de Cimiento; lo demás se pregunta en el análisis y lo decide el usuario.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | `C30` y `F19` dicen lo mismo desde dos lados, `C30` dice qué es lo pedido, y el ejemplo de `F19` deja de chocar con `04·S1` | Regla | Media |
| CA-02 | `C14` derogada, `C30` escrita, y `C25` y `C15` apoyadas en reglas vigentes | Regla | Media |
| CA-03 | Los dos recuerdos dejan de autorizar trabajo fuera del plan aprobado | Documentación | Baja |
| CA-04 | `ID1` rige cómo se hace lo pedido, no qué se agrega | Regla | Baja |

**Fuera de alcance:**

- Los puntos de «Lo que se tiene que hacer» que la propuesta final reparte a las otras HU.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-10-02, sobre la versión 40.1.0:

- `01·C14` dice que lo que el oficio da por sentado se construye de entrada, sin ofrecerlo como opción. Es la regla que el análisis 1 manda cambiar (conclusión 17).
- `02·F19` dice que la implementación hace literal lo que dice el CA, «ni más, ni menos». No cita a `C14`. Las dos chocan: una manda agregar lo que el oficio incluye y la otra prohíbe agregar.
- El ejemplo INCORRECTO de `F19` es agregar la revisión del permiso en el servidor cuando el CA pide ocultar un botón. `04·S1` exige esa revisión en toda acción sensible.
- `01·C25` y `01·C15` dicen «extiende `01·C14`».
- `00·ID1` cita a `C14` como la que fija el listón del oficio. Su cuerpo mide 294 caracteres.
- La última regla del capítulo 01 es `C29`, así que el siguiente número libre es `C30`.
- `C14` está en `base/mapa-de-tareas.md`, en `base/reglas-por-tarea/` (cambiar-codigo y escribir-documento), en `validadores/reglas-validables.md` (lista de no validables del capítulo 01) y en `validadores/reglas-antes-de-la-accion.md`, que es una foto del 2026-09-16 y no se actualiza con cada regla. Las demás coincidencias de «C14» en el repositorio son `13·DOC14`.
- El recuerdo «Corregir el defecto detectado» vale «mientras el agente ejecuta algo que ya le autorizaron», sin límite de plan.
- El recuerdo «Una instrucción se cumple entera» dice que lo que falte para seguir «se decide, se deja escrito el supuesto y se continúa». Choca con la conclusión 18 del análisis 1: ante un hallazgo, la ejecución se detiene.
- Las derogaciones anteriores (`00·ID2` en 6.0.0, `13·DOC8` en 40.0.0) subieron versión MAYOR, porque `02·F22` obliga a cada proyecto a adoptarlas.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `base/01-conducta.md` | Modificar | Regla | `C30` nueva, `C14` derogada, `C25` y `C15` reubicadas |
| `base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md` | Modificar | Regla | Su ejemplo deja de chocar con `04·S1` |
| `base/00-identidad-y-rol/reglas/ID1-trabaja-con-criterio-de-desarrollador-senior.md` | Modificar | Regla | Rige dentro de lo pedido y no cita a `C14` |
| `base/mapa-de-tareas.md` y `base/reglas-por-tarea/` | Modificar | Regla | Los vuelve a escribir `validadores/mapa_tareas.py` |
| `validadores/reglas-validables.md` | Modificar | Validador | `C30` en la lista de no validables del capítulo 01, y `C14` marcada derogada |
| `historico-chat/memory/corregir-el-defecto-que-uno-mismo-detecta.md` | Modificar | Documentación | Vale solo dentro del plan aprobado |
| `historico-chat/memory/una-instruccion-se-cumple-entera.md` | Modificar | Documentación | Un hallazgo detiene la ejecución |
| `historico-chat/memory/memory.md` | Modificar | Documentación | La línea del índice de los dos recuerdos |
| `CHANGELOG.md` y `VERSION` | Modificar | Versión | 41.0.0 |
| Los documentos de esta fase, la HU-005 y el resumen de la sesión | Modificar | Documentación | Cierre |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| `01·C14` deja de regir | `01·C25` | Pasa a extender `01·C4` |
| `01·C14` deja de regir | `01·C15` | Pasa a extender `01·C30` (análisis 6, conclusión 2) |
| `01·C14` deja de regir | `00·ID1` | Rige dentro de lo pedido y deja de citarla (análisis 6, conclusión 3) |
| `01·C14` deja de regir | Mapa de tareas y reglas por tarea | Se vuelven a escribir; una regla derogada no se inyecta |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La regla nueva es `01·C30` y declara «deroga `01·C14` · extiende `02·F19`» | Cambiar lo que exige `F19` | `F19` ya prohíbe agregar; lo que chocaba era `C14`. Con `C30` extendiendo a `F19`, las dos se complementan (`20·M7`). De `F19` solo cambia el ejemplo |
| El ejemplo nuevo de `F19`: el CA pide un listado y se agrega por cuenta propia una exportación que nadie pidió | Dejar el del botón | El del botón prohíbe lo que exige `04·S1` (análisis 6, conclusión 6) |
| `C25` pasa a extender `01·C4`, «No decidas por tu cuenta», y se mueve debajo de ella | Que extienda a `C30` | `C25` dice qué no decide el agente, que es el asunto de `C4`. `C30` habla de qué no se agrega |
| La versión sube a 41.0.0, MAYOR | MENOR | Una derogación obliga a cada proyecto a adoptarla (`02·F22`), como pasó con `ID2` y `DOC8` |
| `validadores/reglas-antes-de-la-accion.md` no se toca | Agregarle `C30` | Es una foto fechada que no se actualizó con `DOC24` ni `DOC25`; tocarla está fuera de los criterios |

### 2.7 Dudas por resolver antes de codificar

Ninguna. El H-5 lo resolvió el análisis 6.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| `01·C14` | Rige: lo que el oficio da por sentado se construye sin preguntar | `[DEROGADA en 41.0.0 → ver 01·C30]`, con su nota y su texto debajo | `20·M11` |
| `01·C30` | No existe | Lo que no se pidió no se agrega. Lo pedido es el CA más lo que exigen las reglas de Cimiento; lo que el oficio suele incluir se pregunta en el análisis | `20·M5`, `20·M7`, `20·M14` |
| `02·F19` | Su ejemplo choca con `04·S1` | Ejemplo de la exportación; lo que exige no cambia; checklist sellado de nuevo | `20·M5`, `20·M14` |
| `01·C25` | Extiende `C14` | Extiende `C4`, debajo de ella, con su checklist sellado de nuevo | `20·M7`, `20·M14` |
| `01·C15` | Extiende `C14` | Extiende `C30`, con su checklist sellado de nuevo | `20·M7`, `20·M14` |
| `00·ID1` | Pide el criterio del oficio y remite a `C14` | Pide el criterio del oficio dentro de lo pedido, sin citar a `C14`; checklist sellado de nuevo | `20·M5`, `20·M14` |
| Recuerdo «Corregir el defecto detectado» | Vale mientras se ejecuta algo autorizado | Vale solo dentro del plan aprobado; lo de afuera es un hallazgo | `01·C19` |
| Recuerdo «Una instrucción se cumple entera» | Lo que falta se decide y se sigue | Dentro del plan se sigue; un hallazgo detiene la ejecución | `01·C19` |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-01 · La regla que reemplaza a `C14` y `F19` se complementan

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | Crear `C30` con el molde de `20·M5`: una sola exigencia, cuerpo de hasta 320 caracteres que diga que lo pedido es el CA más lo que exigen las reglas de Cimiento, «(deroga `01·C14` · extiende `02·F19`)», ejemplo INCORRECTO/CORRECTO con la clase `Matematicas` (RN-01), «Aplica a: escribir-documento, cambiar-codigo» y su checklist. Va debajo de `C14` | `base/01-conducta.md` | CA-01, CA-02 | Rige desde 41.0.0 en todo proyecto | 1 h | Ninguna | CP-001, CP-002 |
| T-08 | Cambiar el ejemplo de `F19` por el de la exportación que nadie pidió, sin cambiar su cuerpo, y volver a sellar su checklist | `base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md` | CA-01 | Ninguno: lo que exige no cambia | 0,3 h | Ninguna | CP-001 |

### CA-02 · `C14` derogada y reemplazada, y `C25` y `C15` reubicadas

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-02 | Marcar `C14` como `[DEROGADA en 41.0.0 → ver 01·C30]`, con la nota de por qué dejó de regir y su texto original debajo | `base/01-conducta.md` | CA-02 | Deja de inyectarse | 0,3 h | T-01 | CP-002 |
| T-03 | Cambiar la dependencia de `C25` a «extiende `01·C4`», moverla debajo de `C4` y volver a sellar su checklist | `base/01-conducta.md` | CA-02 | Ninguno: lo que exige no cambia | 0,3 h | T-02 | CP-003 |
| T-09 | Cambiar la dependencia de `C15` a «extiende `01·C30`» y volver a sellar su checklist | `base/01-conducta.md` | CA-02 | Ninguno: lo que exige no cambia | 0,2 h | T-01 | CP-003 |
| T-06 | Correr `mapa_tareas.py`; sumar `C30` y marcar `C14` derogada en la lista de no validables del capítulo 01 | `base/mapa-de-tareas.md`, `base/reglas-por-tarea/`, `validadores/reglas-validables.md` | CA-02 | Las reglas que llegan con cada mensaje cambian | 0,3 h | T-03, T-09, T-10 | CP-004 |
| T-07 | Subir a 41.0.0 y escribir la entrada con «⚠ obliga a migrar» y lo que cada proyecto tiene que hacer (`20·M10`, `02·F22`) | `VERSION`, `CHANGELOG.md` | CA-02 | Todo proyecto adopta la versión | 0,3 h | T-06 | CP-004 |

### CA-03 · Los recuerdos se ajustan al plan aprobado

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-04 | Cambiar «dónde vale» por «dentro del plan aprobado», y decir que lo que queda fuera es un hallazgo que detiene la ejecución (análisis 1, conclusiones 18 y 45). Ajustar su línea del índice | `historico-chat/memory/corregir-el-defecto-que-uno-mismo-detecta.md`, `historico-chat/memory/memory.md` | CA-03 | Ninguno | 0,3 h | Ninguna | CP-005 |
| T-05 | Cambiar el punto «lo que falte se decide y se continúa»: dentro del plan aprobado se sigue sin preguntar; un hallazgo detiene la ejecución y vuelve al análisis. Ajustar su línea del índice | `historico-chat/memory/una-instruccion-se-cumple-entera.md`, `historico-chat/memory/memory.md` | CA-03 | Ninguno | 0,3 h | Ninguna | CP-005 |

### CA-04 · `ID1` rige dentro de lo pedido

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-10 | Cambiar el cuerpo: el criterio del oficio se aplica dentro de lo pedido. Quitar la frase que cita a `C14`, sin pasar de 320 caracteres, y volver a sellar su checklist | `base/00-identidad-y-rol/reglas/ID1-trabaja-con-criterio-de-desarrollador-senior.md` | CA-04 | Rige desde 41.0.0 en todo proyecto | 0,3 h | T-01 | CP-006 |

## 4. Secuencia de ejecución

T-01, T-02, T-03, T-09, T-10, T-08, T-06 y T-07, en ese orden. T-04 y T-05 en cualquier momento. Al final, los validadores y la medición de marcas (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Leer `C30`, `F19` y `S1` lado a lado | CP-001 |
| CA-02 | Leer `C14`, `C30`, `C25` y `C15`; correr los validadores | CP-002 a CP-004 |
| CA-03 | Leer los dos recuerdos | CP-005 |
| CA-04 | Leer `ID1` | CP-006 |

## 6. Datos y ambiente de prueba

El repositorio del estándar.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Cada proyecto adopta la 41.0.0 con el instalador. Ningún archivo de un proyecto cambia; cambia la regla que recibe el agente.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`20·M5`, `20·M7`, `20·M9`, `20·M10`, `20·M11`, `20·M14`, `02·F22`, `01·C19`, `00·ID8`, `02·F5`, `02·F8`, `02·F18`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Que `C30` lleve dos exigencias, no preguntar y no agregar | Su cuerpo dice una: lo que no se pidió no se agrega; la pregunta en el análisis es el camino, no otra exigencia. El checklist lo mide (fila 9) |
| Que `C30` no quepa en 320 caracteres con la definición de lo pedido | Se mide al escribirla; si no cabe, la fase se detiene y vuelve al análisis |

## 11. Definition of Done

- [ ] CA-01 a CA-04 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Los validadores sin fallas y cero marcas nuevas.
- [ ] `VERSION` y `CHANGELOG.md` en 41.0.0.
- [ ] Aprobación del usuario.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Se llena al cerrar la fase.
