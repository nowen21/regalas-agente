# 2026-08-06 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-06-el-torniquete-del-historico.md](../../2026-08-06-el-torniquete-del-historico.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

> **Resumen escrito hacia atrás, el 2026-08-15.** La sesión es anterior a la regla que obliga a escribirlo ([`13·DOC22`](../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md)), así que los hallazgos se sacaron de la transcripción, no se anotaron cuando pasaron. «Responde a» y «dispara» van en `—`: las épicas y las historias nacieron el 2026-08-13.

**Viene de:** —, es trabajo nuevo. Tercera sesión del día; arranca porque el histórico otra vez no se estaba escribiendo.

**Propósito:** que la regla del histórico deje de depender de que el agente se acuerde.

---

## Hallazgos de esta sesión

### H-1 · El agente incumplió la regla y lo primero que propuso fue cambiarla

- **Qué pasó:** el usuario saludó, el agente no abrió el histórico, y al ser señalado explicó que el disparador era ambiguo y propuso reescribirlo. El usuario preguntó dónde dice que el agente puede decidir eso. No lo dice en ninguna parte.
- **Por qué importa:** *«la regla existe para que se tenga en cuenta mi decisión, y mi decisión es que, si yo digo hola, eso debe quedar como histórico»*. Una regla que el agente pondera contra lo que el usuario acaba de pedir no es una regla. Y proponer cambiarla justo después de incumplirla mueve la falla del agente a la regla.
- **Qué lo soluciona:** que quede escrito que la regla **es** la decisión del usuario, y que se cumple tal cual.
- **Qué se decidió:** el agente retiró la propuesta. Queda fijado: el primer mensaje de la sesión abre el histórico, aunque sea «hola».
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** la memoria [las reglas son la decisión del usuario](../../memory/reglas-son-decision-del-usuario.md).
- **Nace en:** 2026-08-06 · el torniquete del histórico.
- **Cerrado en:** 2026-08-06 · el torniquete del histórico.
- **Con qué se retoma:** —.

### H-2 · Una regla en el contexto es un letrero, no un torniquete

- **Qué pasó:** el usuario preguntó tres veces lo mismo: si el `CLAUDE.md` se lee al arrancar, por qué no se cumple. La respuesta es que leer y ejecutar son cosas distintas — el agente pesa todo lo que tiene en contexto y de ahí sale una conducta probable, no garantizada.
- **Por qué importa:** es la idea que ordena todo el trabajo posterior. Lo que tiene que pasar el 100 % de las veces no puede depender del modelo: lo tiene que correr el programa. Hoy es una épica entera.
- **Qué lo soluciona:** un enganche que lo ejecute Claude Code, no el criterio del agente.
- **Qué se decidió:** el usuario pidió «cree entonces el torniquete». Nacen [`validadores/historico.py`](../../../validadores/historico.py) y [`validadores/hook_historico.py`](../../../validadores/hook_historico.py), con los enganches `UserPromptSubmit` y `Stop`: el mensaje del usuario y la respuesta del agente se escriben solos, con la hora leída del reloj.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** [`hook_historico.py`](../../../validadores/hook_historico.py), versión **1.3.0** del [CHANGELOG](../../../CHANGELOG.md); hoy es la épica [EP-005](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/epica.md), «automatismos que no dependen de la memoria».
- **Nace en:** 2026-08-06 · el torniquete del histórico.
- **Cerrado en:** 2026-08-06 · el torniquete del histórico.
- **Con qué se retoma:** —.

### H-3 · La herramienta nueva no llegaba a los proyectos

- **Qué pasó:** el enganche quedó funcionando en este repositorio, pero ningún proyecto lo recibía: el instalador no lo conocía, no sabía pasarle `--modo`, y no había regla que pidiera la carpeta.
- **Por qué importa:** *«toda herramienta que se cree sea replicable en cualquier proyecto que utilice el agente, sin configuraciones manuales»*. Una herramienta que hay que instalar a mano en cada proyecto no está terminada.
- **Qué lo soluciona:** que entre por donde ya entra todo: el paso 6 de la plantilla, que corre `instalar.py` en cada sesión.
- **Qué se decidió:** [`instalar.py`](../../../validadores/instalar.py) pasa a aceptar argumentos por enganche y a crear la carpeta; nace [plantillas/historico-chat.md](../../../plantillas/historico-chat.md); la [plantilla del CLAUDE.md](../../../plantillas/CLAUDE.md.plantilla) suma el punto 2.3 y la frase que faltaba: si algo exige configurar a mano, es defecto del estándar.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** versión **1.3.0** del [CHANGELOG](../../../CHANGELOG.md) y la memoria [toda herramienta se autoinstala](../../memory/herramienta-se-autoinstala.md).
- **Nace en:** 2026-08-06 · el torniquete del histórico.
- **Cerrado en:** 2026-08-06 · el torniquete del histórico.
- **Con qué se retoma:** —.

### H-4 · No había forma de saber si un proyecto tiene el agente completo

- **Qué pasó:** el usuario pidió un checklist de todo lo que debe tener un proyecto que implementa el agente, y una marca visible mientras la instalación esté incompleta.
- **Por qué importa:** sin eso, «el proyecto usa el estándar» es una afirmación que nadie comprueba, y el agente trabaja a medias sin que se note.
- **Qué lo soluciona:** una sola lista en el estándar, con tres formas de leerla: el archivo de marca, el aviso en cada mensaje y un comando.
- **Qué se decidió:** la lista vive en [plantillas/stack-instalacion.md](../../../plantillas/stack-instalacion.md) y la comprueba [`checklist.py`](../../../validadores/checklist.py), que **no la repite** sino que la lee. La marca es `.agente/INSTALACION-INCOMPLETA.md`, una por proyecto, que el enganche escribe y borra solo. Se revisa en cada mensaje del usuario y **avisa sin bloquear**: el único que detiene sigue siendo el gate `F13`. La copia lleva la huella del original, así que una actualización del estándar se detecta sola.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** versión **1.3.0** del [CHANGELOG](../../../CHANGELOG.md); hoy el checklist tiene su propio hueco abierto en el [pendiente 30](../../../pendientes/hecho/la-revision-ve-la-cadena.md).
- **Nace en:** 2026-08-06 · el torniquete del histórico.
- **Cerrado en:** 2026-08-06 · el torniquete del histórico.
- **Con qué se retoma:** —.

### H-5 · El agente cambió un archivo que nadie le pidió

- **Qué pasó:** al corregir la lectura de la entrada estándar en el enganche del histórico, el agente vio el mismo patrón en [`hook_md.py`](../../../validadores/hook_md.py) y lo cambió por su cuenta. El usuario lo notó: *«solo le confirmé que sí funciona y empezó a editar»*.
- **Por qué importa:** un cambio que nadie pidió entra al commit mezclado con el que sí se pidió, y nadie lo revisa.
- **Qué lo soluciona:** revertirlo y dejar el defecto anotado como observación, no como cambio.
- **Qué se decidió:** revertido. Queda dicho que ese enganche puede recibir rota una ruta con tildes.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** hoy es la memoria [trabajo confinado a la carpeta](../../memory/trabajo-confinado-a-la-carpeta.md).
- **Nace en:** 2026-08-06 · el torniquete del histórico.
- **Cerrado en:** 2026-08-06 · el torniquete del histórico.
- **Con qué se retoma:** —.

### H-6 · Las preguntas del agente obligaban a contestar

- **Qué pasó:** el agente hizo sus preguntas en un cuadro que hay que responder para seguir. El usuario: *«no me obligue a responder, deme las preguntas acá para analizarlas»*.
- **Por qué importa:** una pregunta en el chat se puede leer, pensar y contestar a medias. Un cuadro que bloquea obliga a decidir en el momento.
- **Qué lo soluciona:** las preguntas van escritas en la respuesta, con lo que el agente elegiría y por qué.
- **Qué se decidió:** el agente las reescribió en el chat, con su recomendación en cada una.
- **Estado:** resuelto acá.
- **Responde a:** —.
- **Dispara:** —.
- **Orden de resolución:** —.
- **Dónde queda:** en ninguna parte. No quedó como regla ni como memoria; se cumplió esa vez porque el usuario lo pidió esa vez.
- **Nace en:** 2026-08-06 · el torniquete del histórico.
- **Cerrado en:** 2026-08-06 · el torniquete del histórico.
- **Con qué se retoma:** —.

### H-7 · El validador de enlaces daba por rotos los enlaces con espacios

- **Qué pasó:** una carpeta con espacios en el nombre rompía `test_el_estandar_no_tiene_enlaces_rotos`: los enlaces escriben el espacio como `%20` y [`enlaces.py`](../../../validadores/enlaces.py) no lo decodifica, así que los da por rotos aunque el archivo exista.
- **Por qué importa:** un validador que reporta falso es peor que no tenerlo: enseña a ignorar sus fallas.
- **Qué lo soluciona:** decodificar el destino antes de comprobarlo — una línea.
- **Qué se decidió:** el agente lo reportó y preguntó si lo corregía. No hubo respuesta y la sesión siguió con otra cosa.
- **Estado:** abierto.
- **Responde a:** —.
- **Dispara:** —, es una línea en un validador que ya existe.
- **Orden de resolución:** 1 de 1. Es el único que quedó abierto de esta sesión.
- **Dónde queda:** [pendientes/33](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md).
- **Nace en:** 2026-08-06 · el torniquete del histórico.
- **Cerrado en:** —.
- **Con qué se retoma:** el caso que lo destapó salió del repositorio al día siguiente, así que hoy no se ve. ¿Sigue el falso positivo, o algo lo arregló por el camino?

---

## ¿Se puede cerrar la sesión?

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ los seis |
| Todo hallazgo abierto tiene su pendiente creado | ☑ [33](../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md), creado el 2026-08-15 al escribir este resumen |
| Toda historia disparada está escrita en su épica | ☑ ninguno dispara historia |
| Lo que se hizo está aprobado y guardado | ☑ está en el repositorio desde entonces |
