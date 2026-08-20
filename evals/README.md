# Banco de evaluación del estándar

Sin esto, cada cambio del estándar es una apuesta: se toca una regla o un
validador y nadie mide si el conjunto sigue atrapando lo que atrapaba. Este
banco convierte esa duda en un número. Viene de la brecha que dejó escrita el
análisis contra [notas/estructura.md](../notas/estructura.md) (§9 · Evaluación).

## Correr

```
python evals/correr.py
```

Sale con 0 si todos los casos pasan; con 1 si alguno falla. **Un cambio de
`base/` o de `validadores/` no se da por bueno con un caso en rojo.**

## Qué hay en la carpeta

| Archivo | Qué es |
|---|---|
| [correr.py](correr.py) | El corredor: lee los casos, los ejecuta y da el veredicto. |
| [casos.jsonl](casos.jsonl) | Un caso por línea: qué guardián, con qué entrada, qué se espera. |
| [evals/fixtures/](fixtures/) | Los archivos que algunos casos necesitan (una transcripción inventada). |

## Los tipos de caso

| Tipo | Qué afirma | Guardián |
|---|---|---|
| `commit` | el mensaje malo se atrapa, el bueno pasa | `commits.validar` |
| `codigo-errores` | la captura vacía se atrapa, la manejada pasa | `errores.revisar_texto` |
| `codigo-secretos` | la clave incrustada se atrapa, la del entorno pasa | `secretos.revisar_texto` |
| `transcripcion` | la mediana de las respuestas queda bajo su tope | `brevedad.resumen` |

Cada guardián lleva **su pareja en negativo**: el caso que NO debe detectar.
El falso positivo es lo que hace que un validador se ignore, así que se prueba
con el mismo peso que el acierto.

## Cómo se agrega un caso

Una línea en `casos.jsonl` con `id`, `regla` (el ID que el caso defiende),
`tipo`, la entrada (`texto`, o `fixture` + umbral), y qué se espera. Si el
caso necesita un tipo nuevo, el tipo se agrega en `correr.py` con su guardián
— determinista, como todos (`20·M9`): un caso cuyo veredicto se pueda
discutir no va acá.

## Lo que este banco todavía no mide

El **comportamiento del agente en sesión** —si preguntó antes de tocar, si
reformuló ante la ambigüedad— no se mide con estos casos: exige leer la
transcripción y juzgar. Lo medible de una sesión (cuánto ocupa lo que
contesta, cuánto consume) ya tiene sus números: `validar.py brevedad` y el
enganche de presupuesto. Este banco crece hacia allá caso a caso, siempre que
el veredicto se pueda dar sin opinar.
