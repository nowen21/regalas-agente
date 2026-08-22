# `conteo.py` — por cuál regla se incumple más

**Qué hace.** Al terminar la corrida completa, agrupa los hallazgos por la regla a la que pertenecen, imprime el recuento y anota una línea en un registro para poder comparar dos corridas.

**Para qué sirve el número.** Una regla que produce cien hallazgos por semana casi nunca significa un equipo descuidado: significa una regla **mal escrita**, o una que hace falta automatizar. Sin el número, esa conversación es opinión contra opinión, y [`20·M19`](../../base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md) pide justamente ese dato antes de construir un validador.

## De dónde sale la regla de cada hallazgo

**Del mensaje que el validador ya escribe.** Los veinticuatro citan su regla al explicar el incumplimiento: «(20·M5 · fila 10)», «S4/N6», «02·F24». Agruparlos no exigió tocarlos uno por uno.

| Caso | Qué se toma |
|---|---|
| El hallazgo la declara | esa, sin mirar el mensaje |
| El mensaje cita `20·M5` y `M5` | **`20·M5`**: el capítulo hace único al identificador |
| El mensaje no cita ninguna | `(sin regla)`, contado aparte |

**Lo que no se sabe no se reparte.** Sumar los hallazgos sin regla a cualquier otra falsearía el número que se usa para decidir qué regla cambiar, y ese número es todo el punto.

## Qué se guarda, y qué no

| Se guarda | No se guarda |
|---|---|
| el identificador de la regla | el texto del hallazgo |
| cuántas veces | la ruta ni la línea del archivo revisado |
| la fecha y la versión del estándar | nada del contenido revisado |

**Por qué importa tanto.** En un mensaje de incumplimiento viaja el contenido revisado, y ahí puede ir una clave o un dato personal ([`00·N6`](../../base/00-nucleo-blindado.md), [`12·PR4`](../../base/12-privacidad-datos.md)). Un archivo de métricas que copie lo revisado es una fuga con nombre de estadística.

## Dónde vive

`metricas/conteo-por-regla.jsonl`, **fuera del control de versiones**: es generado, y [`09·G3`](../../base/09-git.md) deja fuera lo generado. Su contenido cambia en cada corrida, así que versionarlo llenaría el historial de ruido. El precedente es `plantillas/proyectos.md`.

Una línea por corrida. Con dos líneas ya se puede decir qué bajó y qué subió, que es lo que se imprime al final.

## Cómo se corre

```
python validadores/validar.py todo
```

No hay subcomando propio: el conteo es lo último de la corrida completa, porque contar exige haber corrido todo.

## Casos que lo protegen

[`validadores/tests/test_el_conteo_por_regla.py`](../tests/test_el_conteo_por_regla.py), once. El que decide es `CP-002`: el registro no puede contener el texto del hallazgo.
