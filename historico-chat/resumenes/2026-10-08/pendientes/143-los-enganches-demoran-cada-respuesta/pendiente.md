# Pendiente: los enganches demoran cada respuesta

| | |
|---|---|
| **De dónde sale** | Proyecto scilit: [hallazgo 1 del resumen del 2026-10-08](C:/DesarrollosClaude/personales/scilit/historico-chat/resumenes/2026-10-08/demora-de-las-respuestas.md); seguimiento en scilit: [pendiente 036](C:/DesarrollosClaude/personales/scilit/historico-chat/resumenes/2026-10-08/pendientes/036-esperando-a-cimiento-los-enganches-demoran-cada-respuesta/pendiente.md) |

## El problema

En scilit, el agente tarda en contestar aun las preguntas cortas. Los tiempos que Claude Code guarda en las transcripciones (las tres últimas sesiones, medidos el 2026-10-08) muestran de dónde sale la demora:

| Momento | Qué corre | Tiempo |
|---|---|---|
| Antes de cada respuesta | 8 enganches de `UserPromptSubmit`, en paralelo | el más lento, «Midiendo el consumo de la sesión», tarda 4,1 s de mediana y hasta 9,4 s |
| Al terminar cada respuesta | 4 enganches de `Stop` | cerca de 2 s cada uno |
| Antes de escribir un guion | el freno (`hook_antes.py`) | 30 s una vez y 293 s otra |

En esa máquina, Python tarda 0,46 s solo en arrancar vacío. Cada mensaje arranca unos 12 intérpretes, y cada uso de una herramienta entre 2 y 8.

Los 293 s salen de `guiones.parecido_a` (`proyectos/cimiento/core/enganches/guiones.py`). La función compara cada guion nuevo de `historico-chat/scripts/` contra todos los anteriores (105 en scilit), letra por letra, con `difflib.SequenceMatcher(autojunk=False)`, y ese tiempo crece con el cuadrado del tamaño. Se reproduce con `planes_adminlte.py` de scilit (9.463 caracteres) pasado con otro nombre: 257,8 s. Comparar por líneas tarda 0,14 s, pero el parecido con `planes_plantilla_completa.py` baja de 0,7 o más a 0,46. Al cambiar la comparación hay que recalibrar `PARECIDO`.

Propuesta, en orden de ganancia:
1. Cambiar la comparación de `parecido_a` y recalibrar `PARECIDO`.
2. Unir los enganches de cada momento en un solo proceso: de 12 arranques de Python por mensaje a 2.
3. Que el consumo y el checklist guarden su resultado y solo recalculen si algo cambió.
4. Pasar a segundo plano lo que la respuesta no necesita esperar: histórico, consumo y redacción.

Ningún proyecto tiene que cambiar nada y no se agrega nada opcional: es una corrección.

## Por qué importa

Cada respuesta espera entre 4 y 9 segundos antes de que el modelo empiece, y escribir un guion puede frenar la sesión casi cinco minutos. El tiempo se pierde en todos los proyectos que usan el estándar.

## Avance (sesión del 2026-10-08 de scilit, «comparar-guiones-por-lineas»)

| Paso | Qué quedó | Commit |
|---|---|---|
| 1 · Comparación de guiones | `parecido_a` compara por líneas y `PARECIDO` baja a 0,4, calibrado con los 105 guiones de scilit. El caso de 257,8 s tarda 0,23 s. | `ba17419` |
| Fase A · Segundo plano | Los 4 enganches de `Stop` se instalan con `async` (`EN_SEGUNDO_PLANO`). | `cd95db4` |
| Acuerdos | `hook_acuerdos` era el que frenaba cada mensaje: recorría la épica por cada fase en curso. De 7,64 s a 1,21 s. | `db0c6d7` |
| Juntar enganches en un proceso | Se probó y salió más lento (6,26 s contra 2,19 s en paralelo): pesa lo que hace cada uno, no arrancar Python. Se descartó. | — |
| Guardar el resultado del consumo y del checklist | Se descartó: solos tardan 0,83 s y 0,31 s. | — |

Medidos solos al enviar cada mensaje (mediana de 5): reglas 1,33 s, acuerdos 1,21 s, consumo 0,83 s, análisis 0,63 s, checklist 0,31 s.

Sigue abierto: `hook_acuerdos` da 208 fases de scilit por «en curso». Si muchas ya cerraron, `Acuerdos.en_curso` las cuenta mal.
