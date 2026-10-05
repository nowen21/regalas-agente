# Plan de Pruebas · Fase `A-EP-004-HU-026-el-validador-avisa-la-funcion-repetida`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP004-HU026-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-026: CA-01 a CA-05 y RNF-01 |
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
| Unitario | La normalización y la comparación | Claude | Textos en memoria | Sí |
| Integración | El subcomando sobre proyectos | Claude | Proyectos de prueba con git en carpetas temporales | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01 a CA-05 |
| Rendimiento | ☑ | RNF-01 |

### 3.3 Técnicas de diseño de casos

- Partición por cuerpo (igual, igual con otros nombres, distinto) y por nombre (igual, distinto).
- Valores límite del tamaño mínimo de la función.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-02, CA-03, CA-04 | 100% |
| Media | CA-01, CA-05, RNF-01 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

`python manage.py test core.validadores.tests_repetidas core.validadores.tests` desde `proyectos/cimiento/`, y las marcas de lo que se va a guardar.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-026 | CA-01 | CP-001 | Funcional | Media | Sí | ☐ |
| HU-026 | CA-02 | CP-002 | Funcional | Alta | Sí | ☐ |
| HU-026 | CA-03 | CP-003 | Funcional | Alta | Sí | ☐ |
| HU-026 | CA-04 | CP-004 | Funcional | Alta | Sí | ☐ |
| HU-026 | CA-05, RNF-01 | CP-005 | Funcional | Media | Sí | ☐ |

**Cobertura:** 5 de 5 criterios y 1 de 1 requisito no funcional.

## 6. Casos de prueba

### CP-001 · `calidad` usa la separación compartida y da lo mismo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-026 / CA-01 |
| **Precondiciones** | T-01 terminada |
| **Datos de entrada** | Las pruebas de `07·Q3` que ya existen |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr las pruebas de `calidad` | Pasan sin cambios |
| 2 | Buscar las expresiones de funciones fuera de `codigo.py` | No están |

### CP-002 · La copia con otros nombres se avisa

| Campo | Valor |
|---|---|
| **HU / CA** | HU-026 / CA-02 |
| **Precondiciones** | T-02 terminada |
| **Datos de entrada** | Dos archivos `.py` y dos `.php` con la misma función, nombres y variables distintos |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `repetidas` | Un AVISO por par, con las dos funciones, sus archivos y sus líneas, citando `07·Q4` |
| 2 | Mirar el código de salida | 0 |

### CP-003 · Lo que no es copia no se avisa

| Campo | Valor |
|---|---|
| **HU / CA** | HU-026 / CA-03 |
| **Precondiciones** | T-02 terminada |
| **Datos de entrada** | Dos funciones con el mismo nombre y otro cuerpo; dos funciones iguales de una línea |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `repetidas` | Ningún aviso |

### CP-004 · Al guardar se avisa solo la nueva

| Campo | Valor |
|---|---|
| **HU / CA** | HU-026 / CA-04 |
| **Precondiciones** | T-03 terminada |
| **Datos de entrada** | Un repositorio con dos copias versionadas, y un commit preparado que agrega una tercera |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `repetidas --preparados` | Un aviso por la nueva, que nombra la que ya estaba |
| 2 | Sin nada preparado | Ningún aviso |

### CP-005 · En un proyecto que no es Cimiento, y a tiempo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-026 / CA-05 y RNF-01 |
| **Precondiciones** | T-03 terminada |
| **Datos de entrada** | agro-system y Cimiento, de solo lectura |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validar.py repetidas` parado en agro-system | Los avisos nombran archivos de agro-system |
| 2 | Medir el tiempo sobre Cimiento | Menos de 30 s |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Una copia no se avisa, o se avisa lo que no es copia | Antes de cerrar la fase |
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
