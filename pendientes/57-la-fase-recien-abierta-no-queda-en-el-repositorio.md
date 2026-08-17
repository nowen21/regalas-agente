# Pendiente · La fase recién abierta no queda en el repositorio

**Estado:** abierto · anotado 2026-08-16 · **falta una decisión del usuario.**

| | |
|---|---|
| **De dónde sale** | El hallazgo H-1 del [resumen de la sesión 9](../historico-chat/resumenes/2026-08-16/sesion-9.md) |
| **Bloquea a** | El [48](48-inventario-hu.md): sus 51 filas no se pueden empezar sin esto |

## El problema

El paso 2 del inventario —en el [48](48-inventario-hu.md) y en la plantilla [`inventario-hu.md`](../plantillas/inventario-hu.md)— dice:

> Se crea la carpeta `<letra>-EP-000-HU-000-<slug>` dentro de la carpeta de la HU ([`02·F12.6`](../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) y se marca **Fase**.

Git no guarda carpetas vacías. Una fase abierta así existe en la máquina donde se creó y en ninguna otra: no aparece en `git status`, no entra en ningún commit, y un clon recién bajado no la ve. La casilla **Fase** en ☑ afirma algo que nadie más puede comprobar.

## Por qué importa

El inventario existe justamente para no recorrer las carpetas a mano. Una columna cuyo ☑ no se corresponde con nada del repositorio es peor que no tenerla: se confía en ella y miente.

Y no es solo el inventario. `02·F12.2` pide al menos una fase por HU, y el validador [`fases.py`](../validadores/fases.py) la busca leyendo el disco. Dos personas con el mismo commit obtienen resultados distintos.

## La decisión que falta

| Opción | Qué deja |
|---|---|
| **1 · Carpeta + `.gitkeep` vacío** | La carpeta entra en git. El `.gitkeep` se borra cuando entre el `plan_trabajo.md` de esa fase. Cuesta un archivo de 0 bytes por fase abierta. |
| 2 · Solo la carpeta | Lo de hoy. La marca no se puede comprobar fuera de una máquina. |
| 3 · No marcar **Fase** hasta que exista el `plan_trabajo.md` | No hace falta archivo extra, pero la columna **Fase** deja de significar algo distinto de la siguiente: sobra. |

**Recomendada la 1**, con el motivo en una línea: es la única que hace cierto lo que la casilla afirma sin borrar la diferencia entre abrir la fase y planificarla.

Lo decide el usuario. Mientras no esté decidido, las 51 filas del [48](48-inventario-hu.md) no arrancan.

## Qué hay que tocar cuando se decida

1. El paso 2 de la plantilla [`inventario-hu.md`](../plantillas/inventario-hu.md) — es `plantillas/`, así que suma entrada en el [CHANGELOG](../CHANGELOG.md) y sube [VERSION](../VERSION) (`20·M10`).
2. El paso 2 del [48](48-inventario-hu.md), que copia ese texto.
3. Mirar si `02·F12` tiene que decirlo también, o si es procedimiento del inventario y no regla.

## Cómo se sabrá que cerró

Se abre una fase en una máquina, se hace `push`, y en un clon nuevo el validador de fases la ve.
