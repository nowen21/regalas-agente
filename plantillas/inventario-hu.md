# Inventario de HU — «nombre del proyecto o del conjunto»

> Plantilla. Es el tablero de **qué historias de usuario están completas y cuáles no**. Reemplace los `«…»`, borre esta caja y las notas entre paréntesis.
>
> **No reemplaza a la HU ni a la fase.** Solo dice qué existe y qué falta, para no tener que recorrer las carpetas a mano cada vez que alguien pregunta cuánto falta.
>
> Vive donde el proyecto lleve su backlog — en el estándar, `pendientes/`; en un proyecto, `documentacion/`.
>
> **Este documento no guarda la cuenta, y esa es su regla principal.** Hasta la versión 34.1.0 traía tres campos con el total, las completas y las incompletas, más una tabla con una fila por historia y una casilla por documento, todo mantenido a mano. Se quitó porque **se desfasa**: en el estándar pasó tres veces, y la última decía 78 historias donde el árbol tenía 113. Cuatro de sus filas daban por completa una historia que no lo estaba. Un dato que vive en dos sitios se separa; este vive en uno solo y se pregunta con un comando.

| Items | Lo que se debe hacer |
|---|---|
| **Qué pasa** | [`02·F12.2`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md) pide al menos una fase por HU, y cada fase deja cinco documentos. |
| **Cuántas faltan** | Lo dice el árbol, no este archivo. Se corre el comando de abajo: la última línea da el total, las completas y las incompletas |
| **Qué le falta a cada una** | El mismo comando lo lista, historia por historia, nombrando el documento que falta |
| **Cierra cuando** | Ese comando reporte cero incompletas |

*Anotado el «AAAA-MM-DD».*

## Cómo se pregunta cuánto falta

Desde la raíz del proyecto:

```
python "«RUTA-ESTANDAR»/validadores/validar.py" fases --raiz .
```

Nombra cada historia sin fase y cada fase a la que le falta alguno de sus cinco documentos, diciendo cuál. Y termina con la cuenta.

**Las comillas no sobran.** La ruta al estándar puede tener espacios (la del propio estándar los tiene), y sin comillas la terminal parte la orden por la mitad. Se descubrió corriéndolo, no leyéndolo.

**No hay nada que instalar.** Los validadores del estándar no se copian al proyecto: los enganches los llaman en su sitio, y este comando hace lo mismo a mano.

**Si vuelve a escribir la cuenta acá, el estándar se lo avisa.** No lo corrige, porque los programas de comprobación reportan y no corrigen. Pero lo dice, para que la segunda copia no aparezca sin que nadie se entere.

## Cómo se completa una historia

1. **Una historia a la vez.** No se abren dos en paralelo.
2. Se crea la carpeta `<letra>-EP-000-HU-000-<slug>` dentro de la carpeta de la HU ([`02·F12.6`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)), **con su `plan_trabajo.md` adentro**. El control de versiones no guarda carpetas vacías: una fase abierta y todavía sin plan existiría en una sola máquina, no entraría en ningún commit, y ningún clon la vería.
3. Los documentos se escriben **en este orden**: `plan_trabajo`, `plan_pruebas`, `resultado_pruebas`, `estado-fase`, `funcionalidad_implementada`. Ninguno se adelanta al anterior.
4. Cada archivo sale de su plantilla de `plantillas/` — la estructura no se inventa.
5. Al escribir el último de los cinco se corrige la **§8 de la HU**, que hasta ese momento dice que no se descompuso en fases, y su **Estado** de la §1.
6. Una fase a medias no se deja sin que su `estado-fase` diga qué la tiene detenida. **Es lo único de esta lista que el árbol no puede deducir solo**: que un documento falte se ve; por qué falta, no.

## Qué clase de trabajo es

> (Borre el que no aplique, o escriba el reparto si hay de los dos.)

- **Construcción** — la HU no se ha hecho: la fase se planifica, se prueba y se implementa.
- **Retrodocumentación** — el código ya existe y ya funciona; lo que falta es el documento que diga con qué plan se hizo, con qué casos se probó y qué salió. Se escribe contra lo que ya está en el repositorio, **sin tocar una línea de producción**.

Mezclar los dos en el mismo inventario está bien, pero **no en la misma historia**: una HU construida a medias se termina de construir, no se retrodocumenta.

## Por qué cambió la cuenta

> Acá van los cambios de la cuenta que **no se explican solos**, con su fecha. Es lo único de este documento que no está en el árbol, y por eso es lo único que se escribe a mano.
>
> Sirve para que una subida o una bajada no se lean al revés. Ejemplo del estándar: *«68 a 74 total: seis historias nuevas escritas al enrutar el backlog. No es trabajo nuevo — es trabajo que ya existía y no tenía a quién rendirle cuentas.»* Sin esa línea, el número parece un retroceso.

## Cómo se sabe que cerró

El comando reporta **cero incompletas**, y ni él ni el validador de trazabilidad nombran una historia sin fase.

Y se sabe **sin editar este archivo**.
