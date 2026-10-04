# Pendiente: el freno detiene lo que el usuario ya autorizó

| | |
|---|---|
| **De dónde sale** | Proyecto scilit, sesión del 2026-10-04; seguimiento en scilit: [pendiente 15](C:/DesarrollosClaude/personales/scilit/historico-chat/resumenes/2026-10-04/pendientes/15-esperando-a-cimiento-el-freno-detiene-lo-que-el-usuario-ya-autorizo/pendiente.md) |

## El problema

El freno (`validadores/freno.py`) solo deja pasar lo que nombra el plan aprobado de la fase en curso (`02·F8`). Detiene lo que el usuario autorizó por otro medio, aunque una regla o el propio `CLAUDE.md` lo permita. En scilit, el 2026-10-04, detuvo tres casos:

1. **Editar el punto 5.1 de `CLAUDE.md`.** El usuario pidió encender el patrón `17` con «Hágalo». `CLAUDE.md` dice que esas líneas «se editan a mano cuando el proyecto necesite otra cosa» y que cambiarlas «es decisión del usuario y basta con editar la línea». El freno respondió «el plan de la fase en curso no lo declara (02·F8)».
2. **Borrar `.gitd`.** El usuario lo aprobó con «Apruebo: borrar .gitd», después de verificar que sus commits ya estaban en GitHub. El freno lo detuvo por `02·F8`.
3. **Arrancar `runserver`** en segundo plano, pedido con «Hágalo: correr los comandos». El freno lo detuvo por «corre en segundo plano y deja su salida fuera del proyecto (04·S9)».

En los tres casos, la tarea terminó en manos del usuario.

El usuario de scilit pide: el freno no debe detener lo que el agente ya tiene autorizado, sea por una regla, por `CLAUDE.md` o por la palabra del usuario en el chat (`01·C24`).

Para corregirlo, el freno podría:
- aceptar como autorización la aprobación explícita del usuario en el último mensaje («Hágalo», «Apruebo: …») cuando nombra la acción o el archivo;
- dejar pasar la edición de las líneas de `CLAUDE.md` que el propio archivo declara editables;
- distinguir un servidor de desarrollo dentro del proyecto de un proceso que escribe fuera de él.

## Por qué importa

Cada caso obliga al usuario a hacer a mano lo que ya autorizó, y repite la conversación. Ya se reportaron casos parecidos (113, 115): el problema de fondo es que el freno no reconoce ninguna autorización fuera del plan de fase.
