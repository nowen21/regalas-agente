# Análisis 6: derogar `01·C14` deja otras dos reglas apoyadas en ella

> **Aprobado** por el usuario el 2026-10-02, en el turno 116. Desde ese momento este análisis no se reescribe.

> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Viene del [análisis 5](analisis-5.md), aprobado el 2026-10-01. Trata solo lo que falló y sus implicaciones sobre lo ya hecho (conclusión 19 del análisis 1).

---

## Hallazgo

### H-5. Derogar `01·C14` deja otras dos reglas apoyadas en ella

| Campo | Valor |
|---|---|
| Qué pasó | Al escribir la fase `A` de la [HU-005](../HU-005-nada-se-agrega-fuera-de-lo-pedido/HU-005-nada-se-agrega-fuera-de-lo-pedido.md) de EP-023, el 2026-10-02, se encontró que además de `01·C25` hay dos reglas que citan `01·C14`: `01·C15` la extiende, y `00·ID1` dice que `C14` fija «dónde queda el listón» del oficio. El análisis 1 solo nombró a `C25` (punto 22). |
| Por qué importa | Si `C14` se deroga y las otras dos no se tocan, quedan apoyadas en una regla que no rige. Y `ID1` pide trabajar con el criterio del oficio, que es lo que `C14` permitía agregar: puede chocar con la regla nueva (análisis 1, conclusión 12). Cambiar lo que `ID1` exige está fuera de los criterios de la HU-005. |

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

> La pasa el enganche desde la [transcripción del día](../../../../historico-chat/2026-10-01-sesion.md), a partir del turno 101, donde se dijo «Analicemos: el pendiente 103».

### 101 · Usuario, 2026-10-02 00:49:54
> Analicemos: el pendiente 103

**Agente**, 2026-10-02 00:51:03
<!-- agente: aa02137e-1ebb-4e6b-a76d-65115bb61400 -->

Ya está el encabezado del análisis 6. Leo `ID1` completa para plantear la pregunta.

En el análisis 6 hay que decidir qué pasa con dos reglas que hoy se apoyan en `01·C14`.

**`01·C15`:** «al replicar un patrón, replicar la paridad completa». La extiende.
- Lo que exige no choca con nada: si el usuario pidió «hazlo como X», la paridad es parte de lo pedido.
- Solo hay que cambiarle la dependencia. Recomiendo que pase a extender `C30`, porque las dos dicen qué hacer con lo que no está explícito: `C15` pregunta antes de omitir y `C30` pregunta antes de agregar.

**`00·ID1`:** «trabaja con criterio de desarrollador senior». Pide no entregar «lo mínimo que funciona» y remite a `C14` para saber dónde queda ese listón.
- Este sí puede chocar. Leída sola, autoriza agregar lo que «un senior firmaría», que es lo mismo que permitía `C14`.
- Recomiendo separar el cómo del qué. `ID1` rige **cómo** se hace lo pedido, con calidad y no lo mínimo. `C30` rige **qué** se hace: nada fuera de lo pedido.
- Para eso, `ID1` diría «resuelve cada decisión técnica **dentro de lo pedido**...» y dejaría de citar a `C14`.
- Eso cambia lo que exige `ID1`, así que entraría a la HU-005 como un criterio nuevo.

**Las preguntas:**
1. ¿`C15` pasa a extender a `C30`?
2. ¿`ID1` se ajusta así, o se maneja de otra forma?

### 102 · Usuario, 2026-10-02 00:51:27
> 00 id9

**Agente**, 2026-10-02 00:51:34
<!-- agente: b736bf8c-8264-420c-9f47-172c183eb7a6 -->

Hay dos reglas que se apoyan en `01·C14`:

1. **`01·C15`:** recomiendo que pase a extender a `C30`. Lo que exige no cambia.
2. **`00·ID1`:** recomiendo que diga «dentro de lo pedido» y deje de citar a `C14`. Así rige cómo se hace lo pedido, y `C30` rige qué se hace. Eso cambia lo que exige `ID1`, así que entra a la HU-005 como un criterio nuevo.

¿Se hacen así?

### 103 · Usuario, 2026-10-02 00:52:21
> si

**Agente**, 2026-10-02 00:52:26
<!-- agente: 85de88ef-27bf-445e-a4ff-24ac1dffaf6f -->

Queda acordado: `C15` pasa a extender a `C30`, e `ID1` se ajusta a «dentro de lo pedido» y entra a la HU-005 como un criterio nuevo.

Para llevar esto a las conclusiones del análisis 6, falta «Escriba».

### 104 · Usuario, 2026-10-02 00:52:35
> Escriba

**Agente**, 2026-10-02 00:54:05
<!-- agente: 0f1f4e30-26a3-4df8-9455-49992a8bc058 -->

Ya escribí lo que falta del análisis 6. Además de las cuatro partes, quedan:

- **Cuatro conclusiones:** el H-5 frena la fase A; `C15` pasa a extender a `C30`; `ID1` rige «dentro de lo pedido» y deja de citar a `C14`; y se dice qué cambia en lo ya hecho.
- **Tres puntos de «Lo que se tiene que hacer»:**
  - El CA-02 de la HU-005 pasa a su versión siguiente y suma `C15`.
  - La HU-005 gana el CA-04, por `ID1`.
  - El plan de la fase A pasa a su versión siguiente.
- **Dos lecciones:**
  - Falló que el análisis 1 no buscó qué reglas citaban a `C14`.
  - Funcionó que el hallazgo salió antes de aprobar el plan.

Una cosa no salió de la conversación: meter `C15` en el CA-02 y no en un criterio aparte. Lo decidí yo para que esa tarea cuelgue de un criterio (`02·F18`), y queda a la revisión del usuario.

`validar.py estandar` y `analisis` pasan. Queda una marca de `00·ID8`, los puntos suspensivos de una respuesta mía, pero está en la conversación copiada y no se edita.

Para cerrarlo: «Apruebo el análisis».

### 105 · Usuario, 2026-10-02 00:54:49
> pregunta: ya está claro lo que se requiere?

**Agente**, 2026-10-02 00:55:20
<!-- agente: 99278959-16a9-4bf0-8d32-ead8099acb59 -->

Sí. Antes de responder volví a buscar en todo el repositorio qué cita a `01·C14`, para no darlo por claro sin medirlo. Las otras coincidencias de «C14» son `DOC14`, que es otra regla.

Lo que cita a `C14` es esto, y todo queda cubierto:
- **Reglas:** `C25`, `C15` e `ID1`, en las conclusiones del análisis 6.
- **Mapa de tareas, reglas por tarea y `reglas-validables.md`:** ya están en el plan.
- **`reglas-antes-de-la-accion.md`:** el plan lo deja fuera porque es una foto con fecha.

`ID1` mide 294 caracteres. Sin la frase que cita a `C14` y con «dentro de lo pedido» cabe en los 320.

Solo falta una decisión del usuario: que `C15` vaya en el CA-02 y no en un criterio aparte.

### 106 · Usuario, 2026-10-02 00:55:34
> nada se contradice?

**Agente**, 2026-10-02 00:55:39
<!-- agente: f12f7736-3e1d-45c6-9d3f-797dca227e7c -->

Falta la palabra que dice qué se espera, por ejemplo «Pregunta» o «Revise».

### 107 · Usuario, 2026-10-02 00:55:58
> Pregunta: nada se contradice?

**Agente**, 2026-10-02 00:56:28
<!-- agente: 1ddc1fe9-a4f2-4382-a79c-11e69eedc75c -->

No del todo. Al revisarlo encontré un choque que ni el análisis 1 ni el 6 tratan.

**`02·F19` contra `04·S1`:**
- `F19` pone como ejemplo de lo INCORRECTO esto: el CA pide ocultar un botón, y el agente agrega además la verificación del permiso en el servidor «porque es buena práctica».
- `S1` exige justo eso: toda acción sensible verifica el permiso en el servidor, porque «ocultar un botón es apariencia, no seguridad».

`C30` va a extender a `F19`. Si se escribe tal como está, hereda el choque: prohibiría agregar lo que una regla del estándar obliga a hacer.

**Lo que habría que decidir:** si lo que exigen las reglas de Cimiento cuenta como parte de lo pedido, aunque el CA no lo diga. Recomiendo que sí. En ese caso, `C30` solo prohíbe lo que el oficio «suele incluir» sin que una regla lo exija, y el ejemplo de `F19` se cambia por uno que no choque con `S1`.

Esto sería la conclusión 5 del análisis 6, y entra a la HU-005 como parte del CA-01.

El resto no choca:
- `02·F20` (para y propón lo que descubras fuera del CA) extiende a `F19` y va en la misma dirección que `C30`.
- `C25`, `C15` e `ID1` ya están resueltas.

### 108 · Usuario, 2026-10-02 00:58:55
> 00 id9

**Agente**, 2026-10-02 00:59:04
<!-- agente: f028d4ed-eac3-4b38-befe-b3944735a867 -->

Hay un choque: el ejemplo de `02·F19` prohíbe verificar el permiso en el servidor, y `04·S1` lo exige. `C30` lo heredaría.

Recomiendo que lo que exigen las reglas de Cimiento cuente como parte de lo pedido y que el ejemplo de `F19` se cambie. Iría al CA-01 de la HU-005.

¿Se hace así?

### 109 · Usuario, 2026-10-02 00:59:35
> explique mejor

**Agente**, 2026-10-02 00:59:42
<!-- agente: e00a315a-d784-4472-afe4-6083cdf603a8 -->

Se pide ocultar el botón «Eliminar» a quien no tiene permiso.

- **`02·F19`** dice que se oculta el botón y nada más. Su ejemplo de lo incorrecto es justo agregar la revisión del permiso en el servidor.
- **`04·S1`** dice que ocultar el botón no basta. Cualquiera puede llamar al servidor sin pasar por el botón, así que el servidor tiene que revisar el permiso siempre.

Las dos reglas dicen lo contrario sobre el mismo caso. `C30` va a extender a `F19`, así que heredaría el choque.

**La propuesta:**
1. Lo que exige una regla de Cimiento siempre se hace, aunque el CA no lo diga. No cuenta como agregado.
2. `C30` prohíbe solo lo que el oficio «suele incluir» sin que ninguna regla lo exija.
3. El ejemplo de `F19` se cambia por uno que no choque con `S1`. Por ejemplo: el CA pide un listado y el agente le agrega por su cuenta la exportación a Excel.

¿Se hace así?

### 110 · Usuario, 2026-10-02 00:59:47
> 00 id9

**Agente**, 2026-10-02 00:59:56
<!-- agente: 3325331f-c0e1-48de-8b0b-63fab007cb77 -->

Con un botón «Eliminar» oculto, `F19` dice que no se revise el permiso en el servidor y `S1` dice que sí.

La propuesta:
- Lo que exige una regla siempre se hace.
- `C30` prohíbe solo lo que ninguna regla exige.
- El ejemplo de `F19` cambia por uno que no choque, como agregar una exportación a Excel que nadie pidió.

¿Se hace así?

### 111 · Usuario, 2026-10-02 01:00:25
> explique para niño

**Agente**, 2026-10-02 01:00:31
<!-- agente: 0d3e4baf-f471-4525-b9bd-26711085b4f5 -->

Una mamá le pide al niño: «esconde las galletas». El niño tiene dos reglas:

- **Regla A:** hacer solo lo que le piden, nada más.
- **Regla B:** las galletas siempre van con la tapa cerrada, para que no entren hormigas.

El niño esconde las galletas. ¿Cierra la tapa? La regla A dice que no, porque nadie se lo pidió. La regla B dice que sí, siempre. Las dos chocan.

**La propuesta:**
- Lo que manda una regla, como cerrar la tapa, siempre se hace aunque no lo pidan.
- Lo que no manda ninguna regla, como ponerle un lazo a la caja, no se hace si no lo piden.

¿Se hace así?

### 112 · Usuario, 2026-10-02 01:01:32
> pero entonces no entiendo lo que se quiere

**Agente**, 2026-10-02 01:01:40
<!-- agente: 850f98fe-8403-4cb2-ad05-ca6e503b24f0 -->

Lo que se busca con la HU-005 es una sola cosa: que el agente no agregue lo que nadie pidió.

El problema es que Cimiento tiene reglas que obligan a hacer cosas aunque el pedido no las nombre. Por ejemplo, `S1` obliga a revisar en el servidor que quien borra tenga permiso. Si «nada fuera de lo pedido» se lee al pie de la letra, el agente dejaría de cumplir esas reglas.

Entonces hay que decir qué cuenta como «lo pedido»:
- **Sí cuenta:** lo que dice el criterio de aceptación y lo que exigen las reglas de Cimiento.
- **No cuenta:** lo que el agente cree que «sería bueno» y que ninguna regla exige. Eso no se agrega, se pregunta en el análisis.

¿Así queda claro?

### 113 · Usuario, 2026-10-02 01:02:15
> 00 id9

**Agente**, 2026-10-02 01:02:20
<!-- agente: 01a88a2b-0d62-4562-b8ff-27c66e537c9c -->

La HU-005 busca que el agente no agregue lo que nadie pidió. «Lo pedido» sería el criterio de aceptación más lo que exigen las reglas de Cimiento. Lo demás no se agrega: se pregunta en el análisis.

¿Así queda claro?

### 114 · Usuario, 2026-10-02 01:02:39
> si

**Agente**, 2026-10-02 01:02:48
<!-- agente: 6bfff232-dd7d-4365-b277-576de620c659 -->

Queda acordado. Lo pedido es el criterio de aceptación más lo que exigen las reglas de Cimiento, y el ejemplo de `F19` se cambia.

Para pasarlo a las conclusiones del análisis 6, falta «Escriba».

### 115 · Usuario, 2026-10-02 01:03:15
> Escriba

**Agente**, 2026-10-02 01:03:59
<!-- agente: 377cb4ff-5663-408b-b11f-31cbc11aa43c -->

Ya está escrito en el [análisis 6](../../../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-6.md):

- **Conclusión 5:** lo pedido es el criterio de aceptación más lo que exigen las reglas de Cimiento.
- **Conclusión 6:** el ejemplo de `F19` cambia para no chocar con `S1`.
- **Punto 4 nuevo:** el CA-01 de la HU-005 pasa a su versión siguiente. El punto 3 suma el ejemplo de `F19` al plan.
- **Dos lecciones nuevas:** el análisis 1 no revisó `F19` contra el resto del estándar, y el ejemplo para niños aclaró lo que se pedía.

Lo escrito no tiene marcas de `00·ID8` y `validar.py estandar` pasa sin incumplimientos.

Para cerrarlo: «Apruebo el análisis».

### 116 · Usuario, 2026-10-02 01:04:19
> Apruebo el análisis

**Agente**, 2026-10-02 01:04:35
<!-- agente: 9cf8a0e7-6854-4cf9-b763-6ec92c27daca -->

El análisis 6 quedó aprobado. La marca está en el turno 116 y `validar.py analisis` lo pasa sin incumplimientos.

Lo que sigue son sus cuatro puntos de «Lo que se tiene que hacer»:
1. Pasar los CA-01 y CA-02 de la HU-005 a su versión siguiente.
2. Sumar el CA-04 de `ID1`.
3. Pasar el plan de la fase A a su versión 2, con `C15`, `ID1` y el ejemplo de `F19`.

Con eso, la HU-005 vuelve a quedar para aprobación. Para hacerlo, falta «Escriba».

> acá termina la conversación

---

## Lo acordado

> Se agregó en el piloto, por el [análisis 9](analisis-9.md), a partir de las conclusiones de este análisis, que después se quitaron para no repetirlas; cada punto conserva el número de su conclusión. No decide nada nuevo.

1. Es parte del plan en curso: El H-5 frena la fase `A` de la HU-005 antes de aprobarse, y se resuelve antes de seguirla (Turno 101).
2. `01·C15`: Pasa a extender a `01·C30`. Lo que exige no cambia (Turno 103).
3. `00·ID1`: Rige cómo se hace lo pedido; `C30` rige qué se hace. `ID1` dice «dentro de lo pedido» y deja de citar a `C14` (Turno 103).
4. Qué cambia en lo ya hecho: El cambio de `ID1` entra a la HU-005 como un criterio nuevo; el de `C15`, en el CA-02, junto a `C25`. El plan de la fase `A` pasa a su versión siguiente (Turno 103).
5. Qué es lo pedido: Lo pedido es el criterio de aceptación más lo que exigen las reglas de Cimiento. Lo que exige una regla siempre se hace y no cuenta como agregado. Lo que ninguna regla exige no se agrega: se pregunta en el análisis (Turnos 107 a 114).
6. El ejemplo de `02·F19`: Se cambia por uno que no choque con ninguna regla, como agregar por cuenta propia una exportación que nadie pidió. Entra al CA-01 de la HU-005 (Turnos 109 y 114).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `20·M7` (una regla declara de cuál se apoya con «extiende»), `20·M11` (`C14` se deroga, no se borra), `20·M14` (la regla que se edita vuelve a sellar su checklist) y `02·F18` (toda tarea del plan cuelga de un criterio). Choca `00·ID1` con la regla nueva `01·C30`: una pide el criterio del oficio y la otra prohíbe agregar lo que no se pidió (análisis 1, conclusión 12). Se resuelve en el punto 2 de lo que se tiene que hacer. Chocan también `02·F19` y `04·S1`: el ejemplo de `F19` pone como incorrecto revisar el permiso en el servidor cuando el CA solo pide ocultar un botón, y `S1` lo exige siempre. `C30` extiende a `F19` y heredaría el choque. Se resuelve en el punto 4.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| `01·C15` | En `base/01-conducta.md`, «extiende `01·C14`» |
| `00·ID1` | En `base/00-identidad-y-rol/reglas/ID1-trabaja-con-criterio-de-desarrollador-senior.md`, cita a `C14` como la que fija el listón del oficio. Llega con la tarea cambiar-codigo |
| `02·F19` | En `base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md`, su ejemplo INCORRECTO es agregar la revisión del permiso en el servidor |
| `04·S1` | En `base/04-seguridad.md`, exige revisar el permiso en el servidor en toda acción sensible |
| Fase `A` de la HU-005 | Plan de trabajo y de pruebas escritos el 2026-10-02, sin aprobar; ningún archivo de `base/` tocado |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Conclusión 45 del análisis 1 | Lo que el análisis no previó y queda fuera de los criterios es un hallazgo. Lo recoge la conclusión 1 |
| Lección 1 del análisis 5 | Ya había pasado: se decidió reemplazar una regla sin revisarla contra el estándar, y el choque salió al preparar el plan. Se repite acá con las reglas que citan a `C14` |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | Ninguno nuevo: la fase ya sube a 41.0.0, MAYOR, por la derogación de `C14`, y `02·F22` aplica. El cambio de `ID1` va en la misma versión |
| Normas y leyes | Ninguna aplica |
| Herramientas | La conversación entró sola, con el enganche de la fase `B` de la HU-001 |

### Dónde más puede pasar

> Se agregó en el piloto, por el [análisis 9](analisis-9.md), a partir de las conclusiones de este análisis; no decide nada nuevo.

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Reglas que citan una regla que se deroga | Cualquier derogación | Quedan apoyadas en lo que no rige | Conclusiones 2 y 3 |
| Lo que exige una regla y el CA no nombra | Cualquier HU | Se deja de cumplir la regla | Conclusión 5 |
| Ejemplo de una regla que choca con otra | Cualquier regla | Dos reglas dicen lo contrario | Conclusión 6 |

---

## Propuesta final: hallazgo y pendiente

> El H-5 no cambia. El pendiente sigue en la V3. EP-023 no suma HU: los cambios caben en la HU-005.

## Lecciones aprendidas

| # | Lección | Tipo | Señal |
|---|---|---|---|
| 1 | El análisis 1 decidió derogar `C14` sin buscar qué reglas la citan | Falló | Por escribir |
| 2 | El hallazgo salió al escribir el plan, antes de aprobarlo y de tocar una regla | Funcionó | Por escribir |
| 3 | El análisis 1 decidió que `C14` y `F19` se complementaran sin revisar `F19` contra el resto del estándar, y su ejemplo chocaba con `04·S1` | Falló | Por escribir |
| 4 | Explicar el choque con un ejemplo para niños aclaró qué se pedía | Funcionó | Por escribir |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Pasar el CA-02 de la HU-005 a la versión siguiente: `C25` y `C15` reubicadas, `C15` extendiendo a `C30` | 2, 4 | EP-023, [HU-005](../HU-005-nada-se-agrega-fuera-de-lo-pedido/HU-005-nada-se-agrega-fuera-de-lo-pedido.md) |
| 2 | Sumar a la HU-005 el CA-04: `00·ID1` rige dentro de lo pedido y no cita a `C14` | 3, 4 | EP-023, [HU-005](../HU-005-nada-se-agrega-fuera-de-lo-pedido/HU-005-nada-se-agrega-fuera-de-lo-pedido.md) |
| 3 | Pasar el plan de la fase `A` a su versión siguiente con `C15`, `ID1` y el ejemplo de `F19`, y volver a aprobarlo | 4, 6 | EP-023, HU-005, fase `A` |
| 4 | Pasar el CA-01 de la HU-005 a la versión siguiente: `C30` dice que lo pedido es el criterio más lo que exigen las reglas de Cimiento, y el ejemplo de `F19` deja de chocar con `04·S1` | 5, 6 | EP-023, [HU-005](../HU-005-nada-se-agrega-fuera-de-lo-pedido/HU-005-nada-se-agrega-fuera-de-lo-pedido.md) |

## Lo que aporta al análisis principal

> Se agregó en el piloto, por el [análisis 9](analisis-9.md), a partir de las conclusiones de este análisis; no decide nada nuevo.

**Resultado:** Modifica la idea.

**Lo que suma al análisis principal:** Lo pedido es el criterio de aceptación más lo que exigen las reglas; lo que nadie pidió no se agrega, se pregunta en el análisis.
