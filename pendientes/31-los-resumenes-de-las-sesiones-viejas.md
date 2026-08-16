# Pendiente · 33 de las 39 sesiones no tienen resumen

**Estado:** abierto · anotado 2026-08-15 · nace de la sesión [historico-chat/2026-08-15-los-resumenes-que-faltan.md](../historico-chat/2026-08-15-los-resumenes-que-faltan.md).

## El problema

[`historico-chat/`](../historico-chat/README.md) tiene 39 transcripciones y [`resumenes/`](../historico-chat/resumenes/README.md) tiene 6 resúmenes escritos, todos del 2026-08-13 en adelante. [`validadores/hook_resumen.py`](../validadores/hook_resumen.py) crea el archivo de la sesión que está corriendo, y hace bien en no ocuparse de las viejas: un programa no reconoce un hallazgo. Pero eso deja 33 sesiones cuyo contenido solo se recupera releyendo 700 KB de diálogo.

El resumen es por donde se arranca a retomar un tema — así lo dice el propio [`resumenes/README.md`](../historico-chat/resumenes/README.md). Sin él, lo que se decidió el 2026-08-06 está escrito pero no está disponible.

## Qué falta

**1. Nombrar las sesiones.** 22 de las que faltan se llaman `AAAA-MM-DD-sesion-N.md` y su línea del índice dice «sesión del 2026-08-07». El resumen vive en `resumenes/AAAA-MM-DD/«tema».md`: sin tema no hay nombre que ponerle. Se renombra con la herramienta que ya existe, que mueve archivo, título, línea del índice y resumen a la vez:

```sh
python validadores/historico.py --renombrar "<archivo>" --tema "<tema>" --resumen "<de qué se trató>"
```

**2. Decidir cómo se llenan cuatro campos hacia atrás.** Los doce campos de [`plantillas/sesion.md`](../plantillas/sesion.md) suponen que el hallazgo se escribe cuando aparece:

- **Responde a** y **dispara** — las épicas y las historias nacieron el 2026-08-13. Ninguna sesión anterior puede citar una épica que todavía no existía. O se dejan en `—`, o se mapea cada hallazgo a la épica que hoy le correspondería.
- **Estado** y **cerrado en** — hay que buscarlos en sesiones posteriores y en el [`CHANGELOG`](../CHANGELOG.md), no en la sesión que se está resumiendo.

**3. Escribir los 33.** No todos cuestan lo mismo. El corte es por cuántos mensajes tuvo la sesión:

| Grupo | Cuántas | Qué se escribe |
|---|---|---|
| Uno o dos mensajes | 9 | Casi todas, «nada»: dos son un «hola» y un «fd». |
| De tres a diez | 8 | Uno o dos hallazgos. |
| De once a veintiséis | 13 | El grueso del trabajo. |
| Más de treinta | 3 | [2026-08-06-sesion-5](../historico-chat/2026-08-06-sesion-5.md) (61), [2026-08-07-sesion-3](../historico-chat/2026-08-07-sesion-3.md) (32) y [2026-08-13-del-brief-a-los-planes-de-la-fase-a](../historico-chat/2026-08-13-del-brief-a-los-planes-de-la-fase-a.md) (38). |

El [`CHANGELOG.md`](../CHANGELOG.md) tiene sus entradas fechadas y sirve de contraste: dice qué quedó del día que se está resumiendo.

## El límite

**La transcripción no se toca.** Guarda lo que se dijo, literal; el resumen guarda lo que quedó. Lo único que cambia de la transcripción es su nombre, y lo hace la herramienta.

**Va después del [29](29-la-transcripcion-se-escribio-dos-veces.md):** ese revisa si hay transcripciones duplicadas, y no tiene sentido resumir dos veces una sesión que pasó una.
