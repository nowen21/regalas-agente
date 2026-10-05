# Plan de Trabajo · Fase `A-EP-004-HU-026-el-validador-avisa-la-funcion-repetida` (módulo `proyectos/cimiento/core/validadores/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-026-el-validador-avisa-la-funcion-repetida` |
| **Épica** | [EP-004](../../epica.md) |
| **HU** | [HU-026](../HU-026-una-funcion-que-ya-existe-se-avisa-al-crearla.md), una sola (`F12.1`) |
| **Módulo** | `proyectos/cimiento/core/validadores/` |
| **Especificación del módulo** | Los CA de la [HU-026](../HU-026-una-funcion-que-ya-existe-se-avisa-al-crearla.md) |
| **Fecha apertura** | 2026-10-04 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva. Sale de los puntos 2 y 3 del [análisis 1 del pendiente 116](../../../../../historico-chat/resumenes/2026-10-04/pendientes/116-el-codigo-de-cimiento-se-repite-en-vez-de-reusarse/analisis-1.md) (acuerdos 2, 3 y 4) y resuelve el pendiente 117.

**Carencias que cierra** (`02·F14` Q3): `07·Q4` no tiene quién lo compruebe, y al crear una función nadie mira si ya existe.

**Aprobación** (`02·F4`): Ing. José Dúmar Jiménez Ruíz, el 2026-10-04, con la versión 53.3.0

**Disparo** (`02·F15`, etapa 2): el usuario pidió construir lo decidido en el análisis el 2026-10-04 con «Hágalo: el 1».

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-026 | Estado |
|---|---|
| CA-01 · La separación de funciones vive una sola vez | ☐ |
| CA-02 · Avisa la función que hace lo mismo que otra, aunque se llame distinto | ☐ |
| CA-03 · No avisa lo que solo se parece por el nombre o es demasiado corto | ☐ |
| CA-04 · Al guardar, avisa la función nueva que repite una que ya estaba | ☐ |
| CA-05 · Corre en un proyecto que no es Cimiento | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** un validador `repetidas` de `07·Q4` que avisa, sin frenar, la función que hace lo mismo que otra del proyecto, sobre todo el código o sobre lo que entra en el commit.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | La separación de funciones en `codigo.py` | Programa | Baja |
| CA-02 | La copia con otros nombres | Programa | Media |
| CA-03 | El mismo nombre con otro cuerpo, y lo muy corto | Programa | Media |
| CA-04 | Lo que entra en el commit | Programa | Media |
| CA-05 | Un proyecto que no es Cimiento | Programa | Baja |
| RNF-01 | Menos de 30 s sobre Cimiento | No funcional | Baja |

**Fuera de alcance:** juntar las copias que ya hay (otra épica, acuerdo 2); sumar el aviso al enganche `pre-commit` del instalador.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-10-04, sobre la versión 53.3.0:

- `proyectos/cimiento/core/validadores/calidad.py` separa las funciones con dos expresiones propias (`_FUNC_LLAVES` y `_DEF_PYTHON`) y con `Bloques.llaves` y `Bloques.sangria` de `codigo.py`.
- `ValidadorDeCodigo` de `codigo.py` recorre una vez los archivos de código versionados y le pasa cada texto a `revisar_texto`; `Git.preparados()` de `core/comun/git.py` da lo que entra en el commit.
- `core/herramientas/validar.py` es el despachador de `validar.py`; cada subcomando corre un validador y reporta.
- Ningún validador cita `07·Q4`.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/validadores/codigo.py` | Modificar | Programa | La clase `Funciones`, que separa las funciones de un texto |
| `proyectos/cimiento/core/validadores/calidad.py` | Modificar | Programa | Usa `Funciones` |
| `proyectos/cimiento/core/validadores/repetidas.py` | Nuevo | Programa | El validador `repetidas` de `07·Q4` |
| `proyectos/cimiento/core/validadores/__init__.py` | Modificar | Programa | Lo exporta |
| `proyectos/cimiento/core/herramientas/validar.py` | Modificar | Programa | El subcomando `repetidas`, con `--preparados` |
| `proyectos/cimiento/core/validadores/tests_repetidas.py` | Nuevo | Pruebas | Los casos del plan de pruebas |
| `validadores/reglas-validables.md` | Modificar | Documentación | `07·Q4` pasa a tener programa |
| `documentacion/epicas/EP-004-comprobacion-automatica/HU-026-una-funcion-que-ya-existe-se-avisa-al-crearla/HU-026-una-funcion-que-ya-existe-se-avisa-al-crearla.md` | Modificar | Documentación | La fila de esta fase |
| `CHANGELOG.md`, `VERSION` | Modificar | Versión | Versión MENOR siguiente |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| Las expresiones de `calidad.py` pasan a `codigo.py` | `FuncionesLargas` | La usa desde `Funciones`; sus pruebas siguen iguales |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

`python validadores/validar.py repetidas [--raiz <proyecto>] [--preparados]`.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Avisa, no falla | Fallar | Así lo acordó el usuario | Análisis 1, acuerdo 4 |
| Se compara el cuerpo normalizado: sin comentarios, sin espacios, y cada nombre propio reemplazado por su orden de aparición | Comparar el nombre | Dos copias con otros nombres hacen lo mismo; el nombre igual no dice nada | Análisis 1, acuerdo 4 |
| Se mide el parecido de los cuerpos normalizados y se avisa desde un umbral alto, con un tamaño mínimo; los dos se fijan midiendo sobre Cimiento y se escriben con el número medido | Un umbral elegido de antemano | Un aviso que sale por casualidad se aprende a ignorar | Propuesta del agente |
| `--preparados` avisa solo la función nueva que repite otra; la copia que ya estaba no se vuelve a avisar en cada commit | Avisar todas en cada commit | El objetivo es que no nazcan copias nuevas | Análisis 1, acuerdo 2 |
| La separación de funciones vive en `codigo.py` (`core/`), no en `validadores/codigo.py` | La ruta del punto 2 | `validadores/` ya pasó a `core/` (punto 21) | Análisis 1, acuerdo 11 |
| Versión MENOR | MAYOR | Es un validador nuevo, que avisa; nadie tiene que hacer algo nuevo | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| `07·Q4` | Sin programa | `validar.py repetidas` | `07·Q4` |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-01 · La separación de funciones vive una sola vez

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | `Funciones.de(texto)` da `[(nombre, línea, cuerpo)]`; `FuncionesLargas` la usa | `proyectos/cimiento/core/validadores/codigo.py`, `proyectos/cimiento/core/validadores/calidad.py` | CA-01 | `calidad` | 1 h | Ninguna | CP-001 |

### CA-02 · Avisa la función que hace lo mismo que otra, aunque se llame distinto

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-02 | `FuncionesRepetidas`: normaliza cada cuerpo, compara por pares y avisa los que pasan el umbral; mide umbral y tamaño sobre Cimiento | `proyectos/cimiento/core/validadores/repetidas.py`, `proyectos/cimiento/core/validadores/__init__.py` | CA-02, CA-03, CA-05 | Todo proyecto | 2 h | T-01 | CP-002, CP-003, CP-005 |

### CA-03 · No avisa lo que solo se parece por el nombre o es demasiado corto

Lo cubre `T-02`: el umbral y el tamaño mínimo son los que dejan fuera lo que no es copia.

### CA-05 · Corre en un proyecto que no es Cimiento

Lo cubre `T-02`: el validador recorre el proyecto que se le pasa, como los demás de `core/validadores/`.

### CA-04 · Al guardar

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-03 | Con `solo_preparados`, compara las funciones de lo que entra en el commit contra las de `HEAD` y avisa solo las nuevas; el subcomando `repetidas` en `validar.py` | `proyectos/cimiento/core/validadores/repetidas.py`, `proyectos/cimiento/core/herramientas/validar.py` | CA-04 | Todo proyecto | 1,5 h | T-02 | CP-004 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-04 | Los casos del plan de pruebas; `07·Q4` en las reglas validables; la fila de la fase en la HU; la versión | `proyectos/cimiento/core/validadores/tests_repetidas.py`, `validadores/reglas-validables.md`, `documentacion/epicas/EP-004-comprobacion-automatica/HU-026-una-funcion-que-ya-existe-se-avisa-al-crearla/HU-026-una-funcion-que-ya-existe-se-avisa-al-crearla.md`, `CHANGELOG.md`, `VERSION` | CA-01 a CA-05 | Todo proyecto adopta la versión | 1 h | T-01 a T-03 | CP-001 a CP-005 |

## 4. Secuencia de ejecución

T-01, T-02 y T-03; al final T-04, con las pruebas de la fase, las de `calidad` y la medición de marcas (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Las pruebas de `calidad` sin cambios | CP-001 |
| CA-02 | Dos copias con otros nombres | CP-002 |
| CA-03 | Mismo nombre y otro cuerpo; funciones muy cortas | CP-003 |
| CA-04 | Un commit que agrega una copia | CP-004 |
| CA-05 | Correrlo parado en agro-system | CP-005 |

## 6. Datos y ambiente de prueba

Proyectos de prueba con git en carpetas temporales; Cimiento y agro-system de solo lectura.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Aditiva: un subcomando nuevo que avisa. Nada que ya corre cambia su resultado.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`07·Q4`, `07·Q3`, `02·F8`, `20·M9`, `20·M10`, `02·F27`, `00·ID8`, `00·ID9`, `02·F5`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Que el aviso salga por casualidad | Umbral y tamaño medidos sobre Cimiento antes de fijarlos |

## 11. Definition of Done

- [ ] CA-01 a CA-05 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Las pruebas de la fase y de `calidad` sin fallas, y cero marcas nuevas.
- [ ] `VERSION` y `CHANGELOG.md` al día.
- [ ] Aprobación del usuario.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 4 tareas quedaron hechas el 2026-10-04, con la versión 54.1.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** 0.
