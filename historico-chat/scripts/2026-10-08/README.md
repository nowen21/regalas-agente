# Los guiones de apoyo del 2026-10-08

| Archivo | Para qué | Fase |
|---|---|---|
| `ver_pestanas.mjs` | Abre el gasto en Chrome sin ventana, pulsa cada pestaña (también mientras otra carga), cuenta lo que se ve y abre un «?» | `B-EP-028-HU-007-pestanas-y-ayuda-del-gasto` |
| `salida_ver_pestanas.txt` | La salida de `ver_pestanas.mjs` después de la corrección | La misma |
| `pestanas.png` | La pantalla con la pestaña Contexto escogida | La misma |
| `diagnostico_sin_trabajo.py` | Clasifica por causa los mensajes sin trabajo de los últimos días; solo lee | `B-EP-025-HU-028-ningun-mensaje-sin-trabajo` |
| `salida_diagnostico_sin_trabajo.txt` | El diagnóstico después de traer las líneas y recalcular: 0 sin trabajo | La misma |
| `salida_reinicio.txt` | El vigilante relevándose solo al cambiar un archivo de código | `A-EP-025-HU-029-reinicio-solo` |
| `salida_recalcular_trabajo.txt` | Los mensajes sin trabajo antes y después de `recalcular_trabajo` en la base real | `A-EP-025-HU-028-el-trabajo-abierto` |

Antes de corregir, la salida decía: `pulsada «Dónde se gasta» mientras cargaba el Resumen: … "activa":"Dónde se gasta","contenido":"/gasto/pestana/resumen/…"`: la pestaña marcada era una y el contenido, otro.

En el ciclo 2 se agregó el caso que reportó el usuario: agrupar en «Dónde se gasta» y pasar a otra pestaña. Antes de corregir, la consola decía `htmx:targetError, #pestana` y la caja de la pestaña había desaparecido.
