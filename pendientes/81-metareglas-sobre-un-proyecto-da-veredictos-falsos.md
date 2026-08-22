# Pendiente · `metareglas --raiz` sobre un proyecto reporta cinco veredictos falsos

**Estado:** abierto, anotado el 2026-08-22.

| | |
|---|---|
| **Historia de usuario** | [EP-004 · HU-011 — Molde de las reglas](../documentacion/epicas/EP-004-comprobacion-automatica/HU-011-molde-de-las-reglas/HU-011-molde-de-las-reglas.md). Es el subcomando que esa historia construyó |
| **De dónde sale** | Ejecutar la fase [`A-EP-001-HU-006`](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-006-capa-propia-del-proyecto/A-EP-001-HU-006-retrodocumentar-la-capa-del-proyecto/resultado_pruebas.md), defecto D-01 |
| **Proyecto de origen** | El estándar mismo |

## El problema

`validar.py metareglas` tiene dos banderas y hacen cosas distintas:

- `--catalogo <proyecto>` comprueba `M16` sobre las reglas propias del proyecto. **Funciona.** Corrido contra AgroSystem encontró 56 reglas `P` sin respaldo.
- `--raiz <proyecto>` corre **las meta-reglas del estándar contra la carpeta del proyecto**.

Lo segundo no tiene sentido y no está impedido. Un proyecto no tiene `CHANGELOG.md`, ni `VERSION`, ni `base/20-meta-reglas/estructura-regla.md`, ni `validadores/reglas-validables.md`, así que el programa devuelve **una falla y cuatro avisos, los cinco falsos**:

```
[FALLA] <proyecto>/CHANGELOG.md — `VERSION` dice  y el CHANGELOG no tiene su entrada — M10 (fila 19)
[AVISO] <proyecto>/VERSION — no se pudo abrir: No such file or directory
[AVISO] <proyecto>/base/20-meta-reglas/estructura-regla.md — no se pudo abrir
[AVISO] <proyecto>/validadores/reglas-validables.md — no se pudo abrir
```

Y fíjese en la falla: dice «`VERSION` dice  y el CHANGELOG», con el hueco vacío donde iría la versión. El programa no encontró el archivo, siguió igual, y afirmó sobre lo que no leyó.

## Por qué importa

Es el caso borde que el [planteamiento](../prompts/cimiento-planteamiento.md) nombra en §8: **un validador que reprueba lo que está bien enseña a ignorar todos los veredictos**, y desde ahí ninguno sirve.

Además le pasa a quien hace lo natural. `--raiz` es la bandera que llevan casi todos los subcomandos para decir «mira este proyecto»; que en este signifique otra cosa es una trampa puesta.

Y hay un daño ya ocurrido: la fase que lo encontró llevaba cinco días detenida en parte porque su plan daba por inexistente la comprobación de `M16`. Existía; lo que no se sabía era cómo invocarla.

## Qué falta

Que `metareglas` sepa que le están apuntando a un proyecto y no al estándar. Dos salidas:

1. **Que `--raiz` rechace lo que no es el estándar.** Si la carpeta no tiene `base/` y `VERSION`, el programa dice que eso no es el estándar y sale, en vez de reportar sobre archivos que no leyó. Barato, y quita el veredicto falso.
2. **Que `--raiz` sobre un proyecto haga lo correcto**, es decir, lo mismo que `--catalogo`. Más cómodo para quien lo usa, pero cambia lo que significa la bandera y hay que mirar quién la llama hoy.

Conviene la primera, y de paso arregla lo otro: **una comprobación que no pudo abrir su archivo no debe afirmar nada**. Que la falla de `M10` salga con la versión vacía es el mismo defecto visto de cerca.

## El límite

No cubre los demás subcomandos. Si el mismo problema aparece en otros, sale como pendiente aparte, y conviene mirarlo: `--raiz` significa «el proyecto» en casi todos.

No corrige las 56 reglas de AgroSystem: eso es del proyecto y va por el canal de defectos de vuelta.

## Cómo se sabrá que cerró

`python validadores/validar.py metareglas --raiz <un proyecto cualquiera>` no devuelve ninguna falla ni aviso sobre archivos del estándar, y dice en una línea que esa carpeta no es el estándar. Y una prueba nueva escribe una carpeta sin `base/` y comprueba que el programa no afirma nada sobre ella.
