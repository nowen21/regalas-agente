# 2026-10-06 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-10-06-sesion.md](../../2026-10-06-sesion.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

| Campo | Valor |
|---|---|
| Viene de | «...» |

---

## Hallazgos de esta sesión

### H-1 · Lo que se guarda en la pantalla de Cimiento no tiene la historia de los archivos, y el estándar no se administra desde ella

| Campo | Valor |
|---|---|
| Qué pasó | Al preguntar si `recuperar.py` se puede manejar por pantalla, salió que la base guarda los cambios de tres maneras distintas y que los ajustes no dejan rastro. El usuario pidió que la pantalla sea el estándar y que todo cambio guardado ahí tenga la historia de los archivos. Eso deroga la decisión del 2026-08-18 y la restricción de EP-016: la fuente de las reglas es el texto |
| Por qué importa | Un cambio sin historia no se puede revisar ni deshacer, y con dos fuentes del estándar una se queda vieja |
| Pendiente | [Pendiente 132: el estándar vive en la base de Cimiento y cada cambio queda versionado](pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/pendiente.md) |

### H-2 · El freno detuvo una edición fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-06 13:09, el freno detuvo una edición sobre `base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md`: no hay una fase en curso y ninguna regla autoriza escribirlo (02·F8). Era el arreglo de un defecto de la fase A de EP-001·HU-041: los totales del sello quedaron con comas y el validador no los leía |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | No hace falta: lo resolvió la fase `B-EP-001-HU-041-los-totales-del-sello-se-leen`, dentro del alcance aprobado del análisis 1 del pendiente 132 |

### H-3 · El freno detuvo lo que escribió una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-06 13:10, el freno detuvo lo que escribió una orden de consola sobre `base/01-conducta.md`: no hay una fase en curso y ninguna regla autoriza escribirlo (02·F8). Es el mismo arreglo de H-2, en el sello de `C19` |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | No hace falta: lo resolvió la fase `B-EP-001-HU-041-los-totales-del-sello-se-leen` |

### H-4 · El freno detuvo lo que escribió una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-06 13:18, el freno detuvo lo que escribió una orden de consola sobre `base/01-conducta/palabras-clave.md`: el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8). Esta sesión no tocó ese archivo: lo cambió la sesión que construye «Respondo» (EP-001·HU-036, fase B), y el freno se lo cobra a esta en cada orden de consola |
| Por qué importa | Mientras el cambio ajeno siga sin guardar, cada orden de consola de esta sesión se detiene y suma otro hallazgo |
| Pendiente | [Pendiente 123: el freno le cobra a una sesión lo que escribe otra](../2026-10-05/pendientes/123-el-freno-le-cobra-a-una-sesion-lo-que-escribe-otra/pendiente.md) |

### H-5 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-06 13:42, el freno detuvo una orden de consola sobre `proyectos/cimiento/de`: el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8). No existe esa ruta: el freno tomó la palabra «de» del texto que la orden `sed` escribía dentro de un archivo del plan |
| Por qué importa | Detiene una orden legítima por un texto que no es una ruta |
| Pendiente | [Pendiente 113: el freno toma texto de los comandos como rutas](../2026-10-04/pendientes/113-el-freno-toma-texto-de-los-comandos-como-rutas/pendiente.md) |

### H-6 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-06 14:01, el freno detuvo una orden de consola sobre `/c/Ing. Jose/ia/cimiento-copias/cimiento-2026-10-06.sql`: queda fuera del proyecto (04·S9). El agente quiso borrar a mano la primera copia, sin comprimir; el freno hizo bien en detenerlo |
| Por qué importa | El agente no escribe ni borra fuera del proyecto; en la carpeta de copias solo trabaja el programa de la copia, que es la ruta autorizada (acuerdo 23) |
| Pendiente | No hace falta: la poda de la copia quita la copia sin comprimir, y así se hizo (fase `A-EP-026-HU-010-la-copia-diaria`) |

### H-7 · El freno detuvo una escritura fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-06 17:44, el freno detuvo una escritura sobre `proyectos/cimiento/core/estandar/en_base.py`: el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8). El agente escribió código de la HU-004 antes de abrir su fase y su plan; la fase en curso era la cerrada de la HU-003 |
| Por qué importa | El código antes del plan salta la cadena (`02·F0`); el freno lo detuvo como debía |
| Pendiente | No hace falta: se escribió la HU-004, se abrió su fase con el archivo en el plan y se volvió a escribir |

### H-8 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-06 18:11, el freno detuvo una orden de consola sobre `proyectos/cimiento/core/estandar/templates/estandar/_mensajes.html`: el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8). Era una plantilla pequeña de mensajes que el plan de la fase A de la HU-005 no nombraba |
| Por qué importa | El plan tiene que nombrar todo archivo antes de escribirlo |
| Pendiente | No hace falta: se sumó al plan de la fase, dentro del alcance de la HU-005, y la orden se volvió a correr |

### H-9 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-06 20:14, el freno detuvo una orden de consola sobre una orden: corre en segundo plano y deja su salida fuera del proyecto (04·S9). El agente quiso correr la regresión de la HU-006 en segundo plano, primero con la salida a la carpeta temporal y después sin ella |
| Por qué importa | En segundo plano la herramienta guarda la salida fuera del proyecto |
| Pendiente | No hace falta: la regresión se corrió en primer plano |

### H-10 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-06 20:14, el freno detuvo la segunda forma de la misma orden de H-9 |
| Por qué importa | El mismo de H-9 |
| Pendiente | No hace falta: lo resuelve lo mismo que H-9 |

### H-11 · Pasar los opt-in a la base apagaba los capítulos que el `CLAUDE.md` no nombra

| Campo | Valor |
|---|---|
| Qué pasó | Al migrar la base real en la HU-009, el estándar mismo quedó con los siete capítulos opt-in apagados: su `CLAUDE.md` no los nombra, y antes eso significaba que regían |
| Por qué importa | El día del paso habrían dejado de llegar reglas sin que nadie lo decidiera |
| Pendiente | No hace falta: se corrigió en la misma fase. Lo que el `CLAUDE.md` no nombra pasa en «sí» (señal S-343) |

### H-12 · Las reglas del estándar se guardan como texto entero, y la pantalla no puede mostrarlas por su nombre ni relacionarlas

| Campo | Valor |
|---|---|
| Qué pasó | La pantalla «Estándar» lista los documentos por la ruta del `.md`. Al analizarlo salió que la causa es más honda: cada regla se guarda como un texto entero, sin casillas, y de ahí no se sacan su nombre, sus relaciones ni sus tareas sin leer el texto |
| Por qué importa | Quien administra el estándar no reconoce las reglas ni puede seguir sus relaciones, y cada pantalla o programa que necesita una parte de la regla tiene que buscarla dentro del texto |
| Pendiente | [136](pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/pendiente.md); el usuario pidió abrir su análisis |

### H-13 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-07 08:23, el freno detuvo una orden de consola sobre `documentacion/epicas/EP-027-las-reglas-del-estandar-viven-en-tablas-con-la-estructura-del-molde/HU-007-las-reglas-m5-y-m9-dicen-que-la-regla-vive-en-casillas/sección`: el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8). La «ruta» era la palabra «sección» del texto que se reemplazaba |
| Por qué importa | El freno detiene lo que sí está en el plan cuando lee texto como ruta |
| Pendiente | No hace falta uno nuevo: es el caso del [pendiente 113](../2026-10-04/pendientes/113-el-freno-toma-texto-de-los-comandos-como-rutas/pendiente.md), el freno toma texto de los comandos como rutas |

### H-14 · Las pantallas no orientan al usuario, y el estándar no tiene guía ni regla que lo exija

| Campo | Valor |
|---|---|
| Qué pasó | Al ir a aprobar las propuestas de la EP-027·HU-007, el usuario no encontró el camino. El análisis mostró que pasa en todo Cimiento y que el estándar no tiene una guía de diseño de pantallas ni una regla obligatoria que exija que la pantalla oriente sola |
| Por qué importa | Cimiento es la línea base de los demás proyectos: si no orienta a su usuario, no puede exigírselo a los demás |
| Pendiente | [137](../2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/pendiente.md), con la regla que lo exija y una guía de diseño de pantallas |

### H-15 · El usuario tuvo que avisar en el chat que ya había aprobado las propuestas

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-07 el usuario aprobó en la pantalla las propuestas 1 a 6, y el agente no se enteró hasta que se lo dijo en el chat |
| Por qué importa | La pantalla es donde se autoriza todo; repetirlo en el chat duplica cada aprobación y detiene el trabajo |
| Pendiente | [138](../2026-10-07/pendientes/138-el-agente-no-se-entera-de-lo-que-se-aprueba-en-la-pantalla/pendiente.md) |

### H-16 · El freno detuvo una escritura fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-07 11:43, el freno detuvo una escritura sobre `historico-chat/scripts/2026-10-07/cierre_ep028_hu001.py`: es un guion para cerrar o reabrir una fase, que Cimiento ya hace: se usa `manage.py cerrar_fase «fase» (o reabrir_fase)`, como acordó el análisis 2 del pendiente 119 (04·S18). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | No hace falta: el agente llenó las marcas del cierre con el editor, que es lo que corresponde; el guion sobraba |

### H-17 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-07 11:43, el freno detuvo una orden de consola sobre `proyectos/cimiento/$F/estado-fase.md`: el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | No hace falta uno nuevo: es el caso del [pendiente 113](../2026-10-04/pendientes/113-el-freno-toma-texto-de-los-comandos-como-rutas/pendiente.md); el freno no reconoce una variable del comando como la ruta que nombra |

### H-18 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-07 11:48, el freno detuvo una orden de consola sobre `$(ls -d documentacion/epicas/EP-028-*/HU-002-*/A-EP-028-HU-002-la-guia)/propuestas`: el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | No hace falta uno nuevo: es el caso del [pendiente 113](../2026-10-04/pendientes/113-el-freno-toma-texto-de-los-comandos-como-rutas/pendiente.md); el freno no reconoce una ruta escrita con una variable |

### H-19 · El freno detuvo una escritura fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-07 11:50, el freno detuvo una escritura sobre `documentacion/epicas/EP-028-las-pantallas-orientan-al-usuario-sin-que-conozca-como-esta-armado-el-sistema/HU-002-el-estandar-tiene-su-guia-de-diseno-de-pantallas/A-EP-028-HU-002-la-guia/propuestas/guia-de-pantallas.txt`: el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | No hace falta: el plan de la fase no traía la versión en su línea de aprobación, y sin ella el freno no lo da por aprobado. Se agregó («con la versión 57.0.0») y la escritura pasó |

### H-20 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-07 13:49, el freno detuvo una orden de consola sobre `$F`: no hay una fase en curso y ninguna regla autoriza escribirlo (02·F8). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | [113](../2026-10-04/pendientes/113-el-freno-toma-texto-de-los-comandos-como-rutas/pendiente.md): el freno tomó una variable de la terminal como ruta. El cambio se hizo con el editor |

### H-21 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-07 14:00, el freno detuvo una orden de consola sobre `C:/Users/user/AppData/Local/Temp/claude/c--Ing--Jose-ia-agente/dad10286-79ce-4758-a237-c9cfbabca21d/scratchpad/ids.py`: queda fuera del proyecto (04·S9). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | Ninguno: el freno acertó. El agente puso un guion de apoyo fuera del repositorio, contra `04·S18`; el cambio se hizo con el editor |

### H-22 · `cerrar_fase` dejó fuera un criterio y anotó la versión vieja

| Campo | Valor |
|---|---|
| Qué pasó | Al cerrar la fase `A-EP-027-HU-004-el-estandar-se-lee-como-pagina`, el resultado de pruebas salió sin el CA-02, cuya fila de la matriz tiene dos casos, y con la versión 56.8.0 del archivo quieto. Se corrigió a mano |
| Por qué importa | El resultado dice que la fase cumple con menos criterios de los que tiene la HU |
| Pendiente | [139](../2026-10-07/pendientes/139-cerrar-fase-pierde-el-ca-con-dos-casos-y-anota-la-version-vieja/pendiente.md) |

### H-23 · El freno detuvo una escritura fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-07 14:33, el freno detuvo una escritura sobre `proyectos/cimiento/core/estandar/molde.py`: no hay una fase en curso y ninguna regla autoriza escribirlo (02·F8). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | Ninguno: el freno acertó. El agente escribió código antes de abrir la fase; se abrió la fase `A-EP-027-HU-001-las-casillas` con su plan y el archivo se escribió después |

### H-24 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-07 14:41, el freno detuvo una orden de consola sobre `proyectos/cimiento/270)/self.assertGreaterEqual(vistas,`: el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | [113](../2026-10-04/pendientes/113-el-freno-toma-texto-de-los-comandos-como-rutas/pendiente.md): el freno tomó el texto de un `sed` como ruta. El cambio se hizo con el editor |

### H-25 · La regla opt-in de un capítulo que no es opt-in ya no se puede apagar

| Campo | Valor |
|---|---|
| Qué pasó | Al correr la regresión de `core.enganches` en la fase `A-EP-027-HU-002-el-paso`, falla `test_la_opt_in_apagada_no_autoriza_y_la_encendida_si`. Desde `041984a` (EP-026·HU-009), los opt-in se filtran a los capítulos 15, 16, 18, 19, 21 y 22, y `13·DOC5`, opt-in dentro del capítulo 13, ya no se apaga |
| Por qué importa | Una regla opcional rige para todos, y una prueba en rojo pasó sin que nadie la viera |
| Pendiente | [140](../2026-10-07/pendientes/140-la-regla-opt-in-de-un-capitulo-que-no-es-opt-in-no-se-apaga/pendiente.md) |

### H-26 · AgroSystem tiene dos reglas con el código P45

| Campo | Valor |
|---|---|
| Qué pasó | Al probar el paso de las reglas de los proyectos (EP-027·HU-006, fase B) contra los archivos reales, AgroSystem trae dos reglas distintas con el código P45: «La última fase de una HU consolida TODO el entregable» (renglón 991) y «HU con múltiples fases muestra historial» (renglón 1010) |
| Por qué importa | En la tabla el código no se repite (`20·M4`): pasar el archivo así perdería una de las dos. El paso se niega, lo dice y deja el archivo como está |
| Pendiente | Ninguno en este repositorio: renumerar una regla de AgroSystem lo decide el usuario |

### H-27 · El freno detuvo lo que escribió una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-07 21:24, el freno detuvo lo que escribió una orden de consola sobre `proyectos/cimiento/package-lock.json`: el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | Por crear: lo decide el análisis siguiente del pendiente de la fase |

### H-28 · El freno detuvo lo que escribió una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-07 21:24, el freno detuvo lo que escribió una orden de consola sobre `proyectos/cimiento/package.json`: el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | Por crear: lo decide el análisis siguiente del pendiente de la fase |

### H-29 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-07 21:49, el freno detuvo una orden de consola sobre `proyectos/cimiento/3`: el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | Por crear: lo decide el análisis siguiente del pendiente de la fase |

### H-30 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-07 22:01, el freno detuvo una orden de consola sobre `proyectos/cimiento/$P`: el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | Por crear: lo decide el análisis siguiente del pendiente de la fase |

---

## ¿Se puede cerrar la sesión?

Se cierra cuando ningún hallazgo queda sin anotar: cada uno enlaza su pendiente, y su pendiente existe. Anotar es dejar el archivo, no decir «quedó pendiente».

| Para cerrar | Estado |
|---|---|
| Todo hallazgo enlaza su pendiente | ☑ H-1 enlaza el pendiente 132 |
| Todo pendiente enlazado existe | ☑ |
| Todo hallazgo enlaza su pendiente, o se resolvió en su fase | ☑ H-11 se corrigió en la HU-009 |
| Lo que se hizo está aprobado y guardado | ☑ El análisis está en `592b426`; la EP-026 terminada, en `9ae058e` y `041984a`. El push de `041984a` quedó sin hacer: la herramienta no lo dejó correr |

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

_(Si la sesión no dejó nada, se escribe «nada»: es un dato, no un olvido.)_

<!-- aviso: falta decir si la sesión se puede cerrar -->
