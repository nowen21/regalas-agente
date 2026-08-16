# Resúmenes

Lo que **dejó** cada sesión: los hallazgos, con su estado y con la pregunta que quedó viva. Se escribe con la plantilla [`plantillas/sesion.md`](../../plantillas/sesion.md).

Es parte del histórico y por eso vive dentro, pero no se mezcla con la transcripción. [`historico-chat/`](../README.md) guarda **lo que se dijo**, literal, y lo escribe el enganche. Esto guarda **lo que quedó**, y lo escribe el agente a medida que aparece cada hallazgo.

## Cuál de los dos abrir

Son dos documentos por sesión y responden preguntas distintas. Abrir el que no es cuesta media hora de lectura.

| Lo que se busca | Dónde está |
|---|---|
| Qué quedó abierto y por dónde se sigue | El resumen |
| Qué se decidió y por qué | El resumen |
| Qué hay que hacer para poder cerrar | El resumen |
| Qué dijo exactamente el usuario, con sus palabras | La transcripción |
| En qué orden pasaron las cosas | La transcripción |
| Qué se probó y qué dio | El resumen apunta; el detalle está en la fase |

La regla práctica: **se arranca siempre por el resumen.** La transcripción se abre cuando el resumen no alcanza, y si eso pasa seguido, lo que falla es el resumen.

## Cómo se organiza

```
resumenes/
  AAAA-MM-DD/          ← una carpeta por día
    <tema>.md          ← un resumen por sesión de ese día
    README.md          ← qué sesiones hubo ese día y qué dejó cada una
```

Una carpeta por fecha y un archivo por sesión: si un día se abrieron veinte sesiones, ahí están los veinte resúmenes. La sesión que cruza la medianoche deja su resumen en el día en que pasaron las cosas.

Se anotan todos los hallazgos, resueltos y abiertos. Los resueltos, para que nadie los vuelva a discutir; los abiertos, para arrancar la próxima discusión sin empezar de cero.

## Días

- [2026-08-14/](2026-08-14/) — cuatro sesiones: las HU de la comprobación automática, el cierre de su hallazgo H-4, por qué ese cierre no funcionó, y el glosario de la terminología.
- [2026-08-15/](2026-08-15/) — dos sesiones: la plantilla del resultado de pruebas, y el inventario de los resúmenes que faltan.
