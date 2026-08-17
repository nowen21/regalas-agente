# Plan de Pruebas — «Fase B-EP-005-HU-008: renombrar deja el resumen coherente»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de la misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-B-EP-005-HU-008 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `B-EP-005-HU-008-renombrar-deja-el-resumen-coherente` |
| **Fecha** | 2026-08-16 |
| **Elaborado por** | El agente |
| **Aprobado por** | Pendiente del usuario |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12**.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Integración | Correr `renombrar()` entero sobre un histórico de mentira y leer lo que quedó escrito | Carpeta temporal | Sí |

**Por qué de integración y no unitaria de `_mover_resumen()`.** El defecto no es que esa función calcule mal: es que el conjunto deja el repositorio con un enlace roto. Probar la pieza suelta comprobaría lo que ya hace bien; probar `renombrar()` comprueba lo que el usuario ejecuta.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | El `CA-04` de la HU-008 |
| No regresión | ☑ | Que lo que el renombrado ya hacía bien —mover, titular, reindexar— siga igual |
| Robustez | ☑ | Renombrar una sesión **sin** resumen no revienta |

### 3.3 Técnicas de diseño de casos

- **Partición de casos** — con resumen, sin resumen, y con un resumen que además nombra otra sesión.
- **Prueba de la prueba** — se revierte el arreglo y el caso tiene que ponerse rojo. Es lo que cierra el riesgo `B-02` del plan de trabajo.
- **Caso trampa** — el resumen menciona una segunda sesión, cuyo enlace **no** se debe tocar. Es el riesgo `B-01`.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/tests/` entera. Son tres archivos que corren en segundos, y el nuevo se suma ahí; aislar más no ahorra nada y deja sin ver una regresión cruzada.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-008 | CA-04 | [CP-001](#cp-001--el-resumen-arrastrado-apunta-al-nombre-nuevo) | Funcional | Alta | Sí | ☐ |
| HU-008 | CA-04 · no tocar lo ajeno | [CP-002](#cp-002--el-enlace-a-otra-sesión-no-se-toca) | Funcional | Alta | Sí | ☐ |
| HU-008 | CA-04 · límite | [CP-003](#cp-003--renombrar-una-sesión-sin-resumen-no-revienta) | Robustez | Media | Sí | ☐ |
| HU-008 | CA-04 · prueba de la prueba | [CP-004](#cp-004--el-caso-se-pone-rojo-si-se-revierte-el-arreglo) | Verificación | Alta | No — a mano, una vez | ☐ |

**Cobertura:** 1 de 1 CA cubierto = 100%.

---

## 6. Casos de prueba

### CP-001 — El resumen arrastrado apunta al nombre nuevo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-008 / CA-04 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Carpeta temporal con un histórico de mentira: la transcripción `2026-01-02-sesion.md`, su índice, y `resumenes/2026-01-02/sesion.md` con el enlace de vuelta |
| **Datos de entrada** | Tema `el-tema-real` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Comprobar el estado inicial del resumen | El enlace nombra y apunta a `2026-01-02-sesion.md` |
| 2 | Correr `renombrar(...)` con el tema | Devuelve la ruta nueva, sin error |
| 3 | Mirar la carpeta del día | El resumen se llama ahora `el-tema-real.md` y el viejo no está |
| 4 | Leer el enlace de adentro | El enlace nombra y apunta a `2026-01-02-el-tema-real.md`, en sus dos partes |
| 5 | Comprobar que el destino existe en disco | El archivo al que apunta está |
| 6 | Comprobar que no quedó ninguna mención al nombre viejo | Cero |

**Resultado esperado final:** el resumen queda con su nombre nuevo y su enlace abre.
**Postcondiciones:** la carpeta temporal se borra.

> **El paso 5 no sobra.** Que el texto cambie no prueba que el enlace sirva: lo que se pide es que abra, y eso se comprueba contra el disco.

---

### CP-002 — El enlace a otra sesión no se toca

| Campo | Valor |
|---|---|
| **HU / CA** | HU-008 / CA-04 · no tocar lo ajeno |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Las del CP-001, y el resumen nombra además la sesión `2026-01-01-otra.md` |
| **Datos de entrada** | Tema `el-tema-real` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `renombrar(...)` | Sin error |
| 2 | Leer el enlace propio | Quedó con el nombre nuevo |
| 3 | Leer el enlace a `2026-01-01-otra.md` | Quedó **igual** que antes |

**Resultado esperado final:** se corrige un enlace, no todos los que se parezcan.

---

### CP-003 — Renombrar una sesión sin resumen no revienta

| Campo | Valor |
|---|---|
| **HU / CA** | HU-008 / CA-04 · límite |
| **Tipo** | Robustez |
| **Prioridad** | Media |
| **Precondiciones** | Histórico de mentira **sin** carpeta de resúmenes |
| **Datos de entrada** | Tema `el-tema-real` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `renombrar(...)` | Termina sin error |
| 2 | Mirar la transcripción y el índice | Renombrada y reindexado, como siempre |

**Resultado esperado final:** el camino sin resumen sigue funcionando igual que antes.

---

### CP-004 — El caso se pone rojo si se revierte el arreglo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-008 / CA-04 · verificación del propio caso |
| **Tipo** | Verificación manual, una sola vez |
| **Prioridad** | Alta |
| **Precondiciones** | El CP-001 pasó |
| **Datos de entrada** | Ninguno |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Quitar la reescritura del enlace que agrega el T-02 | El arreglo queda revertido |
| 2 | Correr el CP-001 | Se pone rojo en el paso 4 |
| 3 | Volver a poner la reescritura | El arreglo vuelve |
| 4 | Correr el CP-001 | Verde otra vez |

**Resultado esperado final:** la prueba mide lo que dice medir.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | El renombrado deja de mover la transcripción o de reindexar | Inmediato — es lo que ya funcionaba |
| **Alta** | La prueba pasa en verde con el arreglo revertido | Inmediato — el caso no sirve |
| **Alta** | Se corrige un enlace que no era | Inmediato — el riesgo `B-01` |
| **Media** | El caso sin resumen deja de pasar | Antes de cerrar |

Se diagnostica, se corrige y se vuelve a correr el caso. El ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de CA | 100% — el 1 con caso |
| Casos ejecutados | 4 de 4 |
| Pruebas del repositorio en verde | Las 19 de hoy, más las 3 nuevas |
| Enlaces rotos después de renombrar | **0** |

El veredicto va en el `resultado_pruebas.md` de esta fase.
