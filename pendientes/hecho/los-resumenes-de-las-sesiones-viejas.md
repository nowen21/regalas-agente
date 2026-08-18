# Pendiente · 33 de las 39 sesiones no tienen resumen

**Estado:** **hecho** el 2026-08-16 · anotado 2026-08-15 · nace de la sesión [historico-chat/2026-08-15-los-resumenes-que-faltan.md](../../historico-chat/2026-08-15-los-resumenes-que-faltan.md).

## El problema

[`historico-chat/`](../../historico-chat/README.md) tiene 39 transcripciones y [`resumenes/`](../../historico-chat/resumenes/README.md) tiene 6 resúmenes escritos, todos del 2026-08-13 en adelante. [`validadores/hook_resumen.py`](../../validadores/hook_resumen.py) crea el archivo de la sesión que está corriendo, y hace bien en no ocuparse de las viejas: un programa no reconoce un hallazgo. Pero eso deja 33 sesiones cuyo contenido solo se recupera releyendo 700 KB de diálogo.

El resumen es por donde se arranca a retomar un tema — así lo dice el propio [`resumenes/README.md`](../../historico-chat/resumenes/README.md). Sin él, lo que se decidió el 2026-08-06 está escrito pero no está disponible.

## Qué falta

**1. Nombrar las sesiones.** 22 de las que faltan se llaman `AAAA-MM-DD-sesion-N.md` y su línea del índice dice «sesión del 2026-08-07». El resumen vive en `resumenes/AAAA-MM-DD/«tema».md`: sin tema no hay nombre que ponerle. Se renombra con la herramienta que ya existe, que mueve archivo, título, línea del índice y resumen a la vez:

```sh
python validadores/historico.py --renombrar "<archivo>" --tema "<tema>" --resumen "<de qué se trató>"
```

**2. Decidir cómo se llenan cuatro campos hacia atrás.** Los doce campos de [`plantillas/sesion.md`](../../plantillas/sesion.md) suponen que el hallazgo se escribe cuando aparece:

- **Responde a** y **dispara** — las épicas y las historias nacieron el 2026-08-13. Ninguna sesión anterior puede citar una épica que todavía no existía. O se dejan en `—`, o se mapea cada hallazgo a la épica que hoy le correspondería.
- **Estado** y **cerrado en** — hay que buscarlos en sesiones posteriores y en el [`CHANGELOG`](../../CHANGELOG.md), no en la sesión que se está resumiendo.

**3. Escribir los 33.** No todos cuestan lo mismo. El corte es por cuántos mensajes tuvo la sesión:

| Grupo | Cuántas | Qué se escribe |
|---|---|---|
| Uno o dos mensajes | 9 | Casi todas, «nada»: dos son un «hola» y un «fd». |
| De tres a diez | 8 | Uno o dos hallazgos. |
| De once a veintiséis | 13 | El grueso del trabajo. |
| Más de treinta | 3 | [2026-08-06-la-anatomia-de-la-regla](../../historico-chat/2026-08-06-la-anatomia-de-la-regla.md) (61), [2026-08-07-el-checklist-de-la-regla](../../historico-chat/2026-08-07-el-checklist-de-la-regla-y-la-carpeta-de-identidad.md) (32) y [2026-08-13-del-brief-a-los-planes-de-la-fase-a](../../historico-chat/2026-08-13-del-brief-a-los-planes-de-la-fase-a.md) (38). |

El [`CHANGELOG.md`](../../CHANGELOG.md) tiene sus entradas fechadas y sirve de contraste: dice qué quedó del día que se está resumiendo.

## Lo que ya se hizo

**Terminado el 2026-08-16.** Las 39 transcripciones quedaron cubiertas: **33 resúmenes escritos**, uno por sesión, y los 6 días que faltaban con su carpeta e índice — [06](../../historico-chat/resumenes/2026-08-06/README.md), [07](../../historico-chat/resumenes/2026-08-07/README.md), [08](../../historico-chat/resumenes/2026-08-08/README.md), [09](../../historico-chat/resumenes/2026-08-09/README.md), [12](../../historico-chat/resumenes/2026-08-12/README.md) y [13](../../historico-chat/resumenes/2026-08-13/README.md). Se renombraron 23 sesiones y cada línea del índice del histórico apunta a su resumen.

**Cuatro transcripciones no llegaron a tener resumen propio porque eran copias a mano de otra sesión** —`2026-08-06-sesion-7`, `2026-08-06-sesion-9`, `2026-08-07-sesion-9` y `2026-08-07-analisis-cumplimiento-reglas`—. Se borraron el 2026-08-16 por decisión del usuario; siguen en el historial de git. Quedan **35 transcripciones y 35 resúmenes**, uno por sesión.

Lo que las sesiones viejas dejaron abierto quedó junto en el [pendiente 33](../33-defectos-que-destaparon-los-resumenes-viejos.md).

Renombrar rompe los enlaces que nombran la sesión desde fuera —sobre todo en [`prompts/`](../../prompts/README.md)— así que **después de cada tanda hay que correr `python validadores/validar.py estandar` y reapuntarlos**. Es el punto 4 del [pendiente 33](../33-defectos-que-destaparon-los-resumenes-viejos.md).

Los supuestos con que se escribieron, para que los que sigan salgan iguales:

- **«Responde a» y «dispara» van en `—`** en todo lo anterior al 2026-08-13. Cada resumen lo dice en una nota al principio.
- **«Estado» y «cerrado en» sí se buscan hacia adelante.** Un hallazgo que se resolvió tres días después queda «resuelto, pero en otra sesión», con la sesión que lo cerró.
- **«Dónde queda» apunta a donde vive hoy**, no a donde vivía entonces: si una decisión de agosto 6 hoy es una regla o una memoria, se enlaza esa.
- **Lo que quedó abierto y sigue abierto** va al [pendiente 33](../33-defectos-que-destaparon-los-resumenes-viejos.md).

## El límite

**La transcripción no se toca.** Guarda lo que se dijo, literal; el resumen guarda lo que quedó. Lo único que cambia de la transcripción es su nombre, y lo hace la herramienta.

**Va después del [29](../29-la-transcripcion-se-escribio-dos-veces.md):** ese revisa si hay transcripciones duplicadas, y no tiene sentido resumir dos veces una sesión que pasó una.
