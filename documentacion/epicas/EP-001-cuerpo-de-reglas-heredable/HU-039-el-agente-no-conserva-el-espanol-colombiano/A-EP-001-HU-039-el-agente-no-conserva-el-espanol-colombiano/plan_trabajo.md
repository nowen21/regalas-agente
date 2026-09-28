# Plan de Trabajo · Fase `A-EP-001-HU-039-el-agente-no-conserva-el-espanol-colombiano` (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba acepta el alcance y el costo. El requisito vive en la HU, el detalle de las pruebas en el `plan_pruebas` de la misma fase, y lo que quedó hecho en el `funcionalidad_implementada.md` del cierre.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-001-HU-039-el-agente-no-conserva-el-espanol-colombiano` |
| **Épica** | [EP-001](../../epica.md) |
| **HU** | [HU-039](../HU-039-el-agente-no-conserva-el-espanol-colombiano.md), una sola (`F12.1`) |
| **Módulo** | Cuerpo de reglas, capítulo 00 |
| **Especificación del módulo** | Las reglas de negocio RN-01 a RN-04 de la HU-039 |
| **Fecha apertura** | 2026-09-27 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- Funcionalidad nueva: la regla `00·ID12` y su anexo `espanol-de-colombia.md`. Salen del [pendiente 96](../../../../../pendientes/96-el-agente-no-conserva-el-espanol-colombiano.md): ninguna regla exigía la norma del español de Colombia.

**CA de la HU que cubre esta fase** (trazabilidad `13·DOC11`):

| CA de HU-039 que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-039-el-agente-no-conserva-el-espanol-colombiano.md#ca-01--la-regla-existe-con-su-identificador-y-su-checklist) | ☐ |
| [CA-02](../HU-039-el-agente-no-conserva-el-espanol-colombiano.md#ca-02--el-cuerpo-de-la-regla-recoge-las-reglas-de-negocio) | ☐ |
| [CA-03](../HU-039-el-agente-no-conserva-el-espanol-colombiano.md#ca-03--el-anexo-existe-con-sus-cuatro-secciones) | ☐ |
| [CA-04](../HU-039-el-agente-no-conserva-el-espanol-colombiano.md#ca-04--el-léxico-queda-en-un-solo-sitio) | ☐ |
| [CA-05](../HU-039-el-agente-no-conserva-el-espanol-colombiano.md#ca-05--el-ejemplo-incumple-los-cuatro-frentes) | ☐ |
| [CA-06](../HU-039-el-agente-no-conserva-el-espanol-colombiano.md#ca-06--un-proyecto-que-no-declara-español-de-colombia-no-queda-obligado) | ☐ |
| [CA-07](../HU-039-el-agente-no-conserva-el-espanol-colombiano.md#ca-07--la-regla-queda-clasificada-como-validable-en-parte) | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que exista la regla `00·ID12` con su anexo de cuatro secciones, y que el léxico de Colombia quede en un solo sitio.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | La regla existe, con su checklist | Funcional, camino feliz | Baja |
| CA-02 | El cuerpo recoge RN-01 y RN-02 y extiende `ID8` | Funcional, camino feliz | Media |
| CA-03 | El anexo tiene sus cuatro secciones | Funcional, camino feliz | Alta |
| CA-04 | El léxico sale de `marcadores-de-ia.md` | Funcional, camino feliz | Media |
| CA-05 | El ejemplo INCORRECTO falla en los cuatro frentes | Funcional, error | Baja |
| CA-06 | Un proyecto de otro idioma no queda obligado | Funcional, caso borde | Baja |
| CA-07 | Clasificada como validable en parte | Funcional, camino feliz | Baja |
| RNF-01 | Versionada como MENOR | No funcional | Baja |

**Fuera de alcance:**

- Construir el conteo automático en `validadores/marcas.py`; aquí solo se clasifica qué parte se puede contar.
- La persona y la forma verbal, que siguen en `00·ID10`.
- Otras variedades del español y otros idiomas.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medida el 2026-09-27, antes de escribir este plan:

```
validar.py metareglas: 0 fallas, 1 aviso · VERSION 38.1.2
base/00-identidad-y-rol/reglas/: ID1 a ID11, ID12 libre
base/00-identidad-y-rol/espanol-de-colombia.md: no existe
```

Quién lee hoy el anexo de marcas:

- `validadores/marcas.py` lo excluye del conteo porque es el catálogo, y no lee su tabla de léxico: el léxico de España no se cuenta hoy. Mover la tabla no le quita nada.
- `adaptadores/claude-code/hook_reglas.py` nombra el anexo en `ANEXO_ID8` y recuerda en cada turno `C5`, `ID8`, `ID9` e `ID10` (`CADA_TURNO`). `ID12` no estará en ese recordatorio si no se agrega.
- `validadores/redaccion.py` ya cuenta *vosotros* y *os* como trato directo (`_TRATO`).

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md` | Nuevo | Estándar | La regla, con su checklist |
| `base/00-identidad-y-rol/espanol-de-colombia.md` | Nuevo | Estándar | El anexo, con sus cuatro secciones |
| `base/00-identidad-y-rol/marcadores-de-ia.md` | Modificar | Estándar | La sección 5 remite al anexo; «Lo que este anexo no cubre» cita `ID10` e `ID12` |
| `base/00-identidad-y-rol/base.md` | Modificar | Estándar | La fila de `ID12` en la tabla del capítulo |
| `adaptadores/claude-code/hook_reglas.py` | Modificar | Adaptador | `ID12` en `CADA_TURNO`, según la duda 1 |
| `validadores/reglas-validables.md` | Modificar | Estándar | `ID12` validable en parte |
| `CHANGELOG.md` y `VERSION` | Modificar | Estándar | `38.2.0`, MENOR |
| `pendientes/96-el-agente-no-conserva-el-espanol-colombiano.md` y `pendientes/README.md` | Modificar | Documentación | Cerrar el pendiente |
| Los documentos de esta fase y la sección 8 de HU-039 | Modificar | Documentación | Estado y enlaces |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Archivo a refactorizar | Cambio de contrato | Archivos que dependen (rompen) | Dónde rompe |
|---|---|---|---|
| `base/00-identidad-y-rol/marcadores-de-ia.md` | La sección 5 pierde su tabla de léxico | Ninguno | `marcas.py` no lee esa tabla; `hook_reglas.py` solo nombra el archivo |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica: la fase no crea ningún servicio.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica: la regla no tiene pantalla. Le llega al agente al abrir la sesión, porque el arranque carga las reglas de `base/`.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El léxico se mueve al anexo y la sección 5 remite a él | Dejarlo en los dos sitios | La RN-04 pide un solo sitio; dos copias se desalinean |
| El nombre del archivo es el de la HU y el encabezado va en imperativo | El encabezado igual al archivo | Mismo criterio que `ID11`: `20·M5` exige título imperativo |
| Extiende `ID8` | Regla suelta | Usa su mecanismo, releer contra una lista cerrada |

### 2.7 Dudas por resolver antes de codificar

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | ¿`ID12` entra en el recordatorio de cada turno (`CADA_TURNO` de `hook_reglas.py`)? Allí están las reglas de redacción, y `ID11` tampoco está | Usuario | Pendiente |

## 3. Desglose de tareas por criterio de aceptación

### CA-01 · La regla existe, con su identificador y su checklist

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Crear el archivo de la regla con encabezado en imperativo, ejemplo y checklist | Estándar | 0,5 h | T-04 | CP-001 |
| T-02 | Agregar su fila a la tabla de `base/00-identidad-y-rol/base.md` | Estándar | 0,2 h | T-01 | CP-001 |

### CA-02 · El cuerpo de la regla recoge las reglas de negocio

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-03 | Redactar el cuerpo con la condición, los cuatro frentes y «extiende `00·ID8`», dentro del molde de `20·M5` | Estándar | 0,5 h | T-01 | CP-002 |

### CA-03 · El anexo existe con sus cuatro secciones

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-04 | Escribir `espanol-de-colombia.md` con ortografía, léxico, gramática y redacción, cada una con su tabla | Estándar | 2 h | — | CP-003 |

### CA-04 · El léxico queda en un solo sitio

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-05 | Llevar la tabla de léxico de la sección 5 al anexo y dejar en su lugar una línea que remite | Estándar | 0,3 h | T-04 | CP-004 |
| T-06 | Cambiar el cierre de `marcadores-de-ia.md` para que cite `ID10` e `ID12` | Estándar | 0,2 h | T-01 | CP-004 |

### CA-05 · El ejemplo incumple los cuatro frentes

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-07 | Escribir el ejemplo INCORRECTO con una falta de cada frente y el CORRECTO que las resuelve | Estándar | 0,2 h | T-03 | CP-005 |

### CA-06 · Un proyecto que no declara español de Colombia no queda obligado

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-08 | Abrir el cuerpo con «Si el proyecto declara español de Colombia» | Estándar | 0,1 h | T-03 | CP-006 |

### CA-07 · La regla queda clasificada como validable en parte

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-09 | Agregar `ID12` a `validadores/reglas-validables.md`, con la parte que se cuenta y la que se lee | Estándar | 0,2 h | T-01 | CP-007 |

### RNF · Requisitos no funcionales

| ID | Tarea | Categoría | Est. | Ev. |
|---|---|---|:--:|---|
| T-10 | Si la duda 1 lo aprueba, agregar `ID12` a `CADA_TURNO` de `hook_reglas.py` | Trazabilidad | 0,2 h | CP-008 |
| T-11 | Registrar la regla en `CHANGELOG.md` y subir `VERSION` a `38.2.0` | Trazabilidad | 0,2 h | CP-008 |
| T-12 | Cerrar el pendiente 96 y actualizar la sección 8 de HU-039 | Trazabilidad | 0,2 h | — |

**Total estimado:** 4,8 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-04, T-01, T-03, T-07, T-08, T-11, T-12
**Paralelizables:** T-02, T-05, T-06, T-09 y T-10, después de la T-01 o de la T-04 según su columna «Depende de».

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | `validar.py metareglas` y leer la tabla del capítulo | CP-001 | | ☐ |
| CA-02 | Leer el cuerpo y correr `validar.py estandar` | CP-002 | | ☐ |
| CA-03 | Abrir el anexo y contar sus secciones | CP-003 | | ☐ |
| CA-04 | Leer la sección 5 y el cierre de `marcadores-de-ia.md` | CP-004 | | ☐ |
| CA-05 | Señalar una falta de cada frente en el ejemplo | CP-005 | | ☐ |
| CA-06 | Leer la condición al comienzo del cuerpo | CP-006 | | ☐ |
| CA-07 | Buscar `ID12` en `reglas-validables.md` | CP-007 | | ☐ |
| RNF-01 | Leer `CHANGELOG.md` y `VERSION` | CP-008 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| CP-001 a CP-008 | Resultado de cada caso | [resultado_pruebas.md](resultado_pruebas.md) |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | El propio repositorio |
| Usuarios de prueba | No aplica: no hay usuarios |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit de la fase. La tabla de léxico vuelve a la sección 5 con la misma reversión.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

No aplica porque la regla se activa con una declaración que el proyecto ya hace, y ningún documento ya escrito se reabre (RNF-02). Por eso es MENOR.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

- Base: `20·M3` (la condición la deja entrar en `base/`), `20·M4` (siguiente identificador libre), `20·M5` (una sola exigencia, título imperativo, ejemplo), `20·M7` (`extiende`), `20·M9` (validable en parte), `20·M10` (versionar), `02·F23` (el pendiente se construye como fase de su HU).

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que el anexo se llene de localismos que no se entienden en todo el país | El texto deja de ser claro para lectores de otras regiones | Cada entrada lleva la palabra que se usa y se entiende en todo el país | Abierto |
| B-02 | Que el cuerpo no quepa en 320 caracteres leídos con la condición y los cuatro frentes | El checklist reprueba la fila 10 | Los frentes se nombran; su detalle va al anexo | Abierto |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] RNF-01 validado
- [ ] `metareglas`, `estandar` y `pendientes` sin fallas
- [ ] Señales registradas, si la fase deja alguna decisión no obvia
- [ ] Commit autorizado por el usuario

## 13. Cierre

El cierre va en [funcionalidad_implementada.md](funcionalidad_implementada.md).
