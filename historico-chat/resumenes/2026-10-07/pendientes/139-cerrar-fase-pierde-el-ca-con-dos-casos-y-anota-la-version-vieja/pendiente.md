# Pendiente: `cerrar_fase` pierde el CA que tiene dos casos y anota la versión vieja

| | |
|---|---|
| **De dónde sale** | [H-22 de la sesión del 2026-10-06](../../../2026-10-06/sesion.md) |

## El problema

Al cerrar la fase `A-EP-027-HU-004-el-estandar-se-lee-como-pagina`, `manage.py cerrar_fase` escribió el `resultado_pruebas.md` con dos casos de cuatro. La fila de la matriz del plan de pruebas que dice `CA-02 | CP-002, CP-003` no entró: ni el CA-02 ni sus dos casos aparecen en el resultado, y los totales dicen «2 de 2». Además, en «Ambiente y versión» y en «Versión del estándar al cerrar» anota 56.8.0, la del archivo `VERSION` quieto, y no la de la base (57.2.0).

Toca la misma lectura de la matriz que el [pendiente 127](../../../../../documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-016-cerrar-y-reabrir-una-fase-y-separar-los-cambios-por-sesion-son-funcionalidades-de-cimiento/pendientes/127-cerrar-fase-no-dice-que-formato-de-matriz-espera/pendiente.md) (`Fase.casos()`, en `proyectos/cimiento/core/herramientas/fase.py`). Ese pide que el mensaje diga qué formato espera; este, que la fila con varios casos no se pierda.

## Por qué importa

El resultado dice que la fase cumple con menos criterios de los que tiene la HU, y con una versión que no es la que rige. Quien lo lea no sabe que falta un criterio, y la traza entre la HU y sus pruebas queda rota sin que nada avise.
