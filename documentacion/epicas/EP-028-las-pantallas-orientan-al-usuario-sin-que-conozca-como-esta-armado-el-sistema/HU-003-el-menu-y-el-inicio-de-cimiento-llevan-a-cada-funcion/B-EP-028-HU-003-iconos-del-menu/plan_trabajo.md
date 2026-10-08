# Plan de Trabajo · Fase B-EP-028-HU-003-iconos-del-menu (módulo Cimiento: el menú)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-028-HU-003-iconos-del-menu` |
| **Épica** | `EP-028` |
| **HU** | [`HU-003`](../HU-003-el-menu-y-el-inicio-de-cimiento-llevan-a-cada-funcion.md), una sola (`F12.1`) |
| **Módulo** | Cimiento: `templates/base.html` y una plantilla parcial de íconos |
| **Especificación del módulo** | La HU-003, CA-03, y la guía de diseño de pantallas (`base/17-guia-de-pantallas.md`, §4 y §9) |
| **Fecha apertura** | 2026-10-07 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | El usuario, con «Corrija los íconos en el menú no están», el 2026-10-07, con la versión 58.0.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): `A-EP-028-HU-003-menu-e-inicio`, que armó el menú sin íconos.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-003` que cierra esta fase | Estado |
|---|---|
| [CA-03](../HU-003-el-menu-y-el-inicio-de-cimiento-llevan-a-cada-funcion.md#ca-03--cada-entrada-del-menú-lleva-su-ícono) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que cada entrada del menú, también las de los submenús, lleve su ícono, como en la plantilla Tabler.

**Fuera de alcance:** íconos en las demás pantallas.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

El menú (`templates/base.html`) solo trae `nav-link-title`; nunca tuvo íconos (`git show 041984a`). Tabler pone en cada entrada un `span.nav-link-icon` con un SVG de Tabler Icons (clase `icon`). En `node_modules/@tabler/` solo está `core`: Tabler Icons no está instalado, y la plantilla de Tabler los pega como SVG en línea.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/templates/includes/icono.html` | Crear | Plantilla | Los íconos de Tabler Icons del menú, por nombre |
| `proyectos/cimiento/templates/base.html` | Modificar | Plantilla | Cada entrada principal con su `nav-link-icon` |
| `proyectos/cimiento/core/inicio/tests_menu.py` | Modificar | Test | El caso del CA-03 |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| `base.html` | Todas las pantallas | `core.inicio`, `core.ayuda` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

Ninguna.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

El menú lateral.

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Los SVG de Tabler Icons en una plantilla parcial | Instalar el paquete de íconos | Es como lo hace la plantilla de Tabler y no agrega una dependencia (`10·DEP`); la parcial evita copiarlos en cada sitio | Guía §12 |
| `aria-hidden` en cada ícono | Darle texto | El texto ya está al lado; el ícono es adorno | Guía §9 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

No hay acciones nuevas.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | La parcial, el menú y su prueba | Plantilla | 0,5 h | Ninguna | EV-01 |

**Total estimado:** 0,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-03 | Prueba de Django | EV-01 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django |
| Usuarios de prueba | Una cuenta administradora |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Sin migración.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `17·I3`, `17·I5`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Ninguno | | | |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.

**Reabierta** el 2026-10-07: El usuario corrigió: los ítems de los submenús tampoco tienen ícono.

Cerrada otra vez el 2026-10-07, con la versión 56.8.0.
