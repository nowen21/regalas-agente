# Pendiente · El instalador copia tres archivos sin rellenar sus marcadores

**Estado:** **cerrado** el 2026-08-16 (v21.1.0) · anotado el mismo día.

| | |
|---|---|
| **De dónde sale** | El hallazgo H-2 del [resumen del 2026-08-16](../../historico-chat/resumenes/2026-08-16/un-pendiente-no-es-un-plan.md) |
| **Historia que lo recoge** | [EP-007 · HU-001](../../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-001-instalar-con-una-linea) |
| **Fase donde se construyó** | [`A-EP-007-HU-001-rellenar-los-marcadores-al-copiar`](../../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-001-instalar-con-una-linea/A-EP-007-HU-001-rellenar-los-marcadores-al-copiar) — veredicto **Cumple** |
| **Proyecto de origen** | `shopnest-mesa`, que reportó el enlace muerto en su `.agente/stack-instalacion.md` |

> **Es el primer pendiente que se cierra por la cadena que exige [`02·F23`](../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md)** — la regla que nació de que este mismo defecto se colara. Falta avisarle a `shopnest-mesa`, que depende del [36](el-defecto-del-estandar-se-reporta-y-se-avisa-de-vuelta.md).

## El problema

El instalador escribe copias en el proyecto desde cuatro sitios, y **solo uno** pasa el texto por `_rellenar()`:

| Dónde | Qué copia | ¿Rellena? |
|---|---|---|
| [`instalar_claude_md`](../../validadores/instalar.py) | `CLAUDE.md` | sí |
| [`instalar_stack`](../../validadores/instalar.py) | `.agente/stack-instalacion.md` | **no** |
| [`instalar_recuerdos`](../../validadores/instalar.py) | `historico-chat/memory/memory.md` | **no** |
| [`instalar_agente_config`](../../validadores/instalar.py) | los 4 archivos de `.agente/` | **no** |

Los tres que no rellenan escriben la plantilla cruda, así que el marcador `«RUTA-ESTANDAR»` viaja intacto al proyecto. Las 22 plantillas traen 84 marcadores entre todas, y las citas a las reglas que los llevan no abren: quien haga clic no llega a ninguna parte.

**De dónde viene.** Lo dejó la [20.0.1](../../CHANGELOG.md), que pasó los 91 enlaces de las plantillas a `«RUTA-ESTANDAR»/base/…` dando por hecho que el instalador siempre rellena. Se cerró sin fase y sin plan de pruebas, que es el hallazgo H-1 de esa misma sesión y el motivo de [`02·F23`](../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md).

## Qué falta

1. Que los tres puntos de copia escriban `_rellenar(leer(origen), _rellenos(ruta))`, como ya hace el cuarto.
2. La prueba que faltó: instalar en una carpeta desechable y comprobar que **ningún** archivo copiado conserva un `«…»`. Es lo que habría atrapado esto.
3. Decir en el `CHANGELOG` qué tiene que hacer un proyecto ya instalado para quedar al día — probablemente reinstalar.

**Lo que no hay que temer:** el sello no se ve afectado. La huella se calcula del stack central ([`checklist.py`](../../validadores/checklist.py) · `huella()`), no del texto del archivo copiado, así que rellenar los marcadores no rompe la comparación que detecta componentes nuevos.

## Con qué se cruza

- El [41](el-marcador-se-resuelve-contra-el-estandar.md) es su red de seguridad y va **después**: este quita la causa, aquel cubre el marcador que se vuelva a escapar.
- El [36](el-defecto-del-estandar-se-reporta-y-se-avisa-de-vuelta.md): al cerrar hay que avisarle a `shopnest-mesa`, que tiene su propio pendiente esperando.

## Cómo se sabe que cerró

Una instalación nueva no deja ningún `«…»` en lo que copió, la prueba lo comprueba sola, y el enlace del `.agente/stack-instalacion.md` de un proyecto abre la regla que cita.

## Qué pasó al cerrarlo

Las tres cosas se cumplen, con una corrección: **el criterio de arriba estaba mal escrito**, y lo destapó la propia prueba.

Un `.md` copiado trae dos clases de hueco. Los que llena el instalador —la ruta del estándar, el nombre del proyecto— y los que llena el proyecto después: a qué se dedica el negocio, quién usa el sistema. Los cuatro archivos de `.agente/` llegan con los segundos **a propósito**: son las preguntas que nadie puede responder desde afuera. Pedir que no quedara *ningún* hueco daba rojo en 65 líneas correctas.

Lo que quedó comprobándose es lo que sí es defecto: ningún archivo copiado conserva un marcador de `_rellenos()`, que es la lista de lo que el instalador se comprometió a llenar.

**Resultado:** los 19 enlaces `.md` de un proyecto recién instalado abren, incluido el de `F13` que reportó `shopnest-mesa`. Detalle en el [`resultado_pruebas.md`](../../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-001-instalar-con-una-linea/A-EP-007-HU-001-rellenar-los-marcadores-al-copiar/resultado_pruebas.md) de la fase.

**Lo que no arregla:** un proyecto instalado **antes** de este cambio conserva los marcadores crudos en sus cuatro archivos de `.agente/`, porque esos no se pisan una vez creados. Está avisado en el `CHANGELOG` de la 21.1.0.
