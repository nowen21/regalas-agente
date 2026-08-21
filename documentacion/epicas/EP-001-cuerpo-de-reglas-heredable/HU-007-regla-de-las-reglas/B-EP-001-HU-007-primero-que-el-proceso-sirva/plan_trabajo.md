# Plan de Trabajo — Fase B-EP-001-HU-007-primero-que-el-proceso-sirva (módulo Cuerpo de reglas)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en [HU-007](../HU-007-regla-de-las-reglas.md); el detalle de las pruebas, en el `plan_pruebas.md` de esta misma fase; lo que dieron al correrlas, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** (identificador · [`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `B-EP-001-HU-007-primero-que-el-proceso-sirva` |
| **Épica** | [EP-001 Cuerpo de reglas heredable y en capas](../../epica.md) |
| **HU** | [HU-007 La regla que gobierna cómo se escriben las reglas](../HU-007-regla-de-las-reglas.md) — una sola (`F12.1`) |
| **Módulo** | Cuerpo de reglas |
| **Especificación del módulo** | [HU-007](../HU-007-regla-de-las-reglas.md). El entregable es texto normativo: su criterio de aceptación es la especificación |
| **Fecha apertura** | 2026-08-20 |
| **Rama** | `main` — el repositorio trabaja los cambios de reglas sobre la rama principal y el commit lo autoriza el usuario |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): ✨ **Funcionalidad nueva**, bajada del [pendiente 16](../../../../../pendientes/hecho/primero-que-el-proceso-sirva.md) por [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md): al backlog de automatizaciones le faltaba el criterio de **si conviene** automatizar, no solo si se puede. Introduce el `CA-05` en HU-007 y la meta-regla `20·M19`.

**Cómo llega este plan.** La sesión 4 del 2026-08-20 recibió la orden de resolver el pendiente, escribió el `CA-05` y la regla `M19` con su checklist, y **quedó cortada sin dejar los documentos de la fase**: las plantillas quedaron vacías y nada se versionó ni se cerró. Este plan, escrito el 2026-08-21, declara lo ya hecho como línea base (§2) y somete a aprobación lo que falta (§3). Que la regla naciera antes que su plan aprobado es un incumplimiento de [`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md) causado por el corte de esa sesión; queda declarado acá y en el riesgo B-01, no escondido.

**CA de la HU que cubre esta fase**

| CA de HU-007 | Qué exige | Estado hoy, verificado el 2026-08-21 |
|---|---|---|
| [CA-05](../HU-007-regla-de-las-reglas.md#ca-05--una-regla-validable-no-se-automatiza-hasta-que-se-sepa-que-sirve) | Antes de construir el validador de una regla se responden por escrito tres preguntas: si se cumple hoy a mano, cuántas veces se incumplió y por qué, y cuántas falsas alarmas daría | El criterio está **escrito** ([`20·M19`](../../../../../base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md), checklist en CUMPLE) y **sin probar**: ninguno de sus tres casos de validación se ha ejecutado ni registrado |

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** dejar el criterio «primero que el proceso sirva, después se automatiza» probado contra los tres casos reales que el propio `CA-05` nombra, versionado en el registro de cambios, y el pendiente 16 cerrado en `hecho/`.

**Fuera de alcance:**

- **Ejecutar los 16 ítems del backlog de automatizaciones** ([pendiente 09](../../../../../pendientes/hecho/autonomia-sin-ia.md)). Esta fase escribe y prueba la puerta; pasar cada ítem por ella ocurre cuando cada uno se promueva.
- **El conteo de incumplimientos por regla.** Ya existe (`validar.py vigencia`, `CA-04` de esta misma HU, cerrado); acá solo se usa.
- **Tocar `M9` o cualquier otra regla del capítulo `20`.** `M19` extiende a `M9`; no la reescribe.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado contra el repositorio el 2026-08-21, archivo por archivo.

**Lo que la sesión cortada ya dejó hecho (sin commit):**

| Pieza | Dónde está | Estado |
|---|---|---|
| El criterio como CA de la HU | [CA-05](../HU-007-regla-de-las-reglas.md#ca-05--una-regla-validable-no-se-automatiza-hasta-que-se-sepa-que-sirve), con su bitácora del 2026-08-20 | Escrito |
| La meta-regla | [`20·M19`](../../../../../base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md), con checklist **CUMPLE** (20 filas, contra v27.2.0) | Escrita y sellada |
| Su fila en el índice del capítulo | [`base/20-meta-reglas/base.md`](../../../../../base/20-meta-reglas/base.md), fila de `M19` y sección «M19 — las tres preguntas» | Escrita |
| Su lugar en el procedimiento | Paso 7 del procedimiento del capítulo `20` («el validador no se construye hasta que la regla demuestre que sirve a mano») | Escrito |
| Su clasificación como no-validable-por-programa | [`validadores/reglas-validables.md`](../../../../../validadores/reglas-validables.md), lista del capítulo `20`, con el motivo | Escrita |
| La fila de la fase en la HU | §7 de [HU-007](../HU-007-regla-de-las-reglas.md), «Abierta 2026-08-20 desde el pendiente 16» | Escrita |

**Lo que falta, y es el trabajo de este plan:**

1. **La decisión que el pendiente reservó al usuario.** El pendiente 16 dice que hay dos caminos —un criterio nuevo en HU-007, o una historia propia— y que «las dos son del usuario». La sesión cortada tomó la opción 1 sin que quedara registrada la aprobación. **Este plan no vale sin esa confirmación** (duda 1, §2.7).
2. **La prueba.** El `CA-05` trae tres casos de validación y ninguno se ha corrido ni registrado.
3. **El versionado.** `M10` exige entrada en el CHANGELOG y subida de `VERSION` para todo cambio de `base/`. `VERSION` dice `28.0.0` y el registro no menciona a `M19`.
4. **El cierre.** El pendiente 16 sigue en «abierto»; los documentos de la fase están en plantilla; el `README.md` de la fase no existe (el enlace del §7 de la HU apunta a un archivo que no está).

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `.../B-EP-001-HU-007-.../plan_pruebas.md` | Llenar | Documentación | Los tres casos del `CA-05` |
| `.../B-EP-001-HU-007-.../resultado_pruebas.md` | Llenar | Documentación | Nace en «no ejecutado»; se llena al correr |
| `.../B-EP-001-HU-007-.../estado-fase.md` | Llenar | Documentación | El checkpoint de las puertas |
| `.../B-EP-001-HU-007-.../funcionalidad_implementada.md` | Llenar | Documentación | El cierre, al final |
| `.../B-EP-001-HU-007-.../README.md` | Nuevo | Documentación | Repara el enlace roto del §7 de la HU ([`13·DOC17`](../../../../../base/13-documentacion/reglas/DOC17-manten-un-readme-en-cada-nivel-del-arbol-de-trabajo.md)) |
| [`CHANGELOG.md`](../../../../../CHANGELOG.md) | Modificar | Versionado | Entrada `28.1.0` — MENOR (§2.6) |
| [`VERSION`](../../../../../VERSION) | Modificar | Versionado | `28.0.0` → `28.1.0`, leída un instante antes de escribir (`20·M18`) |
| [`pendientes/16-primero-que-el-proceso-sirva-despues-se-automatiza.md`](../../../../../pendientes/hecho/primero-que-el-proceso-sirva.md) | Mover | Backlog | A `pendientes/hecho/`, con `cerrar.py`, que arrastra las citas y deja la fila del índice |
| [`pendientes/README.md`](../../../../../pendientes/README.md) | Modificar | Backlog | La fila del 16 pasa a forma de hecho (la deja `cerrar.py`) |
| [`HU-007-regla-de-las-reglas.md`](../HU-007-regla-de-las-reglas.md) | Modificar | Documentación | §7: estado de la fase B al cerrar; bitácora |
| [`pendientes/48-inventario-hu.md`](../../../../../pendientes/48-inventario-hu.md) | Modificar | Backlog | La fila de HU-007, si el cierre de esta fase cambia alguna casilla |

> **`base/20-meta-reglas/` no se toca.** La regla ya está escrita y sellada; editarla anularía su checklist. Si una prueba la reprobara, se pausa y se propone (`02·F20`), no se corrige sobre la marcha.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: no cambia el contrato de ningún programa ni el texto de ninguna regla existente. `M19` **extiende** a `M9` y `M9` queda como está.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque el entregable son archivos de texto del repositorio.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

No aplica. `M19` llega como las demás meta-reglas: en el índice del capítulo `20` al abrir sesión, y en el paso 7 del procedimiento cuando alguien va a construir un validador.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La subida es **MENOR** (`28.1.0`) | MAYOR | Un proyecto al día no tiene que hacer nada hoy: `M19` gobierna un acto futuro (construir un validador). Es el mismo corte de `M17` (23.9.0) y `M18` (registrada MENOR): meta-reglas nuevas sobre cómo trabajar |
| Los casos de prueba son hechos ya medidos del propio repositorio (ítems 01 y 06 del backlog, y la partición de `F4`) | Inventar una regla de mentira y automatizarla mal a propósito | El caso inventado no tiene el defecto real, y después hay que borrarlo. Es la misma decisión de la fase A de esta HU |
| Lo hecho por la sesión cortada se declara como línea base y no se rehace | Borrar `M19` y el `CA-05` y volver a empezar con el plan primero | El texto ya pasó su checklist y responde literal a lo que el pendiente pedía; rehacerlo repite el trabajo sin cambiar el resultado. El incumplimiento de `F4` queda declarado (§0, B-01), que es lo que no se puede perder |

### 2.7 Dudas por resolver antes de ejecutar

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | El pendiente 16 dejó dos caminos y dijo que la decisión es del usuario: **(1)** criterio nuevo en HU-007 —lo que la sesión cortada construyó— o **(2)** historia propia. ¿Confirma la opción 1? | Usuario | Pendiente |

La duda 1 bloquea todo el §3: si la respuesta es la opción 2, esta fase se replantea.

---

## 3. Desglose de tareas por criterio de aceptación

> T-01 a T-04 son la línea base: las dejó hechas la sesión del 2026-08-20 y acá se listan para que el cierre pueda compararlas (`F14` no admite tareas fantasma). El avance en vivo va en el `estado-fase.md`, no acá.

### CA-05 — Una regla validable no se automatiza hasta que se sepa que sirve

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Escribir el `CA-05` en HU-007, con su porqué y sus tres casos de validación | `HU-007-regla-de-las-reglas.md` | 1,5 |
| T-02 | Escribir `M19` con el molde canónico, su fila y su sección en el índice del capítulo, y su lugar en el paso 7 del procedimiento | `base/20-meta-reglas/` | 2,0 |
| T-03 | Registrar `M19` entre las reglas que no valida un programa, con el motivo | `validadores/reglas-validables.md` | 0,5 |
| T-04 | Correr el checklist de veinte filas sobre `M19` y sellar el resultado | `M19-...md` | 1,0 |
| T-05 | Ejecutar los tres casos de prueba del `CA-05` y registrar qué dio cada uno | `resultado_pruebas.md` | 2,0 |
| T-06 | Versionar: entrada `28.1.0` en el CHANGELOG, en castellano llano (`20·M17`), y subir `VERSION` | `CHANGELOG.md` · `VERSION` | 1,0 |
| T-07 | Cerrar: `funcionalidad_implementada.md`, §7 y bitácora de la HU, pendiente 16 a `hecho/` con `cerrar.py`, README de la fase | fase + backlog | 1,5 |

**Total: 7 tareas · 9,5 horas** (4 ya en la línea base · 3 por ejecutar).

---

## 4. Secuencia de ejecución

T-01 a T-04 están hechas. T-05 va primero (sin veredicto no hay nada que versionar ni cerrar), T-06 después (la entrada del registro cita el veredicto) y T-07 cierra. Nada se paraleliza: son tres pasos cortos y encadenados.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). Ninguna regla se edita para que la prueba pase.

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método de verificación | Evidencia |
|---|---|---|
| [CA-05](../HU-007-regla-de-las-reglas.md#ca-05--una-regla-validable-no-se-automatiza-hasta-que-se-sepa-que-sirve) | Los tres casos que el propio CA fija: el criterio **detiene** el ítem 06 del backlog (falsas alarmas), **deja pasar** el ítem 01 (solo fallaba acordarse) y **manda corregir** la `F4` doble antes que construirle validador | CP-001, CP-002 y CP-003 del `plan_pruebas.md` |

---

## 6. Datos y ambiente de prueba

Este repositorio, leyendo documentos que ya existen: el [pendiente 09](../../../../../pendientes/hecho/autonomia-sin-ia.md) con su backlog medido, y las reglas `F4`/`F4.1`-`F4.5`/`F14`-`F18` con su historia de partición y derogación. Las pruebas son de análisis: no ejecutan programas que cambien estado, no usan datos reales y no tocan `base/`.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase, o descarte del árbol de trabajo si no se ha commiteado. Todo el entregable son archivos de texto versionados; no hay datos que restaurar. La regla, si hubiera que retirarla, no se borra: se deroga (`20·M11`).

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

Los proyectos que heredan reciben `M19` con `base/` en su próxima instalación; el aviso de desfase de versión les informa. Nada que migrar: la regla no obliga a hacer nada hoy — actúa cuando alguien vaya a construir un validador (por eso MENOR, §2.6).

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`02·F19`](../../../../../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md), [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), [`02·F25`](../../../../../base/02-flujo-de-trabajo/reglas/F25-autorizar-el-arranque-no-aprueba-el-plan.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`13·DOC17`](../../../../../base/13-documentacion/reglas/DOC17-manten-un-readme-en-cada-nivel-del-arbol-de-trabajo.md), [`20·M5`](../../../../../base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md), [`20·M7`](../../../../../base/20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md), [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md), [`20·M12`](../../../../../base/20-meta-reglas/reglas/M12-antes-de-crear-una-regla-buscar-la-duplicacion-es-el-defecto-mas-caro.md), [`20·M17`](../../../../../base/20-meta-reglas/reglas/M17-la-entrada-del-registro-abre-en-castellano-llano.md), [`20·M18`](../../../../../base/20-meta-reglas/reglas/M18-lo-compartido-se-lee-un-instante-antes-de-escribirlo.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | `M19` y el `CA-05` nacieron antes que este plan, por el corte de la sesión 4 del 2026-08-20 | El orden de `F4` quedó invertido una vez | Se declara acá y en §0; el plan somete lo hecho a la misma verificación que si no existiera. No se normaliza: si vuelve a pasar, es patrón y va a `pendientes/` | Declarado |
| B-02 | La duda 1 (§2.7): la opción entre CA nuevo e historia propia era del usuario y nadie la registró | Bloquea T-05 a T-07 | Se pregunta antes de ejecutar; con la opción 2, la fase se replantea | Abierto |
| R-01 | Que `M19` se use como excusa para no automatizar nunca | El backlog del 09 se congelaría | La última frase de la regla es el corte: si solo falla acordarse, se automatiza ya. CP-002 prueba exactamente eso | Mitigado por diseño |

---

## 11. Definition of Done

- [ ] La duda 1 respondida por el usuario y registrada.
- [ ] Los tres casos del `CA-05` corridos, con lo que dio cada uno y su veredicto en el `resultado_pruebas.md`.
- [ ] Entrada `28.1.0` en el CHANGELOG que un lector de afuera entiende, y `VERSION` al día.
- [ ] Pendiente 16 en `hecho/`, con su fila del índice en forma de hecho.
- [ ] §7 de la HU con el estado real de la fase B, y el README de la fase reparando el enlace roto.
- [ ] `validar.py estandar`, `fases`, `pendientes` y `versionado` sin fallas nuevas.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase. Este plan se queda como se aprobó, para poder comparar lo que se dijo contra lo que pasó.
