# Plan de Trabajo · Fase `A-EP-025-HU-024-la-salida-del-freno` (módulo `proyectos/cimiento/core/enganches/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-024-la-salida-del-freno` |
| **Épica** | [EP-025](../../epica.md) |
| **HU** | [HU-024](../HU-024-el-aviso-del-freno-dice-como-salir-sin-tocar-archivos.md), una sola (`F12.1`) |
| **Módulo** | `proyectos/cimiento/core/enganches/` |
| **Especificación del módulo** | Los CA de la [HU-024](../HU-024-el-aviso-del-freno-dice-como-salir-sin-tocar-archivos.md) |
| **Fecha apertura** | 2026-10-05 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva y corrección. Sale de los puntos 9 y 11 del [análisis 3 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md).

**Carencias que cierra** (`02·F14` Q3): el freno no dice la salida; lee el análisis de otra sesión; ignora el `cd` de un comando.

**Aprobación** (`02·F4`): [análisis 3 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-3.md), el 2026-10-05, con la versión 54.3.0

**Disparo** (`02·F15`, etapa 2): el usuario pidió «continúe» el 2026-10-05, después de aprobar el análisis.

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-024 | Estado |
|---|---|
| CA-01 · El aviso dice la salida | ☑ |
| CA-02 · El análisis de la propia sesión | ☑ |
| CA-03 · El `cd` de un comando | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** el aviso con la salida, el análisis de la propia sesión y el `cd`.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Aviso | Programa | Baja |
| CA-02 | Sesión | Programa | Media |
| CA-03 | `cd` | Programa | Media |

**Fuera de alcance:** suspender desde el aviso.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Verificado el 2026-10-05, sobre la versión 55.0.0:

- `Freno.aviso(porque, ruta, anotado, prendido)` arma el texto de cuando detiene; `hook_antes.py` lo llama.
- `Freno.de_una()` y `Freno.analisis_prendido()` crean `AnalisisEnCurso(self.raiz)` sin sesión: leen la fila más reciente (antes, el archivo único). Es la causa del H-8.
- `Freno.transcripcion_de(sesion)` lee entera cada transcripción buscando la marca, que va en la primera línea.
- `Freno.decidir` resuelve cada destino de un comando desde el `cwd` de la sesión.
- `hook_antes.py` y `hook_despues.py` crean `Freno(proyecto)` y tienen el `session_id` de la entrada.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/enganches/freno.py` | Modificar | Programa | Aviso, sesión, `cd` |
| `adaptadores/claude-code/hook_antes.py`, `adaptadores/claude-code/hook_despues.py` | Modificar | Programa | Le pasan la sesión al freno y la salida al aviso |
| `proyectos/cimiento/core/enganches/tests_freno_salida.py` | Crear | Pruebas | |
| `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-024-el-aviso-del-freno-dice-como-salir-sin-tocar-archivos/HU-024-el-aviso-del-freno-dice-como-salir-sin-tocar-archivos.md`, `documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md` | Modificar | Documentación | La fila de la fase y el estado |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| `Freno` recibe `sesion` | Los dos enganches del freno, las pruebas | Sin sesión, igual que antes; se corre `tests_freno` |
| `decidir` sigue el `cd` | El freno antes de cada orden | Se corre `tests_freno` |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

El aviso del freno.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| El aviso nombra la dirección de «Suspensiones» del proyecto, con el puerto del `.env` de Cimiento | Decir solo «en Cimiento» | El usuario llega en un clic | Propuesta del agente |
| La transcripción se busca por la primera línea | Leer el archivo entero | La marca va arriba, y el freno corre en cada acción | RNF-01 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  `02·F30`

No aplica: la fase no agrega acciones; cambia el aviso y cómo el freno lee lo que ya existe.

## 3. Desglose de tareas por criterio de aceptación

### CA-01 · El aviso dice la salida

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | `Freno.salida(porque)` y el aviso con ella | `proyectos/cimiento/core/enganches/freno.py`, `adaptadores/claude-code/hook_antes.py` | CA-01 | Freno | 1 h | Ninguna | CP-001 |

### CA-02 · El análisis de la propia sesión

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-02 | `Freno(…, sesion)`; `de_una` y `analisis_prendido` con el análisis de la sesión; la transcripción por la primera línea | `proyectos/cimiento/core/enganches/freno.py`, `adaptadores/claude-code/hook_antes.py`, `adaptadores/claude-code/hook_despues.py` | CA-02 | Freno | 1 h | Ninguna | CP-002 |

### CA-03 · El `cd` de un comando

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-03 | Cada parte de la orden resuelve sus rutas desde el `cd` anterior | `proyectos/cimiento/core/enganches/freno.py` | CA-03 | Freno | 1 h | Ninguna | CP-003 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-04 | Pruebas y cierre con `cerrar_fase` | `proyectos/cimiento/core/enganches/tests_freno_salida.py`, la HU y la épica | CA-01 a CA-03 | Documentación | 1 h | T-01 a T-03 | CP-001 a CP-003 |

## 4. Secuencia de ejecución

T-01 a T-04.

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | El texto del aviso | CP-001 |
| CA-02 | Dos sesiones con análisis distintos | CP-002 |
| CA-03 | Órdenes con `cd` | CP-003 |

## 6. Datos y ambiente de prueba

Carpetas temporales con transcripciones y análisis de muestra.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Nada que migrar.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`02·F8`, `02·F30`, `00·N3`, `02·F4`, `02·F5`, `00·ID8`, `00·ID9`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Que el freno deje pasar de más | `tests_freno` completo en verde |

## 11. Definition of Done

- [ ] CA-01 a CA-03 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Las pruebas de la fase sin fallas, y cero marcas nuevas.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Las 4 tareas quedaron hechas el 2026-10-05, con la versión 55.0.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** ninguno.

**Reabierta** el 2026-10-05: con un cd, la orden se partía por líneas antes de mirar las comillas, y un signo dentro de un texto entre comillas parecía una redirección (H-10 del resumen del 2026-10-04, sesión 3).

Cerrada otra vez el 2026-10-05, con la versión 55.0.0.
