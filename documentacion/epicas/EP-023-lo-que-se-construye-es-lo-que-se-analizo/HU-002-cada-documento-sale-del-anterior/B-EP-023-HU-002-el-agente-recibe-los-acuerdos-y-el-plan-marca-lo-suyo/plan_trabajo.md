# Plan de Trabajo · Fase `B-EP-023-HU-002-el-agente-recibe-los-acuerdos-y-el-plan-marca-lo-suyo` (módulo `validadores/`, `adaptadores/claude-code/` y `plantillas/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-023-HU-002-el-agente-recibe-los-acuerdos-y-el-plan-marca-lo-suyo` |
| **Épica** | [EP-023](../../epica.md) |
| **HU** | [HU-002](../HU-002-cada-documento-sale-del-anterior.md), una sola (`F12.1`) |
| **Módulo** | `validadores/`, `adaptadores/claude-code/`, `plantillas/` |
| **Especificación del módulo** | Los CA-04 y CA-05 de la HU-002 |
| **Fecha apertura** | 2026-10-03 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): segunda fase de la HU-002. Sale de los puntos 1 y 2 de «Lo que se tiene que hacer» del [análisis 10](../../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-10.md) (acuerdos 3 y 4).

**Carencias que cierra** (`02·F14` Q3): el agente no recibe los acuerdos de los que sale lo que trabaja y los pierde cuando la conversación se resume; el plan no distingue lo que sale del análisis de lo que propone el agente.

**Aprobación** (`02·F4`): Ing. José Dúmar Jiménez Ruíz, el 2026-10-03, con la versión 49.0.0.

**Disparo** (`02·F15`, etapa 2): el usuario pidió escribir esta fase el 2026-10-03 con «Escriba».

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-002 | Estado |
|---|---|
| CA-04 · El agente recibe los acuerdos de los que sale lo que trabaja | ☐ |
| CA-05 · Lo que el plan decide por su cuenta queda marcado como propuesta del agente | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que con cada mensaje le lleguen al agente los acuerdos de los que sale lo que trabaja, y que toda decisión del plan diga de qué acuerdo sale o que es propuesta del agente.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-04 | Un enganche entrega, con cada mensaje, los acuerdos de la fase en curso y los del análisis prendido | Programa y enganche | Media |
| CA-05 | La tabla de decisiones del plan cita el acuerdo o marca la propuesta, y el validador de origen detiene la que no tiene ninguna | Plantilla y validador | Baja |

**Fuera de alcance:** el freno que compara con el plan de la fase en curso (HU-007, fase `B`).

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-10-03, sobre la versión 49.0.0:

- `adaptadores/claude-code/hook_reglas.py` entrega con cada mensaje las reglas que pide el mensaje. La herramienta acepta 10.000 caracteres por enganche, y el de las reglas ya usa casi todo su tope (`recuperar.TOPE`). No entrega acuerdos.
- `validadores/origen.py` ya sigue la cadena del criterio al punto y del punto al acuerdo (`leer_analisis`, `_revisar_hu`), pero solo para avisar orígenes rotos; no lee el plan.
- `validadores/analisis_en_curso.py` guarda en `historico-chat/.estado/analisis-en-curso.txt` qué análisis está prendido.
- Ningún programa dice qué fase está en curso. `validadores/estacion_commit.py` anota el commit en la estación 12 del estado de la fase. De 240 fases, 105 no lo tienen anotado porque cerraron antes de que existiera esa anotación; las 105 tienen `funcionalidad_implementada.md` y ninguna trae la aprobación con versión que pide el plan desde 48.0.0.
- La tabla 2.6 de `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` tiene «Decisión», «Alternativa descartada» y «Justificación»; no pide de dónde sale la decisión.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

> Cada fila lleva una o más rutas exactas entre comillas invertidas, separadas por coma.

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/acuerdos.py` | Nuevo | Programa | La fase en curso y los acuerdos que le tocan; los del análisis prendido; el texto con su tope |
| `adaptadores/claude-code/hook_acuerdos.py` | Nuevo | Enganche | Entrega el texto con cada mensaje |
| `validadores/instalar.py` | Modificar | Instalador | Registra el enganche |
| `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` | Modificar | Plantilla | La columna «Sale de» en la tabla 2.6 |
| `validadores/origen.py` | Modificar | Validador | La decisión del plan sin acuerdo ni marca |
| `validadores/tests/test_los_acuerdos_llegan.py` | Nuevo | Pruebas | Los casos del plan de pruebas |
| `anatomia/mapa-del-sitio.md` | Modificar | Documentación | El programa y el enganche nuevos |
| `documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/HU-002-cada-documento-sale-del-anterior/HU-002-cada-documento-sale-del-anterior.md` | Modificar | Documentación | La fila de esta fase |
| `CHANGELOG.md`, `VERSION` | Modificar | Versión | 50.0.0 |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| La tabla 2.6 del plan suma una columna | Los planes nuevos | Se exige solo a los planes aprobados desde 50.0.0 |
| La fase en curso | El freno de la HU-007, fase `B` | Queda en `acuerdos.py` para que el freno la use |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Los acuerdos llegan con cada mensaje y, como las reglas, completos los que caben y los demás nombrados con su tema y su número | Cortar el texto donde se acabe el tope | El tema es lo que va antes de los dos puntos del acuerdo | Análisis 10, acuerdo 4 |
| La fase está en curso desde que se crea su carpeta hasta que su estado tiene el commit anotado | Desde que se aprueba su plan | El plan se escribe con la fase ya en curso | Análisis 10, acuerdo 4 |
| La fase cuyo plan no trae la aprobación con versión y ya tiene `funcionalidad_implementada.md` se da por cerrada | Contar en curso toda fase sin commit anotado | 105 fases que cerraron antes de que existiera la anotación quedarían en curso para siempre | Propuesta del agente |
| Los acuerdos de la fase salen de los CA de la tabla de su plan; si el plan todavía no los nombra, de todos los CA de su HU | Esperar a que el plan exista | El acuerdo 4 pide que lleguen desde que se crea la carpeta | Análisis 10, acuerdo 4 |
| Los acuerdos llegan por un enganche propio | Sumarlos al enganche de las reglas | El tope es por enganche y el de las reglas ya va casi lleno | Propuesta del agente |
| La tabla 2.6 suma la columna «Sale de», con «análisis N, acuerdo M» o «Propuesta del agente» | Una tabla aparte | Cada decisión dice de dónde sale en su misma fila | Análisis 10, acuerdo 3 |
| `origen.py` exige la columna solo a los planes aprobados desde 50.0.0 | Exigirla a todos | Los planes aprobados antes no se reabren (`20·M10`) | Propuesta del agente |
| La versión sube a 50.0.0, MAYOR | MENOR | Un plan nuevo no pasa `origen` sin la columna | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| Lo que recibe el agente con cada mensaje | Las reglas | Las reglas y los acuerdos de lo que trabaja | `02·F1` |
| Tabla 2.6 del plan | Sin origen | Cada decisión con su acuerdo o la marca de propuesta | `02·F27` |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-04 · El agente recibe los acuerdos de los que sale lo que trabaja

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | `acuerdos.py`: las fases en curso; los acuerdos de cada una, siguiendo el «Sale de» de sus CA; los de los análisis aprobados del pendiente del análisis prendido; y el texto con su tope, completos los que caben y los demás nombrados | `validadores/acuerdos.py` | CA-04 | Lo usa también el freno de la HU-007 | 2 h | Ninguna | CP-001, CP-002 |
| T-02 | El enganche que entrega ese texto con cada mensaje; nunca detiene el trabajo | `adaptadores/claude-code/hook_acuerdos.py` | CA-04 | Todo mensaje | 0,5 h | T-01 | CP-002 |
| T-03 | El instalador registra el enganche | `validadores/instalar.py` | CA-04 | Todo proyecto, al reinstalar | 0,3 h | T-02 | CP-002 |

### CA-05 · Lo que el plan decide por su cuenta queda marcado como propuesta del agente

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-04 | La tabla 2.6 suma la columna «Sale de», con su nota | `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` | CA-05 | Los planes nuevos | 0,3 h | Ninguna | CP-003 |
| T-05 | `origen.py` detiene, en el plan aprobado desde 50.0.0, la decisión que no cita un acuerdo existente de un análisis de su épica ni dice «Propuesta del agente» | `validadores/origen.py` | CA-05 | Ninguno en los planes aprobados antes | 1 h | T-04 | CP-003 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-06 | Escribir los casos del plan de pruebas; poner el programa y el enganche en el mapa del sitio; la fila de la fase en la HU; subir a 50.0.0 con «⚠ obliga a migrar» | `validadores/tests/test_los_acuerdos_llegan.py`, `anatomia/mapa-del-sitio.md`, `documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/HU-002-cada-documento-sale-del-anterior/HU-002-cada-documento-sale-del-anterior.md`, `CHANGELOG.md`, `VERSION` | CA-04, CA-05 | Todo proyecto adopta la versión | 1 h | T-01 a T-05 | CP-001 a CP-004 |

## 4. Secuencia de ejecución

T-01, T-02 y T-03; después T-04 y T-05; al final T-06, con los validadores, las pruebas de la fase y la medición de marcas (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-04 | Con una fase en curso y con un análisis prendido, leer lo que el enganche entrega | CP-001, CP-002 |
| CA-05 | Leer la plantilla; el validador sobre un plan con una decisión sin acuerdo ni marca | CP-003 |

## 6. Datos y ambiente de prueba

Un proyecto de prueba en una carpeta temporal, con una épica, una HU, un pendiente con análisis aprobados y fases en distintos estados.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Cada proyecto adopta la 50.0.0 con el instalador, que registra el enganche nuevo. Los planes aprobados antes no se revisan; desde esa versión, cada decisión del plan dice de dónde sale.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`02·F1`, `02·F4`, `02·F8`, `02·F27`, `20·M2`, `20·M10`, `00·ID8`, `00·ID9`, `02·F5`, `02·F18`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Que los acuerdos llenen el mensaje | Tienen su propio tope: los que no caben llegan nombrados |
| Que una fase vieja aparezca en curso | Se reconoce por su cierre y por no traer la aprobación con versión |

## 11. Definition of Done

- [ ] CA-04 y CA-05 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Los validadores y las pruebas de la fase sin fallas, y cero marcas nuevas.
- [ ] `VERSION` y `CHANGELOG.md` en 50.0.0.
- [ ] Aprobación del usuario.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Se llena al cerrar la fase.

**Hallazgos al ejecutar:** se anota al cerrar.
