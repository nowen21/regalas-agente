# 2026-08-17 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-17-plan-de-pruebas-y-estado-de-las-51-fases.md](../../2026-08-17-plan-de-pruebas-y-estado-de-las-51-fases.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

**Viene de:** «...»

---

## Hallazgos de esta sesión

### 1 · Las 51 fases abiertas tenían plan de trabajo pero no plan de pruebas ni estado

**Qué pasó.** La sesión anterior abrió 51 fases —una por cada HU sin fase del pendiente [48](../../../pendientes/48-inventario-hu.md)— y les dejó `plan_trabajo.md` y `README.md`. Faltaban los otros dos documentos que la fase necesita **antes** de ejecutarse: el `plan_pruebas.md`, que se aprueba junto con el plan ([`02·F4`](../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)), y el `estado-fase.md`, que dice en qué estación va.

**Dónde queda.** Se escribieron los dos en cada fase. Los otros dos que faltan —`resultado_pruebas.md` y `funcionalidad_implementada.md`— **salen de ejecutar**, y ninguna de las 51 está aprobada todavía: escribirlos ahora sería inventar el resultado.

### 2 · Una fase sin aprobar tiene un estado que decir, y no es "vacío"

**Qué se aprendió.** El `estado-fase.md` no es un documento de cierre: es el que permite retomar. Escrito antes de ejecutar, dice la estación 4 —pausa y presentación—, el veredicto **«Todavía no se ejecutó»**, las tareas en Pendiente o **Bloqueada** con la duda que las bloquea, y qué falta para desbloquear.

**Dónde queda.** En las 51 fases. En varias, la §1.2 deja a la vista que **casi todas las tareas están bloqueadas por una duda de §2.7 del plan** — no es un detalle de forma: es la lista de lo que hay que preguntarle al usuario para que la épica pueda avanzar.

### 3 · Los CA que ya se sabe que van a quedar en «No» se declaran en el plan, no al correr

**Qué se aprendió.** Varias fases retrodocumentan algo que **no está cumplido**: el cambio sin entrada en el registro no lo frena nadie ([EP-002 · HU-002](../../../documentacion/epicas/EP-002-versionado-y-adopcion/HU-002-registro-de-cambios/HU-002-registro-de-cambios.md) CA-02), la regla sin clasificar tampoco ([EP-004 · HU-002](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-002-marca-de-comprobable-en-cada-regla/HU-002-marca-de-comprobable-en-cada-regla.md) CA-03), y el aviso de desfase no dice qué cambió ([EP-002 · HU-004](../../../documentacion/epicas/EP-002-versionado-y-adopcion/HU-004-aviso-al-quedar-atras/HU-004-aviso-al-quedar-atras.md) CA-01).

**Por qué importa.** Un caso escrito esperando que el hueco no exista da un rojo que se lee como defecto de la fase. Escrito al revés —afirmando la falta y dejando la evidencia— el rojo es el dato que la fase siguiente necesita.

**Dónde queda.** En el `plan_pruebas.md` de esas fases, y en el §1.1 de su `estado-fase.md`, que lo dice antes de correr.

### 4 · El marcador `«RUTA-ESTANDAR»` deja 28 enlaces rotos en los documentos de fase de esta casa

**Qué se midió.** Al comprobar los 1438 enlaces relativos de los 140 `plan_pruebas.md` y `estado-fase.md` del árbol, salieron **28 rotos**. Ninguno en lo escrito hoy: los 28 están en las 19 fases que ya tenían esos documentos, y **todos** son el marcador `«RUTA-ESTANDAR»` sin resolver. En `documentacion/` la marca aparece en 47 archivos.

**Por qué importa.** En un proyecto heredero el marcador se rellena al instalar; en **este** repositorio no hay nada que lo rellene, así que queda como marca en un documento entregado — lo que [`13·DOC20`](../../../base/13-documentacion/reglas/DOC20-no-entregues-como-terminado-un-documento-con-marcas.md) prohíbe. En los documentos escritos hoy se usó la ruta relativa real, por eso no tienen ninguno.

**Dónde queda.** Ya está anotado: es el pendiente [41](../../../pendientes/41-el-marcador-no-se-resuelve-dentro-de-un-proyecto.md), con [40](../../../pendientes/40-el-instalador-copia-sin-rellenar-los-marcadores.md) y [42](../../../pendientes/42-el-arreglo-del-40-no-llega-a-los-proyectos-ya-instalados.md) a su lado. Lo que esta sesión agrega es **el número**: 28 enlaces, 47 archivos, medidos el 2026-08-17.

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ |
| Todo hallazgo abierto tiene su pendiente creado | ☑ — el 4 ya estaba en el pendiente [41](../../../pendientes/41-el-marcador-no-se-resuelve-dentro-de-un-proyecto.md); esta sesión le agregó la medición |
| Toda historia disparada está escrita en su épica | ☑ — no se disparó ninguna: las 51 fases ya tenían su HU |
| Lo que se hizo está aprobado y guardado | ☐ — falta que el usuario lea los documentos y autorice el commit |

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

---

_(Si la sesión no dejó nada, se escribe "nada": es un dato, no un olvido.)_
