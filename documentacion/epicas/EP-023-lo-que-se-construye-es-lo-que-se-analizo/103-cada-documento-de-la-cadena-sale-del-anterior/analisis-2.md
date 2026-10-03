# Análisis 2: el enganche del análisis solo sirve para un análisis

> **Aprobado** por el usuario el 2026-10-01, en el turno 173. Antes de aprobarlo, el pendiente pasó a la V3 en sus originales: [pendientes/103](../../../../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior.md) y [pendiente.md](pendiente.md). Desde ese momento este análisis no se reescribe.

> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Viene del [análisis 1](analisis-1.md), aprobado el 2026-10-01. Trata solo lo que falló y sus implicaciones sobre lo ya hecho (conclusión 19 del análisis 1).

---

## Hallazgo

### H-2. El enganche del análisis solo sirve para un análisis

| Campo | Valor |
|---|---|
| Qué pasó | El análisis 1 del pendiente 103 se llenó en tiempo real con un guion hecho solo para él, [crear_analisis_103.py](../../../../historico-chat/scripts/2026-09-30/crear_analisis_103.py), que tiene la ruta de ese análisis escrita adentro. Al aprobarlo hubo que apagarlo a mano en `.claude/settings.json`, y antes de apagarlo alcanzó a pasarle al análisis cerrado un turno posterior a la aprobación. El punto 29 del análisis pide una herramienta general, pero no dice cómo se prende ni cómo se apaga. |
| Por qué importa | Cualquier proyecto que herede Cimiento tendría que configurar a mano el enganche de cada análisis y acordarse de apagarlo al aprobar. Si no se acuerda, la conversación entra en un análisis que ya no se reescribe. |

## Pendiente

### Pendiente. Lo que se construye se aparta de lo aprobado

Reúne los pendientes 103, 104 y 105.

| Campo | Valor |
|---|---|
| De dónde sale | [H-13 de la sesión del 2026-09-28](../../../../historico-chat/resumenes/2026-09-28/sesion.md), que reúne H-10, H-11 y H-13 |
| El problema | No hay un documento que fije el alcance antes de la HU. Nada obliga a que cada documento salga del anterior. Nada detiene al agente cuando trabaja fuera del plan aprobado. Y la plantilla del plan no permite comprobarlo con un programa. |
| Por qué importa | Al ejecutar el plan aparecen hallazgos que se podían evitar, y cada uno se vuelve un pendiente más. |

---

## Conversación

> La pasa el enganche desde la [transcripción del día](../../../../historico-chat/2026-09-30-sesion.md), a partir del turno 142, el que sigue a la aprobación del análisis 1.

### 142 · Usuario, 2026-10-01 15:45:14
> si

**Agente**, 2026-10-01 15:45:58
<!-- agente: 05eef870-81b6-4ee7-92f3-a3e810c8f255 -->

El enganche quedó apagado. Quité sus dos entradas de [.claude/settings.json](../../../../.claude/settings.json) y comprobé que el archivo sigue siendo válido.

Antes de apagarlo, el enganche alcanzó a pasar al análisis el «sí» de este mensaje. Lo quité, y la conversación del análisis termina ahora en el turno 141, el de la aprobación, con su respuesta.

Sigue crear el análisis principal de Cimiento en `analisis/`. Para eso hay que revisar todo el proyecto, y es un trabajo grande. ¿Lo hacemos ahora o en una sesión nueva?

### 143 · Usuario, 2026-10-01 15:46:19
> y cuando lo necesite prender cómo lo hago?

**Agente**, 2026-10-01 15:46:29
<!-- agente: 14108b37-2a50-4d07-a787-7945627aa84b -->

Hoy no hay un interruptor. El guion actual solo sirve para este análisis: tiene la ruta del `analisis-1.md` escrita adentro, así que no se puede volver a prender para otro.

**Mientras no exista la herramienta general:** se pide con una orden, por ejemplo «Hágalo: prenda el enganche para el análisis X». El agente adapta el guion a ese análisis y vuelve a agregar las dos entradas en `.claude/settings.json`, igual que se hizo hoy.

**Con la herramienta general** (punto 29, HU 1), no habrá que prender ni apagar nada. La herramienta buscará sola el análisis que esté abierto, es decir, el que todavía no tenga la marca «Aprobado», y le irá pasando la conversación. Cuando el análisis se apruebe, dejará de escribirle sin que nadie lo apague. La marca de aprobación hace de interruptor.

Lo segundo es lo que se busca: que dependa del estado del análisis y no de que alguien se acuerde. ¿Se agrega eso al punto 29 como detalle de la HU 1?

### 144 · Usuario, 2026-10-01 15:52:32
> 
> Ahí está el problema: el enganche no debió crearse únicamente para este análisis, sino que debe funcionar para cualquier análisis de cualquier proyecto que implemente Cimiento.
>
> ¿Qué propone? ¿Volver a encender el enganche para analizar este tema que no se contempló inicialmente?
> 

**Agente**, 2026-10-01 15:52:47
<!-- agente: ffe9118c-336a-497f-9178-e8f85c6baa98 -->

No propongo volver a encenderlo. El análisis 1 ya está aprobado y no se reescribe, así que esto se resuelve con las reglas que el mismo análisis acaba de definir:

1. **Es un hallazgo que aparece después de aprobar** (conclusiones 10 y 19). No se reabre el análisis 1: se abre el **análisis 2** del mismo pendiente, que trata solo lo que falló y lo que eso implica.
2. **Qué falló:** el punto 29 ya pedía una herramienta general, pero no decía cómo se prende y se apaga. El piloto usó un guion hecho solo para este análisis, y eso es justo lo que el usuario está señalando.
3. **La conversación no se pierde.** La transcripción del día la sigue escribiendo el enganche del histórico, que funciona para cualquier sesión. Al cerrar el análisis 2, sus turnos se copian una sola vez desde ahí.

Así, el análisis 2 queda como la primera prueba real del ciclo: hallazgo, nuevo análisis y versión siguiente. No se repite el error de hacer otro guion para un solo análisis.

Pasos:
1. Anotar el hallazgo en el resumen de hoy, solo con «Qué pasó» y «Por qué importa».
2. Abrir `analisis-2.md` en la misma carpeta, desde el borrador de la plantilla.
3. Analizar ahí cómo se prende y se apaga la herramienta general en cualquier proyecto.

¿Arranco?

### 145 · Usuario, 2026-10-01 15:54:30
> si

**Agente**, 2026-10-01 15:55:44
<!-- agente: bf840213-0697-446a-acb4-04c5e9735318 -->

Ya quedó abierto el análisis 2.

- **El hallazgo H-2**, «El enganche del análisis solo sirve para un análisis», quedó en el [resumen de hoy](../../../../historico-chat/resumenes/2026-09-30/sesion.md), solo con «Qué pasó» y «Por qué importa», y con el enlace a su pendiente.
- **El [analisis-2.md](analisis-2.md)** se armó desde el borrador de la plantilla. Tiene la copia del H-2, la del pendiente vigente y una nota que dice que su conversación empieza en el turno 145 de la transcripción y se copia al cerrar.

Los enlaces funcionan y quité las marcas que señaló el revisor.

Para empezar el análisis, esta es la pregunta de fondo: en una misma sesión se puede hablar de varias cosas, y puede haber más de un análisis abierto. **¿Cómo sabe la herramienta qué parte de la conversación le pertenece a cada análisis?**

Mi propuesta es que el propio análisis lo declare, como ya lo hace este:
- **Prender:** al abrir un análisis se anota la sesión y el turno donde empieza. Desde ese turno, la herramienta le pasa la conversación.
- **Apagar:** la marca «Aprobado» indica el último turno. Ahí la herramienta deja de escribirle, sin que nadie la apague a mano.

Así no hay interruptor: el estado del análisis decide. ¿Así funciona, o la conversación debe asignarse de otra forma?

### 146 · Usuario, 2026-10-01 16:00:03
> en este caso debe arrancar desde donde se aprobo el anterior

**Agente**, 2026-10-01 16:00:25
<!-- agente: 9d813109-66b7-48ca-81be-80574e70fe07 -->

Corregido. El análisis 2 arranca en el turno 142, que es el que sigue a la aprobación del análisis 1. Desde ahí, lo que se habló ya forma parte del hallazgo nuevo. Quedó como su conclusión 1.

Con eso, el encendido y el apagado quedarían así:

| Momento | Qué decide |
|---|---|
| **Prender**, si es el primer análisis | El turno donde se abre |
| **Prender**, si es un análisis siguiente | El turno que sigue a la aprobación del anterior |
| **Apagar** | La marca «Aprobado», que dice el último turno |

¿Así queda, o el apagado también necesita otra condición?

### 147 · Usuario, 2026-10-01 16:01:44
> que recomienda que no sea tan manual pero que también se pueda controlar

**Agente**, 2026-10-01 16:01:57
<!-- agente: 49df7f7a-56fb-40a7-8318-3983105b6f43 -->

Propongo usar las palabras clave que ya existen (`01·C28`). El sistema ya lee la palabra con que abre cada mensaje, así que basta con que la herramienta la escuche:

| Momento | Qué lo dispara | Qué hace la herramienta |
|---|---|---|
| **Prender** | Un mensaje que abre con «Analicemos» y nombra el pendiente: «Analicemos: el pendiente 103» | Si no hay un análisis abierto de ese pendiente, crea el siguiente desde la plantilla, con la copia del hallazgo y del pendiente, y empieza a pasarle la conversación |
| **Seguir** | Cualquier mensaje mientras ese análisis esté abierto | Agrega el turno |
| **Pausar** | «Pare» | Deja de pasar la conversación sin cerrar el análisis. Se reanuda con «Continúe» |
| **Apagar** | «Apruebo el análisis» | Pone la marca «Aprobado» con el número del turno y deja de escribirle |

**El control** está en dos cosas:
- **Un aviso en cada turno** que dice a qué análisis se está pasando la conversación, o que no hay ninguno abierto. Si se ve un aviso equivocado, se corrige en el momento.
- **Un archivo de estado visible**, por ejemplo `historico-chat/.estado/analisis-en-curso`, con una sola línea: qué análisis está abierto. Se puede leer o corregir a mano si algo falla.

Un cuidado: el cierre exige «Apruebo **el análisis**» y no solo «Apruebo», porque «Apruebo» también se usa para aprobar planes y commits. Así un «Apruebo» suelto no cierra un análisis por error.

¿Así funciona?

### 148 · Usuario, 2026-10-01 16:08:21
> Ya está prendido?
> no me parece: "seguir" porque realmente lo que importa es:
> - Prender para arrancar el análisis
> - Pausar para parar el análisis porque que lo que no es parte del análisis
> - Apagar porque ya se aprueba el análisis
> Soy claro?

**Agente**, 2026-10-01 16:08:45
<!-- agente: 0cfbcd5e-fc39-461d-ab22-9f01cf0a7492 -->

**No está prendido.** El enganche sigue apagado desde la aprobación del análisis 1. No se pierde nada, porque la transcripción del día sí se está escribiendo, y al cerrar el análisis 2 sus turnos se copian desde ahí, a partir del 142.

**Sí, es claro.** «Seguir» no es un control: es lo que pasa solo mientras el análisis está prendido. Quedan tres controles:

| Control | Para qué | Palabra |
|---|---|---|
| **Prender** | Arrancar el análisis | «Analicemos» más el pendiente |
| **Pausar** | Que lo que no es del análisis no entre en él. Se reanuda prendiendo otra vez | «Pare» |
| **Apagar** | Cerrar porque se aprobó | «Apruebo el análisis» |

Quedó en el análisis 2 como la conclusión 2. La conclusión 3 recoge el control: el aviso en cada turno y el archivo de estado visible.

Ese cambio deja algo por decidir. Si hay pausas, al copiar la conversación hay que saltarse los turnos pausados. Mi propuesta es que esos turnos se queden fuera del análisis, pero dejando una línea que diga «turnos X a Y en pausa», para que se note que ahí hubo un corte. ¿De acuerdo?

### 149 · Usuario, 2026-10-01 16:09:59
> si y prenda

**Agente**, 2026-10-01 16:11:10
<!-- agente: 76d35627-7e32-4baa-84ce-69f2849a5b2a -->

El análisis 2 ya está prendido y le entró la conversación desde el turno 142 hasta este mensaje.

Esta vez no hice otro guion para un solo análisis. El guion nuevo, [pasar_conversacion.py](../../../../historico-chat/scripts/2026-09-30/pasar_conversacion.py), no tiene la ruta de ningún análisis escrita adentro. La lee de un archivo de estado, `historico-chat/.estado/analisis-en-curso.txt`, que tiene tres líneas: qué análisis, qué transcripción y desde qué turno. Si el archivo no existe, no hace nada.

- **Prender:** escribir ese archivo.
- **Apagar:** borrarlo.

Es el paso intermedio hacia la herramienta general, y el enganche quedó en `.claude/settings.json`.

La conclusión 4 quedó anotada: los turnos en pausa no entran, y en su lugar queda una línea que lo dice.

Todavía faltan tres cosas, que son parte de lo que este análisis tiene que definir:
- Las palabras «Analicemos», «Pare» y «Apruebo el análisis» aún no prenden, pausan ni apagan nada. Por ahora el archivo de estado se cambia a mano.
- No hay aviso en cada turno.
- La pausa no está programada.

### 150 · Usuario, 2026-10-01 16:13:39
> no está aplicando la regla anti IA por que está saliendo esto: —

**Agente**, 2026-10-01 16:14:37
<!-- agente: 39863f51-7252-4cd0-b9fc-ccc8cd3ec895 -->

Tenía razón. Las rayas largas no venían de lo que yo escribo: salían del formato de la transcripción. El programa del histórico ([validadores/historico.py](../../../../validadores/historico.py), líneas 127 y 153) separa cada turno de su hora con una raya, así: `### 142 · Usuario — 2026-10-01`.

La transcripción está exenta de la regla, pero el análisis no, y al copiarla al análisis las rayas pasaban tal cual.

Lo corregí en el guion que pasa la conversación: ahora cambia esa raya por una coma en los encabezados (`### 142 · Usuario, 2026-10-01`). El análisis 2 ya quedó así. La única raya que queda es la de su propio mensaje, que se cita tal como lo escribió.

Queda una decisión sobre el análisis 1. Tiene los mismos encabezados con raya en todos sus turnos, pero está aprobado y no se reescribe. ¿Se corrige solo el formato de esos encabezados, que no cambia nada de lo que se dijo, o se deja como está?

### 151 · Usuario, 2026-10-01 17:07:14
> No entiendo la pregunta

**Agente**, 2026-10-01 17:07:32
<!-- agente: 88a750af-7270-42bd-a470-d0c7f1230eb4 -->

El análisis 1 también tiene las rayas, una en cada turno, por ejemplo `### 2 · Usuario — 2026-09-30`.

Habría que cambiarlas por comas, igual que en el análisis 2. Pero el análisis 1 ya está aprobado, y acordamos que un análisis aprobado no se toca.

Cambiar esas rayas por comas no cambia nada de lo que se dijo; solo arregla la forma. ¿Las cambio en el análisis 1 o lo dejo como está?

### 152 · Usuario, 2026-10-01 17:08:36
> dejémoslo así pero de acá en adelante se debe tener el fomrato

**Agente**, 2026-10-01 17:08:59
<!-- agente: 3b6259a8-b6f2-44d2-a014-7aa8eaa2503f -->

Listo. El análisis 1 se queda como está, y de aquí en adelante la conversación copiada va sin raya.

En el análisis 2 quedó así:
- **Conclusión 5:** al copiar la conversación, la raya de los encabezados de turno se cambia por una coma. Esto vale desde ahora.
- **Punto 1 de «Lo que se tiene que hacer»:** que la herramienta general lo haga sola. El guion actual ya lo hace.

### 153 · Usuario, 2026-10-01 17:10:07
> Bueno cuál es el tema que nos compete en este tema?

**Agente**, 2026-10-01 17:10:18
<!-- agente: 2e5a87a5-f8fd-4aa3-ae78-9986638e3090 -->

El tema del análisis 2 es el hallazgo H-2: **el enganche que pasa la conversación al análisis solo servía para un análisis**. Lo que hay que definir es cómo se prende y se apaga en cualquier análisis de cualquier proyecto que herede Cimiento.

**Ya decidido:**

| # | Conclusión |
|---|---|
| 1 | El análisis siguiente arranca en el turno que sigue a la aprobación del anterior |
| 2 | Hay tres controles: prender con «Analicemos» más el pendiente, pausar con «Pare» y apagar con «Apruebo el análisis» |
| 3 | El control se ve en dos lugares: un aviso en cada turno y un archivo de estado visible |
| 4 | Los turnos en pausa no entran; queda una línea que dice que hubo pausa |
| 5 | La conversación copiada va sin rayas |

**Falta decidir:**
1. Si en el mismo proyecto hay dos análisis abiertos, ¿a cuál le entra la conversación?
2. ¿Cómo llega todo esto a cada proyecto? Por ejemplo, si el instalador crea el archivo de estado y pone el enganche.
3. ¿Qué cambia en lo que ya se hizo? El punto 29 del análisis 1 y la HU 1 tendrían que incluir estos controles. Eso es lo que llevaría a la V3 del pendiente.
4. Llenar las cuatro partes: Cimiento, el proyecto, lo aprendido y el entorno.

¿Empezamos por el 1?

### 154 · Usuario, 2026-10-01 17:12:48
> si

**Agente**, 2026-10-01 17:13:01
<!-- agente: b564af42-6d1f-47ca-8844-e8505adf41fd -->

Hay tres caminos:

| Opción | Cómo funciona | Problema |
|---|---|---|
| **A. Solo uno prendido a la vez** | Puede haber varios análisis abiertos, pero solo uno recibe la conversación. Prender otro pausa el que estaba prendido | Ninguno de fondo |
| B. Cada mensaje dice a cuál va | El usuario nombra el análisis en cada mensaje | Es manual, y un olvido manda el turno al análisis equivocado |
| C. La herramienta adivina por el tema | Lee el mensaje y decide a cuál pertenece | No es confiable y no se puede controlar |

**Recomiendo A.** Separa dos cosas que hoy se confunden:
- **Abierto:** el análisis no se ha aprobado. Puede haber varios.
- **Prendido:** el análisis recibe la conversación. Solo uno a la vez.

Con «Analicemos: el pendiente X» se prende el análisis de X, y el que estuviera prendido queda en pausa, con su línea de «turnos en pausa». El aviso de cada turno dice cuál está prendido, así que nunca hay duda de a dónde va lo que se habla.

¿De acuerdo?

### 155 · Usuario, 2026-10-01 17:15:33
> me parece bien la A pero explíquela mejor

**Agente**, 2026-10-01 17:15:42
<!-- agente: 318a5fcb-cbd0-423c-9252-858f7317abb5 -->

Con un ejemplo de una mañana de trabajo:

| Turno | El usuario dice | Qué pasa |
|---|---|---|
| 10 | «Analicemos: el pendiente 103» | Se prende el análisis del 103. Desde aquí, todo lo que se hable entra en él |
| 11 a 20 | Se discute el 103 | Esos turnos entran en el análisis del 103 |
| 21 | «Analicemos: el pendiente 110» | Se prende el análisis del 110, y el del 103 queda **en pausa**. El 103 sigue abierto: solo deja de recibir |
| 22 a 30 | Se discute el 110 | Entran en el 110, no en el 103 |
| 31 | «Analicemos: el pendiente 103» | Vuelve a prenderse el 103 y el 110 queda en pausa. En el 103 queda una línea: «turnos 21 a 30 en pausa» |
| 40 | «Apruebo el análisis» | Se cierra el que está prendido, el del 103, y ya ninguno recibe la conversación |

Es como una grabadora con varios casetes: se pueden tener varios a la mano (**abiertos**), pero solo uno graba a la vez (**prendido**). Cambiar de casete detiene el que estaba grabando, sin borrarlo.

En cada turno, el aviso dice cuál es el prendido, por ejemplo «la conversación está entrando al análisis del pendiente 110». Así nunca hay duda de a dónde va lo que se habla.

### 156 · Usuario, 2026-10-01 17:19:30
> No debería haber análisis sin que se complete su respectivo plan de trabajo, porque eso terminaría convirtiéndose en un problema: podrían quedar varios análisis abiertos o pendientes haciendo referencia a lo mismo y generando trabajo duplicado.

**Agente**, 2026-10-01 17:19:42
<!-- agente: 52ada76a-cadc-4d8f-9eaa-0c59ee357f0e -->

Entonces la pregunta 1 desaparece. Si no se abre un análisis nuevo hasta que se cumpla el plan del anterior, nunca hay dos análisis abiertos y no hay que elegir a cuál entra la conversación.

Al aplicarlo aparecen dos casos que conviene dejar dichos:

1. **El análisis siguiente del mismo pendiente sí se puede abrir.** Es lo que pasa hoy: el análisis 1 está aprobado pero su plan no se ha ejecutado, y se abrió el análisis 2 por un hallazgo sobre el mismo pendiente. No es un análisis nuevo de otro tema: es la vuelta del mismo ciclo (conclusiones 10 y 19), y reemplaza al anterior como el abierto.
2. **Un tema distinto que surja mientras tanto no abre análisis.** Se anota como hallazgo en el resumen de la sesión, solo con «Qué pasó» y «Por qué importa», y espera a que se cumpla el plan en curso.

La pausa sigue sirviendo, pero para otra cosa: dejar fuera del análisis lo que se habla en la sesión y no es parte de él, como una pregunta suelta o un commit.

¿Así queda?

### 157 · Usuario, 2026-10-01 17:42:32
> 1. Realmente lo que se está haciendo es mejorando el pendiente con un nuevo hallazgo
> 2. 
> 
> De todas maneras, se debe abrir un nuevo análisis porque el hallazgo surge durante la ejecución del plan de trabajo que se está realizando, como ya nos pasó anteriormente. Sin embargo, primero se deben analizar y validar las diferentes posibilidades para determinar si el hallazgo realmente hace parte del plan de trabajo actual o si corresponde a algo diferente.
>
> A partir de ese análisis se debe determinar dónde corresponde darle solución. Si se concluye que el hallazgo hace parte del plan de trabajo actual, primero se debe resolver, ya que está afectando el trabajo que se está ejecutando y no tendría sentido continuar sin solucionarlo.
>
> Si el hallazgo hace parte del plan de trabajo actual, el pendiente existente debe mejorarse para incorporar lo determinado en el nuevo análisis. Si, por el contrario, se determina que no hace parte del plan actual, se debe crear su respectivo pendiente y continuar con el proceso que corresponda.
>
> En cualquiera de los casos, el nuevo análisis debe dejar claro qué se determinó y dónde debe aplicarse. Si corresponde al plan actual, se debe dar prioridad y resolver antes de continuar con el trabajo en curso; si no corresponde, debe continuar por su propio proceso sin afectar el plan que ya se está ejecutando.
> 

**Agente**, 2026-10-01 17:43:02
<!-- agente: 5358f9a0-520c-4822-a953-c0dd14b0b126 -->

Entendido. Quedó así en el análisis 2:

**Conclusión 6, un solo análisis abierto.** No se abre el análisis de otro pendiente mientras no se cumpla el plan del que está abierto. El análisis siguiente del mismo pendiente no cuenta como otro: mejora el pendiente con el hallazgo nuevo, que es lo que está pasando hoy.

**Conclusión 7, qué hace el análisis de un hallazgo.** Todo hallazgo que surge al ejecutar el plan abre un análisis nuevo, y lo primero que hace ese análisis es decidir:

```
¿El hallazgo es parte del plan en curso?
├── Sí → tiene prioridad: el pendiente actual se mejora y se resuelve
│        antes de seguir con el plan
└── No → se crea su propio pendiente, sigue su proceso,
         y el plan en curso continúa sin tocarse
```

En los dos casos, el análisis deja claro qué se determinó y dónde se aplica.

Con esto, la pregunta de los dos análisis abiertos ya no aplica. Quedan dos por resolver:
1. Cómo llega todo esto a cada proyecto que hereda Cimiento.
2. Qué cambia en el punto 29 del análisis 1 y en la HU 1.

¿Seguimos con la 1?

### 158 · Usuario, 2026-10-01 17:44:19
> estas: "pasted_content" etiquetas no deben quedar

**Agente**, 2026-10-01 17:45:02
<!-- agente: 0d95c568-0953-4a4a-9c82-6338dc634172 -->

Listo. El guion que pasa la conversación ahora quita las etiquetas `pasted_content`, que marcan el texto pegado, y también las de «archivo abierto en el editor». Ninguna de las dos son palabras del usuario.

El análisis 2 ya quedó limpio. La única mención que queda es la de su propio mensaje, que nombra la etiqueta.

Agregué esto al guion actual. Como la herramienta general sale de él, también lo va a hacer.

### 159 · Usuario, 2026-10-01 17:49:10
> sigamos con las preguntas de: 157

**Agente**, 2026-10-01 17:49:24
<!-- agente: b56e4e01-da0e-4545-8248-e19c7e638137 -->

Seguimos con la primera: **cómo llega todo esto a cada proyecto que hereda Cimiento.** Propongo que llegue igual que los demás enganches, sin que nadie configure nada a mano (conclusión 47 del análisis 1):

| Pieza | Dónde vive | Cómo llega al proyecto |
|---|---|---|
| **La herramienta** que pasa la conversación | En `adaptadores/claude-code/`, junto a los demás enganches, y no en un guion de sesión | El instalador la agrega al `.claude/settings.json` de cada proyecto |
| **Las palabras** «Analicemos», «Pare» y «Apruebo el análisis» | Se leen con el mismo mecanismo que hoy lee la palabra clave de cada mensaje | Llegan con la herramienta |
| **El aviso en cada turno** | Lo escribe la herramienta, igual que los demás avisos que aparecen en cada mensaje | Llega con la herramienta |
| **El archivo de estado** | `historico-chat/.estado/analisis-en-curso.txt`, en cada proyecto | Lo crea la herramienta al prender y lo borra al apagar. El instalador no lo crea |
| **La plantilla del análisis** | `plantillas/analisis.md`, en el estándar | Se lee del estándar cada vez, como las demás plantillas |

Hay un detalle a tener en cuenta. La carpeta `.estado/` está fuera de git, así que el archivo de estado solo existe en la máquina donde se trabaja. Eso no es un problema: lo que manda es el análisis mismo, con su marca «Aprobado». Si se cambia de máquina, basta con volver a decir «Analicemos» para prenderlo.

¿De acuerdo?

### 160 · Usuario, 2026-10-01 17:53:06
> 00 id9

**Agente**, 2026-10-01 17:53:12
<!-- agente: fa6167e6-eb8b-413c-96a4-a9276c69f1b3 -->

Más corto:

Todo llega con el instalador, como los demás enganches:
- **La herramienta** pasa a `adaptadores/claude-code/` y el instalador la registra en cada proyecto.
- **Las palabras y el aviso** llegan con ella.
- **La plantilla** se lee del estándar.
- **El archivo de estado** lo crea la herramienta al prender y lo borra al apagar. Es local, porque `.estado/` no va a git, y eso no es problema: lo que manda es la marca «Aprobado» del análisis.

¿De acuerdo?

### 161 · Usuario, 2026-10-01 17:55:04
> si

**Agente**, 2026-10-01 17:55:31
<!-- agente: 07c4ccb3-9d4c-4d40-8901-b5ea6f9b1814 -->

Quedó como la conclusión 8.

**Última pregunta: qué cambia en lo que ya se hizo.** El análisis 1 está aprobado y no se toca. Según la conclusión 7, como este hallazgo es parte del plan en curso, lo que cambia es el pendiente:

| Documento | Cambio |
|---|---|
| **Pendiente V3** | «De dónde sale» suma el H-2. «El problema» suma una frase: «Y lo que pasa la conversación al análisis hay que configurarlo a mano para cada análisis». |
| **HU 1 de EP-023** | Recibe los puntos de lo que se tiene que hacer de este análisis: la herramienta general con sus tres controles, el aviso, el archivo de estado, la pausa, el formato sin rayas ni etiquetas, y que la instale el instalador. |
| **Punto 29 del análisis 1** | No se toca. Queda superado por los puntos de este análisis, que lo precisan. |

¿De acuerdo?

### 162 · Usuario, 2026-10-01 17:57:20
> si

**Agente**, 2026-10-01 17:58:38
<!-- agente: a9e5c473-6cb0-4786-9cab-2f0b0a235df6 -->

El análisis 2 quedó completo. En el [analisis-2.md](analisis-2.md) hay:

- **10 conclusiones**, cada una con su turno. La 9 dice qué cambia en lo ya hecho y la 10 trata las etiquetas.
- **Las cuatro partes llenas**:
  - Cimiento: `01·C28` y el «Apruebo» que choca con otros usos;
  - el proyecto: la transcripción, la palabra clave, los enganches y los dos guiones;
  - lo aprendido: la lección 11, S-082 y el turno 142;
  - el entorno: el instalador y la autorización de Claude Code.
- **La propuesta final.** El H-2 no cambia. El pendiente pasa a la V3, que suma el H-2 en «De dónde sale» y una frase en «El problema».
- **3 lecciones**: dos de lo que falló y una de lo que funcionó, que el ciclo hizo bien su primera vuelta.
- **8 puntos de lo que se tiene que hacer**: siete van a la HU 1 y uno a la HU 4.

Ya no tiene nada abierto y pasó el validador de redacción sin marcas. Para cerrarlo hace falta «Apruebo el análisis».

### 163 · Usuario, 2026-10-01 18:02:58
> osea ya se tiene claro el análisis?

**Agente**, 2026-10-01 18:03:10
<!-- agente: 534b5900-9683-4fe9-85da-99a2612de9f2 -->

Sí. Revisé el análisis 2 contra su hallazgo y queda cubierto:

| El H-2 dice | Lo resuelve |
|---|---|
| El guion solo servía para un análisis | Una herramienta general que lee el análisis prendido del archivo de estado (conclusión 8, punto 2) |
| Hubo que apagarlo a mano | Los tres controles por palabra (conclusión 2, punto 3) |
| Entró un turno en un análisis cerrado | Apagar con «Apruebo el análisis» pone la marca y corta (conclusión 2) |
| Cada proyecto tendría que configurarlo | Lo registra el instalador (conclusión 8, punto 8) |

Al aprobarlo pasan dos cosas, por lo que ya se acordó:
1. **El pendiente 103 pasa a la V3** en sus originales: en `pendientes/` y en la carpeta del análisis (conclusión 52 del análisis 1).
2. **El apagado se hace a mano por última vez**, borrando el archivo de estado. Las palabras todavía no prenden ni apagan nada, porque eso lo construye la HU 1.

Si está de acuerdo, la palabra es «Apruebo el análisis».

### 164 · Usuario, 2026-10-01 18:06:35
> lo que no quedó claro es se usa en los proyectos

### 165 · Usuario, 2026-10-01 18:07:16
> lo que no quedó claro es como se usa en los proyectos e inclusive en este de ejemplos

**Agente**, 2026-10-01 18:07:36
<!-- agente: 4b21b534-267c-4249-b536-c6b8b2aad031 -->

Con un ejemplo en otro proyecto, `rni-back`, que tiene abierto el pendiente 12: «el reporte de pagos no cuadra».

| El usuario escribe | Qué hace la herramienta | Aviso que se ve |
|---|---|---|
| «Analicemos: el pendiente 12» | El pendiente pasa a ser carpeta (`pendiente.md`), se crea `analisis-1.md` desde la plantilla con la copia del hallazgo y del pendiente, y se anota en el archivo de estado | «Entra al análisis 1 del pendiente 12» |
| Se discute el reporte | Cada turno entra solo | El mismo aviso |
| «Pare. Pregunta: ¿cuándo fue el último commit?» | Ese turno no entra. Queda la línea «turno X en pausa» | «Análisis en pausa» |
| «Analicemos: el pendiente 12» | Se reanuda | «Entra al análisis 1 del pendiente 12» |
| «Apruebo el análisis» | Pone la marca con el último turno y borra el archivo de estado | «Ningún análisis prendido» |
| Días después, al ejecutar el plan, aparece un hallazgo: «Analicemos: el pendiente 12» | Crea `analisis-2.md` con el hallazgo nuevo | «Entra al análisis 2 del pendiente 12» |

**En este proyecto** sería igual. Cuando, al construir la HU 1, aparezca un hallazgo, «Analicemos: el pendiente 103» abre el `analisis-3.md`.

El ejemplo deja ver dos cosas que hay que corregir:
1. **La conclusión 1 solo funcionó por casualidad.** Hoy el análisis 2 arrancó justo después de la aprobación porque fue en la misma sesión. Si el hallazgo aparece días después, los turnos de por medio son de otro trabajo. Lo correcto es que **el análisis arranque en el turno donde se dice «Analicemos: el pendiente N»**.
2. **«Analicemos» también se usa para analizar cualquier cosa en el chat**, como hicimos con la tabla de enlaces. Solo debe prender un análisis si el mensaje nombra un pendiente.

¿Se corrigen las conclusiones 1 y 2 así?

### 166 · Usuario, 2026-10-01 18:11:08
> si

**Agente**, 2026-10-01 18:11:39
<!-- agente: 79bff274-7b98-40bc-8367-f14bd8bdd01a -->

Corregido en el [analisis-2.md](analisis-2.md):

- **Conclusión 1:** el análisis arranca en el turno donde se dice «Analicemos: el pendiente N». Hoy coincidió con el turno siguiente a la aprobación solo porque todo pasó en la misma sesión.
- **Conclusión 2:** «Analicemos» prende un análisis solo si nombra un pendiente. Sin pendiente, sigue siendo analizar en el chat.
- **Punto 3 de lo que se tiene que hacer:** se ajustó igual.
- **Lección 4, de lo que funcionó:** recorrer un ejemplo en otro proyecto destapó dos fallas que en este caso no se veían.

Pasó el validador de redacción sin marcas. ¿Queda claro cómo se usa, o se recorre otro caso?

### 167 · Usuario, 2026-10-01 18:13:07
> qué falta?

**Agente**, 2026-10-01 18:13:13
<!-- agente: 35cc9c0f-026f-433c-82dd-4bfb2b0d84a1 -->

Del análisis 2, solo falta su aprobación: «Apruebo el análisis».

Después de eso, en orden:

1. **Apagar el guion** borrando el archivo de estado. Es la última vez que se hace a mano.
2. **Pasar el pendiente 103 a la V3** en sus originales: en `pendientes/` y en la carpeta del análisis.
3. **Guardar en git** lo de hoy desde el último commit: el análisis 2, la propuesta final y el guion nuevo.
4. **Crear el análisis principal de Cimiento** en `analisis/`, con base en todo el proyecto.
5. **Escribir EP-023 y sus siete HU**, con los puntos de los dos análisis.
6. **Arrancar la HU 1** con su plan y sus pruebas.

Los pasos 4 y 5 son trabajo grande. Conviene hacerlos en una sesión nueva.

### 168 · Usuario, 2026-10-01 18:16:59
> debe ser al contrario primero se pasa y luego se apaga porque entonces no queda esa trazabilidad en el análisis

**Agente**, 2026-10-01 18:17:26
<!-- agente: be9bd868-95f2-45e9-953e-2be8dd9c6942 -->

Tiene razón: si se apaga primero, el paso de la V3 a los originales queda por fuera del análisis. Quedó como la conclusión 11, y ajusté el punto 3 de lo que se tiene que hacer:

1. **Aprobar** con «Apruebo el análisis».
2. **Pasar los cambios a los originales.** El pendiente 103 pasa a la V3, con el guion todavía prendido, para que ese paso entre en la conversación del análisis.
3. **Apagar.**

La herramienta general hará lo mismo: con «Apruebo el análisis» pone la marca, pero no apaga hasta que los cambios estén en los originales.

### 169 · Usuario, 2026-10-01 18:20:32
> si se aprueba no se pueden hacer más cambios y debe quedar la trazabilidad de que se pasó el pendiente a nueva versión el original

**Agente**, 2026-10-01 18:20:43
<!-- agente: e87cad3f-0ddf-478b-a320-b1cfc3368efb -->

Entonces el paso a la V3 no puede quedar después de la aprobación, ni tampoco antes (la conclusión 52 del análisis 1 dice que los originales no se tocan hasta aprobar). La salida es que ocurra **en el mismo acto de aprobar**:

1. El usuario escribe «Apruebo el análisis».
2. En ese mismo turno, la herramienta:
   - pasa el pendiente a la versión siguiente en sus originales;
   - escribe la marca de cierre en el análisis, que ya incluye la trazabilidad: «**Aprobado** el 2026-10-01, turno N. El pendiente pasó a la V3: [enlace al original]»;
   - y apaga.

Así la marca de aprobación es lo último que se escribe en el análisis, y dice qué cambió y dónde. Después de ella no se toca nada. El paso a la V3 queda registrado sin abrir otra vez el análisis.

¿Así queda? Si es así, corrijo la conclusión 11.

### 170 · Usuario, 2026-10-01 18:25:54
> La conclusión 52 está mal, porque todo lo que haga parte del análisis debe quedar registrado. El cambio de versión del hallazgo y del pendiente también hace parte del análisis, precisamente porque ese cambio surgió como resultado de lo que se determinó durante el análisis. Nada de lo que es del análisis debe quedar por fuera

**Agente**, 2026-10-01 18:26:22
<!-- agente: f0672e4e-fe7c-4c3f-9705-fce1eaef8a75 -->

Entendido. En el análisis 2 quedó así:

- **Conclusión 12:** el cambio de versión del hallazgo y del pendiente es parte del análisis y queda en su conversación. Corrige la conclusión 52 y la lección 13 del análisis 1, que estaban mal. El análisis 1 no se toca, porque ya está aprobado; la corrección vive aquí.
- **Conclusión 11:** el orden de cierre queda así:
  1. Pasar el hallazgo y el pendiente a su versión siguiente en los originales, con la conversación prendida.
  2. Aprobar.
  3. Apagar.
- **El punto 3** de lo que se tiene que hacer y **la nota del borrador** de la plantilla dicen lo mismo.

Según ese orden, lo siguiente es pasar el pendiente 103 a la V3 en sus originales: `pendientes/103` y el `pendiente.md` de la carpeta. ¿Lo hago?

### 171 · Usuario, 2026-10-01 18:29:43
> al aprobarse este análisis cuál es el camino a seguir

**Agente**, 2026-10-01 18:29:55
<!-- agente: acca1428-0e5b-4749-8dfc-cb9dee4aa31b -->

Este es el camino según lo que concluyeron los dos análisis:

**Antes de aprobar**
1. Pasar el pendiente 103 a la V3 en sus originales, con la conversación prendida (conclusión 11).

**Al aprobar**
2. Escribir «Apruebo el análisis», poner la marca y apagar borrando el archivo de estado.
3. Guardar en git, con su pregunta aparte.

**Después, siguiendo la cadena de `02·F0`**
4. **Análisis principal de Cimiento** en `analisis/`. Se hace con base en todo el proyecto y lo alimentan los análisis 1 y 2 (conclusión 49). Va primero porque es el que decide las épicas.
5. **EP-023 y sus siete HU.** Los criterios de cada HU salen de «Lo que se tiene que hacer» de los dos análisis, cada uno con su «Sale de».
6. **HU 1:** especificación, plan con rutas exactas, aprobación del plan, construcción, pruebas y cierre. El cierre registra cuántos hallazgos salieron.
7. **Las demás HU**, en este orden: 5, 2, 3, 4, 7 y 6.

**Si al ejecutar aparece un hallazgo**, se detiene el plan y se escribe «Analicemos: el pendiente 103». Eso abre el análisis 3, y lo primero que decide es si el hallazgo es parte del plan en curso o es otra cosa (conclusión 7).

Los pasos 4 y 5 conviene hacerlos en una sesión nueva. ¿Arranco con el paso 1?

### 172 · Usuario, 2026-10-01 19:01:02
> pase el pendiente

**Agente**, 2026-10-01 19:01:57
<!-- agente: 625e361c-470e-4f35-9158-f138382c509c -->

El pendiente 103 quedó en la V3, en sus dos lugares: [pendientes/103](../../../../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior.md) y el [pendiente.md](pendiente.md) de la carpeta del análisis.

- **De dónde sale:** ahora incluye el H-2 junto al H-13.
- **El problema:** suma la frase sobre configurar a mano lo que pasa la conversación al análisis.
- **Encabezado:** dice que es la versión 3 y enlaza al análisis 2.

Como la conversación sigue prendida, este paso queda registrado en el análisis 2. Corregí las dos marcas que señaló el revisor; los enlaces funcionan.

Lo siguiente es la aprobación, con «Apruebo el análisis».

### 173 · Usuario, 2026-10-01 19:02:26
> Apruebo el análisis

**Agente**, 2026-10-01 19:03:10
<!-- agente: ac3568b6-624f-424f-a0a3-50cb6d73f934 -->

El análisis 2 quedó aprobado. La marca en su cabecera dice:

> **Aprobado** por el usuario el 2026-10-01, en el turno 173. Antes de aprobarlo, el pendiente pasó a la V3 en sus originales: pendientes/103 y pendiente.md. Desde ese momento este análisis no se reescribe.

El apagado ya no es manual. Le agregué al guion una regla: cuando el análisis tiene la marca «Aprobado» y la respuesta a ese turno ya entró, borra el archivo de estado. Así, al terminar esta respuesta, el guion la pasa al análisis y se apaga solo. El próximo mensaje ya no entra.

Para el siguiente paso, guardar en git, hace falta la palabra «Suba».

> acá termina la conversación

---

## Lo acordado

> Se agregó en el piloto, por el [análisis 9](analisis-9.md), a partir de las conclusiones de este análisis, que después se quitaron para no repetirlas; cada punto conserva el número de su conclusión. No decide nada nuevo.

1. Dónde arranca un análisis: En el turno donde se dice «Analicemos: el pendiente N». En este análisis coincidió con el turno siguiente a la aprobación del anterior porque fue en la misma sesión; si el hallazgo aparece días después, los turnos de por medio son de otro trabajo y no entran (Turnos 146, 165, 166).
2. Tres controles, nada más: Prender, para arrancar el análisis: «Analicemos» solo prende si el mensaje nombra un pendiente («Analicemos: el pendiente N»); sin pendiente, «Analicemos» sigue siendo analizar en el chat. Pausar, para que lo que no es parte del análisis no entre en él («Pare»); se reanuda prendiendo otra vez. Apagar, cuando se aprueba («Apruebo el análisis»), que pone la marca con el último turno. Entre prender y pausar o apagar, cada turno entra solo, sin que nadie lo pida (Turnos 147, 148, 165, 166).
3. Cómo se controla: Un aviso en cada turno dice a qué análisis está entrando la conversación, o que ninguno está prendido. Un archivo de estado visible guarda qué análisis está prendido y se puede corregir a mano si algo falla (Turno 147).
4. Los turnos en pausa: No entran en el análisis. En su lugar queda una línea que dice «turnos X a Y en pausa», para que se note el corte (Turno 149).
5. El formato de la conversación copiada: Al pasar la conversación al análisis, la raya larga que separa cada turno de su hora se cambia por una coma, porque el análisis sigue `00·ID8`. Vale de aquí en adelante; el análisis 1 se deja como está (Turnos 150, 152).
6. Un solo análisis abierto: No se abre el análisis de otro pendiente mientras no se cumpla el plan de trabajo del análisis abierto; si no, quedan varios análisis o pendientes sobre lo mismo y el trabajo se duplica. Como nunca hay dos abiertos, no hay que elegir a cuál entra la conversación. El análisis siguiente del mismo pendiente no es otro análisis: mejora el pendiente con el hallazgo nuevo (Turnos 156, 157).
7. Qué hace el análisis de un hallazgo: Todo hallazgo que surge al ejecutar el plan abre un análisis nuevo, que primero valida las posibilidades y decide si el hallazgo es parte del plan en curso o es otra cosa. Si es parte del plan, tiene prioridad: el pendiente actual se mejora con lo que se determinó y se resuelve antes de seguir. Si no es parte del plan, se crea su propio pendiente, sigue su proceso y el plan en curso continúa sin tocarse. En los dos casos, el análisis deja claro qué se determinó y dónde se aplica (Turno 157).
8. Cómo llega a cada proyecto: Con el instalador, como los demás enganches. La herramienta pasa a `adaptadores/claude-code/` y el instalador la registra en cada proyecto; las palabras y el aviso llegan con ella; la plantilla se lee del estándar. El archivo de estado lo crea la herramienta al prender y lo borra al apagar; es local porque `.estado/` no va a git, y lo que manda es la marca «Aprobado» del análisis (Turnos 159, 160, 161).
9. Qué cambia en lo ya hecho: El análisis 1 no se toca y su punto 29 queda superado por los puntos de este. El hallazgo H-2 es parte del plan en curso, así que mejora el pendiente (V3) y sus puntos pasan a la HU 1 de EP-023 (Turnos 161, 162).
10. Las marcas de la herramienta: Al pasar la conversación se quitan las etiquetas que la herramienta le pone al mensaje del usuario (texto pegado, archivo abierto en el editor), porque no son palabras del usuario (Turno 158).
11. El orden al cerrar: Primero se pasan el hallazgo y el pendiente a su versión siguiente en los originales, dentro del análisis y con la conversación prendida; después se aprueba; y por último se apaga. Después de aprobado no se hace ningún cambio (Turnos 168, 169, 170).
12. Nada del análisis queda por fuera: El cambio de versión del hallazgo y del pendiente es parte del análisis, porque sale de lo que se determinó en él, y queda registrado en su conversación. Corrige la conclusión 52 y la lección 13 del análisis 1, que decían que los originales se cambiaban después de aprobar (Turno 170).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `01·C28` (la palabra clave de cada mensaje, que ya trae «Analicemos», «Pare» y «Apruebo»), `13·DOC22` (lo que deja la sesión se escribe en el momento) y `20·M10` (versionar). Choca: «Apruebo» se usa también para planes y commits; se resuelve con «Apruebo el análisis» (conclusión 2).

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| Transcripción | `validadores/historico.py` la escribe en cada turno, separando el turno de su hora con raya larga. Funciona en cualquier proyecto. |
| Palabra clave | `validadores/recuperar.py` ya lee con qué palabra abre cada mensaje. |
| Enganches | Viven en `adaptadores/claude-code/` y el instalador los registra en cada proyecto. |
| Estado | `historico-chat/.estado/` existe y está fuera de git. |
| Guiones de esta sesión | `crear_analisis_103.py` servía solo para el análisis 1. `pasar_conversacion.py` ya lee el análisis del archivo de estado, pero no tiene palabras, aviso ni pausa. |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Lección 11 del análisis 1 | Lo escrito por un camino que el revisor no mira queda sin control. Pasó igual con las rayas y las etiquetas copiadas de la transcripción (conclusiones 5 y 10). |
| S-082 | Un aviso que no detiene no cambia nada. El aviso de cada turno sirve para ver a dónde va la conversación, no para frenar. |
| El turno 142 | Entró en el análisis 1 ya aprobado porque el enganche se apagaba a mano. Lo resuelve la conclusión 2. |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | Lo reciben con el instalador (conclusión 8), sin configurar nada a mano. |
| Claude Code | Cambiar `.claude/settings.json` pide autorización; el instalador debe registrar el enganche, no el agente en cada sesión. |
| Normas y leyes | Ninguna aplica. |

### Dónde más puede pasar

> Se agregó en el piloto, por el [análisis 9](analisis-9.md), a partir de las conclusiones de este análisis; no decide nada nuevo.

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Turnos que no son del análisis | Cualquier sesión | Entra al análisis lo que no se decidió ahí | Conclusión 4 |
| Dos análisis abiertos | Cualquier proyecto | Quedan dos análisis sobre lo mismo | Conclusión 6 |
| Etiquetas que la herramienta pone al mensaje | Cualquier herramienta | Se copian palabras que el usuario no dijo | Conclusión 10 |
| Otro proyecto que hereda | Cualquier proyecto | La conversación hay que pasarla a mano | Conclusión 8 |

---

## Propuesta final: pendiente V3 y HU

> El hallazgo H-2 no cambia: es nuevo y queda como está en el resumen del 2026-09-30. Cambia el pendiente.

### Pendiente V3. Lo que se construye se aparta de lo aprobado

Reúne los pendientes 103, 104 y 105.

| Campo | Valor |
|---|---|
| De dónde sale | El H-13 de la sesión del 2026-09-28, que reúne H-10, H-11 y H-13, y el H-2 de la sesión del 2026-09-30 |
| El problema | No hay un documento que fije el alcance antes de la HU. Nada obliga a que cada documento salga del anterior. Nada detiene al agente cuando trabaja fuera del plan aprobado. La plantilla del plan no permite comprobarlo con un programa. Y lo que pasa la conversación al análisis hay que configurarlo a mano para cada análisis. |
| Por qué importa | Al ejecutar el plan aparecen hallazgos que se podían evitar, y cada uno se vuelve un pendiente más. |

### HU

Los puntos de lo que se tiene que hacer pasan a la HU 1 de EP-023 (el análisis existe, tiene su forma y revisa las cuatro partes), menos el 7, que pasa a la HU 4 (un hallazgo detiene la ejecución y vuelve al análisis).

> Orden puesto al día en el piloto, por el [análisis 9](analisis-9.md), con el que fijó el [análisis 8](analisis-8.md), conclusión 8. El número identifica a la HU; el orden sale de sus dependencias.

| Orden | HU | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|
| 1 | HU-001 · El análisis existe, tiene su forma y revisa las cuatro partes | Ninguna | Las demás se apoyan en el análisis | Todos menos el 7 |
| 2 | HU-004 · Un hallazgo detiene la ejecución y vuelve al análisis | HU-003 | Detener la ejecución necesita la forma del hallazgo | 7 |

## Lecciones aprendidas

| # | Lección | Tipo | Señal |
|---|---|---|---|
| 1 | La herramienta del análisis 1 se hizo para un solo análisis y hubo que apagarla a mano. Lo que se construya en el estándar sirve para cualquier análisis de cualquier proyecto. | Falló | Por escribir |
| 2 | Lo copiado de la transcripción trajo rayas y etiquetas que el análisis no admite. Lo que se copia a un documento pasa por las reglas del documento. | Falló | Por escribir |
| 3 | El ciclo diseñado en el análisis 1 funcionó en su primer uso: el hallazgo abrió el análisis 2 sin tocar el análisis aprobado. | Funcionó | Por escribir |
| 4 | Recorrer un ejemplo en otro proyecto mostró dos fallas que en este caso no se veían: el arranque dependía de que todo pasara en la misma sesión, y «Analicemos» se usa también sin pendiente. | Funcionó | Por escribir |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Que la herramienta que pasa la conversación al análisis cambie la raya larga de los encabezados de turno por una coma. | 5 | EP-023, HU 1 |
| 2 | Volver una herramienta del estándar, en `adaptadores/claude-code/`, el guion que pasa la conversación al análisis, que lea el análisis prendido de `historico-chat/.estado/analisis-en-curso.txt`. | 8 | EP-023, HU 1 |
| 3 | Prender con «Analicemos» más el pendiente; pausar con «Pare», dejando la línea de turnos en pausa; apagar con «Apruebo el análisis», poniendo la marca; antes de aprobar, el hallazgo y el pendiente ya pasaron a su versión siguiente dentro del análisis. El análisis arranca en el turno donde se prende; «Analicemos» sin pendiente no prende nada. | 1, 2, 4, 11, 12 | EP-023, HU 1 |
| 4 | Un aviso en cada turno que diga a qué análisis entra la conversación, o que ninguno está prendido. | 3 | EP-023, HU 1 |
| 5 | Quitar de la conversación copiada las etiquetas que la herramienta le pone al mensaje del usuario. | 10 | EP-023, HU 1 |
| 6 | Que la herramienta no prenda el análisis de otro pendiente mientras el plan del análisis abierto no se cumpla. | 6 | EP-023, HU 1 |
| 7 | Que el análisis de un hallazgo decida primero si es parte del plan en curso: si lo es, mejora el pendiente y se resuelve antes de seguir; si no, se crea su pendiente y el plan continúa. | 7 | EP-023, HU 4 |
| 8 | Que el instalador registre la herramienta en cada proyecto. | 8 | EP-023, HU 1 |

## Lo que aporta al análisis principal

> Se agregó en el piloto, por el [análisis 9](analisis-9.md), a partir de las conclusiones de este análisis; no decide nada nuevo.

**Resultado:** Cambia lo que se construye.

**Lo que suma al análisis principal:** La conversación del análisis pasa sola a su archivo, y el análisis se prende, se pausa y se aprueba con tres palabras, con uno solo abierto a la vez.
