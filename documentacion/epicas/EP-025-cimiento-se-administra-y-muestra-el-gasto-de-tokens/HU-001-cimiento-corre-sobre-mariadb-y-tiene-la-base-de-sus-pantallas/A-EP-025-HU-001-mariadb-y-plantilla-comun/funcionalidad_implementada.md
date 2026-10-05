# Funcionalidad implementada · Fase `A-EP-025-HU-001-mariadb-y-plantilla-comun` (módulo `proyectos/cimiento/` y `plantillas/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-001-mariadb-y-plantilla-comun` |
| **Módulo** | `proyectos/cimiento/`, `plantillas/`, `validadores/instalar.py` |
| **Especificación del módulo** | Los CA de la [HU-001](../HU-001-cimiento-corre-sobre-mariadb-y-tiene-la-base-de-sus-pantallas.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-001 (CA-01 a CA-05) |
| **Fecha de cierre** | 2026-10-04 |
| **Versión del estándar al cerrar** | 54.2.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Cimiento guarda en MariaDB `cimiento` con la conexión del `.env`. `manage.py preparar_base` crea la base si falta y la migra, y si MariaDB no responde dice que hay que prenderla. Las pantallas tienen una plantilla común con menú lateral y cabecera, hecha con Tabler, htmx y ApexCharts instalados con npm, y una página de inicio que dice a qué base está conectado Cimiento. La instalación del estándar prepara Cimiento antes de poner los enganches, y la plantilla de estructura Django admite dependencias de npm.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Programa | `proyectos/cimiento/config/settings/base.py`, `proyectos/cimiento/.env.example`, `proyectos/cimiento/core/inicio/base_de_datos.py`, `proyectos/cimiento/core/inicio/management/commands/preparar_base.py` | ✅ | CP-001 |
| CA-02 | Programa | `proyectos/cimiento/core/inicio/middleware.py`, `proyectos/cimiento/core/inicio/templates/inicio/base_apagada.html` | ✅ | CP-002 |
| CA-03 | Plantilla | `plantillas/estructura-proyecto-django.md`, `CHANGELOG.md`, `VERSION` | ✅ | CP-003 |
| CA-04 | Pantalla | `proyectos/cimiento/package.json`, `proyectos/cimiento/templates/base.html`, `proyectos/cimiento/core/inicio/views.py`, `proyectos/cimiento/core/inicio/templates/inicio/inicio.html` | ✅ | CP-004 |
| CA-05 | Programa | `proyectos/cimiento/core/herramientas/instalar.py`, `validadores/instalar.py` | ✅ | CP-005 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 8 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

En `proyectos/cimiento/`: `npm ci`, `.venv\Scripts\python manage.py preparar_base` y `.venv\Scripts\python manage.py runserver`; la página queda en `http://127.0.0.1:«PUERTO del .env»/`. Una pantalla nueva extiende `templates/base.html` y llena los bloques `menu`, `cabecera` y `contenido`.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Las carpetas `dist` de npm van sin prefijo en `STATICFILES_DIRS` | Con prefijo, Django no las sirve en Windows | S-299 |
| `DB_NOMBRE`, `DB_USUARIO`, `DB_SERVIDOR` y `DB_PUERTO` se leen con `or` y no con el valor por defecto de `get` | Una variable copiada de `.env.example` sin llenar llega vacía, y vacía no es un nombre de base | No hace falta: está en el comentario |
| La conexión fija InnoDB y `preparar_base` convierte lo que esté en otro motor | El MariaDB de WAMP crea las tablas con MyISAM, sin transacciones | S-300 |
| La base apagada la atiende un middleware | Las pantallas de las demás HU lo heredan sin escribir nada | No hace falta |

## 6. Deuda técnica y pendientes generados

- [Pendiente 121](../../../../../historico-chat/resumenes/2026-10-04/pendientes/121-importar-el-instalador-de-cimiento-cae-en-un-ciclo/pendiente.md): el instalador de Cimiento solo se importa después de `core.validadores`.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] `CHANGELOG.md` y `VERSION`.
- [x] `proyectos/cimiento/README.md`.

## 8. Despliegue, si aplica  ·  `13·DOC4`

En esta máquina, al instalar el estándar en su propia carpeta. Los proyectos que heredan reciben la plantilla al adoptar la 54.2.0.
