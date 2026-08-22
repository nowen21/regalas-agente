# Pendiente · Los diez moldes del ciclo llevan marcas de prosa, y cada copia se las pasa a un proyecto

**Estado:** cerrado el 2026-08-22, en dos fases de EP-004 · HU-012: la [`B`](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-012-marcas-de-generacion-automatica/B-EP-004-HU-012-limpiar-los-diez-moldes-del-ciclo/funcionalidad_implementada.md) y la [`C`](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-012-marcas-de-generacion-automatica/C-EP-004-HU-012-el-recuento-no-cuenta-la-notacion/funcionalidad_implementada.md) (v31.12.0 y v31.15.0) · anotado ese mismo día.

| | |
|---|---|
| **Historia de usuario** | [EP-004 · HU-012 — Marcas de generación automática](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-012-marcas-de-generacion-automatica/HU-012-marcas-de-generacion-automatica.md). La misma del [pendiente 11](limpiar-marcadores-de-ia-del-texto-del-estandar.md), del que este sale |
| **De dónde sale** | Hallazgo H-3 del resumen [2026-08-22 · sesión 2](../../historico-chat/resumenes/2026-08-22/sesion-2.md) |
| **Proyecto de origen** | El estándar mismo |

## El problema

**Esto no es un descubrimiento: es la decisión que el [pendiente 11](limpiar-marcadores-de-ia-del-texto-del-estandar.md) dejó al usuario al cerrar.** Ese pendiente limpió lo mecánico, puso el trinquete para que la deuda no creciera, y escribió textualmente que las marcas de prosa siguen ahí, que no se limpian con un programa, y que si alguna vez se decide que la voz del estándar no las lleva, se hace capítulo por capítulo, con su fase y su plan. Acá se propone empezar por un pedazo concreto y chico.

El pedazo son los diez moldes de `plantillas/ciclo-vida-proyectos/`. Recuento del 2026-08-22 con `python validadores/marcas.py`:

| Carpeta | Marcas | Archivos |
|---|---|---|
| `plantillas/` completa | 461 | 31 |
| `plantillas/ciclo-vida-proyectos/` | 197 | 10 |

En el ciclo de vida: 92 rayas largas de inciso, 62 puntos medios en prosa y 43 viñetas que abren con negrita y dos puntos.

**Por qué los moldes y no otro pedazo.** Un capítulo de `base/` se lee. Un molde se **copia**, y lo copiado sale con el nombre de quien lo llenó. Se vio el 2026-08-22 al reescribir [`prompts/cimiento-planteamiento.md`](../../prompts/cimiento-planteamiento.md): el documento salió con 33 marcas, limpiándolo bajó a 2, y las 2 que quedaron venían del molde, el título y el nombre de la sección 1.

## Por qué importa

Quien llena un molde no puede distinguir lo que metió él de lo que venía adentro. Si le señalan una marca, no tiene cómo saber de quién es, y la única salida honesta es ir a leer el molde.

El trinquete no lo cubre. Reparte así: en `base/` y `plantillas/` falla ante cualquier marca; en el resto solo avisa y deja pasar. El planteamiento que destapó esto vive en `prompts/`, o sea en «el resto», y por eso pasó sin que nada lo detuviera. Y sobre el molde en sí el trinquete tampoco sirve, porque no exige limpiar lo que ya está: exige no agregar.

## Qué falta

Reescribir la prosa de los diez moldes quitando las tres marcas que exigen criterio. Va a mano y leyendo: el propio [`validadores/marcas.py`](../../validadores/marcas.py) explica por qué no está en su tabla de reemplazos, y es que quitarlas es reescribir la frase, y un programa que reescribe frases del estándar cambia lo que el estándar dice.

Dos formas de cortarlo:

1. **Los 10 del ciclo primero**, que es lo que se propone: 197 marcas, y son los que producen documentos nuevos todos los días en todos los proyectos.
2. **Los 31 de `plantillas/` de una**, que cierra el tema pero es más del doble de trabajo y toca moldes que casi nadie abre.

Conviene la primera, y los 21 restantes salen como otro pendiente cuando estos estén.

**Antes de empezar hay una decisión del usuario**, y es la misma que el pendiente 11 dejó escrita: si se concluye que la voz de esta casa **sí** lleva la raya larga y el punto medio, entonces lo que hay que cambiar es [`marcadores-de-ia.md`](../../base/00-identidad-y-rol/marcadores-de-ia.md), no los moldes. Este pendiente supone que no, porque `00·ID8` está vigente y se está aplicando a lo que se escribe hoy.

## El límite

No cubre `base/`, ni `skills/`, ni `notas/`, ni los 21 moldes restantes de `plantillas/`, ni la documentación ya escrita en los proyectos instalados.

No cubre las marcas que exigen juicio y ningún programa cuenta, como el paralelismo perfecto o la densidad pareja. Cierra sobre las tres mecánicas.

No reabre lo que el pendiente 11 cerró: el trinquete y la limpieza mecánica quedan como están.

## Cómo se sabrá que cerró

`python validadores/marcas.py --raiz plantillas/ciclo-vida-proyectos` devuelve 0, y los diez moldes siguen pidiendo lo mismo que pedían: se compara sección por sección contra la versión anterior antes de dar por buena la limpieza. Un molde que quedó más corto porque se perdió una exigencia es un fallo de esta limpieza, no un ahorro.

**El adorno ya se limpió el 2026-08-22**, de 197 a 126, en la [fase B de EP-004 · HU-012](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-012-marcas-de-generacion-automatica/B-EP-004-HU-012-limpiar-los-diez-moldes-del-ciclo/funcionalidad_implementada.md). Llegar a 0 ya no es trabajo de limpieza: las 126 que quedan son todas notación, y qué hacer con ellas es la decisión de arriba.

---

## Cómo se cerró — 2026-08-22

**En dos mitades, y la segunda no era la que este pendiente esperaba.**

La primera fue la limpieza que pedía: de **197 marcas a 126**, quitando el adorno de prosa a mano, molde por molde, con las citas de regla escritas en formato canónico de paso.

La segunda fue el hallazgo. Las 126 que quedaban se clasificaron una por una, y **ninguna era adorno**: 23 en títulos y nombres de sección, 21 tras un identificador en negrita, 39 en celdas de tabla y 43 rótulos de campo con su espacio por llenar. Este pendiente daba por hecho que había que decidir si se declaraban notación. No hubo nada que decidir: **el anexo ya lo decía**. Sus filas dicen «la raya larga **como inciso**» y «el punto medio separando frases **en prosa**», y un título no es un inciso ni una celda es prosa. El contador era más ancho que la regla.

**Los moldes del ciclo quedaron en 0**, sin renombrar una sola sección y sin romper la comprobación de forma de 651 documentos. El árbol entero bajó de **15 485 a 6 440**.

**Es la segunda vez que ocurre lo mismo.** El 2026-08-18 pasó con el punto medio de los encabezados, y quedó escrito en el anexo que el código ya lo tenía decidido y no lo había implementado. Vale la pena mirar si hay una tercera.
