# Plan de Trabajo — Fase F-EP-001-HU-009-nadie-se-pasa-del-molde (módulo Cuerpo de reglas)

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden y sobre qué archivos. El requisito vive en [HU-009](../HU-009-reglas-sin-checklist-al-dia.md); las pruebas, en el [plan_pruebas.md](plan_pruebas.md).

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `F-EP-001-HU-009-nadie-se-pasa-del-molde` |
| **Épica** | [EP-001 Cuerpo de reglas heredable](../../epica.md) |
| **HU** | [HU-009 Poner al día las reglas que no pasan su propio checklist](../HU-009-reglas-sin-checklist-al-dia.md), una sola ([`02·F12`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md), punto 1) |
| **Módulo** | Cuerpo de reglas, `base/` completo |
| **Fecha apertura** | 2026-08-22 |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📝 **Modifica fases anteriores.** Sexta fase de la historia: retoma lo que las fases `B`, `C`, `D` y `E` dejaron abierto, que era todo lo que dependía de una decisión del usuario.

**De dónde sale:** el [pendiente 19](../../../../../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md), que el usuario mandó resolver dentro de la orden «resuelva todos los pendientes menos el 10 y el 48».

**CA que cubre:** el `CA-01` (ninguna regla publicada reprueba su checklist) y el transversal de no regresión.

### 0.1 Cómo llega este plan, y por qué se escribe después

**Este plan se escribe retrodocumentando.** El trabajo se ejecutó capítulo por capítulo el 2026-08-22, autorizado en el chat uno por uno, y se publicó en seis versiones antes de que existiera esta carpeta. Eso incumplió [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), que pide bajar el pendiente a fase **antes** de construir.

**Se escribe igual, y no se disimula.** La otra salida, dar el trabajo por bueno sin fase, deja seis versiones publicadas que ninguna historia reclama: la cadena queda rota hacia arriba y la pregunta «¿de dónde salió este cambio?» se queda sin respuesta. Lo que aquí se declara como línea base es **lo que ya está publicado**, y las pruebas se corrieron de verdad, no se dieron por corridas.

## 1. Objetivo y alcance

**Objetivo:** que ninguna regla del cuerpo esté publicada reprobando su propio checklist, ni por lo que exige ni por su largo.

**Las dos deudas que quedaban, y por qué van juntas:**

| Deuda | Tamaño al abrir | Qué exige |
|---|---|---|
| Reglas con el sello en NO CUMPLE | 27 | corregir la regla y volver a aplicarle las veinte filas |
| Reglas con el sello en CUMPLE y el cuerpo pasado de 320 | 34 | recortar sin tocar la exigencia, y volver a sellar |

Van juntas porque el remedio de la segunda es el mismo que el de varias de la primera: decir lo mismo en menos palabras y mandar el porqué a `notas/`.

**Fuera de alcance:**

- **Partir las 26 reglas con más de una exigencia.** Se comprobó al abrir cada capítulo que 23 ya estaban partidas desde el 2026-08-18 y dos se habían resuelto sin partirse; solo quedaba `17·I3`, que entra acá porque era una decisión, no una partición.
- **Las 21 fases de retrodocumentación de los capítulos** (HU-015 a HU-035), que son de otra historia.
- **El pendiente 33 y el 59**, que dependen de datos del usuario.

## 2. Análisis previo, línea base verificada

**Medido el 2026-08-22 antes de tocar nada:**

```
$ python validadores/validar.py metareglas
27 falla(s), 38 aviso(s).
```

**Las 27 en NO CUMPLE, por capítulo:** `18` entero (`DP1` a `DP8`), `19` entero (`OB1` a `OB6`), `20` (`M2`, `M4`, `M7`, `M8`), `02` (`F5`, `F12`), `01` (`C1`, `C15`, `C16`, `C18`), `04` (`S4`), `08` (`T4`) y `10` (`DEP3`).

**Los 34 avisos de largo:** `00` (4), `01` (3), `02` (12), `03` (2), `13` (13) y `20` (2), midiendo entre 323 y 725 caracteres contra un molde de 320.

**Tres hechos de la línea base que cambiaron el plan:**

1. **`04·S7` ya estaba derogada** desde la 23.17.0, así que `10·DEP3` no repetía a una regla viva: le faltaba declararlo.
2. **Las tres blindadas del núcleo ya estaban partidas** (`N7`, `N8`, `N9`, del 2026-08-18), y `20·M7` prohíbe que una regla declare que **extiende** a una blindada: la forma correcta es «depende de».
3. **`12·PR3` había sido reescrita el 2026-08-18** y ya no era el índice sin exigencia propia que el pendiente describía.

## 3. Qué se hace, en orden

Una unidad por capítulo, cada una con su verificación y su publicación:

| # | Unidad | Qué toca | Versión |
|---|---|---|---|
| 1 | Las 27 en NO CUMPLE | ejemplos para `18` y `19`; cuerpos de `C1`, `C15`, `C16`, `C18`, `S4`, `T4`; `DEP3` declara la derogación; `F12` gana anexo; `M2` aclara el preámbulo | 30.8.0 |
| 2 | Capítulo `00` | `ID5`, `ID7`, `ID8`, `ID9` al molde; el glosario decía seis reglas del núcleo | 30.8.1 |
| 3 | Capítulo `01` | `C5`, `C21`, `C22` al molde | 30.8.2 |
| 4 | Capítulo `02` | las doce largas al molde | 30.8.3 |
| 5 | Capítulos `03`, `13`, `20` | quince al molde; anexos para `DOC11` y `M6` | 30.9.0 |
| 6 | Las dos decisiones del usuario | `17·I3` queda como una regla con su lista; `12·PR3` no se deroga | 30.9.1 |

### 3.1 Archivos que se crean o modifican

| Archivo | Qué se hace |
|---|---|
| `base/`, 34 archivos de regla y capítulo | cuerpos recortados, ejemplos agregados, sellos vueltos a aplicar con fecha 2026-08-22 |
| [`base/02-flujo-de-trabajo/nomenclatura-de-fases.md`](../../../../../base/02-flujo-de-trabajo/nomenclatura-de-fases.md) | nace: el texto literal del usuario que era el cuerpo de `F12` |
| [`base/13-documentacion/tabla-de-trazabilidad.md`](../../../../../base/13-documentacion/tabla-de-trazabilidad.md) | nace: la tabla de cinco columnas que era el cuerpo de `DOC11` |
| [`base/20-meta-reglas/desempate.md`](../../../../../base/20-meta-reglas/desempate.md) | nace: los seis pasos que eran el cuerpo de `M6` |
| [`notas/porques-recortados-al-molde.md`](../../../../../notas/porques-recortados-al-molde.md) | nace: lo que salió de cada regla recortada |
| `CHANGELOG.md`, `VERSION` | seis entradas y seis subidas de versión ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)) |
| `pendientes/19-...md`, `documentacion/senales.md` | el estado de la ronda y la señal S-020 |

### 3.2 Las trece preguntas, en corto

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Qué se construye | reglas que cumplen su propio checklist |
| 2 | De dónde sale | pendiente 19, orden del usuario del 2026-08-22 |
| 3 | Quién lo usa | todo proyecto que hereda `base/` |
| 4 | Objetivo y alcance | §1 |
| 5 | Qué NO entra | §1, fuera de alcance |
| 6 | Datos | no hay: son documentos |
| 7 | Reglas de negocio | el checklist de veinte filas y `20·M5` |
| 8 | Interfaz | no aplica porque el entregable es texto del estándar |
| 9 | Archivos | §3.1 |
| 10 | Dónde queda accesible | en `base/`, que ya se carga al abrir sesión |
| 11 | Permisos | no aplica porque no hay ejecución ni datos |
| 12 | Migración | no aplica porque ninguna exigencia cambia; los proyectos al día no hacen nada |
| 13 | Cómo se comprueba | [plan_pruebas.md](plan_pruebas.md) |

## 4. Riesgos

| # | Riesgo | Cómo se ataca |
|---|---|---|
| F-01 | Que recortar se lleve la exigencia y no el porqué | cada recorte deja escrito en `notas/` qué salió, y el sello dice contra qué cuerpo se aplicó |
| F-02 | Que el sello quede diciendo lo contrario de lo que la regla dice hoy | se vuelve a aplicar el checklist con fecha y versión del día, y `validar.py metareglas` reprueba el sello vencido |
| F-03 | Que mover texto a un anexo rompa las citas | `validar.py estandar` comprueba cada enlace y cada cita; las trece citas a `F12.N` se reescribieron |
| F-04 | Que un sí viejo del usuario se ejecute sobre un diagnóstico caducado | las dos que cambiaron de sentido se le devolvieron antes de tocarlas (señal S-020) |

## 5. Cómo se aprobó

El usuario autorizó **capítulo por capítulo**, con el commit y el push pedidos aparte cada vez ([`00·N1`](../../../../../base/00-nucleo-blindado.md#n1--ningún-cambio-de-estado-sin-aprobación-explícita-blindada), [`00·N2`](../../../../../base/00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada)), y decidió las dos que eran suyas: `17·I3` como una regla con su lista, y `12·PR3` en pie.
