# Resultado de Pruebas — Fase «B-EP-007-HU-001-prepara-su-propia-salida»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [`plan_pruebas.md`](plan_pruebas.md), que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-007-HU-001-prepara-su-propia-salida` |
| **HU** | [HU-001 — Instalar con una línea](../HU-001-instalar-con-una-linea.md) |
| **Ciclo** | 2 |
| **Fecha de ejecución** | 2026-08-16 |
| **Ejecutado por** | El agente |
| **Ambiente y versión** | Windows 11 · Python 3.11 · estándar 21.2.0 → 21.2.1 |

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 1 | 1 | 0 | 0 |
| 2 | 2 | 2 | 2 | 0 | 0 | 0 |

**El que falló en el ciclo 1 fue el CP-002, y falló haciendo exactamente lo que tenía que hacer:** destapar que el CP-001 no servía.

---

## 2. Ejecución caso por caso

### CA-01 · CP-001 — instalar no revienta con una consola que no admite la flecha

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Armar una salida en `cp1252` sin perdón y escribirle `→` | Falla | Falla con `UnicodeEncodeError` |
| 2 | Instalar una primera vez, con la consola normal | Termina | «13 de 13» |
| 3 | Subir el `VERSION` de la copia del estándar a `99.0.0` | Los sellos quedan viejos | Quedaron |
| 4 | Cambiar la salida del proceso por la pobre y volver a instalar | Termina sin reventar | Terminó |
| 5 | Comprobar que lo impreso trae una `→` | La trae | La trae |
| 6 | Restaurar la salida | Queda como estaba | Restaurada |

**Por qué el paso 5 decide.** Sin él, el caso pasa cuando el instalador **no imprimió ninguna flecha**, que es justo el escenario en que no prueba nada. Es lo que pasó en el ciclo 1.

**Veredicto:** ✅ Cumple.

---

### CA-01 · CP-002 — el caso se pone rojo si se revierte el arreglo

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Comentar la línea `preparar_salida()` de `instalar()` | El arreglo queda revertido | Revertido |
| 2 | Correr el CP-001 | Se pone rojo con `UnicodeEncodeError` | **Ciclo 1: pasó en verde.** Ciclo 2: `UnicodeEncodeError: 'charmap' codec can't encode character '→'` |
| 3 | Volver a poner la línea | El arreglo vuelve | Vuelto |
| 4 | Correr todo | 19 de 19 en verde | 19 de 19 |

**Veredicto:** ✅ Cumple.

---

## 3. Defectos encontrados

| ID | Caso | Qué pasó | De quién era | Estado |
|---|---|---|---|---|
| DEF-01 | CP-001 | El caso instalaba en una carpeta vacía, y esa corrida **nunca imprime una flecha** — la flecha sale al refrescar un sello que ya existía. Pasaba en verde con el defecto puesto | Del caso, no del código | Corregido: se instala primero, se sube la versión para que los sellos queden viejos, y la corrida que se mide es la segunda. Se agregó la comprobación de que se imprimió una `→` |

**Es el riesgo `B-01` del plan, y se materializó.** Vale la pena dejarlo escrito: la prueba de robustez estaba armando un escenario que no reproducía el defecto, y **el único motivo por el que se supo es que el plan obligaba a verla fallar**. Sin el CP-002, la fase habría cerrado con una prueba que no comprueba nada y con el arreglo dado por bueno sin evidencia.

---

## 4. Lo que se descubrió fuera del criterio

Nada nuevo.

---

## 5. Cobertura contra el plan de pruebas

| Exigencia | Caso | Estado |
|---|---|---|
| CA-01 — una línea deja el proyecto listo, sin morirse al imprimir | CP-001 | ✅ |
| CA-01 · prueba de la prueba | CP-002 | ✅ |

**Cobertura:** 1 de 1 exigencia = 100%.

---

## 6. Veredicto de la fase

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 1 de 1 |
| **CA en "No"** | ninguno |
| **Defectos abiertos aceptados** | ninguno. El `DEF-01` era del caso y quedó corregido |

---

## 7. Métricas contra la meta del plan

| Métrica | Meta | Dio |
|---|---|---|
| Cobertura de exigencias | 100% | 100% |
| Casos ejecutados | 2 de 2 | 2 de 2 |
| Pruebas del repositorio en verde | 19 de 19 | 19 de 19 |
| Llamadas a `preparar_salida()` fuera del propio programa | 0 | 0 — el rodeo de la fase anterior quedó quitado |
