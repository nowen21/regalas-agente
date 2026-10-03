# Plan de Pruebas · Fase `A-EP-023-HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-suyo`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP023-HU003-A |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-003: CA-01 a CA-08 |
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
| Unitario | El estado calculado, la numeración única, el índice, el validador de fases y la lectura de hallazgos y pendientes | Claude | Carpeta temporal | Sí |
| Sistema | Los validadores sobre el repositorio y las marcas | Claude | Local, en primer plano | Sí |
| Aceptación | Que las plantillas y las reglas digan lo que piden los criterios | Ing. José Dúmar Jiménez Ruíz | Lectura | No |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-01 a CA-08 |
| Seguridad | ☐ | No toca accesos |
| Rendimiento | ☐ | Lee archivos de texto |
| Usabilidad | ☐ | No hay interfaz |
| Compatibilidad | ☑ | Los pendientes y hallazgos viejos siguen pasando |
| Accesibilidad | ☐ | No hay interfaz |
| Migración de datos | ☐ | Nada se mueve |
| Recuperación | ☐ | Revertir el commit basta |

### 3.3 Técnicas de diseño de casos

- Partición: forma nueva y forma vieja; pendiente con plan cumplido y sin cumplir; con análisis aprobado y sin él.
- Inspección: lectura de las plantillas y de las reglas.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-03, CA-04, CA-05, CA-07 y CA-08 | 100% |
| Media | CA-01, CA-02 y CA-06 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Las pruebas de la fase: `test_el_pendiente_tiene_solo_lo_suyo.py`, y las de los programas que cambia (`test_pendientes_historia.py`, `test_el_andamio_levanta_la_historia_y_el_pendiente.py`, `test_aviso_de_vuelta.py`); `validar.py estandar`, `origen`, `fases`, `pendientes` y `flujo`, y `marcas.py` sobre los archivos de la fase. La suite completa no se corre: cada funcionalidad tiene su fase y sus pruebas.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-003 | CA-01 | CP-001 | Funcional | Media | Parcial | ☑ |
| HU-003 | CA-02 | CP-002 | Funcional | Media | No | ☑ |
| HU-003 | CA-03 | CP-003 | Compatibilidad | Alta | Sí | ☑ |
| HU-003 | CA-04 | CP-004 | Funcional | Alta | Sí | ☑ |
| HU-003 | CA-05 | CP-005 | Funcional | Alta | Parcial | ☑ |
| HU-003 | CA-06 | CP-006 | Funcional | Media | Parcial | ☑ |
| HU-003 | CA-07 | CP-007 | Funcional | Alta | Parcial | ☑ |
| HU-003 | CA-08 | CP-008 | Funcional | Alta | Sí | ☑ |
| HU-003 | RNF-06 | CP-009 | Trazabilidad | Media | Parcial | ☑ |

**Cobertura:** 8 de 8 criterios y el RNF-06.

## 6. Casos de prueba

### CP-001 · El pendiente vive dentro de lo que lo genera

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-01 |
| **Precondiciones** | T-09 y T-14 terminadas |
| **Datos de entrada** | Un proyecto de prueba |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer la tabla de `20·M13` y el glosario | La mejora acordada vive en una carpeta `pendientes/` dentro de lo que la origina |
| 2 | Crear un pendiente con el andamio, sin HU | Queda en `historico-chat/resumenes/«hoy»/pendientes/«NNN-slug»/pendiente.md`, y no en la raíz |
| 3 | Crear uno con su HU | Queda en la carpeta `pendientes/` de esa HU |

### CP-002 · Las plantillas tienen solo sus campos

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-02 |
| **Precondiciones** | T-01 y T-02 terminadas |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer las tres plantillas del pendiente | «De dónde sale», «El problema» y «Por qué importa», y nada más |
| 2 | Leer la plantilla del resumen | El hallazgo trae «Qué pasó», «Por qué importa» y «Pendiente», y nada más |

### CP-003 · Los validadores aceptan lo nuevo y lo viejo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-03 |
| **Precondiciones** | T-03 y T-04 terminadas |
| **Datos de entrada** | Un pendiente y un hallazgo con solo sus campos, y otros con la forma vieja |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Validar un pendiente con sus tres partes | Pasa |
| 2 | Validar un hallazgo con sus tres filas | Pasa |
| 3 | Validar `pendientes/` del repositorio | Pasa, también el 103 de la raíz |
| 4 | Leer un resumen viejo con «Estado» escrito | Su estado es el escrito |

### CP-004 · El cierre lo marca el plan

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-04 |
| **Precondiciones** | T-05 terminada |
| **Datos de entrada** | Pendientes de prueba con análisis aprobados que nombran HU |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Consultar uno sin análisis aprobado | Abierto |
| 2 | Consultar uno cuya HU no está terminada | Abierto |
| 3 | Consultar uno con todas sus HU terminadas | Cerrado, y su `pendiente.md` no cambió |

### CP-005 · El hallazgo con estado y retoma calculados

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-05 |
| **Precondiciones** | T-02, T-06 y T-07 terminadas |
| **Datos de entrada** | Un resumen de prueba con hallazgos de la forma nueva |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `13·DOC22` y la plantilla del resumen | Piden el hallazgo de dos campos y el enlace a su pendiente |
| 2 | `resumen.py` sobre un hallazgo sin pendiente | «sin pendiente» |
| 3 | Sobre uno cuyo pendiente sigue abierto | «anotado», y se retoma por el último análisis del pendiente |
| 4 | Sobre uno cuyo pendiente cerró | «resuelto» |

### CP-006 · Sin «Proyecto de origen»

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-06 |
| **Precondiciones** | T-01 y T-08 terminadas |
| **Datos de entrada** | Un pendiente de seguimiento que enlaza un padre |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar «Proyecto de origen» en las plantillas del pendiente, `pendientes.py` y `02·F24` | Ninguno lo exige |
| 2 | Consultar el seguimiento cuyo padre sigue abierto | Abierto |
| 3 | Consultar el seguimiento cuyo padre cerró | Cerrado |

### CP-007 · `pendientes/` queda como historia

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-07 |
| **Precondiciones** | T-03, T-09 y T-10 terminadas |
| **Datos de entrada** | Un proyecto nuevo de prueba |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `02·F13` y `20·M13` | `pendientes/` no se crea y queda como historia |
| 2 | Correr `validar.py pendientes` sobre el repositorio | Los pendientes viejos pasan |
| 3 | Instalar un proyecto nuevo | No tiene `pendientes/`, y `validar.py pendientes` no falla por eso |
| 4 | Comparar `pendientes/` y `pendientes/hecho/` contra el commit anterior | Ningún archivo cambió |

### CP-008 · La carpeta `pendientes/` dentro de lo que origina

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / CA-08 |
| **Precondiciones** | T-11 a T-14 y T-16 terminadas |
| **Datos de entrada** | Épicas, HU y resúmenes de prueba con pendientes, y el repositorio |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr el validador de fases sobre una épica, una HU y un resumen con `pendientes/` | Pasa |
| 2 | Correrlo sobre el repositorio | Ya no falla por el 103, que vive en `EP-023/pendientes/`, ni por `HU-036/pendientes` |
| 2a | Buscar enlaces rotos con `validar.py estandar` y correr `validar.py origen` | Ninguno roto; `origen` lee los análisis del 103 en su lugar nuevo |
| 3 | Pedir el próximo número con pendientes en varias carpetas | Uno más que el mayor de todas |
| 4 | Correr el programa del índice | Escribe `documentacion/pendientes.md` con todos, su número, dónde viven y si su plan cerró |

### CP-009 · Cada tarea cita su criterio

| Campo | Valor |
|---|---|
| **HU / CA** | HU-003 / RNF-06 |
| **Precondiciones** | Fase terminada |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validar.py flujo` y leer el plan | Ninguna tarea sin su criterio |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Un pendiente o un hallazgo viejo deja de pasar, o uno se calcula cerrado sin que su plan se cumpliera | Antes de cerrar la fase |
| **Media** | Un validador falla o un enlace queda roto | Antes de cerrar la fase |
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
| Hallazgos al ejecutar | Hallazgos que salieron al ejecutar el plan | Los que no se podían prever |

### 12.2 Dónde se miden

En el `resultado_pruebas.md` de la fase.
