# Plan de Pruebas · Fase `D-EP-023-HU-001-el-analisis-abre-todos-los-casos-y-ordena-las-hu`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP023-HU001-D |
| **Versión** | 2.0, por el análisis 9 |
| **Alcance del plan** | HU-001: CA-17 a CA-26 |
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
| Unitario | Las comprobaciones nuevas de `analisis.py`, la marca con la versión y lo que hace `aprobar()` | Claude | Carpeta temporal | Sí, `test_analisis.py` y `test_analisis_en_curso.py` |
| Sistema | El validador sobre los análisis reales, la suite del estándar y las marcas | Claude | Local, en primer plano | Sí |
| Aceptación | Que las plantillas, las recomendaciones, `DOC25` y el análisis principal digan lo que piden los criterios | Ing. José Dúmar Jiménez Ruíz | Lectura | No |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-17 a CA-26 |
| Seguridad | ☐ | No toca accesos |
| Rendimiento | ☐ | Lee unos pocos archivos de texto |
| Usabilidad | ☐ | No hay interfaz |
| Compatibilidad | ☑ | Los análisis aprobados antes siguen pasando (CA-22) |
| Accesibilidad | ☐ | No hay interfaz |
| Migración de datos | ☐ | Nada se migra |
| Recuperación | ☐ | Revertir el commit basta |

### 3.3 Técnicas de diseño de casos

- Partición: para cada comprobación, un análisis que cumple y uno que no, aprobado antes y después de 44.0.0.
- Inspección: lectura de las plantillas, del archivo de recomendaciones, de `DOC25` y del análisis principal.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-17, CA-18, CA-19, CA-22, CA-24, CA-25 y CA-26 | 100% |
| Media | CA-20, CA-21 y CA-23 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

`test_analisis.py`, `test_analisis_en_curso.py`, `validar.py analisis`, `estandar`, `origen`, `plantilla`, `version` y `flujo`, la suite completa por partes y en primer plano y `marcas.py` sobre los archivos de la fase.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-001 | CA-17 | CP-001 | Funcional | Alta | Parcial | ☐ |
| HU-001 | CA-18 | CP-002 | Funcional | Alta | Parcial | ☐ |
| HU-001 | CA-19 | CP-003 | Funcional | Alta | Parcial | ☐ |
| HU-001 | CA-20 | CP-004 | Funcional | Media | Parcial | ☐ |
| HU-001 | CA-21 | CP-005 | Funcional | Media | No | ☐ |
| HU-001 | CA-22 | CP-006 | Compatibilidad | Alta | Sí | ☐ |
| HU-001 | CA-23 | CP-008 | Funcional | Media | No | ☐ |
| HU-001 | CA-24 | CP-009 | Funcional | Alta | Parcial | ☐ |
| HU-001 | CA-25 | CP-010 | Funcional | Alta | Sí | ☐ |
| HU-001 | CA-26 | CP-011 | Funcional | Alta | Sí | ☐ |
| HU-001 | RNF-06 | CP-007 | Trazabilidad | Media | Parcial | ☐ |

**Cobertura:** 10 de 10 criterios y el RNF-06.

## 6. Casos de prueba

### CP-001 · «Dónde más puede pasar»

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-17 |
| **Precondiciones** | T-01, T-02 y T-09 terminadas |
| **Datos de entrada** | Análisis de prueba aprobados con la versión 44.0.0 |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer la plantilla del análisis | Tiene la sección, con su nota y sus cuatro columnas |
| 2 | Validar un análisis con la sección completa | Ninguna falla |
| 3 | Validar uno sin la sección | Una falla |
| 4 | Validar uno con una fila sin lo que la cubre | Una falla que nombra el caso |

### CP-002 · La tabla de HU con su dependencia y su orden

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-18 |
| **Precondiciones** | T-03, T-04, T-05 y T-09 terminadas |
| **Datos de entrada** | Análisis de prueba aprobados con la versión 44.0.0 |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer la plantilla del análisis y la de la épica | Las dos piden orden, dependencia y razón |
| 2 | Validar una tabla bien ordenada | Ninguna falla |
| 3 | Validar una donde una HU va antes de la que depende | Una falla que nombra las dos HU |
| 4 | Validar una con un puesto sin razón | Una falla |

### CP-003 · Las recomendaciones

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-19 |
| **Precondiciones** | T-06, T-07, T-08, T-09, T-12 y T-15 terminadas |
| **Datos de entrada** | Archivos de recomendaciones y análisis de prueba |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `plantillas/recomendaciones-del-analisis.md` | Su forma, sus dos niveles y las recomendaciones de arranque, cada una con su análisis de origen |
| 2 | Leer la plantilla del análisis | Abre con «Recomendaciones», que enlaza los dos archivos y pide decir cuáles aplican |
| 3 | Validar una recomendación sin origen y dos con el mismo «qué se hace» | Una falla por cada una |
| 4 | Validar un análisis aprobado con 44.0.0 que no dice cuáles consultó | Una falla |
| 5 | Leer los análisis 1 a 9 del pendiente 103 | Cada uno tiene «Recomendaciones», con la nota del piloto |
| 6 | Correr `validar.py plantilla` sobre el archivo | Sin fallas |
| 7 | Leer el recuerdo | Enlaza la R-1 y conserva que el usuario lo pidió |

### CP-004 · El análisis principal al día

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-20 |
| **Precondiciones** | T-10 y T-11 terminadas |
| **Datos de entrada** | El análisis principal y análisis de prueba |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer el análisis principal | Su contenido es la redacción que forman los aportes, sin «Qué se construye hoy» |
| 2 | Leer la «Lista de análisis» | Tiene los diez análisis, del de la forma anterior al 9, con fecha, resultado y enlace |
| 3 | Validar con un análisis aprobado que no aparece en la lista | Un aviso, aunque se haya aprobado antes de 44.0.0 |

### CP-005 · Medir la respuesta antes de entregarla

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-21 |
| **Precondiciones** | T-13 terminada |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer las recomendaciones de arranque | Una dice que la respuesta se mide contra `00·ID9` antes de entregarla, con su origen en el análisis 8 |

### CP-006 · Lo nuevo no reabre lo aprobado

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-22 |
| **Precondiciones** | T-09 y T-14 terminadas |
| **Datos de entrada** | Los análisis 1 a 9 del repositorio y uno de prueba |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Aprobar un análisis de prueba | La marca dice la fecha, el turno y la versión, y la siguen encontrando `aprobado()` y `turno_aprobado()` |
| 2 | Correr `validar.py analisis` sobre el repositorio | Los análisis 1 a 9 pasan sin lo que exige la 44.0.0 |
| 3 | Validar uno aprobado con 44.0.0 sin las secciones | Falla |

### CP-008 · `DOC25` anota todo análisis aprobado

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-23 |
| **Precondiciones** | T-16 terminada |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `13·DOC25` | Pide anotar cada análisis aprobado en el principal de su alcance, aunque no cambie el sistema, con lo que aportó tal cual |
| 2 | Leer su checklist | Cumple, contra 44.0.0 |

### CP-009 · Lo que suma pasa tal cual al principal

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-24 |
| **Precondiciones** | T-10, T-17, T-18 y T-19 terminadas |
| **Datos de entrada** | Un proyecto de prueba con su principal, y otro con un principal de módulo |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer la plantilla del análisis | Termina con «Lo que aporta al análisis principal», con el resultado y lo que suma |
| 2 | Aprobar un análisis de prueba | Lo que suma queda, letra por letra, al final de la redacción del principal, y su fila al final de la «Lista de análisis» |
| 3 | Aprobar uno dentro de un módulo con principal propio | Queda en el principal del módulo y no en el del proyecto |
| 4 | Cambiar una palabra en el principal y correr el validador | Una falla que nombra el análisis |
| 5 | Correr `validar.py analisis` sobre el repositorio | Los diez análisis del piloto pasan |

### CP-010 · Sin filas no se aprueba

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-25 |
| **Precondiciones** | T-20 terminada |
| **Datos de entrada** | Un análisis de prueba con «Lo que se tiene que hacer» vacía |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Aprobarlo | No tiene la marca, y el aviso dice que falta al menos una fila |

### CP-011 · Sin «Lo que aporta» no se aprueba

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-26 |
| **Precondiciones** | T-21 terminada |
| **Datos de entrada** | Un análisis de prueba sin la sección, y otro con la sección sin lo que suma |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Aprobar cada uno | Ninguno tiene la marca, y el aviso dice qué falta |

### CP-007 · Cada tarea cita su criterio

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
| **Alta** | Un análisis ya aprobado falla, uno nuevo sin las secciones pasa, o lo que suma no llega tal cual al principal | Antes de cerrar la fase |
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
