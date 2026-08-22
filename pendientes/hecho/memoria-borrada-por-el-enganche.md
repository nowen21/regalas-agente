# Hecho · La memoria que borró el enganche, y a qué proyectos alcanzó

Origen: pendiente 39 — antes punto 6 del [33](lo-que-quedo-abierto-en-las-sesiones-viejas.md), promovido a pendiente propio el 2026-08-16 y cerrado el mismo día.

| | |
|---|---|
| **Quién lo reportó** | **`agro-system`** · `C:\wamp64\www\proyectos\personales\agro-system`. El usuario preguntó allá *«¿quién borró el contenido de `historico-chat/memory`?»* y de esa pregunta salió el defecto |
| **De quién era el defecto** | Del estándar. Lo causó `validadores/recuerdos.py`, una pieza del estándar corriendo dentro del proyecto |
| **Dónde quedó la conversación** | [2026-08-07 · la memoria del agente en el repositorio](../../historico-chat/2026-08-07-memoria-del-agente-en-el-repo.md), hallazgo H-3 de su [resumen](../../historico-chat/resumenes/2026-08-07/memoria-del-agente-en-el-repo.md) |

Cerrado el 2026-08-16.

---

## Qué era

El 2026-08-07, `recuerdos.migrar()` borró la memoria de `agro-system`: 75 archivos, dos veces —una desde el instalador y otra sola, en el arranque siguiente—.

La intención era *«si el archivo del almacén de la herramienta es idéntico al del repositorio, borro el del almacén»*. Se cae cuando el almacén es un **junction de Windows** hacia `historico-chat/memory/`: origen y gemelo son **el mismo archivo**, compararlo consigo mismo da idéntico siempre, y el `os.remove` se lleva el único ejemplar.

## Qué se hizo

**1 · El código, en la versión 3.1.1.** `migrar()` ya no borra nada, nunca: todo lo que hay en el almacén se mueve, y si el nombre está ocupado entra como `<nombre>-local.md` para que decida el usuario. Se agregaron dos guardas — `enlazada()` compara por identidad en disco con `os.path.samefile` y no por el texto de la ruta, y un cinturón que se salta mover un archivo sobre sí mismo. El almacén enlazado pasó a ser una forma **válida** de cumplir `01·C19`: si la herramienta ya escribe dentro del repositorio, no hay nada que mover.

El arreglo llegó solo a todos los proyectos, sin reinstalar nada: los enganches llaman al estándar por ruta absoluta.

**2 · La recuperación, en el proyecto que lo reportó.** `agro-system` restauró los 75 archivos del commit `713444b` y sacó la memoria del junction — quedó en su commit `6d4b130`, *«actualiza a 3.1.1 y saca la memoria del junction»*.

**3 · La revisión proyecto por proyecto**, que era lo único que seguía abierto. Se hizo el 2026-08-16 y dio que **ningún otro proyecto pudo estar afectado**:

| Qué se miró | Resultado |
|---|---|
| Las nueve carpetas `historico-chat/memory/` del registro [`plantillas/proyectos.md`](../../plantillas/proyectos.md) | Todas carpeta normal. Ninguna enlazada |
| Los 16 almacenes de `~/.claude/projects/*/memory/` | Todos carpeta normal. Ninguno enlazado |
| `git status` de la carpeta de memoria de `agro-system` | Limpio: 78 archivos, nada borrado ni sin rastrear |

Sin junction el defecto no se dispara, ni entonces ni ahora. Y el `CHANGELOG.md` de la 3.1.1 ya lo decía en una línea: *«Pasó en un proyecto real, dos veces»* — un proyecto, no varios.

## Por qué se cerró sin ejecutar lo que pedía

El pendiente pedía cuatro pasos: listar los proyectos con el enganche puesto el 2026-08-07, mirar en qué estado quedó la memoria de cada uno, recuperar lo que faltara y escribir el resultado por proyecto. Lo que hace falta para eso —saber quién estuvo enlazado— se contesta más corto y sin fechas: **ninguno lo estuvo salvo el que reportó**, y ese ya se recuperó.

Su paso 1 era además inejecutable como estaba escrito: mandaba sacar la fecha de instalación de cada proyecto del historial de git de [`plantillas/proyectos.md`](../../plantillas/proyectos.md), y ese archivo está en `.gitignore` — git no lo rastrea, así que `git log` sobre él devuelve vacío. Si alguna vez hace falta esa fecha, sale del **primer commit del `CLAUDE.md`** instalado en cada proyecto, que sí se versiona.

## Lo que deja escrito

- Un enganche que corre solo no puede tener permiso de destruir: se equivoca una vez y se lleva la memoria entera sin que nadie lo pida.
- Dos rutas distintas pueden ser el mismo sitio. Comparar el texto de la ruta no es comparar el archivo.
- Que un arreglo se propague no significa que el daño esté deshecho. Son dos preguntas y se contestan por separado — esta segunda es la que se quedó nueve días abierta.
