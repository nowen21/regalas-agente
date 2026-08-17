# A-EP-001-HU-006-retrodocumentar-la-capa-del-proyecto

Contenido inmediato de esta carpeta.

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer, en qué orden y sobre qué archivos |

**Por qué esta fase no construye nada.** La capa propia existe y se usa: el instalador la crea, [`plantillas/reglas-proyecto.md`](../../../../../plantillas/reglas-proyecto.md) es su molde, [`20·M16`](../../../../../base/20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md) le exige respaldo y `validar.py version` lee qué versión declara adoptada. Lo que nadie ha hecho es probar el desempate: que el ajuste propio gane a la convención general y pierda contra el núcleo.

**Lo que la fase destapa.** La comprobación de `M16` está escrita en [`validadores/metareglas.py`](../../../../../validadores/metareglas.py) y no se puede correr: sin punto de entrada ni subcomando, termina en silencio con código 0. Es el mismo defecto del pendiente [53](../../../../../pendientes/53-enlaces-py-no-tiene-punto-de-entrada.md), y la fase lo deja anotado ahí en vez de abrir un pendiente nuevo.

**Lo que falta de la fase:** `plan_pruebas.md`, `resultado_pruebas.md`, `estado-fase.md` y `funcionalidad_implementada.md`. La fila de HU-006 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md) lleva la cuenta.

**Estado:** abierta con su plan escrito, sin aprobar. Dos dudas de §2.7 bloquean el arranque.
