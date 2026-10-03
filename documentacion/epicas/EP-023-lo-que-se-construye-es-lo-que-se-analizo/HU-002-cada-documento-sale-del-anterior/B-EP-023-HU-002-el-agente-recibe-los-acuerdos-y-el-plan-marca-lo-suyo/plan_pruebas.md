# Plan de Pruebas · Fase `B-EP-023-HU-002-el-agente-recibe-los-acuerdos-y-el-plan-marca-lo-suyo`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP023-HU002-B |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-002: CA-04 y CA-05 |
| **Fecha** | 2026-10-03 |
| **Elaborado por** | Claude |
| **Revisado por** | Ing. José Dúmar Jiménez Ruíz |
| **Aprobado por** | Ing. José Dúmar Jiménez Ruíz, el 2026-10-03 |
| **Estado** | Aprobado |

Para una fase, la plantilla pide las secciones 3, 5, 6, 9 y 12; las demás son opcionales y no se usan.

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Unitario | La fase en curso, los acuerdos, el tope, el enganche y el validador de origen | Claude | Proyecto de prueba en una carpeta temporal | Sí |
| Aceptación | Que la plantilla diga lo que pide el criterio | Ing. José Dúmar Jiménez Ruíz | Lectura | No |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-04 y CA-05 |
| Compatibilidad | ☑ | Las fases y los planes de antes no cambian de estado |

### 3.3 Técnicas de diseño de casos

- Partición: fase recién creada, con plan, con commit y vieja; plan aprobado antes y desde 50.0.0; acuerdos que caben y que no.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-04 y CA-05 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Las pruebas de la fase: `validadores/tests/test_los_acuerdos_llegan.py`; las de los programas que cambia: `test_origen.py` y las del instalador; `validar.py estandar`, `flujo` y `origen`, y las marcas de lo que se va a guardar.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-002 | CA-04 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-002 | CA-04 | CP-002 | Funcional | Alta | Sí | ☑ |
| HU-002 | CA-05 | CP-003 | Funcional | Alta | Sí | ☑ |
| HU-002 | RNF-06 | CP-004 | Trazabilidad | Media | Parcial | ☑ |

**Cobertura:** 2 de 2 criterios de esta fase y el RNF-06.

## 6. Casos de prueba

### CP-001 · Los acuerdos de la fase en curso

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-04 |
| **Precondiciones** | T-01 terminada |
| **Datos de entrada** | Una HU con CA que salen de un análisis aprobado y fases en distintos estados |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Fase recién creada, sin plan | Llegan los acuerdos de todos los CA de la HU |
| 2 | Fase con plan que nombra un solo CA | Llegan solo los acuerdos de ese CA |
| 3 | Fase con el commit anotado en su estado | No llega nada de esa fase |
| 4 | Fase cuyo plan no trae la aprobación con versión y tiene `funcionalidad_implementada.md` | No llega nada de esa fase |

### CP-002 · Los acuerdos del análisis prendido, con su tope

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-04 |
| **Precondiciones** | T-01 a T-03 terminadas |
| **Datos de entrada** | Un pendiente con los análisis 1 y 2 aprobados y el 3 prendido |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir el texto con el análisis 3 prendido | Trae los acuerdos de los análisis 1 y 2 |
| 2 | Pedir el texto con un tope pequeño | Los que no caben llegan nombrados con su tema y su número |
| 3 | Correr el enganche con una entrada dañada | Sale con 0 y no detiene |
| 4 | Leer los enganches que registra el instalador | Está el de los acuerdos |

### CP-003 · La decisión del plan dice de dónde sale

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-05 |
| **Precondiciones** | T-04 y T-05 terminadas |
| **Datos de entrada** | Planes de prueba aprobados con 49.0.0 y con 50.0.0 |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer la tabla 2.6 de la plantilla | Tiene la columna «Sale de» |
| 2 | Validar un plan de 50.0.0 con una decisión sin acuerdo ni marca | Una falla |
| 3 | Validar uno que cita un acuerdo que no existe | Una falla |
| 4 | Validar uno con una cita válida y una «Propuesta del agente» | Ninguna falla |
| 5 | Validar un plan aprobado con 49.0.0 sin la columna | Ninguna falla |

### CP-004 · Cada tarea cita su criterio

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / RNF-06 |
| **Precondiciones** | Fase terminada |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validar.py flujo` y leer el plan | Ninguna tarea sin su criterio |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Un acuerdo que debía llegar no llega, o una decisión sin origen pasa | Antes de cerrar la fase |
| **Baja** | Una marca de redacción | Antes de cerrar la fase |

### 9.2 Flujo del defecto

Un defecto se anota en el resultado de las pruebas. Si es un error dentro de lo que el plan aprobó, se corrige y se vuelve a correr el caso. Si está fuera del plan, es un hallazgo: se detiene la fase y vuelve al análisis.

### 9.3 Contenido mínimo de un reporte

- Caso y paso donde apareció.
- Resultado esperado frente al obtenido.

### 9.4 Registro

Los defectos van en el `resultado_pruebas.md` de la fase.

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de exigencias | Criterios y RNF con caso / criterios y RNF de la fase | 100% |
| Casos ejecutados | Ejecutados / diseñados | 100% |

### 12.2 Dónde se miden

En el `resultado_pruebas.md` de la fase.
