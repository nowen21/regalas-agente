# Resultado de Pruebas — Fase C-EP-001-HU-007-el-barrido-de-candidatas-tiene-molde-y-disparador

**Para qué sirve este documento.** Dice qué se ejecutó, con qué y qué dio. El plan está en [plan_pruebas.md](plan_pruebas.md).

## 0. Veredicto

**Cumple**, ciclo 1. Cinco casos de cinco. Ejecutado el 2026-08-22 contra la versión 30.9.1, en Windows con Python 3.

## 1. Caso por caso

| Caso | Resultado | Veredicto |
|---|---|---|
| CP-01 · el molde habría producido el barrido de 2026-08-13 | las 27 fichas caen en las cuatro salidas, sin sobrar ninguna | ✅ |
| CP-02 · el disparo existe en el flujo | `M20` dice «antes de publicar una versión», momento que `20·M10` ya obliga a atravesar | ✅ |
| CP-03 · la regla cumple el checklist | `validar.py metareglas`: sin incumplimientos | ✅ |
| CP-04 · nada se rompe | `validar.py estandar`: sin incumplimientos | ✅ |
| CP-05 · el texto heredable sin marcas | `validar.py marcas --preparados`: cero fallas | ✅ |

## 2. La evidencia de CP-01, contada

El barrido viejo escribió sus salidas con otras palabras. Contadas una por una:

| Salida del barrido de 2026-08-13 | Cuántas | A qué salida del molde corresponde |
|---|---|---|
| «Ya está cubierta» | 13 | **Ya está cubierta** |
| «Complementar una regla» | 5 | **Afinar una existente** |
| «Afinar una regla» | 3 | **Afinar una existente** |
| «No es regla» | 4 | **No es regla del estándar** |
| «Regla nueva sin dependencia» | 2 | **Regla nueva** |

**27 de 27, y ninguna pidió una quinta salida.** Lo que el molde sí cambia es que junta «complementar» y «afinar» en una sola: son lo mismo dicho de dos formas, y tenerlas separadas obligaba a decidir cuál usar sin que la decisión cambiara nada.

## 3. Lo que costó llegar al verde

**CP-05 detuvo la publicación una vez.** El molde nuevo traía dos puntos medios y dos rayas en su cabecera y en sus tablas de ejemplo. Es texto que viaja a los proyectos, así que el trinquete lo cuenta y tiene razón: se cambiaron por comas y por la palabra «ninguna».

## 4. Lo que no se probó

**Que el barrido encuentre lo que hay que encontrar.** Eso solo se sabe corriéndolo: el primero real lo dispara la próxima publicación, y ahí se verá si el molde pide los datos correctos. Por eso `M20` queda clasificada como no validable hasta que se cumpla a mano ([`20·M19`](../../../../../base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md)).
