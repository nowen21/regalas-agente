# Estado de fase — Fase «A-EP-007-HU-006-poner-al-dia-lo-ya-instalado» (módulo «Instalación»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-007-HU-006-poner-al-dia-lo-ya-instalado` |
| **Módulo** | Instalación (`validadores/instalar.py`) |
| **Planteamiento / Épica / HU** | [EP-007](../../epica.md) · [HU-006](../HU-006-poner-al-dia.md) · pendientes [42](../../../../../pendientes/hecho/poner-al-dia-lo-ya-instalado.md) y [44](../../../../../pendientes/hecho/poner-al-dia-lo-ya-instalado.md) |
| **Última actualización** | 2026-08-16 |

---

## 1. En qué estación va

**Estación actual:** 10 — reporte al usuario. **Última puerta pasada:** 9, commit `9846650`.

Se usan las **once etapas de [`02·F15`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F15-no-saltes-ni-reordenes-las-once-etapas-de-la-fase.md)**, que es la fuente única del ciclo de una fase en este repositorio.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 el usuario pidió ejecutar el 42 y el 44 de una | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | presentados al usuario | ☑ |
| 5 | Aprobación del plan detallado | 👤 aprobados el 2026-08-16 | ☑ |
| 6 | Ejecución continua | plan implementado, 13 tareas | ☑ |
| 7 | Pruebas | `resultado_pruebas` con veredicto por CA | ☑ Cumple, ciclo 2 · 6 de 6 |
| 8 | Cierre documental | trazabilidad sin faltantes | ☑ |
| 9 | Commit único | 👤 autorizado · `9846650`, 22 archivos | ☑ |
| 10 | Reporte al usuario | hash, resumen y estado | ☑ |
| 11 | Publicación / despliegue | 👤 **acá está detenida** — falta el `push` | ☐ |

**El CP-006 no lo corrió esta casa:** lo corrió `shopnest-mesa`, que es quien reportó los dos defectos, y desde acá se verificó leyendo sus archivos sin escribir nada. Vale más así — el que reporta es el que dice si desapareció.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 2 de 2 (CA-01 y CA-02), por prueba automática |
| **CA en "No"** | ninguno |
| **Defectos abiertos aceptados** | ninguno. El `DEF-01` y el `DEF-02` eran de la prueba y quedaron corregidos |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | `_reparar_marcadores` en `instalar.py` |
| T-02 | Hecha | `instalar_stack` repara en la rama de «ya estaba al día» |
| T-03 | Hecha | `instalar_agente_config` repara los que ya existían |
| T-04 | Hecha | `_refrescar_sello` repara, así que entran el histórico y la memoria |
| T-05 | Hecha | CP-001 |
| T-06 | Hecha | CP-003 |
| T-07 | Hecha | `registrar_version` registra por subida de versión; el propio estándar exento |
| T-08 | Hecha | Fila `versiones` de `plantillas/stack-instalacion.md` |
| T-09 | Hecha | CP-004 |
| T-10 | Hecha | CP-005 |
| T-11 | Hecha | `validadores/docs/instalar.md` y §8 de la HU-006 |
| T-12 | Hecha | `pendientes/hecho/poner-al-dia-lo-ya-instalado.md` y el `README` del backlog |
| T-13 | Hecha | `CHANGELOG` 21.2.0 y `VERSION` |

**Hechas:** 13 de 13. **Bloqueadas:** ninguna.

---

## 2. Decisiones y señales generadas

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Dos pendientes que son el mismo defecto se cierran en una sola fase, no en dos | Queda en el §0 del plan de trabajo |
| «Al día» contra la plantilla no significa «bien escrito»: son dos preguntas distintas y el instalador solo hacía una | Queda en el `_reparar_marcadores` y en el CP-001 |
| Una prueba que necesita que el estándar cambie se hace contra una copia desechable, no contra el estándar | Queda en el `_estandar_temporal()` de la suite |
| El veredicto de un arreglo del instalador no lo da el instalador: lo da `checklist` | Queda en el paso 6 del CP-004 |

---

## 3. Pendiente / preguntas abiertas

- **El `push`.** Lo autoriza el usuario aparte, y la autorización del commit no lo cubre ([`00·N2`](«RUTA-ESTANDAR»/base/00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)). Es lo único que detiene la fase.
- **Dos archivos de otra sesión quedaron sin commitear** a propósito: la transcripción y el resumen de `un-pendiente-no-es-un-plan`. Son de otra sesión y mezclarlos ensucia el versionado.
- **Avisado a `shopnest-mesa`** el 2026-08-16, en sus pendientes `01` y `06`. Se le corrigió además una conclusión equivocada: había entendido que el 42 cerró «de rebote» y que un proyecto ya instalado solo se repara si cambia la huella de la plantilla. Que el aviso haya tenido que salir a mano sigue siendo el [pendiente 36](../../../../../pendientes/hecho/el-defecto-del-estandar-se-reporta-y-se-avisa-de-vuelta.md).
- **Dos hallazgos fuera del criterio**, en el §4 del [`resultado_pruebas.md`](resultado_pruebas.md). El primero —las 99 filas de prueba en `plantillas/proyectos.md`— lo amplió el usuario al plan y quedó resuelto. El segundo sigue abierto: `instalar()` revienta al imprimir si nadie llamó antes a `preparar_salida()`.

---

## 4. Si se bloqueó

No está bloqueada. Espera una autorización, que es distinto.
