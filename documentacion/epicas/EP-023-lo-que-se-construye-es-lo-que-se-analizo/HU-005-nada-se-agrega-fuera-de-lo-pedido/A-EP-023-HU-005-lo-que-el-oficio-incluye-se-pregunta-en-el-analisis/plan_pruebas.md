# Plan de Pruebas · Fase `A-EP-023-HU-005-lo-que-el-oficio-incluye-se-pregunta-en-el-analisis`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP023-HU005-A |
| **Versión** | 2.0, del análisis 6 |
| **Alcance del plan** | HU-005: CA-01 a CA-04 |
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
| Sistema | Formato de las reglas, derogación, mapa de tareas, versión y marcas | Claude | Local | Sí, con `validar.py` y `marcas.py` |
| Aceptación | Que `C30` y `F19` se complementen y que los recuerdos no autoricen trabajo fuera del plan | Ing. José Dúmar Jiménez Ruíz | Lectura | No |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01 a CA-04 |
| Seguridad | ☐ | No toca accesos |
| Rendimiento | ☐ | Son documentos |
| Usabilidad | ☐ | No hay interfaz |
| Compatibilidad | ☐ | No hay interfaz |
| Accesibilidad | ☐ | No hay interfaz |
| Migración de datos | ☐ | Nada se migra |
| Recuperación | ☐ | Revertir el commit basta |

### 3.3 Técnicas de diseño de casos

- Inspección: lectura de las reglas y los recuerdos contra los criterios y contra las conclusiones 12, 17, 18 y 45 del análisis 1 y 2, 3, 5 y 6 del análisis 6.
- Comprobación con programa: los validadores del estándar y las pruebas de las derogaciones.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | `C14` derogada y `C30` en su lugar, sin choque con `F19` | 100% |
| Media | Recuerdos, versión y trazabilidad | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

`validar.py estandar`, `metareglas`, `checklist`, `tareas`, `version`, `versiones` y `flujo`; `pytest validadores/tests/test_version_derogaciones.py`; `marcas.py` sobre los archivos de la fase.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-005 | CA-01 | CP-001 | Funcional | Alta | No | ☐ |
| HU-005 | CA-02 | CP-002, CP-003, CP-004 | Funcional | Alta | Parcial | ☐ |
| HU-005 | CA-03 | CP-005 | Funcional | Media | No | ☐ |
| HU-005 | CA-04 | CP-006 | Funcional | Alta | No | ☐ |
| HU-005 | RNF-06 | CP-007 | Trazabilidad | Media | Parcial | ☐ |

**Cobertura:** 4 de 4 criterios y el RNF-06.

## 6. Casos de prueba

### CP-001 · `C30` y `F19` se complementan, y `F19` no choca con `S1`

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-01 |
| **Precondiciones** | T-01 y T-08 terminadas |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `01·C30` y `02·F19` | `F19` pide implementar literal el CA; `C30` dice que lo que el oficio suele incluir no se agrega y se pregunta en el análisis |
| 2 | Buscar un caso que una permita y la otra prohíba | Ninguno |
| 3 | Leer la dependencia de `C30` | Dice «extiende `02·F19`» |
| 4 | Leer qué es lo pedido en `C30` | El CA más lo que exigen las reglas de Cimiento (RN-05) |
| 5 | Leer el ejemplo de `F19` junto a `04·S1` | El ejemplo ya no prohíbe revisar el permiso en el servidor; su checklist está sellado de nuevo |

### CP-002 · `C14` derogada y `C30` escrita con su molde

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-02 |
| **Precondiciones** | T-01 y T-02 terminadas |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer el encabezado de `C14` | `[DEROGADA en 41.0.0 → ver 01·C30]`, con su nota y su texto original debajo (`20·M11`) |
| 2 | Leer `C30` | Una sola exigencia, cuerpo de hasta 320 caracteres, «deroga `01·C14`», ejemplo INCORRECTO/CORRECTO, «Aplica a» y checklist en CUMPLE |
| 3 | Correr `validar.py metareglas` y `checklist` | Sin fallas |
| 4 | Correr `pytest validadores/tests/test_version_derogaciones.py` | Pasan |

### CP-003 · `C25` y `C15` ya no extienden una regla derogada

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-02 |
| **Precondiciones** | T-03 y T-09 terminadas |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `C25` | Dice «extiende `01·C4`», está debajo de `C4` y su checklist está sellado de nuevo |
| 2 | Leer `C15` | Dice «extiende `01·C30`» y su checklist está sellado de nuevo |
| 3 | Comparar lo que exigen las dos con la versión 40.1.0 | Exigen lo mismo |

### CP-004 · Las reglas por tarea, el registro y la versión

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-02 |
| **Precondiciones** | T-06 y T-07 terminadas |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validar.py tareas` | Sin fallas |
| 2 | Buscar `C14` y `C30` en `base/reglas-por-tarea/` | `C30` en escribir-documento y cambiar-codigo; `C14` no aparece |
| 3 | Leer la lista de no validables del capítulo 01 en `validadores/reglas-validables.md` | Nombra `C30`, y `C14` como derogada en 41.0.0 |
| 4 | Correr `validar.py version`, `versiones` y `estandar` | Sin fallas; `VERSION` dice 41.0.0 |
| 5 | Medir con `marcas.py` los archivos tocados | Ninguna marca nueva |

### CP-005 · Los recuerdos solo valen dentro del plan aprobado

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-03 |
| **Precondiciones** | T-04 y T-05 terminadas |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer «Corregir el defecto detectado» | Vale solo dentro del plan aprobado; lo de afuera es un hallazgo |
| 2 | Leer «Una instrucción se cumple entera» | Ningún punto dice que ante lo no previsto se decide y se sigue; un hallazgo detiene la ejecución |
| 3 | Leer sus dos líneas en `historico-chat/memory/memory.md` | Dicen lo mismo que los recuerdos |

### CP-006 · `ID1` rige dentro de lo pedido

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-04 |
| **Precondiciones** | T-10 terminada |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `ID1` | Pide el criterio del oficio dentro de lo pedido y no cita a `C14` |
| 2 | Medir su cuerpo y leer su checklist | Hasta 320 caracteres; checklist en CUMPLE |

### CP-007 · Cada tarea cita su criterio

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / RNF-06 |
| **Precondiciones** | Fase terminada |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validar.py flujo` y leer el plan | Ninguna tarea sin su criterio |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | `C14` sigue rigiendo, o `C30` choca con `F19` o `F19` con `S1` | Antes de cerrar la fase |
| **Media** | Un validador falla o un enlace queda roto | Antes de cerrar la fase |
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
