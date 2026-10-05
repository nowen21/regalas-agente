# Plan de Trabajo · Fase `A-EP-025-HU-001-mariadb-y-plantilla-comun` (módulo `proyectos/cimiento/` y `plantillas/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-001-mariadb-y-plantilla-comun` |
| **Épica** | [EP-025](../../epica.md) |
| **HU** | [HU-001](../HU-001-cimiento-corre-sobre-mariadb-y-tiene-la-base-de-sus-pantallas.md), una sola (`F12.1`) |
| **Módulo** | `proyectos/cimiento/`, `plantillas/`, `validadores/instalar.py` |
| **Especificación del módulo** | Los CA de la [HU-001](../HU-001-cimiento-corre-sobre-mariadb-y-tiene-la-base-de-sus-pantallas.md) |
| **Fecha apertura** | 2026-10-04 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva. Sale de los puntos 2, 3 y 11 del [análisis 1 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md) (acuerdos 3, 5, 6 y 15).

**Carencias que cierra** (`02·F14` Q3): Cimiento corre sobre SQLite, no tiene pantallas propias y la plantilla Django del estándar no admite dependencias de npm.

**Aprobación** (`02·F4`): [análisis 1 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md), el 2026-10-04, con la versión 54.0.0

**Disparo** (`02·F15`, etapa 2): el usuario aprobó el análisis el 2026-10-04 («Apruebo el análisis») y pidió seguir con «Continúe con el pendiente 119».

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-001 | Estado |
|---|---|
| CA-01 · Cimiento guarda en MariaDB con la conexión del `.env` | ☑ |
| CA-02 · Sin MariaDB, Cimiento dice qué hacer | ☑ |
| CA-03 · La plantilla de estructura Django admite dependencias de npm | ☑ |
| CA-04 · Las pantallas tienen su plantilla común | ☑ |
| CA-05 · La instalación prepara Cimiento | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que Cimiento guarde en MariaDB, tenga una plantilla común para sus pantallas con Tabler, htmx y ApexCharts, y que la instalación lo deje listo.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | La base se crea y migra con la conexión del `.env` | Programa | Baja |
| CA-02 | MariaDB apagada | Programa | Media |
| CA-03 | npm en la plantilla Django | Plantilla | Baja |
| CA-04 | Plantilla común y página de inicio | Programa | Media |
| CA-05 | La instalación prepara Cimiento | Programa | Media |

**Fuera de alcance:** la entrada con usuario (HU-002) y que el freno lea la base (HU-005).

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-10-04, sobre la versión 54.0.0:

- `config/settings/base.py` ya apunta a `django.db.backends.mysql` con las variables `DB_*`, pero su comentario sigue diciendo «Un archivo local»; `requirements/base.txt` ya trae `mysqlclient` y `lock.txt` no. El `.env` de esta máquina ya trae la conexión; `.env.example` no la lista.
- El `.venv` de Cimiento tiene `mysqlclient` 2.3.0 y Django 5.2.17. `manage.py check --database default` conecta con MariaDB 11.4.9 y ninguna migración está aplicada.
- `INSTALLED_APPS` solo tiene las aplicaciones de Django; `config/urls.py` solo tiene `admin/`; `templates/` y `static/` están vacías.
- `manage.py` usa `config.settings.local`, con `DEBUG = True`.
- La clase `Instalador` (`core/herramientas/instalar.py`) instala por pasos; en la carpeta del propio estándar pone los enganches de git y de Claude Code y después el histórico y la memoria. `validadores/instalar.py` es la orden que corre el usuario y todavía tiene su propia copia de los pasos (fila 21 del análisis 1 del pendiente 116).
- npm 11.6.2; versiones vigentes: `@tabler/core` 1.6.1, `htmx.org` 2.0.11, `apexcharts` 7.8.0.
- `plantillas/estructura-proyecto-django.md` dice que las dependencias se instalan con pip y que no hay `static/vendor/`.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `plantillas/estructura-proyecto-django.md` | Modificar | Plantilla | npm en el árbol y en «Dependencias» |
| `CHANGELOG.md`, `VERSION` | Modificar | Versión | MENOR: 54.2.0 |
| `.gitignore` | Modificar | Configuración | `proyectos/*/node_modules/` |
| `proyectos/cimiento/.env.example` | Modificar | Configuración | Las variables `DB_*`, sin valores |
| `proyectos/cimiento/config/settings/base.py` | Modificar | Configuración | Comentario de la base, la aplicación `core.inicio`, el middleware y los `dist` de npm en `STATICFILES_DIRS` |
| `proyectos/cimiento/config/urls.py` | Modificar | Configuración | La ruta de inicio |
| `proyectos/cimiento/requirements/base.txt`, `proyectos/cimiento/requirements/lock.txt` | Modificar | Dependencias | `mysqlclient` con versión |
| `proyectos/cimiento/package.json`, `proyectos/cimiento/package-lock.json` | Crear | Dependencias | Tabler, htmx y ApexCharts con versión exacta |
| `proyectos/cimiento/README.md` | Modificar | Documentación | MariaDB, `npm ci` y `preparar_base` en los pasos |
| `proyectos/cimiento/core/inicio/__init__.py`, `proyectos/cimiento/core/inicio/apps.py`, `proyectos/cimiento/core/inicio/base_de_datos.py`, `proyectos/cimiento/core/inicio/middleware.py`, `proyectos/cimiento/core/inicio/views.py`, `proyectos/cimiento/core/inicio/urls.py`, `proyectos/cimiento/core/inicio/tests.py` | Crear | Programa | El módulo de inicio |
| `proyectos/cimiento/core/inicio/management/__init__.py`, `proyectos/cimiento/core/inicio/management/commands/__init__.py`, `proyectos/cimiento/core/inicio/management/commands/preparar_base.py` | Crear | Programa | La orden que crea la base y migra |
| `proyectos/cimiento/core/inicio/templates/inicio/inicio.html`, `proyectos/cimiento/core/inicio/templates/inicio/base_apagada.html` | Crear | Pantalla | La página de inicio y la de base apagada |
| `proyectos/cimiento/templates/base.html` | Crear | Pantalla | La plantilla común: menú lateral y cabecera |
| `proyectos/cimiento/core/herramientas/instalar.py`, `proyectos/cimiento/core/herramientas/tests_instalacion.py` | Modificar | Programa | `Instalador.preparar_cimiento()` y sus pruebas |
| `validadores/instalar.py` | Modificar | Programa | Llama a `Instalador.preparar_cimiento()` en la carpeta del estándar |
| `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-001-cimiento-corre-sobre-mariadb-y-tiene-la-base-de-sus-pantallas/HU-001-cimiento-corre-sobre-mariadb-y-tiene-la-base-de-sus-pantallas.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | Modificar | Documentación | La fila de la fase y el estado |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| La base pasa de SQLite a MariaDB | Las pruebas de `core/` | Son `unittest.TestCase` y no abren la base: siguen igual |
| `Instalador.instalar()` suma un paso | `hook_sesion.py` (solo comprueba), `tests_instalacion.py` | El paso solo corre en la carpeta del estándar, y en simulación no ejecuta nada |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

| Ruta | Vista | Acceso |
|---|---|---|
| `/` | `core.inicio.views.Inicio` | Abierta en esta fase; la HU-002 la protege |

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

`http://127.0.0.1:«PUERTO»/`, con «Inicio» en el menú lateral.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno: los grupos llegan con la HU-002.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Django usa `mysqlclient`; el freno usará `PyMySQL` | Un solo controlador para los dos | `mysqlclient` es el que Django soporta; el freno no arranca Django | Acuerdo 15 |
| `preparar_base` crea la base con `CREATE DATABASE IF NOT EXISTS` y llama a `migrate` | Crearla a mano | La instalación la tiene que dejar lista, y repetirla no cambia nada | Acuerdo 15, punto 11 |
| `STATICFILES_DIRS` apunta solo a la carpeta `dist` de cada paquete, sin prefijo | Todo `node_modules/`; con prefijo, que Django no sirve en Windows (señal S-299) | Django solo ve lo que se usa en el navegador | Acuerdo 6 |
| Un middleware muestra la página de base apagada en cualquier pantalla | Atrapar el error en cada vista | Las pantallas de las demás HU lo heredan sin hacer nada | Acuerdo 15 |
| El paso nuevo va en `Instalador` y `validadores/instalar.py` lo llama | Escribirlo dos veces | Lo nuevo va como clase en Cimiento | Análisis 1 del pendiente 116, acuerdo 8 |
| La preparación corre antes de los enganches, y sin MariaDB queda como pendiente sin detener lo demás | Detener la instalación | La instalación no pregunta ni se cae; reporta lo que exige al usuario | Acuerdo 15 |
| Versión MENOR | MAYOR | La plantilla admite npm, pero ningún proyecto tiene que hacer nada | «El entorno» del análisis |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| Base de Cimiento | SQLite en el comentario, MariaDB a medias en el código | MariaDB `cimiento`, creada y migrada | `00·N6` |
| Pantallas | Solo el administrador de Django | Plantilla común y página de inicio | Acuerdo 3 |
| Plantilla Django | Solo pip | pip y npm | `10·DEP2` |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-01 · Cimiento guarda en MariaDB con la conexión del `.env`

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | Comentario de la base; `.env.example` con las `DB_*`; `mysqlclient` con versión en `base.txt` y `lock.txt` | `proyectos/cimiento/config/settings/base.py`, `proyectos/cimiento/.env.example`, `proyectos/cimiento/requirements/base.txt`, `proyectos/cimiento/requirements/lock.txt` | CA-01 | Cimiento | 0,5 h | Ninguna | CP-001 |
| T-02 | Módulo `core/inicio/` con `BaseDeDatos` (responde, crea si falta, versión) y la orden `preparar_base` | `proyectos/cimiento/core/inicio/` | CA-01, CA-02 | Cimiento | 1,5 h | T-01 | CP-001, CP-002 |

### CA-02 · Sin MariaDB, Cimiento dice qué hacer

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-03 | Middleware `BaseApagada`: ante un `OperationalError`, la página `base_apagada.html` con servidor y puerto, código 503 | `proyectos/cimiento/core/inicio/middleware.py`, `proyectos/cimiento/core/inicio/templates/inicio/base_apagada.html`, `proyectos/cimiento/config/settings/base.py` | CA-02 | Toda pantalla | 1 h | T-02 | CP-002 |

### CA-03 · La plantilla de estructura Django admite dependencias de npm

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-04 | El árbol suma `package.json`, `package-lock.json` y `node_modules/`; «Dependencias» explica npm; versión 54.2.0 | `plantillas/estructura-proyecto-django.md`, `CHANGELOG.md`, `VERSION` | CA-03 | Todo proyecto Django | 0,5 h | Ninguna | CP-003 |

### CA-04 · Las pantallas tienen su plantilla común

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-05 | `package.json` con versiones exactas y `npm install` para el `package-lock.json`; `node_modules/` en `.gitignore`; los `dist` en `STATICFILES_DIRS` | `proyectos/cimiento/package.json`, `proyectos/cimiento/package-lock.json`, `.gitignore`, `proyectos/cimiento/config/settings/base.py` | CA-04 | Cimiento | 0,5 h | Ninguna | CP-004 |
| T-06 | `templates/base.html` con menú lateral y cabecera; la vista `Inicio` en `/` con la base y su versión | `proyectos/cimiento/templates/base.html`, `proyectos/cimiento/core/inicio/views.py`, `proyectos/cimiento/core/inicio/urls.py`, `proyectos/cimiento/core/inicio/templates/inicio/inicio.html`, `proyectos/cimiento/config/urls.py` | CA-04 | Todas las pantallas de la épica | 1,5 h | T-02, T-05 | CP-004 |

### CA-05 · La instalación prepara Cimiento

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-07 | `Instalador.preparar_cimiento(aplicar)`: si falta `node_modules/`, `npm ci`; después `manage.py preparar_base` con el Python del `.venv`; lo que falle queda como pendiente. Corre antes de los enganches, solo en la carpeta del estándar | `proyectos/cimiento/core/herramientas/instalar.py`, `validadores/instalar.py` | CA-05 | La instalación del estándar | 1,5 h | T-02, T-05 | CP-005 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-08 | Pruebas de `core/inicio/` y de la preparación; README de Cimiento; fila de la fase en la HU y estado en la épica | `proyectos/cimiento/core/inicio/tests.py`, `proyectos/cimiento/core/herramientas/tests_instalacion.py`, `proyectos/cimiento/README.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-001-cimiento-corre-sobre-mariadb-y-tiene-la-base-de-sus-pantallas/HU-001-cimiento-corre-sobre-mariadb-y-tiene-la-base-de-sus-pantallas.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | CA-01 a CA-05 | Documentación | 1 h | T-01 a T-07 | CP-001 a CP-005 |

## 4. Secuencia de ejecución

T-01, T-02, T-03; T-04 y T-05 en cualquier orden; T-06, T-07 y al final T-08, con las pruebas de la fase y la medición de marcas (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | `preparar_base` y `showmigrations` contra MariaDB; leer `.env.example` | CP-001 |
| CA-02 | `preparar_base` con un puerto sin servidor; la pantalla con la base apagada | CP-002 |
| CA-03 | Leer la plantilla, `CHANGELOG.md` y `VERSION` | CP-003 |
| CA-04 | Abrir `/` con el servidor corriendo; pruebas de la página | CP-004 |
| CA-05 | Simular la instalación del estándar; pruebas de la preparación | CP-005 |

## 6. Datos y ambiente de prueba

MariaDB 11.4.9 en `127.0.0.1:3307`, base `cimiento`. El `.venv` de Cimiento. Para la base apagada, el puerto 3399, donde no hay servidor.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase. La base `cimiento` se puede borrar sin perder nada: solo tiene las tablas de Django.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Aditiva: SQLite no tenía datos propios (épica, §16). Para los proyectos que heredan, la plantilla solo suma una opción.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`00·N6`, `10·DEP2`, `14·EST1`, `20·M10`, `02·F4`, `02·F5`, `02·F8`, `00·ID8`, `00·ID9`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| MariaDB apagada al correr las pruebas | Las pruebas de esta fase no abren la base real; la de base apagada usa un puerto sin servidor |
| `npm ci` falla sin internet | La instalación lo deja como pendiente y sigue |

## 11. Definition of Done

- [x] CA-01 a CA-05 con veredicto y evidencia en `resultado_pruebas.md`.
- [x] Las pruebas de la fase sin fallas, y cero marcas nuevas.
- [x] `VERSION` y `CHANGELOG.md` al día.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 8 tareas quedaron hechas el 2026-10-04, con la versión 54.2.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** 1. Con prefijo en `STATICFILES_DIRS`, Django no servía los estáticos en Windows; se quitó el prefijo dentro de los mismos archivos (señal S-299). 2. `node_modules/` se creó antes de quedar en `.gitignore`, y el freno avisó por cada archivo (pendiente 120). 3. Otra sesión dejó un ciclo de importación en Cimiento; `validadores/instalar.py` importa `core.validadores` primero (pendiente 121). 4. Otra sesión publicó la 54.1.0 al mismo tiempo; esta fase quedó como 54.2.0.
