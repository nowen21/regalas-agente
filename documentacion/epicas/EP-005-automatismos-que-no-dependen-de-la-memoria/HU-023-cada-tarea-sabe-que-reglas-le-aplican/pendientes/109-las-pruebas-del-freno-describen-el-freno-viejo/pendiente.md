# Pendiente: las pruebas del freno describen el freno viejo

| | |
|---|---|
| **De dónde sale** | [H-15 de la sesión del 2026-10-01](../../../../../../historico-chat/resumenes/2026-10-01/sesion.md) |

## El problema

Tres pruebas de `validadores/tests/test_las_reglas_llegan_antes_de_actuar.py`, escritas en esta HU cuando el freno solo cuidaba que nada se escribiera fuera del proyecto, fallan desde el 2026-10-03:

- `test_el_instalador_solo_pone_el_freno_de_escritura` exige que `hook_antes.py` corra solo con la herramienta de escritura.
- `test_escribir_fuera_del_proyecto_se_detiene` y `test_la_carpeta_hermana_con_el_mismo_comienzo_es_afuera` esperan el mensaje «FUERA DEL PROYECTO».

La fase `B` de la HU-007 de EP-023 cambió ese freno: ahora corre antes de toda acción, compara con el plan de la fase en curso y su mensaje es otro.

## Por qué importa

Las pruebas describen un comportamiento que ya no existe: fallan aunque el freno funcione, y quien las lea entiende mal qué hace hoy.
