# Pendiente · `cerrar.py` reescribe el enlace de salida con el espacio sin codificar

**Estado:** cerrado el 2026-08-22, versión 30.6.0 · anotado 2026-08-20.

| | |
|---|---|
| **Historia de usuario** | [EP-005 · HU-003 — Disparo al escribir un archivo](../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-003-disparo-al-escribir-un-archivo/HU-003-disparo-al-escribir-un-archivo.md) — su fase C es la que dejó a `cerrar.py` moviendo el pendiente y recalculando sus enlaces |
| **Proyecto de origen** | **shopnest-mesa** · `C:/DesarrollosClaude/personales/shopnest-mesa` |
| **Su pendiente de seguimiento** | `pendientes/41-cerrar-reescribe-el-enlace-con-el-espacio-sin-codificar.md` — queda **abierto allá** hasta que este se corrija |
| **A quién avisar al cerrar** | a **todos los instalados**: `cerrar.py` corre igual en cualquier proyecto que cierre un pendiente con un enlace al estándar — la lista está en [../plantillas/proyectos.md](../../plantillas/proyectos.md) |

## El problema

`reescribir_salientes()` ([validadores/cerrar.py](../../validadores/cerrar.py), líneas 111-135) recalcula los enlaces de salida del archivo que se mueve: resuelve el destino con `unquote` (`_resuelve_a`, línea 75), calcula la ruta nueva con `os.path.relpath` (`_nuevo_destino`, línea 105) y la escribe **tal cual**, sin volver a codificar. Un destino que llegó como `../../../../../Ing.%20Jose/ia/agente/...` sale como `../../../../../Ing. Jose/ia/agente/...`.

Y el validador no lo ve: `_ENLACE` en [validadores/comun.py](../../validadores/comun.py) (línea 29, `[^)\s]+`) corta el destino en el primer espacio, así que el enlace reescrito **deja de ser un enlace** para `validar.py estandar`. Se comprobó escribiendo un enlace a un archivo inexistente con espacio en la ruta: cero fallas.

Es el 33·1 visto del otro lado: aquel arregló la **lectura** (`unquote` antes de buscar); este es la **escritura**, que deshace lo que la lectura ya entiende.

## Cómo se reproduce

`shopnest-mesa`, 2026-08-20. El cierre de su pendiente 20 llevaba, como comprobación del 33·1, un enlace a `../../../../Ing.%20Jose/ia/agente/validadores/enlaces.py`. Se cerró con:

```
python validadores/cerrar.py 20 --como 20-el-validador-no-decodifica-los-enlaces-con-espacio --fecha 2026-08-20 --raiz C:/DesarrollosClaude/personales/shopnest-mesa --aplicar
```

En `pendientes/hecho/20-....md` el enlace quedó `(../../../../../Ing. Jose/ia/agente/validadores/enlaces.py)`. `validar.py estandar` en verde. Luego, con un `.md` y a propósito: `[x](../../../../Ing. Jose/ia/agente/plantillas/nada.md)` — el archivo no existe y el validador no dijo nada.

## Por qué importa

No bloquea. El daño es doble y lento: el enlace deja de abrir en cualquier visor que siga CommonMark —el espacio termina el destino—, y el validador que existe para atraparlo deja de verlo. Hoy hay un solo caso porque enlazar al estándar con `%20` se habilitó hace tres días (33·1); va a crecer con cada cierre que cite el estándar, que es justamente lo que `02·F24` pide que hagan los proyectos.

## Qué falta

Dos cosas, y la segunda es la que evita que vuelva:

1. `_nuevo_destino()` devuelve la ruta relativa **codificada** (`urllib.parse.quote` sobre cada tramo, respetando `/` y `..`), o conserva el destino escrito cuando solo cambia el prefijo `../`. El mismo cuidado en `mover()` para las citas de entrada y en `enlaces.reparar_texto` si recalcula destinos.
2. `comun._ENLACE` —o `enlaces()`— debería, como mínimo, **avisar** del enlace cuyo destino lleva un espacio en vez de ignorarlo: hoy un destino con espacio es invisible para todo validador que use `enlaces()`.

## Cómo cerró

Las dos piezas que pedía, con prueba cada una:

1. `_nuevo_destino()` de `cerrar.py` devuelve el espacio codificado (`%20`); los acentos se dejan literales porque así los escribe y resuelve todo el repositorio. Prueba: mover un pendiente con un enlace a `../con%20espacio/x.md` conserva el `%20` y `validar.py estandar` lo resuelve.
2. `enlaces.py` gana `destinos_con_espacio()`: el enlace cuyo destino lleva un espacio literal ya no es invisible: `validar.py estandar` lo avisa y dice cómo escribirlo. Al estrenarlo encontró **9** en el propio repositorio que ningún validador veía; se corrigieron en la misma ronda.

## El límite

No cubre los enlaces con espacio que ya estén escritos a mano en otros repositorios, ni decide si el estándar prefiere `%20` o `<...>` para rutas con espacio.

## Cómo se sabrá que cerró

Una prueba en `validadores/tests/` que mueva un `.md` con un enlace de salida a `.../con%20espacio/x.md` y compruebe que el destino reescrito conserva `%20` y que `validar.py estandar` lo resuelve; y otra que un destino con espacio literal no pase en silencio. Del lado de `shopnest-mesa`, cerrar un pendiente cuyo cierre enlace al estándar y ver el `%20` intacto.
