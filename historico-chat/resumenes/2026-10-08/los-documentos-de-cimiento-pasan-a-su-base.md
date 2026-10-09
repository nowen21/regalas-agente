# 2026-10-08 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-10-08-los-documentos-de-cimiento-pasan-a-su-base.md](../../2026-10-08-los-documentos-de-cimiento-pasan-a-su-base.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

| Campo | Valor |
|---|---|
| Viene de | «...» |

---

## Hallazgos de esta sesión

### H-1 · Los documentos de Cimiento pasan a la base y dejan de ser archivos .md

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-08, al analizar si los .md gastan más que la base, el usuario señaló que cada operación termina en un guion nuevo (hay 250 en `historico-chat/scripts/`) aunque la estructura podría estar en la base. La base no tiene tablas para épicas, HU, análisis, pendientes ni planes. El usuario decidió que todos los .md de Cimiento pasan a la base y ninguno queda como archivo; los .py siguen siendo archivos porque son el programa de Cimiento |
| Por qué importa | Sin tabla ni comando fijo, cada operación se resuelve con un guion de un solo uso; con el .md y la base a la vez, una de las dos copias se queda vieja |
| Pendiente | [Pendiente 142: los documentos de Cimiento viven en su base, con un comando fijo por cada tipo](pendientes/142-los-documentos-de-cimiento-viven-en-la-base/pendiente.md) |

### H-2 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-08 21:01, el freno detuvo una orden de consola sobre `/tmp/idx.md`: queda fuera del proyecto (04·S9). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | No hace falta: el archivo temporal no era necesario; el commit se hizo sin `historico-chat/README.md`, cuya línea entra en el commit siguiente |

### H-3 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-08 21:25, el freno detuvo una orden de consola sobre `$TEMP/ve.txt`: queda fuera del proyecto (04·S9). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | No hace falta: el archivo temporal no era necesario; la consulta se repitió sin él |


### H-4 · La consulta de las reglas falla porque el aviso manda a usar el Python que no tiene el conector de MySQL

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-08, `python manage.py ver_estandar base/01-conducta/palabras-clave.md` terminó con `ModuleNotFoundError: No module named 'MySQLdb'`. El `python` del sistema (3.11, y también 3.13 y 3.14) no tiene el conector; el de Cimiento, `proyectos/cimiento/.venv/Scripts/python.exe`, sí lo tiene y con él la consulta funciona. El aviso de cada sesión manda a usar `python` (`proyectos/cimiento/core/enganches/cargador.py:68`). Además, con el Python de Cimiento las tildes salen dañadas en la consola de Windows |
| Por qué importa | Toda sesión, en cualquier proyecto, recibe la orden de leer las reglas con un comando que falla; sin leerlas, trabaja sin las reglas completas |
| Pendiente | [Pendiente 145: `manage.py` se abre siempre con el Python de Cimiento y escribe bien las tildes](pendientes/145-manage-py-usa-el-python-de-cimiento/pendiente.md) |

### H-5 · El freno detuvo una edición fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-08 22:04, el freno detuvo una edición sobre `proyectos/cimiento/manage.py`: el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8). El plan sí lo declara; no cuenta como aprobado porque el análisis 1 del pendiente 145 no nombra la HU en «Lo que se tiene que hacer» (dice «la HU de EP-026 que salga de este análisis» en vez de EP-026·HU-011), y además a la aprobación del plan le faltaba la versión, que ya se corrigió |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | El mismo pendiente 145: se trata en su análisis 2 |

### H-6 · El freno detuvo lo que escribió una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-08 22:17, el freno detuvo lo que escribió una orden de consola sobre `proyectos/cimiento/core/comun/enganches.py`: el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | No hace falta: el cambio lo escribió otra sesión, que trabaja la EP-029, a las 22:17; esta sesión no tocó el archivo |

### H-7 · El freno detuvo lo que escribió una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-08 22:29, el freno detuvo lo que escribió una orden de consola sobre `.githooks/pre-commit`: no hay una fase en curso y ninguna regla autoriza escribirlo (02·F8). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | No hace falta: el cambio es de la EP-029·HU-003, que trabaja otra sesión; esta sesión no tocó el archivo |

### H-8 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-08 23:52, el freno detuvo una orden de consola sobre una orden: corre en segundo plano y deja su salida fuera del proyecto (04·S9). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | Por crear: lo decide el análisis siguiente del pendiente de la fase |

---

## ¿Se puede cerrar la sesión?

Se cierra cuando ningún hallazgo queda sin anotar: cada uno enlaza su pendiente, y su pendiente existe. Anotar es dejar el archivo, no decir «quedó pendiente».

| Para cerrar | Estado |
|---|---|
| Todo hallazgo enlaza su pendiente | ☑ |
| Todo pendiente enlazado existe | ☑ |
| Lo que se hizo está aprobado y guardado | ☐ |

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

_(Si la sesión no dejó nada, se escribe «nada»: es un dato, no un olvido.)_

<!-- aviso: falta decir si la sesión se puede cerrar -->
