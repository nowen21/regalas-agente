# Plan de Pruebas · Fase `C-EP-005-HU-023-las-reglas-llegan-antes-de-actuar`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que ningún criterio de aceptación quede sin al menos un caso, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-023-C |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-023, CA-08 a CA-10 |
| **Fecha** | 2026-09-28 |
| **Elaborado por** | El agente |
| **Revisado por** | El usuario |
| **Aprobado por** | El usuario |
| **Estado** | Aprobado el 2026-09-28 |

## 3. Estrategia de pruebas

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Unitario | Tareas por palabra clave y por acción; registro de lo leído | El agente | Carpeta temporal | Sí |
| Integración | El enganche con entradas como las de la herramienta | El agente | Carpeta temporal | Sí |
| Sistema | Los archivos por tarea sobre el repositorio real | El agente | Local | Sí, con `validar.py tareas` |
| Aceptación | Que el agente, trabajando, se detenga y lea antes de actuar | El usuario | Esta misma sesión, después de instalar | No |

Se corren solo las pruebas que la fase toca (`02·F5`): las de `mapa_tareas`, `recuperar`, `leidas`, `hook_antes`, las del instalador y las del amarre, más `validar.py estandar`, `tareas`, `amarre` y `versionado`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-023 | CA-08 | [CP-001](#cp-001--la-palabra-clave-elige-las-tareas) | Funcional | Crítica | Sí | ☐ |
| HU-023 | CA-09 | [CP-002](#cp-002--ninguna-acción-pasa-sin-sus-reglas-leídas) | Funcional | Crítica | Sí | ☐ |
| HU-023 | CA-10 | [CP-003](#cp-003--los-archivos-por-tarea-no-envejecen) | Funcional, error | Crítica | Sí | ☐ |
| HU-023 | RNF | [CP-004](#cp-004--versionado-amarre-y-pruebas) | Trazabilidad | Media | Parcial | ☐ |

**Cobertura:** 4 de 4, 100%.

## 6. Casos de prueba

### CP-001 · La palabra clave elige las tareas

| Campo | Valor |
|---|---|
| **HU / CA** | HU-023 / CA-08 |
| **Precondiciones** | T-01 a T-03 terminadas |
| **Datos de entrada** | Mensajes reales del 2026-09-28 |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | «Suba» | `tocar-git`, `recibir-pedido` y `responder` |
| 2 | «es sencillo debe entender las reglas no lo que le parezca» | Solo `recibir-pedido` y `responder` |
| 3 | «como así que entendió que yo quería cambiar el estándar?» | Solo `recibir-pedido` y `responder` |
| 4 | «Escriba el plan del estándar» | `escribir-documento`, sin `cambiar-estandar` ni `trabajar-cadena` |
| 5 | «Apruebo los dos planes. Hágalo» | `trabajar-cadena` |
| 6 | Cada mensaje nombra el archivo de reglas de cada tarea | Está la ruta de `base/reglas-por-tarea/` |

### CP-002 · Ninguna acción pasa sin sus reglas leídas

| Campo | Valor |
|---|---|
| **HU / CA** | HU-023 / CA-09 |
| **Precondiciones** | T-04 a T-06 terminadas |
| **Datos de entrada** | Entradas JSON de `PreToolUse`, `PostToolUse`, `Stop` y `SessionStart`, en carpeta temporal |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `Bash` con `git commit -m x`, sin lecturas | Se detiene y nombra el archivo de `tocar-git` y el de `correr-comando` |
| 2 | Anotar la lectura de esos archivos y repetir | Pasa |
| 3 | `Bash` con `python -m unittest pruebas`, sin leer `correr-comando` | Se detiene; ese archivo contiene `02·F5` completa |
| 4 | `Write` de un `.md` en `documentacion/epicas/` | Pide `escribir-documento` y `trabajar-cadena` |
| 5 | `Write` de un `.py` | Pide `cambiar-codigo` |
| 6 | `WebFetch` | Pide `ir-afuera` |
| 7 | Una tarea partida en varios archivos, con uno solo leído | Se detiene y nombra el que falta |
| 8 | `SessionStart` por resumen y repetir el paso 2 | Se vuelve a detener |
| 9 | `Stop` sin haber leído `recibir-pedido` y `responder` | Se detiene una vez; con la marca de que ya se detuvo, pasa |
| 10 | Una acción que no calza en la tabla | Pide `correr-comando` o `cambiar-codigo`, nunca ninguna |

### CP-003 · Los archivos por tarea no envejecen

| Campo | Valor |
|---|---|
| **HU / CA** | HU-023 / CA-10 |
| **Precondiciones** | T-02 terminada |
| **Datos de entrada** | El repositorio, y una copia en carpeta temporal |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir los archivos y correr `validar.py tareas` | Sin fallas |
| 2 | En la copia, cambiar una regla sin volver a escribirlos | Falla, nombrando el archivo |
| 3 | Leer cada parte con la herramienta de lectura | Cabe en una lectura |
| 4 | Contar las reglas de cada archivo | Las mismas que el mapa pone bajo su tarea |

### CP-004 · Versionado, amarre y pruebas

| Campo | Valor |
|---|---|
| **HU / CA** | HU-023 / RNF |
| **Precondiciones** | T-07 a T-09 terminadas |
| **Datos de entrada** | `VERSION`, `CHANGELOG.md` y las pruebas tocadas |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `VERSION` y `CHANGELOG.md` | `39.6.0`, MENOR, en palabras llanas |
| 2 | `validar.py estandar`, `tareas`, `amarre` y `versionado` | Sin fallas |
| 3 | Las pruebas de la sección 3 | OK |

## 9. Gestión de defectos

Un caso que no da lo esperado se corrige en la misma fase si está dentro de los archivos de la sección 2.1 del plan de trabajo. Si pide tocar otro archivo, se detiene el trabajo y se le pregunta al usuario (`02·F8`).

| ID | Título | CP | Severidad | Estado | Asignado | Fecha | Cierre |
|---|---|---|---|---|---|---|---|
| | Ninguno todavía | | | | | | |

## 12. Métricas e informe

| Métrica | Fórmula | Meta |
|---|---|---|
| Acciones que pasan sin sus reglas leídas | Casos del CP-002 que pasan de más | 0 |
| Tareas elegidas por palabras que no son la clave | Casos del CP-001 | 0 |

El resultado de cada métrica va en el [resultado_pruebas.md](resultado_pruebas.md).

## 15. Aprobación

| Rol | Nombre | Firma | Fecha |
|---|---|---|---|
| Product Owner | El usuario | «Apruebo los dos planes. Hágalo», en el chat | 2026-09-28 |
