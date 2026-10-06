# Análisis 1: el tapado de claves no reconoce las de Anthropic

> **Aprobado** por el usuario el 2026-10-06, en el turno 51, con la versión 55.2.0. Desde ese momento este análisis no se reescribe.

> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../../../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../../../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Un análisis aprobado no se reescribe. Si al ejecutar el plan aparece un hallazgo que obliga a tocar algo que el plan no declara, se abre `analisis-2.md`, que trata solo lo que falló y sus implicaciones sobre lo ya hecho.

---

## Recomendaciones

Se leyeron las [recomendaciones de Cimiento](../../../../../../plantillas/recomendaciones-del-analisis.md); el proyecto no tiene `analisis/recomendaciones.md`.

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-1 | Se revisó dónde más pasa: los cuatro usos del tapado y de la lista de secretos (guardado del gasto, histórico, validador de secretos y control de commits) |
| R-2 | Se midió lo que ya está guardado antes de proponer: la base y el repositorio |
| R-8 | Se buscaron claves sin mostrarlas: solo se contaron y se clasificaron |
| R-10 | La explicación al usuario usa el ejemplo del tapador que conoce unas claves y otras no |
| R-17 | Las respuestas se miden contra `00·ID9` |
| Las demás | No aplican: no se crea regla (R-3, R-4), es el análisis 1 (R-6), no hay piloto (R-16) |

---

## Hallazgo

### H-3 · El enmascarador no reconoce las claves de Anthropic

| Campo | Valor |
|---|---|
| Qué pasó | Al probar EP-025·HU-025, una línea con una clave `sk-ant-api03-…` y otra con `ANTHROPIC_API_KEY=…` quedaron en claro: el `Enmascarador` no conoce esas formas |
| Por qué importa | Las líneas de los `.jsonl` entran a la base pasando por ese tapado, y el histórico también lo usa; una clave sin tapar queda guardada, contra `00·N6` |

## Pendiente

## Pendiente: el enmascarador no reconoce las claves de Anthropic

| | |
|---|---|
| **De dónde sale** | [H-3 · El enmascarador no reconoce las claves de Anthropic](../../../../../../historico-chat/resumenes/2026-10-05/sesion-2.md), en el resumen de la sesión del 2026-10-05 |

### El problema

`Enmascarador.enmascarar`, en [enmascarar.py](../../../../../../proyectos/cimiento/core/enganches/enmascarar.py), no tapa una clave con la forma `sk-ant-api03-…` ni una asignación como `ANTHROPIC_API_KEY=…`. Las formas de proveedor que conoce vienen de `SEGUROS`, en `core/validadores/secretos.py`, y Anthropic no está. En `ANTHROPIC_API_KEY`, la parte `API_KEY` va pegada a `ANTHROPIC_` y el patrón pide un límite de palabra antes de `api`, así que tampoco la reconoce. Se vio el 2026-10-06 al probar EP-025·HU-025: la clave de prueba quedó en claro.

### Por qué importa

Desde EP-025·HU-025 cada línea de los `.jsonl` de Claude Code entra a la base pasando por este tapado, y esas líneas pueden traer la clave con la que corre Claude Code. También el histórico usa el mismo tapado. Una clave que no se tapa queda guardada, contra `00·N6`.

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 46 · Usuario, 2026-10-06 00:55:59
> Analicemos el pendiente 129

**Agente**, 2026-10-06 00:58:57
<!-- agente: 662dd61d-8f27-42ef-be7f-8b7aeffdab38 -->

Prendido el análisis 1 del pendiente 129. Antes de proponer, mido el alcance real: dónde se usa el tapador y si ya hay claves de Anthropic en claro. Solo cuento; no muestro ninguna clave.

El análisis quedó escrito en [analisis-1.md](../../../../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-002-enmascarar-claves/pendientes/129-el-enmascarador-no-reconoce-las-claves-de-anthropic/analisis-1.md), con lo que medí. Hoy no hay ninguna clave real de Anthropic guardada en claro: las 7 coincidencias son la clave falsa de la prueba.

**Decisión 1: ¿qué aprende el tapador?**

- **A (recomendada):** dos cosas.
  1. La forma de las claves de Anthropic (`sk-ant-` seguido de la clave).
  2. Cualquier variable que **termine** en `_API_KEY`, `_TOKEN`, `_SECRET` o `_PASSWORD`, tenga lo que tenga delante: `ANTHROPIC_API_KEY=`, `OPENAI_API_KEY=`, `GITHUB_TOKEN=`.

  Así queda cubierto el proveedor que falta y también los que vengan, sin tener que sumarlos uno por uno.
- **B:** solo las claves de Anthropic, con su forma y su variable.

Con cualquiera de las dos, el control de commits de todos los proyectos va a detectar más. Un commit que hoy pasa con una clave así escrita quedaría detenido, y eso es justo lo que se busca.

¿A o B?

### 47 · Usuario, 2026-10-06 01:01:31
> apruebo A

**Agente**, 2026-10-06 01:02:02
<!-- agente: b016fa6d-d486-4b54-a59f-24031fc3e1b1 -->

Queda anotado como **acuerdo 1**.

**Decisión 2: ¿qué se hace con lo que ya está guardado?**

Hoy en la base solo está la clave falsa de la prueba, y en el repositorio no hay nada. Pero cada vez que el tapador aprenda una forma nueva, lo guardado antes quedará sin revisar.

- **A (recomendada):** una orden, `manage.py retapar_lineas`, que pasa el tapador otra vez por todas las líneas guardadas. Se corre ahora una vez, y después cada vez que el tapador aprenda algo nuevo.
- **B:** no hacer nada, porque hoy solo está la clave falsa.

¿A o B?

### 48 · Usuario, 2026-10-06 01:02:48
> apruebo B

### 49 · Usuario, 2026-10-06 01:03:03
> apruebo A

**Agente**, 2026-10-06 01:03:28
<!-- agente: 84360d3e-0590-4d4a-915f-19ff7bc3d5ec -->

Queda anotado como **acuerdo 2**, la opción A. También quedó escrito que primero dijo B y lo corrigió.

**Decisión 3: ¿dónde va el trabajo?** Toca dos partes distintas de Cimiento, y `02·F11` pide una fase por cada parte:

| Parte | Qué cambia | Dueña |
|---|---|---|
| El tapador | La forma de Anthropic y las variables con prefijo | **EP-005·HU-002**, «enmascarar claves»: una fase nueva, la B |
| La base del gasto | La orden `retapar_lineas` | **EP-025·HU-025**, la que acabamos de hacer: una fase B |

**Recomiendo ese reparto:** no hace falta crear HU nuevas, porque cada cosa va como fase de la HU que ya es su dueña. Primero el tapador, después la orden, porque la orden usa al tapador.

¿Se aprueba?

### 50 · Usuario, 2026-10-06 01:06:19
> apruebo

**Agente**, 2026-10-06 01:08:34
<!-- agente: c25f7dcd-d206-4845-9a0a-fd89817ac078 -->

Ahora paso el hallazgo y el pendiente a su versión 2, antes de la aprobación.

Ya queda anotado como **acuerdo 3**, y el análisis está completo en [analisis-1.md](../../../../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-002-enmascarar-claves/pendientes/129-el-enmascarador-no-reconoce-las-claves-de-anthropic/analisis-1.md).

- **Los 3 acuerdos:**
  1. El tapador aprende la forma `sk-ant-` y cualquier variable que termine en `_API_KEY`, `_TOKEN`, `_SECRET` o `_PASSWORD`.
  2. La orden `retapar_lineas` vuelve a pasar el tapador por todo lo ya guardado.
  3. El trabajo va en dos fases: la fase B de EP-005·HU-002 y la fase B de EP-025·HU-025.
- **Lo que hay que hacer:** 4 filas. El pendiente y el hallazgo ya están pasados a la versión 2, que es la fila 1.
- **Lecciones:** dos, registradas como señales S-315 y S-316. La primera es que una prueba que falla imprime la clave que compara, y así entró la clave falsa al registro de la sesión.

Para cerrarlo, escribir un mensaje que empiece con **«Apruebo el análisis»**.

### 51 · Usuario, 2026-10-06 01:09:29
> Apruebo el análisis

**Agente**, 2026-10-06 01:09:41
<!-- agente: de96a5e5-36f3-455c-953a-d0f3560c0277 -->

El análisis 1 del pendiente 129 quedó **aprobado**: el enganche le puso la marca en el turno 51 y lo pasó al análisis principal. Se apaga al terminar esta respuesta, y con el próximo mensaje arranco las dos fases en su orden:

1. **EP-005·HU-002, fase B:** el tapador aprende las claves `sk-ant-` y las variables con prefijo.
2. **EP-025·HU-025, fase B:** la orden `retapar_lineas`, que se corre una vez sobre lo que ya está guardado.

Después siguen las HU de la pantalla: HU-026, HU-027 y EP-005·HU-024.

> acá termina la conversación

---

## Lo acordado

1. Lo que aprende el tapado: la forma de las claves de Anthropic (`sk-ant-` seguido de la clave) en la lista de formas de proveedor, y toda variable que termine en `_API_KEY`, `_TOKEN`, `_SECRET` o `_PASSWORD`, tenga lo que tenga delante. Como la lista la usa también el validador de secretos, el control de commits de todos los proyectos detecta lo mismo (turnos 46 y 47).
2. Lo ya guardado: una orden, `manage.py retapar_lineas`, pasa el tapado otra vez por todas las líneas guardadas en la base. Se corre una vez al terminar y cada vez que el tapado aprenda una forma nueva. El usuario primero escribió «B» y lo corrigió a «A» en el mismo mensaje (turno 49).

3. Dónde va: una fase B en EP-005·HU-002, dueña del tapado, para las formas nuevas; y una fase B en EP-025·HU-025, dueña de la base del gasto, para `retapar_lineas`. Primero el tapado, porque la orden lo usa. Es una fase por módulo (`02·F11`) y no hacen falta HU nuevas (turnos 49 y 50).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

`00·N6`: ninguna clave se deja en un registro ni entra al control de versiones. `01·C29`, desde 55.1.0: lo que se trae a la base entra sin claves. `04·S4`: la lista de secretos que usa el validador. `02·F11`: una fase por módulo, de ahí las dos fases del acuerdo 3. Ninguna regla choca.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| Lista de formas de proveedor | `SEGUROS`, en [secretos.py](../../../../../../proyectos/cimiento/core/validadores/secretos.py): AWS, clave privada, Stripe, SendGrid, Slack, GitHub, GitLab y Google. No está Anthropic |
| Asignación con comillas | `ASIGNA`, en el mismo archivo: pide un límite de palabra antes de `api_key`, así que `ANTHROPIC_API_KEY="..."` no entra |
| Asignación sin comillas | `_ASIGNA_SIN_COMILLAS`, en [enmascarar.py](../../../../../../proyectos/cimiento/core/enganches/enmascarar.py): el mismo límite, el mismo hueco |
| Quién usa la lista | El tapado (`Enmascarador`), y por él el guardado del gasto (`consumo/guardar.py`) y el histórico (`enganches/historico.py`); el validador de secretos (`validar.py secretos`), que corre también en el control de commits |
| Lo ya guardado | Medido el 2026-10-06: en la base, 3 coincidencias de `sk-ant-` y 4 de `ANTHROPIC_API_KEY=`, todas la clave falsa que armó la prueba de EP-025·HU-025 al fallar; en `historico-chat/`, `documentacion/` y `analisis/`, ninguna. No hay claves reales en claro |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Pendiente 84 | Ya amplió el tapado a la clave tecleada sin comillas; el acuerdo 1 sigue esa línea con el nombre compuesto |
| Resultado de EP-025·HU-025, DEF-01 | Es el hallazgo que abrió este análisis |
| [Fixtures sin secretos literales](../../../../../../historico-chat/memory/fixtures-sin-secretos-literales.md) | Las pruebas arman la clave al correr; el acuerdo 1 lo aplica en sus pruebas |
| Señal S-315 | Una prueba que falla imprime la clave que compara: así entró la clave falsa a la base. Lo recoge la lección 1 |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | El validador de secretos corre en todos los proyectos: una forma nueva puede detener un commit que hoy pasa. Versión MENOR según `20·M10`, porque solo detecta más; `02·F22` no aplica |
| Normas y leyes | Ninguna |
| Herramientas | Claude Code guarda en el `.jsonl` lo que leen sus herramientas, incluido un `.env` |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Clave de Anthropic en una línea de sesión | Base de Cimiento | Queda guardada en claro | Filas 2 y 4 |
| Clave de Anthropic en el histórico | `historico-chat/` | Se versiona y no se borra | Fila 2: el histórico usa el mismo tapado; hoy no hay ninguna (medido) |
| Clave de Anthropic en código o documentos | Control de commits de todo proyecto | Entra al repositorio | Fila 2: el validador usa la misma lista |
| Variable con prefijo de otro proveedor | `OPENAI_API_KEY=`, `GITHUB_TOKEN=` y otras | Igual que Anthropic | Fila 3 |
| La clave falsa de la prueba guardada en la base | 3 líneas de la sesión del 2026-10-05 | Ninguno: no es real | Fila 4 la tapa igual |

---

## Propuesta final: hallazgo y pendiente V2, épica y HU

### Hallazgo V2. El tapado de claves no reconoce las de Anthropic ni las variables con prefijo

| Campo | Valor |
|---|---|
| Qué pasó | Al probar EP-025·HU-025, una clave `sk-ant-api03-...` y una asignación `ANTHROPIC_API_KEY=...` quedaron en claro: el tapado no conoce la forma de Anthropic, y su patrón de asignación pide que la variable empiece en `api_key`, así que no ve las que traen un prefijo |
| Por qué importa | Las líneas de los `.jsonl` entran a la base pasando por ese tapado, el histórico también lo usa y el control de commits usa la misma lista; una clave sin tapar queda guardada, contra `00·N6` |

### Pendiente V2. El tapado de claves no reconoce las de Anthropic ni las variables con prefijo

| Campo | Valor |
|---|---|
| De dónde sale | El hallazgo V2, «El tapado de claves no reconoce las de Anthropic ni las variables con prefijo» |
| El problema | `SEGUROS` no trae la forma `sk-ant-`, y `ASIGNA` y `_ASIGNA_SIN_COMILLAS` exigen un límite de palabra antes de `api_key`, así que `ANTHROPIC_API_KEY=...` no entra. Lo ya guardado en la base no se vuelve a revisar cuando el tapado aprende algo |
| Por qué importa | Una clave sin tapar queda en la base, en el histórico o en un commit, contra `00·N6` |

### Épica y HU que salen del análisis

Épicas existentes: EP-005 (automatismos que no dependen de la memoria) y EP-025 (Cimiento se administra y muestra el gasto de tokens).

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | EP-005·HU-002, fase B | El tapado reconoce las claves de Anthropic y las variables con prefijo | El tapado no las reconoce | Ninguna | La orden de la fila siguiente lo usa | 2, 3 |
| 2 | EP-025·HU-025, fase B | Lo guardado se vuelve a tapar | Lo ya guardado no se revisa | EP-005·HU-002, fase B | Necesita el tapado nuevo | 4 |

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Una prueba que falla imprime la clave que compara, y así la clave entra al registro de la sesión; las pruebas de claves no deben repetir el valor al fallar | Falló | S-315 | No aplica: es de pruebas, no de análisis |
| 2 | Medir lo ya guardado antes de proponer cambió la urgencia: no había claves reales en claro | Funcionó | S-316 | Complementa R-2 |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Pasar el pendiente a su versión siguiente | `13·DOC26` | Este análisis, de una y sin fase: `documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-002-enmascarar-claves/pendientes/129-el-enmascarador-no-reconoce-las-claves-de-anthropic/pendiente.md`, hecho el 2026-10-06 |
| 2 | Sumar a `SEGUROS` la forma de las claves de Anthropic, con su prueba de clave armada al correr | 1 | EP-005·HU-002, fase B |
| 3 | Que `ASIGNA` y `_ASIGNA_SIN_COMILLAS` reconozcan las variables que terminan en `_API_KEY`, `_TOKEN`, `_SECRET` o `_PASSWORD` con cualquier prefijo, sin tapar lo que lee del entorno | 1 | EP-005·HU-002, fase B |
| 4 | `manage.py retapar_lineas` pasa el tapado por todas las líneas guardadas, y se corre una vez | 2 | EP-025·HU-025, fase B |

## Lo que aporta al análisis principal

**Resultado:** amplía.

**Lo que suma al análisis principal:** el tapado de claves reconoce también las de Anthropic y cualquier variable de clave con prefijo, y lo ya guardado en la base se vuelve a tapar cada vez que el tapado aprende una forma nueva.
