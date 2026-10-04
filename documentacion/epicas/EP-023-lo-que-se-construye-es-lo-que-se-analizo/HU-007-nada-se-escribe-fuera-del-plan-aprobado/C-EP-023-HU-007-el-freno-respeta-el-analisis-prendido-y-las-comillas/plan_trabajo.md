# Plan de Trabajo · Fase `C-EP-023-HU-007-el-freno-respeta-el-analisis-prendido-y-las-comillas` (módulo `validadores/` y `adaptadores/claude-code/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-023-HU-007-el-freno-respeta-el-analisis-prendido-y-las-comillas` |
| **Épica** | [EP-023](../../epica.md) |
| **HU** | [HU-007](../HU-007-nada-se-escribe-fuera-del-plan-aprobado.md), una sola (`F12.1`) |
| **Módulo** | `validadores/`, `adaptadores/claude-code/` |
| **Especificación del módulo** | El CA-05 y el CA-06 de la HU-007 |
| **Fecha apertura** | 2026-10-03 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): tercera fase de la HU-007. Sale de los puntos 5 y 6 del [análisis 13](../../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-13.md) (acuerdos 6 y 7). La integración continua y el contrato de cada adaptador, que el plan de la fase `B` anunciaba como fase `C`, pasan a la fase `D`.

**Carencias que cierra** (`02·F14` Q3): con un análisis prendido, el freno anota un hallazgo aparte en el resumen (H-17 y H-19), y toma por escritura un `>` que está entre comillas (H-17).

**Aprobación** (`02·F4`): Ing. José Dúmar Jiménez Ruíz, el 2026-10-03, con la versión 52.1.2.

**Disparo** (`02·F15`, etapa 2): el usuario pidió escribir esta fase el 2026-10-03 con «Escriba».

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-007 | Estado |
|---|---|
| CA-05 · Con un análisis prendido, el freno no anota hallazgos | ☐ |
| CA-06 · Un `>` entre comillas no es escritura | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que con un análisis prendido el freno detenga y avise sin escribir en el resumen, y que un `>` entre comillas no cuente como escritura.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-05 | El freno con un análisis prendido, y `13·DOC22` | Programa, enganche y regla | Baja |
| CA-06 | Los destinos de una orden de consola | Programa | Media |

**Fuera de alcance:** la integración continua y el contrato de cada adaptador (fase `D`).

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-10-03, sobre la versión 52.1.2:

- `adaptadores/claude-code/hook_antes.py` llama a `freno.anotar_hallazgo()` cada vez que detiene, haya o no un análisis prendido; `freno.aviso()` dice «Quedó anotado en el resumen de la sesión».
- `freno.destinos()` saca los archivos de una orden de consola; trata un `>` dentro de comillas como redirección.
- `analisis_en_curso.leer_estado()` dice si hay un análisis prendido.
- `13·DOC22` manda escribir en el resumen lo que la sesión deja, sin distinguir si hay un análisis prendido; su texto se copia en `base/reglas-por-tarea/escribir-documento-2.md`.
- Lee el programa que cambia: `validadores/tests/test_el_freno.py`. Las tres pruebas del freno viejo en `test_las_reglas_llegan_antes_de_actuar.py` son del pendiente 109 y no se tocan.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

> Cada fila lleva una o más rutas exactas entre comillas invertidas, separadas por coma.

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/freno.py` | Modificar | Programa | No anota con un análisis prendido; el `>` entre comillas no es destino |
| `adaptadores/claude-code/hook_antes.py` | Modificar | Enganche | El aviso dice que se reporta en la conversación cuando hay un análisis prendido |
| `base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md` | Modificar | Regla | Con un análisis prendido, lo que aparece va a la conversación; su sello |
| `base/reglas-por-tarea/escribir-documento-2.md` | Modificar | Generado | Lo vuelve a escribir `mapa_tareas.py` |
| `validadores/tests/test_el_freno.py` | Modificar | Pruebas | Los casos del plan de pruebas |
| `documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/HU-007-nada-se-escribe-fuera-del-plan-aprobado/HU-007-nada-se-escribe-fuera-del-plan-aprobado.md` | Modificar | Documentación | La fila de esta fase |
| `CHANGELOG.md`, `VERSION` | Modificar | Versión | Versión MENOR siguiente |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| `freno.anotar_hallazgo()` | `hook_antes.py` | Devuelve que no anotó, y el aviso lo dice |
| `freno.destinos()` | `freno.revisar()` y la capa 2 | Una orden que solo lee texto con `>` pasa; la capa 2 sigue viendo lo que de verdad se escribió |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Con un análisis prendido, el freno detiene y avisa, pero no escribe en el resumen; el agente lo reporta en la conversación | Anotarlo siempre | Así lo acordó el usuario | Análisis 13, acuerdo 6 |
| Prendido es el análisis que recibe la conversación y no se ha aprobado: lo dice `analisis_en_curso.leer_estado()` | Usar «abierto» de `analisis_en_curso.abiertos()` | Así lo acordó el usuario | Análisis 13, acuerdo 6 |
| `13·DOC22` lo dice | Dejarlo solo en el programa | La regla y el programa dicen lo mismo | Análisis 13, acuerdo 6 |
| El texto entre comillas simples o dobles se quita antes de buscar redirecciones | Buscar `>` en toda la orden | Así lo acordó el usuario | Análisis 13, acuerdo 7 |
| La versión sube a la MENOR siguiente | MAYOR | El freno detiene lo mismo y anota menos; nadie tiene que hacer algo nuevo | Propuesta del agente |
| La integración continua pasa a la fase `D` | Llamar `D` a esta | Esta se escribe primero | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| Hallazgo del freno con un análisis prendido | Va al resumen | Va a la conversación | `13·DOC22` |
| `>` entre comillas | Redirección | Texto | `02·F8` |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-05 · Con un análisis prendido, el freno no anota hallazgos

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | `freno.anotar_hallazgo()` no escribe si hay un análisis prendido; `freno.aviso()` y `hook_antes.py` dicen que se reporta en la conversación | `validadores/freno.py`, `adaptadores/claude-code/hook_antes.py` | CA-05 | Toda detención del freno | 1 h | Ninguna | CP-001 |
| T-02 | `13·DOC22` lo dice; checklist, sello y `mapa_tareas.py` | `base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md`, `base/reglas-por-tarea/escribir-documento-2.md` | CA-05 | Todo proyecto que adopte la versión | 0,5 h | Ninguna | CP-001 |

### CA-06 · Un `>` entre comillas no es escritura

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-03 | `freno.destinos()` quita el texto entre comillas antes de buscar redirecciones | `validadores/freno.py` | CA-06 | Toda orden de consola | 1 h | Ninguna | CP-002 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-04 | Escribir los casos del plan de pruebas; la fila de la fase en la HU; subir la versión | `validadores/tests/test_el_freno.py`, `documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/HU-007-nada-se-escribe-fuera-del-plan-aprobado/HU-007-nada-se-escribe-fuera-del-plan-aprobado.md`, `CHANGELOG.md`, `VERSION` | CA-05, CA-06 | Todo proyecto adopta la versión | 0,5 h | T-01 a T-03 | CP-001, CP-002 |

## 4. Secuencia de ejecución

T-01, T-02 y T-03; al final T-04, con los validadores, las pruebas de la fase y la medición de marcas (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-05 | Detener una acción con y sin análisis prendido; leer `13·DOC22` | CP-001 |
| CA-06 | Una búsqueda con `>` entre comillas y una redirección real | CP-002 |

## 6. Datos y ambiente de prueba

Un proyecto de prueba con git en una carpeta temporal, con una fase en curso, su resumen de sesión y el estado de un análisis prendido.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase y reinstalar.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Cada proyecto lo recibe al adoptar la versión; los enganches ya están instalados y no cambian de sitio.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`02·F8`, `13·DOC22`, `20·M5`, `20·M10`, `02·F27`, `00·ID8`, `00·ID9`, `02·F5`, `02·F18`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Que una redirección real quede dentro de comillas que el freno no entiende | La capa 2 ve después lo que de verdad se escribió |

## 11. Definition of Done

- [ ] CA-05 y CA-06 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Los validadores y las pruebas de la fase sin fallas, y cero marcas nuevas.
- [ ] `VERSION` y `CHANGELOG.md` al día.
- [ ] Aprobación del usuario.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 4 tareas quedaron hechas el 2026-10-03, con la versión 52.2.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** 0.
