# Estado de fase — Fase A-EP-001-HU-006-retrodocumentar-la-capa-del-proyecto (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **en qué estación va la fase y qué la tiene detenida**, para que una sesión nueva lo lea y siga desde ahí sin releer la conversación.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-001-HU-006-retrodocumentar-la-capa-del-proyecto` |
| **Módulo** | Cuerpo de reglas — la capa propia del proyecto ([`plantillas/reglas-proyecto.md`](../../../../../plantillas/reglas-proyecto.md)) |
| **Épica / HU / origen** | [EP-001](../../epica.md) · [HU-006](../HU-006-capa-propia-del-proyecto.md) · retro-documentación, fila de HU-006 del pendiente [48](../../../../../pendientes/48-inventario-hu.md) |
| **Última actualización** | 2026-08-17 |

---

## 1. En qué estación va

**Estación actual:** cerrada con **No cumple**. **Última puerta pasada:** 11, el cierre documental.

> **La fase se cerró el 2026-08-27 con veredicto «No cumple».** Cerrar no es aprobar: es dejar escrito qué salió. El criterio en rojo y adónde fue a parar están en el [funcionalidad_implementada.md](funcionalidad_implementada.md).

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 orden de bajar a fase las HU del inventario 48 | ☑ |
| 3 | Diseño del plan detallado | plan de trabajo y plan de pruebas escritos | ☑ |
| 4 | Pausa y presentación | 👤 presentado el 2026-08-17 | ☑ |
| 5 | Aprobación del plan detallado | 👤 «autorizados los planes de trabajo», 2026-08-17 | ☑ |
| 6 | Ejecución continua | 8 tareas · **detenida por las 2 dudas de §2.7** | ☐ |
| 7 | Pruebas | `resultado_pruebas` con veredicto | ☐ |
| 8 | Cierre documental | trazabilidad sin faltantes | ☐ |
| 9 | Commit único | 👤 pendiente de autorización | ☐ |
| 10 | Reporte al usuario | — | ☐ |
| 11 | Publicación / despliegue | 👤 pendiente | ☐ |

**Nada se ejecutó todavía.** La fase trabaja sobre una **copia** del proyecto elegido: en la carpeta viva de un proyecto ajeno no se escribe ([`00·N4`](../../../../../base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)).

> **El plan quedó aprobado el 2026-08-17** y la fase **no arrancó**: las 2 dudas de §2.7 del plan sigue sin resolver, y solo la puede resolver el usuario. Lo que falta ya no es la aprobación — es la respuesta.

---

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | **No cumple** |
| **CA cumplidos** | 2 de 3 |
| **CA en "No"** | **CA-03.** No se pudo provocar sin escribir un ajuste contra el núcleo en un proyecto real, y la decisión 35 del pendiente 59 lo prohíbe |
| **Defectos abiertos aceptados** | D-01, `metareglas --raiz` sobre un proyecto da cinco veredictos falsos · D-02, las 56 reglas `P` de AgroSystem sin respaldo, que es del proyecto · D-03, el CA-03 sin provocar |
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) §6 |

---

## 1.2 Avance de las tareas del plan

> Los identificadores se copian del [`plan_trabajo.md`](plan_trabajo.md) §3, que no se toca.

| Tarea | Estado | Nota |
|---|---|---|
| T-01 | Hecha | El proyecto se eligió, y **no fue el propuesto**: shopnest-mesa no tiene reglas propias. Se usó AgroSystem, con 56 |
| T-02 | Hecha | La propia capa de AgroSystem declara la precedencia, y el cuerpo central no cambió |
| T-03 | Hecha | La comprobación de `M16` corre: 56 fallas de 56 reglas |
| T-04 | Hecha, y al revés de lo que decía | La comprobación **sí** corre. La construyó el pendiente 53 cinco días antes. Lo que no sirve es invocarla con `--raiz`, y eso queda como defecto D-01 |
| T-05 | **No hecha** | Provocar el ajuste contra una `[BLINDADA]` exige escribirlo en un proyecto real, y la decisión 35 lo prohíbe. Falta hacerlo sobre un proyecto de mentira en carpeta temporal |
| T-06 | **No hecha** | Depende de T-05 |
| T-07 | Hecha | `validar.py version` avisa del desfase, y avisa sin detener, que es lo previsto |
| T-08 | Hecha | El resultado escrito y la trazabilidad cerrada |

**Hechas:** 6 de 8. **Sin hacer:** T-05 y T-06, que son las del CA-03.

---

## 2. Decisiones y señales generadas  ·  [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión / aprendizaje | Señal registrada |
|---|---|
| Se prueba sobre un proyecto ya instalado, no sobre uno armado: un proyecto de prueba trae ajustes inventados para que la prueba pase | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) |
| El CA-03 necesita su par: el mismo ajuste contra el núcleo y contra una convención de capa 2. Con uno solo no se distingue "no manda nunca" de "no manda sobre el núcleo" | §3.3 y CP-004 del [`plan_pruebas.md`](plan_pruebas.md) |
| El CA-02 se cierra por lectura y se dice que fue por lectura: [`validadores/metareglas.py`](../../../../../validadores/metareglas.py) no tiene punto de entrada | §2.6 del [`plan_trabajo.md`](plan_trabajo.md) y pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md) |

---

## 3. Pendiente / preguntas abiertas

- **El CA-03**, que es lo único que impide cerrar. Falta provocarlo sobre un proyecto de mentira en carpeta temporal.
- **El defecto D-01**, que es del estándar: `metareglas --raiz` sobre un proyecto da cinco veredictos falsos. Necesita su pendiente.
- **El defecto D-02**, que es de AgroSystem: 56 reglas propias sin respaldo. Va por el canal de defectos hacia el proyecto, no se corrige desde acá.

---

## 4. Si se bloqueó

- No está bloqueada. Está en verificación con un CA en rojo, y lo que falta para cerrarla es una tarea, no una decisión. **Motivo original, ya superado:** el plan estaba aprobado desde el 2026-08-17 y sin el proyecto de la duda 1 no arranca ninguno de los tres CA. **Qué falta para desbloquear:** que el usuario apruebe el plan, elija el proyecto y decida la forma del caso del CA-03.

---

## Lo que la desbloqueó

**Las dudas de la §2.7 quedaron decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md). La decisión está escrita en el propio plan, con su motivo.

**La fase no arrancó todavía:** decidir no es ejecutar.
