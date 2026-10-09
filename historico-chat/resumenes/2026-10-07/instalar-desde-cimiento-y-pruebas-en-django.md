# 2026-10-07 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-10-07-instalar-desde-cimiento-y-pruebas-en-django.md](../../2026-10-07-instalar-desde-cimiento-y-pruebas-en-django.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

| Campo | Valor |
|---|---|
| Viene de | Ninguna sesión anterior: empezó con una pregunta sobre instalar desde Cimiento |

---

## Hallazgos de esta sesión

### H-1 · Cimiento no sabe qué parte del programa de cada proyecto queda sin pruebas, ni lo exige

V2, según el [análisis 1 del pendiente 141](../2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-1.md).

| Campo | Valor |
|---|---|
| Qué pasó | Al preguntar qué sistemas de pruebas sirven en Django, salió que ni Cimiento ni los proyectos que administra miden qué parte de su programa queda sin pruebas, que ninguna prueba usa un navegador real y que la configuración de cada proyecto no exige nada de eso |
| Por qué importa | Cimiento es la línea base de todos los proyectos: un hueco que no se mide no se ve en ninguno, y lo que corre en el navegador se puede dañar sin que falle ninguna prueba |
| Pendiente | [Pendiente 141: Cimiento revisa qué parte de cada proyecto queda sin pruebas y lo exige desde su configuración](../2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/pendiente.md) |

### H-2 · El plan de la EP-029·HU-001 no declara la migración que piden los ajustes nuevos

V2, según el [análisis 2 del pendiente 141](../2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-2.md).

| Campo | Valor |
|---|---|
| Qué pasó | Al ejecutar la fase A de la EP-029·HU-001, Django pidió una migración de `core/proyectos/` que el plan no declaraba: cambiar el catálogo de ajustes cambia las opciones de un campo de la base. El plan no preguntó qué archivos pedía el cambio antes de escribirse |
| Por qué importa | Lo que el plan no declara no se escribe, y la fase se detiene. Le puede pasar a cualquier plan que cambie la base de datos de cualquier proyecto |
| Pendiente | El mismo [pendiente 141](../2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/pendiente.md): se trata en su análisis 2 |

### H-3 · El plan de la EP-029·HU-002 no declara la sección del manual que pide toda pantalla nueva

V2, según el [análisis 3 del pendiente 141](../2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-3.md).

| Campo | Valor |
|---|---|
| Qué pasó | Al ejecutar la fase A de la EP-029·HU-002, la prueba del manual pidió la sección de las pantallas nuevas en `core/ayuda/secciones.py` y su texto. El plan no buscó qué pruebas le exigen piezas a toda pantalla nueva |
| Por qué importa | Lo que el plan no declara no se escribe, y la fase se detiene. Le puede pasar a cualquier plan que cree una pantalla en cualquier proyecto |
| Pendiente | El mismo [pendiente 141](../2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/pendiente.md): se trata en su análisis 3 |

### H-4 · La prueba de la guía de pantallas está en rojo

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-08, al correr `core.estandar` para la EP-029·HU-002, falló `test_cp002_cada_seccion_de_construccion_dice_como_con_tabler`: la sección 13 de `base/17-guia-de-pantallas.md` dice «En Cimiento» y la prueba busca «Cómo con Tabler». No lo causa la EP-029: viene del cambio a AdminLTE de la EP-028·HU-007 |
| Por qué importa | Una prueba en rojo que nadie vio se confunde con un defecto de la próxima fase que la corra |
| Pendiente | [Pendiente 143: la prueba de la guía busca «Cómo con Tabler» y la guía dice «En Cimiento»](../../../documentacion/epicas/EP-028-las-pantallas-orientan-al-usuario-sin-que-conozca-como-esta-armado-el-sistema/HU-002-el-estandar-tiene-su-guia-de-diseno-de-pantallas/pendientes/143-la-prueba-de-la-guia-busca-como-con-tabler-y-la-guia-dice-en-cimiento/pendiente.md) |

### H-5 · El freno detuvo lo que escribió una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-08 22:19, el freno detuvo lo que escribió una orden de consola sobre `proyectos/cimiento/core/herramientas/tests_instalacion.py`: el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8). Esta sesión no tocó ese archivo: lo cambió otra sesión, y el freno se lo cobró a una orden de `git` que solo leía |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | [Pendiente 123: el freno le cobra a una sesión lo que escribe otra](../2026-10-05/pendientes/123-el-freno-le-cobra-a-una-sesion-lo-que-escribe-otra/pendiente.md) |

---

## ¿Se puede cerrar la sesión?

Se cierra cuando ningún hallazgo queda sin anotar: cada uno enlaza su pendiente, y su pendiente existe. Anotar es dejar el archivo, no decir «quedó pendiente».

| Para cerrar | Estado |
|---|---|
| Todo hallazgo enlaza su pendiente | ☑ H-1, H-2 y H-3 al 141; H-4 al 143; H-5 al 123 |
| Todo pendiente enlazado existe | ☑ |
| Lo que se hizo está aprobado y guardado | ☐ Aprobado por los análisis 1 a 3; falta el commit |

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

_(Si la sesión no dejó nada, se escribe «nada»: es un dato, no un olvido.)_

<!-- aviso: falta decir si la sesión se puede cerrar -->
