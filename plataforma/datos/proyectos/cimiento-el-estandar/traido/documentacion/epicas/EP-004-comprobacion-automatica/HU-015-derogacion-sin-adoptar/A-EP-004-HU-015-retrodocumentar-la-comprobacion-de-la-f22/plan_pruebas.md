# Plan de Pruebas — «Fase A-EP-004-HU-015: retrodocumentar la comprobación de la F22»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de la misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-004-HU-015 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-004-HU-015-retrodocumentar-la-comprobacion-de-la-f22` |
| **Fecha** | 2026-08-16 |
| **Elaborado por** | El agente |
| **Aprobado por** | El usuario, en la orden de resolver los ocho pendientes `P1` |
| **Estado** | Aprobado |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12**.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Unitario | El filtro de versiones, que es aritmética pura | En memoria | Sí |
| Integración | El recorrido de fases que decide si se cobra o no | Carpeta temporal | Sí |

**Por qué los dos niveles.** El `CA-02` vive en `sin_adoptar()`, que no toca disco: armarle carpetas sería probar el andamio en vez de la regla. El `CA-03` vive en `flujo.py`, que decide **si llamar** a la comprobación: eso solo se ve corriendo el recorrido entero.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los tres CA |
| Límites | ☑ | Los transversales: sin `CLAUDE.md`, sin versión declarada |
| No regresión | ☑ | Que las 22 pruebas que ya existen sigan en verde |

### 3.3 Técnicas de diseño de casos

- **Partición por versión declarada** — anterior a la derogación, intermedia y al día.
- **Comprobación previa del dato** — antes de afirmar nada, el caso verifica que el estándar **tenga** reglas derogadas de verdad. Si no las tuviera, todos los casos pasarían sin comprobar nada; es el riesgo `B-03` del plan.
- **Retrodocumentación honesta** — la evidencia sale de correr hoy, no de lo que otra sesión dijo haber corrido a mano.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/tests/` entera, que corre en segundos.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-015 | CA-01 | [CP-001](#cp-001--el-proyecto-atrasado-con-fases-falla-y-la-falla-nombra-las-reglas) | Funcional | Alta | Sí | ☐ |
| HU-015 | CA-02 | [CP-002](#cp-002--lo-ya-adoptado-no-se-cuenta) | Funcional | Alta | Sí | ☐ |
| HU-015 | CA-03 | [CP-003](#cp-003--sin-fases-no-se-cobra) | Funcional | Alta | Sí | ☐ |
| HU-015 | Transversales | [CP-004](#cp-004--los-límites-callan-en-vez-de-romper) | Límites | Media | Sí | ☐ |

**Cobertura:** 3 de 3 CA, más los transversales = 100%.

---

## 6. Casos de prueba

### CP-001 — El proyecto atrasado con fases falla, y la falla nombra las reglas

| Campo | Valor |
|---|---|
| **HU / CA** | HU-015 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | El estándar tiene al menos una regla derogada con su marca |
| **Datos de entrada** | Un proyecto de mentira con `CLAUDE.md` declarando una versión anterior a la primera derogación, y una carpeta de fase |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir las derogaciones del estándar | Hay al menos una; si no, el caso falla acá y lo dice |
| 2 | Correr la comprobación sobre el proyecto atrasado | Sale exactamente una falla |
| 3 | Leer el texto de la falla | Nombra la regla jubilada, en qué versión y qué la reemplaza |
| 4 | Subir la versión declarada a la vigente y correr | Ningún hallazgo de este tipo |

**Resultado esperado final:** el atraso con derogación no pasa como aviso.

---

### CP-002 — Lo ya adoptado no se cuenta

| Campo | Valor |
|---|---|
| **HU / CA** | HU-015 / CA-02 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna: la función no toca disco |
| **Datos de entrada** | Tres derogaciones de mentira, en versiones distintas |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Filtrar desde una versión anterior a las tres | Salen las tres |
| 2 | Filtrar desde una versión intermedia | Salen solo las posteriores |
| 3 | Filtrar desde la versión vigente | No sale ninguna |
| 4 | Filtrar sin versión declarada | Vacío, no error |

**Resultado esperado final:** el hallazgo dice lo que falta, no la historia entera.

> **Acá sí van datos inventados**, al revés que en el CP-001: lo que se prueba es la aritmética del rango, y con datos reales el caso cambiaría de significado cada vez que se derogue una regla.

---

### CP-003 — Sin fases no se cobra

| Campo | Valor |
|---|---|
| **HU / CA** | HU-015 / CA-03 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Las del CP-001 |
| **Datos de entrada** | El mismo proyecto atrasado, sin ninguna carpeta de fase |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Quitarle las fases al proyecto y correr el recorrido de flujo | Ninguna falla de derogación sin adoptar |
| 2 | Devolverle la fase y correr otra vez | Vuelve la falla |

**Resultado esperado final:** el trabajo que `02·F0` exceptúa no queda bloqueado.

> **El paso 2 es el que da valor al 1.** Sin él, el caso pasaría también si la comprobación estuviera rota y no fallara nunca.

---

### CP-004 — Los límites callan en vez de romper

| Campo | Valor |
|---|---|
| **HU / CA** | HU-015 / transversales |
| **Tipo** | Límites |
| **Prioridad** | Media |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Un proyecto sin `CLAUDE.md`, y otro con `CLAUDE.md` sin versión declarada |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr sobre el proyecto sin `CLAUDE.md` | Lista vacía, sin excepción |
| 2 | Correr sobre el que no declara versión | Lista vacía, sin excepción |
| 3 | Comprobar que el proyecto quedó igual | Ningún archivo modificado |

**Resultado esperado final:** lo que no se puede decidir no se inventa, y comprobar no escribe.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | El código no hace lo que la HU dice | Se reporta y el CA queda en «No». **Corregirlo es otra fase**: esta retrodocumenta, no arregla |
| **Alta** | El caso pasa sin que haya derogaciones reales que mirar | Inmediato — el caso no sirve |
| **Media** | La comprobación modifica algo del proyecto | Antes de cerrar |

Se diagnostica y se deja escrito. El ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de CA | 100% — los 3 con caso |
| Casos ejecutados | 4 de 4 |
| Pruebas del repositorio en verde | Las 22 de hoy, más las nuevas |
| Archivos del proyecto de prueba modificados por comprobar | **0** |

El veredicto va en el `resultado_pruebas.md` de esta fase.
