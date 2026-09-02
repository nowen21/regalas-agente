# Pendiente · Las conversaciones quedan escritas pero nadie puede contar qué se repite

> **Este pendiente es del producto, no del cuerpo de reglas.** Entra por acá porque es el camino que la etapa de análisis dejó escrito en su sección 11: un cambio a lo ya acordado se pide como pendiente, el agente dice a qué le pega, y el usuario aprueba.

**Estado:** **hecho** el 2026-09-02. Lo cerró la plataforma, no una sesión que viniera a cerrarlo: las dos mitades que pedía se construyeron como `F-033` y `F-034` el 2026-08-31, y nadie volvió a mirar este archivo.

| | |
|---|---|
| **Historia de usuario** | [EP-011 · HU-001](../documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-001-buscar-en-lo-conversado/HU-001-buscar-en-lo-conversado.md) y [HU-002](../documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-002-ver-que-correccion-se-repite/HU-002-ver-que-correccion-se-repite.md), las dos cerradas el 2026-08-31 |
| **De dónde sale** | Lo pidió el usuario el 2026-08-25: *"la idea es que todo ese historial también se vaya guardando en la DB, porque eso va a permitir sacar estadísticas y encontrar soluciones. Por ejemplo, algo que se repita mucho es porque el agente no lo está contemplando"* |
| **Proyecto de origen** | Cimiento, como producto |

## El problema

Las conversaciones se están guardando: [validadores/historico.py](../validadores/historico.py) escribe cada mensaje del usuario y cada respuesta del agente en `historico-chat/`, con su hora y con las claves ya tapadas.

Lo que no existe es la otra mitad: **contar**. Hoy nadie puede preguntar cuántas veces el usuario tuvo que repetir la misma corrección, ni cuál fue. Para saberlo hay que releer las transcripciones una por una, que es exactamente lo que el histórico vino a evitar.

Y esa cuenta es la que importa: **una corrección que se repite no es un descuido del usuario, es una regla que falta.** Si el usuario tuvo que decir tres veces «español colombiano», el problema no fueron las tres veces: fue que el estándar no lo exigía.

## Por qué importa

No bloquea nada, y ese es el punto: el daño es lento. Cada corrección repetida cuesta tiempo del usuario y no deja rastro que alguien pueda mirar después. Se corrige el caso y se pierde el patrón.

Ya pasó en esta misma sesión, dos veces:

- **Español colombiano** se pidió tres veces antes de quedar escrito como recuerdo del repositorio.
- **`00·ID9`** se citó cuatro veces sobre respuestas distintas del agente.

Las dos terminaron en algo escrito, pero porque el usuario insistió, no porque el sistema lo hubiera detectado.

## Qué falta

Dos cosas, y el orden importa porque la segunda no sirve sin la primera:

1. **Que las conversaciones entren a la plataforma.** El texto ya existe y ya está limpio de claves; falta indexarlo para poder buscar en él sin abrir archivo por archivo. Es barato: la fase A ya guarda e indexa texto.
2. **Que se pueda contar qué se repite.** Definir qué se mide, qué cuenta como «lo mismo dicho otra vez», y dónde se ve. Acá está el trabajo de verdad, y también la duda: agrupar frases parecidas no es contar palabras iguales.

## El límite

Este pendiente **no** cubre:

- **La auditoría.** Son cosas distintas: la auditoría registra qué se hizo, esto registra qué se conversó. La regla `RN-4` del módulo Auditoría se queda como está, y la fase D no cambia por esto.
- **Decidir sola.** El sistema muestra qué se repite; escribir la regla que lo resuelve la sigue decidiendo el usuario, por la cadena de siempre.
- **Traer conversaciones de otras herramientas.** Solo lo que el enganche del histórico escribe.

## A qué le pega

| Documento | Qué cambia |
|---|---|
| [cvds/analisis-requisitos/README.md](../cvds/analisis-requisitos/README.md) | Dos requisitos funcionales nuevos, y sus filas en la trazabilidad |
| [cvds/analisis-requisitos/inventario-funcionalidades.md](../cvds/analisis-requisitos/inventario-funcionalidades.md) | Dos fichas nuevas, la tabla de resumen y la cuenta |
| [cvds/implementacion/README.md](../cvds/implementacion/README.md) | Las dos entran a la versión 2 |
| `F-032` medir el tiempo que se gasta revisando | Le llega la fuente que le faltaba: hoy dice que recibe «cuántas correcciones se repiten» y nada las cuenta |

**Lo que no cambia:** la versión 1, sus siete fases, y la especificación del módulo Auditoría.

## Cómo se sabrá que cerró

Que alguien pueda preguntarle a la plataforma cuáles fueron las cinco correcciones más repetidas del último mes, y que la respuesta salga de las conversaciones guardadas, sin abrir un archivo a mano.

La prueba de que sirve es más dura que esa: que de esa lista salga al menos una regla nueva que nadie había visto que faltaba.
