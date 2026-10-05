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

---

## ¿Se puede cerrar la sesión?

Se cierra cuando ningún hallazgo queda sin anotar: cada uno enlaza su pendiente, y su pendiente existe. Anotar es dejar el archivo, no decir «quedó pendiente».

| Para cerrar | Estado |
|---|---|
| Todo hallazgo enlaza su pendiente | ☑ H-2, H-4, H-5, H-6 y H-7 se corrigieron dentro de sus fases |
| Todo pendiente enlazado existe | ☑ |
| Lo que se hizo está aprobado y guardado | ☐ |

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

<!-- aviso: falta decir si la sesión se puede cerrar -->
