# 2026-08-22 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-22-sesion-2.md](../../2026-08-22-sesion-2.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

**Viene de:** —, es trabajo nuevo.

---

## Hallazgos de esta sesión

### H-1 · El encuadre del planteamiento de Cimiento se llenó con procedencia en vez de con instrucción de uso

- **Qué pasó:** [`prompts/cimiento-planteamiento.md`](../../../prompts/cimiento-planteamiento.md) ocupa el renglón «Encuadre» del molde con fecha de redacción, fuentes, una cita del usuario y el número del pendiente que cierra, en lugar de lo que el molde pone ahí ([`plantillas/ciclo-vida-proyectos/01-planteamiento.md`](../../../plantillas/ciclo-vida-proyectos/01-planteamiento.md)): la ruta del flujo y el «no generar código hasta que el plan esté aprobado».
- **Por qué importa:** el encuadre es lo primero que lee un agente en frío y es lo único que le dice que ese documento es **insumo y no orden**. Sustituido por procedencia, el archivo queda sin la barrera que evita que alguien lo lea como encargo y arranque a codificar. Además, tres de sus cuatro datos ya están repetidos en §0 y §2.
- **Qué lo soluciona:**
  **Reescribir el encuadre con dos párrafos:** el del molde (qué es el documento y qué no autoriza) y uno propio de este archivo (se escribió con el proyecto ya andando, así que su uso es medir contra él lo que se le proponga a Cimiento). La procedencia baja a un renglón «Cómo se levantó» en la tabla de §0; «cierra el pendiente 56» se va al `CHANGELOG.md` y al estado de la fase.
- **Qué se decidió:** el encuadre comunica **cómo se usa el documento**, no de dónde salió. Y el usuario amplió el criterio: el planteamiento **se redacta como si el proyecto fuera a empezar ahora**, tomando lo construido solo como materia prima. Nada de «se escribió hacia atrás», «hoy 14 de 14» ni identificadores de señales y pendientes ya cerrados: eso es descripción de lo hecho, no planteamiento de lo que se necesita.
- **Estado:** resuelto acá
- **Responde a:** — (salió de revisar el entregable del pendiente 56, no de un criterio planeado)
- **Dispara:** —
- **Orden de resolución:** 1 de 2 · es el archivo concreto; H-2 generaliza lo que acá se ve.
- **Dónde queda:** [`prompts/cimiento-planteamiento.md`](../../../prompts/cimiento-planteamiento.md). No se parchó: el usuario pidió borrarlo y escribirlo de nuevo desde las fuentes (README, `prompts/`, notas, inventario), para que la reconstrucción no arrastrara la voz descriptiva del texto anterior.
- **Nace en:** 2026-08-22 · encuadre del planteamiento
- **Cerrado en:** 2026-08-22 · encuadre del planteamiento
- **Con qué se retoma:** —

### H-2 · Nada impide que un planteamiento llenado pise el encuadre del molde

- **Qué pasó:** el molde marca su recuadro de instrucciones con «borrar este recuadro», pero el renglón «Encuadre para el agente» queda fuera de ese recuadro y sin decir que **no se sustituye**. H-1 es la consecuencia: un planteamiento real lo reemplazó por otra cosa y ningún validador lo notó.
- **Por qué importa:** si el encuadre se puede pisar, cualquier planteamiento heredado puede llegar al agente sin la frase que frena el código antes del plan aprobado. Es el mismo riesgo en todos los proyectos instalados, no solo acá.
- **Qué lo soluciona:**
  **EP-004 · HU nueva — «el planteamiento conserva su encuadre»**
  - **Como** quien mantiene el estándar
  - **Quiero** que el molde declare el encuadre como texto fijo y que la comprobación automática avise cuando un `*-planteamiento.md` no lo tenga
  - **Para** que ningún planteamiento llegue al agente sin la instrucción que le impide leerlo como orden de entregar código
  - **Contexto:** hoy el molde deja el encuadre fuera del recuadro que sí manda borrar, sin decir si se conserva o se reemplaza; `validar.py` no lo mira. Si no se hace, el caso de H-1 se repite en cada proyecto que herede el molde y el freno de `02·F2`/`02·F4` desaparece del punto donde más se necesita.
- **Qué se decidió:** el usuario aprobó atacarlo. Se parte en dos: que el molde declare el encuadre como texto fijo entra en la fase C de HU-002; que un programa lo compruebe queda como pendiente 77, en EP-004 · HU-004.
- **Estado:** abierto, anotado
- **Responde a:** —
- **Dispara:** 1. [Pendiente 77](../../../pendientes/77-el-planteamiento-conserva-su-encuadre.md), EP-004 · HU-004.
- **Orden de resolución:** 2 de 2 · conviene fijar primero la redacción buena en H-1 y recién después exigirla a todos.
- **Dónde queda:** [pendiente 77](../../../pendientes/77-el-planteamiento-conserva-su-encuadre.md), y la mitad del molde en la [fase C de HU-002](../../../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-002-modelos-del-encargo/C-EP-003-HU-002-el-planteamiento-se-reconstruye-igual/plan_trabajo.md), tarea T-05.
- **Nace en:** 2026-08-22 · encuadre del planteamiento
- **Cerrado en:** —
- **Con qué se retoma:** el pendiente 77 propone comprobar las dos frases que importan en vez del texto literal, para que corregir el molde no reviente el validador. Falta que el usuario lo confirme al construirlo.

### H-3 · Los moldes del ciclo llevan las marcas que el estándar prohíbe, y se las pasan a todo documento que nace de ellos

- **Qué pasó:** el planteamiento reescrito salió con 33 marcas mecánicas de [`00·ID8`](../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md); el usuario lo notó antes que el agente, que no había corrido [`validadores/marcas.py`](../../../validadores/marcas.py). Al limpiarlo quedaron 2, y las 2 vienen copiadas del molde: el título y el nombre de la sección 1. Contados aparte, los moldes de `plantillas/` suman **461 marcas en 31 archivos**, y los del ciclo de vida **197 en 10**.
- **Por qué importa:** el estándar exige `00·ID8` a todo documento que el agente entrega, y sus propios moldes son la fuente. Todo planteamiento, especificación o plan que un proyecto escriba nace incumpliendo, y el que lo llena no tiene forma de saber si la marca es suya o heredada. El trinquete del commit reparte así: en `base/` y `plantillas/` falla ante cualquier marca, y en el resto solo avisa. El planteamiento vive en `prompts/`, o sea en «el resto», y por eso pasó sin que nada lo detuviera. Y sobre el molde tampoco sirve, porque no exige limpiar lo que ya está: exige no agregar.
- **Qué lo soluciona:**
  **EP-003 · HU nueva — «los moldes se entregan limpios de marcas»**
  - **Como** quien llena un molde en cualquier proyecto
  - **Quiero** que el molde no traiga marcas de generación automática
  - **Para** que el documento que escribo no nazca incumpliendo una regla que yo no escribí
  - **Contexto:** hoy `plantillas/` acumula 461 marcas mecánicas y cada copia las propaga al proyecto que la usa. Limpiar la prosa de un molde es reescribirla, así que no lo puede hacer el reemplazo automático: va molde por molde. Si no se hace, la regla queda escrita y sistemáticamente incumplida desde su propia fuente, que es la peor forma de tener una regla.
- **Qué se decidió:** el usuario aprobó anotarlo. No es hallazgo nuevo: es el pedazo chico de la decisión que el [pendiente 11](../../../pendientes/hecho/limpiar-marcadores-de-ia-del-texto-del-estandar.md) dejó abierta al cerrar, acotada a los 10 moldes del ciclo. El planteamiento de Cimiento quedó limpio salvo las 2 heredadas del molde.
- **Estado:** abierto, anotado
- **Responde a:** —
- **Dispara:** 1. [Pendiente 78](../../../pendientes/78-los-moldes-se-entregan-limpios-de-marcas.md), EP-004 · HU-012, la misma historia del pendiente 11.
- **Orden de resolución:** 3 de 3 · es el trabajo más largo de los tres y no bloquea a los otros dos.
- **Dónde queda:** [pendiente 78](../../../pendientes/78-los-moldes-se-entregan-limpios-de-marcas.md).
- **Nace en:** 2026-08-22 · encuadre del planteamiento
- **Cerrado en:** —
- **Con qué se retoma:** antes de limpiar hay una decisión del usuario que el pendiente 11 ya había dejado escrita: si la voz de esta casa sí lleva la raya larga, lo que se cambia es el anexo de marcadores, no los moldes.

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ (H-1) |
| Todo hallazgo abierto tiene su pendiente creado | ☑ (77 y 78) |
| Toda historia disparada está escrita en su épica | ☑ (CA-04 en HU-002; 77 y 78 entran en HU existentes) |
| Lo que se hizo está aprobado y guardado | ☐ sin commitear, y la fase C espera la puerta 7 |

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

---

_(Si la sesión no dejó nada, se escribe "nada": es un dato, no un olvido.)_

<!-- aviso: falta decir si la sesión se puede cerrar -->
