# Plan de Trabajo · Fase `A-EP-025-HU-013-tres-capas` (módulo `proyectos/cimiento/core/proyectos/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-013-tres-capas` |
| **Épica** | [EP-025](../../epica.md) |
| **HU** | [HU-013](../HU-013-cada-proyecto-tiene-su-configuracion-en-tres-capas.md), una sola (`F12.1`) |
| **Módulo** | `proyectos/cimiento/core/proyectos/` |
| **Especificación del módulo** | Los CA de la [HU-013](../HU-013-cada-proyecto-tiene-su-configuracion-en-tres-capas.md) |
| **Fecha apertura** | 2026-10-05 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva. Sale de los puntos 5 y 6 del [análisis 2 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md) y del punto 3 del [análisis 3](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md).

**Carencias que cierra** (`02·F14` Q3): no hay valor común de los ajustes, ni dónde poner el de las rutas, ni salida prevista ante un bloqueo del freno.

**Aprobación** (`02·F4`): [análisis 3 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md), el 2026-10-05, con la versión 54.3.0

**Disparo** (`02·F15`, etapa 2): el usuario pidió «continúe» el 2026-10-05, después de aprobar el análisis.

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-013 | Estado |
|---|---|
| CA-01 · Base y proyecto | ☑ |
| CA-02 · Suspender y levantar | ☑ |
| CA-03 · La copia y los límites | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** los ajustes en tres capas, en la base, con sus pantallas, la lectura sin Django, la suspensión en el freno y la copia en el proyecto.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Base y proyecto | Programa y pantallas | Alta |
| CA-02 | Suspender | Programa y pantallas | Alta |
| CA-03 | Copia y límites | Programa | Media |

**Fuera de alcance:** el aviso del freno con la salida (HU-024) y las rutas según el ajuste (HU-014).

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Verificado el 2026-10-05, sobre la versión 55.0.0:

- `Proyecto` tiene las columnas `limite_enganche` y `limite_archivo`; las usan el formulario, la lista, `LimitesDelProyecto` (sin Django), `hook_presupuesto.py` y las pruebas de `core/proyectos/` y de `tests_limites.py`.
- `NivelDeRegla` guarda el nivel por regla y proyecto; el freno lo lee con `NivelesDelProyecto.todos()` y `Freno.nivel_para`, que deja siempre en «frena» el núcleo.
- `NivelesDelProyecto.consultar` solo pasa la ruta del proyecto como parámetro.
- `core/comun/enganches.py` marca `hook_historico.py` como lo que ningún proyecto suspende. El freno son `hook_antes.py` y `hook_despues.py`.
- `formulario.html` arma cada campo como un `input`: no sabe mostrar una lista.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/proyectos/ajustes.py`, `proyectos/cimiento/core/proyectos/copia.py` | Crear | Programa | El catálogo de ajustes y la copia `.agente/configuracion.md` |
| `proyectos/cimiento/core/proyectos/models.py`, `proyectos/cimiento/core/proyectos/migrations/0004_tres_capas.py` | Modificar, crear | Datos | Los tres modelos; los límites pasan a ajustes |
| `proyectos/cimiento/core/proyectos/forms.py`, `proyectos/cimiento/core/proyectos/views.py`, `proyectos/cimiento/core/proyectos/urls.py` | Modificar | Pantallas | «Configuración», ajustes del proyecto y suspensiones |
| `proyectos/cimiento/core/proyectos/templates/proyectos/formulario.html`, `proyectos/cimiento/core/proyectos/templates/proyectos/lista.html`, `proyectos/cimiento/core/proyectos/templates/proyectos/configuracion.html`, `proyectos/cimiento/core/proyectos/templates/proyectos/suspensiones.html`, `proyectos/cimiento/templates/base.html` | Modificar, crear | Pantallas | |
| `proyectos/cimiento/core/enganches/configuracion.py` | Crear | Programa | La lectura sin Django |
| `proyectos/cimiento/core/enganches/niveles.py`, `proyectos/cimiento/core/enganches/freno.py`, `proyectos/cimiento/core/enganches/presupuesto.py` | Modificar | Programa | Suspensiones en los niveles; el freno entero; el aviso por límite |
| `adaptadores/claude-code/hook_presupuesto.py` | Modificar | Programa | Llama al aviso de `core/` |
| `proyectos/cimiento/core/proyectos/tests_configuracion.py` | Crear | Pruebas | |
| `proyectos/cimiento/core/proyectos/tests.py`, `proyectos/cimiento/core/proyectos/tests_registro.py`, `proyectos/cimiento/core/enganches/tests_limites.py` | Modificar | Pruebas | Los límites ya no son columnas |
| `proyectos/cimiento/core/proyectos/tests_analisis_prendido.py`, `proyectos/cimiento/core/consumo/tests_vigilante.py` | Modificar | Pruebas | Declarado durante la fase: sin `serialized_rollback`, al vaciar la base dejan recreados los tipos de contenido y tumban a las pruebas que vienen después |
| `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-013-cada-proyecto-tiene-su-configuracion-en-tres-capas/HU-013-cada-proyecto-tiene-su-configuracion-en-tres-capas.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | Modificar | Documentación | La fila de la fase y el estado |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| Salen `Proyecto.limite_enganche` y `limite_archivo` | Formulario, lista, `LimitesDelProyecto`, pruebas | Pasan a leer el ajuste; la migración copia los valores |
| `NivelesDelProyecto.todos()` suma las suspensiones | El freno | Se corren `tests_freno` y `tests_lectura` de niveles |
| `aviso_de_limites` pasa a `core/` | `hook_presupuesto.py` | Se corren las pruebas de límites y la de consumo que importa el enganche |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

| Ruta | Quién la ve | Quién cambia |
|---|---|---|
| `/proyectos/configuracion/` | Toda cuenta | Administrador |
| `/proyectos/<pk>/suspensiones/` | Toda cuenta | Administrador |
| `/proyectos/<pk>/suspensiones/<id>/levantar/` | Solo `POST` | Administrador |

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

«Configuración» en el menú; los ajustes en «Editar» de cada proyecto; «Suspensiones» en la fila de cada proyecto.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno nuevo: los grupos administrador y consulta.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Lo que se suspende es una regla o el freno entero (`hook_antes.py` y `hook_despues.py` como uno) | Cualquier enganche | El acuerdo habla del enganche que frena; los demás solo informan | Análisis 3, acuerdo 5 |
| Las suspensiones duran a lo sumo 30 días | Sin tope | Una suspensión olvidada deja la regla apagada | Propuesta del agente |
| Suspendido, el nivel queda «apagada» mientras dure; el núcleo sigue en «frena» | Otro nivel | Es lo que el freno ya sabe aplicar | Propuesta del agente |
| Las suspensiones no se borran: se levantan, con quién y cuándo | Borrar la fila | Es la historia de por qué se dejó pasar algo | RNF-02 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  `02·F30`

| Acción nueva | Su contraria | Prueba |
|---|---|---|
| Poner un valor en la base o en el proyecto | Dejarlo vacío, y vuelve a valer el de la capa de abajo | CP-001 |
| Suspender | Levantar | CP-002 |
| La migración que pasa los límites a ajustes | Su reversa los devuelve a las columnas | CP-003 |

## 3. Desglose de tareas por criterio de aceptación

### CA-01 · Base y proyecto

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | El catálogo de ajustes y los modelos `AjusteBase`, `AjusteDelProyecto` y `Suspension`; la migración | `proyectos/cimiento/core/proyectos/ajustes.py`, `proyectos/cimiento/core/proyectos/models.py`, `proyectos/cimiento/core/proyectos/migrations/0004_tres_capas.py` | CA-01 | Base | 1,5 h | Ninguna | CP-001 |
| T-02 | La lectura sin Django | `proyectos/cimiento/core/enganches/configuracion.py`, `proyectos/cimiento/core/enganches/niveles.py` | CA-01 | Enganches | 1 h | T-01 | CP-001 |
| T-03 | «Configuración» y los ajustes en el formulario del proyecto | `proyectos/cimiento/core/proyectos/forms.py`, `proyectos/cimiento/core/proyectos/views.py`, `proyectos/cimiento/core/proyectos/urls.py`, las plantillas, `proyectos/cimiento/templates/base.html` | CA-01 | Pantallas | 2 h | T-01 | CP-001 |

### CA-02 · Suspender y levantar

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-04 | La pantalla de suspensiones, con su validación | `proyectos/cimiento/core/proyectos/views.py`, `proyectos/cimiento/core/proyectos/forms.py`, `proyectos/cimiento/core/proyectos/templates/proyectos/suspensiones.html` | CA-02 | Pantallas | 1,5 h | T-01 | CP-002 |
| T-05 | El freno aplica las suspensiones | `proyectos/cimiento/core/enganches/niveles.py`, `proyectos/cimiento/core/enganches/freno.py` | CA-02 | Freno | 1 h | T-02 | CP-002 |

### CA-03 · La copia y los límites

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-06 | La copia `.agente/configuracion.md` en cada cambio | `proyectos/cimiento/core/proyectos/copia.py` | CA-03 | Proyectos | 1 h | T-01 | CP-003 |
| T-07 | Los límites desde los ajustes; el aviso por límite en `core/` | `proyectos/cimiento/core/enganches/niveles.py`, `proyectos/cimiento/core/enganches/presupuesto.py`, `adaptadores/claude-code/hook_presupuesto.py` | CA-03 | Enganches | 0,5 h | T-02 | CP-003 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-08 | Pruebas nuevas y las que cambian; migración real; cierre con `cerrar_fase` | `proyectos/cimiento/core/proyectos/tests_configuracion.py`, `proyectos/cimiento/core/proyectos/tests.py`, `proyectos/cimiento/core/proyectos/tests_registro.py`, `proyectos/cimiento/core/enganches/tests_limites.py`, la HU y la épica | CA-01 a CA-03 | Documentación | 1,5 h | T-01 a T-07 | CP-001 a CP-003 |

## 4. Secuencia de ejecución

T-01 a T-08.

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Capas leídas sin Django contra la base de pruebas; pantallas | CP-001 |
| CA-02 | Suspensiones en el freno; validaciones | CP-002 |
| CA-03 | Copia, límites y migración | CP-003 |

## 6. Datos y ambiente de prueba

La base de pruebas de Django en MariaDB y carpetas temporales para los proyectos.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit y `migrate proyectos 0003`: la reversa devuelve los límites a sus columnas.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

`preparar_base` aplica la `0004`; los límites de cada proyecto pasan a sus ajustes.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`02·F30`, `00·N6`, `03·D2`, `03·D6`, `04·S9`, `02·F4`, `02·F5`, `02·F8`, `00·ID8`, `00·ID9`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Una suspensión que deja pasar el núcleo | El freno lo deja siempre en «frena» |
| Perder los límites al quitar las columnas | La migración los copia antes, y su reversa los devuelve |

## 11. Definition of Done

- [ ] CA-01 a CA-03 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Las pruebas de la fase sin fallas, y cero marcas nuevas.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 8 tareas quedaron hechas el 2026-10-05, con la versión 55.0.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** ninguno.
