# Plan de Trabajo · Fase `B-EP-001-HU-011-nada-del-proyecto-queda-fuera-del-proyecto` (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba acepta el alcance y el costo. El requisito vive en la HU, el detalle de las pruebas en el `plan_pruebas` de la misma fase, y lo que quedó hecho en el `funcionalidad_implementada.md` del cierre.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-001-HU-011-nada-del-proyecto-queda-fuera-del-proyecto` |
| **Épica** | [EP-001](../../epica.md) |
| **HU** | [HU-011](../HU-011-buscar-antes-de-preguntar.md), una sola (`F12.1`) |
| **Módulo** | Cuerpo de reglas, capítulo 01, conducta |
| **Especificación del módulo** | La regla de negocio RN-06 de la HU-011 |
| **Fecha apertura** | 2026-09-28 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- Funcionalidad nueva: la regla `01·C29`. Sale del [pendiente 99](../../../../../pendientes/99-nada-del-proyecto-queda-fuera-del-proyecto.md), aprobado por el usuario el 2026-09-28: ninguna regla impedía que contenido del proyecto quedara guardado fuera del repositorio. Va en HU-011 porque es la historia dueña del capítulo 01.

**CA de la HU que cubre esta fase** (trazabilidad `13·DOC11`):

| CA de HU-011 que cierra esta fase | Estado |
|---|---|
| [CA-04](../HU-011-buscar-antes-de-preguntar.md#ca-04--nada-del-agente-ni-del-proyecto-queda-fuera-de-ellos) | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que exista la regla `01·C29`, que diga que todo lo del agente y del proyecto vive en el repositorio y se alcanza por un enlace, y que `01·C19` la extienda en vez de repetirla.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-04 | Algo del proyecto se guarda o se necesita: vive en el repositorio y se llega por enlace | Funcional, camino feliz | Media |

**Fuera de alcance:**

- Cambiar `04·S9`: su capítulo tiene su propia historia dueña, HU-017.
- Construir un programa que avise cuando algo del proyecto quede afuera.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medida el 2026-09-28, antes de escribir este plan:

```
validar.py metareglas: sin incumplimientos
VERSION: 39.0.0
base/01-conducta.md: C1 a C28, C29 libre
```

Lo que ya existe y la regla nueva toca:

- `01·C19` pide que la memoria del agente viva en el repositorio. Su cuerpo tiene 317 caracteres, para un molde de 320.
- `04·S9` pide que el agente escriba solo dentro del proyecto, y dice «Leer fuera sí».
- El recuerdo `historico-chat/memory/nada-del-proyecto-queda-en-la-herramienta.md` dice lo mismo que la regla nueva, como preferencia de este repositorio.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `base/01-conducta.md` | Modificar | Estándar | La regla `C29` con su checklist, y `C19` extendiéndola, con su checklist vuelto a aplicar |
| `validadores/reglas-validables.md` | Modificar | Estándar | `C29` registrada, como pide la fila 18 del checklist |
| `historico-chat/memory/nada-del-proyecto-queda-en-la-herramienta.md` | Modificar | Memoria | Una línea que dice que subió a regla `01·C29` |
| `CHANGELOG.md` y `VERSION` | Modificar | Estándar | `39.1.0`, MENOR |
| `pendientes/99-nada-del-proyecto-queda-fuera-del-proyecto.md` y `pendientes/README.md` | Modificar | Documentación | Cerrar el pendiente |
| Los documentos de esta fase y la sección 8 de HU-011 | Modificar | Documentación | Estado y enlaces |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

No aplica: la fase no cambia el contrato de ningún programa.

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica: la fase no crea ningún servicio.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica: la regla no tiene pantalla.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Regla nueva en conducta `01` | Ampliar `04·S9` | Decisión del usuario al aprobar el pendiente 99: el principio vale para todo, y en una regla de rutas quedaría escondido |
| `C19` extiende `C29` | Dejar `C19` sin relación | `C19` es el caso de la memoria dentro del principio general; declararlo evita que las dos se lean como reglas sueltas |
| `C29` enlaza `S9` desde su texto, y `S9` no cambia | Cambiar `S9` en esta fase | El capítulo 04 tiene historia dueña, HU-017, y todo cambio suyo baja por ella |
| MENOR | MAYOR | Una regla de conducta nueva que no obliga a un proyecto a tocar ningún archivo |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

## 3. Desglose de tareas por criterio de aceptación

### CA-04 · Nada del agente ni del proyecto queda fuera de ellos

> Agrupa las tareas que escriben la regla y dejan a `C19` como su caso particular.

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Escribir `C29` en `base/01-conducta.md`: encabezado en imperativo, una sola exigencia, el enlace a `S9` con el límite de su «leer fuera sí», ejemplo INCORRECTO y CORRECTO, y la línea de quién la hace cumplir | Estándar | 0,5 h | — | CP-001 |
| T-02 | Aplicar el checklist a `C29`, registrarla en `validadores/reglas-validables.md` y dejarlo en CUMPLE | Estándar | 0,5 h | T-01 | CP-001 |
| T-03 | Agregar a `C19` «extiende `01·C29`», acortando su cuerpo para que siga cabiendo en 320 caracteres, y volver a aplicarle el checklist | Estándar | 0,5 h | T-01 | CP-002 |

### RNF · Requisitos no funcionales

> Agrupa las tareas que dejan el cambio registrado y cerrado.

| ID | Tarea | Categoría | Est. | Ev. |
|---|---|---|:--:|---|
| T-04 | Anotar en el recuerdo que subió a regla `01·C29`; el recuerdo se queda | Trazabilidad | 0,1 h | CP-003 |
| T-05 | Registrar la regla en `CHANGELOG.md` y subir `VERSION` a `39.1.0` | Trazabilidad | 0,2 h | CP-003 |
| T-06 | Cerrar el pendiente 99 y actualizar la sección 8 de HU-011 | Trazabilidad | 0,2 h | — |

**Total estimado:** 2 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03, T-05, T-06.
**Paralelizables:** T-04, después de la T-01.

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-04 | Leer `C29` y `C19`, y correr `metareglas` y `estandar` | CP-001 y CP-002 | | ☐ |
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

No aplica: la regla le llega a cada proyecto con el estándar, y ningún proyecto tiene que tocar un archivo.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

- Base: `20·M4` (siguiente identificador libre), `20·M5` (una sola exigencia, título imperativo, ejemplo, cuerpo de hasta 320 caracteres), `20·M7` (`extiende`), `20·M9` (validable o no), `20·M10` (versionar), `02·F23` (el pendiente se construye como fase de su HU), `00·N10` (la historia dueña manda sobre lo pedido), `00·ID8`, `00·ID9`, `00·ID11` e `00·ID12` en todo lo que se escribe.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que `C19` no quepa en 320 caracteres con la dependencia | Su checklist reprueba la fila 10 | Se acorta sin cambiar qué exige; lo que se quite, si es porqué, ya está en el índice de la memoria | Abierto |
| B-02 | Que `C29` choque con el «leer fuera sí» de `S9` | Su checklist reprueba la fila 17 | `C29` dice en su texto que leer afuera vale para lo que no es del proyecto | Abierto |

## 11. Definition of Done

- [ ] El CA de la sección 0 verificado con evidencia en la sección 5
- [ ] `metareglas`, `estandar` y `pendientes` sin fallas
- [ ] Señales registradas, si la fase deja alguna decisión no obvia
- [ ] Commit autorizado por el usuario

## 13. Cierre

El cierre va en [funcionalidad_implementada.md](funcionalidad_implementada.md).
