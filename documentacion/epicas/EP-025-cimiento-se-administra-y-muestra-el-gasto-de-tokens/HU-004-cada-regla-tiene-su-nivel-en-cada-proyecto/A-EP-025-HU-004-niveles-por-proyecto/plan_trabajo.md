# Plan de Trabajo · Fase `A-EP-025-HU-004-niveles-por-proyecto` (módulo `proyectos/cimiento/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-004-niveles-por-proyecto` |
| **Épica** | [EP-025](../../epica.md) |
| **HU** | [HU-004](../HU-004-cada-regla-tiene-su-nivel-en-cada-proyecto.md), una sola (`F12.1`) |
| **Módulo** | `proyectos/cimiento/` |
| **Especificación del módulo** | Los CA de la [HU-004](../HU-004-cada-regla-tiene-su-nivel-en-cada-proyecto.md) |
| **Fecha apertura** | 2026-10-04 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva. Sale del punto 13 del [análisis 1 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md) (acuerdos 12 y 13).

**Carencias que cierra** (`02·F14` Q3): ajustar una regla obliga a cambiar código y afecta a todos los proyectos.

**Aprobación** (`02·F4`): [análisis 1 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md), el 2026-10-04, con la versión 54.2.0

**Disparo** (`02·F15`, etapa 2): el usuario aprobó el análisis el 2026-10-04 y pidió seguir con «Continúe con el pendiente 119».

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-004 | Estado |
|---|---|
| CA-01 · Un administrador cambia el nivel de una regla en un proyecto | ☑ |
| CA-02 · Las reglas del núcleo no se pueden cambiar | ☑ |
| CA-03 · Cada cambio queda registrado | ☑ |
| CA-04 · El grupo consulta solo ve los niveles | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** guardar por proyecto el nivel de cada regla, con su historial, y cambiarlo en una pantalla.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Cambiar un nivel | Programa | Media |
| CA-02 | Núcleo y nivel inválido | Programa | Baja |
| CA-03 | Historial | Programa | Baja |
| CA-04 | Permiso por grupo | Programa | Baja |

**Fuera de alcance:** que el freno lea el nivel (HU-005).

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-10-04, sobre la versión 54.2.0:

- `CuerpoDeReglas.leer()` (`core/validadores/metareglas.py`) devuelve las 268 reglas de `base/`, cada una con `capitulo`, `id`, `titulo` y `derogada`; 10 son del núcleo (`00·N…`).
- Importar `core.validadores.metareglas` exige importar `core.validadores` primero, por el ciclo del pendiente 121.
- `core/proyectos/` (HU-003) tiene el modelo `Proyecto` y la lista en `/proyectos/`.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/niveles/__init__.py`, `proyectos/cimiento/core/niveles/apps.py`, `proyectos/cimiento/core/niveles/models.py`, `proyectos/cimiento/core/niveles/catalogo.py`, `proyectos/cimiento/core/niveles/views.py`, `proyectos/cimiento/core/niveles/urls.py`, `proyectos/cimiento/core/niveles/tests.py` | Crear | Programa | El módulo de niveles |
| `proyectos/cimiento/core/niveles/migrations/__init__.py`, `proyectos/cimiento/core/niveles/migrations/0001_initial.py` | Crear | Datos | Niveles y cambios de nivel |
| `proyectos/cimiento/core/niveles/templates/niveles/reglas.html`, `proyectos/cimiento/core/niveles/templates/niveles/historial.html` | Crear | Pantalla | Niveles e historial |
| `proyectos/cimiento/config/settings/base.py`, `proyectos/cimiento/config/urls.py` | Modificar | Configuración | La aplicación y sus rutas |
| `proyectos/cimiento/core/proyectos/templates/proyectos/lista.html` | Modificar | Pantalla | «Reglas» en cada fila |
| `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-004-cada-regla-tiene-su-nivel-en-cada-proyecto/HU-004-cada-regla-tiene-su-nivel-en-cada-proyecto.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | Modificar | Documentación | La fila de la fase y el estado |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

No aplica: no cambia contratos existentes.

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

| Ruta | Vista | Acceso |
|---|---|---|
| `/proyectos/«id»/reglas/` | Niveles, por GET | Con cuenta |
| `/proyectos/«id»/reglas/` | Guardar niveles, por POST | Administrador |
| `/proyectos/«id»/reglas/historial/` | Historial | Con cuenta |

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

«Reglas» en cada fila de la lista de proyectos.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno nuevo: el POST usa `es_administrador`.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Solo se guarda una fila por regla que no esté en «frena» o que alguien haya cambiado | Una fila por cada regla y proyecto | Sin fila, la regla frena, que es lo de hoy; la tabla queda corta y el freno consulta poco | RN-03 |
| El ID se guarda completo, `02·F8` | Capítulo e ID en dos columnas | Es como el freno nombra la regla en sus avisos | Acuerdo 13 |
| Un formulario con todas las reglas; se guardan solo las que cambiaron, en una transacción | Un envío por regla | Cambiar varias de una vez, todo o nada | `03` |
| El catálogo se lee una vez por proceso (`lru_cache`) | Leer `base/` en cada petición | 268 reglas en decenas de archivos | RNF-02 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| Nivel de una regla | Fijo en el código, igual para todos | Por proyecto, en la base de Cimiento, con historial | Acuerdo 13 |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-01 · Un administrador cambia el nivel de una regla en un proyecto

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | Modelos `NivelDeRegla` y `CambioDeNivel`, y su migración | `proyectos/cimiento/core/niveles/__init__.py`, `proyectos/cimiento/core/niveles/apps.py`, `proyectos/cimiento/core/niveles/models.py`, `proyectos/cimiento/core/niveles/migrations/__init__.py`, `proyectos/cimiento/core/niveles/migrations/0001_initial.py`, `proyectos/cimiento/config/settings/base.py` | CA-01, CA-03 | La base | 1 h | Ninguna | CP-001 |
| T-02 | Catálogo: reglas de `base/` sin núcleo ni derogadas, por capítulo | `proyectos/cimiento/core/niveles/catalogo.py` | CA-01, CA-02 | La pantalla y HU-005 | 0,5 h | Ninguna | CP-001, CP-002 |
| T-03 | Pantalla de niveles: lista por capítulo y guardado de lo que cambió; «Reglas» en la lista de proyectos | `proyectos/cimiento/core/niveles/views.py`, `proyectos/cimiento/core/niveles/urls.py`, `proyectos/cimiento/core/niveles/templates/niveles/reglas.html`, `proyectos/cimiento/config/urls.py`, `proyectos/cimiento/core/proyectos/templates/proyectos/lista.html` | CA-01 | Cimiento | 2 h | T-01, T-02 | CP-001 |

### CA-02 · Las reglas del núcleo no se pueden cambiar

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-04 | El guardado rechaza todo el envío si trae una regla fuera del catálogo o un nivel que no existe | `proyectos/cimiento/core/niveles/views.py` | CA-02 | El guardado | 0,5 h | T-03 | CP-002 |

### CA-03 · Cada cambio queda registrado

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-05 | Historial del proyecto | `proyectos/cimiento/core/niveles/views.py`, `proyectos/cimiento/core/niveles/urls.py`, `proyectos/cimiento/core/niveles/templates/niveles/historial.html` | CA-03 | Auditoría | 0,5 h | T-03 | CP-003 |

### CA-04 · El grupo consulta solo ve los niveles

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-06 | Consulta ve el nivel como texto; su POST recibe 403 | `proyectos/cimiento/core/niveles/views.py`, `proyectos/cimiento/core/niveles/templates/niveles/reglas.html` | CA-04 | El guardado | 0,5 h | T-03 | CP-004 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-07 | Pruebas; fila de la fase en la HU y estado en la épica | `proyectos/cimiento/core/niveles/tests.py`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-004-cada-regla-tiene-su-nivel-en-cada-proyecto/HU-004-cada-regla-tiene-su-nivel-en-cada-proyecto.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | CA-01 a CA-04 | Documentación | 1 h | T-01 a T-06 | CP-001 a CP-004 |

## 4. Secuencia de ejecución

T-01 y T-02; T-03, T-04, T-05, T-06 y al final T-07, con las pruebas de la fase (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Cambiar `02·F8` en un proyecto y mirar otro | CP-001 |
| CA-02 | Buscar el núcleo; enviar núcleo, regla inventada y nivel inválido | CP-002 |
| CA-03 | El historial después de un cambio | CP-003 |
| CA-04 | Lista y envío como consulta | CP-004 |

## 6. Datos y ambiente de prueba

La base de pruebas en MariaDB; dos proyectos con carpetas temporales; el catálogo real de `base/`.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase y `manage.py migrate niveles zero`.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Aditiva: dos tablas nuevas; sin filas, todo sigue en «frena».

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`03`, `04`, `05`, `14·EST1`, `02·F4`, `02·F5`, `02·F8`, `00·ID8`, `00·ID9`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| El ciclo de importación del pendiente 121 | `catalogo.py` importa `core.validadores` antes que `metareglas` |

## 11. Definition of Done

- [x] CA-01 a CA-04 con veredicto y evidencia en `resultado_pruebas.md`.
- [x] Las pruebas de la fase sin fallas, y cero marcas nuevas.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 7 tareas quedaron hechas el 2026-10-05, con la versión 54.2.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** ninguno.
