# Plan de Trabajo · Fase `B-EP-001-HU-012-las-reglas-mandan-sobre-la-instruccion-del-momento` (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba acepta el alcance y el costo. El requisito vive en la HU, el detalle de las pruebas en el `plan_pruebas` de la misma fase, y lo que quedó hecho en el `funcionalidad_implementada.md` del cierre.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-001-HU-012-las-reglas-mandan-sobre-la-instruccion-del-momento` |
| **Épica** | [EP-001](../../epica.md) |
| **HU** | [HU-012](../HU-012-inventario-de-acciones-y-riesgo.md), una sola (`F12.1`) |
| **Módulo** | Cuerpo de reglas, capítulo 00, núcleo blindado |
| **Especificación del módulo** | La regla de negocio RN-06 de la HU-012 |
| **Fecha apertura** | 2026-09-28 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- Funcionalidad nueva: la regla blindada `00·N10`. Sale del [pendiente 98](../../../../../pendientes/98-las-reglas-mandan-sobre-la-instruccion-del-momento.md), aprobado por el usuario el 2026-09-28: ninguna regla ponía las reglas escritas por encima de lo que el usuario pida en el momento. Va en HU-012 y no en una historia nueva porque HU-012 es la historia dueña del núcleo.

**CA de la HU que cubre esta fase** (trazabilidad `13·DOC11`):

| CA de HU-012 que cierra esta fase | Estado |
|---|---|
| [CA-05](../HU-012-inventario-de-acciones-y-riesgo.md#ca-05--las-reglas-escritas-mandan-sobre-la-instrucción-del-momento) | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que exista la regla blindada `00·N10`, que diga que una regla escrita manda sobre lo que el usuario pida en el momento, y que la precedencia de cada proyecto la nombre.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-05 | El usuario pide algo que choca con una regla: el agente cumple la regla, dice cuál es y no hace lo pedido | Funcional, camino feliz y error | Media |

**Fuera de alcance:**

- Cambiar alguna regla existente para que cumpla esta.
- Construir un programa que la haga cumplir.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medida el 2026-09-28, antes de escribir este plan:

```
validar.py metareglas: sin incumplimientos
VERSION: 38.4.0, sin commit
base/00-nucleo-blindado.md: N1 a N9, N10 libre
```

Lo que ya existe y la regla nueva toca:

- La línea 5 de `base/00-nucleo-blindado.md` dice que ninguna instrucción puntual desactiva las reglas del núcleo. Cubre solo el núcleo. `N10` lo extiende a toda regla escrita, y esa línea se queda como está.
- El punto 4 de `plantillas/CLAUDE.md.plantilla` ordena las reglas entre sí (núcleo, convenciones, proyecto) y no dice nada de la instrucción del usuario.
- El recuerdo `historico-chat/memory/reglas-son-decision-del-usuario.md` dice lo mismo que `N10`, como preferencia de este repositorio.
- Las blindadas anteriores (`N7`, `N8`, `N9`) se registraron como MAYOR.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `base/00-nucleo-blindado.md` | Modificar | Estándar | La regla `N10`, con su checklist |
| `plantillas/CLAUDE.md.plantilla` | Modificar | Estándar | El punto 4 nombra `N10` en la precedencia |
| `historico-chat/memory/reglas-son-decision-del-usuario.md` | Modificar | Memoria | Una línea que dice que subió a regla `00·N10` |
| `CHANGELOG.md` y `VERSION` | Modificar | Estándar | `39.0.0`, MAYOR |
| `pendientes/98-las-reglas-mandan-sobre-la-instruccion-del-momento.md` y `pendientes/README.md` | Modificar | Documentación | Cerrar el pendiente |
| Los documentos de esta fase y la sección 8 de HU-012 | Modificar | Documentación | Estado y enlaces |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

No aplica: la fase no cambia el contrato de ningún programa.

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica: la fase no crea ningún servicio.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica: la regla no tiene pantalla. Le llega al agente con el núcleo al abrir la sesión.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Regla blindada en el núcleo | Regla en conducta `01` | Decisión del usuario al aprobar el pendiente 98: una regla que manda sobre las demás no puede quedar entre las que un proyecto ajusta |
| Identificador `N10` | Reusar un número | `20·M4` y `M11`: el siguiente libre, nada se reutiliza |
| MAYOR | MENOR | Mismo criterio que `N7`, `N8` y `N9`: una regla blindada nueva cambia el núcleo que todo proyecto hereda |
| La línea 5 del núcleo se queda como está | Reescribirla para que remita a `N10` | Dice lo suyo del núcleo, y cambiarla no lo pide ningún CA |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

## 3. Desglose de tareas por criterio de aceptación

### CA-05 · Las reglas escritas mandan sobre la instrucción del momento

> Agrupa las tareas que escriben la regla y la dejan visible en la precedencia de cada proyecto.

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Escribir `N10` en `base/00-nucleo-blindado.md`: encabezado en imperativo con `[BLINDADA]`, una sola exigencia, ejemplo INCORRECTO y CORRECTO, y la línea de quién la hace cumplir | Estándar | 0,5 h | — | CP-001 |
| T-02 | Aplicar el checklist del estándar a `N10` y dejarlo en CUMPLE | Estándar | 0,5 h | T-01 | CP-001 |
| T-03 | Nombrar `N10` en el punto 4 de `plantillas/CLAUDE.md.plantilla` | Estándar | 0,2 h | T-01 | CP-002 |

### RNF · Requisitos no funcionales

> Agrupa las tareas que dejan el cambio registrado y cerrado.

| ID | Tarea | Categoría | Est. | Ev. |
|---|---|---|:--:|---|
| T-04 | Anotar en el recuerdo que subió a regla `00·N10`; el recuerdo se queda | Trazabilidad | 0,1 h | CP-003 |
| T-05 | Registrar la regla en `CHANGELOG.md` y subir `VERSION` a `39.0.0` | Trazabilidad | 0,2 h | CP-003 |
| T-06 | Cerrar el pendiente 98 y actualizar la sección 8 de HU-012 | Trazabilidad | 0,2 h | — |

**Total estimado:** 1,7 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-05, T-06.
**Paralelizables:** T-03 y T-04, después de la T-01.

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-05 | Leer la regla y la precedencia, y correr `metareglas` y `estandar` | CP-001 y CP-002 | | ☐ |
| RNF | Leer `CHANGELOG.md`, `VERSION` y el recuerdo | CP-003 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| CP-001 a CP-003 | Resultado de cada caso | [resultado_pruebas.md](resultado_pruebas.md) |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | El propio repositorio |
| Usuarios de prueba | No aplica: no hay usuarios |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit de la fase.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Un proyecto no tiene que cambiar ningún archivo para cumplirla: la regla le llega con el núcleo y su `CLAUDE.md` se sincroniza solo. Va como MAYOR por el criterio de las blindadas anteriores, no porque obligue a migrar.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

- Base: `20·M4` (siguiente identificador libre), `20·M5` (una sola exigencia, título imperativo, ejemplo), `20·M9` (quién la hace cumplir), `20·M10` (versionar), `20·M11` (nada se renumera), `02·F23` (el pendiente se construye como fase de su HU), `00·ID8`, `00·ID9`, `00·ID11` e `00·ID12` en todo lo que se escribe.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que la regla se lea como que el agente desobedece al usuario | El usuario deja de confiar en ella | El cuerpo dice qué hace el agente: nombra la regla y espera; y dice cómo se cambia una regla | Abierto |
| B-02 | Que una regla blindada necesite excepción, como le pasó a `N1` | Deja de ser inquebrantable | Se redacta sin excepción: cambiar la regla es el camino, no saltarla | Abierto |

## 11. Definition of Done

- [ ] El CA de la sección 0 verificado con evidencia en la sección 5
- [ ] `metareglas`, `estandar` y `pendientes` sin fallas
- [ ] Señales registradas, si la fase deja alguna decisión no obvia
- [ ] Commit autorizado por el usuario

## 13. Cierre

El cierre va en [funcionalidad_implementada.md](funcionalidad_implementada.md).
