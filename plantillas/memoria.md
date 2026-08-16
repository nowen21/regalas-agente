# Memoria del agente

Lo que el agente debe recordar entre sesiones se escribe **aquí**, dentro del repositorio: preferencias del usuario, acuerdos sobre cómo trabajar, correcciones que valen para mañana.

**No en el almacenamiento local de la herramienta.** Claude Code guarda su memoria en `~/.claude/projects/<ruta-del-proyecto>/memory/`; esa carpeta queda **vacía**. Lo que aparezca ahí se mueve acá, y no se deja copia ni puntero: dos versiones del mismo recuerdo terminan diciendo cosas distintas, y la que manda es la que nadie puede leer.

**Por qué acá:** lo local no se ve en `git`, no se puede revisar en un cambio, no se versiona y no viaja a otra máquina. Al clonar el proyecto en otro equipo, esa memoria se queda atrás y nadie se entera.

Lo mueve el programa, no el agente: un enganche recoge la carpeta local al abrir la sesión y cada vez que se escribe un archivo. No hay que acordarse. **Solo mueve: no borra nada, nunca.** Si el nombre ya está ocupado, el que llega entra como `<nombre>-local.md` y decide el usuario cuál manda.

**La otra forma de cumplir: enlazar.** Si la carpeta de la herramienta es un *junction* (o un enlace simbólico) a esta, la herramienta ya escribe dentro del repositorio y no hay nada que mover — el estándar lo detecta y no toca la carpeta. Un aviso para ese montaje: en Windows `MEMORY.md` y `memory.md` son el mismo archivo, así que la herramienta puede sobrescribir este índice con el suyo.

## Cómo es cada recuerdo

**Un archivo por recuerdo**, `<nombre-corto>.md` en kebab-case, con las mismas tres partes:

- **Qué se pide** — la instrucción, en una o dos líneas.
- **Por qué** — de dónde salió. Sin el motivo, el recuerdo se reinterpreta hasta que deja de cumplirse.
- **Cómo se aplica** — qué hace el agente distinto por saberlo.

Un recuerdo que se contradice con otro se corrige; no se agrega al lado. Al crear uno, se agrega su línea al índice de abajo.

> Esto **no** es la memoria por señales del proyecto (regla [`13·DOC5`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md) del capítulo 13, la que registra decisiones y aprendizajes del sistema). Aquella guarda lo que el proyecto aprendió; esta, cómo quiere el usuario que se trabaje.

> Tampoco es norma del estándar: la norma es la regla [`01·C19`](«RUTA-ESTANDAR»/base/01-conducta.md#c19--escribe-la-memoria-del-agente-dentro-del-repositorio-del-proyecto) del capítulo 01, que obliga a guardar la memoria acá. Lo que va dentro de cada archivo es preferencia del usuario de este proyecto.

> Si en este proyecto la memoria **no** debe versionarse, agregar `historico-chat/memory/` al `.gitignore`. Se sigue escribiendo acá; solo que no viaja al repositorio.

## Índice

| Recuerdo | De qué se trata |
|---|---|
| (una línea por recuerdo; se agrega al crearlo) | |
