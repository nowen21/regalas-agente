# Pendiente · Una versión adoptada inventada pasa, y encima apaga el aviso de desfase

**Estado:** abierto, anotado el 2026-08-22.

| | |
|---|---|
| **Historia de usuario** | [EP-002 · HU-003 — Versión adoptada por el proyecto](../documentacion/epicas/EP-002-versionado-y-adopcion/HU-003-version-adoptada-por-el-proyecto/HU-003-version-adoptada-por-el-proyecto.md), cuyo CA-02 quedó en rojo por esto |
| **De dónde sale** | Ejecutar la fase [`A-EP-002-HU-003`](../documentacion/epicas/EP-002-versionado-y-adopcion/HU-003-version-adoptada-por-el-proyecto/A-EP-002-HU-003-retrodocumentar-la-version-adoptada/resultado_pruebas.md), defectos D-01 y D-02 |
| **Proyecto de origen** | El estándar mismo |

## El problema

Son dos, y salieron juntos.

**Primero: la versión declarada no se comprueba contra nada.** Un proyecto puede escribir cualquier número en su `CLAUDE.md` y nadie lo mira. Probado sobre una copia temporal:

```
- **Versión del estándar adoptada:** `99.9.9` · sellada `2026-08-20`

$ python validadores/validar.py version --raiz C:/tmp/prueba-version
OK: sin incumplimientos.
```

**Y lo peor no es que pase: es que apaga la comprobación que sí servía.** Como `99.9.9` es mayor que la vigente, el programa concluye que el proyecto está al día y **deja de avisar del desfase**. Un número inventado hacia adelante no se detecta y además silencia lo único que había.

**Segundo: la versión declarada y el historial de adopciones pueden contradecirse.** El instalador escribe un registro en `documentacion/versiones/` por cada actualización, y nada compara ese registro con lo que el `CLAUDE.md` declara. Caso real, encontrado el 2026-08-22 en shopnest-mesa:

| Dónde | Qué dice | Cuándo |
|---|---|---|
| `documentacion/versiones/2026-08-20-28.0.0.md` | «Desde 2026-08-20 18:35:16 este proyecto usa la versión **28.0.0**» | 2026-08-20 |
| `CLAUDE.md`, línea 41 | «Versión del estándar adoptada: **27.2.0** · sellada 2026-08-20» | el mismo día |

## Por qué importa

El aviso de desfase se calcula sobre la versión declarada. Si esa está mal, **el aviso miente en la dirección que sea**: de más si el número quedó atrás, y de menos —o callado del todo— si quedó adelante.

Y la contradicción del segundo caso lleva dos días en un proyecto real sin que nadie la notara, porque no hay quién mire las dos cosas a la vez.

Es, otra vez, el caso borde del [planteamiento](../prompts/cimiento-planteamiento.md) §8: **una comprobación que da por bueno lo que no revisó enseña a no creerle a ninguna.**

## Qué falta

Dos comprobaciones en [`validadores/version.py`](../validadores/version.py), y las dos son de contar, no de opinar:

1. **Que la versión declarada exista en el `CHANGELOG.md` del estándar.** Si no está, es una falla: alguien escribió un número que nadie publicó.
2. **Que la versión declarada coincida con el último registro de `documentacion/versiones/`.** Si difieren, es una falla y se nombran las dos, porque una de las dos está mal y no se sabe cuál sin mirar.

**Y el orden importa:** la primera hay que hacerla antes que la segunda, porque mientras un número inventado apague el aviso, cualquier proyecto puede quedar en silencio sin que se note.

## El límite

No decide qué hacer cuando las dos difieren: eso es del usuario, y lo que se pide es que se vea.

No toca el instalador. Si resulta que el instalador escribe el registro y no actualiza la declaración, eso es otro pendiente y sale de comprobarlo.

## Cómo se sabrá que cerró

Una copia temporal con `99.9.9` declarada **falla**, diciendo que esa versión no existe en el registro de cambios. Otra copia que declare una versión real distinta de su último registro de adopción **falla**, nombrando las dos. Y un proyecto bien declarado sigue dando lo mismo que hoy: el aviso de desfase, y nada más.
