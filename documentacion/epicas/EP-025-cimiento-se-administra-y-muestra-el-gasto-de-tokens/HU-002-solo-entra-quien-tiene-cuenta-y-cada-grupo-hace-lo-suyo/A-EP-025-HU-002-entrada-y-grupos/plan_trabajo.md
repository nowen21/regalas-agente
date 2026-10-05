# Plan de Trabajo · Fase `A-EP-025-HU-002-entrada-y-grupos` (módulo `proyectos/cimiento/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-002-entrada-y-grupos` |
| **Épica** | [EP-025](../../epica.md) |
| **HU** | [HU-002](../HU-002-solo-entra-quien-tiene-cuenta-y-cada-grupo-hace-lo-suyo.md), una sola (`F12.1`) |
| **Módulo** | `proyectos/cimiento/` |
| **Especificación del módulo** | Los CA de la [HU-002](../HU-002-solo-entra-quien-tiene-cuenta-y-cada-grupo-hace-lo-suyo.md) |
| **Fecha apertura** | 2026-10-04 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva. Sale del punto 12 del [análisis 1 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md) (acuerdo 14).

**Carencias que cierra** (`02·F14` Q3): las pantallas de Cimiento están abiertas a quien abra la dirección.

**Aprobación** (`02·F4`): [análisis 1 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md), el 2026-10-04, con la versión 54.2.0

**Disparo** (`02·F15`, etapa 2): el usuario aprobó el análisis el 2026-10-04 y pidió seguir con «Continúe con el pendiente 119».

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-002 | Estado |
|---|---|
| CA-01 · Sin cuenta, se pide entrar | ☑ |
| CA-02 · Una contraseña equivocada no deja entrar | ☑ |
| CA-03 · El grupo consulta no puede cambiar nada | ☑ |
| CA-04 · Las cuentas se crean con una orden | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que a Cimiento solo entre quien tiene cuenta, y que las pantallas de administración tengan con qué negarle el paso al grupo consulta.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Entrada obligatoria | Programa | Media |
| CA-02 | Contraseña equivocada | Programa | Baja |
| CA-03 | Permiso por grupo | Programa | Media |
| CA-04 | Orden `crear_cuenta` y los dos grupos | Programa | Baja |

**Fuera de alcance:** una pantalla para administrar cuentas; recuperar la contraseña.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-10-04, sobre la versión 54.2.0:

- Django 5.2.17 trae `django.contrib.auth.middleware.LoginRequiredMiddleware`: manda a `LOGIN_URL` toda vista que no esté marcada con `login_not_required`; `LoginView` ya viene marcada.
- `core/inicio/middleware.py` (HU-001) atiende la base apagada en `process_exception`, que solo ve los errores de la vista. Con la entrada obligatoria, el error de base apagada sale antes, al revisar la sesión en `LoginRequiredMiddleware.process_view`, y Django lo convierte en una página de error 500.
- Las pruebas de `core/inicio/tests.py` piden `/` sin cuenta y esperan 200; con la entrada obligatoria reciben la redirección.
- `templates/base.html` no muestra la cuenta.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/cuentas/__init__.py`, `proyectos/cimiento/core/cuentas/apps.py`, `proyectos/cimiento/core/cuentas/permisos.py`, `proyectos/cimiento/core/cuentas/urls.py`, `proyectos/cimiento/core/cuentas/tests.py` | Crear | Programa | El módulo de cuentas |
| `proyectos/cimiento/core/cuentas/migrations/__init__.py`, `proyectos/cimiento/core/cuentas/migrations/0001_grupos.py` | Crear | Datos | Crea los grupos `administrador` y `consulta` |
| `proyectos/cimiento/core/cuentas/management/__init__.py`, `proyectos/cimiento/core/cuentas/management/commands/__init__.py`, `proyectos/cimiento/core/cuentas/management/commands/crear_cuenta.py` | Crear | Programa | La orden que crea una cuenta en un grupo |
| `proyectos/cimiento/core/cuentas/templates/cuentas/entrar.html`, `proyectos/cimiento/core/cuentas/templates/cuentas/sin_permiso.html` | Crear | Pantalla | La página de entrada y la de 403 |
| `proyectos/cimiento/config/settings/base.py` | Modificar | Configuración | La aplicación, `LoginRequiredMiddleware` después de la revisión de la base, `LOGIN_URL` y las redirecciones |
| `proyectos/cimiento/config/urls.py` | Modificar | Configuración | Las rutas de entrada y salida |
| `proyectos/cimiento/core/inicio/middleware.py` | Modificar | Programa | `process_view` revisa la base antes que la entrada |
| `proyectos/cimiento/core/inicio/templates/inicio/base_apagada.html` | Modificar | Pantalla | Se ve sin entrar: no extiende la plantilla que muestra la cuenta |
| `proyectos/cimiento/core/inicio/tests.py` | Modificar | Pruebas | La página se pide con una cuenta |
| `proyectos/cimiento/templates/base.html` | Modificar | Pantalla | La cuenta y «Salir» en la cabecera |
| `proyectos/cimiento/README.md` | Modificar | Documentación | Cómo crear la primera cuenta |
| `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-002-solo-entra-quien-tiene-cuenta-y-cada-grupo-hace-lo-suyo/HU-002-solo-entra-quien-tiene-cuenta-y-cada-grupo-hace-lo-suyo.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | Modificar | Documentación | La fila de la fase y el estado |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| `BaseApagada` suma `process_view` | Toda pantalla | Revisa la base una vez por petición, antes que la entrada |
| `base_apagada.html` deja de extender `base.html` | `BaseApagada` | Carga la hoja de Tabler por su cuenta |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

| Ruta | Vista | Acceso |
|---|---|---|
| `/entrar/` | `LoginView` de Django | Abierta |
| `/salir/` | `LogoutView` de Django, por POST | Con cuenta |
| `/` y las demás | Las de cada módulo | Con cuenta |

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

`/entrar/`; «Salir» en la cabecera de toda pantalla.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Los grupos `administrador` y `consulta`, sin permisos de modelo todavía: las HU siguientes agregan los suyos.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| `LoginRequiredMiddleware` de Django | `login_required` en cada vista | Una pantalla nueva nace protegida sin acordarse | Acuerdo 14 |
| Un superusuario cuenta como administrador | Exigir que esté en el grupo | La primera cuenta se crea con `createsuperuser`, que no pone grupo | Propuesta del agente |
| `SoloAdministrador` responde 403 con una página sin datos | Mandar a la entrada | La cuenta ya entró: lo que le falta es permiso | `04` |
| La base se revisa en `process_view` de `BaseApagada`, antes de `LoginRequiredMiddleware` | Solo `process_exception` | Con la entrada obligatoria, la sesión se lee antes de la vista y su error no llega a `process_exception` | Acuerdo 15 |
| `crear_cuenta` pide la contraseña sin mostrarla | Pasarla como argumento | Una contraseña en la orden queda en el historial de la consola (`00·N6`) | `00·N6` |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| Pantallas de Cimiento | Abiertas | Con cuenta; las de administración, solo para administradores | `04` |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-01 · Sin cuenta, se pide entrar

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | Módulo `core/cuentas/` con entrada y salida; `LoginRequiredMiddleware`; `LOGIN_URL` y redirecciones | `proyectos/cimiento/core/cuentas/__init__.py`, `proyectos/cimiento/core/cuentas/apps.py`, `proyectos/cimiento/core/cuentas/urls.py`, `proyectos/cimiento/core/cuentas/templates/cuentas/entrar.html`, `proyectos/cimiento/config/settings/base.py`, `proyectos/cimiento/config/urls.py` | CA-01 | Toda pantalla | 1 h | Ninguna | CP-001 |
| T-02 | La cuenta y «Salir» en la cabecera | `proyectos/cimiento/templates/base.html` | CA-01 | Toda pantalla | 0,5 h | T-01 | CP-001 |
| T-03 | `BaseApagada.process_view` revisa la base antes de la entrada; `base_apagada.html` sin la cuenta | `proyectos/cimiento/core/inicio/middleware.py`, `proyectos/cimiento/core/inicio/templates/inicio/base_apagada.html` | CA-01 | Toda pantalla | 0,5 h | T-01 | CP-001 |

### CA-02 · Una contraseña equivocada no deja entrar

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-04 | El mensaje de error de la entrada, igual para usuario inexistente y contraseña equivocada | `proyectos/cimiento/core/cuentas/templates/cuentas/entrar.html` | CA-02 | La entrada | 0,5 h | T-01 | CP-002 |

### CA-03 · El grupo consulta no puede cambiar nada

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-05 | `es_administrador(cuenta)` y la mezcla `SoloAdministrador`, que responde 403 | `proyectos/cimiento/core/cuentas/permisos.py`, `proyectos/cimiento/core/cuentas/templates/cuentas/sin_permiso.html` | CA-03 | Las pantallas de HU-003 en adelante | 1 h | T-06 | CP-003 |

### CA-04 · Las cuentas se crean con una orden

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-06 | Migración que crea los dos grupos | `proyectos/cimiento/core/cuentas/migrations/__init__.py`, `proyectos/cimiento/core/cuentas/migrations/0001_grupos.py` | CA-04 | La base | 0,5 h | T-01 | CP-004 |
| T-07 | Orden `crear_cuenta --usuario U --grupo G`, con la contraseña pedida dos veces sin mostrarse | `proyectos/cimiento/core/cuentas/management/__init__.py`, `proyectos/cimiento/core/cuentas/management/commands/__init__.py`, `proyectos/cimiento/core/cuentas/management/commands/crear_cuenta.py` | CA-04 | Cimiento | 1 h | T-06 | CP-004 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-08 | Pruebas de cuentas; las de inicio piden la página con una cuenta; README; fila de la fase en la HU y estado en la épica | `proyectos/cimiento/core/cuentas/tests.py`, `proyectos/cimiento/core/inicio/tests.py`, `proyectos/cimiento/README.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-002-solo-entra-quien-tiene-cuenta-y-cada-grupo-hace-lo-suyo/HU-002-solo-entra-quien-tiene-cuenta-y-cada-grupo-hace-lo-suyo.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | CA-01 a CA-04 | Documentación | 1 h | T-01 a T-07 | CP-001 a CP-004 |

## 4. Secuencia de ejecución

T-01, T-06, T-02, T-03, T-04, T-05, T-07 y al final T-08, con las pruebas de la fase (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Pedir `/` sin cuenta y con cuenta; la base apagada sin cuenta | CP-001 |
| CA-02 | Entrar con contraseña equivocada y con usuario inexistente | CP-002 |
| CA-03 | Una vista de prueba con `SoloAdministrador`, pedida por consulta, administrador y superusuario | CP-003 |
| CA-04 | Los grupos después de migrar; `crear_cuenta` con contraseña coincidente y no coincidente | CP-004 |

## 6. Datos y ambiente de prueba

La base de pruebas que Django crea en MariaDB (`test_cimiento`), con cuentas de prueba creadas en cada caso.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase y `manage.py migrate cuentas zero`, que borra los dos grupos.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Aditiva: la migración solo crea dos grupos. Sin cuentas, nadie entra hasta correr `createsuperuser`; lo dice el README.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`00·N6`, `04`, `14·EST1`, `02·F4`, `02·F5`, `02·F8`, `00·ID8`, `00·ID9`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Las pruebas necesitan MariaDB prendida | Lo dice el README; la de base apagada sustituye la conexión |

## 11. Definition of Done

- [x] CA-01 a CA-04 con veredicto y evidencia en `resultado_pruebas.md`.
- [x] Las pruebas de la fase sin fallas, y cero marcas nuevas.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 8 tareas quedaron hechas el 2026-10-04, con la versión 54.2.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** 1. Las tablas de MariaDB eran MyISAM; se corrigió en la fase de la HU-001, que declara esos archivos (señal S-300). 2. La plantilla `sin_permiso.html` se agregó al plan antes de crearla.
