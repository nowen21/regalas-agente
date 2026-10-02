# Plan de Pruebas · Fase `B-EP-023-HU-001-la-conversacion-pasa-sola-al-analisis`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueba cada criterio de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP023-HU001-B |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-001: CA-03, CA-09, CA-10, CA-11, CA-12, CA-13, CA-14 y CA-15 |
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
| Unitarias | Estado, prender, pausar, aprobar, pasar y abiertos | Claude | Carpeta temporal | Sí |
| Integración | El enganche con la entrada que manda la herramienta | Claude | Carpeta temporal | Sí |
| Sistema | El instalador sobre un proyecto de prueba | Claude | Carpeta temporal con git | Sí |
| Aceptación | Prender, pausar y apagar un análisis de verdad en esta sesión | Ing. José Dúmar Jiménez Ruíz | Esta sesión, después de instalar | No |
| Regresión | Que los demás enganches y validadores sigan pasando | Claude | Local | Sí |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los ocho criterios de la fase |
| Seguridad | ☐ | La fase no toca accesos ni credenciales |
| Rendimiento | ☐ | El enganche lee un archivo de estado y una transcripción |
| Usabilidad | ☐ | No hay interfaz |
| Compatibilidad | ☐ | No hay interfaz |
| Accesibilidad | ☐ | No hay interfaz |
| Migración de datos | ☐ | Nada se migra |
| Recuperación | ☑ | Revertir el commit y volver a instalar deja el estado anterior |

### 3.3 Técnicas de diseño de casos

- Transición de estados: ninguno prendido, prendido, en pausa, prendido otra vez y aprobado.
- Partición de equivalencia: «Analicemos» con pendiente y sin pendiente; un pendiente con análisis abierto y otro sin él.
- Valores límite: el primer análisis de un pendiente (no existe ninguno) y el siguiente de uno aprobado.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Crítica | Que la conversación entre al análisis prendido y no a uno aprobado | 100% |
| Alta | Prender, pausar, apagar, aviso y el instalador | 100% |
| Media | Marcas y etiquetas | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

1. La suite nueva: `validadores/tests/test_analisis_en_curso.py`.
2. Las que dependen de lo tocado: las pruebas del instalador que cuentan enganches.
3. `validar.py amarre`, `estandar`, `metareglas` y `analisis`.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-001 | CA-10 | CP-001 | Funcional | Crítica | Sí | ☐ |
| HU-001 | CA-03 | CP-002 | Funcional | Crítica | Sí | ☐ |
| HU-001 | CA-09, CA-13 | CP-003 | Funcional | Media | Sí | ☐ |
| HU-001 | CA-11 | CP-004 | Funcional | Alta | Sí | ☐ |
| HU-001 | CA-14 | CP-005 | Funcional, error | Alta | Sí | ☐ |
| HU-001 | CA-12 | CP-006 | Funcional | Alta | Sí | ☐ |
| HU-001 | CA-15 | CP-007 | Funcional | Alta | Sí | ☐ |
| HU-001 | RNF-06 | CP-008 | Trazabilidad | Media | No | ☐ |

**Cobertura:** 8 de 8 criterios de la fase y el RNF-06.

## 6. Casos de prueba

### CP-001 · La herramienta escribe en el análisis que nombra el estado

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-10 |
| **Precondiciones** | T-01 terminada |
| **Datos de entrada** | Una transcripción de tres turnos y dos análisis de prueba |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar el enganche en `adaptadores/claude-code/` | `hook_analisis.py` está ahí |
| 2 | Escribir el estado con el segundo análisis y correr `pasar` | Los turnos entran en el segundo y el primero no cambia |
| 3 | Buscar una ruta de análisis escrita dentro del código | No hay ninguna |

### CP-002 · Lo que el usuario agregó no se toca

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-03 |
| **Precondiciones** | T-01 terminada |
| **Datos de entrada** | Un análisis con una nota escrita a mano en «Conclusiones» |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `pasar` dos veces, con un turno nuevo entre una y otra | El turno nuevo entra |
| 2 | Comparar todo lo que está fuera de la sección «Conversación» | Igual al de antes, letra por letra |

### CP-003 · Sin marcas ni etiquetas en lo que escribe la herramienta

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-09 y CA-13 |
| **Precondiciones** | T-02 terminada |
| **Datos de entrada** | Una transcripción con raya en los encabezados, texto pegado y archivo abierto |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `pasar` | Los encabezados llevan coma y no raya |
| 2 | Buscar las etiquetas de texto pegado y de archivo abierto | No están; las palabras del usuario sí |
| 3 | Medir con `marcas.py` las líneas que escribe la herramienta | Cero marcas |

### CP-004 · Prender, pausar, volver a prender y aprobar

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-11 |
| **Precondiciones** | T-03 terminada |
| **Datos de entrada** | Un pendiente de prueba sin análisis |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Mensaje «Analicemos: el pendiente 7» en el turno 2 | Se crea `analisis-1.md` desde la plantilla y el estado arranca en el turno 2 |
| 2 | Mensaje «Pare» en el turno 4, y «Analicemos: el pendiente 7» en el turno 6 | El análisis trae la línea «turnos 4 a 5 en pausa» y no trae esos turnos |
| 3 | Mensaje «Apruebo el análisis» en el turno 7 | El análisis queda con la marca, la fecha y el turno 7 |
| 4 | Pasar la respuesta del turno 7 | El estado se borra; el turno 8 no entra |
| 5 | Mensaje «Analicemos por qué falla esto», sin pendiente | No se prende nada |

### CP-005 · No se prende otro pendiente con un análisis abierto

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-14 |
| **Precondiciones** | T-04 terminada |
| **Datos de entrada** | Dos pendientes; el primero con un análisis aprobado cuya «Pasó a» nombra una HU sin terminar |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | «Analicemos: el pendiente» del segundo | No se prende y el aviso nombra el análisis abierto |
| 2 | «Analicemos: el pendiente» del primero | Se prende su análisis siguiente |
| 3 | Marcar la HU como terminada y repetir el paso 1 | Se prende |

### CP-006 · El aviso de cada turno

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-12 |
| **Precondiciones** | T-05 terminada |
| **Datos de entrada** | La entrada que manda la herramienta en un mensaje |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr el enganche con un análisis prendido | El aviso nombra el análisis; sale con código 0 |
| 2 | Correr el enganche sin ninguno | El aviso dice que ninguno está prendido; sale con código 0 |

### CP-007 · El instalador registra la herramienta

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / CA-15 |
| **Precondiciones** | T-06 terminada |
| **Datos de entrada** | Un proyecto de prueba vacío con git |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validadores/instalar.py` sobre el proyecto | Termina sin error |
| 2 | Leer su `.claude/settings.json` | `hook_analisis.py` está en `UserPromptSubmit` y en `Stop` |
| 3 | Leer el `.claude/settings.json` del estándar | Ya no nombra `pasar_conversacion.py` |
| 4 | Correr `validar.py amarre` | Sin fallas |

### CP-008 · Cada tarea cita su criterio

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / RNF-06 |
| **Precondiciones** | Fase terminada |
| **Datos de entrada** | Ninguno |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Revisar que cada tarea del plan cite su CA y cada CA su «Sale de» | Ninguna sin origen |

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Crítica** | La conversación entra en un análisis aprobado o en otro distinto del prendido | Antes de cerrar la fase |
| **Alta** | Una palabra no prende, no pausa o no apaga; el instalador no registra | Antes de cerrar la fase |
| **Media** | Queda una raya o una etiqueta | Antes de cerrar la fase |
| **Baja** | Una marca de redacción en el aviso | Antes de cerrar la fase |

### 9.2 Flujo del defecto

Un defecto se anota en el resultado de las pruebas. Si es un error dentro de lo que el plan aprobó, se corrige y se vuelve a correr el caso (análisis 1, conclusión 45). Si está fuera del plan, es un hallazgo: se detiene la fase y vuelve al análisis (análisis 1, conclusión 18).

### 9.3 Contenido mínimo de un reporte

- Caso y paso donde apareció.
- Resultado esperado frente al obtenido.
- Salida de la prueba o fragmento del archivo.

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
