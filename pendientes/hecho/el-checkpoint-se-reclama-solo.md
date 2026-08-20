# Pendiente · El checkpoint de la fase depende de que el agente se acuerde

**Estado:** abierto · anotado 2026-08-20.

| | |
|---|---|
| **Historia de usuario** | [EP-005 · HU-013 — El checkpoint de la fase se reclama solo](../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-013-el-checkpoint-se-reclama-solo/HU-013-el-checkpoint-se-reclama-solo.md) — es un automatismo que deja de depender de la memoria, que es lo que cubre esa épica |
| **De dónde sale** | El H-1 del resumen [../historico-chat/resumenes/2026-08-20/core-del-agente-en-la-herramienta.md](../../historico-chat/resumenes/2026-08-20/core-del-agente-en-la-herramienta.md): la comparación contra `notas/estructura.md` §3.1 (`AgentState`) |
| **Proyecto de origen** | El estándar mismo |

## El problema

El estado de una fase vive en `estado-fase.md`, y la plantilla lo define como el checkpoint que se escribe "en cada puerta" para sobrevivir a la compactación. Lo escribe el agente cuando se acuerda. [validadores/fases.py](../../validadores/fases.py) lo compara con el resultado de pruebas **después**, al correr `validar.py fases`; nada lo reclama en el momento en que una puerta pasa sin él.

El repositorio ya escribió la lección para el histórico y para el resumen de sesión: *un `CLAUDE.md` informa; un enganche ejecuta*. El checkpoint es la única pieza de la fase que sigue del lado que informa.

## Por qué importa

El checkpoint existe para que una sesión nueva lea en qué estación va la fase sin releer la conversación. Si no se escribió cuando pasó la puerta, la sesión que retoma lee un estado viejo y lo cree: la compactación mata la decisión que el archivo venía a proteger.

## Qué falta

Un enganche que, al escribir uno de los documentos que marcan una puerta (`plan_trabajo.md`, `resultado_pruebas.md`, `funcionalidad_implementada.md`), mire si `estado-fase.md` de esa fase existe y es tan reciente como el documento escrito. Si falta o quedó atrás, avisa nombrando la fase y el documento. No escribe el checkpoint: decir en qué estación va es criterio.

## El límite

No decide si el estado escrito es **cierto**. Eso sigue siendo de `fases.py` (que compara el veredicto) y de quien lee.

## Cómo se sabrá que cerró

Escribir `resultado_pruebas.md` en una fase de prueba sin tocar su `estado-fase.md` produce el aviso con el nombre de la fase; escribir después el `estado-fase.md` y volver a escribir el resultado no lo produce. Las dos cosas con caso automatizado.
