# Plan de Pruebas · Fase `C-EP-023-HU-003-el-proyecto-reporta-a-la-hu-y-se-entera`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP023-HU003-C |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-003: CA-10 y CA-11 |
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
| Unitario | El aviso y el cierre del seguimiento | Claude | Dos carpetas temporales enlazadas | Sí |
| Revisión | La regla y las plantillas | Claude | El repositorio del estándar | No |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-10, CA-11 |

### 3.3 Técnicas de diseño de casos

- Partición por estado: plan sin cumplir, cumplido sin comprobar, cumplido y comprobado; y enlace roto.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-10, CA-11 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Las pruebas de la fase: `validadores/tests/test_el_proyecto_reporta_y_se_entera.py`; las de los programas que cambian: las de `pendientes.py` y `estacion_commit.py` en `validadores/pruebas.py`; `validar.py estandar`, `tareas`, `flujo` y `origen`, y las marcas de lo que se va a guardar.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-003 | CA-10 | CP-001 | Funcional | Alta | No | ☐ |
| HU-003 | CA-11 | CP-002 | Funcional | Alta | Sí | ☐ |
| HU-003 | CA-11 | CP-003 | Funcional | Alta | Sí | ☐ |

**Cobertura:** 2 de 2 criterios de esta fase.

## 6. Casos de prueba

### CP-001 · `02·F24` dice dónde nace el reporte

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-10 |
| **Precondiciones** | T-01 terminada |
| **Datos de entrada** | `02·F24` y las dos plantillas |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `02·F24` | El pendiente nace en la HU que citan la regla o el programa que fallan; si no la citan, en el resumen del día del estándar; la HU se cita cuando un análisis la decide |
| 2 | Leer las dos plantillas | Dicen dónde se crea cada pendiente y que el seguimiento cierra al comprobar |

### CP-002 · El aviso llega al lado del seguimiento

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-11 |
| **Precondiciones** | T-02 y T-03 terminadas |
| **Datos de entrada** | Un pendiente reportado en el estándar, enlazado al hallazgo del proyecto, y ese hallazgo a su seguimiento |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr el aviso con el plan del pendiente sin cumplir | No escribe nada |
| 2 | Cumplir el plan y correr el aviso | Escribe `aviso-resuelto.md` en la carpeta del seguimiento |
| 3 | Correrlo otra vez | No lo duplica |
| 4 | Romper el enlace al seguimiento y correrlo | No escribe y dice qué enlace falta |

### CP-003 · El seguimiento cierra al comprobar

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-11 |
| **Precondiciones** | T-04 terminada |
| **Datos de entrada** | El seguimiento con su aviso |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Consultar el estado con «Comprobado: no» | Abierto |
| 2 | Poner la fecha en «Comprobado» y consultarlo | Cerrado |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | El aviso no llega o el seguimiento cierra sin comprobar | Antes de cerrar la fase |
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
