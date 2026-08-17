# 2026-08-16 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-16-que-pendiente-sigue.md](../../2026-08-16-que-pendiente-sigue.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

**Viene de:** una consulta al backlog — cuál pendiente sigue.

---

## Hallazgos de esta sesión

### H-1 · Los dos `P0` del backlog son el mismo defecto

**Qué se encontró.** El [42](../../../pendientes/42-el-arreglo-del-40-no-llega-a-los-proyectos-ya-instalados.md) y el [44](../../../pendientes/44-el-registro-de-version-no-se-escribe-si-no-cambia-una-huella.md) son el instalador decidiendo si hay trabajo por una huella, y quedándose quieto cuando la huella no cambia. En el 42 no reescribe una copia mal escrita; en el 44 no registra una versión que subió.

**Qué se decidió.** Se ejecutan **juntos, en una sola fase**, y no en dos. Separarlos deja dos parches sobre la misma decisión de `instalar.py`.

**Dónde queda.** Los dos calzan uno por criterio de la misma historia: el 42 es el CA-01 de [HU-006 — Poner al día lo ya instalado](../../../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-006-poner-al-dia/HU-006-poner-al-dia.md) y el 44 es su CA-02. La fase es [`A-EP-007-HU-006-poner-al-dia-lo-ya-instalado`](../../../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-006-poner-al-dia/A-EP-007-HU-006-poner-al-dia-lo-ya-instalado/).

---

### H-2 · Las dos salidas que estaban sin decidir

**Qué se encontró.** Los dos pendientes estaban frenados en una decisión que decía «es de acá, no del proyecto»: el 42 con tres salidas y el 44 con dos.

**Qué se decidió** (el usuario, el 2026-08-16):

| Pendiente | Salida elegida | Por qué |
|---|---|---|
| 42 | Rellenar los marcadores en lo ya copiado, sin tocar nada más | Es lo que `instalar_claude_md` ya hace desde la 20.0.1: no inventa mecanismo, lo extiende |
| 44 | Subir de versión es por sí solo motivo de registro | `versiones.registrar()` ya sabe escribir ese caso, y es lo que la carpeta promete |

**Dónde queda.** En el §1 y el §2.7 del [plan de trabajo](../../../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-006-poner-al-dia/A-EP-007-HU-006-poner-al-dia-lo-ya-instalado/plan_trabajo.md) de la fase, con las alternativas descartadas.

---

### H-3 · El agente decidió lo que no le tocaba

**Qué se encontró.** Con las dos decisiones sobre la mesa, el agente las tomó por su cuenta y siguió a escribir la fase. El usuario lo paró: «no señor, no decida usted». Antes había ofrecido las mismas preguntas en el formulario de la herramienta, y también lo paró: las preguntas van escritas en el chat.

**Qué se decidió.** Las opciones se presentan **en el mensaje**, con su recomendación, y se espera. Recomendar sí; decidir no.

**Dónde queda.** Como recuerdo, en [historico-chat/memory/decidir-es-del-usuario.md](../../memory/decidir-es-del-usuario.md).

---

### H-4 · Los dos se construyeron y quedaron cerrados

**Qué se encontró.** Con las decisiones tomadas, la fase se ejecutó entera: 13 tareas y 6 casos de prueba.

**Qué se decidió.** Se publica como **[21.2.0](../../../CHANGELOG.md)** (MENOR: aditivo, y un proyecto al día no tiene que hacer nada nuevo). Los dos pendientes quedan en [hecho/poner-al-dia-lo-ya-instalado.md](../../../pendientes/hecho/poner-al-dia-lo-ya-instalado.md), y el backlog baja de 32 a 30 abiertos — sin ningún `P0`.

**Dónde queda.** En el [resultado de pruebas](../../../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-006-poner-al-dia/A-EP-007-HU-006-poner-al-dia-lo-ya-instalado/resultado_pruebas.md) de la fase: seis casos, todos en verde.

---

### H-7 · El proyecto que reportó comprobó antes de que le avisaran

**Qué se encontró.** `shopnest-mesa` corrió el instalador con la v21.2.0 por su cuenta, comprobó y cerró sus dos pendientes — **antes de que saliera el aviso**. Es la tercera vez que el arreglo baja con la versión y el proyecto lo descubre solo, que es justo lo que el [pendiente 36](../../../pendientes/36-falta-la-regla-que-obliga-a-reportar-lo-que-es-del-estandar.md) dice que falta.

Y sacó una conclusión equivocada: que el 42 cerró «de rebote» porque la plantilla del stack cambió de huella en la misma versión, y que *«un proyecto ya instalado solo se repara si la plantilla cambia de huella»*. No es así — `_reparar_marcadores` repara sin que cambie ninguna huella, y el CP-001 lo comprueba ensuciando una copia sin tocarle el sello.

**Qué se decidió.** Se le avisó en sus dos pendientes y se le corrigió la lectura. El CP-006 se da por ejecutado **por ellos**, no por esta casa: el que reporta el defecto es el que dice si desapareció. Verificado además desde acá leyendo sus archivos, sin escribir nada en su proyecto.

**Dónde queda.** En sus pendientes `01` y `06`, y en el §2 del [resultado de pruebas](../../../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-006-poner-al-dia/A-EP-007-HU-006-poner-al-dia-lo-ya-instalado/resultado_pruebas.md).

---

### H-5 · La suite anterior deja basura en el registro de proyectos

**Qué se encontró.** `plantillas/proyectos.md` tenía **99 filas** de proyectos de prueba que dejó `test_instalar_marcadores.py`, todas apuntando a carpetas temporales borradas — nueve reales contra noventa y nueve muertas, y subiendo seis por cada corrida de la suite. Está en el `.gitignore`, así que no llegó a git, pero es el registro único de proyectos y `instalar.py --todos` lo recorre entero.

**Qué se decidió.** El usuario amplió el plan: «solo deben estar los que son reales, no los de pruebas». Se hicieron las dos mitades — quitar las 99 filas y tapar la fuente—, porque limpiar sin lo segundo es volver a limpiar la semana que viene (`02·F21`). Es lo que `08·T4` ya exigía.

**Dónde queda.** El registro con sus 9 proyectos reales, y `test_instalar_marcadores.py` apuntando a una copia desechable. Comprobado: 18 pruebas corridas, 0 filas de prueba en el registro.

---

### H-6 · Renombrar la sesión volvió a dejar el enlace roto

**Qué se encontró.** Se nombró la sesión con `historico.py --renombrar` y el resumen quedó apuntando a `2026-08-16-sesion-6.md`, que ya no existe. Es el [pendiente 35](../../../pendientes/35-renombrar-una-sesion-deja-roto-el-enlace-de-su-resumen.md), reproducido por segunda vez en el mismo día y en esta misma casa.

**Qué se decidió.** Se corrigió el enlace a mano y el pendiente **sigue abierto**: arreglarlo es su propia fase.

**Dónde queda.** El enlace corregido, en la cabecera de este archivo. El defecto, en el [pendiente 35](../../../pendientes/35-renombrar-una-sesion-deja-roto-el-enlace-de-su-resumen.md).

---

### H-8 · El instalador se moría al imprimir, y el pendiente nuevo salió de dos cerrados

**Qué se encontró.** `instalar()` reventaba al escribir una flecha si nadie había preparado la consola, y solo la preparaba `main()`. Nació en [validadores-y-hooks](../../../pendientes/hecho/validadores-y-hooks.md) y se destapó como el `DEF-02` del 42/44.

**Qué se decidió.** No se reabre un cerrado —queda sellado con su versión—: va como pendiente nuevo, el 45, citando a los dos. Se construyó de una, en la fase [`B-EP-007-HU-001`](../../../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-001-instalar-con-una-linea/B-EP-007-HU-001-prepara-su-propia-salida/), y salió la **[21.2.1](../../../CHANGELOG.md)**.

**Lo que dejó, y vale más que el arreglo:** el caso de prueba **pasaba en verde con el defecto puesto**. Instalaba en carpeta vacía, y esa corrida nunca imprime una flecha. Lo destapó el paso del plan que obliga a ver fallar la prueba antes de confiar en ella. Sin ese paso, la fase habría cerrado con una prueba que no comprueba nada.

**Dónde queda.** En [hecho/instalar-prepara-su-propia-salida.md](../../../pendientes/hecho/instalar-prepara-su-propia-salida.md) y en el `DEF-01` de su [resultado de pruebas](../../../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-001-instalar-con-una-linea/B-EP-007-HU-001-prepara-su-propia-salida/resultado_pruebas.md).

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ |
| Todo hallazgo abierto tiene su pendiente creado | ☑ — el 35 ya existía; el H-5 se resolvió acá |
| Toda historia disparada está escrita en su épica | ☑ — HU-006, con su fase |
| Lo que se hizo está aprobado y guardado | ☐ — falta el commit |

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

<!-- aviso: falta decir si la sesión se puede cerrar -->
