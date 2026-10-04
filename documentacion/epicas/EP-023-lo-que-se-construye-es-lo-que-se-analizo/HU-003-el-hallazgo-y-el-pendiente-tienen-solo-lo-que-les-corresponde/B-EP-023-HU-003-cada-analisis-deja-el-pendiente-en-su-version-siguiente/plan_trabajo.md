# Plan de Trabajo · Fase `B-EP-023-HU-003-cada-analisis-deja-el-pendiente-en-su-version-siguiente` (módulo `validadores/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-023-HU-003-cada-analisis-deja-el-pendiente-en-su-version-siguiente` |
| **Épica** | [EP-023](../../epica.md) |
| **HU** | [HU-003](../HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde.md), una sola (`F12.1`) |
| **Módulo** | `validadores/` |
| **Especificación del módulo** | El CA-09 de la HU-003 |
| **Fecha apertura** | 2026-10-03 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): segunda fase de la HU-003. Sale del punto 4 del [análisis 11](../../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-11.md) (acuerdo 5). La fase `A` cubrió los criterios anteriores.

**Carencias que cierra** (`02·F14` Q3): un análisis se aprueba aunque su hallazgo no haya pasado al pendiente, y nada lo detiene. Así pasó en los análisis 8 a 11.

**Aprobación** (`02·F4`): Ing. José Dúmar Jiménez Ruíz, el 2026-10-03, con la versión 51.1.0.

**Disparo** (`02·F15`, etapa 2): el usuario pidió escribir esta fase el 2026-10-03 con «Escriba».

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-003 | Estado |
|---|---|
| CA-09 · Cada análisis deja el pendiente en su versión siguiente | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que «Apruebo el análisis» no ponga la marca si el hallazgo del análisis falta en «De dónde sale» de su pendiente, y que el aviso diga qué falta.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-09 | Aprobar un análisis cuyo hallazgo falta en el pendiente | Programa | Baja |
| CA-09 | La plantilla pide el pendiente en su versión siguiente | Plantilla | Ninguna: ya lo pide |

**Fuera de alcance:** reescribir el pendiente. Lo hace el agente antes de aprobar, como ya pide la plantilla.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-10-03, sobre la versión 51.0.0:

- `validadores/analisis_en_curso.py` decide si un análisis se aprueba: `faltantes()` revisa «Lo que se tiene que hacer» y «Lo que aporta al análisis principal»; `por_que_no_se_aprueba()` arma el aviso y `aprobar()` pone la marca. No mira el pendiente.
- `adaptadores/claude-code/hook_analisis.py` llama a esas dos funciones al recibir «Apruebo el análisis»; no cambia.
- El hallazgo de cada análisis va en su sección «Hallazgo», con un título `### H-N · …` (análisis 10, 11 y 12). El `pendiente.md` cita sus hallazgos por número en la fila «De dónde sale».
- `plantillas/analisis.md` ya pide, en «Propuesta final», el «Pendiente V«N+1»» y pasarlo al original antes de aprobar. La parte de la plantilla del CA-09 ya está.
- Leen el programa que cambia: `validadores/tests/test_analisis_en_curso.py`. Sus análisis de prueba salen de la plantilla, sin número de hallazgo.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

> Cada fila lleva una o más rutas exactas entre comillas invertidas, separadas por coma.

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/analisis_en_curso.py` | Modificar | Programa | Revisa que el hallazgo esté en el pendiente antes de aprobar |
| `validadores/tests/test_el_analisis_mejora_su_pendiente.py` | Nuevo | Pruebas | Los casos del plan de pruebas |
| `documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde/HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde.md` | Modificar | Documentación | La fila de esta fase |
| `CHANGELOG.md`, `VERSION` | Modificar | Versión | 52.0.0 |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| `por_que_no_se_aprueba()` y `aprobar()` revisan el pendiente | `hook_analisis.py` | Nada: ya muestra lo que devuelve |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| El control va en `analisis_en_curso.py`, donde ya se decide si un análisis se aprueba, y el aviso dice qué hallazgo falta | Un validador aparte | Es el mismo momento: «Apruebo el análisis» | Análisis 11, acuerdo 5 |
| El hallazgo se reconoce por su número `H-N` en el título de «Hallazgo» y se busca en «De dónde sale» del `pendiente.md` de la misma carpeta | Comparar el texto del hallazgo | El pendiente cita sus hallazgos por número | Propuesta del agente |
| El análisis 1 no se revisa | Revisarlos todos | Ese análisis origina el pendiente; lo mejoran los siguientes | Análisis 11, acuerdo 5 |
| Desde el análisis 2, si «Hallazgo» no trae número, el aviso lo dice y no se aprueba | Dejarlo pasar | Sin número no se puede revisar, y el hallazgo siempre tiene uno en el resumen de su sesión | Propuesta del agente |
| El programa solo revisa; el pendiente lo reescribe el agente antes de aprobar | Que el programa escriba el pendiente | «El problema» y «Por qué importa» recogen lo que el análisis precisó, y eso no lo sabe un programa | Análisis 11, acuerdo 5 |
| Lo ya aprobado no se revisa: el control corre solo al aprobar | Revisar los análisis viejos | Un análisis aprobado no se reescribe (`13·DOC24`) | Propuesta del agente |
| La versión sube a 52.0.0, MAYOR | MENOR | Aprobar un análisis exige algo nuevo | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| «Apruebo el análisis» | Pone la marca aunque el hallazgo falte en el pendiente | No la pone, y el aviso dice qué hallazgo falta | `02·F28` |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-09 · Cada análisis deja el pendiente en su versión siguiente

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | Una función que lee el `H-N` de «Hallazgo» y lo busca en «De dónde sale» del pendiente; `por_que_no_se_aprueba()` y `aprobar()` la usan | `validadores/analisis_en_curso.py` | CA-09 | Todo análisis que se apruebe desde la 52.0.0 | 1 h | Ninguna | CP-001, CP-002 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-02 | Escribir los casos del plan de pruebas; la fila de la fase en la HU; subir a 52.0.0 con «⚠ obliga a migrar» | `validadores/tests/test_el_analisis_mejora_su_pendiente.py`, `documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde/HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde.md`, `CHANGELOG.md`, `VERSION` | CA-09 | Todo proyecto adopta la versión | 0,5 h | T-01 | CP-001 a CP-003 |

## 4. Secuencia de ejecución

T-01 y después T-02, con los validadores, las pruebas de la fase y la medición de marcas (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-09 | Aprobar un análisis con el hallazgo en el pendiente y otro sin él; leer la «Propuesta final» de la plantilla | CP-001 a CP-003 |

## 6. Datos y ambiente de prueba

Un proyecto de prueba en una carpeta temporal, con un pendiente, sus análisis 1 y 2, y el estado del análisis prendido.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Cada proyecto adopta la 52.0.0 al actualizar el estándar. Desde ahí, antes de «Apruebo el análisis», el hallazgo tiene que estar en «De dónde sale» de su pendiente.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`02·F28`, `13·DOC24`, `20·M10`, `02·F27`, `00·ID8`, `00·ID9`, `02·F5`, `02·F18`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Que un número de hallazgo se repita entre sesiones y pase por otro | Se acepta: el pendiente cita pocos hallazgos y el agente los pasa al aprobar |

## 11. Definition of Done

- [ ] CA-09 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Los validadores y las pruebas de la fase sin fallas, y cero marcas nuevas.
- [ ] `VERSION` y `CHANGELOG.md` en 52.0.0.
- [ ] Aprobación del usuario.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 2 tareas quedaron hechas el 2026-10-03, con la versión 52.0.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** 0. Una prueba escrita en el análisis 14 armaba un análisis sin hallazgo; se ajustó bajo la fila 4 de ese análisis.
