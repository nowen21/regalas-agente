# Análisis 5: el CA-05 pide una regla con dos exigencias

> **Aprobado** por el usuario el 2026-10-01, en el turno 72. El hallazgo y el pendiente no pasaron a otra versión, porque el análisis no los cambió. Desde ese momento este análisis no se reescribe.

> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Viene del [análisis 4](analisis-4.md), aprobado el 2026-10-01. Trata solo lo que falló y sus implicaciones sobre lo ya hecho (conclusión 19 del análisis 1).

---

## Recomendaciones

> Se agregó en el piloto, por el [análisis 9](analisis-9.md): este análisis no consultó recomendaciones, porque el archivo no existía. De sus lecciones salen: R-3 y R-15.

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| Ninguna | El archivo de [recomendaciones del análisis](../../../../plantillas/recomendaciones-del-analisis.md) nació después |

---

## Hallazgo

### H-4. El CA-05 pide una regla con dos exigencias

| Campo | Valor |
|---|---|
| Qué pasó | Al preparar la fase `A` de la [HU-001](../HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes/HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes.md) de EP-023, la tarea T-03 pide escribir `13·DOC24` con dos exigencias, como dice el CA-05: que el análisis principal se reescribe con su lista de cambios, y que el individual cierra al final de su mismo archivo y no se reescribe. El checklist de toda regla (fila 9, `20·M5`) admite una sola exigencia, y estas dos se pueden cumplir por separado. |
| Por qué importa | Escrita así, la regla no puede quedar sellada como CUMPLE. Partirla en dos reglas agrega un archivo que el plan aprobado no declara (`02·F8`), así que la fase se detuvo antes de empezar. |

## Pendiente

### Pendiente. Lo que se construye se aparta de lo aprobado

Reúne los pendientes 103, 104 y 105. Versión 3, del [análisis 2](analisis-2.md).

| Campo | Valor |
|---|---|
| De dónde sale | [H-13 de la sesión del 2026-09-28](../../../../historico-chat/resumenes/2026-09-28/sesion.md), que reúne H-10, H-11 y H-13, y [H-2 de la sesión del 2026-09-30](../../../../historico-chat/resumenes/2026-09-30/sesion.md) |
| El problema | No hay un documento que fije el alcance antes de la HU. Nada obliga a que cada documento salga del anterior. Nada detiene al agente cuando trabaja fuera del plan aprobado. La plantilla del plan no permite comprobarlo con un programa. Y lo que pasa la conversación al análisis hay que configurarlo a mano para cada análisis. |
| Por qué importa | Al ejecutar el plan aparecen hallazgos que se podían evitar, y cada uno se vuelve un pendiente más. |

---

## Conversación

> La pasa el enganche desde la [transcripción del día](../../../../historico-chat/2026-10-01-sesion.md), a partir del turno 64, donde se dijo «Analicemos: el pendiente 103».

### 64 · Usuario, 2026-10-01 23:19:07
> Registre y después Analicemos: el pendiente 103

**Agente**, 2026-10-01 23:19:54
<!-- agente: 1e64bb88-9796-472d-8535-a2a0e7744488 -->

Quedó registrado el H-4 en el [resumen de hoy](../../../../historico-chat/resumenes/2026-10-01/sesion.md), y el [análisis 5](../../../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-5.md) está prendido desde el turno 64.

**Primera pregunta (conclusión 7 del análisis 2): ¿el H-4 es parte del plan en curso?** Sí: frena la fase A de la HU-001. Lo que queda por decidir es la salida:

| Opción | Qué pasa |
|---|---|
| **A. Dos reglas** | `DOC24`: el análisis individual cierra al final de su mismo archivo y no se reescribe. `DOC25`: el análisis principal se reescribe y lleva su lista de cambios. El CA-05 se parte en dos y el plan de la fase A suma un archivo |
| B. Una regla con las dos partes | Cumple el CA-05 como está, pero su checklist no puede decir CUMPLE |

**Recomiendo A**, porque `20·M5` se cumple y ninguna regla queda mal sellada.

¿A o B?

### 65 · Usuario, 2026-10-01 23:21:13
> A

**Agente**, 2026-10-01 23:21:18
<!-- agente: 0a553a96-b60c-41dd-8449-9a7f0a19074d -->

Falta la palabra que dice qué se espera (`01·C28`). Con «Escriba», la opción A queda en las conclusiones del análisis 5 y lo dejo listo para aprobar.

### 66 · Usuario, 2026-10-01 23:21:35
> Escriba

**Agente**, 2026-10-01 23:22:19
<!-- agente: f937b456-f9a8-490a-9386-85c1cba2fd94 -->

Quedó escrito el [análisis 5](../../../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-5.md), con cero marcas.

**Conclusiones:**
1. El H-4 es parte del plan en curso.
2. Van dos reglas: `DOC24` para el análisis individual y `DOC25` para el principal.
3. El CA-05 y el plan de la fase A pasan a su versión siguiente.

**Lo que se tiene que hacer:**
1. Reescribir el CA-05 con las dos reglas.
2. Sumar `DOC25` al plan de la fase A y volver a aprobarlo.

El hallazgo y el pendiente no cambian. Para cerrarlo hace falta «Apruebo el análisis».

### 67 · Usuario, 2026-10-01 23:24:17
> Pregunta: ya no necesita nada más?

**Agente**, 2026-10-01 23:24:55
<!-- agente: 0bb05026-a037-4aaa-8434-ae9d995b564c -->

Sí, falta algo. Revisé el resto del plan de la fase A contra el checklist de las reglas, que es justo lo que dice la lección 1, y el plan tampoco declara dos archivos que va a necesitar:

| Archivo | Por qué hace falta |
|---|---|
| `validadores/reglas-validables.md` | La fila 18 del checklist exige registrar ahí cada regla nueva: `DOC24` y `DOC25`. Además, su línea 65 todavía nombra `DOC8` como validada por `plantillas.py` |
| `anatomia/mapa-del-sitio.md` | Dice qué hace cada validador, y `validadores/analisis.py` es nuevo |

Si no se suman ahora, saldrían como otro hallazgo al ejecutar, y la fase se volvería a detener.

Lo que propongo es agregar al análisis 5 una conclusión con estos dos archivos y ampliar el punto 2 de lo que se tiene que hacer: el plan de la fase A pasa a su versión siguiente con `DOC25`, `reglas-validables.md` y `mapa-del-sitio.md`. Para eso hace falta «Escriba». Después se cierra con «Apruebo el análisis».

### 68 · Usuario, 2026-10-01 23:25:40
> Escriba

**Agente**, 2026-10-01 23:26:10
<!-- agente: ee395ac3-83e4-42c2-8d51-baf4957dcc9d -->

Quedó en el [análisis 5](../../../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-5.md), con cero marcas:

- **Conclusión 4:** el plan de la fase A tampoco declaraba `validadores/reglas-validables.md` ni `anatomia/mapa-del-sitio.md`.
- **Punto 2 de lo que se tiene que hacer:** el plan pasa a su versión siguiente con `DOC25` y esos dos archivos, y se vuelve a aprobar.
- **El proyecto:** la tabla ahora nombra los dos archivos.

Para cerrarlo hace falta «Apruebo el análisis».

### 69 · Usuario, 2026-10-01 23:26:41
> Pregunta: ya quedó claro?

**Agente**, 2026-10-01 23:27:08
<!-- agente: 9d310289-707a-4332-9a24-5046a7b09627 -->

Casi. Medí el cuerpo de las dos reglas que se modifican contra la fila 10 del checklist, que permite máximo 320 caracteres:

| Regla | Hoy | Lo que pasa al agregar el análisis |
|---|---|---|
| `02·F0` | 291 | Pasa de 320 |
| `02·F23` | 320, justo en el tope | Pasa de 320 |

Para que quepan, las tareas T-01 y T-02 tienen que acortar el texto que ya tienen esas reglas, no solo sumarle.

No hace falta otro análisis: son los mismos archivos y las mismas tareas del plan. Pero conviene escribirlo ya en el análisis 5 y en esas dos tareas, para que no aparezca como sorpresa al ejecutar. Para sumarlo hace falta «Escriba». Después se cierra con «Apruebo el análisis».

### 70 · Usuario, 2026-10-01 23:27:55
> Escriba

**Agente**, 2026-10-01 23:28:17
<!-- agente: 5794a94e-54f4-4a64-857e-00b9feadcc1a -->

Quedó en el [análisis 5](../../../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-5.md), con cero marcas:

- **Conclusión 5:** `02·F0` tiene 291 caracteres y `02·F23` tiene 320. Para sumar el análisis, las tareas T-01 y T-02 acortan su texto sin cambiar lo que exigen.
- **Punto 3 de lo que se tiene que hacer:** esas dos tareas del plan lo dicen.

Para cerrarlo hace falta «Apruebo el análisis».

### 71 · Usuario, 2026-10-01 23:28:42
> Pregunta: ya quedó claro?

**Agente**, 2026-10-01 23:29:02
<!-- agente: 8129dc1e-0699-4439-9acc-0fc9f97536a6 -->

Sí, con lo que se puede comprobar antes de ejecutar. Revisé el plan de la fase A contra:

- **El checklist de las reglas:** una exigencia por regla (fila 9), el largo del cuerpo (fila 10), el registro de validables (fila 18) y la versión (fila 19). Las tres faltas que había están en las conclusiones 2, 4 y 5.
- **Los validadores que vigilan lo que se toca:** `validadores/sitio.py` exige que cada validador esté en `anatomia/mapa-del-sitio.md`, que ya está en la conclusión 4. Ninguno exige una guía en `validadores/docs/`.
- **Las rutas:** la carpeta `validadores/tests/` existe, y `DOC24` y `DOC25` son los siguientes números libres.

No queda nada abierto. Para cerrarlo hace falta «Apruebo el análisis».

### 72 · Usuario, 2026-10-01 23:29:26
> Apruebo el análisis

**Agente**, 2026-10-01 23:31:15
<!-- agente: 675e78fa-9c2d-4890-8b77-29b7019ea038 -->

El análisis 5 quedó aprobado en el turno 72, y ya apliqué sus tres puntos.

- **CA-05 de la HU-001:** ahora pide `DOC8` derogada y dos reglas nuevas, `DOC24` y `DOC25`. Como la HU cambió, volvió a quedar «Pendiente» para que la revise de nuevo.
- **Plan de la fase A, versión 2:**
  - la T-03 escribe las dos reglas y las registra en `reglas-validables.md`;
  - la T-06 pone el validador en `mapa-del-sitio.md`;
  - la T-01 y la T-02 acortan `F0` y `F23` para que quepan en 320 caracteres.
- **Plan de pruebas, versión 2.0:** suma esas comprobaciones.
- **Estado de la fase:** vuelve a la estación 7 y anota el bloqueo por el H-4.

Los cuatro documentos tienen cero marcas y ningún enlace roto.

Faltan dos aprobaciones: «Apruebo la HU-001» y «Apruebo los planes de la fase A».

> acá termina la conversación

---

## Lo acordado

> Se agregó en el piloto, por el [análisis 9](analisis-9.md), a partir de las conclusiones de este análisis, que después se quitaron para no repetirlas; cada punto conserva el número de su conclusión. No decide nada nuevo.

1. Es parte del plan en curso: El H-4 frena la fase `A` de la HU-001 y se resuelve antes de seguirla (Turnos 64 y 65).
2. Dos reglas: `DOC24`: el análisis individual cierra al final de su mismo archivo y no se reescribe. `DOC25`: el análisis principal se reescribe con lo que se va a construir y lleva su lista de cambios, cada uno con el enlace al análisis que lo produjo (Turno 65).
3. Qué cambia en lo ya hecho: El CA-05 de la HU-001 pasa a la versión siguiente y dice las dos reglas; el plan de la fase `A` suma `DOC25` y vuelve a aprobarse (Turno 65).
4. Lo que el plan tampoco declaraba: Al revisar el resto del plan de la fase `A` contra el checklist de las reglas faltaban dos archivos: `validadores/reglas-validables.md`, donde la fila 18 exige registrar `DOC24` y `DOC25` y donde todavía se nombra `DOC8`, y `anatomia/mapa-del-sitio.md`, que dice qué hace cada validador y no tendría `validadores/analisis.py` (Turnos 67 y 68).
5. El largo de las reglas que cambian: La fila 10 del checklist admite un cuerpo de hasta 320 caracteres. `02·F0` tiene 291 y `02·F23`, 320. Para sumar el análisis, las tareas T-01 y T-02 acortan el texto que ya tienen esas reglas, sin cambiar lo que exigen. Son los mismos archivos y las mismas tareas del plan (Turnos 69 y 70).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `20·M5` (una sola exigencia por regla, fila 9 del checklist), `20·M11` (`DOC8` se deroga, no se reescribe) y `02·F8` (no se edita un archivo que el plan no declara). Choca el CA-05 de la HU-001, que pide las dos exigencias en una regla; se resuelve en el punto 1 de lo que se tiene que hacer.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| Capítulo 13 | La última regla es `DOC23`; las nuevas son `DOC24` y `DOC25` |
| Fase `A` de la HU-001 | Plan aprobado el 2026-10-01 y detenido antes de la T-01; ningún archivo tocado |
| `validadores/reglas-validables.md` | Registra si cada regla es validable; su línea 65 nombra `DOC8` |
| `anatomia/mapa-del-sitio.md` | Dice qué hace cada validador |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Conclusión 18 del análisis 1 | Un hallazgo detiene la ejecución en ese momento. Así se hizo: la fase se detuvo antes de empezar |
| Conclusión 7 del análisis 2 | El análisis decide primero si el hallazgo es parte del plan en curso. Lo recoge la conclusión 1 |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | Ninguno nuevo: la versión sigue siendo 40.0.0, MAYOR, por la derogación de `DOC8` |
| Normas y leyes | Ninguna aplica |
| Herramientas | La conversación entró con el guion intermedio, prendido escribiendo a mano el archivo de estado |

### Dónde más puede pasar

> Se agregó en el piloto, por el [análisis 9](analisis-9.md), a partir de las conclusiones de este análisis; no decide nada nuevo.

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Criterio que pide una regla con dos exigencias | Cualquier HU | La regla no pasa su checklist | Conclusión 2 |
| Archivo que el plan no declara | Cualquier fase | Se edita fuera del plan | Conclusión 4 |
| Regla que no cabe en su largo | Cualquier regla que cambia | La regla queda fuera del molde | Conclusión 5 |

---

## Propuesta final: hallazgo y pendiente

> El H-4 no cambia. El pendiente sigue en la V3. EP-023 no suma puntos: el punto 16 del análisis 1 ya pide derogar `DOC8` y escribir lo que la reemplaza.

## Lecciones aprendidas

| # | Lección | Tipo | Señal |
|---|---|---|---|
| 1 | Los análisis 1 y 4 no aplicaron el checklist de las reglas al decidir que una regla nueva reemplaza a `DOC8`, y el choque salió al ejecutar | Falló | Por escribir |
| 2 | La fase se detuvo antes de tocar un archivo, como manda la conclusión 18 del análisis 1 | Funcionó | Por escribir |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Pasar el CA-05 de la HU-001 a la versión siguiente: `DOC8` derogada y reemplazada por `DOC24` y `DOC25` | 2, 3 | EP-023, HU-001 |
| 2 | Pasar el plan de la fase `A` a la versión siguiente con `DOC25`, `validadores/reglas-validables.md` y `anatomia/mapa-del-sitio.md` en su tabla de archivos, y volver a aprobarlo | 3, 4 | EP-023, HU-001, fase `A` |
| 3 | Que las tareas T-01 y T-02 del plan de la fase `A` digan que acortan el cuerpo de `02·F0` y de `02·F23` para que quepa en 320 caracteres con el análisis | 5 | EP-023, HU-001, fase `A` |

## Lo que aporta al análisis principal

> Se agregó en el piloto, por el [análisis 9](analisis-9.md), a partir de las conclusiones de este análisis; no decide nada nuevo.

**Resultado:** Modifica la idea.

**Lo que suma al análisis principal:** El análisis individual cierra en su mismo archivo y no se reescribe; el principal se reescribe con lo que aportan los individuales.
