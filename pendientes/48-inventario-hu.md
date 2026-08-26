# Inventario de HU — el estándar


| Items|Lo que se debe hacer |
|---|---|
| **Historia de usuario** | [EP-004 · HU-017 — Inventario de HU sin fase](../documentacion/epicas/EP-004-comprobacion-automatica/HU-017-inventario-de-hu-sin-fase/HU-017-inventario-de-hu-sin-fase.md), que hizo la cuenta automática, y [EP-004 · HU-019](../documentacion/epicas/EP-004-comprobacion-automatica/HU-019-inventario-que-no-se-mantiene-a-mano/HU-019-inventario-que-no-se-mantiene-a-mano.md), que quitó la copia a mano. Las 42 dudas que lo detenían son el [59](hecho/las-42-dudas-que-detenian-26-fases.md) |
| **Qué pasa** | `02·F12.2` pide al menos una fase por HU, y cada fase deja cinco documentos. |
| **Cuántas faltan** | Lo dice el árbol, no este archivo. Se corre `python validadores/validar.py fases` desde la raíz: la última línea da el total, las completas y las incompletas |
| **Qué le falta a cada una** | El mismo comando lo lista, historia por historia, nombrando el documento que falta |
| **Cierra cuando** | Ese comando reporte cero incompletas |

**Este archivo ya no guarda la cuenta, y esa es la corrección.** La guardó hasta el 2026-08-26 y se desfasó tres veces: la última decía 78 historias donde el árbol tenía 113, y su propia tabla traía 74 filas — ni siquiera cuadraba consigo misma. De esas 74, **26 tenían alguna casilla equivocada y 4 daban por completa una historia que no lo estaba**. Un dato que vive en dos sitios se separa; ahora vive en uno solo y se pregunta con un comando.

*Anotado el 2026-08-16 sobre 66 HU —14 completas y 52 incompletas—, y ese mismo día nacieron [HU-017](../documentacion/epicas/EP-004-comprobacion-automatica/HU-017-inventario-de-hu-sin-fase/HU-017-inventario-de-hu-sin-fase.md) y [HU-018](../documentacion/epicas/EP-004-comprobacion-automatica/HU-018-numero-de-pendiente-ya-tomado/HU-018-numero-de-pendiente-ya-tomado.md), que lo dejaron en 68 y 54. La HU-017 es la que hace esta cuenta sola.*

> **Los tres números cambiaron el 2026-08-17 y conviene leer por qué, o se leen como un retroceso.**
>
> **68 → 74 total.** Seis historias nuevas, escritas al enrutar el backlog: ningún pendiente podía quedar suelto y seis no tenían dónde caer. No son trabajo nuevo pendiente — son trabajo que ya existía y no tenía a quién rendirle cuentas.
>
> **39 → 31 completas.** Ocho historias que estaban completas ganaron una fase **sin terminar**, y una fase a medias vuelve incompleta a su historia. Seis vienen de la sesión que ejecutaba los 51 planes y quedó detenida; la séptima es la fase `B` de [EP-004 · HU-016](../documentacion/epicas/EP-004-comprobacion-automatica/HU-016-el-pendiente-cerrado-nombra-su-fase/), que espera aprobación.
>
> **2026-08-20 · 78 total, 47 completas.** Nacieron [EP-005 · HU-015](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-015-lo-que-llega-de-afuera-llega-marcado/HU-015-lo-que-llega-de-afuera-llega-marcado.md) y [EP-005 · HU-016](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-016-la-traza-de-la-sesion-paso-a-paso/HU-016-la-traza-de-la-sesion-paso-a-paso.md), cada una con su fase A levantada por el andamio con los cinco documentos; cuentan como completas aunque la fase esté en curso, porque el conteo mira que los documentos existan, no que estén terminados.
>
> **2026-08-18 · sube a 33.** La [EP-001 · HU-011](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-011-buscar-antes-de-preguntar/HU-011-buscar-antes-de-preguntar.md) —buscar en el repositorio antes de preguntar— cerró su fase `A` con los cinco documentos. Nació ayer al enrutar el backlog y se construyó hoy. Y la [EP-007 · HU-008](../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-008-el-proyecto-reporta-al-estandar/HU-008-el-proyecto-reporta-al-estandar.md) —el proyecto reporta lo que es del estándar y el estándar le avisa de vuelta— cerró la suya, también del día a la mañana siguiente.
>
> **2026-08-18, más tarde · sube a 34.** La [EP-004 · HU-012](../documentacion/epicas/EP-004-comprobacion-automatica/HU-012-marcas-de-generacion-automatica/HU-012-marcas-de-generacion-automatica.md) —comprobar las marcas de generación automática— cerró su fase `A`, **que llevaba un día detenida por una duda que su propio pendiente ya contestaba**.
>
> **2026-08-18, al final del día · sube a 35.** La [EP-005 · HU-002](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-002-enmascarar-claves/HU-002-enmascarar-claves.md) —enmascarar la clave antes de escribirla— cerró la suya. Era la fase con daño vivo: hasta hoy, una clave pegada en el chat quedaba escrita en claro en un archivo que se versiona.
>
> **2026-08-19 · sube a 43.** [EP-001 · HU-008](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-008-derogacion-sin-borrar/) —la derogación sin borrar— y [EP-002 · HU-001](../documentacion/epicas/EP-002-versionado-y-adopcion/HU-001-numero-de-version-y-que-significa/) —qué significa el número de versión— recibieron los dos documentos que les faltaban, y sus fases quedaron con los cinco.
>
> **Y la cifra escrita acá llevaba dos de retraso.** Lo dijo la prueba que compara este encabezado con lo que cuenta el programa, no una lectura: un inventario a mano se desactualiza el día que alguien cierra algo y no vuelve acá, que es siempre.
>
> **Y las seis histórias nuevas entran a la tabla.** Contaban en el total desde ayer, pero no tenían fila: el total decía 74 y la tabla listaba 68. Un inventario al que hay que creerle el encabezado porque su propia tabla no lo respalda no sirve de inventario.
>
> **No se deshizo nada.** Las 39 que estaban cerradas siguen cerradas; lo que pasó es que se abrió trabajo encima. El número baja porque mide *historias sin nada pendiente*, no *trabajo hecho*.


## Qué le falta a cada HU

**Lo dice el árbol.** Desde la raíz del repositorio:

```
python validadores/validar.py fases
```

Nombra cada historia sin fase y cada fase a la que le falta alguno de sus cinco documentos, diciendo cuál. Y termina con la cuenta: cuántas historias hay, cuántas completas y cuántas incompletas.

**Acá hubo una tabla con una fila por historia, y se quitó el 2026-08-26.** No porque estorbara: porque **era una segunda copia de algo que el árbol ya sabía**, y las dos copias se separaron. Le faltaban 39 historias, 26 de sus 74 filas tenían alguna casilla equivocada, y cuatro daban por completa una historia que no lo estaba — que es la dirección que hace daño, porque esconde trabajo en vez de inventarlo.

Antes de quitarla se comparó fila por fila contra el árbol: **ninguna guardaba trabajo que no estuviera ahí**, y los 74 enlaces resolvían. No se perdió nada. Si hace falta verla, sigue en el historial.

**Y no se reemplazó por un programa que la reescriba**, aunque `EP-004 §10.2` lo permitiría. Eso dejaría otra vez dos copias, con alguien teniendo que acordarse de correrlo: el mismo fallo, más lento.

## Cómo se completa una historia

1. **Una historia a la vez.** No se abren dos en paralelo.
2. Se crea la carpeta `<letra>-EP-0NN-HU-0NN-<slug>` dentro de la carpeta de la HU (`02·F12.6`), **con su `plan_trabajo.md` adentro**.
3. Los documentos se escriben **en este orden**: `plan_trabajo`, `plan_pruebas`, `resultado_pruebas`, `estado-fase`, `funcionalidad_implementada`. Ninguno se adelanta al anterior.
4. Cada archivo sale de su plantilla de [`plantillas/`](../plantillas/) — la estructura no se inventa.
5. Al escribir el último de los cinco se corrige la **§8 de la HU**, que hasta ahí dice que no se descompuso en fases, y su **Estado** de la §1.
6. Una fase a medias no se deja sin que su `estado-fase` diga qué la tiene detenida. Es lo único que el árbol no puede deducir solo: que un documento falte se ve, pero **por qué falta, no**.

**El paso 2 quedó decidido el 2026-08-17: la carpeta nace con su `plan_trabajo.md` adentro.** Git no guarda carpetas vacías, así que una fase abierta y todavía sin plan existe en la máquina donde se creó y en ninguna otra: no entra en ningún commit, un clon no la ve, y `fases.py` tampoco, porque lee el disco. La salida que eligió el usuario es que el problema no se presente: **no hay momento en que la carpeta exista vacía**.

De las tres salidas que estaban sobre la mesa —`.gitkeep` en cada carpeta, carpeta sola, o escribir ya el plan— se tomó la tercera. No hacen falta archivos de 0 bytes, y no queda nada afirmado que no se pueda comprobar en un clon.

**La plantilla [`inventario-hu.md`](../plantillas/inventario-hu.md) sigue describiendo la tabla que acá se quitó**, y ahora la diferencia es mayor que antes: un proyecto que herede el estándar arma su inventario a mano, con el mismo defecto que este archivo acaba de dejar atrás. Ponerla al día es cambio de `plantillas/`: suma entrada en el [CHANGELOG](../CHANGELOG.md) y sube [VERSION](../VERSION) (`20·M10`). **No se hizo acá porque el plan de esta fase no declara ese archivo** (`02·F8`), y tocarlo por iniciativa es lo que la regla prohíbe.

**Y el orden de llenado cambió a propósito.** El paso 1 pide una historia a la vez. El 2026-08-17 el usuario pidió el `plan_trabajo` de todas las fases que no lo tenían, que es lo contrario: recorrer un documento a lo ancho de muchas fases. Se hizo así, y tiene un costo: cada fase abierta queda a medias hasta que le entren los otros cuatro, y el paso 6 pide que no se deje así sin que su `estado-fase` diga qué la tiene detenida. Mientras esos `estado-fase` no existan, lo que dice qué falta es el `README.md` de cada carpeta de fase.

## Casi todo es retrodocumentación

No falta trabajo: falta la cadena. La memoria, el versionado, los validadores y los enganches **ya están construidos y cerrados** — los pendientes [02](hecho/vigencia-y-poda-de-memoria.md), [04](hecho/version-del-estandar.md), [05](hecho/memoria-semantica.md) y [validadores-y-hooks](hecho/validadores-y-hooks.md). Lo que no existe es el documento que diga con qué plan se hizo, con qué casos se probó y qué salió.

Por eso esas fases se escriben contra lo que ya está en el repo, sin tocar una línea de producción. Es lo mismo que se hizo en el [38](hecho/el-validador-de-la-f22-tiene-su-fase.md), donde se supo que al trabajo sin cadena no le faltaba documentación: le faltaba prueba atada a su criterio.

## Cómo se sabe que cerró

`python validadores/validar.py fases` reporta **cero incompletas**, y ni ese comando ni `validar.py trazabilidad` nombran una historia sin fase.

Y se sabe **sin editar este archivo**: esa es la diferencia con como estaba antes.
