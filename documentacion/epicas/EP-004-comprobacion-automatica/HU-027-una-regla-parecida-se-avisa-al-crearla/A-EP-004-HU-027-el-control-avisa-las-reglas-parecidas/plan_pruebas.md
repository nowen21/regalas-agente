# Plan de Pruebas · Fase `A-EP-004-HU-027-el-control-avisa-las-reglas-parecidas`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP004-HU027-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-027: CA-01 a CA-03 y RNF-01 |
| **Fecha** | 2026-10-04 |
| **Elaborado por** | Claude |
| **Revisado por** | Ing. José Dúmar Jiménez Ruíz |
| **Aprobado por** | Ing. José Dúmar Jiménez Ruíz, el 2026-10-04 |
| **Estado** | Aprobado |

Para una fase, la plantilla pide las secciones 3, 5, 6, 9 y 12; las demás son opcionales y no se usan.

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Unitario | La búsqueda y su salida sin el modelo | Claude | Reglas de este repositorio | Sí |
| Integración | El enganche y el subcomando | Claude | Este repositorio, de solo lectura, y repositorios en carpetas temporales | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01 a CA-03 |
| Rendimiento | ☑ | RNF-01 |

### 3.3 Técnicas de diseño de casos

- Un par conocido que tiene que salir (`02·F4` y `02·F25`) y una regla sin parecidas.
- La búsqueda presente y apagada.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-01, CA-02 | 100% |
| Media | CA-03, RNF-01 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

`python manage.py test core.validadores.tests_parecidas core.validadores.tests_reglas` desde `proyectos/cimiento/`, y las marcas de lo que se va a guardar.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-027 | CA-01, RNF-01 | CP-001 | Funcional | Alta | Sí | ☐ |
| HU-027 | CA-02 | CP-002 | Funcional | Alta | Sí | ☐ |
| HU-027 | CA-03 | CP-003 | Funcional | Media | Sí | ☐ |

**Cobertura:** 3 de 3 criterios y 1 de 1 requisito no funcional.

## 6. Casos de prueba

### CP-001 · Al escribir `F25` llega `F4`

| Campo | Valor |
|---|---|
| **HU / CA** | HU-027 / CA-01 y RNF-01 |
| **Precondiciones** | T-03 terminada |
| **Datos de entrada** | La entrada del enganche por la escritura de `F25` |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr el enganche | La salida nombra `02·F4` entre las parecidas, y sale con 0 |
| 2 | Medir el tiempo, con la tabla de palabras ya armada | Menos de 3 s |
| 3 | Traducir las reglas de hoy con la tabla y con la librería | Los mismos números |

### CP-002 · El subcomando, por regla y por commit

| Campo | Valor |
|---|---|
| **HU / CA** | HU-027 / CA-02 |
| **Precondiciones** | T-02 terminada |
| **Datos de entrada** | `F25`; un repositorio con una regla cambiada y preparada |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `validar.py parecidas --regla F25` | Un aviso con `02·F4` entre las parecidas, código 0 |
| 2 | `validar.py parecidas --preparados` | Un aviso por la regla preparada |
| 3 | Sin reglas preparadas | Ningún aviso |

### CP-003 · Sin la búsqueda, lo dice

| Campo | Valor |
|---|---|
| **HU / CA** | HU-027 / CA-03 |
| **Precondiciones** | T-01 terminada |
| **Datos de entrada** | La búsqueda apagada en la prueba |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir las parecidas de `F25` | Dice que no pudo buscar por significado y no nombra ninguna regla |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | El enganche detiene algo, o la búsqueda inventa parecidas sin el modelo | Antes de cerrar la fase |
| **Baja** | Una marca de redacción | Antes de cerrar la fase |

### 9.2 Flujo del defecto

Un defecto se anota en el resultado de las pruebas. Si es un error dentro de lo que el plan aprobó, se corrige y se vuelve a correr el caso. Si para cerrar la fase obliga a tocar algo que el plan no declara, es un hallazgo: se detiene la fase y vuelve al análisis.

### 9.3 Contenido mínimo de un reporte

- Caso y paso donde apareció.
- Resultado esperado frente al obtenido.

### 9.4 Registro

Los defectos van en el `resultado_pruebas.md` de la fase.

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de exigencias | Criterios con caso / criterios de la fase | 100% |
| Casos ejecutados | Ejecutados / diseñados | 100% |

### 12.2 Dónde se miden

En el `resultado_pruebas.md` de la fase.
