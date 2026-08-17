# Inventario de HU — «nombre del proyecto o del conjunto»

> Plantilla. Es el tablero de **qué historias de usuario están completas y cuáles no**: una fila por HU, una casilla por documento. Reemplace los `«…»`, borre esta caja y las notas entre paréntesis.
>
> **No reemplaza a la HU ni a la fase.** Solo dice qué existe y qué falta, para no tener que recorrer las carpetas a mano cada vez que alguien pregunta cuánto falta.
>
> Vive donde el proyecto lleve su backlog — en el estándar, `pendientes/`; en un proyecto, `documentacion/`.

| Items | Lo que se debe hacer |
|---|---|
| **Qué pasa** | [`02·F12.2`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md) pide al menos una fase por HU, y cada fase deja cinco documentos. |
| **Qué se debe completar** | lo que esté en ☐ en la tabla |
| **Total de HU** | «N» |
| **Completas** | «N» |
| **Incompletas** | «N» |
| **Cierra cuando** | Incompletas = 0 ☐ |

**Los dos números se corrigen en la misma edición en que se marca la casilla.** Cuando una fila queda con todas sus ☑, **Completas** sube uno e **Incompletas** baja uno — nunca se toca una sola de las dos. Si hace falta recontar desde cero, se cuenta la tabla: fila con todas las casillas en ☑ es completa, cualquier otra es incompleta.

*Anotado el «AAAA-MM-DD», y ese día los números eran «C» y «I».*

## Qué le falta a cada HU

☐ incompleto · ☑ completo. Una casilla se marca ☑ **solo** cuando el archivo existe en la carpeta de la fase, no cuando se decidió hacerlo.

> **Una fila por HU, todas las del proyecto** — también las completas. La tabla es el inventario, no la lista de lo que falta: si solo se anota lo incompleto, nadie puede decir cuántas hay en total ni de dónde salió el número.
>
> La columna **Fase** es la carpeta; las otras cinco son los documentos que esa carpeta debe tener. Si una HU tiene más de una fase, la casilla del documento va en ☑ **solo si está en todas**.

| Épica | HU | Fase | `plan_trabajo` | `plan_pruebas` | `resultado_pruebas` | `estado-fase` | `funcionalidad_implementada` |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|
| EP-000 | [HU-000 — «título de la HU»](«ruta a la HU») | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| EP-000 | [HU-000 — «título de la HU»](«ruta a la HU») | ☑ | ☑ | ☑ | ☑ | ☑ | ☐ |
| EP-000 | [HU-000 — «título de la HU»](«ruta a la HU») | ☑ | ☑ | ☑ | ☑ | ☑ | ☑ |

## Cómo se llena la tabla

1. **Una fila a la vez**, de arriba abajo. No se abren dos en paralelo.
2. Se crea la carpeta `<letra>-EP-000-HU-000-<slug>` dentro de la carpeta de la HU ([`02·F12.6`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) y se marca **Fase**.
3. Los documentos se escriben **en el orden de las columnas**: el `resultado_pruebas` no se marca antes que el `plan_pruebas`, y ninguno antes que el `plan_trabajo`.
4. Cada archivo sale de su plantilla de `plantillas/` — la estructura no se inventa.
5. Al marcar la última casilla de una fila se corrige la **§8 de la HU**, que hasta ese momento dice que no se descompuso en fases, y su **Estado** de la §1.
6. La casilla la marca quien escribió el archivo, en la misma sesión. Una fila a medias no se deja sin que `estado-fase` diga qué la tiene detenida.

## Qué clase de trabajo es

> (Borre el que no aplique, o escriba el reparto si hay de los dos.)

- **Construcción** — la HU no se ha hecho: la fase se planifica, se prueba y se implementa.
- **Retrodocumentación** — el código ya existe y ya funciona; lo que falta es el documento que diga con qué plan se hizo, con qué casos se probó y qué salió. Se escribe contra lo que ya está en el repositorio, **sin tocar una línea de producción**.

Mezclar los dos en la misma tabla está bien, pero **no en la misma fila**: una HU construida a medias se termina de construir, no se retrodocumenta.

## Cómo se sabe que cerró

No queda ni un ☐ en la tabla, y los validadores de fases y de trazabilidad no reportan HU sin fase.
