# Pendiente: los programas se encienden y se apagan desde Cimiento

| | |
|---|---|
| **De dónde sale** | [Sesión del 2026-10-09 (3)](../../../../2026-10-09-sesion-3.md), que parte de la idea de un chat con Claude dentro de Cimiento planteada en la [sesión del 2026-10-09 (2)](../../../../2026-10-09-sesion-2.md) |

## El problema

El usuario quiere manejar todo desde la pantalla de Cimiento. Cimiento es lo único que se arranca desde la consola o como servicio. Cualquier otro programa que necesite un comando para correr tiene en esa pantalla un botón de **Encender** y otro de **Apagar**, y Cimiento ejecuta por debajo lo que haga falta. Así nadie tiene que abrir una consola y escribir comandos cada vez.

Lo que hay hoy:

- Ningún proyecto de la base se puede encender ni apagar. El modelo `Proyecto` (`proyectos/cimiento/core/proyectos/models.py`) no guarda ningún comando.
- El vigilante del consumo arranca solo al iniciar sesión en Windows, como lo dejó `instalar.py` en EP-025·HU-011. Con este pendiente, ese arranque pasa a Cimiento.
- Cimiento ya reconoce los programas que hay dentro de un proyecto, uno por carpeta (EP-029·HU-007). Ese reconocimiento se reutiliza.

Lo que el análisis tiene que resolver:

1. **Qué se enciende.** No es uno por proyecto sino uno por programa: un proyecto puede tener una parte de servidor y otra de pantallas. A eso se suman el vigilante del consumo y el chat con Claude.
2. **De dónde sale el comando.** Cimiento lo propone según la tecnología: con `manage.py` usa `runserver`, con `package.json` usa `npm run dev` y con `docker-compose.yml` usa `docker compose up`. El usuario lo confirma o lo corrige en la pantalla, y queda guardado en la base. La pantalla no acepta un comando escrito suelto.
3. **El estado.** La pantalla muestra si el programa está encendido, apagado o se cayó, en qué puerto corre y lo que va escribiendo mientras corre. Antes de encender, Cimiento revisa que el puerto no esté ocupado.
4. **El apagado.** En Windows hay que apagar el programa junto con los que él mismo arrancó (`taskkill /T` sobre su número de proceso exacto, `04·S10`). Si no, quedan procesos colgados.
5. **Cuando Cimiento se reinicia.** Al volver, debe reconocer los programas que siguen corriendo, y para eso guarda el número de cada proceso en la base. Falta que el usuario decida si apagar Cimiento apaga también lo que encendió.

## El chat con Claude, como un caso de este pendiente

La idea que lo originó es poder cerrar VS Code, que ocupa unos 2,2 GB de memoria. Para eso, Cimiento tendría su propio chat con Claude. Lo que se averiguó:

- El Agent SDK, la biblioteca oficial para manejar a Claude desde un programa, no funciona con la suscripción de claude.ai: exige una clave de la API, que se cobra aparte por cada token. Lo dice su documentación: «Anthropic does not allow third party developers to offer claude.ai login [...] including agents built on the Claude Agent SDK» ([overview](https://code.claude.com/docs/en/agent-sdk/overview.md)).
- Hay tres opciones, y falta que el usuario elija una:
  1. **Una consola dentro de una página de Cimiento**: Cimiento arranca el `claude` de siempre y lo muestra con xterm.js, que dibuja la consola en el navegador, y pywinpty, que la conecta con el programa en Windows. Usa la suscripción y mantiene los permisos, los enganches y `/resume`. Es lo más barato de construir. La contra: se ve como una consola.
  2. **Un chat propio sobre `claude -p`**: también usa la suscripción, pero los permisos exigen que Cimiento atienda la herramienta de aprobación (`--permission-prompt-tool`), y la documentación no dice con claridad si está permitido manejar el `claude` desde otro programa con la suscripción.
  3. **El Agent SDK con clave de la API**: es el chat más completo, pero cada mensaje se paga aparte de la suscripción.

En las tres, la vista de los archivos que cambian sale de la pantalla de revisión de EP-030·HU-002.

## Por qué importa

Hoy, para tener corriendo un proyecto hay que abrir una consola y escribir su comando, y nada muestra qué está encendido. Tampoco hay forma de apagarlo sin buscar el proceso a mano. Centralizar el encendido en Cimiento deja un solo punto de control, y permite cerrar programas pesados como VS Code cuando no se necesitan.
