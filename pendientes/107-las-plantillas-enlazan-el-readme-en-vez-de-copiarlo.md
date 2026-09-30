# Pendiente · Las plantillas enlazan el README en vez de copiarlo

**Estado:** abierto. Espera la aprobación del usuario.

| | |
|---|---|
| **Historia de usuario** | Por asignar: nace al aprobarse este pendiente |
| **De dónde sale** | [H-3 de la sesión del 2026-09-28](../historico-chat/resumenes/2026-09-28/sesion.md), sobre por qué el agente olvida las reglas |
| **Proyecto de origen** | El estándar mismo |

## El problema

La tabla de reglas de redacción, con `ID8`, `ID9`, `ID11` e `ID12`, está copiada en las 55 plantillas, y cada cambio obliga a tocarlas todas: la 38.3.1 agregó `ID12` en las 55. El formato de las plantillas ya está escrito en [plantillas/README.md](../plantillas/README.md), sección «Cómo está hecho un modelo», y `CLAUDE.md.plantilla` manda leerlo antes de crear, cambiar o llenar una plantilla. Además:

- [plantillas/ciclo-vida-proyectos/04-HU.md](../plantillas/ciclo-vida-proyectos/04-HU.md) dice «Elimine las secciones que no apliquen», y [`13·DOC21`](../base/13-documentacion/reglas/DOC21-escribe-n-a-en-la-seccion-que-no-aplica.md) pide escribirlas `N/A`.
- [plantillas/ADR.md](../plantillas/ADR.md) cierra su caja con «Reemplaza los `«…»` y borra esta caja», que tutea.

## Por qué importa

El usuario fijó el rumbo: *«la idea no es saturar las plantillas sabiendo que hay un documento maestro que le dice cómo hacer las cosas»*. Lo copiado en 55 sitios envejece distinto en cada uno.

## Qué falta

1. Reemplazar la caja de reglas de cada plantilla por un enlace a la sección del README.
2. Corregir la frase de `04-HU.md` para que diga `N/A`, como pide `13·DOC21`.
3. Corregir la caja de `ADR.md`.

Falta decidir si el cambio es PARCHE o MAYOR para los proyectos que ya usan las plantillas.

## El límite

- No cambia qué exigen las reglas de redacción.
- No cambia los documentos ya escritos con las plantillas.

## Cómo se sabrá que cerró

- Ninguna plantilla tiene copiada la tabla de reglas de redacción; todas enlazan el README.
- `04-HU.md` y `ADR.md` quedan corregidas.
- `python validadores/validar.py estandar` termina sin incumplimientos.
