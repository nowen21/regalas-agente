# Plan de Pruebas · Fase `B-EP-001-HU-012-las-reglas-mandan-sobre-la-instruccion-del-momento`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que ningún criterio de aceptación quede sin al menos un caso, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-012-B |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-012, CA-05 |
| **Fecha** | 2026-09-28 |
| **Elaborado por** | El agente |
| **Revisado por** | El usuario |
| **Aprobado por** | El usuario |
| **Estado** | Aprobado el 2026-09-28 |

## 3. Estrategia de pruebas

En seco, sobre el propio repositorio. Los validadores comprueban el molde de la regla y sus enlaces. Lo que la regla dice se lee.

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Sistema | Que la regla cumpla su molde y sus enlaces resuelvan | El agente | Local | Sí, con `validar.py` |
| Aceptación | Que la regla diga lo que pide RN-06 | El usuario | Local | No |
| Regresión | Que `metareglas`, `estandar` y `pendientes` sigan sin fallas | El agente | Local | Sí |

Se corren solo los validadores que la fase toca (`02·F5`): `metareglas`, `estandar`, `pendientes` y `versionado`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-012 | [CA-05](../HU-012-inventario-de-acciones-y-riesgo.md#ca-05--las-reglas-escritas-mandan-sobre-la-instrucción-del-momento) | [CP-001](#cp-001--la-regla-existe-y-cumple-su-molde), [CP-002](#cp-002--la-precedencia-la-nombra) | Funcional | Crítica | Parcial | ☐ |
| HU-012 | RNF | [CP-003](#cp-003--el-cambio-queda-versionado-y-el-recuerdo-anotado) | Trazabilidad | Media | Parcial | ☐ |

**Cobertura:** 2 de 2 exigencias cubiertas, 100%.

## 6. Casos de prueba

### CP-001 · La regla existe y cumple su molde

| Campo | Valor |
|---|---|
| **HU / CA** | HU-012 / CA-05 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | La T-01 y la T-02 terminadas |
| **Datos de entrada** | `base/00-nucleo-blindado.md` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar `## N10` en `base/00-nucleo-blindado.md` | Encabezado en imperativo, marcado `[BLINDADA]` |
| 2 | Leer su cuerpo | Una sola exigencia: la regla escrita gana sobre lo que pida el usuario; el agente dice cuál es y no hace lo pedido; la regla se cambia por el capítulo 20 (RN-06) |
| 3 | Leer su ejemplo | Un INCORRECTO donde el agente hace lo pedido contra la regla, y un CORRECTO donde nombra la regla y espera |
| 4 | Buscar la línea de quién la hace cumplir | Existe, con su motivo |
| 5 | Leer su checklist | En CUMPLE |
| 6 | Correr `python validadores/validar.py metareglas` y `python validadores/validar.py estandar` | Sin incumplimientos |

**Resultado esperado final:** la regla existe, dice lo que pide RN-06 y el validador la acepta.

### CP-002 · La precedencia la nombra

| Campo | Valor |
|---|---|
| **HU / CA** | HU-012 / CA-05 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Alta |
| **Precondiciones** | La T-03 terminada |
| **Datos de entrada** | `plantillas/CLAUDE.md.plantilla` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer el punto 4 | Nombra `N10`, enlazada, y dice que una regla escrita gana sobre la instrucción del momento |

**Resultado esperado final:** cada proyecto ve la regla en su precedencia.

### CP-003 · El cambio queda versionado y el recuerdo anotado

| Campo | Valor |
|---|---|
| **HU / CA** | HU-012 / RNF |
| **Tipo** | Trazabilidad |
| **Prioridad** | Media |
| **Precondiciones** | La T-04 y la T-05 terminadas |
| **Datos de entrada** | `VERSION`, `CHANGELOG.md` y el recuerdo |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir `VERSION` | `39.0.0` |
| 2 | Abrir `CHANGELOG.md` | La entrada `39.0.0` dice qué regla nació y por qué, marcada `**MAYOR**`, y abre en palabras llanas |
| 3 | Correr `python validadores/validar.py versionado` y la prueba `test_la_entrada_del_registro_se_entiende` | 0 fallas y OK |
| 4 | Abrir `historico-chat/memory/reglas-son-decision-del-usuario.md` | Dice que subió a regla `00·N10` y conserva el resto |

**Resultado esperado final:** el cambio queda registrado con su tipo y el recuerdo apunta a la regla.

## 9. Gestión de defectos

Un caso que no da lo esperado se corrige en la misma fase si está dentro de los archivos de la sección 2.1 del plan de trabajo. Si pide tocar otro archivo, se detiene el trabajo y se le pregunta al usuario (`02·F8`).

| ID | Título | CP | Severidad | Estado | Asignado | Fecha | Cierre |
|---|---|---|---|---|---|---|---|
| | Ninguno todavía | | | | | | |

## 12. Métricas e informe

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de exigencias | (CA + RNF) con caso / (CA + RNF) totales | 100% |
| Fallas de `metareglas`, `estandar` y `versionado` | Conteo | 0 |

El resultado de cada métrica va en el [resultado_pruebas.md](resultado_pruebas.md).

## 15. Aprobación

| Rol | Nombre | Firma | Fecha |
|---|---|---|---|
| Product Owner | El usuario | «Apruebo el plan de pruebas», en el chat | 2026-09-28 |
