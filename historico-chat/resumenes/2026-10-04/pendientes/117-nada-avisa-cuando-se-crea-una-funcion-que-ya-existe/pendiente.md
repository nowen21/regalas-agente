# Pendiente: nada avisa cuando se crea una función que ya existe

| | |
|---|---|
| **De dónde sale** | El inventario de los `.py` de Cimiento, en la [sesión del 2026-10-04](../../../../2026-10-04-optimizar-el-codigo-de-cimiento.md), y el [pendiente: el código de Cimiento se repite en vez de reusarse](../116-el-codigo-de-cimiento-se-repite-en-vez-de-reusarse/pendiente.md) |

## El problema

[`07·Q4`](../../../../../base/07-calidad-de-codigo.md#q4--no-repitas-dry-pero-no-abstraigas-de-más) pide no repetir lógica, pero ningún validador lo comprueba. Al crear una función nadie revisa si ya existe en otro archivo, y así se acumularon las copias: `_leer` en 13 archivos, `raiz_pedida` en 10, `dicho` en 9, `_entrada` en 8, `_git` en 6.

## Por qué importa

Si solo se juntan las copias de hoy, las nuevas siguen apareciendo, porque la causa sigue igual. Los proyectos que heredan el estándar tampoco tienen con qué comprobar `07·Q4` en su propio código.
