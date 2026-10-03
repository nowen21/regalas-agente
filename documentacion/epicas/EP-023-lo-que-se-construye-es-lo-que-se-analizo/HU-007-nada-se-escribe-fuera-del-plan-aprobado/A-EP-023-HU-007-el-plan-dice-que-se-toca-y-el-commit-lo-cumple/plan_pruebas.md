# Plan de Pruebas · Fase `A-EP-023-HU-007-el-plan-dice-que-se-toca-y-el-commit-lo-cumple`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP023-HU007-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-007: CA-01, CA-03 y CA-04 |
| **Fecha** | 2026-10-02 |
| **Elaborado por** | Claude |
| **Revisado por** | Ing. José Dúmar Jiménez Ruíz |
| **Aprobado por** | Ing. José Dúmar Jiménez Ruíz, el 2026-10-02 |
| **Estado** | Aprobado |

Para una fase, la plantilla pide las secciones 3, 5, 6, 9 y 12; las demás son opcionales y no se usan.

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Unitario | El validador del plan, lo autorizado y la comparación del commit | Claude | Repositorio de git temporal | Sí |
| Aceptación | Que la plantilla y las reglas digan lo que piden los criterios | Ing. José Dúmar Jiménez Ruíz | Lectura | No |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01, CA-03 y CA-04 |
| Compatibilidad | ☑ | Los planes aprobados antes no se revisan |

### 3.3 Técnicas de diseño de casos

- Partición: archivo declarado, autorizado por regla, de la fase y ninguno; plan aprobado antes y desde 48.0.0.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-01, CA-03 y CA-04 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Las pruebas de la fase: `validadores/tests/test_nada_fuera_del_plan.py`; `validar.py estandar`, `flujo` y `plan --preparados`, y `marcas.py` sobre los archivos de la fase.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-007 | CA-01 | CP-001 | Funcional | Alta | Sí | ☑ |
| HU-007 | CA-03 | CP-002 | Funcional | Alta | Sí | ☑ |
| HU-007 | CA-04 | CP-003 | Funcional | Alta | Sí | ☑ |
| HU-007 | RNF-06 | CP-004 | Trazabilidad | Media | Parcial | ☑ |

**Cobertura:** 3 de 3 criterios de esta fase y el RNF-06.

## 6. Casos de prueba

### CP-001 · El plan dice qué toca y quién lo aprobó

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-01 |
| **Precondiciones** | T-01 y T-02 terminadas |
| **Datos de entrada** | Planes de prueba aprobados con 48.0.0 |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer la plantilla del plan | La sección 0 pide la aprobación con quién, cuándo y versión; la 2.1 pide rutas exactas |
| 2 | Validar un plan con una fila que es una carpeta, un comodín o una descripción | Una falla por fila |
| 3 | Validar un plan sin quién o sin fecha en la aprobación | Una falla |
| 4 | Validar un plan aprobado con 47.0.0 con esas filas | Ninguna falla |

### CP-002 · El commit con un archivo no declarado se rechaza

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-03 |
| **Precondiciones** | T-05 a T-07 terminadas |
| **Datos de entrada** | Un repositorio de git de prueba con una fase y su plan |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Preparar un archivo que el plan declara y correr `validar.py plan --preparados` | Pasa |
| 2 | Preparar uno que el plan no declara ni ninguna regla autoriza | Falla y nombra el archivo |
| 3 | Preparar un documento de la propia fase y el resumen de la sesión | Pasan |
| 4 | Leer el `pre-commit` que escribe el instalador | Corre `validar.py plan --preparados` |

### CP-003 · Lo que autorizan las reglas, también las del proyecto

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-04 |
| **Precondiciones** | T-03 a T-05 terminadas |
| **Datos de entrada** | Reglas de prueba de `base/` y una regla `P1` en `.agente/reglas-proyecto.md` |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer las diez reglas de la línea base | Cada una trae su línea «Autoriza escribir» |
| 2 | Preguntar a `autorizado.py` por un análisis, un guion y la memoria | Dice la regla que los autoriza |
| 3 | Preparar para el commit un archivo que solo autoriza la `P1` | Pasa |

### CP-004 · Cada tarea cita su criterio

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / RNF-06 |
| **Precondiciones** | Fase terminada |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validar.py flujo` y leer el plan | Ninguna tarea sin su criterio |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Un commit con un archivo no autorizado pasa, o uno autorizado se rechaza | Antes de cerrar la fase |
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
