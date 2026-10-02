# Plan de Pruebas · Fase `C-EP-023-HU-001-el-analisis-principal-de-cimiento`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueba el criterio de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP023-HU001-C |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-001: CA-08 |
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
| Sistema | Enlaces y marcas del análisis principal y del índice | Claude | Local | Sí, con `validar.py estandar` y `marcas.py` |
| Aceptación | Que el análisis principal diga lo que pide el criterio | Ing. José Dúmar Jiménez Ruíz | Lectura | No |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | El CA-08 |
| Seguridad | ☐ | No toca accesos |
| Rendimiento | ☐ | Es un documento |
| Usabilidad | ☐ | No hay interfaz |
| Compatibilidad | ☐ | No hay interfaz |
| Accesibilidad | ☐ | No hay interfaz |
| Migración de datos | ☐ | Nada se migra |
| Recuperación | ☐ | Revertir el commit basta |

### 3.3 Técnicas de diseño de casos

- Inspección: lectura del documento contra el criterio y contra `13·DOC25`.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | Que el análisis principal exista y lleve su lista de cambios | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

`validar.py estandar` y `validadores/marcas.py` sobre los dos archivos de la fase.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-001 | CA-08 | CP-001, CP-002, CP-003 | Funcional | Alta | Parcial | ☐ |
| HU-001 | RNF-06 | CP-004 | Trazabilidad | Media | No | ☐ |

**Cobertura:** 1 de 1 criterio de la fase y el RNF-06.

## 6. Casos de prueba

### CP-001 · El análisis principal está en `analisis/` y se basa en todo el proyecto

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-08 |
| **Precondiciones** | T-01 terminada |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir `analisis/proyecto-2026-10-02-analisis-principal.md` | Existe |
| 2 | Leer qué dice de Cimiento y de lo que se construye | Enlaza el planteamiento y el índice de épicas, sin copiarlos |
| 3 | Buscar el análisis 1 del pendiente 103 | Está enlazado |

### CP-002 · Lleva su lista de cambios

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-08 |
| **Precondiciones** | T-01 terminada |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer la lista de cambios | Una línea por cada análisis 1, 2, 4 y 5 del pendiente 103, con su fecha y su enlace (`13·DOC25`) |

### CP-003 · El índice lo nombra

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-08 |
| **Precondiciones** | T-02 terminada |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `analisis/README.md` | Nombra el análisis principal y ya no dice que un análisis es una fotografía |
| 2 | Correr `validar.py estandar` | Sin fallas |
| 3 | Medir con `marcas.py` los dos archivos | Ninguna marca nueva |

### CP-004 · Cada tarea cita su criterio

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / RNF-06 |
| **Precondiciones** | Fase terminada |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validar.py flujo` y leer el plan | Ninguna tarea sin su criterio |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Falta el análisis principal o su lista de cambios | Antes de cerrar la fase |
| **Media** | Un enlace roto | Antes de cerrar la fase |
| **Baja** | Una marca de redacción | Antes de cerrar la fase |

### 9.2 Flujo del defecto

Un defecto se anota en el resultado de las pruebas. Si es un error dentro de lo que el plan aprobó, se corrige y se vuelve a correr el caso (análisis 1, conclusión 45). Si está fuera del plan, es un hallazgo: se detiene la fase y vuelve al análisis (análisis 1, conclusión 18).

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
| Hallazgos al ejecutar | Hallazgos que salieron al ejecutar el plan (análisis 1, conclusión 41) | Los que no se podían prever |

### 12.2 Dónde se miden

En el `resultado_pruebas.md` de la fase.
