# Pendiente: la pantalla «Gasto» no dice por dónde empezar, y el gasto no llega en vivo ni queda dentro del proyecto

| | |
|---|---|
| **De dónde sale** | [H-1 · La pantalla «Gasto» no dice por dónde empezar, y el gasto no llega en vivo ni queda dentro del proyecto](../../sesion-2.md), en el resumen de la sesión del 2026-10-05, versión 2 según el [análisis 1](analisis-1.md). La versión 1 decía solo «La pantalla «Gasto» muestra todo con el mismo peso» |

## El problema

La pantalla «Gasto» de Cimiento ([tablero.html](../../../../../proyectos/cimiento/core/consumo/templates/consumo/tablero.html) y [_datos.html](../../../../../proyectos/cimiento/core/consumo/templates/consumo/_datos.html)) pone 20 bloques seguidos y todos pesan lo mismo: 2 gráficas, 4 cifras, 13 tablas y una franja de contexto.

- Las cifras quedan debajo de las gráficas, y «Candidatos a automatizar», que es lo que dice dónde ahorrar, queda de último.
- No hay total de tokens del período ni comparación con el período anterior.
- La gráfica «Por proyecto» y la tabla «Proyectos» muestran lo mismo.
- Las tablas solo traen números, sin porcentaje ni barra que deje comparar.
- Los seis bloques en `col-lg-4` (palabra, trabajo, modelo, agente, tipo de token, herramienta) dejan filas con alturas distintas.
- «Estimado» se repite en cada encabezado.

Lo «en vivo» acordado en el pendiente 119 se construyó con relojes que nadie acordó: la pantalla pregunta cada 10 segundos y redibuja todas las tablas, y el [vigilante](../../../../../proyectos/cimiento/core/consumo/vigilante.py) guarda cada 2 y relee los proyectos cada 60.

El gasto se lee de `~/.claude/projects/`, fuera del proyecto, y la base guarda solo conteos: el contenido se pierde cuando Claude Code borra el `.jsonl` a los 30 días.

El [histórico](../../../../../proyectos/cimiento/core/enganches/historico.py) anota como «Usuario» los avisos internos de Claude Code (`<task-notification>` y `<agent-message>`).

## Por qué importa

Quien abre la pantalla no ve en qué se gasta más ni qué se puede ahorrar sin recorrer las 13 tablas, y para eso existe: para decidir qué pasar a un programa. Con relojes, lo en vivo llega tarde y se aparta de lo acordado. Lo que vive en el almacén de Claude Code incumple `01·C29` y desaparece a los 30 días. Y la trazabilidad pone en boca del usuario lo que no escribió.
