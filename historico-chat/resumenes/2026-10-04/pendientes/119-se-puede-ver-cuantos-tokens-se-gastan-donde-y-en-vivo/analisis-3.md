# Análisis 3: toda acción de Cimiento trae su contraria

> **Aprobado** por el usuario el 2026-10-05, en el turno 64, con la versión 54.4.0. Desde ese momento este análisis no se reescribe.

> Plantilla del análisis. Al llenarla se reemplazan los `«…»` y se borran las notas como esta, menos la tabla de reglas.
>
> Solo entra lo que ayuda a entender qué pasa y a tomar una decisión. Lo que no aporta a decidir no se escribe.
>
> Todo título y todo enlace dicen de qué se trata, nunca solo un número: «Pendiente: lo que se construye se aparta de lo aprobado», no «pendiente 103».
>
> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Un análisis aprobado no se reescribe. Si al ejecutar el plan aparece un hallazgo que obliga a tocar algo que el plan no declara, se abre `analisis-«N+1»`.md, que trata solo lo que falló y sus implicaciones sobre lo ya hecho. El hallazgo que no obliga a eso no abre análisis: se anota con su pendiente donde pertenece y el plan continúa.

---

## Recomendaciones

Se leyeron las [recomendaciones de Cimiento](../../../../../plantillas/recomendaciones-del-analisis.md); el proyecto no tiene `analisis/recomendaciones.md`.

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-1 | Se revisó dónde más falta la contraria: andamio, instalación, tarea programada, pendientes, fases y análisis (acuerdo 4) |
| R-2 | Se buscó lo que ya existe: no hay ninguna contraria en `core/`; `Sesiones`, `andamio.py`, `cerrar.py` y el estado del análisis prendido se revisaron antes de proponer |
| R-3 | La regla nueva del acuerdo 2 pasa su checklist al escribirse, en la HU-019 |
| R-6 | Se partió de los acuerdos de los análisis 1 y 2, que llegan en cada mensaje; el acuerdo 5 reemplaza el 3 del análisis 2 |
| R-7 | Lo que llegó de la otra sesión (las tres capas) se trató aquí como decisión, no directo a la épica |
| R-8 | Cada decisión se planteó sola; cuando la pregunta salió mal planteada (regla o criterio), se rehízo (turno 54) |
| R-9 | El hallazgo y el pendiente V4 se pasan a sus originales antes de aprobar |
| R-10 | El acuerdo 1 se explicó con el ejemplo de la HU mal numerada (turno 51) |
| R-17 | Se acortaron las respuestas que el enganche midió largas |
| Las demás | No aplican: no se exige campo nuevo en plantillas (R-4), no hay piloto (R-16), la épica se enlaza (R-13) |

---

## Hallazgo

### H-1 · El gasto no llega en vivo de todas las sesiones, y lo que se repite no se automatiza

| Campo | Valor |
|---|---|
| Qué pasó | EP-025 dejó el gasto en la base y en un tablero, pero lo vivo depende de la telemetría, que no trae enganches y solo la mandan las sesiones abiertas después de activarla; el `.jsonl` se lee al abrir el tablero y una vez al día. Además, cada proyecto no tiene su configuración sobre una base común, el tablero no separa lo que corre sin tokens de lo que podría automatizarse, el cierre de cada fase se hizo con guiones casi iguales, y Cimiento no trae ayuda ni manual |
| Por qué importa | Sin ver el gasto en cuanto ocurre y sin separar lo automatizable, no se sabe qué pasar a un programa; y cada guion repetido es gasto del modelo en algo que un programa haría sin tokens |

## Pendiente

**De dónde sale.** H-1 del resumen de la sesión del 2026-10-04, versión 3 según el análisis 2.

**El problema.** Falta un proceso que guarde el gasto en cuanto Claude Code lo escribe, con el tablero leyendo solo la base y sin telemetría; configuración base de Cimiento con la propia de cada proyecto; ver lo que corre sin tokens y lo que podría automatizarse; cerrar fases y separar los cambios por sesión como funcionalidades de Cimiento; y la ayuda y el manual de Cimiento.

**Por qué importa.** Lo que se repite sin automatizar gasta tokens que un programa ahorraría, y sin el gasto en vivo no se ve dónde.

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 38 · Usuario, 2026-10-05 12:05:40
> <cross-session-message from="uds:\\.\pipe\LOCAL\cc-msg-aab5bd61f926cd2b96df084192e8b3bd" from-name="agente-e6" from-mode="prompting">
> Segundo encargo para la EP-025: construir la configuración de cada proyecto en tres capas (fila 24 del análisis 1 del pendiente 116, acuerdo 12, aprobado por el usuario el 2026-10-05).
>
> El acuerdo 12, tal como quedó escrito:
> 1. La base de Cimiento es común a todos e incluye los enganches y las reglas obligatorias.
> 2. La configuración del proyecto, en la pantalla «Proyectos», prende o apaga lo que no es obligatorio.
> 3. El propio proyecto puede hacer un ajuste temporal para suspender una regla o un enganche que frena el trabajo mientras se corrige. Lleva motivo y fecha de vencimiento, afecta solo a ese proyecto y Cimiento lo muestra.
> 4. Nunca se suspende tapar las claves (00·N6) ni el histórico de la conversación. Todo lo demás sí se puede suspender, incluido el freno.
> 5. El proyecto siempre sabe qué tiene. Cimiento escribe en .agente/configuracion.md lo instalado, lo configurado y los ajustes vigentes, al instalar y cada vez que se guarda un cambio en la pantalla.
> 6. Si Cimiento no responde al instalar, el instalador conserva lo último instalado y avisa. Si el proyecto es nuevo, instala solo lo obligatorio y lo dice.
> 7. Ninguna configuración puede impedir corregir las reglas de Cimiento.
>
> Esto incluye el encargo anterior de hook_md.py: «Rutas en los avisos» sería una opción más de la capa 2.
>
> Esta sesión (agente-e6) hace la fila 23. Pasa a core/comun/enganches.py el catálogo de enganches (HOOKS, HOOKS_CLAUDE, CONFIG_AGENTE, IGNORADOS), con la marca de cuáles son obligatorios. Así se quita el ciclo de importación entre instalar y checklist. La pantalla debería leer ese catálogo para saber qué enganches existen y cuáles son obligatorios.
> </cross-session-message>

**Agente**, 2026-10-05 12:05:52
<!-- agente: 3b946ada-a827-4da3-ace6-5c77b1e5c126 -->

Llegó otro encargo de la sesión agente-e6 para EP-025, y lo dejo quieto porque no viene con una palabra de `01·C28`.

El encargo es construir la configuración de cada proyecto en tres capas:
1. La base obligatoria de Cimiento.
2. Lo que cada proyecto prende o apaga.
3. Ajustes temporales con motivo y vencimiento.

Además, `.agente/configuracion.md` en cada proyecto. Sale del acuerdo 12 del análisis 1 del pendiente 116.

Se cruza con el acuerdo 3 del análisis 2 del pendiente 119, recién aprobado, que solo tiene dos capas (base y proyecto). Hay que decidir si la HU-013 se amplía a las tres capas. Para eso, el mensaje empieza con «Analicemos».

### 39 · Usuario, 2026-10-05 12:05:54
> hágalo

**Agente**, 2026-10-05 12:09:06
<!-- agente: 42ed7072-526e-4e1a-953c-d8696d9868f0 -->

Primero verifico que el acuerdo 12 del análisis 1 del pendiente 116 esté escrito y aprobado como dice la otra sesión.

Las herramientas del estándar viven en `core/herramientas/` y se corren por su ruta, como el andamio. Reviso cómo crea el andamio una HU nueva, para usarlo y no armarla a mano.

Creo la HU-016 con el andamio.

El freno no me deja borrar la carpeta. Lo que pasó:
- Creé con el andamio la HU de cerrar fases, y el andamio le puso el número siguiente, 011.
- En el análisis aprobado, esa HU es la 016, y la 011 es «El gasto llega a la base en cuanto Claude Code lo escribe».
- Para que los números coincidan, hay que borrar la carpeta y crear las ocho HU en orden. El freno no deja borrarla porque no hay una fase en curso que la declare. No lo voy a saltar.

**Lo que necesito:** que se borre esta carpeta, que creé yo hace un momento y solo tiene la plantilla vacía:

```
documentacion\epicas\EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens\HU-011-cerrar-una-fase-y-separar-los-cambios-por-sesion-son-funcionalidades-de-cimiento
```

Con «Hágalo» se le puede pedir a la otra sesión, o se borra a mano. Cuando ya no esté, quito su fila de la épica, creo las HU-011 a HU-018 con los títulos del análisis y sigo con la construcción.

### 40 · Usuario, 2026-10-05 12:15:42
> Pregunta: cual carpeta?

**Agente**, 2026-10-05 12:15:53
<!-- agente: 4de724b6-9b83-4a19-a43b-ebdfc8772fde -->

Está dentro de la épica EP-025. Esta es la ruta completa:

```
C:\Ing. Jose\ia\agente\documentacion\epicas\EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens\HU-011-cerrar-una-fase-y-separar-los-cambios-por-sesion-son-funcionalidades-de-cimiento
```

Es la carpeta `HU-011-cerrar-una-fase-...`, al lado de `HU-010-el-gasto-se-ve-por-los-demas-niveles`. Tiene dos archivos de plantilla vacíos, `HU-011-...md` y `README.md`. Se puede borrar entera.

### 41 · Usuario, 2026-10-05 12:19:05
> pregunta y por qué la va a borrar?

**Agente**, 2026-10-05 12:19:18
<!-- agente: 20041575-ff8d-4216-aea9-65807b09f303 -->

Porque quedó con el número equivocado. El análisis aprobado le dio a cada HU nueva un número, y la de cerrar fases es la 016. La 011 le toca a «El gasto llega a la base en cuanto Claude Code lo escribe». El andamio no deja escoger el número: pone el siguiente libre, que era el 011. Así, la de cerrar fases quedó como HU-011.

Si se queda así, el número de cada HU no coincide con el que dice el análisis, y quien lea el análisis para saber de dónde sale cada HU encuentra otra cosa con ese número.

**Hay otra salida, sin borrar nada:** dejar la carpeta como está y que la HU-011 sea la de cerrar fases, con los demás números corridos. En la épica quedaría escrita la equivalencia: «HU-016 del análisis = HU-011». Funciona, pero cada vez hay que traducir los números.

Recomiendo borrarla: es una plantilla vacía de hace un momento, y así cada número coincide con el análisis.

### 42 · Usuario, 2026-10-05 12:20:05
> analicemos: ya la borré

**Agente**, 2026-10-05 12:20:32
<!-- agente: c0bf49ca-d1ff-4c39-a14e-9d00c1ec1fdd -->

Confirmado: la carpeta ya no está y la HU-010 es la última de la épica.

Queda una sola huella: la fila que el andamio agregó en la tabla de HU de `epica.md`. Apunta a la carpeta borrada, así que hoy es un enlace roto.

**Lo que sigue, con «Continúe» o «Hágalo»:**
1. Quitar esa fila de la épica.
2. Crear las HU-011 a HU-018 en orden, con los títulos del análisis, para que cada número coincida.
3. Construir en el orden del análisis, empezando por la HU-016, cerrar fases y separar los cambios por sesión. La HU-013 se construye con las tres capas del acuerdo 12 del pendiente 116.

### 43 · Usuario, 2026-10-05 13:14:03
> analicemos: no entiendo porque me pregunta cosas que son obvias si me dijo que eliminara la carpeta para qué quiere conservar la línea?

**Agente**, 2026-10-05 13:14:23
<!-- agente: 070ffa07-c019-4ef3-8dfe-f8d1cdaf2da4 -->

Tiene razón: esa línea no hay que conservarla, y no debí presentarla como pregunta.

No la quité por la palabra del mensaje anterior: «Analicemos» solo autoriza estudiar, no cambiar archivos (`01·C28`). Pero la fila es un defecto que dejé yo al crear la HU con el número equivocado, y quitarla hace parte de la orden de construir que ya está aprobada. Lo correcto era decir «la quito con el siguiente "Continúe"», sin ofrecerlo como algo por decidir.

Con «Continúe» la quito, creo las HU-011 a HU-018 y sigo con la construcción sin volver a preguntar lo obvio. Solo voy a preguntar el commit, lo que no se pueda deshacer y lo que salga del alcance.

### 44 · Usuario, 2026-10-05 13:28:50
> analicemos: mi lógica es esta: si para crearla cuando creo la HU no me preguntó por que para borrarla si me dice que si la borra cuando me dijo que borrar la HU

**Agente**, 2026-10-05 13:29:08
<!-- agente: efbab64e-2941-4cff-afd1-9c39a1c3debb -->

Su lógica es correcta. La HU es una sola cosa: la carpeta más su fila en la épica. El andamio crea las dos juntas, en un paso, sin preguntar. Borrar la HU es borrar las dos, y eso ya estaba dicho cuando aceptó borrarla. Yo las separé y le pregunté por la mitad. Ese fue el error.

**Por qué pasó:** Cimiento sabe crear una HU pero no quitarla. Como no existe lo contrario del andamio, traté la carpeta y la fila como dos cosas distintas, y el freno, al no tener una herramienta que lo haga, bloqueó el borrado de la carpeta.

**Cómo evitar que se repita:** que el andamio también sepa quitar una HU (`andamio quitar-hu`), con la carpeta y su fila en la épica a la vez, y solo si la HU no tiene nada escrito más allá de la plantilla. Encaja en el acuerdo 6 del análisis 2: lo que el proceso ya define es una funcionalidad de Cimiento. Se haría dentro de la HU-016.

Con «Continúe» quito la fila y sigo. Si se quiere sumar `quitar-hu` a la HU-016, basta decirlo en el mismo mensaje.

### 45 · Usuario, 2026-10-05 14:13:58
> analicemos: todo proceso tiene su proceso contrario como dice la tercera ley newton ley acción y reacción

**Agente**, 2026-10-05 14:14:35
<!-- agente: a1835d5e-5ef4-4635-a771-f440c34ad87f -->

Es un buen principio para Cimiento: toda acción que crea o cambia algo trae su acción contraria, que deja todo como estaba. Revisé qué tiene hoy su contraria y qué no.

Ninguna de las acciones contrarias que faltan existe todavía en `core/`. El inventario:

| Acción | Su contraria | Hoy |
|---|---|---|
| El andamio crea una fase, una HU o un pendiente | Quitarla, solo si sigue siendo la plantilla vacía | No existe; por eso pasó lo de la HU-011 |
| Instalar el estándar en un proyecto | Desinstalarlo | No existe |
| Programar la lectura diaria del gasto | Quitar la tarea | No existe |
| Cerrar un pendiente (`cerrar.py`, que lo mueve a `hecho/`) | Reabrirlo | No existe |
| Arrancar el proceso que carga la base (HU-011) | Detenerlo por su número de proceso | Se construye con la HU-011 |
| Activar la telemetría | Retirarla | La HU-012 |
| Cerrar una fase (HU-016) | Reabrirla | No está en el análisis |
| Registrar un proyecto o cambiar un nivel | Desactivarlo o volver al nivel anterior | Ya existe |

**Propuesta, en dos partes:**
1. **Como criterio para todo lo que se construya:** ninguna acción nueva de Cimiento se da por terminada sin su contraria y su prueba. Así la HU-016 trae `reabrir_fase` junto a `cerrar_fase`.
2. **Para lo que ya existe sin contraria:** construir quitar (en el andamio), desinstalar, quitar la tarea programada y reabrir un pendiente.

El análisis 2 ya está aprobado y no se reescribe. Esto entra como análisis 3 del pendiente 119, con «Analicemos: el pendiente 119». Ahí también decide si el principio queda como regla del estándar, que vale para todos los proyectos, o solo como criterio de Cimiento.

### 46 · Usuario, 2026-10-05 14:16:16
> osea esto no se estaba analizando?

**Agente**, 2026-10-05 14:16:25
<!-- agente: f6ce3073-ab0f-4adb-b90d-6de074d9fa3a -->

A este mensaje le falta la palabra de `01·C28`. Si es una pregunta, mándelo empezando con «Pregunta» y la respondo.

### 47 · Usuario, 2026-10-05 14:16:46
> Pregunta: osea esto no se estaba analizando?

**Agente**, 2026-10-05 14:16:57
<!-- agente: 8efce725-dce9-4749-ac08-f8edf2e762d9 -->

No, no estaba dentro de un análisis. El análisis 2 del pendiente 119 se cerró cuando lo aprobó, en el turno 37. Desde entonces ningún análisis está prendido, y el enganche lo confirma en cada mensaje: «Ningún análisis está prendido».

Lo que hablamos después («Analicemos» sobre la carpeta, la línea de la épica y el principio de acción y reacción) se respondió en el chat, pero no quedó escrito en ningún análisis. Por eso propuse abrir el análisis 3: para que el principio y sus acuerdos queden registrados y se puedan construir.

Para abrirlo, el mensaje es «Analicemos: el pendiente 119».

### 48 · Usuario, 2026-10-05 14:17:31
> Analicemos: el pendiente 119 y que quede todo desde que se empezó la discución

**Agente**, 2026-10-05 14:18:45
<!-- agente: a6da68b6-919b-441f-a9bc-6d44bb423247 -->

Quedó abierto el análisis 3, desde el turno 48. Pide que entre la discusión desde que empezó. Reviso cómo copia el enganche los turnos, para hacerlo con la herramienta y no a mano.

El freno no me deja cambiar el estado del análisis: ese archivo solo lo escribe la herramienta, y ella solo sabe prender «desde el turno actual», no desde uno anterior. Es otro caso del mismo tema de este análisis: la herramienta tiene la acción pero le falta la variante que se necesita. Lo anoto como punto del análisis.

**Lo que necesito para que entre todo desde el turno 38:** cambiar una línea en este archivo:

```
C:\Ing. Jose\ia\agente\historico-chat\.estado\analisis-en-curso\2026-10-04-sesion-3.txt
```

donde dice `desde=48`, poner `desde=38`. Con eso, el enganche copia en el análisis 3 los turnos 38 a 47 con el próximo mensaje: el encargo de las tres capas, el «hágalo», lo de la carpeta y la línea de la épica, y la ley de acción y reacción.

¿Lo cambia a mano o se lo pido a otra sesión?

### 49 · Usuario, 2026-10-05 14:21:46
> 
> analicemos: ya lo cambié

**Agente**, 2026-10-05 14:22:41
<!-- agente: b04c0997-4b07-4700-8988-1c0138aef8b4 -->

Quedó: el análisis 3 tiene la conversación desde el turno 38. Le pongo título.

El análisis 3 se titula «Toda acción de Cimiento trae su contraria».

**Hay cuatro decisiones, de a una:**
1. Si el principio es regla del estándar o criterio solo de Cimiento.
2. Qué contrarias que faltan se construyen: quitar una HU, fase o pendiente; desinstalar; quitar la tarea programada; reabrir un pendiente o una fase; prender un análisis desde un turno anterior.
3. El andamio crea la HU con el número que le diga el análisis, no solo con el siguiente libre.
4. La configuración en tres capas que pidió la otra sesión (acuerdo 12 del pendiente 116), que amplía la HU-013 del análisis 2.

**La primera: ¿regla del estándar o criterio de Cimiento?**
- **Regla del estándar:** vale para todos los proyectos. Ningún plan que agregue una acción se aprueba sin su contraria y su prueba. Es versión MAYOR, porque obliga a los proyectos a algo nuevo.
- **Criterio de Cimiento:** solo para las herramientas del estándar. Es versión MENOR, y los proyectos no cambian nada.

**Recomiendo la regla del estándar.** El problema de hoy (crear sin poder deshacer) puede pasar en cualquier proyecto, y el recuerdo «todo multiproyecto» pide construir para todos. El costo es que los planes nuevos de cada proyecto tendrán que declarar la contraria de lo que agregan.

### 50 · Usuario, 2026-10-05 14:24:50
> analicemos: si ve eso que nos pasó el freno bloqueó y tocó entrar al código a tocarlo para solucionar a eso es lo que me refiero con la flexibilidad

**Agente**, 2026-10-05 14:25:11
<!-- agente: 9002f530-c2dc-404c-b56e-ed9915a746b0 -->

Entiendo, y lo de hoy lo muestra bien. Dos veces el freno detuvo algo correcto (borrar la carpeta mal numerada y cambiar el turno de inicio del análisis) y la única salida fue que usted tocara archivos a mano. Eso es justo la falta de flexibilidad: la regla se cumplió, pero no había una forma prevista de hacer lo legítimo.

**Cómo se resuelve, uniendo lo que ya está sobre la mesa:**
1. **La contraria como herramienta:** si existe `andamio quitar-hu` o «prender el análisis desde el turno N», el freno las deja pasar como hoy deja pasar el andamio, y nadie toca archivos.
2. **El ajuste temporal de la capa 3** (acuerdo 12 del pendiente 116): cuando una regla frena algo legítimo y no hay herramienta, se suspende para ese proyecto desde la pantalla de Cimiento, con motivo y fecha de vencimiento, sin tocar código. Nunca se suspenden tapar las claves ni el histórico.
3. **El aviso del freno dice la salida:** en vez de solo «detenido», dice qué herramienta usar o qué regla suspender en Cimiento para hacerlo bien.

**Propuesta de acuerdo 1:** cuando el freno detiene algo legítimo, la salida nunca es tocar archivos o código a mano. Es la contraria que ofrece Cimiento o el ajuste temporal en su pantalla, y el aviso del freno dice cuál. Esto deja las tres capas dentro de este análisis y responde también si el principio es regla del estándar: lo es, porque protege a todos los proyectos.

¿Lo anoto así?

### 51 · Usuario, 2026-10-05 14:32:01
> explique mejor y aplique 00 id9

**Agente**, 2026-10-05 14:32:15
<!-- agente: a0ab5754-a8f0-4726-bb5c-ca4f484fe1a1 -->

Hoy el freno detuvo dos cosas correctas y la única salida fue editar archivos a mano. La propuesta es que eso no vuelva a pasar.

**Ejemplo con lo de hoy:** se creó una HU con el número equivocado y había que borrarla. El freno lo impidió, y hubo que borrar la carpeta a mano.

**Con la propuesta, hay dos salidas sin tocar archivos:**
1. **Una herramienta que deshaga:** `andamio quitar-hu` borra la HU completa, carpeta y fila de la épica. El freno la deja pasar, como hoy deja pasar al andamio que la crea.
2. **Si no hay herramienta:** se suspende esa regla solo para ese proyecto, desde la pantalla de Cimiento, con el motivo y la fecha en que vence. Tapar las claves y el histórico nunca se suspenden.

Además, cuando el freno detenga algo, su aviso dice cuál de las dos salidas usar.

**Acuerdo propuesto:** ante un bloqueo del freno, nunca se tocan archivos ni código a mano: se usa la herramienta que deshace o la suspensión temporal en Cimiento.

¿Lo anoto así?

### 52 · Usuario, 2026-10-05 14:34:33
> pregunta: osea desde la interfaz?

**Agente**, 2026-10-05 14:34:45
<!-- agente: eac75038-1e89-40a5-be48-324fe9245745 -->

Sí, desde la interfaz de Cimiento, en el navegador.

- **La suspensión temporal:** en «Proyectos», al entrar a un proyecto, se elige la regla o el enganche que frena, se escribe el motivo y la fecha en que vence, y se guarda. El freno la lee de la base y deja pasar la acción mientras no venza.
- **Las herramientas que deshacen**, como quitar una HU: las corre el agente cuando se le pide, igual que hoy el andamio que crea. Se pueden sumar como botones en la interfaz más adelante, si se quiere.

En ningún caso hay que abrir archivos ni tocar código.

### 53 · Usuario, 2026-10-05 14:36:44
> apruebo

**Agente**, 2026-10-05 14:38:04
<!-- agente: 8fdad1c4-0a13-49a8-aea8-4cce273bc3e8 -->

El enganche avisa del enlace roto que dejó la HU borrada en la épica. Es un defecto mío, así que lo quito.

Quedó anotado el acuerdo 1 del análisis 3: ante un bloqueo del freno, nunca se tocan archivos a mano. Se usa la herramienta que deshace o la suspensión temporal desde la interfaz, y el aviso del freno dice cuál. También quité de la épica la fila con el enlace roto de la HU borrada.

**La decisión que sigue: ¿«toda acción trae su contraria» es regla del estándar o criterio de Cimiento?**
- **Regla del estándar:** vale para todos los proyectos. Ningún plan que agregue una acción se aprueba sin su contraria y su prueba. Es versión MAYOR.
- **Criterio de Cimiento:** solo para las herramientas del estándar. Es versión MENOR.

**Recomiendo regla del estándar,** porque crear algo sin poder deshacerlo le puede pasar a cualquier proyecto.

### 54 · Usuario, 2026-10-05 14:44:14
> analicemos: el estándar y cimiento son lo mismo

**Agente**, 2026-10-05 14:44:27
<!-- agente: 6c69f37c-fdf7-46fb-8013-dff880507a58 -->

Correcto, y mi pregunta estaba mal planteada al separarlos. La diferencia real es otra: **a qué código se aplica.**

- **El código de Cimiento:** el andamio, el instalador, el freno, las pantallas. Ahí el principio aplica sí o sí, porque es lo que nos bloqueó hoy.
- **El código propio de cada proyecto que hereda Cimiento,** como scilit o agro-system. Si el principio entra a `base/` como regla, también les exige a esos proyectos que cada acción que construyan, por ejemplo «crear sesión», traiga su contraria, «borrar sesión».

**La pregunta, bien hecha: ¿el principio rige solo para el código de Cimiento, o también para lo que construye cada proyecto?**

Recomiendo que rija para todo. «Crear algo que no se puede deshacer» es un defecto en cualquier sistema, no solo en Cimiento. El costo es que en los proyectos, los planes nuevos declaran la contraria de cada acción que agregan.

### 55 · Usuario, 2026-10-05 14:45:31
> analicemos: para los proyectos también

**Agente**, 2026-10-05 14:46:11
<!-- agente: 9c284937-a43c-44a6-b8d4-b01c606b33e6 -->

Quedó anotado el acuerdo 2: es regla del estándar y rige también para lo que construye cada proyecto.

**La decisión que sigue: ¿qué contrarias que faltan se construyen?** Propongo todas las del inventario:

| Acción | Su contraria |
|---|---|
| El andamio crea una HU, fase o pendiente | `quitar`: si sigue siendo la plantilla, se borra; si ya tiene contenido, se archiva en vez de borrarse, para no perder trabajo |
| Instalar el estándar en un proyecto | `desinstalar`: quita enganches, tareas programadas y lo que puso la instalación, y deja lo propio del proyecto |
| Cerrar un pendiente | `reabrir`: lo devuelve de `hecho/` con sus enlaces |
| Cerrar una fase (HU-016) | `reabrir_fase` |
| Prender un análisis | Prenderlo desde un turno anterior |

Más el andamio con número: que cree la HU con el número que diga el análisis.

**Recomiendo todas, con el archivado** para lo que ya tiene contenido. Borrar trabajo escrito no tendría contraria, y eso rompe la misma regla.

### 56 · Usuario, 2026-10-05 14:48:41
> Analicemos: todo lo que se maneja por interfaz debe ser desde la DB

**Agente**, 2026-10-05 14:48:59
<!-- agente: 2db2c8ec-a748-4a71-8cb4-2393df6e645f -->

De acuerdo. Lo aterrizo con lo que hay hoy, porque cambia dos cosas.

**Ya viven en la base:** los proyectos, los niveles de las reglas, los límites, las cuentas y el gasto.

**Cambiarían a la base:**
1. **Las suspensiones temporales y la configuración en tres capas:** en la base, no en archivos. El `.agente/configuracion.md` que pide el acuerdo 12 del pendiente 116 sería una copia que Cimiento escribe desde la base para que el proyecto sepa qué tiene, nunca la fuente.
2. **El estado del análisis prendido,** que hoy es un archivo en `historico-chat/.estado/`. Si «prender desde un turno anterior» se maneja desde la interfaz, ese estado pasa a la base. Fue el archivo que hubo que editar a mano hoy.

**No cambian:** los documentos de la cadena (análisis, épicas, HU y planes) siguen siendo archivos del repositorio, versionados en git. La interfaz los crea o los quita con las herramientas (el andamio y su contraria), pero no los guarda en la base.

**Acuerdo propuesto:** todo dato que se maneja desde la interfaz vive en la base de Cimiento; lo que un proyecto necesite como archivo es una copia generada desde la base. Los documentos de la cadena siguen en el repositorio.

¿Lo anoto así?

### 57 · Usuario, 2026-10-05 14:50:56
> apruebo

**Agente**, 2026-10-05 14:51:50
<!-- agente: 2a95c4b1-9c31-4947-a91f-28e70d5cb393 -->

Corrijo los turnos citados en los tres acuerdos, que quedaron corridos en uno.

Quedó anotado el acuerdo 3: lo que se maneja desde la interfaz vive en la base, y los archivos que un proyecto necesite son copias generadas desde ella. También corregí los turnos citados en los tres acuerdos, que estaban corridos en uno.

**Sigue abierta la propuesta de las contrarias que faltan:**
- `quitar` para lo que crea el andamio: si es plantilla, la borra; si ya tiene contenido, la archiva.
- `desinstalar` el estándar de un proyecto.
- `reabrir` un pendiente.
- `reabrir_fase`.
- Prender un análisis desde un turno anterior.
- El andamio con número.

Recomiendo todas, con el archivado para lo que ya tiene contenido.

### 58 · Usuario, 2026-10-05 14:52:59
> apruebo

**Agente**, 2026-10-05 14:53:40
<!-- agente: 722794d7-aa2b-4eda-9385-b2e60b4f7011 -->

Quedó anotado el acuerdo 4: se construyen todas las contrarias que faltan, con el archivado para lo que ya tiene contenido, y el andamio crea la HU con el número del análisis.

**Queda una decisión: la configuración en tres capas** del acuerdo 12 del pendiente 116.
1. **Base de Cimiento,** común a todos: enganches y reglas obligatorias.
2. **Configuración del proyecto,** en «Proyectos»: prende o apaga lo que no es obligatorio. Ahí van «Rutas en los avisos» y los límites.
3. **Ajuste temporal del proyecto:** suspende una regla o un enganche que frena, con motivo y vencimiento. Es la salida del acuerdo 1.

Reemplaza los dos niveles del acuerdo 3 del análisis 2 y amplía la HU-013. Por el acuerdo 3 de este análisis, todo vive en la base, y `.agente/configuracion.md` es una copia generada desde ella. Nunca se suspenden tapar las claves ni el histórico.

**Recomiendo tomarla tal cual,** porque ya está aprobada en el pendiente 116 y encaja con los acuerdos 1 y 3 de aquí.

### 59 · Usuario, 2026-10-05 14:55:21
> apruebo

**Agente**, 2026-10-05 14:55:55
<!-- agente: 57426843-cc1a-4e0b-89c2-520e5bd9247e -->

Quedó anotado el acuerdo 5: la configuración en tres capas reemplaza los dos niveles del análisis 2. El análisis 3 ya no tiene decisiones abiertas.

**Sus cinco acuerdos:**
1. Ante un bloqueo del freno, nunca se tocan archivos a mano: se usa la herramienta que deshace o la suspensión temporal desde la interfaz.
2. «Toda acción trae su contraria» es regla del estándar, para Cimiento y para los proyectos.
3. Lo que se maneja desde la interfaz vive en la base.
4. Se construyen todas las contrarias que faltan, con el andamio creando la HU con el número del análisis.
5. La configuración va en tres capas.

**Lo que sigue:** escribir el resto del análisis 3 (hallazgo, aportes, HU y «Lo que se tiene que hacer») y presentarlo para «Apruebo el análisis». Para que lo escriba, el mensaje empieza con «Hágalo».

### 60 · Usuario, 2026-10-05 14:56:44
> Hágalo

**Agente**, 2026-10-05 15:03:46
<!-- agente: 0529c0c4-1f02-485f-a9d0-3017d01471cd -->

Escribo el resto del análisis 3. Antes registro las lecciones como señales, para tener sus números.

Reviso cómo numera el andamio, para escribir con precisión la fila que lo corrige.

Hago la fila 1: paso el hallazgo y el pendiente a su versión 4.

Ahora la fila 4, que este análisis hace de una: el andamio crea la HU con el número que se le pida. Miro cómo prueban el andamio las pruebas actuales, para escribir las nuevas igual.

Cambio el andamio.

El freno dejó cambiar `andamio.py` pero no crear `tests_andamio.py`, aunque la fila 4 nombra los dos. Y una prueba que ya existía da error. Veo cuál.

Las rutas del análisis incluyen `tests_andamio.py`; el bloqueo fue de antes de que el freno releyera la fila. Lo intento de nuevo.

El análisis 3 quedó escrito, y la fila 1 (hallazgo y pendiente en versión 4) ya está hecha. Me frené en la fila 4.

**Lo que pasó:**
- El cambio del andamio entró: `andamio hu ... --numero 16` crea la HU con ese número y rechaza uno que ya exista.
- Sus pruebas no entraron. El freno no deja crear `tests_andamio.py`, aunque la fila 4 lo nombra y el mismo freno, consultado aparte, dice que esa ruta está permitida. Es un defecto del freno: lo que dice que permite no coincide con lo que deja hacer cuando corre como enganche.

No lo salto ni lo hago por otro camino.

**Lo que necesito:** un mensaje que empiece con «Corrija». Esa palabra deja corregir las herramientas del proceso por una respuesta. Con ella busco por qué el enganche no ve la ruta, lo corrijo, escribo las tres pruebas del andamio y las corro.

Después queda presentar el análisis 3 para «Apruebo el análisis».

### 61 · Usuario, 2026-10-05 15:06:03
> Corrija

**Agente**, 2026-10-05 15:09:54
<!-- agente: 07cd6901-d42d-4865-ab9e-1fb368240bf9 -->

Busco la causa simulando el enganche del freno con la misma escritura que bloqueó.

En la simulación el freno deja pasar la escritura. Lo intento de nuevo con la herramienta.

Ahora entró. Confirmo la causa: el bloqueo pasó mientras la carpeta de trabajo de la sesión era `proyectos/cimiento`. Repito la simulación corriendo el enganche desde esa carpeta.

Pasan las 6. Marco hecha la fila 4 y anoto el hallazgo del freno en el resumen de la sesión.

Sumo esa corrección del freno como fila del análisis, dentro de la HU-024, y valido el análisis.

El validador no le encuentra fallas al análisis 3; las dos que reporta son las viejas del pendiente 103. Ajusto la HU-024 para que cubra también la fila 11.

El análisis 3 está escrito y el validador no le encuentra fallas; las dos que reporta son de análisis viejos del pendiente 103.

**Lo que dejó «Corrija»:**
- La fila 4 está hecha: el andamio crea la HU con el número que se le pida (`--numero`) y rechaza uno que ya exista. Pasan sus 3 pruebas y las 3 que ya tenía.
- El bloqueo del freno no lo pude reproducir: con «Corrija» activo, el freno deja pasar todo lo de herramientas. Lo anoté como H-8 en el resumen de la sesión y como fila 11 del análisis, para corregirlo en la HU-024 con «Corrija» apagado. También va ahí otro defecto que vi: al revisar un comando de Bash, el freno no tiene en cuenta el `cd`.

**El análisis 3 propone:**
- El hallazgo y el pendiente en versión 4, ya pasados a sus originales.
- Seis HU nuevas en EP-025: 019 (la regla de la contraria), 020 (quitar lo que crea el andamio), 021 (desinstalar), 022 (reabrir un pendiente), 023 (prender un análisis desde un turno anterior) y 024 (el aviso del freno dice la salida).
- Dos ampliaciones: la HU-013 pasa a tres capas y la HU-016 suma `reabrir_fase`.

Para aprobarlo: «Apruebo el análisis».

### 62 · Usuario, 2026-10-05 15:11:56
> pregunta: cuál es problema que desató este análisis y ya quedó aclarado?

**Agente**, 2026-10-05 15:12:09
<!-- agente: 8714ec00-9e01-4b44-bd87-2bf271abbf09 -->

**El problema que lo desató:** el andamio creó una HU con el número equivocado (011 en vez de 016) y no había forma de deshacerlo. El freno bloqueó borrarla y hubo que hacerlo a mano. Lo mismo pasó al querer que el análisis tomara la conversación desde antes: hubo que editar a mano el archivo de estado.

**Ya quedó aclarado, en el análisis:**
- La causa: Cimiento tiene acciones que crean pero no las que deshacen, y el freno, cuando bloquea, no ofrece salida (acuerdos 1, 2 y 4).
- El número: ya está resuelto. El andamio crea la HU con el número que le diga el análisis, con sus pruebas pasando (fila 4).
- La carpeta mal numerada ya no está, y su fila de la épica la quité.

**No quedó aclarado del todo:** por qué el freno bloqueó `tests_andamio.py` si la fila del análisis lo permitía. No se pudo reproducir con «Corrija» activo. Queda como H-8 y fila 11, para corregirlo en la HU-024.

**Lo que falta:** construir las contrarias (quitar, desinstalar, reabrir, prender desde un turno anterior), la suspensión desde la interfaz y el aviso del freno con la salida. Eso es lo que aprueba el análisis.

### 63 · Usuario, 2026-10-05 15:13:13
> pregunta entonces que hago?

**Agente**, 2026-10-05 15:13:27
<!-- agente: 53b5db57-ab47-40fc-b549-effcd9b05eea -->

Si el análisis 3 refleja lo que se acordó, el siguiente paso es aprobarlo con este mensaje:

> Apruebo el análisis

Con eso queda la orden de construir todo lo de los análisis 2 y 3 en EP-025: las 14 HU nuevas (de la 011 a la 024) y las ampliaciones de la HU-013 y la HU-016. Arranco por la HU-020 (quitar lo que crea el andamio) y la HU-016 (cerrar y reabrir fases). Desde ahí sigo sin pedir aprobación de planes ni de fases; solo pregunto el commit, lo que no se pueda deshacer y lo que salga del alcance.

Si algo del análisis no quedó bien, se dice antes de aprobar y lo corrijo.

### 64 · Usuario, 2026-10-05 15:14:10
> Apruebo el análisis

**Agente**, 2026-10-05 15:14:30
<!-- agente: e400b770-f09a-47a5-a9d6-8567dd5aba79 -->

Quedó aprobado el análisis 3 del pendiente 119, con la marca del programa en el turno 64. Con este y el análisis 2 queda la orden de construir en EP-025 las HU-011 a HU-024, más la HU-013 en tres capas y la HU-016 con `reabrir_fase`.

**Orden de construcción:**
1. HU-020: quitar lo que crea el andamio.
2. HU-016: cerrar y reabrir fases, y separar los cambios por sesión.
3. HU-019: la regla de la contraria.
4. HU-022, HU-023 y HU-021: reabrir un pendiente, prender un análisis desde un turno anterior y desinstalar.
5. HU-011 y HU-012: el proceso que carga la base y quitar la telemetría.
6. HU-013 y HU-014: las tres capas y las rutas de los avisos.
7. HU-024: el aviso del freno, con la corrección del H-8.
8. HU-015, HU-017 y HU-018: lo que corre sin tokens, el freno ante guiones repetidos, y la ayuda y el manual.

Arranco con el próximo mensaje, sin pedir aprobación de planes ni de fases. Solo voy a preguntar el commit, lo que no se pueda deshacer y lo que salga del alcance.

> acá termina la conversación

---

## Lo acordado

> Se escribe en el mismo turno en que el usuario acepta algo: un punto por cada decisión, con su tema y el turno de la conversación donde se acordó.

1. Salida ante un bloqueo del freno: cuando el freno detiene algo legítimo, nunca se tocan archivos ni código a mano. La salida es la herramienta que deshace (por ejemplo `andamio quitar-hu`, que quita la carpeta y su fila de la épica, y que el freno deja pasar como al andamio que crea) o, si no hay herramienta, la suspensión temporal de esa regla o ese enganche para ese proyecto, desde la interfaz de Cimiento, con motivo y fecha de vencimiento; nunca se suspenden tapar las claves ni el histórico. El aviso del freno dice cuál de las dos salidas usar (turnos 49 a 53).

2. Toda acción trae su contraria: es regla del estándar (el estándar y Cimiento son lo mismo) y rige para el código de Cimiento y para lo que construye cada proyecto que lo hereda. Ninguna acción que crea o cambia algo se da por terminada sin la acción que lo deja como estaba, y su prueba; los planes nuevos la declaran (turnos 54 y 55).
3. Lo que se maneja desde la interfaz vive en la base de Cimiento: los niveles, los límites, los ajustes en sus capas, las suspensiones temporales y el estado del análisis prendido, que hoy es un archivo de `historico-chat/.estado/`. Lo que un proyecto necesite como archivo, como `.agente/configuracion.md`, es una copia que Cimiento genera desde la base, nunca la fuente. Los documentos de la cadena (análisis, épicas, HU y planes) siguen siendo archivos del repositorio, que la interfaz crea o quita con las herramientas (turnos 56 y 57).
4. Las contrarias que faltan se construyen todas: `quitar` para lo que crea el andamio (HU, fase o pendiente), que borra si sigue siendo la plantilla y archiva si ya tiene contenido, para no perder trabajo; `desinstalar` el estándar de un proyecto, que quita los enganches, las tareas programadas y lo que puso la instalación, y deja lo propio del proyecto; `reabrir` un pendiente cerrado, con sus enlaces; `reabrir_fase`, contraria de `cerrar_fase`; y prender un análisis desde un turno anterior. El andamio crea una HU con el número que le diga el análisis (turnos 55 a 58).

5. Configuración en tres capas, como el acuerdo 12 del análisis 1 del pendiente 116: la base de Cimiento, común a todos, con los enganches y las reglas obligatorias; la configuración del proyecto en «Proyectos», que prende o apaga lo que no es obligatorio, y donde van «Rutas en los avisos» y los límites de tokens; y el ajuste temporal del proyecto, que suspende una regla o un enganche que frena, con motivo y vencimiento (la salida del acuerdo 1). Nunca se suspenden tapar las claves (`00·N6`) ni el histórico. Todo vive en la base (acuerdo 3), y `.agente/configuracion.md` es una copia generada desde ella. Reemplaza los dos niveles del acuerdo 3 del análisis 2 y amplía la HU-013 (turnos 58 y 59).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

> Cada subsección es obligatoria: el validador detiene el cierre si falta una. Lo que aportan el usuario y Claude queda en la conversación y no se repite aquí.

### Cimiento: las reglas que aplican y las que chocan

Aplican `02·F8` (el freno, que hoy no ofrece salida), `00·N6` (tapar las claves nunca se suspende), `00·N3` (no saltar el freno: la salida tiene que estar prevista), `20·M10` (la regla nueva sube la versión mayor) y las meta-reglas de una regla nueva (`20·M3`, `20·M4`, `20·M5`, `20·M12`), que sigue la HU-019.

Chocan dos cosas, y se resuelven así:
- El freno bloquea con razón lo que no está en un plan, y eso dejó al usuario editando archivos (turnos 39 a 50). Lo resuelve el acuerdo 1: la salida es una herramienta o una suspensión temporal (puntos 3 y 8).
- El acuerdo 3 del análisis 2 pedía dos niveles de configuración, y el acuerdo 12 del análisis 1 del pendiente 116, tres. Lo resuelve el acuerdo 5: tres capas (punto 2).

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| Contrarias | Ninguna en `core/`: el andamio crea HU, fases y pendientes pero no los quita; la instalación no se deshace; `cerrar.py` cierra pendientes y no los reabre |
| Número de una HU | `Andamio.siguiente_hu` toma el siguiente al mayor; no deja pedir uno. Así nació la HU-011 con el número de la HU-016 del análisis 2 |
| Estado del análisis prendido | Un archivo en `historico-chat/.estado/analisis-en-curso/`, que solo escribe la herramienta; prende desde el turno actual |
| Suspensión de una regla | No existe; los niveles por proyecto (frena, avisa, apagada) son permanentes y no llevan motivo ni vencimiento |
| Aviso del freno | Dice la regla y que vuelve al análisis; no dice cómo salir |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Análisis 1 del pendiente 116, acuerdo 12 | Confirma las tres capas y lo que nunca se suspende; lo recoge el acuerdo 5 |
| Análisis 2 del pendiente 119, acuerdo 3 | Lo reemplaza el acuerdo 5 |
| Lo de la HU-011 mal numerada (turnos 39 a 47) | Muestra el intento que falló: crear sin poder deshacer; lo recogen los acuerdos 1 y 4 (lecciones 1 y 2) |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | Versión MAYOR por la regla nueva: los planes nuevos de cada proyecto declaran la contraria de cada acción que agregan. `02·F22` no aplica: no se deroga ninguna regla |
| Normas y leyes | Ninguna nueva |
| Herramientas | El freno corre en cada acción del agente y lee la base sin Django: la suspensión tiene que leerse igual, en la misma consulta |

### Dónde más puede pasar

> Lo que destapó el hallazgo puede pasar en otros sitios, otros proyectos u otras herramientas. Cada caso dice qué lo cubre: un punto de «Lo que se tiene que hacer», un punto de «Lo acordado» o la razón por la que no hace falta cubrirlo. Ningún caso queda sin esa columna.

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Un proyecto construye algo sin su contraria | Cualquier proyecto | Lo mismo de hoy, en su código | Acuerdo 2: regla del estándar (punto 1) |
| Una suspensión que se olvida | Cualquier proyecto | La regla queda apagada para siempre | Acuerdo 5: toda suspensión tiene vencimiento, y Cimiento la muestra (punto 2) |
| Se intenta suspender tapar las claves | Cualquier proyecto | Un secreto entra al repositorio | Acuerdo 5: `00·N6` y el histórico nunca se suspenden (punto 2) |
| Quitar algo que ya tiene trabajo | Andamio | Se pierde lo escrito | Acuerdo 4: se archiva, no se borra (punto 4) |
| Otra sesión crea una HU al mismo tiempo | Andamio | Dos HU con el mismo número | La razón: el andamio rechaza un número que ya existe (punto 3) |

---

## Propuesta final: hallazgo y pendiente V«N+1», épica y HU

> Así quedan el hallazgo y el pendiente según lo que concluyó el análisis, con solo los campos que les corresponden. Antes de aprobar, se pasan a los originales con la conversación prendida, para que el cambio quede en el análisis: el hallazgo en el resumen de su sesión y el pendiente en su archivo. Después de aprobar no se cambia nada.

### Hallazgo V4. El gasto no llega en vivo, lo repetido no se automatiza, y lo que Cimiento hace no siempre se puede deshacer

| Campo | Valor |
|---|---|
| Qué pasó | A lo de la versión 3 se suma que Cimiento crea sin poder deshacer: el andamio creó una HU con el número equivocado y no había cómo quitarla, y el freno, que bloqueó con razón, no ofrecía salida; el usuario tuvo que borrar la carpeta y editar el estado del análisis a mano |
| Por qué importa | Cada acción sin contraria y cada bloqueo sin salida terminan en el usuario tocando archivos, que es lo que el freno quiere evitar, en Cimiento y en todo proyecto que lo herede |

### Pendiente V4. El gasto no llega en vivo, lo repetido no se automatiza, y lo que Cimiento hace no siempre se puede deshacer

| Campo | Valor |
|---|---|
| De dónde sale | El hallazgo V4, «El gasto no llega en vivo, lo repetido no se automatiza, y lo que Cimiento hace no siempre se puede deshacer» |
| El problema | A lo de la versión 3 se suma: la regla de que toda acción trae su contraria; quitar lo que crea el andamio, desinstalar, reabrir pendientes y fases, y prender un análisis desde un turno anterior; la configuración en tres capas con la suspensión temporal desde la interfaz, todo en la base; y que el aviso del freno diga la salida |
| Por qué importa | Sin contrarias ni salida prevista, los bloqueos se resuelven tocando archivos a mano |

### Épica y HU que salen del análisis

Las HU se suman a la épica [EP-025, Cimiento se administra y muestra el gasto de tokens en vivo](../../../../../documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md). Además, la HU-013 del análisis 2 pasa a tener tres capas (acuerdo 5) y la HU-016 suma `reabrir_fase` (acuerdo 4). Las HU de este análisis van antes de las del análisis 2, salvo la HU-024, que va después de la HU-013.

> El número identifica a la HU; el orden de construcción sale de sus dependencias. Una HU no va antes de otra de la que depende, y cada puesto dice por qué va ahí.

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | 020 | Lo que crea el andamio se puede quitar | El andamio crea sin poder deshacer, y el freno no deja borrar a mano | Ninguna | Es la salida que faltó hoy, y las demás HU ya pueden corregirse con ella | 5 |
| 2 | 019 | Toda acción trae su contraria | Ninguna regla pide la contraria de lo que se construye | Ninguna | Las HU que siguen ya la declaran | 2 |
| 3 | 022 | Un pendiente cerrado se puede reabrir | `cerrar.py` no tiene contraria | HU-019 | Cumple la regla con lo que ya existe | 7 |
| 4 | 023 | El análisis se prende desde un turno anterior, y su estado vive en la base | El estado del análisis es un archivo que hubo que editar a mano | HU-019 | Cumple los acuerdos 3 y 4 sobre lo que ya existe | 10 |
| 5 | 021 | El estándar se puede desinstalar de un proyecto | La instalación no se deshace | HU-019 | Es la contraria más grande; va cuando la regla ya rige | 6 |
| 6 | 024 | El aviso del freno dice cómo salir sin tocar archivos | El freno bloquea sin ofrecer salida | HU-013, HU-020 | Necesita la suspensión de la HU-013 y la herramienta de la HU-020 para nombrarlas | 9, 11 |

## Lecciones aprendidas

> Salen de lo que funcionó, para repetirlo, y de lo que falló, para no repetirlo. Cada una se escribe como señal de tipo `leccion` en la base de señales (`python memoria/memoria.py add --tipo leccion`) y aquí va el número que le da. «Recomendación» dice si la lección complementa una de las [recomendaciones](«RUTA-ESTANDAR»/plantillas/recomendaciones-del-analisis.md), crea una nueva o no aplica; antes de crear una se busca si ya existe.

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Toda acción que crea necesita la que deshace, o el freno obliga a tocar archivos a mano | Falló | S-306 | complementa R-1 |
| 2 | Lo que una herramienta crea junto se deshace junto, sin preguntar por partes | Falló | S-307 | complementa R-8 |

## Lo que se tiene que hacer

> Cada fila se convierte en un criterio de aceptación de una HU, y «Pasó a» dice cuál. Ninguna fila queda sin destino. «Sale de» cita de dónde sale, de una de tres formas: un número es un punto de «Lo acordado» de este análisis, «Análisis N, acuerdo M» es un acuerdo de otro análisis del mismo pendiente, y una regla del estándar, como `13·DOC26`, es lo que la regla exige. Lo que no tenga acuerdo no entra. La fila que se hace «de una y sin fase» nombra las rutas exactas que toca, entre comillas invertidas: mientras el análisis está prendido, el freno deja escribir esas y ninguna otra.
>
> La fila 1 va siempre, salvo en el análisis que origina el pendiente: pasar el pendiente a su versión siguiente, con el hallazgo de este análisis en «De dónde sale».

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Pasar el hallazgo y el pendiente a su versión 4 | `13·DOC26` | Este análisis, de una y sin fase: `historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/pendiente.md`, `historico-chat/resumenes/2026-10-04/sesion-2.md`, hecho el 2026-10-05 |
| 2 | Escribir la regla «toda acción trae su contraria»: ninguna acción que crea o cambia algo se da por terminada sin la que lo deja como estaba, y su prueba; rige para el código de Cimiento y para el de cada proyecto; versión MAYOR | 2 | `EP-025` HU-019 |
| 3 | Configuración en tres capas, toda en la base: la base de Cimiento con lo obligatorio; la del proyecto en «Proyectos», con «Rutas en los avisos» y los límites; y la suspensión temporal de una regla o un enganche, con motivo y vencimiento, que nunca alcanza a `00·N6` ni al histórico; `.agente/configuracion.md` es una copia generada desde la base | 3, 5 | `EP-025` HU-013 |
| 4 | El andamio crea una HU con el número que se le pida (`--numero`), y rechaza un número que ya existe | 4 | Este análisis, de una y sin fase: `proyectos/cimiento/core/herramientas/andamio.py`, `proyectos/cimiento/core/herramientas/tests_andamio.py`, hecho el 2026-10-05 |
| 5 | `andamio quitar` para una HU, una fase o un pendiente, con lo que el andamio creó junto (sus filas en la épica y en los índices): borra si sigue siendo la plantilla y archiva si ya tiene contenido; el freno la deja pasar como al andamio que crea | 1, 4 | `EP-025` HU-020 |
| 6 | `desinstalar` el estándar de un proyecto: quita los enganches, las tareas programadas y lo que puso la instalación, y deja lo propio del proyecto | 4 | `EP-025` HU-021 |
| 7 | `reabrir` un pendiente cerrado: lo devuelve de `hecho/` y arrastra sus enlaces, como `cerrar.py` | 4 | `EP-025` HU-022 |
| 8 | `reabrir_fase`, contraria de `cerrar_fase` | 4 | `EP-025` HU-016 |
| 9 | El aviso del freno dice la salida: la herramienta que deshace o la suspensión temporal en Cimiento | 1 | `EP-025` HU-024 |
| 10 | Prender un análisis desde un turno anterior, con el estado del análisis prendido guardado en la base | 3, 4 | `EP-025` HU-023 |
| 11 | El freno deja escribir toda ruta que el análisis prendido manda hacer «de una y sin fase», también un archivo nuevo, y resuelve las rutas de un comando de Bash teniendo en cuenta su `cd` (H-8 del resumen del 2026-10-04, sesión 3) | 1 | `EP-025` HU-024 |

## Lo que aporta al análisis principal

> Todo análisis se anota en el análisis principal de su alcance, aunque no cambie el sistema ([`13·DOC25`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC25-reescribe-el-analisis-principal-con-su-lista-de-cambios.md)). Al aprobar, el programa pasa tal cual lo que suma al final de la redacción del principal, y una fila con la fecha, el resultado y el enlace a su «Lista de análisis». Sin esta sección el análisis no se aprueba.

**Resultado:** amplía.

**Lo que suma al análisis principal:** toda acción de Cimiento y de los proyectos que lo heredan trae su contraria; lo que se maneja desde la interfaz vive en la base; la configuración de cada proyecto va en tres capas; y ante un bloqueo del freno la salida es una herramienta o una suspensión temporal, nunca tocar archivos a mano.
