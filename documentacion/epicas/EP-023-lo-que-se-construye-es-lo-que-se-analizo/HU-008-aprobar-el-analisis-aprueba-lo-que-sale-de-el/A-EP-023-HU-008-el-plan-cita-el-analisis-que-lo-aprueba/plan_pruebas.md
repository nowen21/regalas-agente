# Plan de Pruebas · Fase `A-EP-023-HU-008-el-plan-cita-el-analisis-que-lo-aprueba`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP023-HU008-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-008: CA-01, CA-02 y CA-03 |
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
| Unitario | La aprobación que cita un análisis | Claude | Proyecto de prueba en una carpeta temporal | Sí |
| Revisión | Las reglas, la plantilla y la versión | Claude | Este repositorio | No |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01, CA-02, CA-03 |

### 3.3 Técnicas de diseño de casos

- Partición por la forma de la aprobación (persona o análisis) y por el estado del análisis citado (aprobado o no, nombra la HU o no).

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-02 | 100% |
| Media | CA-01, CA-03 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Las pruebas del programa que cambia: `python manage.py test core.enganches.tests_freno` desde `proyectos/cimiento/`; `validar.py metareglas`, `tareas`, `flujo` y `estandar`, y las marcas de lo que se va a guardar.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-008 | CA-01 | CP-001 | Funcional | Media | No | ☐ |
| HU-008 | CA-02 | CP-002 | Funcional | Alta | Sí | ☐ |
| HU-008 | CA-03 | CP-003 | Funcional | Media | No | ☐ |

**Cobertura:** 3 de 3 criterios de esta fase.

## 6. Casos de prueba

### CP-001 · Las reglas lo dicen

| Campo | Valor |
|---|---|
| **HU / CA** | HU-008 / CA-01 |
| **Precondiciones** | T-01 y T-05 terminadas |
| **Datos de entrada** | `F4`, `F25`, `CHANGELOG.md`, `VERSION` |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `F4` y `F25` | Dicen que el plan que sale de un análisis aprobado y cumple sus filas queda aprobado, y que lo no contemplado pide el OK |
| 2 | Leer `VERSION` y `CHANGELOG.md` | 54.0.0, con su entrada |
| 3 | Correr `validar.py metareglas` y `tareas` | Sin fallas nuevas |

### CP-002 · El programa acepta solo el análisis que vale

| Campo | Valor |
|---|---|
| **HU / CA** | HU-008 / CA-02 |
| **Precondiciones** | T-02 y T-03 terminadas |
| **Datos de entrada** | Una fase con su plan y un análisis en `pendientes/` |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | El plan cita un análisis aprobado que nombra su HU | Cuenta como aprobado, y el freno deja escribir las rutas de su §2.1 |
| 2 | El análisis citado no está aprobado | No cuenta como aprobado |
| 3 | El análisis está aprobado y no nombra la HU | No cuenta como aprobado |
| 4 | El plan lo aprobó una persona, como antes | Cuenta como aprobado |

### CP-003 · La plantilla muestra las dos formas

| Campo | Valor |
|---|---|
| **HU / CA** | HU-008 / CA-03 |
| **Precondiciones** | T-04 terminada |
| **Datos de entrada** | `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer la fila **Aprobación** | Muestra la persona con fecha y versión, y el análisis aprobado con su enlace |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Un plan cuenta como aprobado con un análisis que no vale | Antes de cerrar la fase |
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
