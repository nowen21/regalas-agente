# Hecho · El validador de la `F22` tiene su fase

Origen: pendiente 38, abierto y cerrado el 2026-08-16, versión **21.3.1**.

| | |
|---|---|
| **De dónde salía** | El hallazgo H-3 del [resumen del 2026-08-16](../../historico-chat/resumenes/2026-08-16/sesion.md) |
| **Proyecto de origen** | El estándar mismo |
| **Dónde se construyó** | Fase [`A-EP-004-HU-015-retrodocumentar-la-comprobacion-de-la-f22`](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-015-derogacion-sin-adoptar/A-EP-004-HU-015-retrodocumentar-la-comprobacion-de-la-f22/) |

## Qué pasaba

El 2026-08-16 se escribió [`02·F22`](../../base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md) y, en la misma sesión, el programa que la comprueba: `derogaciones`, `sin_adoptar` y `validar_fase` en `validadores/version.py`, llamados desde `validadores/flujo.py`.

Eso es desarrollo, y [`02·F0`](../../base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) pide recorrer la cadena entera sin atajos por tamaño. No hubo historia ni fase: el código existía y su cadena no. Lo grave era de dónde venía — el mismo repositorio que escribe la regla, incumpliéndola mientras la escribe.

## Cómo cerró

Con la fase `A` de la [HU-015](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-015-derogacion-sin-adoptar/HU-015-derogacion-sin-adoptar.md): plan de trabajo, plan de pruebas, resultado y cierre. **No se cambió una línea de producción**, que era justamente el alcance: retrodocumentar no es reescribir.

Los tres criterios quedaron con evidencia de una corrida real, en [`validadores/tests/test_version_derogaciones.py`](../../validadores/tests/test_version_derogaciones.py):

- Un proyecto atrasado **con fases** falla, y la falla nombra la regla jubilada, su versión y su reemplazo.
- Lo ya adoptado no se vuelve a cobrar.
- Sin fases no se cobra, que es lo que `F0` exceptúa.
- Sin `CLAUDE.md` o sin versión declarada, calla en vez de romper, y comprobar no modifica nada.

**Los casos corren contra las derogaciones reales del estándar**, no contra una inventada: si cambia la marca del encabezado que `20·M11` exige, la prueba lo dice en vez de pasar contra un dato de mentira.

## Lo que se supo al cerrarlo

**El diagnóstico estaba a medias.** El pendiente decía que el código había quedado «sin el registro que dice por qué es como es», y resultó que `validadores/docs/version.md` ya lo explicaba con ejemplos de lo que retorna cada función.

Lo que faltaba no era documentación: era **prueba**. Un trabajo que se salta la fase se queda sin plan de pruebas, y eso es lo que no se recupera solo — la explicación se puede escribir después, la evidencia de que funcionaba el día que se escribió, no.

## Lo que quedó fuera

- Reconocer cuál de las fases abiertas es la que adopta la derogación, para dejarla pasar.
- El filtro de las reglas opcionales que el proyecto nunca encendió.
- La especificación del módulo de comprobación, que sigue sin existir.
- **Mirar cuánto trabajo más del propio estándar se hizo sin cadena.** El pendiente lo proponía y no se hizo acá: es un barrido, no una fase.

## Cómo se supo que cerró

La fase existe con su plan, su resultado de pruebas y su cierre, y la HU-015 la nombra en su sección 8.
