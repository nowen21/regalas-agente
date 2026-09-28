# Plan de Pruebas · Fase `B-EP-001-HU-011-nada-del-proyecto-queda-fuera-del-proyecto`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que ningún criterio de aceptación quede sin al menos un caso, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-011-B |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-011, CA-04 |
| **Fecha** | 2026-09-28 |
| **Elaborado por** | El agente |
| **Revisado por** | El usuario |
| **Aprobado por** | El usuario |
| **Estado** | Aprobado el 2026-09-28 |

## 3. Estrategia de pruebas

En seco, sobre el propio repositorio. Los validadores comprueban el molde de las reglas y sus enlaces. Lo que dicen se lee.

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Sistema | Que `C29` y `C19` cumplan su molde y sus enlaces resuelvan | El agente | Local | Sí, con `validar.py` |
| Aceptación | Que `C29` diga lo que pide RN-06 | El usuario | Local | No |
| Regresión | Que `metareglas`, `estandar` y `pendientes` sigan sin fallas | El agente | Local | Sí |

Se corren solo los validadores que la fase toca (`02·F5`): `metareglas`, `estandar`, `pendientes` y `versionado`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-011 | [CA-04](../HU-011-buscar-antes-de-preguntar.md#ca-04--nada-del-agente-ni-del-proyecto-queda-fuera-de-ellos) | [CP-001](#cp-001--la-regla-existe-y-cumple-su-molde), [CP-002](#cp-002--c19-la-extiende-y-sigue-cumpliendo) | Funcional | Crítica | Parcial | ☐ |
| HU-011 | RNF | [CP-003](#cp-003--el-cambio-queda-versionado-y-el-recuerdo-anotado) | Trazabilidad | Media | Parcial | ☐ |

**Cobertura:** 2 de 2 exigencias cubiertas, 100%.

## 6. Casos de prueba

### CP-001 · La regla existe y cumple su molde

| Campo | Valor |
|---|---|
| **HU / CA** | HU-011 / CA-04 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | La T-01 y la T-02 terminadas |
| **Datos de entrada** | `base/01-conducta.md` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar `## C29` en `base/01-conducta.md` | Encabezado en imperativo |
| 2 | Leer su cuerpo | Una sola exigencia: lo del agente y del proyecto vive en el repositorio y se llega por enlace; lo guardado afuera se corrige en su origen y no se lee de allá (RN-06) |
| 3 | Buscar en el cuerpo el enlace a `04·S9` | Está, y dice que leer afuera vale para lo que no es del proyecto |
| 4 | Leer su ejemplo y la línea de quién la hace cumplir | Un INCORRECTO que es el error real, un CORRECTO que lo resuelve, y la línea con su motivo |
| 5 | Leer su checklist y buscar `C29` en `validadores/reglas-validables.md` | Checklist en CUMPLE; la regla registrada |
| 6 | Correr `python validadores/validar.py metareglas` y `python validadores/validar.py estandar` | Sin incumplimientos |

**Resultado esperado final:** la regla existe, dice lo que pide RN-06 y el validador la acepta.

### CP-002 · `C19` la extiende y sigue cumpliendo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-011 / CA-04 |
| **Tipo** | Funcional, caso borde |
| **Prioridad** | Alta |
| **Precondiciones** | La T-03 terminada |
| **Datos de entrada** | `## C19` en `base/01-conducta.md` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer el cuerpo de `C19` | Dice «extiende `01·C29`», enlazada, y sigue exigiendo lo mismo sobre la memoria |
| 2 | Contar los caracteres de su cuerpo | 320 o menos |
| 3 | Leer su checklist | Vuelto a aplicar el 2026-09-28, en CUMPLE, con la fila 14 en ✅ |

**Resultado esperado final:** `C19` queda como el caso de la memoria dentro de `C29`, sin salirse del molde.

### CP-003 · El cambio queda versionado y el recuerdo anotado

| Campo | Valor |
|---|---|
| **HU / CA** | HU-011 / RNF |
| **Tipo** | Trazabilidad |
| **Prioridad** | Media |
| **Precondiciones** | La T-04 y la T-05 terminadas |
| **Datos de entrada** | `VERSION`, `CHANGELOG.md` y el recuerdo |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir `VERSION` | `39.1.0` |
| 2 | Abrir `CHANGELOG.md` | La entrada `39.1.0` dice qué regla nació y por qué, marcada `**MENOR**`, y abre en palabras llanas |
| 3 | Correr `python validadores/validar.py versionado` y `python -m unittest test_la_entrada_del_registro_se_entiende` desde `validadores/tests` | 0 fallas y OK |
| 4 | Abrir `historico-chat/memory/nada-del-proyecto-queda-en-la-herramienta.md` | Dice que subió a regla `01·C29` y conserva el resto |

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
| Product Owner | El usuario | «Apruebo el plan de trabajo y el plan de pruebas», en el chat | 2026-09-28 |
