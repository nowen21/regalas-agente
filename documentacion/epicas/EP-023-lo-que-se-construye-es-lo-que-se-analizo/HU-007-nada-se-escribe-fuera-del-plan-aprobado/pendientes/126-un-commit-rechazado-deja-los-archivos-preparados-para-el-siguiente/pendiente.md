# Pendiente: un commit rechazado deja los archivos preparados para el siguiente

| | |
|---|---|
| **De dónde sale** | Proyecto scilit: [H-8 del resumen del 2026-10-05](C:/DesarrollosClaude/personales/scilit/historico-chat/resumenes/2026-10-05/construir-ep-007.md); seguimiento en scilit: [pendiente 023](C:/DesarrollosClaude/personales/scilit/historico-chat/resumenes/2026-10-05/pendientes/023-esperando-a-cimiento-un-commit-rechazado-deja-los-archivos-preparados/pendiente.md) |

## El problema

Cuando el `pre-commit` rechaza un commit (por ejemplo, `validar.py plan` porque un archivo no está declarado en el plan de la HU), los archivos siguen preparados con `git add`. Nada los quita. El commit siguiente los recoge sin que nadie lo note.

En scilit, el 2026-10-05, se rechazó el commit de EP-008 HU-001 porque llevaba `models.py` y la migración `0008`, que solo declara el plan de HU-002. El commit de HU-002 se hizo a continuación y se llevó todo lo preparado: EP-008 subió en un solo commit (`ab41479`), contra `09·G9`, y ya estaba publicado cuando se vio.

## Por qué importa

El control rechaza un commit y el siguiente mete justo lo que el control acababa de rechazar. Con el rechazo debería salir también lo preparado, o al menos un aviso que diga que sigue preparado y cómo quitarlo (`git reset`).
