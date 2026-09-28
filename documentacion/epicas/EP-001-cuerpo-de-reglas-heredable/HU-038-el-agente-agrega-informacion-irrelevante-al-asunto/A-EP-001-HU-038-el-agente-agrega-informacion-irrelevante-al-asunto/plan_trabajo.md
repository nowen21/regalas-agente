# Plan de Trabajo · Fase `A-EP-001-HU-038-el-agente-agrega-informacion-irrelevante-al-asunto` (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba acepta el alcance y el costo. El requisito vive en la HU, el detalle de las pruebas en el `plan_pruebas` de la misma fase, y lo que quedó hecho en el `funcionalidad_implementada.md` del cierre.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-001-HU-038-el-agente-agrega-informacion-irrelevante-al-asunto` |
| **Épica** | [EP-001](../../epica.md) |
| **HU** | [HU-038](../HU-038-el-agente-agrega-informacion-irrelevante-al-asunto.md), una sola (`F12.1`) |
| **Módulo** | Cuerpo de reglas, capítulo 00 |
| **Especificación del módulo** | Las reglas de negocio RN-01 a RN-04 de la HU-038 |
| **Fecha apertura** | 2026-09-27 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- Funcionalidad nueva: la regla `00·ID11`, que exige que el contenido del agente sea pertinente al asunto que se trata. No estaba prevista: sale del [pendiente 95](../../../../../pendientes/95-el-agente-agrega-informacion-irrelevante-al-asunto.md), al ver que `00·ID9` y `01·C5` solo miden extensión.

**CA de la HU que cubre esta fase** (trazabilidad `13·DOC11`):

| CA de HU-038 que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-038-el-agente-agrega-informacion-irrelevante-al-asunto.md#ca-01--la-regla-existe-con-su-identificador-y-su-checklist) | ☐ |
| [CA-02](../HU-038-el-agente-agrega-informacion-irrelevante-al-asunto.md#ca-02--el-cuerpo-de-la-regla-recoge-las-cuatro-reglas-de-negocio) | ☐ |
| [CA-03](../HU-038-el-agente-agrega-informacion-irrelevante-al-asunto.md#ca-03--la-regla-declara-en-qué-se-apoya) | ☐ |
| [CA-04](../HU-038-el-agente-agrega-informacion-irrelevante-al-asunto.md#ca-04--la-regla-queda-clasificada-como-no-validable) | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que exista la regla `00·ID11`, con las cuatro reglas de negocio de HU-038.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | La regla existe, con su checklist | Funcional, camino feliz | Baja |
| CA-02 | El cuerpo recoge RN-01 a RN-04 | Funcional, camino feliz | Media |
| CA-03 | Declara que extiende `ID7`, `ID8` e `ID9` | Funcional, camino feliz | Baja |
| CA-04 | Clasificada como no validable | Funcional, camino feliz | Baja |
| RNF-01 | Versionada como MENOR | No funcional | Baja |

**Fuera de alcance:**

- La extensión del contenido, que sigue en `00·ID9` y `01·C5`.
- Un validador automático: decidir si un dato es pertinente pide leerlo.
- Aplicar la regla a documentos ya escritos, como los pendientes 96 y 97.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medida el 2026-09-27, antes de escribir este plan:

```
validar.py metareglas: 0 fallas, 1 aviso · VERSION 38.0.5
base/00-identidad-y-rol/reglas/: ID1 a ID10, ID11 libre
```

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

Son los que tocó `00·ID10`, la regla anterior del capítulo (commit `83d874a`) y el pendiente que se cierra.

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md` | Nuevo | Estándar | La regla, con su checklist |
| `base/00-identidad-y-rol/base.md` | Modificar | Estándar | Su fila en la tabla del capítulo |
| `validadores/reglas-validables.md` | Modificar | Estándar | `ID11` entre las no validables del capítulo 00 |
| `pendientes/95-el-agente-agrega-informacion-irrelevante-al-asunto.md` y `pendientes/README.md` | Modificar | Documentación | Cerrar el pendiente |
| `CHANGELOG.md` y `VERSION` | Modificar | Estándar | `38.1.0`, MENOR |
| Los documentos de esta fase y la sección 8 de HU-038 | Modificar | Documentación | Estado y enlaces |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

No aplica: la fase no cambia ningún contrato de código. Crea un archivo de regla y agrega filas a dos tablas.

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica: la fase no crea ningún servicio.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica: la regla no tiene pantalla. Le llega al agente al abrir la sesión, porque el arranque carga todas las reglas de `base/`.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Va en el capítulo 00, identidad y rol | En el de documentación | Ahí viven las reglas de cómo escribe el agente: `ID7`, `ID8`, `ID9` e `ID10` |
| Extiende `ID7`, `ID8` e `ID9` | Regla suelta | Lo decidió el usuario: las tres siguen rigiendo y esta suma la pertinencia |
| El nombre del archivo es el de la HU | El imperativo del resto del capítulo, `escribe-solo-...` | Lo decidió el usuario |
| El ejemplo INCORRECTO es la frase sobre HU-037 | Un ejemplo inventado | Es el caso real que dio origen a la regla |

### 2.7 Dudas por resolver antes de codificar

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | El título del encabezado de la regla: el mismo del archivo o uno en imperativo como el resto del capítulo («Escribe solo lo pertinente al asunto») | Usuario | Pendiente |

## 3. Desglose de tareas por criterio de aceptación

### CA-01 · La regla existe, con su identificador y su checklist

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Crear el archivo de la regla con su encabezado, su ejemplo INCORRECTO/CORRECTO y su checklist | Estándar | 0,5 h | Duda 1 | CP-001 |
| T-02 | Agregar su fila a la tabla de `base/00-identidad-y-rol/base.md` | Estándar | 0,2 h | T-01 | CP-001 |

### CA-02 · El cuerpo de la regla recoge las cuatro reglas de negocio

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-03 | Redactar el cuerpo con RN-01 a RN-04, dentro del molde de `20·M5` | Estándar | 0,5 h | T-01 | CP-002 |

### CA-03 · La regla declara en qué se apoya

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-04 | Cerrar el cuerpo con «extiende `00·ID7`, `00·ID8` y `00·ID9`», enlazadas | Estándar | 0,1 h | T-03 | CP-003 |

### CA-04 · La regla queda clasificada como no validable

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-05 | Agregar `ID11` a las no validables del capítulo 00 en `validadores/reglas-validables.md`, con su motivo | Estándar | 0,2 h | T-01 | CP-004 |

### RNF · Requisitos no funcionales

| ID | Tarea | Categoría | Est. | Ev. |
|---|---|---|:--:|---|
| T-06 | Registrar la regla en `CHANGELOG.md` y subir `VERSION` a `38.1.0` | Trazabilidad | 0,2 h | CP-005 |
| T-07 | Cerrar el pendiente 95 y actualizar la sección 8 de HU-038 | Trazabilidad | 0,2 h | — |

**Total estimado:** 1,9 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-03, T-04, T-06, T-07
**Paralelizables:** T-02 y T-05, en cualquier momento después de la T-01.

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | `validar.py metareglas` y leer la tabla del capítulo | CP-001 | | ☐ |
| CA-02 | Leer el cuerpo contra RN-01 a RN-04 | CP-002 | | ☐ |
| CA-03 | Leer la dependencia y correr `validar.py estandar` | CP-003 | | ☐ |
| CA-04 | Buscar `ID11` en `reglas-validables.md` | CP-004 | | ☐ |
| RNF-01 | Leer `CHANGELOG.md` y `VERSION` | CP-005 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| CP-001 a CP-005 | Resultado de cada caso | [resultado_pruebas.md](resultado_pruebas.md) |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | El propio repositorio |
| Usuarios de prueba | No aplica: no hay usuarios |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit de la fase. La regla no se deroga: nunca llegó a regir.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

No aplica porque la regla rige lo que se entregue de aquí en adelante y ningún documento ya escrito se reabre (RNF-02). Por eso es MENOR.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

- Base: `20·M4` (siguiente identificador libre), `20·M5` (una sola exigencia, cuerpo de una a cuatro líneas, ejemplo INCORRECTO/CORRECTO), `20·M7` (la dependencia con `extiende`), `20·M9` (no validable), `20·M10` (versionar y registrar), `02·F23` (el pendiente se construye como fase de su HU).

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que el cuerpo no quepa en el molde de `M5` con las cuatro RN | El checklist reprueba la fila 10 | Una frase por RN; lo que no quepa va al porqué del checklist | Abierto |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] RNF-01 validado
- [ ] `metareglas`, `estandar` y `pendientes` sin fallas
- [ ] Señales registradas, si la fase deja alguna decisión no obvia
- [ ] Commit autorizado por el usuario

## 13. Cierre

El cierre va en [funcionalidad_implementada.md](funcionalidad_implementada.md).
