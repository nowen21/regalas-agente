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

---

## ¿Se puede cerrar la sesión?

Se cierra cuando ningún hallazgo queda sin anotar: cada uno enlaza su pendiente, y su pendiente existe. Anotar es dejar el archivo, no decir «quedó pendiente».

| Para cerrar | Estado |
|---|---|
| Todo hallazgo enlaza su pendiente | ☑ H-1 enlaza el pendiente 132 |
| Todo pendiente enlazado existe | ☑ |
| Lo que se hizo está aprobado y guardado | ☐ El análisis está aprobado y en `592b426`; la construcción de EP-026 sigue abierta |

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

_(Si la sesión no dejó nada, se escribe «nada»: es un dato, no un olvido.)_

<!-- aviso: falta decir si la sesión se puede cerrar -->
