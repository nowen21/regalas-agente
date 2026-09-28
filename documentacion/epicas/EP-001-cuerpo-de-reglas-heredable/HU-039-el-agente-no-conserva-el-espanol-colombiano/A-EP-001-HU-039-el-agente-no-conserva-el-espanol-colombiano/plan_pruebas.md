# Plan de Pruebas · Fase `A-EP-001-HU-039-el-agente-no-conserva-el-espanol-colombiano`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que ningún criterio de aceptación quede sin al menos un caso, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-039 |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-039 |
| **Fecha** | 2026-09-27 |
| **Elaborado por** | El agente |
| **Revisado por** | El usuario |
| **Aprobado por** | El usuario |
| **Estado** | Borrador |

## 3. Estrategia de pruebas

En seco, sobre el propio repositorio. Los validadores comprueban el molde, los enlaces y la clasificación. El contenido de la regla, del anexo y del ejemplo se lee.

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Sistema | Que la regla cumpla su molde y sus enlaces resuelvan | El agente | Local | Sí, con `validar.py` |
| Aceptación | Que la regla, el anexo y el ejemplo digan lo que piden las RN | El usuario | Local | No |
| Regresión | Que `metareglas`, `estandar`, `pendientes` y `marcas` sigan sin fallas | El agente | Local | Sí |

Se corren solo los validadores que la fase toca (`02·F5`): `metareglas`, `estandar`, `pendientes` y `marcas`, este último porque la fase cambia su catálogo.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-039 | [CA-01](../HU-039-el-agente-no-conserva-el-espanol-colombiano.md#ca-01--la-regla-existe-con-su-identificador-y-su-checklist) | [CP-001](#cp-001--la-regla-existe-y-cumple-su-molde) | Funcional | Crítica | Sí | ☐ |
| HU-039 | [CA-02](../HU-039-el-agente-no-conserva-el-espanol-colombiano.md#ca-02--el-cuerpo-de-la-regla-recoge-las-reglas-de-negocio) | [CP-002](#cp-002--el-cuerpo-recoge-las-reglas-de-negocio) | Funcional | Crítica | Parcial | ☐ |
| HU-039 | [CA-03](../HU-039-el-agente-no-conserva-el-espanol-colombiano.md#ca-03--el-anexo-existe-con-sus-cuatro-secciones) | [CP-003](#cp-003--el-anexo-tiene-sus-cuatro-secciones) | Funcional | Crítica | No | ☐ |
| HU-039 | [CA-04](../HU-039-el-agente-no-conserva-el-espanol-colombiano.md#ca-04--el-léxico-queda-en-un-solo-sitio) | [CP-004](#cp-004--el-léxico-queda-en-un-solo-sitio) | Funcional | Alta | No | ☐ |
| HU-039 | [CA-05](../HU-039-el-agente-no-conserva-el-espanol-colombiano.md#ca-05--el-ejemplo-incumple-los-cuatro-frentes) | [CP-005](#cp-005--el-ejemplo-falla-en-los-cuatro-frentes) | Funcional, error | Alta | No | ☐ |
| HU-039 | [CA-06](../HU-039-el-agente-no-conserva-el-espanol-colombiano.md#ca-06--un-proyecto-que-no-declara-español-de-colombia-no-queda-obligado) | [CP-006](#cp-006--la-condición-deja-fuera-a-otro-idioma) | Funcional, caso borde | Alta | No | ☐ |
| HU-039 | [CA-07](../HU-039-el-agente-no-conserva-el-espanol-colombiano.md#ca-07--la-regla-queda-clasificada-como-validable-en-parte) | [CP-007](#cp-007--queda-clasificada-como-validable-en-parte) | Funcional | Alta | No | ☐ |
| HU-039 | RNF-01 | [CP-008](#cp-008--el-cambio-queda-versionado) | Trazabilidad | Media | Parcial | ☐ |

**Cobertura:** 8 de 8 exigencias cubiertas = 100%.

## 6. Casos de prueba

### CP-001 · La regla existe y cumple su molde

| Campo | Valor |
|---|---|
| **HU / CA** | HU-039 / CA-01 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | La T-01 y la T-02 terminadas |
| **Datos de entrada** | El repositorio |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir `base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md` | Encabezado en imperativo, cuerpo, ejemplo INCORRECTO/CORRECTO y checklist en CUMPLE |
| 2 | Abrir `base/00-identidad-y-rol/base.md` | `ID12` está en la tabla, con su enlace |
| 3 | Correr `python validadores/validar.py metareglas` | 0 fallas |

**Resultado esperado final:** la regla existe y el validador la acepta.

### CP-002 · El cuerpo recoge las reglas de negocio

| Campo | Valor |
|---|---|
| **HU / CA** | HU-039 / CA-02 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | La T-03 terminada |
| **Datos de entrada** | El cuerpo de la regla |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar en el cuerpo a qué contenido aplica y con qué condición | Documentos y chat, en un proyecto que declara español de Colombia (RN-01) |
| 2 | Buscar los frentes que nombra | Ortografía, léxico, gramática y redacción (RN-02) |
| 3 | Leer el paréntesis del cuerpo | «extiende `00·ID8`», enlazada |
| 4 | Correr `python validadores/validar.py estandar` | Sin incumplimientos |

**Resultado esperado final:** el cuerpo dice lo que piden las RN y sus enlaces resuelven.

### CP-003 · El anexo tiene sus cuatro secciones

| Campo | Valor |
|---|---|
| **HU / CA** | HU-039 / CA-03 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | La T-04 terminada |
| **Datos de entrada** | `base/00-identidad-y-rol/espanol-de-colombia.md` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir el anexo | Existe |
| 2 | Contar sus secciones `##` | Ortografía, léxico, gramática y redacción, una por frente |
| 3 | Revisar cada sección | Cada una tiene su tabla de qué se escribe y qué no |

**Resultado esperado final:** el anexo cubre los cuatro frentes.

### CP-004 · El léxico queda en un solo sitio

| Campo | Valor |
|---|---|
| **HU / CA** | HU-039 / CA-04 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Alta |
| **Precondiciones** | La T-05 y la T-06 terminadas |
| **Datos de entrada** | `base/00-identidad-y-rol/marcadores-de-ia.md` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar «ordenador» en `marcadores-de-ia.md` | No está: la tabla de léxico salió |
| 2 | Leer la sección 5 | Una línea que remite a `espanol-de-colombia.md` |
| 3 | Leer «Lo que este anexo no cubre» | Ya no dice que la regla «todavía no existe»; cita `ID10` e `ID12` |
| 4 | Correr `python validadores/validar.py marcas` | 0 fallas |

**Resultado esperado final:** el léxico vive solo en el anexo nuevo.

### CP-005 · El ejemplo falla en los cuatro frentes

| Campo | Valor |
|---|---|
| **HU / CA** | HU-039 / CA-05 |
| **Tipo** | Funcional, error |
| **Prioridad** | Alta |
| **Precondiciones** | La T-07 terminada |
| **Datos de entrada** | El ejemplo INCORRECTO/CORRECTO de la regla |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Señalar en el INCORRECTO la falta de ortografía | Hay una |
| 2 | Señalar la falta de léxico | Hay una |
| 3 | Señalar la falta de gramática | Hay una |
| 4 | Señalar la falta de redacción | Hay una |
| 5 | Leer el CORRECTO | Ninguna de las cuatro sigue |

**Resultado esperado final:** el ejemplo enseña los cuatro frentes.

### CP-006 · La condición deja fuera a otro idioma

| Campo | Valor |
|---|---|
| **HU / CA** | HU-039 / CA-06 |
| **Tipo** | Funcional, caso borde |
| **Prioridad** | Alta |
| **Precondiciones** | La T-08 terminada |
| **Datos de entrada** | El cuerpo de la regla |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer el comienzo del cuerpo | Empieza con «Si el proyecto declara español de Colombia» |

**Resultado esperado final:** un proyecto en otro idioma o en otra variedad no queda obligado.

### CP-007 · Queda clasificada como validable en parte

| Campo | Valor |
|---|---|
| **HU / CA** | HU-039 / CA-07 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Alta |
| **Precondiciones** | La T-09 terminada |
| **Datos de entrada** | `validadores/reglas-validables.md` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar `ID12` en `validadores/reglas-validables.md` | Una fila que dice qué se cuenta (tildes de pregunta, signos de apertura, *vosotros*, *os*, léxico de España) y qué se lee (concordancia, régimen de las preposiciones) |

**Resultado esperado final:** la clasificación dice las dos partes.

### CP-008 · El cambio queda versionado

| Campo | Valor |
|---|---|
| **HU / CA** | HU-039 / RNF-01 |
| **Tipo** | Trazabilidad |
| **Prioridad** | Media |
| **Precondiciones** | La T-11 terminada |
| **Datos de entrada** | `VERSION` y `CHANGELOG.md` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir `VERSION` | `38.2.0` |
| 2 | Abrir `CHANGELOG.md` | La entrada `38.2.0` dice qué regla nació y por qué, marcada `**MENOR**` |
| 3 | Correr `python -m unittest -k test_toda_entrada_del_registro_declara_su_tipo validadores/pruebas.py` | OK |

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
| Fallas de `metareglas` y de `marcas` | Conteo | 0 |

El resultado de cada métrica va en el [resultado_pruebas.md](resultado_pruebas.md).

## 15. Aprobación

| Rol | Nombre | Firma | Fecha |
|---|---|---|---|
| Product Owner | El usuario | | |
