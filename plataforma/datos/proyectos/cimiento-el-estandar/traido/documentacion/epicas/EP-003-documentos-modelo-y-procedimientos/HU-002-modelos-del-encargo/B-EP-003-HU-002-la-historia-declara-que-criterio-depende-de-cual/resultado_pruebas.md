# Resultado de Pruebas — Fase B-EP-003-HU-002-la-historia-declara-que-criterio-depende-de-cual

**Para qué sirve este documento.** Dice qué se ejecutó, con qué y qué dio. El plan está en [plan_pruebas.md](plan_pruebas.md).

## 0. Veredicto

**Cumple**, ciclo 1. Cuatro casos de cuatro.** Ejecutado el 2026-08-22 contra la versión 31.1.0, en Windows con Python 3.

## 1. Caso por caso

| Caso | Resultado | Veredicto |
|---|---|---|
| CP-01 · se entiende sin ir a otro lado | la frase contesta las dos preguntas | ✅ |
| CP-02 · la historia sin dependencias no paga | columna vacía, tabla válida, ningún validador la reporta | ✅ |
| CP-03 · el estándar sigue coherente | `validar.py estandar`: sin incumplimientos | ✅ |
| CP-04 · sin marcas | `validar.py marcas --preparados`: cero fallas | ✅ |

## 2. Lo que costó llegar al verde

**Nada.** Es el cambio más barato de los cuatro que dejó abierto el pendiente 33, y salió a la primera.

## 3. Lo que no se probó

**Que la dependencia declarada sea la correcta.** Ningún programa puede decidir si un criterio depende de otro; lo decide quien escribe la historia, y por eso la columna no tiene validador.
