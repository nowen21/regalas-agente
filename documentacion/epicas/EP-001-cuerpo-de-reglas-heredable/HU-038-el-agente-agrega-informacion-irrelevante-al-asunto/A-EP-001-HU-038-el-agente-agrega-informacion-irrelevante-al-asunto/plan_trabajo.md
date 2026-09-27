# Plan de Trabajo · Fase `A-EP-001-HU-038-el-agente-agrega-informacion-irrelevante-al-asunto` (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio antes de darlo por cumplido.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-001-HU-038-el-agente-agrega-informacion-irrelevante-al-asunto` |
| **Épica** | [EP-001](../../epica.md) |
| **HU** | [HU-038](../HU-038-el-agente-agrega-informacion-irrelevante-al-asunto.md), **una sola** (`F12.1`) |
| **Módulo** | Cuerpo de reglas, capítulo 00 |
| **Fecha apertura** | 2026-09-27 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): funcionalidad nueva. Ninguna regla exige que el contenido del agente sea pertinente al asunto; `00·ID9` y `01·C5` solo miden extensión. Sale del [pendiente 95](../../../../../pendientes/95-el-agente-agrega-informacion-irrelevante-al-asunto.md).

**CA de la HU que cubre esta fase:**

| CA de HU-038 | Estado |
|---|---|
| [CA-01](../HU-038-el-agente-agrega-informacion-irrelevante-al-asunto.md#ca-01--la-regla-existe-con-su-identificador-y-su-checklist) · la regla existe | ☐ |
| [CA-02](../HU-038-el-agente-agrega-informacion-irrelevante-al-asunto.md#ca-02--el-cuerpo-de-la-regla-recoge-las-cuatro-reglas-de-negocio) · recoge RN-01 a RN-04 | ☐ |
| [CA-03](../HU-038-el-agente-agrega-informacion-irrelevante-al-asunto.md#ca-03--la-regla-declara-en-qué-se-apoya) · declara en qué se apoya | ☐ |
| [CA-04](../HU-038-el-agente-agrega-informacion-irrelevante-al-asunto.md#ca-04--la-regla-queda-clasificada-como-no-validable) · clasificada como no validable | ☐ |
| [CA-05](../HU-038-el-agente-agrega-informacion-irrelevante-al-asunto.md#ca-05--los-pendientes-96-y-97-cumplen-la-regla) · los pendientes 96 y 97 la cumplen | ☐ |
| [CA-06](../HU-038-el-agente-agrega-informacion-irrelevante-al-asunto.md#ca-06--un-dato-que-parece-ajeno-pero-es-pertinente-se-conserva) · lo pertinente se conserva | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que exista la regla `00·ID11`, con las cuatro reglas de negocio de HU-038, y que los pendientes 96 y 97 queden releídos contra ella.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | La regla existe, con su checklist | Funcional, camino feliz | Baja |
| CA-02 | El cuerpo recoge RN-01 a RN-04 | Funcional, camino feliz | Media |
| CA-03 | Declara que extiende `ID7`, `ID8` e `ID9` | Funcional, camino feliz | Baja |
| CA-04 | Clasificada como no validable | Funcional, camino feliz | Baja |
| CA-05 | Los pendientes 96 y 97 quedan sin datos ajenos | Funcional, error | Media |
| CA-06 | Lo pertinente se conserva | Funcional, caso borde | Media |
| RNF-01 | Versionada como MENOR | No funcional | Baja |

**Fuera de alcance:**
- La extensión del contenido, que sigue en `00·ID9` y `01·C5`.
- Un validador automático: decidir si un dato es pertinente pide leerlo.
- Construir las reglas de los pendientes 96 y 97. Aquí solo se releen.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

### 2.0 La línea base

Medida el 2026-09-27, antes de escribir este plan:

```
validar.py metareglas: 0 fallas, 1 aviso (M17 sobre la entrada 38.0.3) · VERSION 38.0.3
base/00-identidad-y-rol/reglas/: ID1 a ID10, ID11 libre
```

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

Son los mismos que tocó `00·ID10`, la regla anterior del capítulo (commit `83d874a`), más los dos pendientes que se releen.

| Archivo | Tipo | Nota |
|---|---|---|
| `base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md` | Crear | La regla, con su checklist |
| `base/00-identidad-y-rol/base.md` | Modificar | Su fila en la tabla del capítulo |
| `validadores/reglas-validables.md` | Modificar | `ID11` en la lista de no validables del capítulo 00, con su motivo |
| `pendientes/96-la-norma-del-espanol-de-colombia-no-tiene-regla.md` | Modificar, si hace falta | Quitar lo que no sea pertinente |
| `pendientes/97-el-andamio-exige-la-historia-antes-que-el-pendiente.md` | Modificar, si hace falta | Lo mismo |
| `pendientes/95-el-agente-agrega-informacion-irrelevante-al-asunto.md` y `pendientes/README.md` | Modificar | Cerrar el pendiente |
| `CHANGELOG.md` y `VERSION` | Modificar | `38.1.0`, MENOR |
| Los documentos de esta fase y la sección 8 de HU-038 | Modificar | Estado y enlaces |

### 2.2 Matriz de dependencias del refactor

No aplica: la fase no cambia ningún contrato de código. Solo crea un archivo de regla y agrega filas a dos tablas.

### 2.3 Rutas / endpoints y control de acceso

No aplica: la fase no crea ningún servicio.

### 2.4 Punto de entrada en la UI

No aplica: la regla no tiene pantalla. Le llega al agente al abrir la sesión, porque el arranque carga todas las reglas de `base/`.

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Va en el capítulo 00, identidad y rol | En el de documentación | Ahí viven las reglas de cómo escribe el agente: `ID7`, `ID8`, `ID9` e `ID10` |
| Extiende `ID7`, `ID8` e `ID9` | Regla suelta | Lo decidió el usuario: las tres siguen rigiendo y esta suma la pertinencia |
| El nombre del archivo es el de la HU | El imperativo que usa el resto del capítulo, `escribe-solo-…` | Lo decidió el usuario |
| El ejemplo INCORRECTO es la frase sobre HU-037 | Un ejemplo inventado | Es el caso real que dio origen a la regla (`00·ID8`, sección 6: el caso real del proyecto) |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | El título del encabezado de la regla: el del archivo, que describe el problema, o uno en imperativo como el resto del capítulo (*«Escribe solo lo pertinente al asunto»*) | Usuario | Pendiente |

## 3. Desglose de tareas por criterio de aceptación

### CA-01 · La regla existe, con su identificador y su checklist

| ID | Tarea | Est. | Depende de | Ev. |
|---|---|:--:|---|---|
| T-01 | Crear el archivo de la regla con su encabezado, su ejemplo INCORRECTO/CORRECTO y su checklist | 0,5 h | Duda 1 | CP-001 |
| T-02 | Agregar su fila a la tabla de `base/00-identidad-y-rol/base.md` | 0,2 h | T-01 | CP-001 |

### CA-02 · El cuerpo de la regla recoge las cuatro reglas de negocio

| ID | Tarea | Est. | Depende de | Ev. |
|---|---|:--:|---|---|
| T-03 | Redactar el cuerpo con RN-01 a RN-04, dentro del molde de `20·M5` | 0,5 h | T-01 | CP-002 |

### CA-03 · La regla declara en qué se apoya

| ID | Tarea | Est. | Depende de | Ev. |
|---|---|:--:|---|---|
| T-04 | Cerrar el cuerpo con «extiende `00·ID7`, `00·ID8` y `00·ID9`», enlazadas | 0,1 h | T-03 | CP-003 |

### CA-04 · La regla queda clasificada como no validable

| ID | Tarea | Est. | Depende de | Ev. |
|---|---|:--:|---|---|
| T-05 | Agregar `ID11` a la lista de no validables del capítulo 00 en `validadores/reglas-validables.md`, con su motivo | 0,2 h | T-01 | CP-004 |

### CA-05 · Los pendientes 96 y 97 cumplen la regla

| ID | Tarea | Est. | Depende de | Ev. |
|---|---|:--:|---|---|
| T-06 | Releer los pendientes 96 y 97 contra la regla y quitar lo que no sea pertinente | 0,5 h | T-04 | CP-005 |

### CA-06 · Un dato que parece ajeno pero es pertinente se conserva

| ID | Tarea | Est. | Depende de | Ev. |
|---|---|:--:|---|---|
| T-07 | Comprobar que la mención de `00·ID10` sigue en el pendiente 96 después de la T-06 | 0,1 h | T-06 | CP-006 |

### RNF · Requisitos no funcionales

| ID | Tarea | Categoría | Est. | Ev. |
|---|---|---|:--:|---|
| T-08 | Registrar la regla en `CHANGELOG.md` y subir `VERSION` a `38.1.0` | Trazabilidad | 0,2 h | CP-007 |

### Cierre

| ID | Tarea | Est. | Depende de | Ev. |
|---|---|:--:|---|---|
| T-09 | Cerrar el pendiente 95 y actualizar la sección 8 de HU-038 | 0,2 h | T-01 a T-08 | — |

**Total estimado:** 2,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-03, T-04, T-06, T-07, T-08, T-09. La T-02 y la T-05 se hacen en cualquier momento después de la T-01.

Solo se tocan los archivos de la sección 2.1 (`02·F8`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| CA-01 | `validar.py metareglas` y leer la tabla del capítulo | CP-001 | ☐ |
| CA-02 | Leer el cuerpo de la regla contra RN-01 a RN-04 | CP-002 | ☐ |
| CA-03 | Leer la dependencia y correr `validar.py estandar` | CP-003 | ☐ |
| CA-04 | Buscar `ID11` en `reglas-validables.md` | CP-004 | ☐ |
| CA-05 | Releer los pendientes 96 y 97 | CP-005 | ☐ |
| CA-06 | Comprobar que `00·ID10` sigue en el pendiente 96 | CP-006 | ☐ |
| RNF-01 | Leer `CHANGELOG.md` y `VERSION` | CP-007 | ☐ |

## 6. Datos y ambiente de prueba

El propio repositorio.

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit de la fase. La regla no se deroga: nunca llegó a regir.

## 8. Producción y migración incremental  ·  `02·F14` Q12

No obliga a migrar: la regla rige lo que se entregue de aquí en adelante y ningún documento ya escrito se reabre (RNF-02). Por eso es MENOR.

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `20·M4`: `ID11` es el siguiente identificador libre del capítulo.
- `20·M5`: una sola exigencia, cuerpo de una a cuatro líneas, ejemplo INCORRECTO/CORRECTO.
- `20·M7`: la dependencia se declara con `extiende`.
- `20·M9`: se clasifica como no validable.
- `20·M10`: el cambio se versiona y se registra.
- `02·F23`: el pendiente 95 se construye como fase de HU-038.

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que el cuerpo no quepa en el molde de `M5` con las cuatro RN | El checklist reprueba la fila 10 | Las RN se dicen en una frase cada una; lo que no quepa va al porqué del checklist | Abierto |
| B-02 | Que al releer los pendientes 96 y 97 se quite algo pertinente | Se pierde contexto | El CP-006 lo comprueba | Abierto |

## 11. Definition of Done

- [ ] Los CA-01 a CA-06 y el RNF-01, verificados con su evidencia
- [ ] `metareglas`, `estandar` y `pendientes` sin fallas
- [ ] Autorizado el commit por el usuario

## 12. Seguimiento

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

## 13. Cierre

El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
