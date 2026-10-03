# Plan de Trabajo · Fase `A-EP-023-HU-006-la-leccion-tiene-su-categoria-y-alimenta-las-recomendaciones` (módulo `memoria/`, `plantillas/` y `validadores/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-023-HU-006-la-leccion-tiene-su-categoria-y-alimenta-las-recomendaciones` |
| **Épica** | [EP-023](../../epica.md) |
| **HU** | [HU-006](../HU-006-lo-aprendido-incluye-las-lecciones.md), una sola (`F12.1`) |
| **Módulo** | `memoria/`, `plantillas/` y `validadores/` |
| **Especificación del módulo** | Los CA-01 y CA-02 de la HU-006 |
| **Fecha apertura** | 2026-10-02 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): primera fase de la HU-006. Sale del punto 9 de «Lo que se tiene que hacer» del [análisis 1](../../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-1.md) y del punto 6 del [análisis 8](../../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-8.md).

**Carencias que cierra** (`02·F14` Q3): la lección de un análisis no tiene dónde guardarse con su propia categoría, y no alimenta las recomendaciones del análisis siguiente (análisis 1, conclusión 13; análisis 8, punto 6).

**Aprobación** (`02·F4`): el usuario aprobó el plan el 2026-10-02.

**Disparo** (`02·F15`, etapa 2): el usuario pidió seguir con la HU-006 el 2026-10-02 con «Continúe».

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-006 | Estado |
|---|---|
| CA-01 · La lección aprendida tiene su categoría y el análisis la enlaza | ☑ |
| CA-02 · Las lecciones alimentan las recomendaciones | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que cada lección de un análisis quede en el almacén de señales con la categoría «lección», que la tabla de lecciones la enlace, y que diga si complementa una recomendación, crea una nueva o no aplica.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | El tipo «lección» en el almacén de señales; la tabla de lecciones enlaza la señal | Programa, plantilla y validador | Baja |
| CA-02 | La columna de la recomendación en la tabla de lecciones; la recomendación queda complementada | Plantilla y validador | Baja |

**Fuera de alcance:**

- Las lecciones de los análisis ya aprobados: quedan como están, con «Por escribir».

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-10-02, sobre la versión 45.0.0:

- `memoria/memoria.py` acepta diez tipos de señal (`TIPOS`, línea 30); no hay «lección». `memoria/pruebas.py` (línea 227) comprueba que sean diez. `documentacion/senales.md` lista los diez en «Tipos».
- La tabla de lecciones de `plantillas/analisis.md` tiene «#», «Lección», «Tipo» y «Señal», con la nota «El texto completo vive en el almacén de señales; aquí va el enlace». No dice qué recomendación complementa.
- `validadores/analisis.py` no mira la tabla de lecciones. La puerta de versión de la fase D de la HU-001 exige lo nuevo solo a los análisis aprobados desde la versión que lo trae.
- Las recomendaciones de Cimiento viven en `plantillas/recomendaciones-del-analisis.md`, de la R-1 a la R-17.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `memoria/memoria.py`, `memoria/esquema.sql`, `memoria/pruebas.py` | Modificar | Programa | El tipo «leccion» |
| `documentacion/senales.md` | Modificar | Documentación | El tipo en la lista |
| `plantillas/analisis.md` | Modificar | Plantilla | La tabla de lecciones con la señal y la recomendación |
| `validadores/analisis.py` | Modificar | Validador | La señal y la recomendación de cada lección, desde 46.0.0 |
| `validadores/tests/test_analisis.py` | Modificar | Pruebas | Los casos del plan de pruebas |
| `CHANGELOG.md` y `VERSION` | Modificar | Versión | 46.0.0 |
| Los documentos de esta fase y la HU-006 | Modificar | Documentación | Cierre |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| `TIPOS` suma uno | `memoria/pruebas.py`, que cuenta diez | La prueba pasa a once |
| La tabla de lecciones suma una columna | `analisis.py` | Lee la columna solo en los aprobados desde 46.0.0 |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El tipo se llama `leccion`, sin tilde, como `decision` y `restriccion` | `lección` | Los tipos del almacén se escriben sin tilde |
| La columna «Recomendación» dice «complementa R-n», «nueva R-n» o «no aplica»; el validador comprueba que la R-n exista | Que el validador busque la lección dentro de la recomendación | Lo que la lección dice no se puede comparar con un programa; que la recomendación exista sí |
| La lección enlaza su señal (`S-NNN`) y el validador comprueba que exista en `documentacion/senales.md` con el tipo `leccion` | Aceptar «Por escribir» | El CA-01 pide que la lección quede con su categoría y que el análisis la enlace |
| La versión sube a 46.0.0, MAYOR | MENOR | Todo análisis nuevo tiene que traer la señal y la recomendación de cada lección |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| Tipos de señal | Diez | Once, con `leccion` | `13·DOC5` |
| Tabla de lecciones | Lección, tipo y señal | Además, la recomendación que complementa o crea | `13·DOC24` |
| `analisis.py` | No mira las lecciones | Señal y recomendación de cada lección, desde 46.0.0 | `13·DOC24` |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-01 · La lección aprendida tiene su categoría y el análisis la enlaza

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | Sumar `leccion` a los tipos del almacén, al comentario del esquema y a la lista de `documentacion/senales.md`; la prueba cuenta once | `memoria/memoria.py`, `memoria/esquema.sql`, `memoria/pruebas.py`, `documentacion/senales.md` | CA-01 | Ninguno en las señales que existen | 0,3 h | Ninguna | CP-001 |
| T-02 | La nota de la tabla de lecciones dice que cada una se escribe como señal de tipo `leccion` y que la columna «Señal» la enlaza | `plantillas/analisis.md` | CA-01 | Los análisis nuevos | 0,2 h | T-01 | CP-001 |
| T-03 | Falla si una lección de un análisis aprobado desde 46.0.0 no enlaza una señal que exista con el tipo `leccion` | `validadores/analisis.py` | CA-01 | Ninguno en los aprobados antes | 0,7 h | T-01 | CP-001 |

### CA-02 · Las lecciones alimentan las recomendaciones

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-04 | Sumar a la tabla de lecciones la columna «Recomendación» («complementa R-n», «nueva R-n» o «no aplica»), con la nota de buscar antes de crear una | `plantillas/analisis.md` | CA-02 | Los análisis nuevos | 0,2 h | Ninguna | CP-002 |
| T-05 | Falla si en un análisis aprobado desde 46.0.0 una lección deja vacía la columna, o nombra una R-n que no existe | `validadores/analisis.py` | CA-02 | Ninguno en los aprobados antes | 0,5 h | T-04 | CP-002 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-06 | Escribir los casos del plan de pruebas; subir a 46.0.0 con «⚠ obliga a migrar» | `validadores/tests/test_analisis.py`, `VERSION`, `CHANGELOG.md` | CA-01, CA-02 | Todo proyecto adopta la versión | 0,7 h | T-01 a T-05 | CP-001 a CP-003 |

## 4. Secuencia de ejecución

T-01, T-02 y T-04; después T-03 y T-05; al final T-06, con los validadores, las pruebas de la fase y la medición de marcas (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Escribir una señal `leccion`; el validador sobre un análisis que la enlaza y otro que no | CP-001 |
| CA-02 | Leer la plantilla; el validador sobre una lección que complementa una R-n que existe y otra que no | CP-002 |

## 6. Datos y ambiente de prueba

El repositorio del estándar, y carpetas temporales con análisis, señales y recomendaciones de prueba.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Cada proyecto adopta la 46.0.0 con el instalador. Las lecciones de los análisis aprobados antes no cambian; las de los nuevos se escriben como señal y dicen qué recomendación alimentan.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`13·DOC5`, `13·DOC24`, `20·M10`, `02·F27`, `00·ID8`, `00·ID9`, `02·F5`, `02·F18`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Que un análisis viejo empiece a fallar | La comprobación solo corre en los aprobados desde 46.0.0; lo prueba el CP-003 |

## 11. Definition of Done

- [ ] CA-01 y CA-02 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Los validadores y las pruebas de la fase sin fallas, y cero marcas nuevas.
- [ ] `VERSION` y `CHANGELOG.md` en 46.0.0.
- [ ] Aprobación del usuario.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Se llena al cerrar la fase.
