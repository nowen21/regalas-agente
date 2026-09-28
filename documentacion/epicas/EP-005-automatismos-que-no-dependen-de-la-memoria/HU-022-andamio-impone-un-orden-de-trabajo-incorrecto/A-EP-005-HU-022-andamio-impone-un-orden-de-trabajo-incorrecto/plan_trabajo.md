# Plan de Trabajo · Fase `A-EP-005-HU-022-andamio-impone-un-orden-de-trabajo-incorrecto` (módulo Automatismos)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba acepta el alcance y el costo. El requisito vive en la HU, el detalle de las pruebas en el `plan_pruebas` de la misma fase, y lo que quedó hecho en el `funcionalidad_implementada.md` del cierre.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-022-andamio-impone-un-orden-de-trabajo-incorrecto` |
| **Épica** | [EP-005](../../epica.md) |
| **HU** | [HU-022](../HU-022-andamio-impone-un-orden-de-trabajo-incorrecto.md), una sola (`F12.1`) |
| **Módulo** | Automatismos: `validadores/andamio.py` y la regla `02·F23` |
| **Especificación del módulo** | Las reglas de negocio RN-01 a RN-05 de la HU-022 |
| **Fecha apertura** | 2026-09-27 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- Modifica fase(s): corrige lo que dejó el `09·12` del backlog «Autonomía sin IA», que construyó `andamio.py` con `--hu` obligatorio para el pendiente. El gap: el andamio nació sin contemplar un pendiente que todavía no tiene historia. Sale del [pendiente 97](../../../../../pendientes/97-andamio-impone-un-orden-de-trabajo-incorrecto.md).

**CA de la HU que cubre esta fase** (trazabilidad `13·DOC11`):

| CA de HU-022 que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-022-andamio-impone-un-orden-de-trabajo-incorrecto.md#ca-01--un-pendiente-se-anota-sin-historia) | ☐ |
| [CA-02](../HU-022-andamio-impone-un-orden-de-trabajo-incorrecto.md#ca-02--con-historia-sigue-como-hoy) | ☐ |
| [CA-03](../HU-022-andamio-impone-un-orden-de-trabajo-incorrecto.md#ca-03--una-historia-que-no-existe-sigue-siendo-un-error) | ☐ |
| [CA-04](../HU-022-andamio-impone-un-orden-de-trabajo-incorrecto.md#ca-04--el-orden-queda-escrito-en-la-regla) | ☐ |
| [CA-05](../HU-022-andamio-impone-un-orden-de-trabajo-incorrecto.md#ca-05--el-índice-dice-cuándo-vale-por-asignar) | ☐ |
| [CA-06](../HU-022-andamio-impone-un-orden-de-trabajo-incorrecto.md#ca-06--un-pendiente-por-asignar-no-reprueba-la-validación) | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que `andamio.py` deje anotar un pendiente sin historia, y que `02·F23` escriba el orden hallazgo, pendiente, HU y fase.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Un pendiente se anota sin historia | Funcional, camino feliz | Media |
| CA-02 | Con `--hu`, sigue como hoy | Funcional, regresión | Baja |
| CA-03 | Un `--hu` que no existe sigue siendo error | Funcional, error | Baja |
| CA-04 | `F23` nombra el orden | Funcional, camino feliz | Media |
| CA-05 | El índice dice cuándo vale «Por asignar» | Funcional, camino feliz | Baja |
| CA-06 | «Por asignar» no reprueba la validación | Funcional, caso borde | Baja |
| RNF-01 | Versionada como MENOR | No funcional | Baja |
| RNF-02 | Quien usa `--hu` no cambia nada | No funcional | Baja |

**Fuera de alcance:**

- Cuándo se construye un pendiente: sigue necesitando su HU y su fase.
- Asignar la historia de los pendientes que hoy dicen «Por asignar».

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medida el 2026-09-27, antes de escribir este plan:

```
andamio.py:366  p.add_argument("--hu", required=True, ...)
andamio.py:286-287  crear_pendiente falla con "no existe la historia"
validadores/pendientes.py:147-159  falla si la fila "Historia de usuario" falta o está vacía; "Por asignar" pasa
tests: test_el_andamio_levanta_la_historia_y_el_pendiente.py, 8 pruebas, todas OK
VERSION 38.1.2
```

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/andamio.py` | Modificar | Validador | `--hu` opcional; `crear_pendiente` sin historia escribe «Por asignar» y no toca el mapa |
| `validadores/tests/test_el_andamio_levanta_la_historia_y_el_pendiente.py` | Modificar | Test | Pruebas del modo sin historia y del `--hu` inexistente |
| `base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md` | Modificar | Estándar | El orden y la épica de la HU; checklist vuelto a aplicar |
| `plantillas/pendiente.md` | Modificar | Estándar | La nota que da el comando del andamio dice que `--hu` es opcional |
| `pendientes/README.md` | Modificar | Documentación | La frase sobre «Por asignar» en «Ningún pendiente vive suelto» |
| `CHANGELOG.md` y `VERSION` | Modificar | Estándar | `38.2.0`, MENOR |
| `pendientes/97-andamio-impone-un-orden-de-trabajo-incorrecto.md` | Modificar | Documentación | Cerrar el pendiente |
| Los documentos de esta fase y la sección 8 de HU-022 | Modificar | Documentación | Estado y enlaces |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Archivo a refactorizar | Cambio de contrato | Archivos que dependen (rompen) | Dónde rompe |
|---|---|---|---|
| `validadores/andamio.py` | `crear_pendiente(raiz, descripcion, hu_ref, escribir)` acepta `hu_ref` vacío | Ninguno | Los llamadores que pasan `hu_ref` siguen igual; la prueba `test_la_llamada_de_siempre` lo comprueba |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica: la fase no crea ningún servicio.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica: no hay pantalla. El punto de entrada es el comando `python validadores/andamio.py pendiente <slug>`.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Sin `--hu`, el pendiente no entra al mapa de historias | Una fila del mapa con «Por asignar» | El mapa cruza historias con pendientes; una fila sin historia no cruza nada |
| Precisar `F23` | Una regla nueva del capítulo 02 | Es más barata y deja el orden junto a la regla que ya cubre la mitad. Si agrega una segunda exigencia, se pasa a regla nueva (supuesto 3.2 de la HU) |
| Un `--hu` mal escrito sigue fallando | Tratarlo como «sin historia» | Si se confundieran, un error de tipeo dejaría un pendiente suelto sin aviso |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

## 3. Desglose de tareas por criterio de aceptación

### CA-01 · Un pendiente se anota sin historia

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Hacer opcional `--hu` en el modo `pendiente` de `andamio.py` | Validador | 0,2 h | — | CP-001 |
| T-02 | En `crear_pendiente`, sin `hu_ref`: escribir «Por asignar: nace al aprobarse este pendiente» y no tocar el mapa | Validador | 0,5 h | T-01 | CP-001 |
| T-03 | Prueba del modo sin historia | Test | 0,5 h | T-02 | CP-001 |

### CA-02 · Con historia, sigue como hoy

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-04 | Correr las pruebas del andamio que ya existen | Test | 0,1 h | T-02 | CP-002 |

### CA-03 · Una historia que no existe sigue siendo un error

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-05 | Prueba de `--hu` con una HU inexistente: falla y no crea archivos | Test | 0,3 h | T-02 | CP-003 |

### CA-04 · El orden queda escrito en la regla

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-06 | Precisar el cuerpo de `02·F23` con el orden y la épica de la HU, dentro del molde de `20·M5` | Estándar | 0,5 h | — | CP-004 |
| T-07 | Volver a aplicar el checklist de `F23` | Estándar | 0,3 h | T-06 | CP-004 |

### CA-05 · El índice dice cuándo vale «Por asignar»

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-08 | Agregar la frase a «Ningún pendiente vive suelto» en `pendientes/README.md` | Documentación | 0,1 h | — | CP-005 |
| T-09 | Decir en la nota de `plantillas/pendiente.md` que `--hu` es opcional | Estándar | 0,1 h | T-01 | CP-005 |

### CA-06 · Un pendiente «Por asignar» no reprueba la validación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-10 | Correr `validar.py pendientes` con los pendientes «Por asignar» que ya existen | Validador | 0,1 h | — | CP-006 |

### RNF · Requisitos no funcionales

| ID | Tarea | Categoría | Est. | Ev. |
|---|---|---|:--:|---|
| T-11 | Registrar el cambio en `CHANGELOG.md` y subir `VERSION` a `38.2.0` | Trazabilidad | 0,2 h | CP-007 |
| T-12 | Cerrar el pendiente 97 y actualizar la sección 8 de HU-022 | Trazabilidad | 0,2 h | — |

**Total estimado:** 3,1 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03, T-05, T-04, T-11, T-12
**Paralelizables:** T-06 y T-07, T-08 y T-10, en cualquier momento; T-09 después de la T-01.

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Prueba del modo sin historia | CP-001 | | ☐ |
| CA-02 | Pruebas del andamio que ya existen | CP-002 | | ☐ |
| CA-03 | Prueba del `--hu` inexistente | CP-003 | | ☐ |
| CA-04 | Leer `F23` y correr `validar.py metareglas` | CP-004 | | ☐ |
| CA-05 | Leer la sección del índice y la nota de la plantilla | CP-005 | | ☐ |
| CA-06 | `validar.py pendientes` | CP-006 | | ☐ |
| RNF-01 | Leer `CHANGELOG.md` y `VERSION` | CP-007 | | ☐ |
| RNF-02 | Prueba `test_la_llamada_de_siempre` | CP-002 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| CP-001 a CP-007 | Resultado de cada caso | [resultado_pruebas.md](resultado_pruebas.md) |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | Las pruebas del andamio corren sobre una copia temporal del repositorio, como las que ya existen |
| Usuarios de prueba | No aplica: no hay usuarios |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit de la fase: `--hu` vuelve a ser obligatorio y `F23` vuelve a su texto anterior, con su checklist anterior.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

No aplica porque el cambio es aditivo: quien usa `--hu` sigue igual (RNF-02) y ningún pendiente escrito cambia. Por eso es MENOR.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

- Base: `02·F23` (la regla que se precisa y la que ordena construir el pendiente como fase), `20·M5` (una sola exigencia al precisar `F23`), `20·M10` (versionar), `02·F8` (solo los archivos de la sección 2.1).

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que precisar `F23` le agregue una segunda exigencia | El checklist reprueba la fila 9 | El orden pasa a una regla nueva del capítulo 02 y se amplía el plan con aprobación | Abierto |
| B-02 | Que la prueba del modo sin historia toque el repositorio real | Crea un pendiente de prueba en `pendientes/` | La prueba corre sobre una copia temporal, como las demás del andamio | Abierto |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] RNF-01 y RNF-02 validados
- [ ] Pruebas del andamio en verde, y `metareglas`, `estandar` y `pendientes` sin fallas
- [ ] Señales registradas, si la fase deja alguna decisión no obvia
- [ ] Commit autorizado por el usuario

## 13. Cierre

El cierre va en [funcionalidad_implementada.md](funcionalidad_implementada.md).
