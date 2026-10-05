# Plan de Trabajo · Fase `A-EP-025-HU-003-registro-de-proyectos` (módulo `proyectos/cimiento/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-003-registro-de-proyectos` |
| **Épica** | [EP-025](../../epica.md) |
| **HU** | [HU-003](../HU-003-los-proyectos-quedan-registrados-en-cimiento.md), una sola (`F12.1`) |
| **Módulo** | `proyectos/cimiento/` |
| **Especificación del módulo** | Los CA de la [HU-003](../HU-003-los-proyectos-quedan-registrados-en-cimiento.md) |
| **Fecha apertura** | 2026-10-04 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva. Sale del punto 4 del [análisis 1 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md) (acuerdos 2, 10 y 11).

**Carencias que cierra** (`02·F14` Q3): Cimiento no sabe qué proyectos existen ni dónde están sus registros de Claude Code.

**Aprobación** (`02·F4`): [análisis 1 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md), el 2026-10-04, con la versión 54.2.0. El ciclo 2, por orden del usuario del 2026-10-05: «hágalo cree las migraciones de los proyectos que existen y reinicie la DB»

**Disparo** (`02·F15`, etapa 2): el usuario aprobó el análisis el 2026-10-04 y pidió seguir con «Continúe con el pendiente 119».

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-003 | Estado |
|---|---|
| CA-01 · Un administrador registra un proyecto | ☑ |
| CA-02 · Lo que no vale no se guarda | ☑ |
| CA-03 · Un proyecto se edita y se desactiva | ☑ |
| CA-04 · El grupo consulta solo ve | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que cada proyecto quede registrado en Cimiento con su ruta, su carpeta de Claude Code y sus límites de aviso.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Registrar | Programa | Media |
| CA-02 | Validaciones | Programa | Media |
| CA-03 | Editar y desactivar | Programa | Baja |
| CA-04 | Permiso por grupo | Programa | Baja |

**Fuera de alcance:** traer los proyectos de `plantillas/proyectos.md`; niveles de reglas; gasto.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-10-04, sobre la versión 54.2.0:

- `~/.claude/projects/` tiene 19 carpetas; todas siguen la regla de la HU, por ejemplo `C:\Ing. Jose\ia\agente` da `c--Ing--Jose-ia-agente` y la `ó` de «Especialización» da `-`.
- `core/cuentas/permisos.py` (HU-002) trae `SoloAdministrador` y `es_administrador`.
- `core/comun/proyecto.py` ya tiene una clase `Proyecto` (rutas dentro del repositorio); el modelo nuevo vive en otro módulo, `core/proyectos/`, y no la toca.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/proyectos/__init__.py`, `proyectos/cimiento/core/proyectos/apps.py`, `proyectos/cimiento/core/proyectos/models.py`, `proyectos/cimiento/core/proyectos/claude.py`, `proyectos/cimiento/core/proyectos/forms.py`, `proyectos/cimiento/core/proyectos/views.py`, `proyectos/cimiento/core/proyectos/urls.py`, `proyectos/cimiento/core/proyectos/tests.py` | Crear | Programa | El módulo de proyectos |
| `proyectos/cimiento/core/proyectos/migrations/__init__.py`, `proyectos/cimiento/core/proyectos/migrations/0001_initial.py` | Crear | Datos | La tabla de proyectos |
| `proyectos/cimiento/core/proyectos/templates/proyectos/lista.html`, `proyectos/cimiento/core/proyectos/templates/proyectos/formulario.html` | Crear | Pantalla | Lista y formulario |
| `proyectos/cimiento/config/settings/base.py`, `proyectos/cimiento/config/urls.py` | Modificar | Configuración | La aplicación y sus rutas |
| `proyectos/cimiento/templates/base.html` | Modificar | Pantalla | «Proyectos» en el menú |
| `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-003-los-proyectos-quedan-registrados-en-cimiento/HU-003-los-proyectos-quedan-registrados-en-cimiento.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | Modificar | Documentación | La fila de la fase y el estado |
| `proyectos/cimiento/core/proyectos/registro.py`, `proyectos/cimiento/core/proyectos/migrations/0002_proyectos_existentes.py`, `proyectos/cimiento/core/proyectos/management/__init__.py`, `proyectos/cimiento/core/proyectos/management/commands/__init__.py`, `proyectos/cimiento/core/proyectos/management/commands/registrar.py`, `proyectos/cimiento/core/proyectos/tests_registro.py` | Crear | Datos | Ciclo 2 (D-01): los proyectos que existen entran a la base nueva, y la puerta del instalador |
| `proyectos/cimiento/core/herramientas/instalar.py`, `validadores/instalar.py` | Modificar | Programa | Ciclo 2 (D-01): el instalador registra en Cimiento y no en `interfaz/` |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

No aplica: no cambia contratos existentes.

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

| Ruta | Vista | Acceso |
|---|---|---|
| `/proyectos/` | Lista | Con cuenta |
| `/proyectos/registrar/` | Registro | Administrador |
| `/proyectos/«id»/editar/` | Edición | Administrador |

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

«Proyectos» en el menú lateral.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno nuevo: el permiso es por grupo, con `SoloAdministrador`.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| La carpeta de Claude Code se calcula en `carpeta_de_claude(ruta)` y se guarda al guardar | Escribirla en el formulario | Así se equivoca menos, y una sola función sabe la regla | Punto 4 |
| Si existe la carpeta con la unidad en mayúscula, se usa esa | Solo minúscula | La letra depende de cómo se abrió la herramienta | Propuesta del agente |
| La ruta se guarda absoluta y se compara sin distinguir mayúsculas | Comparar el texto tal cual | En Windows `C:\X` y `c:\x` son la misma carpeta | RN-03 |
| Desactivar con un campo `activo`; no hay borrar | Borrar | El gasto y los niveles de un proyecto inactivo siguen valiendo como historia | RN-05 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| Proyectos en Cimiento | Solo en `plantillas/proyectos.md` | También en la base de Cimiento, con límites | `14·EST1` |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-01 · Un administrador registra un proyecto

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | Modelo `Proyecto` (nombre, ruta, carpeta de Claude Code, dos límites, activo, fechas) y su migración | `proyectos/cimiento/core/proyectos/__init__.py`, `proyectos/cimiento/core/proyectos/apps.py`, `proyectos/cimiento/core/proyectos/models.py`, `proyectos/cimiento/core/proyectos/migrations/__init__.py`, `proyectos/cimiento/core/proyectos/migrations/0001_initial.py`, `proyectos/cimiento/config/settings/base.py` | CA-01 | La base | 1 h | Ninguna | CP-001 |
| T-02 | `carpeta_de_claude(ruta)` | `proyectos/cimiento/core/proyectos/claude.py` | CA-01 | HU-006 la usa | 0,5 h | Ninguna | CP-001 |
| T-03 | Lista y registro; «Proyectos» en el menú | `proyectos/cimiento/core/proyectos/forms.py`, `proyectos/cimiento/core/proyectos/views.py`, `proyectos/cimiento/core/proyectos/urls.py`, `proyectos/cimiento/core/proyectos/templates/proyectos/lista.html`, `proyectos/cimiento/core/proyectos/templates/proyectos/formulario.html`, `proyectos/cimiento/config/urls.py`, `proyectos/cimiento/templates/base.html` | CA-01 | Cimiento | 1,5 h | T-01, T-02 | CP-001 |

### CA-02 · Lo que no vale no se guarda

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-04 | Validación de ruta existente y no repetida, nombre único y límites mayores que cero | `proyectos/cimiento/core/proyectos/models.py`, `proyectos/cimiento/core/proyectos/forms.py` | CA-02 | El registro | 1 h | T-01 | CP-002 |

### CA-03 · Un proyecto se edita y se desactiva

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-05 | Edición con el mismo formulario, con «Activo» | `proyectos/cimiento/core/proyectos/views.py`, `proyectos/cimiento/core/proyectos/urls.py` | CA-03 | El registro | 0,5 h | T-03 | CP-003 |

### CA-04 · El grupo consulta solo ve

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-06 | Registro y edición con `SoloAdministrador`; la lista muestra los botones solo a administradores | `proyectos/cimiento/core/proyectos/views.py`, `proyectos/cimiento/core/proyectos/templates/proyectos/lista.html` | CA-04 | El registro | 0,5 h | T-03 | CP-004 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-07 | Pruebas; fila de la fase en la HU y estado en la épica | `proyectos/cimiento/core/proyectos/tests.py`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-003-los-proyectos-quedan-registrados-en-cimiento/HU-003-los-proyectos-quedan-registrados-en-cimiento.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | CA-01 a CA-04 | Documentación | 1 h | T-01 a T-06 | CP-001 a CP-004 |

### Ciclo 2 · D-01, la tabla de la plataforma vieja  ·  orden del usuario del 2026-10-05

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-08 | Migración de datos `0002`: trae los proyectos de `plantillas/proyectos.md` cuya carpeta existe; en la base de pruebas no trae nada | `proyectos/cimiento/core/proyectos/registro.py`, `proyectos/cimiento/core/proyectos/migrations/0002_proyectos_existentes.py`, `proyectos/cimiento/core/proyectos/tests_registro.py` | D-01 | La base | 1 h | T-01 | CP-001 |
| T-09 | `manage.py registrar`, y el instalador la llama en vez de `interfaz/manage.py registrar`; la fila de `proyectos.md` se sigue escribiendo | `proyectos/cimiento/core/proyectos/management/__init__.py`, `proyectos/cimiento/core/proyectos/management/commands/__init__.py`, `proyectos/cimiento/core/proyectos/management/commands/registrar.py`, `proyectos/cimiento/core/herramientas/instalar.py`, `validadores/instalar.py` | D-01 | El instalador | 1 h | T-08 | CP-001 |
| T-10 | Respaldo de la base en `cimiento_respaldo_20261005`, borrar `cimiento` y crearla con `preparar_base` | La base `cimiento` | D-01 | Datos locales | 0,5 h | T-08, T-09 | CP-001 |

## 4. Secuencia de ejecución

T-01 y T-02; T-03, T-04, T-05, T-06 y al final T-07, con las pruebas de la fase (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Registrar por la pantalla; el cálculo de la carpeta con rutas conocidas | CP-001 |
| CA-02 | Cada dato inválido, uno por uno | CP-002 |
| CA-03 | Editar un límite y desactivar | CP-003 |
| CA-04 | Lista y formularios pedidos por consulta | CP-004 |

## 6. Datos y ambiente de prueba

La base de pruebas en MariaDB; carpetas temporales como rutas de proyecto.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase y `manage.py migrate proyectos zero`.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Aditiva: tabla nueva.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`04`, `03`, `14·EST1`, `02·F4`, `02·F5`, `02·F8`, `00·ID8`, `00·ID9`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Claude Code cambie cómo nombra la carpeta | La regla vive en `carpeta_de_claude`, con su prueba |

## 11. Definition of Done

- [x] CA-01 a CA-04 con veredicto y evidencia en `resultado_pruebas.md`.
- [x] Las pruebas de la fase sin fallas, y cero marcas nuevas.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 7 tareas quedaron hechas el 2026-10-04, con la versión 54.2.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Ciclo 2, 2026-10-05.** T-08 a T-10 hechas: corrigen D-01 (H-6 del resumen del 2026-10-04, sesión 3).

**Hallazgos al ejecutar:** D-01, la tabla de la plataforma vieja con la misma etiqueta.
