# Plan de Trabajo · Fase A-EP-029-HU-006-sin-interfaz (módulo Estándar: el repositorio)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-029-HU-006-sin-interfaz` |
| **Épica** | `EP-029` |
| **HU** | [`HU-006`](../HU-006-el-visor-viejo-interfaz-sale-del-estandar.md), una sola (`F12.1`) |
| **Módulo** | Estándar: `interfaz/`, `.claude/settings.json` y `anatomia/` |
| **Especificación del módulo** | La HU-006 |
| **Fecha apertura** | 2026-10-08 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 4 del pendiente 141](../../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-4.md), el 2026-10-08, con la versión 59.0.0 |
| **Rama** | `main` |

**ORIGEN:** análisis 4 del pendiente 141, punto 2.

| CA de `HU-006` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-006-el-visor-viejo-interfaz-sale-del-estandar.md#ca-01--interfaz-ya-no-existe-y-nada-vivo-la-nombra) | ☑ |

## 1. Objetivo y alcance

**Objetivo:** borrar `interfaz/` y sus menciones vivas.

**Fuera de alcance:** las fases cerradas, `CHANGELOG.md`, `cvds/` y `documentacion/senales.md`, que son historia.

## 2. Análisis previo, línea base verificada

`git ls-files interfaz` da 50 archivos; su `.venv`, `terceros/` y `__pycache__/` no están en git. Ningún `.py` vivo del repositorio la nombra. La nombran `.claude/settings.json` (un permiso), `anatomia/componentes-del-agente.md` y `anatomia/mapa-del-sitio.md`. Lo que pide el cambio (R-19): ninguna migración ni pantalla.

### 2.1 Archivos que se crean o modifican

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `interfaz/.env.example` | Borrar | Visor viejo | |
| `interfaz/README.md` | Borrar | Visor viejo | |
| `interfaz/cimiento/__init__.py` | Borrar | Visor viejo | |
| `interfaz/cimiento/proyectos/__init__.py` | Borrar | Visor viejo | |
| `interfaz/cimiento/proyectos/admin.py` | Borrar | Visor viejo | |
| `interfaz/cimiento/proyectos/apps.py` | Borrar | Visor viejo | |
| `interfaz/cimiento/proyectos/core.py` | Borrar | Visor viejo | |
| `interfaz/cimiento/proyectos/forms.py` | Borrar | Visor viejo | |
| `interfaz/cimiento/proyectos/management/__init__.py` | Borrar | Visor viejo | |
| `interfaz/cimiento/proyectos/management/commands/__init__.py` | Borrar | Visor viejo | |
| `interfaz/cimiento/proyectos/management/commands/registrar.py` | Borrar | Visor viejo | |
| `interfaz/cimiento/proyectos/migrations/0001_initial.py` | Borrar | Visor viejo | |
| `interfaz/cimiento/proyectos/migrations/__init__.py` | Borrar | Visor viejo | |
| `interfaz/cimiento/proyectos/models.py` | Borrar | Visor viejo | |
| `interfaz/cimiento/proyectos/templates/proyectos/editar.html` | Borrar | Visor viejo | |
| `interfaz/cimiento/proyectos/templates/proyectos/lista.html` | Borrar | Visor viejo | |
| `interfaz/cimiento/proyectos/templates/proyectos/medir.html` | Borrar | Visor viejo | |
| `interfaz/cimiento/proyectos/tests.py` | Borrar | Visor viejo | |
| `interfaz/cimiento/proyectos/views.py` | Borrar | Visor viejo | |
| `interfaz/cimiento/visor/__init__.py` | Borrar | Visor viejo | |
| `interfaz/cimiento/visor/admin.py` | Borrar | Visor viejo | |
| `interfaz/cimiento/visor/apps.py` | Borrar | Visor viejo | |
| `interfaz/cimiento/visor/core.py` | Borrar | Visor viejo | |
| `interfaz/cimiento/visor/forms.py` | Borrar | Visor viejo | |
| `interfaz/cimiento/visor/migrations/__init__.py` | Borrar | Visor viejo | |
| `interfaz/cimiento/visor/models.py` | Borrar | Visor viejo | |
| `interfaz/cimiento/visor/templates/visor/_memoria_tabla.html` | Borrar | Visor viejo | |
| `interfaz/cimiento/visor/templates/visor/_senal_detalle.html` | Borrar | Visor viejo | |
| `interfaz/cimiento/visor/templates/visor/doc.html` | Borrar | Visor viejo | |
| `interfaz/cimiento/visor/templates/visor/home.html` | Borrar | Visor viejo | |
| `interfaz/cimiento/visor/templates/visor/memoria.html` | Borrar | Visor viejo | |
| `interfaz/cimiento/visor/templates/visor/panel.html` | Borrar | Visor viejo | |
| `interfaz/cimiento/visor/templatetags/__init__.py` | Borrar | Visor viejo | |
| `interfaz/cimiento/visor/templatetags/visor_extras.py` | Borrar | Visor viejo | |
| `interfaz/cimiento/visor/tests.py` | Borrar | Visor viejo | |
| `interfaz/cimiento/visor/views.py` | Borrar | Visor viejo | |
| `interfaz/config/__init__.py` | Borrar | Visor viejo | |
| `interfaz/config/asgi.py` | Borrar | Visor viejo | |
| `interfaz/config/settings/__init__.py` | Borrar | Visor viejo | |
| `interfaz/config/settings/base.py` | Borrar | Visor viejo | |
| `interfaz/config/settings/local.py` | Borrar | Visor viejo | |
| `interfaz/config/urls.py` | Borrar | Visor viejo | |
| `interfaz/config/wsgi.py` | Borrar | Visor viejo | |
| `interfaz/descargar_estaticos.py` | Borrar | Visor viejo | |
| `interfaz/manage.py` | Borrar | Visor viejo | |
| `interfaz/requirements/base.txt` | Borrar | Visor viejo | |
| `interfaz/requirements/local.txt` | Borrar | Visor viejo | |
| `interfaz/requirements/lock.txt` | Borrar | Visor viejo | |
| `interfaz/static/cimiento/visor.css` | Borrar | Visor viejo | |
| `interfaz/templates/base.html` | Borrar | Visor viejo | |
| `.claude/settings.json` | Modificar | Configuración | Sale el permiso de `interfaz/manage.py` |
| `anatomia/componentes-del-agente.md` | Modificar | Documentación | Sin `interfaz/` |
| `anatomia/mapa-del-sitio.md` | Modificar | Documentación | Sin `interfaz/` |
| `proyectos/cimiento/core/pruebas/tests_un_programa.py` | Crear | Test | El estándar es un solo programa |
| `README.md` | Modificar | Documentación | Su enlace a `interfaz/` queda como texto; lo agregó el análisis 5 del pendiente 141, acuerdo 1 |
| `metricas/README.md` | Modificar | Documentación | Su enlace a `interfaz/` queda como texto; lo agregó el análisis 5 del pendiente 141, acuerdo 1 |
| `cvds/cumplimiento.md` | Modificar | Documentación | Su enlace a `interfaz/` queda como texto; lo agregó el análisis 5 del pendiente 141, acuerdo 1 |
| `pendientes/hecho/los-proyectos-se-administran-desde-cimiento.md` | Modificar | Documentación | Su enlace a `interfaz/` queda como texto; lo agregó el análisis 5 del pendiente 141, acuerdo 1 |
| `pendientes/hecho/metricas-del-proceso.md` | Modificar | Documentación | Su enlace a `interfaz/` queda como texto; lo agregó el análisis 5 del pendiente 141, acuerdo 1 |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Las fases cerradas no se tocan | Corregir sus enlaces | Son historia | `20·M11` |

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

Borrar `interfaz/` se deshace recuperándola de git, del commit anterior.

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Borrar `interfaz/` y quitar sus menciones | Estándar | 0,5 h | Ninguna | EV-01 |
| T-02 | Prueba | Test | 0,5 h | T-01 | EV-01 |

## 5. Verificación de criterios de aceptación

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Prueba de Django | EV-01 | 2026-10-08 | ☑ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 7. Reversión / rollback

Recuperar `interfaz/` de git, del commit anterior.

## 8. Producción y migración incremental

Sin migración.

## 9. Reglas del estándar y del proyecto aplicadas

- Base: `02·F8`, `02·F30`, `20·M11`.

## 11. Definition of Done

- [x] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [x] Pruebas en verde
- [ ] Rama lista para el commit único de la fase

## 13. Cierre

**Hallazgos al ejecutar:** H-8 del 2026-10-07: borrar la carpeta dejó 6 enlaces rotos; los resolvió el análisis 5 del pendiente 141.
