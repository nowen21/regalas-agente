# Plan de Pruebas · Fase `B-EP-023-HU-003-cada-analisis-deja-el-pendiente-en-su-version-siguiente`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP023-HU003-B |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-003: CA-09 |
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
| Unitario | La aprobación revisa el hallazgo en el pendiente | Claude | Proyecto de prueba en una carpeta temporal | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-09 |

### 3.3 Técnicas de diseño de casos

- Partición por análisis: el 1, uno con el hallazgo en el pendiente, uno sin él y uno sin número de hallazgo.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-09 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Las pruebas de la fase: `validadores/tests/test_el_analisis_mejora_su_pendiente.py`; las del programa que cambia: `validadores/tests/test_analisis_en_curso.py`; `validar.py estandar`, `flujo` y `origen`, y las marcas de lo que se va a guardar.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-003 | CA-09 | CP-001 | Funcional | Alta | Sí | ☐ |
| HU-003 | CA-09 | CP-002 | Funcional | Alta | Sí | ☐ |
| HU-003 | CA-09 | CP-003 | Funcional | Media | No | ☐ |

**Cobertura:** 1 de 1 criterio de esta fase.

## 6. Casos de prueba

### CP-001 · Sin el hallazgo en el pendiente no se aprueba

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-09 |
| **Precondiciones** | T-01 terminada |
| **Datos de entrada** | Un pendiente y su análisis 2 prendido, con el título `### H-7 · …` en «Hallazgo» y el resto completo |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | «De dónde sale» no cita el H-7; pedir la aprobación | No hay marca, y el aviso dice que falta el H-7 en «De dónde sale» del pendiente |
| 2 | Sumar el H-7 a «De dónde sale» y pedir la aprobación | Queda la marca |
| 3 | «Hallazgo» sin número de hallazgo | No hay marca, y el aviso dice que falta el número |

### CP-002 · El análisis 1 no se revisa

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-09 |
| **Precondiciones** | T-01 terminada |
| **Datos de entrada** | Un pendiente y su análisis 1 prendido, completo |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pedir la aprobación | Queda la marca |

### CP-003 · La plantilla pide el pendiente en su versión siguiente

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-09 |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | `plantillas/analisis.md` |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer la «Propuesta final» | Pide el «Pendiente V«N+1»» y pasarlo al original antes de aprobar |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Se aprueba un análisis cuyo hallazgo falta en el pendiente, o no se aprueba uno completo | Antes de cerrar la fase |
| **Baja** | Una marca de redacción | Antes de cerrar la fase |

### 9.2 Flujo del defecto

Un defecto se anota en el resultado de las pruebas. Si es un error dentro de lo que el plan aprobó, se corrige y se vuelve a correr el caso. Si está fuera del plan y obliga a tocar algo que el plan no declara, es un hallazgo: se detiene la fase y vuelve al análisis.

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
