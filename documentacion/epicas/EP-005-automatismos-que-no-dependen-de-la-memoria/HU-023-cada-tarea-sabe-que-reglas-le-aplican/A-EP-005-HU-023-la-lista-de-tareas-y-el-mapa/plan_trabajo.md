# Plan de Trabajo · Fase `A-EP-005-HU-023-la-lista-de-tareas-y-el-mapa` (módulo Cuerpo de reglas y validadores)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba acepta el alcance y el costo. El requisito vive en la HU, el detalle de las pruebas en el `plan_pruebas` de la misma fase, y lo que quedó hecho en el `funcionalidad_implementada.md` del cierre.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-023-la-lista-de-tareas-y-el-mapa` |
| **Épica** | [EP-005](../../epica.md) |
| **HU** | [HU-023](../HU-023-cada-tarea-sabe-que-reglas-le-aplican.md), una sola (`F12.1`) |
| **Módulo** | Cuerpo de reglas y `validadores/` |
| **Especificación del módulo** | Las reglas de negocio RN-01 a RN-03 de la HU-023 |
| **Fecha apertura** | 2026-09-28 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- Funcionalidad nueva: la lista de tareas, la línea `**Aplica a:**` y el programa que arma el mapa. Sale del [pendiente 100](../../../../../pendientes/100-cada-tarea-sabe-que-reglas-le-aplican.md), aprobado por el usuario el 2026-09-28.

**CA de la HU que cubre esta fase** (trazabilidad `13·DOC11`):

| CA de HU-023 que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-023-cada-tarea-sabe-que-reglas-le-aplican.md#ca-01--la-lista-de-tareas-existe-y-es-cerrada) | ☐ |
| [CA-02](../HU-023-cada-tarea-sabe-que-reglas-le-aplican.md#ca-02--una-regla-declara-sus-tareas-sin-cambiar-lo-que-exige) | ☐ |
| [CA-03](../HU-023-cada-tarea-sabe-que-reglas-le-aplican.md#ca-03--el-mapa-sale-de-las-reglas) | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que exista la lista cerrada de tareas, que una regla pueda declarar sus tareas sin cambiar lo que exige, y que un programa arme el mapa desde esas declaraciones. Las 10 reglas del núcleo se anotan en esta fase para probar la lista con reglas reales.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | La lista existe y ninguna tarea se superpone con otra | Funcional, camino feliz | Media |
| CA-02 | La línea `**Aplica a:**` no cambia el largo ni anula el checklist | Funcional, caso borde | Baja |
| CA-03 | El mapa sale de las reglas y cambia cuando ellas cambian | Funcional, camino feliz | Media |
| RNF-01 | Versionado | No funcional | Baja |
| RNF-02 | El programa tiene sus pruebas | No funcional | Baja |

**Fuera de alcance:**

- El validador que falla con una regla sin tareas y anotar las 251 reglas que quedan fuera del núcleo: son la fase `B` (CA-04 y CA-05).

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medida el 2026-09-28, antes de escribir este plan:

```
metareglas.py: cuenta 261 reglas
metareglas.py:165: _FUERA_DEL_CUERPO = («Quién la hace cumplir:», «Nadie la hace cumplir:»)
base/tareas.md, base/mapa-de-tareas.md, validadores/mapa_tareas.py: no existen
VERSION: 39.1.0
```

`_FUERA_DEL_CUERPO` se usa en dos sitios de `metareglas.py`: al medir el cuerpo (línea 231) y al comparar el texto con el que se selló el checklist (`_sin_declaracion`, línea 544). Agregar `**Aplica a:**` a esa lista basta para que la línea no cuente en el largo ni anule el checklist.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `base/tareas.md` | Nuevo | Estándar | La lista cerrada de tareas |
| `base/mapa-de-tareas.md` | Nuevo | Estándar | Lo escribe el programa |
| `validadores/mapa_tareas.py` | Nuevo | Validador | Lee las líneas `**Aplica a:**` y escribe el mapa |
| `validadores/tests/test_cada_tarea_sabe_que_reglas_le_aplican.py` | Nuevo | Pruebas | Las pruebas del programa y de la línea |
| `validadores/metareglas.py` | Modificar | Validador | `**Aplica a:**` en `_FUERA_DEL_CUERPO` |
| `base/00-nucleo-blindado.md` | Modificar | Estándar | La línea `**Aplica a:**` en `N1` a `N10` |
| `CHANGELOG.md` y `VERSION` | Modificar | Estándar | `39.2.0`, MENOR |
| Los documentos de esta fase, la sección 8 de HU-023 y el pendiente 100 | Modificar | Documentación | Estado y enlaces |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Archivo a refactorizar | Cambio de contrato | Archivos que dependen (rompen) | Dónde rompe |
|---|---|---|---|
| `validadores/metareglas.py` | `_FUERA_DEL_CUERPO` suma un tercer prefijo | Ninguno | Solo se lee dentro de `metareglas.py`; la tupla crece y ningún uso depende de su tamaño |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica: la fase no crea ningún servicio.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica: no hay pantalla. El mapa se abre como archivo de `base/`, y el programa se corre desde la consola.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La lista en `base/tareas.md` y el mapa en `base/mapa-de-tareas.md`, separados | Un solo archivo | La lista la decide una persona y el mapa lo escribe un programa; si comparten archivo, el programa pisa lo que decidió la persona |
| La línea va fuera del cuerpo, como «Nadie la hace cumplir» | Meterla en el cuerpo | Dentro del cuerpo contaría para el largo y anularía los 261 checklists |
| Se anota el núcleo en esta fase | Anotar todo en la fase `B` | Probar la lista con reglas reales antes de anotar el resto; si la lista falla, se corrige con 10 reglas y no con 261 |

### 2.7 Dudas por resolver antes de codificar

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | La lista de tareas. Propuesta: recibir un pedido, responder en el chat, escribir un documento, cambiar código, correr un comando, tocar git, tocar datos reales, enviar o traer algo de afuera, cambiar el estándar y trabajar la cadena (pendiente, HU, fase). Se prueba con el núcleo y se ajusta antes de cerrar la fase | Usuario | Resuelta el 2026-09-28: el usuario aprobó la propuesta |

## 3. Desglose de tareas por criterio de aceptación

### CA-01 · La lista de tareas existe y es cerrada

> Agrupa las tareas que escriben la lista y la prueban contra el núcleo.

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Escribir `base/tareas.md` con la lista que apruebe el usuario: nombre corto y cuándo aplica cada tarea | Estándar | 0,5 h | Duda 1 | CP-001 |

### CA-02 · Una regla declara sus tareas sin cambiar lo que exige

> Agrupa las tareas que dejan la línea fuera del cuerpo y la ponen en las reglas del núcleo.

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-02 | Agregar `**Aplica a:**` a `_FUERA_DEL_CUERPO` de `validadores/metareglas.py` | Validador | 0,2 h | — | CP-002 |
| T-03 | Anotar `N1` a `N10` con su línea `**Aplica a:**` | Estándar | 0,5 h | T-01, T-02 | CP-002 |

### CA-03 · El mapa sale de las reglas

> Agrupa las tareas que escriben el programa, sus pruebas y el mapa.

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-04 | Escribir `validadores/mapa_tareas.py`: lee las reglas con `metareglas.reglas()`, junta sus tareas y escribe `base/mapa-de-tareas.md` con el enlace a cada regla | Validador | 1,5 h | T-02 | CP-003 |
| T-05 | Escribir sus pruebas en `validadores/tests/test_cada_tarea_sabe_que_reglas_le_aplican.py` | Pruebas | 1 h | T-04 | CP-003 |
| T-06 | Correr el programa y dejar escrito el mapa con las reglas del núcleo | Estándar | 0,1 h | T-03, T-04 | CP-003 |

### RNF · Requisitos no funcionales

> Agrupa las tareas que dejan el cambio registrado y cerrado.

| ID | Tarea | Categoría | Est. | Ev. |
|---|---|---|:--:|---|
| T-07 | Registrar el cambio en `CHANGELOG.md` y subir `VERSION` a `39.2.0` | Trazabilidad | 0,2 h | CP-004 |
| T-08 | Actualizar la sección 8 de HU-023 y el pendiente 100 | Trazabilidad | 0,1 h | — |

**Total estimado:** 4,1 h

## 4. Secuencia de ejecución

**Ruta crítica:** duda 1, T-01, T-03, T-06, T-07, T-08.
**Paralelizables:** T-02 y T-04 no esperan la lista; T-05 va después de T-04.

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Leer la lista y comparar sus tareas de dos en dos | CP-001 | | ☐ |
| CA-02 | Medir el cuerpo antes y después de la línea, y correr `metareglas` | CP-002 | | ☐ |
| CA-03 | Correr el programa, leer el mapa, cambiar una tarea y volver a correrlo; y las pruebas | CP-003 | | ☐ |
| RNF | Leer `CHANGELOG.md` y `VERSION`, y correr las pruebas | CP-004 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| CP-001 a CP-004 | Resultado de cada caso | [resultado_pruebas.md](resultado_pruebas.md) |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | El propio repositorio, y carpetas temporales de las pruebas para los casos que cambian una regla |
| Usuarios de prueba | No aplica: no hay usuarios |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit de la fase. El mapa se borra con él, porque es un archivo generado.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

No aplica: la línea nueva no cambia qué exige ninguna regla, y ningún proyecto tiene que tocar un archivo. Por eso es MENOR.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

- Base: `20·M5` (la línea queda fuera del cuerpo), `20·M10` (versionar), `02·F4` (plan y pruebas aprobados antes de construir), `02·F23` (el pendiente se construye como fase de su HU), `01·C29` (el mapa vive en el repositorio y lleva a cada regla por enlace), `00·ID8`, `00·ID9`, `00·ID11` e `00·ID12` en todo lo que se escribe.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que la lista propuesta no sirva al anotar el núcleo | Hay que rehacer la lista | Se ajusta en la misma fase, con 10 reglas anotadas, y se le muestra al usuario antes de cerrar | Abierto |
| B-02 | Que agregar la línea a una regla del núcleo cambie la fecha del archivo y `metareglas` avise que el sello venció | Aviso falso sobre los checklists del núcleo | Se comprueba en el CP-002; si pasa, se anota como defecto y se decide con el usuario | Abierto |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] RNF-01 y RNF-02 validados
- [ ] `metareglas`, `estandar` y las pruebas nuevas sin fallas
- [ ] Señales registradas, si la fase deja alguna decisión no obvia
- [ ] Commit autorizado por el usuario

## 13. Cierre

El cierre va en [funcionalidad_implementada.md](funcionalidad_implementada.md).
