# -*- coding: utf-8 -*-
"""Fase A de la HU-003, T-02: el hallazgo de la plantilla del resumen queda con «Qué pasó», «Por qué
importa» y el enlace a su pendiente (análisis 1, conclusiones 14, 34 y 35). Su estado y por dónde se
retoma los calcula el programa siguiendo los enlaces. Se conserva la caja de reglas de redacción."""
import os
import re

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
RUTA = os.path.join(RAIZ, "plantillas", "sesion.md")

RESTO = """> Plantilla del resumen de una sesión. No se escribe al final: un chat no tiene final, y lo que se deja para el cierre no se escribe nunca. Se llena en el momento en que aparece el hallazgo, con qué pasó, por qué importa y el enlace a su pendiente. Al llenarla se reemplazan los `«…»` y se borran esta caja y las notas de cada sección.
>
> La conversación entera ya queda en la transcripción de la sesión (`historico-chat/`), que sigue su curso y no se toca. Esto es lo otro: lo que la sesión **dejó** y hay que poder encontrar sin releerla. Se guarda en `historico-chat/resumenes/AAAA-MM-DD/«tema».md`: una carpeta por día y un archivo por sesión, con su línea en el índice de ese día.

## Lo que lleva cada hallazgo

> Define las filas de cada hallazgo y qué se escribe en cada una.

| Fila | Qué se escribe |
|---|---|
| **Qué pasó** | El hecho, en una frase. Sin interpretación. |
| **Por qué importa** | Qué se pierde o qué cuesta si nadie lo sabe. |
| **Pendiente** | El enlace al pendiente que abrió. Mientras no lo tenga, el hallazgo no está anotado. |

Nada más va acá. La solución, las decisiones, el orden y la historia que dispara son del análisis de su pendiente. El estado tampoco se escribe: el programa lo calcula siguiendo los enlaces. Sin pendiente, el hallazgo está **sin anotar**; con pendiente, está **anotado**; cuando se cumple el plan que salió del pendiente, está **resuelto**. Y se retoma por el último análisis de su pendiente, que es donde quedó la conversación.

Un hallazgo se nombra `AAAA-MM-DD · tema · H-N`. El número dice en qué orden apareció. No se cambia, porque otros documentos lo citan. Cada resumen numera los suyos desde `H-1`, así que el número solo no identifica nada: «el H-4» existe en todas las sesiones que tuvieron cuatro hallazgos.

El hallazgo que se hereda no se copia. La sesión que retoma un hallazgo de otra lo **nombra** en su «viene de» y sigue en el análisis de su pendiente. Copiarlo al resumen nuevo deja dos versiones del mismo hallazgo.

Toda regla que se nombre va enlazada ([`20·M15`](«RUTA-ESTANDAR»/base/20-meta-reglas/reglas/M15-toda-cita-a-otra-regla-lleva-su-enlace.md)): quien lea el resumen meses después tiene que llegar a la regla en un clic.

## Dónde termina cada cosa

> Dice a qué archivo va cada hallazgo según lo que es.

| Si es... | Va a... |
|---|---|
| Algo que se **aprendió** y no se recupera del código | `documentacion/senales.md` ([`13·DOC5`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)) |
| Algo que **falta hacer** | Un pendiente, en la carpeta `pendientes/` de lo que lo origina; si todavía no tiene dueño, en `pendientes/` de la carpeta de este día |
| Algo que **hay que exigir siempre** | Una regla de `base/`, por el procedimiento del [capítulo `20`](«RUTA-ESTANDAR»/base/20-meta-reglas/base.md) |
| Cómo quiere trabajar **el usuario** | `historico-chat/memory/` ([`01·C19`](«RUTA-ESTANDAR»/base/01-conducta.md#c19--escribe-la-memoria-del-agente-dentro-del-repositorio-del-proyecto)) |

Un hallazgo que no cabe en ninguno de los cuatro no era un hallazgo: era conversación, y ya quedó en la transcripción.

## De dónde viene esta sesión

> Nombra los hallazgos de otras sesiones que esta retoma, todos si son varios, o dice que es trabajo nuevo.

| Campo | Valor |
|---|---|
| Viene de | «AAAA-MM-DD · tema · H-N» / «—, es trabajo nuevo» |

Ese hallazgo no se copia acá. Se nombra, y lo que se decida queda en el análisis de su pendiente. Este resumen anota los hallazgos **nuevos**, los que aparecieron en esta sesión.

## Hallazgos de esta sesión

> Lleva un bloque `### H-N` por cada hallazgo que apareció en esta sesión.

### H-1 · «título corto»

| Campo | Valor |
|---|---|
| Qué pasó | «…» |
| Por qué importa | «…» |
| Pendiente | «enlace a la carpeta del pendiente» |

## ¿Se puede cerrar la sesión?

Se cierra cuando ningún hallazgo queda sin anotar: cada uno enlaza su pendiente, y su pendiente existe. Anotar es dejar el archivo, no decir «quedó pendiente».

| Para cerrar | Estado |
|---|---|
| Todo hallazgo enlaza su pendiente | ☐ |
| Todo pendiente enlazado existe | ☐ |
| Lo que se hizo está aprobado y guardado | ☐ |

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

_(Si la sesión no dejó nada, se escribe «nada»: es un dato, no un olvido.)_
"""


def main():
    with open(RUTA, encoding="utf-8") as f:
        texto = f.read()
    m = re.search(r"^> Todo documento creado con esta plantilla.*?\n\n", texto, re.M | re.S)
    titulo = texto[:m.start()]
    with open(RUTA, "w", encoding="utf-8", newline="\n") as f:
        f.write(titulo + m.group(0) + RESTO)


if __name__ == "__main__":
    main()
