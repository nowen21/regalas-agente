# Plan de Pruebas · Fase `A-EP-001-HU-038-el-agente-agrega-informacion-irrelevante-al-asunto`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que ningún criterio de aceptación quede sin al menos un caso, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-038 |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-038 |
| **Fecha** | 2026-09-27 |
| **Elaborado por** | El agente |
| **Revisado por** | El usuario |
| **Aprobado por** | El usuario |
| **Estado** | Borrador |

## 3. Estrategia de pruebas

En seco, sobre el propio repositorio. Los validadores comprueban el molde, los enlaces y la clasificación. El contenido de la regla se lee.

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Sistema | Que la regla cumpla su molde y sus enlaces resuelvan | El agente | Local | Sí, con `validar.py` |
| Aceptación | Que la regla diga lo que piden las RN | El usuario | Local | No |
| Regresión | Que `metareglas`, `estandar` y `pendientes` sigan sin fallas | El agente | Local | Sí |

Se corren solo los validadores que la fase toca: `metareglas`, `estandar` y `pendientes` (`02·F5`).

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-038 | [CA-01](../HU-038-el-agente-agrega-informacion-irrelevante-al-asunto.md#ca-01--la-regla-existe-con-su-identificador-y-su-checklist) | [CP-001](#cp-001--la-regla-existe-y-cumple-su-molde) | Funcional | Crítica | Sí | ☐ |
| HU-038 | [CA-02](../HU-038-el-agente-agrega-informacion-irrelevante-al-asunto.md#ca-02--el-cuerpo-de-la-regla-recoge-las-cuatro-reglas-de-negocio) | [CP-002](#cp-002--el-cuerpo-recoge-las-cuatro-reglas-de-negocio) | Funcional | Crítica | No | ☐ |
| HU-038 | [CA-03](../HU-038-el-agente-agrega-informacion-irrelevante-al-asunto.md#ca-03--la-regla-declara-en-qué-se-apoya) | [CP-003](#cp-003--la-dependencia-está-declarada-y-resuelve) | Funcional | Alta | Sí | ☐ |
| HU-038 | [CA-04](../HU-038-el-agente-agrega-informacion-irrelevante-al-asunto.md#ca-04--la-regla-queda-clasificada-como-no-validable) | [CP-004](#cp-004--queda-clasificada-como-no-validable) | Funcional | Alta | No | ☐ |
| HU-038 | RNF-01 | [CP-005](#cp-005--el-cambio-queda-versionado) | Trazabilidad | Media | No | ☐ |

**Cobertura:** 5 de 5 exigencias cubiertas = 100%.

## 6. Casos de prueba

### CP-001 · La regla existe y cumple su molde

| Campo | Valor |
|---|---|
| **HU / CA** | HU-038 / CA-01 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | La T-01 y la T-02 terminadas |
| **Datos de entrada** | El repositorio |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir `base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md` | Tiene encabezado, cuerpo, ejemplo INCORRECTO/CORRECTO y checklist en CUMPLE |
| 2 | Abrir `base/00-identidad-y-rol/base.md` | `ID11` está en la tabla de reglas, con su enlace |
| 3 | Correr `python validadores/validar.py metareglas` | 0 fallas |

**Resultado esperado final:** la regla existe y el validador la acepta.

### CP-002 · El cuerpo recoge las cuatro reglas de negocio

| Campo | Valor |
|---|---|
| **HU / CA** | HU-038 / CA-02 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | La T-03 terminada |
| **Datos de entrada** | El cuerpo de la regla |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar en el cuerpo a qué contenido aplica | Documentos y respuestas del chat (RN-01) |
| 2 | Buscar contra qué se mide la pertinencia | El tema, el objetivo y el alcance del elemento que se trata (RN-02) |
| 3 | Buscar qué pasa con lo no pertinente | Se omite aunque sea breve, claro y correcto (RN-03) |
| 4 | Leer el cuerpo y el ejemplo buscando la relación con la extensión | Queda claro que un texto corto también puede incumplirla (RN-04) |

**Resultado esperado final:** las cuatro reglas de negocio se leen en la regla.

### CP-003 · La dependencia está declarada y resuelve

| Campo | Valor |
|---|---|
| **HU / CA** | HU-038 / CA-03 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Alta |
| **Precondiciones** | La T-04 terminada |
| **Datos de entrada** | El cuerpo de la regla |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer el paréntesis del cuerpo | Dice `extiende` con `00·ID7`, `00·ID8` y `00·ID9`, enlazadas |
| 2 | Correr `python validadores/validar.py estandar` | Sin incumplimientos |

**Resultado esperado final:** la dependencia está declarada como pide `20·M7`.

### CP-004 · Queda clasificada como no validable

| Campo | Valor |
|---|---|
| **HU / CA** | HU-038 / CA-04 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Alta |
| **Precondiciones** | La T-05 terminada |
| **Datos de entrada** | `validadores/reglas-validables.md` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar `ID11` en `validadores/reglas-validables.md` | Aparece entre las no validables del capítulo 00, con su motivo: decidir si un dato es pertinente pide leerlo |

**Resultado esperado final:** la clasificación existe con su motivo.

### CP-005 · El cambio queda versionado

| Campo | Valor |
|---|---|
| **HU / CA** | HU-038 / RNF-01 |
| **Tipo** | Trazabilidad |
| **Prioridad** | Media |
| **Precondiciones** | La T-06 terminada |
| **Datos de entrada** | `VERSION` y `CHANGELOG.md` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir `VERSION` | `38.1.0` |
| 2 | Abrir `CHANGELOG.md` | La entrada `38.1.0` dice qué regla nació y por qué, marcada como `**MENOR**` |

**Resultado esperado final:** el cambio queda registrado con su tipo.

## 9. Gestión de defectos

Un caso que no da lo esperado se corrige en la misma fase si está dentro de los archivos de la sección 2.1 del plan de trabajo. Si pide tocar otro archivo, se detiene el trabajo y se le pregunta al usuario (`02·F8`).

| ID | Título | CP | Severidad | Estado | Asignado | Fecha | Cierre |
|---|---|---|---|---|---|---|---|
| | Ninguno todavía | | | | | | |

## 12. Métricas e informe

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de exigencias | (CA + RNF) con caso / (CA + RNF) totales | 100% |
| Fallas de `metareglas` | Conteo | 0 |

El resultado de cada métrica va en el [resultado_pruebas.md](resultado_pruebas.md).

## 15. Aprobación

| Rol | Nombre | Firma | Fecha |
|---|---|---|---|
| Product Owner | El usuario | | |
