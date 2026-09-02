# HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido

Contenido inmediato de esta carpeta.

| Qué | De qué se trata |
|---|---|
| [HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido.md](HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido.md) | La historia de usuario: que el número que dice cuánto falta no cuente como hecha una fase que no cumplió |
| [documentacion/epicas/EP-004-comprobacion-automatica/HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido/A-EP-004-HU-021-la-cuenta-mira-el-veredicto/](A-EP-004-HU-021-la-cuenta-mira-el-veredicto/) | **Cerrada, Cumple.** El conteo separa terminadas de cumplidas, y los moldes ganan una sola forma de decirlo |
| [documentacion/epicas/EP-004-comprobacion-automatica/HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido/B-EP-004-HU-021-el-veredicto-se-lee-en-sus-tres-formas/](B-EP-004-HU-021-el-veredicto-se-lee-en-sus-tres-formas/) | **Cerrada, Cumple.** Corrige un defecto de la `A`: leía dos de las tres formas en que el veredicto está escrito |
| [documentacion/epicas/EP-004-comprobacion-automatica/HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido/C-EP-004-HU-021-cualquier-encabezado-de-veredicto-se-lee/](C-EP-004-HU-021-cualquier-encabezado-de-veredicto-se-lee/) | **Cerrada, Cumple.** Corrige un defecto de la `B`: dijo «tres formas y 39 fases sin encabezado», y sin encabezado hay **2** |

Nace de `S-054`: cerrar cinco fases con veredicto «No cumple» bajó el número de incompletas en cinco.

**Diecinueve fases cerradas dicen «No cumple», y las diecinueve contaban como completas.** De las 84 historias que el inventario daba por hechas, casi una de cada cuatro descansaba en una fase que no cumplió.

**Y la causa no era descuido: los dos moldes se contradecían.** El del resultado decía `Cumple / No cumple`; el del cierre ofrecía `Cumple / Cumple con observaciones`, así que **no tenía forma de decir «No cumple»**. Por eso las 19 lo escribían en prosa, y lo que se inventaba cada uno ningún programa lo leía.

**Cómo quedó el número.** Antes decía `85 completas`. Ahora dice `84 terminadas, de las cuales 63 cumplen, 16 no cumplen y 5 no dicen si cumplen` — y las tres fases hicieron falta para llegar ahí: la `A` separó terminado de cumplido, y la `B` y la `C` enseñaron al programa a leer lo que las fases ya decían.
