# 2026-10-04 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-10-04-sesion-3.md](../../2026-10-04-sesion-3.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

| Campo | Valor |
|---|---|
| Viene de | «Continúe con el pendiente 119»: construir la épica `EP-025` que salió del análisis 1, aprobado el 2026-10-04 |

---

## Hallazgos de esta sesión

### H-1 · El freno repitió su aviso unas 1700 veces en una sola acción

| Campo | Valor |
|---|---|
| Qué pasó | `npm install` en `proyectos/cimiento/` creó `node_modules/` antes de que estuviera en `.gitignore`, y el freno devolvió un bloque igual por cada archivo creado |
| Por qué importa | Del orden de 380 000 tokens en un turno, releídos en cada llamada siguiente |
| Pendiente | [Pendiente 120: el freno repite el mismo aviso por cada archivo](pendientes/120-el-freno-repite-el-aviso-por-cada-archivo/pendiente.md) |

### H-2 · En Windows, Django no sirve las carpetas de estáticos con prefijo

| Campo | Valor |
|---|---|
| Qué pasó | El plan de la fase A de `EP-025·HU-001` ponía cada carpeta `dist` de npm con prefijo en `STATICFILES_DIRS`. Django 5.2 compara el prefijo con `\` y la URL llega con `/`: los archivos daban 404 |
| Por qué importa | Las pantallas cargaban sin estilos y el `check` de Django no lo decía |
| Lo corregido | Dentro de los archivos del plan: las carpetas van sin prefijo y una prueba pide los estáticos a la vista que los sirve. Señal S-299 |

### H-3 · Las pruebas del instalador de Cimiento no cargan solas

| Campo | Valor |
|---|---|
| Qué pasó | Un cambio sin guardar de otra sesión en `core/validadores/__init__.py` cerró un ciclo de importación entre el instalador, los validadores y el arranque de sesión. `tests_instalacion` falla al importar |
| Por qué importa | Las pruebas del instalador no corren; esta fase tuvo que correr las suyas importando `core.validadores` primero |
| Pendiente | [Pendiente 121: importar el instalador de Cimiento cae en un ciclo](pendientes/121-importar-el-instalador-de-cimiento-cae-en-un-ciclo/pendiente.md) |

### H-4 · El MariaDB de WAMP crea las tablas con MyISAM

| Campo | Valor |
|---|---|
| Qué pasó | Al probar la HU-002, los grupos desaparecían entre casos. El motor por defecto era MyISAM: sin transacciones ni llaves foráneas, y Django vaciaba la base entre pruebas |
| Por qué importa | Una escritura a medias quedaba a medias en toda la base de Cimiento |
| Lo corregido | En la fase de la HU-001 (ciclo 2): la conexión fija InnoDB y `preparar_base` convierte lo que esté en otro motor. La base local se rehízo con las migraciones de Django; no tenía cuentas. Señal S-300 |

### H-5 · La suma del consumo contaba cada llamada unas tres veces

| Campo | Valor |
|---|---|
| Qué pasó | Claude Code parte una llamada en varias líneas del `.jsonl`, cada una con el mismo `usage`. `hook_presupuesto.py` sumaba por línea: en la sesión `c3d82767`, 619 líneas para 208 llamadas, 3,79 millones de tokens donde había 1,15 millones |
| Por qué importa | El aviso por tramo (`EP-005·HU-014`) salía unas tres veces antes de tiempo, y la medición del H-1 de la sesión 2 (1012 llamadas) pudo contar líneas |
| Lo corregido | En `EP-025·HU-006`, que declara `hook_presupuesto.py`: el lector nuevo cuenta una vez cada llamada, por su `message.id` |

### H-6 · El registro de proyectos ya existía, con 13 proyectos, y la HU-003 creó otro con el mismo nombre

| Campo | Valor |
|---|---|
| Qué pasó | La base `cimiento` ya tenía la tabla `proyectos_proyecto` de la plataforma vieja (`interfaz/`, aplicación `cimiento.proyectos`, migración del 2026-08-22), con 13 proyectos reales, y el instalador sigue anotando ahí (`interfaz/manage.py registrar`). El módulo nuevo `core/proyectos/` usa la misma etiqueta, `proyectos`: Django dio su migración por aplicada y no creó la tabla nueva. Las pruebas pasaron porque corren en una base nueva; `leer_consumo` falló contra la base real con «Unknown column carpeta_claude» |
| Por qué importa | Las pantallas de proyectos de la HU-003 fallan contra la base real; las tablas de niveles y consumo apuntan a la tabla vieja; y hay dos registros de proyectos. El análisis 1 del pendiente 119 dijo que el registro no existía («la épica EP-008 se retiró en el análisis 116») |
| Lo corregido | Por orden del usuario del 2026-10-05, en el ciclo 2 de la fase de la HU-003: la base se respaldó en `cimiento_respaldo_20261005`, se borró y se creó con las migraciones; la `0002` trajo los 12 proyectos de `plantillas/proyectos.md` cuya carpeta existe (`plataforma` ya no existe), y el instalador registra con `proyectos/cimiento/manage.py registrar`. Las HU-003, 004 y 006 quedaron terminadas. Señal S-302 |

### H-7 · El lector no contaba ni nombraba bien los enganches de cada mensaje

| Campo | Valor |
|---|---|
| Qué pasó | Al probar el aviso por límite (`EP-025·HU-009`) con la sesión real, el aviso decía «UserPromptSubmit» en vez del nombre del enganche, y el de las señales no aparecía |
| Por qué importa | El gasto por enganche, que es lo que muestra qué automatizar, se veía incompleto: faltaban 1973 enganches (de 3850 a 5823) |
| Lo corregido | En `lector.py`, dentro de la fase de la HU-009: el texto plano de un enganche en `UserPromptSubmit` y `SessionStart` cuenta, y un contexto sin `hook_success` al lado se nombra por su título entre corchetes. Los enganches guardados se volvieron a leer |

### H-8 · El freno bloqueó una ruta que el análisis prendido permitía

| Campo | Valor |
|---|---|
| Qué pasó | La fila 4 del análisis 3 del pendiente 119 nombra `andamio.py` y `tests_andamio.py` «de una y sin fase». El freno dejó cambiar el primero y bloqueó dos veces crear el segundo, aunque `Freno.rutas_de_una` lo devolvía como permitido. Con «Corrija» entró, y con «Corrija» activo ya no se pudo reproducir. Aparte, al revisar un comando de Bash, el freno resuelve las rutas relativas contra la carpeta de trabajo de la sesión y no tiene en cuenta el `cd` del comando. Al construir la HU-016 bloqueó tres comandos de Bash por palabras que no son rutas: una variable (`$H`), la palabra «los» dentro de una expresión de `sed` y un archivo de un `for`; con Edit pasaron, porque las rutas sí estaban declaradas |
| Por qué importa | El freno deja sin salida justo lo que el análisis aprobado manda hacer, y empuja a tocar archivos a mano (lo que trata el análisis 3) |
| Estado | Causa encontrada el 2026-10-05 al construir la HU-023: `Freno.de_una()` y `Freno.analisis_prendido()` crean `AnalisisEnCurso(raiz)` sin la sesión, así que leen solo el archivo único `historico-chat/.estado/analisis-en-curso.txt`, que apunta al análisis 1 del pendiente 116 de otra sesión. El estado de esta sesión vivía en `analisis-en-curso/<sesión>.txt` y el freno no lo miraba: `andamio.py` pasó porque lo nombra el análisis del 116, y `tests_andamio.py` no. Corregido el 2026-10-05 en la HU-024 de EP-025 (fila 11 del análisis 3 del pendiente 119): el freno lee el análisis de su propia sesión y sigue el `cd` de una orden |

### H-9 · Cambiar la consulta del freno antes de migrar lo deja sin base

| Campo | Valor |
|---|---|
| Qué pasó | Al construir la HU-013 de EP-025, `NivelesDelProyecto.todos()` pasó a leer también la tabla de suspensiones. El freno usa ese código en vivo, y la tabla todavía no existía en la base real: el freno respondió «sin base» y detuvo toda escritura. Se destrabó aplicando la migración, que era un paso del mismo plan |
| Por qué importa | Cimiento se corrige con el mismo freno que lo vigila: un cambio de su esquema tiene que llegar a la base antes que el código que lo lee, o el freno se bloquea a sí mismo. Le pasa a cualquier fase que toque lo que el freno consulta |
| Estado | Se resolvió en la fase. Para que no se repita, el aviso de base sin preparar ya dice qué correr (`manage.py preparar_base`, que aplica las migraciones) |

### H-10 · El freno partió una orden por líneas antes de mirar las comillas

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-05 18:30, el freno detuvo una orden `cd … && python -c "…"` como si escribiera en `proyectos/cimiento/0),`. La HU-024 de EP-025 hizo que, cuando una orden trae `cd`, el freno la parta por `&&`, `;` y saltos de línea antes de saber qué va entre comillas: un `v>0` dentro del código Python entre comillas le pareció una redirección |
| Por qué importa | El freno detiene órdenes legítimas, que es lo que la HU-024 venía a quitar |
| Estado | Corregido el 2026-10-05: se reabrió la fase de la HU-024 con `reabrir_fase`, la orden se parte solo por lo que queda fuera de las comillas, con su prueba, y se cerró otra vez con `cerrar_fase` |

### H-11 · El freno le cobra a esta sesión lo que otra escribe al mismo tiempo

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-05 entre las 18:56 y las 18:58, otra sesión editaba `base/00-identidad-y-rol/marcadores-de-ia.md`, la regla `ID8`, los pendientes 91 y 92, seis de `pendientes/hecho/`, cuatro de `validadores/` y dos de `plantillas/`. Esta sesión corrió dos órdenes de consola que no escriben ahí (`cerrar_fase` y una lectura con `ls` y `grep`). Después de cada orden, el freno compara lo que cambió en el repositorio con el plan, le atribuyó a esta sesión los 17 archivos de la otra y escribió acá 17 hallazgos iguales (se cambiaron por este) |
| Por qué importa | Con dos sesiones abiertas, cada orden de consola de una llena de hallazgos falsos el resumen de la otra y el aviso pide detener la ejecución por trabajo ajeno. Es el mismo caso de las sesiones paralelas que `cambios_por_sesion` resuelve para el commit, pero el freno no lo usa |
| Pendiente | [Pendiente 123: el freno le cobra a una sesión lo que escribe otra](../2026-10-05/pendientes/123-el-freno-le-cobra-a-una-sesion-lo-que-escribe-otra/pendiente.md) |

### H-12 · El agente quiso guardar una salida fuera del repositorio

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-05 19:32, al preparar el commit, el agente mandó la salida de `cambios_por_sesion` a un archivo de la carpeta temporal de la herramienta. El freno lo detuvo: queda fuera del proyecto (04·S9) |
| Por qué importa | Lo que se guarda fuera del repositorio se pierde (`04·S9`) |
| Estado | El freno acertó y no hay nada que corregir en el estándar: la salida se leyó directo en la consola |

---

## ¿Se puede cerrar la sesión?

Se cierra cuando ningún hallazgo queda sin anotar: cada uno enlaza su pendiente, y su pendiente existe. Anotar es dejar el archivo, no decir «quedó pendiente».

| Para cerrar | Estado |
|---|---|
| Todo hallazgo enlaza su pendiente | ☑ H-1, H-3 y H-11 enlazan los pendientes 120, 121 y 123; H-2 y H-4 a H-10 se corrigieron dentro de sus fases; H-12 no deja nada que corregir |
| Todo pendiente enlazado existe | ☑ |
| Lo que se hizo está aprobado y guardado | ☑ Commit `eda8871`, del 2026-10-05 |

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

<!-- aviso: falta decir si la sesión se puede cerrar -->
