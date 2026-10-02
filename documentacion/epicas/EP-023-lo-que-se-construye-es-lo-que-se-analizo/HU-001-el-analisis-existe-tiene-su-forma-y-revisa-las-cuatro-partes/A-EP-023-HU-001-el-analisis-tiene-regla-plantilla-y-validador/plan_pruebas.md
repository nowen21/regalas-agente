# Plan de Pruebas · Fase `A-EP-023-HU-001-el-analisis-tiene-regla-plantilla-y-validador`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueba cada criterio de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase, para no perder la línea base aprobada.

| Campo | Valor |
|---|---|
| **Código** | PP-EP023-HU001-A |
| **Versión** | 2.0, del análisis 5 |
| **Alcance del plan** | HU-001: CA-01, CA-02, CA-04, CA-05, CA-06, CA-07 y CA-16 |
| **Fecha** | 2026-10-01 |
| **Elaborado por** | Claude |
| **Revisado por** | Ing. José Dúmar Jiménez Ruíz |
| **Aprobado por** | Ing. José Dúmar Jiménez Ruíz: la versión 1.0 y la 2.0, el 2026-10-01 |
| **Estado** | Aprobado |

Para una fase, la plantilla pide las secciones 3, 5, 6, 9 y 12; las demás son opcionales y no se usan.

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Unitarias | El validador de las cuatro secciones, con análisis completos e incompletos | Claude | Carpeta temporal | Sí |
| Sistema | Reglas, plantillas, tareas y versión sobre el repositorio real | Claude | Local | Sí, con `validar.py` |
| Aceptación | Que las reglas y la plantilla digan lo que pide la HU | Ing. José Dúmar Jiménez Ruíz | Lectura | No |
| Regresión | Que las demás reglas y plantillas sigan pasando | Claude | Local | Sí, con `validar.py estandar` y `plantillas` |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los siete criterios de la fase |
| Seguridad | ☐ | La fase no toca accesos ni credenciales |
| Rendimiento | ☐ | El validador lee pocos archivos |
| Usabilidad | ☐ | No hay interfaz |
| Compatibilidad | ☐ | No hay interfaz |
| Accesibilidad | ☐ | No hay interfaz |
| Migración de datos | ☐ | Nada se migra: los análisis viejos quedan como están |
| Recuperación | ☑ | Revertir el commit deja vigente `DOC8` (plan de trabajo, sección 7) |

### 3.3 Técnicas de diseño de casos

- Partición de equivalencia: análisis aprobado completo, aprobado incompleto y abierto incompleto.
- Valores límite: un análisis al que le falta una sola de las cuatro secciones.
- Inspección: lectura de cada regla y de la plantilla contra el texto del criterio.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Crítica | Que un análisis aprobado sin sus cuatro partes no pase | 100% |
| Alta | Que las reglas y la plantilla digan lo que pide la HU | 100% |
| Media | Versión y CHANGELOG | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Se corre solo lo que la fase toca:

1. La suite nueva: `validadores/tests/test_analisis.py`.
2. Las que dependen de lo tocado: las pruebas de `validadores/plantillas.py`.
3. `validar.py estandar`, `plantillas`, `tareas`, `versionado` y `analisis`.

No se corre la suite completa del estándar.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-001 | CA-01 | CP-001 | Funcional | Alta | Parcial | ☐ |
| HU-001 | CA-04 | CP-002 | Funcional | Alta | Parcial | ☐ |
| HU-001 | CA-05 | CP-003 | Funcional | Alta | Parcial | ☐ |
| HU-001 | CA-02, CA-16 | CP-004 | Funcional | Alta | Parcial | ☐ |
| HU-001 | CA-06 | CP-005 | Funcional, error | Crítica | Sí | ☐ |
| HU-001 | CA-07 | CP-006 | Funcional | Media | Sí | ☐ |
| HU-001 | RNF-06 | CP-007 | Trazabilidad | Media | No | ☐ |

**Cobertura:** 7 de 7 criterios de la fase y el RNF-06.

## 6. Casos de prueba

### CP-001 · `02·F0` pide el análisis en los tres puntos de reparto

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-01 |
| **Precondiciones** | T-01 terminada |
| **Datos de entrada** | `F0` de la versión 39.6.0, como línea base |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer el cuerpo de `F0` | Pide el análisis antes de las épicas, antes de las HU de cada épica y cada vez que entra un pendiente |
| 2 | Comparar sus eslabones con la versión 39.6.0 | No falta ninguno |
| 3 | Medir el cuerpo de `F0` | Cabe en 320 caracteres |
| 4 | Correr `validar.py estandar` | Sin fallas en `F0` |

### CP-002 · `02·F23` pone el análisis antes de la HU

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-04 |
| **Precondiciones** | T-02 terminada |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer el cuerpo de `F23` | El pendiente pasa por su análisis antes de bajar a la HU |
| 2 | Medir el cuerpo de `F23` | Cabe en 320 caracteres |
| 3 | Correr `validar.py estandar` | Sin fallas en `F23` |

### CP-003 · `DOC8` derogada y `DOC24` y `DOC25` en su lugar

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-05 |
| **Precondiciones** | T-03 y T-04 terminadas |
| **Datos de entrada** | Las siete citas a `DOC8` de la línea base |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `DOC8` | Título con `[DEROGADA en 40.0.0 → ver 13·DOC24]`, nota de por qué y el texto original |
| 2 | Leer `DOC24` | El análisis individual cierra al final de su mismo archivo y no se reescribe |
| 3 | Leer `DOC25` | El análisis principal se reescribe con su lista de cambios |
| 4 | Buscar `DOC8` en `base/`, `plantillas/` y `validadores/` | Solo aparece en la regla derogada, en las que la reemplazan y en el CHANGELOG |
| 5 | Leer `validadores/reglas-validables.md` | `DOC24` y `DOC25` están registradas |
| 6 | Correr `validar.py estandar` | Sin fallas en `DOC8`, `DOC24` ni `DOC25`, y los checklists de las dos nuevas en CUMPLE |

### CP-004 · La plantilla del análisis

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-02 y CA-16 |
| **Precondiciones** | T-05 terminada |
| **Datos de entrada** | El borrador de la plantilla |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `plantillas/analisis.md` | Trae la tabla de reglas de redacción, el hallazgo y el pendiente de origen, la conversación, lo que aportó cada parte, las conclusiones, las lecciones aprendidas y lo que se tiene que hacer |
| 2 | Leer la tabla de HU de su propuesta final | Pide la parte del problema que resuelve cada HU |
| 3 | Correr `validar.py plantillas` | La plantilla está registrada y pasa |
| 4 | Correr `validadores/marcas.py` sobre la plantilla | Cero marcas |

### CP-005 · El análisis sin una de las cuatro partes no cierra

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-06 |
| **Precondiciones** | T-06 y T-07 terminadas |
| **Datos de entrada** | Los análisis 1 a 4 del pendiente 103 y copias modificadas en una carpeta temporal |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validar.py analisis` sobre el repositorio | Los análisis 1 a 4 pasan |
| 2 | Copia aprobada del análisis 3 sin la sección «Lo aprendido» | Falla y nombra la sección |
| 3 | Copia aprobada sin la sección del entorno | Falla y nombra la sección |
| 4 | Copia sin la marca «Aprobado» y sin una sección | Pasa: todavía no se cierra |
| 5 | Correr `test_analisis.py` | En verde |
| 6 | Correr `validar.py sitio` | `validadores/analisis.py` está en el mapa del sitio |

### CP-006 · La versión 40.0.0

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-07 |
| **Precondiciones** | T-08 terminada |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer `VERSION` | 40.0.0 |
| 2 | Leer la entrada del CHANGELOG | «⚠ obliga a migrar», lo que cada proyecto tiene que hacer, `20·M10` y `02·F22` |
| 3 | Correr `validar.py versionado` y `tareas` | Sin fallas |

### CP-007 · Cada criterio cita su origen

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / RNF-06 |
| **Precondiciones** | Fase terminada |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Revisar que cada tarea del plan cite su CA y cada CA su «Sale de» | Ninguna tarea ni criterio sin origen |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Crítica** | Un análisis aprobado sin sus cuatro partes pasa el validador | Antes de cerrar la fase |
| **Alta** | Una regla o la plantilla no dice lo que pide su criterio | Antes de cerrar la fase |
| **Media** | Una cita a `DOC8` quedó sin cambiar | Antes de cerrar la fase |
| **Baja** | Una marca de redacción | Antes de cerrar la fase |

### 9.2 Flujo del defecto

Un defecto detiene la ejecución y se anota en el resultado de las pruebas. Si es un error dentro de lo que el plan aprobó, se corrige y se vuelve a correr el caso (análisis 1, conclusión 45). Si está fuera del plan, es un hallazgo: se detiene la fase y vuelve al análisis (análisis 1, conclusión 18).

### 9.3 Contenido mínimo de un reporte

- Caso y paso donde apareció.
- Resultado esperado frente al obtenido.
- Salida del comando o fragmento del archivo.

### 9.4 Registro

Los defectos van en el `resultado_pruebas.md` de la fase.

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de exigencias | Criterios y RNF con caso / criterios y RNF de la fase | 100% |
| Casos ejecutados | Ejecutados / diseñados | 100% |
| Tasa de aprobación | Aprobados / ejecutados | 100% |
| Hallazgos al ejecutar | Hallazgos que salieron al ejecutar el plan (análisis 1, conclusión 41) | Los que no se podían prever |

### 12.2 Dónde se miden

En el `resultado_pruebas.md` de la fase.
