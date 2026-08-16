# 2026-08-16 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-16-un-pendiente-no-es-un-plan.md](../../2026-08-16-un-pendiente-no-es-un-plan.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

**Viene de:** —, es trabajo nuevo. Lo disparó un proyecto heredero que reportó un enlace roto en su instalación.

---

## Hallazgos de esta sesión

### H-1 · Un pendiente se estaba ejecutando sin bajar a HU ni a fase

- **Qué pasó:** los cuatro pendientes que se cerraron el 2026-08-16 —el 39, el 34, el 31 y el punto 2 del 29— y las reglas que se escribieron ese día se hicieron editando `base/` directo. La última fase abierta es del 2026-08-15.
- **Por qué importa:** sin fase no hay plan de pruebas, y sin plan de pruebas nadie escribe qué había que comprobar. El 34 se publicó sin que nadie corriera la única prueba que importaba —instalar en un proyecto y hacer clic en el enlace—, y el defecto lo encontró el proyecto que lo sufrió.
- **Qué lo soluciona:**
  **EP-004 · HU nueva — comprobar que el pendiente cerrado nombre su fase**
  - **Como** quien mantiene el estándar
  - **Quiero** que un programa avise cuando un pendiente se marca hecho sin nombrar la HU y la fase donde se construyó
  - **Para** que la cadena no dependa de que el agente se acuerde
  - **Contexto:** hoy [`02·F23`](../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md) lo exige y nada lo comprueba. Falta antes fijar en la plantilla del pendiente dónde se escribe esa referencia; sin un sitio fijo el programa no tiene qué leer.
- **Qué se decidió:** los pendientes mejoran el cimiento y por eso recorren la cadena como cualquier desarrollo. Queda escrito como regla.
- **Estado:** resuelto acá
- **Responde a:** —
- **Dispara:** 1. [EP-004 · HU-016](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-016-el-pendiente-cerrado-nombra-su-fase/HU-016-el-pendiente-cerrado-nombra-su-fase.md) — el validador de `F23`. Escrita; su primera tarea es fijar en la plantilla del pendiente dónde va la referencia a la fase, porque sin sitio fijo el programa no tiene qué leer.
- **Orden de resolución:** —
- **Dónde queda:** regla [`02·F23`](../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md) (v21.0.0), y corregidos los dos procedimientos que autorizaban lo contrario: los nueve pasos de [`20 · base.md`](../../../base/20-meta-reglas/base.md) y el §2 del [CLAUDE.md](../../../CLAUDE.md).
- **Nace en:** 2026-08-16 · un-pendiente-no-es-un-plan
- **Cerrado en:** 2026-08-16 · un-pendiente-no-es-un-plan
- **Con qué se retoma:** —

### H-2 · El instalador copia tres archivos sin rellenar sus marcadores

- **Qué pasó:** de los cuatro sitios donde el instalador escribe una copia en el proyecto, solo [`instalar_claude_md`](../../../validadores/instalar.py) pasa el texto por `_rellenar()`. Los otros tres escriben la plantilla cruda: [línea 333](../../../validadores/instalar.py) (`.agente/stack-instalacion.md`), [línea 434](../../../validadores/instalar.py) (`historico-chat/memory/memory.md`) y [línea 708](../../../validadores/instalar.py) (los 4 archivos de `.agente/`).
- **Por qué importa:** el marcador `«RUTA-ESTANDAR»` viaja intacto al proyecto, así que la cita a la regla no abre. Lo reportó un proyecto heredero. Es la deuda que dejó cerrar el pendiente 34 sin fase — el H-1.
- **Qué lo soluciona:**
  **EP-007 · HU-001 — fase nueva: toda copia pasa por el mismo filtro**
  - **Como** quien instala el estándar en un proyecto
  - **Quiero** que ningún archivo copiado conserve un marcador sin llenar
  - **Para** que las citas a las reglas abran desde el primer día
  - **Contexto:** hay que llevar los tres puntos de copia a `_rellenar(leer(origen), _rellenos(ruta))` y agregar la prueba que instala en una carpeta desechable y comprueba que no queda ningún `«…»`. El sello no se ve afectado: la huella se calcula del stack central, no del texto del archivo.
- **Qué se decidió:** se arregla en los tres puntos de copia, y la prueba comprueba **solo los marcadores que el instalador sabe llenar** — no todos los huecos. Los 4 archivos de `.agente/` llegan con huecos a propósito: son las preguntas que contesta el proyecto. El criterio original del plan los daba por defecto y salió rojo en 65 líneas correctas; se corrigió con aprobación del usuario, sin ajustarlo en silencio.
- **Estado:** **resuelto acá** — v21.1.0, veredicto Cumple. Los 19 enlaces de un proyecto **recién instalado** abren, incluido el que reportó el proyecto.
  **Su límite, destapado por otra sesión el mismo día:** un proyecto ya instalado no se arregla reinstalando, porque la huella sale del stack central y el instalador lo da por al día. Quedó como [pendiente 42](../../../pendientes/42-el-arreglo-del-40-no-llega-a-los-proyectos-ya-instalados.md), que no es de esta sesión.
- **Responde a:** EP-007 · HU-001
- **Dispara:** 1. [EP-007 · HU-001 · fase A](../../../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-001-instalar-con-una-linea/A-EP-007-HU-001-rellenar-los-marcadores-al-copiar/) — arregló los tres puntos de copia y dejó la primera prueba del repositorio. **Cerrada el mismo día**, veredicto Cumple.
- **Orden de resolución:** 1 de 2 · va antes que el H-3, porque si el marcador nunca sale del estándar el H-3 deja de tener efecto en un proyecto.
- **Dónde queda:** [pendiente 40](../../../pendientes/40-el-instalador-copia-sin-rellenar-los-marcadores.md), cerrado · fase [`A-EP-007-HU-001`](../../../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-001-instalar-con-una-linea/A-EP-007-HU-001-rellenar-los-marcadores-al-copiar/)
- **Nace en:** 2026-08-16 · un-pendiente-no-es-un-plan
- **Cerrado en:** 2026-08-16 · un-pendiente-no-es-un-plan
- **Con qué se retoma:** —

### H-3 · El marcador nunca se resuelve bien dentro de un proyecto

- **Qué pasó:** [`enlaces.py`](../../../validadores/enlaces.py) resuelve `«RUTA-ESTANDAR»` contra la raíz que está validando, dando por hecho que esa raíz es el estándar. Los enganches lo corren como `python "<estandar>/validadores/<guion>" --raiz "<proyecto>"`, así que dentro de un proyecto busca `<proyecto>/base/…`, que nunca existe.
- **Por qué importa:** el proyecto que reportó el defecto creyó que el revisor callaba; no calla, pero tampoco acierta. Y el arreglo del H-2 no lo cubre: mañana se escapa otro marcador y vuelve a fallar en silencio.
- **Qué lo soluciona:**
  **EP-004 · HU-005 — fase nueva: el marcador se resuelve contra el estándar**
  - **Como** quien revisa los enlaces de un proyecto
  - **Quiero** que el marcador se resuelva contra la carpeta donde vive el estándar
  - **Para** que el resultado sea el mismo se corra desde donde se corra
  - **Contexto:** es cambiar `base = raiz` por la raíz del propio módulo. Dentro del estándar las dos son la misma carpeta, así que no cambia nada acá; dentro de un proyecto es la diferencia entre resolver y no resolver nunca.
- **Qué se decidió:** el marcador se resuelve contra la carpeta donde vive el estándar, deducida del propio archivo. Se conserva la rama aunque el H-2 haga que dejen de llegar marcadores: es la red para el que se escape mañana.
- **Estado:** **resuelto acá** — v21.1.1, veredicto Cumple. La salida sobre el propio estándar quedó idéntica antes y después, comparada línea por línea.
- **Responde a:** EP-004 · HU-005
- **Dispara:** 1. [EP-004 · HU-005 · fase A](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-005-enlaces-y-citas/A-EP-004-HU-005-el-marcador-se-resuelve-contra-el-estandar/) — la red de seguridad del H-2. **Cerrada el mismo día**, veredicto Cumple.
- **Orden de resolución:** 2 de 2 · después del H-2, que quita la causa; este cubre lo que se vuelva a escapar.
- **Dónde queda:** [pendiente 41](../../../pendientes/41-el-marcador-no-se-resuelve-dentro-de-un-proyecto.md), cerrado · fase [`A-EP-004-HU-005`](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-005-enlaces-y-citas/A-EP-004-HU-005-el-marcador-se-resuelve-contra-el-estandar/)
- **Nace en:** 2026-08-16 · un-pendiente-no-es-un-plan
- **Cerrado en:** 2026-08-16 · un-pendiente-no-es-un-plan
- **Con qué se retoma:** —

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ los tres |
| Todo hallazgo abierto tiene su pendiente creado | ☑ ninguno quedó abierto: el [40](../../../pendientes/40-el-instalador-copia-sin-rellenar-los-marcadores.md) y el [41](../../../pendientes/41-el-marcador-no-se-resuelve-dentro-de-un-proyecto.md) cerraron el mismo día |
| Toda historia disparada está escrita en su épica | ☑ [EP-004 · HU-016](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-016-el-pendiente-cerrado-nombra-su-fase/) nueva, y las dos fases colgando de HU existentes |
| Lo que se hizo está aprobado y guardado | ☐ **sin commit** — es lo único que falta |

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

---

_(Si la sesión no dejó nada, se escribe "nada": es un dato, no un olvido.)_

<!-- aviso: falta decir si la sesión se puede cerrar -->
