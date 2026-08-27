# Programas de un solo uso · 2026-08-25

Los quince programas que el agente escribió el 2026-08-25, construyendo las fases de la versión 1 de la plataforma. **No se vuelven a correr**: llevan dentro la ruta de la máquina donde corrieron, y escriben sobre texto que ya cambió.

De qué sesión salen: [2026-08-22 · sesion-6](../../2026-08-22-sesion-6.md), que cruzó varios días.

> **Estos quince llegaron tarde al repositorio.** Se escribieron en la carpeta temporal del sistema y se trajeron el 2026-08-27, cuando el usuario preguntó por qué se seguía escribiendo afuera. Está contado en `S-057`.

## Qué hizo cada uno

### El código de las fases de la plataforma

| Programa | Qué hizo |
|---|---|
| `core_c.py` | Agregó a `nucleo/proyectos/core.py` lo de la fase `C`: la ruta que se pierde se avisa |
| `core_h.py` | Reescribió ese mismo archivo con lo de la fase `H`: desconectar saca y no borra |
| `hueco_e.py` | Cerró el hueco de la fase `E`: `cvds/` entra a lo que se trae |
| `reporte_f.py` | Agregó a `nucleo/importacion/core.py` el reporte de la fase `F` |
| `aplicar_h.py` | Resolvió en el plan de la fase `H` las dudas que la detenían |

### Sus pruebas

| Programa | Qué hizo |
|---|---|
| `tests_c.py` | La ruta perdida se avisa y no pierde nada |
| `tests_f.py` | Qué dice el reporte guardado |
| `tests_g.py` | El estado de un proyecto con documentación traída |
| `tests_h.py` | Desconectar saca y no borra, y la marca vive en el texto |

### Los sabotajes

| Programa | Qué hizo |
|---|---|
| `sabotaje_c.py` · `sabotaje_e.py` · `sabotaje_f.py` · `sabotaje_g.py` · `sabotaje_h.py` | Uno por fase. Cada uno lleva escritas en su cabecera **las lecciones de los anteriores**: restaurar con copia y no con git (fase `B`), declarar los rastros que quedan fuera del código, y correr el escenario en vez de suponer el diagnóstico |

### Las marcas que nadie ponía

| Programa | Qué hizo |
|---|---|
| `marcar_23.py` | Pasó a cerrada la estación de 23 fases que estaban cerradas de hecho, comprobado contra `git log`. Es el pendiente 87 |

## Lo que no está acá

**Dos clones enteros de la plataforma** (`limpio/` y `limpio2/`, 6.831 archivos con su `.venv`), del experimento que comprobó que **la configuración de git no viaja al clonar**. Traerlos sería meter un entorno virtual al repositorio; lo que valía era el resultado, y quedó escrito en la fase que lo midió.
