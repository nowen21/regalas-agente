# Pendiente: la regla opt-in de un capítulo que no es opt-in ya no se puede apagar

| | |
|---|---|
| **De dónde sale** | [H-25 de la sesión del 2026-10-06](../../../2026-10-06/sesion.md) |

## El problema

`13·DOC5` es una regla marcada *opt-in* dentro del capítulo 13, que no es opt-in. Desde el commit `041984a` (EP-026·HU-009), `opt_in_apagados` (`proyectos/cimiento/core/herramientas/recuperar.py`) solo reconoce los capítulos de `CAPITULOS_OPT_IN` (`core/proyectos/ajustes.py`): 15, 16, 18, 19, 21 y 22. Una línea «Patrón opt-in `13`: no» en el `CLAUDE.md` de un proyecto ya no apaga `DOC5`, y la base no tiene un ajuste para hacerlo.

Lo detecta la prueba `test_la_opt_in_apagada_no_autoriza_y_la_encendida_si` (`core/enganches/tests_freno.py`), que falla desde ese commit.

## Por qué importa

Una regla que el molde declara opcional (`20·M5`) rige para todos los proyectos sin que ninguno la pueda apagar. Y la suite de `core.enganches` tiene una prueba en rojo que nadie vio, porque la fase que hizo el cambio no corrió esa suite.
