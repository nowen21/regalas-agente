# Plan de Trabajo · Fase `A-EP-004-HU-027-el-control-avisa-las-reglas-parecidas` (módulo `proyectos/cimiento/core/validadores/` y `adaptadores/claude-code/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-027-el-control-avisa-las-reglas-parecidas` |
| **Épica** | [EP-004](../../epica.md) |
| **HU** | [HU-027](../HU-027-una-regla-parecida-se-avisa-al-crearla.md), una sola (`F12.1`) |
| **Módulo** | `proyectos/cimiento/core/validadores/`, `adaptadores/claude-code/` |
| **Especificación del módulo** | Los CA de la [HU-027](../HU-027-una-regla-parecida-se-avisa-al-crearla.md) |
| **Fecha apertura** | 2026-10-04 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva. Sale del punto 7 del [análisis 1 del pendiente 116](../../../../../historico-chat/resumenes/2026-10-04/pendientes/116-el-codigo-de-cimiento-se-repite-en-vez-de-reusarse/analisis-1.md) (acuerdo 5).

**Carencias que cierra** (`02·F14` Q3): `20·M12` manda buscar por concepto antes de crear una regla, y nada lo hace.

**Aprobación** (`02·F4`): Ing. José Dúmar Jiménez Ruíz, el 2026-10-04, con la versión 53.3.0

**Cambio aprobado** (versión 2 del plan): Ing. José Dúmar Jiménez Ruíz, el 2026-10-05, con «Apruebo». Cargar el modelo tardaba casi 4 s y el RNF-01 pide menos de 3: su tabla de palabras se guarda en una base de datos y la regla nueva se traduce buscando solo sus palabras. Se midió en 1 s y con los mismos números que la librería.

**Disparo** (`02·F15`, etapa 2): el usuario pidió construir lo decidido en el análisis el 2026-10-04 con «Hágalo: el 1».

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-027 | Estado |
|---|---|
| CA-01 · Al escribir una regla llegan las parecidas | ☑ |
| CA-02 · Se puede pedir para una regla o para lo que entra en el commit | ☑ |
| CA-03 · Sin la búsqueda por significado, lo dice | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que al escribir una regla, o al guardarla, se avise qué reglas se le parecen por significado, sin frenar.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | El enganche al escribir | Enganche | Media |
| CA-02 | `validar.py parecidas` | Programa | Media |
| CA-03 | Sin la búsqueda por significado | Programa | Baja |
| RNF-01 | Menos de 3 s | No funcional | Media |

**Fuera de alcance:** decidir si dos reglas se contradicen.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-10-04, sobre la versión 53.3.0:

- `memoria/semantica.py` da `disponible()` y `embed(textos)`, con el modelo local `potion-base-8M`; hoy está disponible. `memoria/parecidas.py` compara por coseno con un umbral medido (0,90 para señales) y, sin la búsqueda, devuelve vacío y lo dice.
- `CuerpoDeReglas.leer(raiz)` de `core/validadores/metareglas.py` da todas las reglas con su identificador, título y texto.
- `adaptadores/claude-code/hook_relacionadas.py` corre al escribir un documento que un capítulo gobierna y entrega lo que `ReglasRelacionadas` de `core/validadores/relacionadas.py` encuentra; una vez por archivo y por sesión, y sale siempre con 0.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/validadores/parecidas.py` | Nuevo | Programa | `ReglasParecidas`: las reglas que se parecen a una, por significado; y `Diccionario`, la tabla de palabras del modelo en una base de datos |
| `proyectos/cimiento/core/validadores/__init__.py` | Modificar | Programa | Lo exporta |
| `proyectos/cimiento/core/validadores/relacionadas.py` | Modificar | Programa | `como_texto` suma las parecidas |
| `proyectos/cimiento/core/herramientas/validar.py` | Modificar | Programa | El subcomando `parecidas`, con `--regla` y `--preparados` |
| `adaptadores/claude-code/hook_relacionadas.py` | Modificar | Enganche | Entrega también las parecidas |
| `proyectos/cimiento/core/validadores/tests_parecidas.py` | Nuevo | Pruebas | Los casos del plan de pruebas |
| `validadores/reglas-validables.md` | Modificar | Documentación | `20·M12` pasa a tener control |
| `documentacion/epicas/EP-004-comprobacion-automatica/HU-027-una-regla-parecida-se-avisa-al-crearla/HU-027-una-regla-parecida-se-avisa-al-crearla.md` | Modificar | Documentación | La fila de esta fase |
| `CHANGELOG.md`, `VERSION` | Modificar | Versión | Versión MENOR siguiente |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| `ReglasRelacionadas.como_texto` | `hook_relacionadas.py` | Suma una sección; lo que ya entregaba no cambia |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

El enganche al escribir una regla, y `python validadores/validar.py parecidas --regla <ID>` o `--preparados`.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Se usa `memoria/semantica.py`, sin copiarlo | Otra búsqueda | Así lo acordó el usuario | Análisis 1, acuerdo 5 |
| Se compara el título con el cuerpo de la regla, sin el sello del checklist | Solo el título | Los títulos siguen un molde y se parecen por la forma | Análisis 1, acuerdo 5 |
| El umbral se mide sobre las reglas de hoy, con `02·F4` y `02·F25` como par que tiene que salir, y se escribe con el número medido; tope de cinco | Un umbral elegido de antemano | Una lista larga se deja de leer | Propuesta del agente |
| Va en el enganche de reglas relacionadas, no en uno nuevo | Un enganche nuevo | Ya corre al escribir una regla, una vez por archivo y sin frenar | Propuesta del agente |
| La tabla de palabras del modelo se guarda en `memoria/diccionario.db` (que git ignora), se arma sola la primera vez, y cada regla se traduce con ella; el modelo se abre solo para armarla | Guardar los vectores de las reglas en `.agente/`: no sirve, porque traducir las 257 tarda 0,02 s y lo lento es abrir el modelo, que la regla recién escrita siempre necesita | RNF-01: abrir el modelo tarda de 2 a 6 s; con la tabla, 1 s | Decisión del usuario, 2026-10-05 |
| El umbral es 0,85 y se compara el título con la exigencia, sin ejemplos | El texto entero de la regla, con el que `02·F4` no salía entre las seis primeras de `02·F25` | Medido sobre las 257 reglas vigentes; ver el comentario de `UMBRAL` | Propuesta del agente |
| Versión MENOR | MAYOR | Es un aviso nuevo; nadie tiene que hacer algo nuevo | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| Escribir una regla | Llegan las que cita y las que la citan | Llegan también las que se le parecen | `20·M12` |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-02 · Se puede pedir para una regla o para lo que entra en el commit

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | `ReglasParecidas(raiz).de(id)`: las reglas con coseno sobre el umbral, de mayor a menor, hasta cinco; sin la búsqueda, dice que no pudo. Medir el umbral | `proyectos/cimiento/core/validadores/parecidas.py`, `proyectos/cimiento/core/validadores/__init__.py` | CA-02, CA-03 | Todo proyecto | 2 h | Ninguna | CP-002, CP-003 |
| T-02 | El subcomando `parecidas`, con `--regla` y `--preparados` | `proyectos/cimiento/core/herramientas/validar.py` | CA-02 | Todo proyecto | 1 h | T-01 | CP-002 |

### CA-03 · Sin la búsqueda por significado, lo dice

Lo cubre `T-01`: sin `memoria/semantica.py` disponible, la búsqueda dice que no pudo y no nombra ninguna regla.

### CA-01 · Al escribir

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-03 | `ReglasRelacionadas.como_texto` y el enganche suman las parecidas de la regla escrita | `proyectos/cimiento/core/validadores/relacionadas.py`, `adaptadores/claude-code/hook_relacionadas.py` | CA-01 | Toda escritura de una regla | 1 h | T-01 | CP-001 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-04 | Los casos del plan de pruebas; `20·M12` en las reglas validables; la fila de la fase en la HU; la versión | `proyectos/cimiento/core/validadores/tests_parecidas.py`, `validadores/reglas-validables.md`, `documentacion/epicas/EP-004-comprobacion-automatica/HU-027-una-regla-parecida-se-avisa-al-crearla/HU-027-una-regla-parecida-se-avisa-al-crearla.md`, `CHANGELOG.md`, `VERSION` | CA-01 a CA-03 | Todo proyecto adopta la versión | 1 h | T-01 a T-03 | CP-001 a CP-003 |

## 4. Secuencia de ejecución

T-01, T-02 y T-03; al final T-04, con las pruebas de la fase, las de `relacionadas` y la medición de marcas (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | El enganche al escribir `F25` | CP-001 |
| CA-02 | `--regla F25` y `--preparados` | CP-002 |
| CA-03 | La búsqueda apagada | CP-003 |

## 6. Datos y ambiente de prueba

Las reglas de este repositorio, de solo lectura, y repositorios de prueba en carpetas temporales.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Aditiva: el enganche entrega una sección más; donde no está la búsqueda, lo dice y sigue.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`20·M12`, `02·F8`, `20·M9`, `20·M10`, `02·F27`, `00·ID8`, `00·ID9`, `02·F5`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Que cargar el modelo pase de 3 s | Pasó: la tabla de palabras en una base de datos (cambio del 2026-10-05) |
| Que la tabla traduzca distinto que la librería | Una prueba compara las dos traducciones de las reglas de hoy |

## 11. Definition of Done

- [ ] CA-01 a CA-03 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Las pruebas de la fase y de `relacionadas` sin fallas, y cero marcas nuevas.
- [ ] `VERSION` y `CHANGELOG.md` al día.
- [ ] Aprobación del usuario.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 4 tareas quedaron hechas el 2026-10-05, con la versión 54.3.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** 1. El enganche tardaba 3,9 s y el RNF-01 pide menos de 3; el usuario aprobó el 2026-10-05 guardar la tabla de palabras del modelo en una base de datos (versión 2 de este plan).
