# Plan de Pruebas · Fase `A-EP-001-HU-038-el-agente-agrega-informacion-irrelevante-al-asunto`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos y qué resultado se espera de cada paso. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar: lo que pase va en el [resultado_pruebas.md](resultado_pruebas.md).

## 3. Estrategia de pruebas

En seco, sobre el propio repositorio. Los validadores comprueban el molde, los enlaces y la clasificación; el contenido de la regla y la relectura de los pendientes se leen.

**Documentos de referencia:** [HU-038](../HU-038-el-agente-agrega-informacion-irrelevante-al-asunto.md), el [pendiente 95](../../../../../pendientes/95-el-agente-agrega-informacion-irrelevante-al-asunto.md) y el [checklist del estándar](../../../../../base/20-meta-reglas/checklist.md).

**Criterios de salida:**
- `validar.py metareglas`, `estandar` y `pendientes` sin fallas.
- Los siete casos con su resultado esperado.

## 5. Matriz de trazabilidad

| HU | Exigencia | Caso | Tipo | Prioridad |
|---|---|---|---|---|
| HU-038 | CA-01 | [CP-001](#cp-001--la-regla-existe-y-cumple-su-molde) | De ejecución | Crítica |
| HU-038 | CA-02 | [CP-002](#cp-002--el-cuerpo-recoge-las-cuatro-reglas-de-negocio) | De lectura | Crítica |
| HU-038 | CA-03 | [CP-003](#cp-003--la-dependencia-está-declarada-y-resuelve) | De ejecución | Alta |
| HU-038 | CA-04 | [CP-004](#cp-004--queda-clasificada-como-no-validable) | De lectura | Alta |
| HU-038 | CA-05 | [CP-005](#cp-005--los-pendientes-96-y-97-quedan-sin-datos-ajenos) | De lectura, caso de error | Alta |
| HU-038 | CA-06 | [CP-006](#cp-006--lo-pertinente-se-conserva) | De lectura, caso borde | Alta |
| HU-038 | RNF-01 | [CP-007](#cp-007--el-cambio-queda-versionado) | De lectura | Media |

**Cobertura:** 7 de 7 exigencias con caso (100%).

## 6. Casos de prueba

### CP-001 · La regla existe y cumple su molde

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir `base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md` | Tiene encabezado, cuerpo, ejemplo INCORRECTO/CORRECTO y checklist en CUMPLE |
| 2 | Abrir `base/00-identidad-y-rol/base.md` | `ID11` está en la tabla de reglas, con su enlace |
| 3 | Correr `python validadores/validar.py metareglas` | 0 fallas |

### CP-002 · El cuerpo recoge las cuatro reglas de negocio

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer el cuerpo buscando a qué contenido aplica | Documentos y respuestas del chat (RN-01) |
| 2 | Leer el cuerpo buscando contra qué se mide la pertinencia | El tema, el objetivo y el alcance del elemento que se está tratando (RN-02) |
| 3 | Leer el cuerpo buscando qué pasa con lo no pertinente | Se omite aunque sea breve, claro y correcto (RN-03) |
| 4 | Leer el cuerpo y el ejemplo buscando la relación con la extensión | Queda claro que un texto corto también puede incumplirla (RN-04) |

### CP-003 · La dependencia está declarada y resuelve

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer el paréntesis del cuerpo | Dice `extiende` con `00·ID7`, `00·ID8` y `00·ID9`, enlazadas |
| 2 | Correr `python validadores/validar.py estandar` | Sin incumplimientos |

### CP-004 · Queda clasificada como no validable

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar `ID11` en `validadores/reglas-validables.md` | Aparece entre las no validables del capítulo 00, con el motivo: decidir si un dato es pertinente pide leerlo |

### CP-005 · Los pendientes 96 y 97 quedan sin datos ajenos

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar en el pendiente 96 la frase «No entra en HU-037» | No está |
| 2 | Buscar en el pendiente 97 la frase «La épica candidata» | No está |
| 3 | Mostrarle al usuario los dos pendientes | No encuentra nada que sobre |

### CP-006 · Lo pertinente se conserva

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar `00·ID10` en «El problema» del pendiente 96 | Sigue ahí, porque explica qué cubre ya el estándar |

### CP-007 · El cambio queda versionado

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir `VERSION` | `38.1.0` |
| 2 | Abrir `CHANGELOG.md` | La entrada `38.1.0` dice qué regla nació y por qué, y la marca como MENOR |

## 9. Gestión de defectos

Un caso que no da lo esperado se corrige en la misma fase si está dentro de los archivos de la sección 2.1 del plan de trabajo. Si pide tocar otro archivo, se detiene y se le pregunta al usuario (`02·F8`).

## 12. Métricas

| Métrica | Meta |
|---|---|
| Fallas de `metareglas` | 0 |
| Exigencias sin caso | 0 |
| Datos pertinentes quitados de los pendientes 96 y 97 | 0 |
