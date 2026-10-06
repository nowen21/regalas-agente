# Plan de Trabajo · Fase `A-EP-025-HU-018-la-ayuda` (módulo `proyectos/cimiento/core/ayuda/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-018-la-ayuda` |
| **Épica** | [EP-025](../../epica.md) |
| **HU** | [HU-018](../HU-018-cimiento-trae-su-ayuda-y-su-manual.md), una sola (`F12.1`) |
| **Módulo** | `proyectos/cimiento/core/ayuda/` |
| **Especificación del módulo** | Los CA de la [HU-018](../HU-018-cimiento-trae-su-ayuda-y-su-manual.md) |
| **Fecha apertura** | 2026-10-05 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva, traída de scilit. Sale del punto 14 del [análisis 2 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md).

**Carencias que cierra** (`02·F14` Q3): Cimiento no tiene ayuda ni manual.

**Aprobación** (`02·F4`): [análisis 2 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md), el 2026-10-05, con la versión 54.4.0

**Disparo** (`02·F15`, etapa 2): el usuario pidió «continúe» el 2026-10-05, después de aprobar el análisis.

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-018 | Estado |
|---|---|
| CA-01 · Ayuda en campos y pantallas | ☑ |
| CA-02 · El manual y su cobertura | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** `core/ayuda/` con la ayuda de scilit, las secciones de las pantallas de Cimiento y sus pruebas de cobertura.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Campos y pantallas | Pantallas | Media |
| CA-02 | Manual y cobertura | Pantallas y pruebas | Media |

**Fuera de alcance:** que scilit use esta ayuda.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Verificado el 2026-10-05, sobre la versión 55.0.0:

- En scilit, `proyectos/scilit/apps/ayuda/` tiene `textos.py` (CAMPOS y PANTALLAS), `secciones.py`, `claves.py`, `views.py`, `urls.py`, `templatetags/ayuda_tags.py`, ocho plantillas base y una sección por pantalla; el CSS y el JS viven en su `static/css/main.css` y `static/js/main.js`, y el botón y el panel en su `templates/base.html`. Usa Bootstrap Icons.
- Cimiento usa Tabler 1.6.1, htmx y ApexCharts desde `node_modules`; no trae Bootstrap Icons. Sus pantallas: entrar, inicio, proyectos (lista, registrar, editar, configuración, suspensiones), reglas e historial, y gasto.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/ayuda/__init__.py`, `proyectos/cimiento/core/ayuda/apps.py`, `proyectos/cimiento/core/ayuda/textos.py`, `proyectos/cimiento/core/ayuda/secciones.py`, `proyectos/cimiento/core/ayuda/claves.py`, `proyectos/cimiento/core/ayuda/views.py`, `proyectos/cimiento/core/ayuda/urls.py`, `proyectos/cimiento/core/ayuda/tests.py` | Crear | Programa | La aplicación |
| `proyectos/cimiento/core/ayuda/templatetags/__init__.py`, `proyectos/cimiento/core/ayuda/templatetags/ayuda.py` | Crear | Programa | Las etiquetas |
| `proyectos/cimiento/core/ayuda/static/ayuda/ayuda.css`, `proyectos/cimiento/core/ayuda/static/ayuda/ayuda.js` | Crear | Pantallas | Globos, panel y mapa |
| `proyectos/cimiento/core/ayuda/templates/ayuda/tooltip.html`, `proyectos/cimiento/core/ayuda/templates/ayuda/tooltip_contenido.html`, `proyectos/cimiento/core/ayuda/templates/ayuda/campo.html`, `proyectos/cimiento/core/ayuda/templates/ayuda/ayuda_corta.html`, `proyectos/cimiento/core/ayuda/templates/ayuda/ayuda_pantalla.html`, `proyectos/cimiento/core/ayuda/templates/ayuda/mapa.html`, `proyectos/cimiento/core/ayuda/templates/ayuda/panel.html`, `proyectos/cimiento/core/ayuda/templates/ayuda/manual.html` | Crear | Pantallas | |
| `proyectos/cimiento/core/ayuda/templates/ayuda/secciones/primeros-pasos.html`, `proyectos/cimiento/core/ayuda/templates/ayuda/secciones/palabras.html`, `proyectos/cimiento/core/ayuda/templates/ayuda/secciones/entrar.html`, `proyectos/cimiento/core/ayuda/templates/ayuda/secciones/inicio.html`, `proyectos/cimiento/core/ayuda/templates/ayuda/secciones/proyectos.html`, `proyectos/cimiento/core/ayuda/templates/ayuda/secciones/registrar.html`, `proyectos/cimiento/core/ayuda/templates/ayuda/secciones/reglas.html`, `proyectos/cimiento/core/ayuda/templates/ayuda/secciones/configuracion.html`, `proyectos/cimiento/core/ayuda/templates/ayuda/secciones/suspensiones.html`, `proyectos/cimiento/core/ayuda/templates/ayuda/secciones/gasto.html` | Crear | Documentación | Una por pantalla |
| `proyectos/cimiento/config/settings/base.py`, `proyectos/cimiento/config/urls.py`, `proyectos/cimiento/templates/base.html` | Modificar | Programa | La aplicación, sus rutas, el botón y el panel |
| `proyectos/cimiento/core/proyectos/templates/proyectos/configuracion.html`, `proyectos/cimiento/core/proyectos/templates/proyectos/suspensiones.html` | Modificar | Pantallas | La ayuda en sus campos y en la pantalla |
| `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-018-cimiento-trae-su-ayuda-y-su-manual/HU-018-cimiento-trae-su-ayuda-y-su-manual.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | Modificar | Documentación | La fila de la fase y el estado |
| `CHANGELOG.md` | Modificar | Documentación | Declarado durante la fase: la entrada 55.0.0 suma las HU-013, 014, 015, 017, 018 y 024 |
| `anatomia/que-esta-amarrado-a-la-herramienta.md` | Modificar | Documentación | Declarado durante la fase: la batería completa mostró que las piezas nuevas de EP-025 no estaban en el mapa del amarre |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| `templates/base.html` suma el botón «Ayuda», el panel, el CSS y el JS | Todas las pantallas | Se corren las pruebas de todas las aplicaciones |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

| Ruta | Quién la ve |
|---|---|
| `/ayuda/`, `/ayuda/pantalla/`, `/ayuda/<sección>/` | Toda cuenta |

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

El botón «Ayuda» arriba de cada pantalla; el «?» de cada campo; los botones de ayuda de «Configuración» y «Suspensiones»; `/ayuda/` para el manual completo.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Sin Bootstrap Icons: el «?» y los demás signos van en CSS y texto | Sumar la dependencia | Cimiento no la trae, y sería una dependencia nueva solo para íconos | RN-05 |
| Las etiquetas se llaman `ayuda` (no `ayuda_tags`) | El nombre de scilit | Cimiento nombra sus etiquetas por su tema (`gasto`) | Propuesta del agente |
| La prueba de cobertura recorre las rutas de Cimiento con nombre, menos las que no son pantallas (salir, la parte que se recarga, levantar, las de la ayuda) | Una lista escrita a mano | Una pantalla nueva sin sección hace fallar la prueba sola | Punto 14 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  `02·F30`

No aplica: la ayuda muestra; no crea ni cambia nada.

## 3. Desglose de tareas por criterio de aceptación

### CA-01 · Ayuda en campos y pantallas

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | La aplicación, sus etiquetas, plantillas, CSS y JS, traídos de scilit sin íconos | `proyectos/cimiento/core/ayuda/` | CA-01 | Nuevo | 2 h | Ninguna | CP-001 |
| T-02 | Los textos de «Configuración» y «Suspensiones», y su uso en esas pantallas | `proyectos/cimiento/core/ayuda/textos.py`, las dos plantillas | CA-01 | Pantallas | 1 h | T-01 | CP-001 |
| T-03 | El botón y el panel en la plantilla base; la aplicación y sus rutas | `proyectos/cimiento/templates/base.html`, `proyectos/cimiento/config/settings/base.py`, `proyectos/cimiento/config/urls.py` | CA-01 | Todas | 0,5 h | T-01 | CP-001 |

### CA-02 · El manual y su cobertura

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-04 | Las secciones del manual, con el molde del estándar | `proyectos/cimiento/core/ayuda/secciones.py`, `proyectos/cimiento/core/ayuda/templates/ayuda/secciones/` | CA-02 | Documentación | 2 h | T-01 | CP-002 |
| T-05 | Las pruebas: toda clave con texto, toda pantalla con sección | `proyectos/cimiento/core/ayuda/claves.py`, `proyectos/cimiento/core/ayuda/tests.py` | CA-02 | Pruebas | 1 h | T-04 | CP-002 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-06 | Correr todo y cerrar con `cerrar_fase` | La HU y la épica | CA-01, CA-02 | Documentación | 0,5 h | T-01 a T-05 | CP-001, CP-002 |

## 4. Secuencia de ejecución

T-01 a T-06.

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Las páginas traen el «?», los botones y el panel | CP-001 |
| CA-02 | El manual y las dos pruebas de cobertura | CP-002 |

## 6. Datos y ambiente de prueba

La base de pruebas y una cuenta de consulta.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Nada que migrar; `collectstatic` junta el CSS y el JS nuevos.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`00·ID7`, `00·ID10`, `17`, `07·Q4`, `02·F4`, `02·F5`, `02·F8`, `00·ID8`, `00·ID9`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Una pantalla sin sección | La prueba de cobertura |

## 11. Definition of Done

- [ ] CA-01 y CA-02 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Las pruebas de la fase sin fallas, y cero marcas nuevas.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 6 tareas quedaron hechas el 2026-10-05, con la versión 55.0.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** ninguno.
