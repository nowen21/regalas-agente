# Pendiente · El marcador nunca se resuelve bien dentro de un proyecto

**Estado:** **cerrado** el 2026-08-16 (v21.1.1) · anotado el mismo día.

| | |
|---|---|
| **De dónde sale** | El hallazgo H-3 del [resumen del 2026-08-16](../../historico-chat/resumenes/2026-08-16/un-pendiente-no-es-un-plan.md) |
| **Historia que lo recoge** | [EP-004 · HU-005](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-005-enlaces-y-citas) |
| **Fase donde se construyó** | [`A-EP-004-HU-005-el-marcador-se-resuelve-contra-el-estandar`](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-005-enlaces-y-citas/A-EP-004-HU-005-el-marcador-se-resuelve-contra-el-estandar) — veredicto **Cumple** |
| **Proyecto de origen** | El estándar mismo, destapado al revisar lo que reportó `shopnest-mesa` |

## El problema

[`validadores/enlaces.py`](../../validadores/enlaces.py) resuelve `«RUTA-ESTANDAR»` contra `raiz` —la carpeta que está validando— dando por hecho que esa raíz **es** el estándar:

```python
if ruta.startswith(MARCADOR_RAIZ):
    base = raiz
```

Dentro del estándar la suposición se cumple. Pero el enganche lo corre así:

```
python "<carpeta-del-estandar>/validadores/enlaces.py" --raiz "<carpeta-del-proyecto>"
```

Ahí `raiz` es el proyecto, así que el marcador se resuelve contra `<proyecto>/base/…`, una carpeta que **nunca existe**: el instalador no copia `base/` a ningún proyecto, lo engancha por ruta absoluta. O sea que dentro de un proyecto el marcador no se resuelve bien nunca — ni cuando está bien puesto.

**Por qué importa aunque se cierre el [40](el-instalador-rellena-los-marcadores.md):** aquel quita los marcadores que hoy se escapan. Este cubre el que se escape mañana. Sin él, el revisor de enlaces da un veredicto que depende de desde dónde se lo corra.

## Qué falta

1. Que `base` sea la carpeta donde vive el estándar —la del propio módulo— y no la raíz que se está validando. Dentro del estándar las dos son la misma carpeta, así que acá no cambia nada.
2. Su caso de prueba: el mismo `.md` con el mismo marcador da el mismo veredicto corriendo con `--raiz` sobre el estándar y sobre un proyecto.

## Lo que se vio de paso, y no es este pendiente

`enlaces.py` no tiene bloque `__main__`: correrlo directo no imprime nada y sale con código 0, que se lee como "sin hallazgos". Se comprueba con `validar.py estandar`. Ya pasó una vez que se dio por bueno un resultado que nadie había calculado. Merece su propio pendiente si nadie lo resuelve de camino.

## Cómo se sabe que cerró

Un `.md` con `«RUTA-ESTANDAR»` da el mismo veredicto se corra desde donde se corra, y hay una prueba que lo fija.

## Qué pasó al cerrarlo

Las dos cosas se cumplen, sin sorpresas: el caso salió verde a la primera.

- **El marcador se resuelve contra la carpeta donde vive el estándar**, deducida del propio archivo. Corriendo sobre el estándar las dos carpetas coinciden, así que acá no cambió nada — y eso **se comprobó comparando** la salida de `validar.py estandar` antes y después: idénticas línea por línea. Sin esa comparación, «no cambió nada» habría sido una afirmación sin respaldo.
- **La prueba está en** [`validadores/tests/test_enlaces_marcador.py`](../../validadores/tests/test_enlaces_marcador.py). Comprueba las dos direcciones: que la cita buena no se reporte desde ninguna carpeta, y que la que no resuelve **se siga reportando** — un arreglo que callara sería peor que el defecto.
- **Se comprobó que la prueba no es vacía:** cargando en memoria la versión vieja del programa, el caso se pone rojo.

**Lo que se vio de paso y sigue abierto:** `enlaces.py` no tiene bloque `__main__`. Correrlo directo no imprime nada y sale con código 0, que se lee como «sin hallazgos» — y ya pasó una vez en esta misma sesión: se dio por buena una comprobación que nadie había calculado. Es de la [HU-008](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-008-corrida-completa), no de esta, y merece su propio pendiente.
