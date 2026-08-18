# B-EP-002-HU-002-la-entrada-se-entiende-sin-conocer-el-proyecto

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se hace y sobre qué archivos |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se comprueba |
| [resultado_pruebas.md](resultado_pruebas.md) | Qué se ejecutó y el veredicto |
| [estado-fase.md](estado-fase.md) | En qué estación va |
| [funcionalidad_implementada.md](funcionalidad_implementada.md) | Qué quedó hecho |

**Sale de una prueba que falló.** El `CA-03` de esta historia exige que una entrada del registro se entienda sin haber seguido el trabajo. Se le mostró al usuario la entrada de la `15.2.0` y respondió **«no entendí nada»**.

**No era una entrada mala: eran todas.** De las 83, 74 citan una ruta, 43 un identificador de regla, y **ninguna** tiene menos de tres marcas de jerga.

Nace [`20·M17`](../../../../../base/20-meta-reglas/reglas/M17-la-entrada-del-registro-abre-en-castellano-llano.md): la entrada abre con qué cambió y por qué, y el detalle va debajo.

**Estado:** estación 8, [v23.9.0](../../../../../CHANGELOG.md). Veredicto **Cumple**, 5 casos.
