# Memoria del agente — cómo se trabaja en este repo

Lo que el agente debe recordar entre sesiones se escribe **aquí**, en el repo. El almacén de memoria de la herramienta (`~/.claude/projects/<proyecto>/memory/`) queda **vacío** — ni el texto ni un puntero: dos versiones del mismo recuerdo terminan diciendo cosas distintas, y la que manda es la que nadie puede leer.

**Por qué acá:** lo local no se ve en git, no se puede revisar, no se versiona y no viaja a otra máquina. Esto sí.

**Un archivo por recuerdo.** Cada uno lleva la misma forma: **qué se pide**, **por qué** y **cómo se aplica**.

Lo mueve el programa, no el agente: `validadores/hook_recuerdos.py` recoge el almacén local al abrir la sesión y cada vez que se escribe un archivo.

Lo que obliga a guardarlo acá es norma del estándar (`01·C19`); lo que dice cada recuerdo es preferencia del usuario sobre cómo trabajar, y eso no va en `base/` (`20·M13`).

---

## Cuál va dónde

Hay **tres** sitios y se parecen lo suficiente como para equivocarse. La pregunta que los separa es **qué haría que eso cambiara**:

| Si cambiaría porque… | Es | Va en |
|---|---|---|
| …el **usuario** cambia de opinión sobre cómo quiere trabajar | **Preferencia** | Un recuerdo, acá |
| …el **código o el proyecto** cambian | **Aprendizaje** | Una señal, en `memoria/senales.db` |
| …cambia lo que se le exige a **cualquier** proyecto | **Regla** | `base/`, con su versión (`20·M10`) |

Dicho corto: *«no me pongas `Co-Authored-By`»* es preferencia — nadie más tiene por qué compartirla. *«`git add -A` arrastró un archivo local y se publicó»* es aprendizaje — pasó, y seguirá siendo cierto aunque el usuario opine distinto. *«Toda cita lleva su enlace»* es regla — se le exige a cualquiera.

**El caso de borde: la preferencia que resulta valer para todos.** Cuando una preferencia deja de ser gusto y pasa a ser algo exigible a cualquier proyecto, **sube a `base/` como regla** y el recuerdo **no se borra**: se queda con el registro de que el usuario lo pidió, cuándo, y cuántas veces tuvo que repetirlo. Eso no cabe en una regla y es lo que evita volver a discutirlo. Así está hecho [Respuestas cortas](respuestas-cortas.md), que es hoy la regla `00·ID9`.

**Nada se guarda en dos sitios.** Si algo ya está en uno, el otro lo **enlaza**; nunca lo copia. Dos copias envejecen distinto y la que manda termina siendo la que nadie mira — que es la misma razón por la que el almacén de la herramienta queda vacío.

> **Ya pasó.** La terminología del proyecto está en el recuerdo [Terminología](terminologia-agente-vs-estandar.md) **y** en la señal `S-002`, y hoy dicen cosas distintas: el recuerdo dice que se llama **Cimiento** desde el 2026-08-14, y la señal sigue diciendo *«'el agente' = Claude Code»*. Detectado el 2026-08-17 en la fase [`A-EP-006-HU-005`](../../documentacion/epicas/EP-006-memoria-de-lo-aprendido/HU-005-separar-aprendizaje-de-preferencia/A-EP-006-HU-005-retrodocumentar-la-separacion-aprendizaje-preferencia/resultado_pruebas.md).

---

## Índice

| Recuerdo | De qué se trata |
|---|---|
| [Aprobar antes de commit](aprobar-antes-de-commit.md) | No hay commit ni push hasta que el usuario lea el cambio y lo apruebe; "sí" al cambio no es "sí" al commit. |
| [Corregir el defecto detectado](corregir-el-defecto-que-uno-mismo-detecta.md) | Lo que el agente reporta como mal, lo arregla; no pregunta "¿lo corrijo?". Vale solo mientras ejecuta algo ya autorizado. |
| [Decidir es del usuario](decidir-es-del-usuario.md) | Las opciones se escriben en el chat, con recomendación, y se espera. Ni las decide el agente ni van en el formulario de la herramienta. |
| [Una instrucción se cumple entera](una-instruccion-se-cumple-entera.md) | Las unidades de una misma orden se hacen todas y se reporta al final; no se pregunta «¿sigo?» con una orden ya dada. |
| [Estilo de redacción simple](estilo-redaccion-simple.md) | Todo lo que se escribe lo entiende quien no sabe del tema, e idealmente un niño — también las reglas (`00·ID7`). |
| [Fixtures sin secretos literales](fixtures-sin-secretos-literales.md) | En tests y ejemplos, los tokens se arman en runtime: GitHub bloquea el push si ve un secreto con forma real. |
| [Histórico de sesiones](historico-chat.md) | Cada sesión se transcribe literal en `historico-chat/`, con marca de tiempo del reloj del sistema. |
| [Las reglas son la decisión del usuario](reglas-son-decision-del-usuario.md) | Una regla escrita se cumple tal cual; no se pondera, no se reinterpreta, no se propone cambiarla al incumplirla. |
| [Manuales claros](manuales-claros.md) | Tercera persona, sin etiquetar al lector por rol, paso a paso literal, el camino más simple. |
| [No tocar el trabajo de otras sesiones](no-tocar-trabajo-de-otras-sesiones.md) | Se commitea solo lo que hizo esta sesión; commitear lo ajeno mezcla el versionado. |
| [Pendientes en el repo](pendiente-patrones-devops.md) | El backlog del estándar vive en `pendientes/`, versionado; la memoria es solo el puntero. |
| [Respuestas cortas](respuestas-cortas.md) | Conclusión primero y pocas líneas; los detalles van en los archivos, no en el chat. |
| [Terminología: agente vs estándar vs Claude](terminologia-agente-vs-estandar.md) | El agente es lo que se instala; el estándar son `base/` + `plantillas/`; Claude es la IA que lo opera. Claude no es el agente. |
| [Toda herramienta se autoinstala](herramienta-se-autoinstala.md) | Llega sola a cada proyecto vía `instalar.py`; exigir configuración manual es defecto del estándar. |
| [Todo multiproyecto](todo-multiproyecto.md) | Lo que se construya sirve a cualquier proyecto: universal de raíz, o universal por detección de stack. |
| [Trabajo confinado a la carpeta](trabajo-confinado-a-la-carpeta.md) | Mientras se trabaja un tema, todo va dentro de su carpeta; replicar al resto lo indica el usuario. |
| [Pregunta, afirmación o indicación](pregunta-no-es-instruccion.md) | Pregunta: solo se responde. Observación: se explica y se espera. Indicación: se ejecuta. En la duda, no se toca. |
| [Convención de commits](sin-coauthored-by.md) | El cuerpo arranca con la idea del usuario y sigue con lo que hizo el agente; nunca `Co-Authored-By`. |

<!-- huella: 83db0387a355 · estandar 25.2.0 -->