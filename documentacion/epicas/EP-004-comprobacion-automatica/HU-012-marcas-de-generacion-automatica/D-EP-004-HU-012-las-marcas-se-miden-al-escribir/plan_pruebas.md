# Plan de Pruebas · Fase `D-EP-004-HU-012-las-marcas-se-miden-al-escribir`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que ningún criterio de aceptación quede sin al menos un caso, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-004-012-D |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-012 de EP-004, CA-05 y CA-06 |
| **Fecha** | 2026-09-28 |
| **Elaborado por** | El agente |
| **Revisado por** | El usuario |
| **Aprobado por** | El usuario |
| **Estado** | Aprobado el 2026-09-28 |

## 3. Estrategia de pruebas

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Unitario | Que `marcas.py` mida un texto suelto y `resumen.py` lea las dos formas | El agente | Carpeta temporal | Sí |
| Integración | Que `hook_md.py` devuelva las marcas con una entrada como la de la herramienta | El agente | Carpeta temporal | Sí |
| Aceptación | Que el aviso se entienda y el molde se llene cómodo | El usuario | Local | No |

Se corren solo las pruebas que la fase toca (`02·F5`): las de `hook_md.py`, las de `marcas.py`, las de `resumen.py` y `validar.py estandar` y `versionado`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-012 | CA-05 | [CP-001](#cp-001--al-escribir-llegan-las-marcas-de-lo-escrito) | Funcional | Crítica | Sí | ☐ |
| HU-012 | CA-06 | [CP-002](#cp-002--el-molde-lleno-no-suma-marcas-y-se-sigue-leyendo) | Funcional | Crítica | Sí | ☐ |
| HU-012 | RNF | [CP-003](#cp-003--versionado-y-pruebas) | Trazabilidad | Media | Parcial | ☐ |

**Cobertura:** 3 de 3, 100%.

## 6. Casos de prueba

### CP-001 · Al escribir llegan las marcas de lo escrito

| Campo | Valor |
|---|---|
| **HU / CA** | HU-012 / CA-05 |
| **Tipo** | Funcional |
| **Prioridad** | Crítica |
| **Precondiciones** | La T-01 a la T-03 terminadas |
| **Datos de entrada** | Entradas JSON como las de `Write` y `Edit`, sobre un proyecto temporal |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `Write` de un `.md` con una raya larga como inciso y una viñeta que abre con negrita y dos puntos | Sale con código 0 y el contexto del agente trae las dos marcas, con su línea y qué poner en su lugar |
| 2 | `Edit` del mismo archivo con un texto sin marcas, aunque el archivo tenga marcas viejas | No trae aviso de marcas |
| 3 | `Write` de un `.py` con una raya larga | No trae nada |
| 4 | `Write` de un `.md` con un enlace roto y una marca | Sale con código 2 por el enlace, y las marcas también se nombran |
| 5 | Una marca dentro de un bloque de código | No se reporta |

**Resultado esperado final:** el agente se entera en el turno, y solo de lo que acaba de escribir.

### CP-002 · El molde lleno no suma marcas y se sigue leyendo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-012 / CA-06 |
| **Tipo** | Funcional |
| **Prioridad** | Crítica |
| **Precondiciones** | La T-04 a la T-06 terminadas |
| **Datos de entrada** | Un hallazgo real de la sesión del 2026-09-28 pasado al molde nuevo |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Contar las marcas del molde vacío | Cero |
| 2 | Llenar un hallazgo con el molde nuevo y contar sus marcas | Cero |
| 3 | `resumen.hallazgos()` sobre el resumen nuevo | Da el id, el título y el estado |
| 4 | `resumen.hallazgos()` sobre el resumen de la sesión del 2026-09-28, que usa la forma vieja | Da lo mismo que antes del cambio |
| 5 | `resumen._retoma()` en las dos formas | Da la pregunta que quedó viva |

**Resultado esperado final:** el molde nuevo no produce marcas y nada que leía los resúmenes se rompe.

### CP-003 · Versionado y pruebas

| Campo | Valor |
|---|---|
| **HU / CA** | HU-012 / RNF |
| **Tipo** | Trazabilidad |
| **Prioridad** | Media |
| **Precondiciones** | La T-07 terminada |
| **Datos de entrada** | `VERSION`, `CHANGELOG.md` y las pruebas tocadas |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir `VERSION` y `CHANGELOG.md` | `39.5.0`, entrada MENOR en palabras llanas |
| 2 | Correr `validar.py versionado`, `validar.py estandar` y las pruebas de la sección 3 | 0 fallas y OK |

**Resultado esperado final:** el cambio queda registrado y lo nuevo tiene sus pruebas.

## 9. Gestión de defectos

Un caso que no da lo esperado se corrige en la misma fase si está dentro de los archivos de la sección 2.1 del plan de trabajo. Si pide tocar otro archivo, se detiene el trabajo y se le pregunta al usuario (`02·F8`).

| ID | Título | CP | Severidad | Estado | Asignado | Fecha | Cierre |
|---|---|---|---|---|---|---|---|
| | Ninguno todavía | | | | | | |

## 12. Métricas e informe

| Métrica | Fórmula | Meta |
|---|---|---|
| Marcas del molde lleno | Recuento del paso 2 del CP-002 | 0 |
| Fallas de `estandar` y `versionado` | Conteo | 0 |

El resultado de cada métrica va en el [resultado_pruebas.md](resultado_pruebas.md).

## 15. Aprobación

| Rol | Nombre | Firma | Fecha |
|---|---|---|---|
| Product Owner | El usuario | «Apruebo los dos planes. Hágalo», en el chat | 2026-09-28 |
