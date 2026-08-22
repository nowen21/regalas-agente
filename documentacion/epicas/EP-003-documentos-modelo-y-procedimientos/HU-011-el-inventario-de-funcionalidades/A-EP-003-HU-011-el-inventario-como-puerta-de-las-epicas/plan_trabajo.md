# Plan de Trabajo — Fase A-EP-003-HU-011-el-inventario-como-puerta-de-las-epicas (módulo Documentos modelo)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en [HU-011](../HU-011-el-inventario-de-funcionalidades.md); el detalle de las pruebas, en el `plan_pruebas.md`; lo que dieron al correrlas, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** (identificador · [`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-003-HU-011-el-inventario-como-puerta-de-las-epicas` |
| **Épica** | [EP-003 Documentos modelo y procedimientos guiados](../../epica.md) |
| **HU** | [HU-011 El inventario de funcionalidades como puerta de las épicas](../HU-011-el-inventario-de-funcionalidades.md) — una sola (`F12.1`) |
| **Módulo** | Documentos modelo |
| **Especificación del módulo** | [HU-011](../HU-011-el-inventario-de-funcionalidades.md). Los CA son la especificación |
| **Fecha apertura** | 2026-08-21 |
| **Rama** | `main` — el commit lo autoriza el usuario |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): ✨ **Funcionalidad nueva**, bajada del [pendiente 74](../../../../../pendientes/hecho/el-inventario-es-la-puerta-de-las-epicas.md) por [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), reportado por `shopnest-mesa` con pedido explícito del usuario. El orden lo acordó el usuario en el chat del 2026-08-21: primero el 73 (cerrado en 28.2.0), ahora el 74.

**CA de la HU que cubre esta fase**

| CA de HU-011 | Qué exige | Estado hoy, verificado el 2026-08-21 |
|---|---|---|
| [CA-01](../HU-011-el-inventario-de-funcionalidades.md#ca-01--el-molde-del-inventario-existe-y-nace-para-madurar-hasta-manual) | El molde del inventario en `plantillas/`, con estados por ítem y nacido para madurar hasta manual | No existe; el caso semilla vive en `shopnest-mesa` (`propuesta-desarrollo/inventario-funcionalidades.md`, en revisión del usuario) |
| [CA-02](../HU-011-el-inventario-de-funcionalidades.md#ca-02--sin-inventario-aprobado-no-se-derivan-épicas) | Una regla del `02`: inventario aprobado por el usuario antes de derivar épicas | No existe; el `02` tiene `F0` a `F25` y ninguna pone esa puerta |
| [CA-03](../HU-011-el-inventario-de-funcionalidades.md#ca-03--queda-escrito-si-la-conducta-existente-cubría-preguntar-el-alcance) | El veredicto escrito sobre si `C4`/`C7`/`C17`/`C21` cubrían preguntar el alcance | No existe; las cuatro reglas están leídas y ninguna nombra el caso del alcance asumido |

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que ningún proyecto vuelva a derivar épicas sobre un alcance que el usuario no confirmó: molde publicado, regla vigente y el veredicto de conducta escrito; el pendiente 74 cerrado con su aviso.

**Fuera de alcance:**

- Un validador de la puerta (`20·M19`: la regla primero demuestra servir a mano; las tres preguntas quedan respondidas en el resultado de esta fase para cuando alguien proponga automatizarla).
- Reabrir planteamientos ya escritos (límite del pendiente).
- Migrar los inventarios de proyectos existentes.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-21.

- El caso semilla existe y es bueno: estados por ítem (Existe / Parcial / Por construir / Por confirmar), sección «lo que el usuario ya definió», preguntas abiertas como preguntas, y la declaración de destino (madura hasta manual). Se generaliza quitándole el dominio (ITIL, MAGERIT, sus EP/HU).
- El capítulo `02` recibe la regla nueva con el ID libre siguiente: **`F26`** (`F0` a `F25` tomados, ninguno derogado que la cubra; se buscó por concepto: `F2` pone la puerta spec→código, ninguna pone la puerta propuesta→épicas).
- `plantillas/README.md` indexa los moldes: fila nueva.
- El molde de planteamiento (§6, requerimientos) queda como está: la regla no lo cambia, lo complementa (el inventario es documento aparte que acompaña la propuesta).

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md` | Nuevo | Plantillas | El molde, generalizado del caso semilla; sin rayas ni marcas (el trinquete bloquea en `plantillas/`) |
| [`plantillas/README.md`](../../../../../plantillas/README.md) | Modificar | Plantillas | Su fila |
| `base/02-flujo-de-trabajo/reglas/F26-….md` | Nuevo | Cuerpo de reglas | La regla, por el procedimiento del `20`, con checklist |
| [`base/02-flujo-de-trabajo/base.md`](../../../../../base/02-flujo-de-trabajo/base.md) | Modificar | Cuerpo de reglas | Fila del índice y sección de `F26` |
| [`CHANGELOG.md`](../../../../../CHANGELOG.md) · [`VERSION`](../../../../../VERSION) | Modificar | Versionado | Entrada **MAYOR** (la regla obliga hacia adelante); `VERSION` leída un instante antes (`20·M18`) |
| [`pendientes/74-…`](../../../../../pendientes/hecho/el-inventario-es-la-puerta-de-las-epicas.md) | Mover | Backlog | A `hecho/` con `cerrar.py`, con su aviso de vuelta (`shopnest-mesa` y todos los instalados) |
| [`pendientes/README.md`](../../../../../pendientes/README.md) | Modificar | Backlog | La fila del 74 |
| [`HU-011](../HU-011-el-inventario-de-funcionalidades.md) | Modificar | Documentación | §7 al cerrar; bitácora |
| Documentos de esta fase | Llenar | Documentación | resultado (con el veredicto del CA-03), estado, cierre |
| [`validadores/reglas-validables.md`](../../../../../validadores/reglas-validables.md) | Modificar | Validadores | `F26` se registra (`20·M9`): validable en principio, sin validador por `20·M19` |

> **Ninguna regla existente se toca.** `F26` extiende la cadena; `F2` y el molde de planteamiento quedan como están.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: nada existente cambia de contrato.

### 2.3 Rutas / endpoints  ·  Q6 · 2.4 Punto de entrada  ·  Q7 · 2.5 Permisos  ·  Q8

No aplica API ni permisos. Punto de entrada: la regla llega con el capítulo `02` al abrir sesión; el molde, desde el índice de `plantillas/` y citado por la propia `F26`.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Una sola HU con los tres CA | Partir en molde (EP-003) y regla (otra épica) | Es un solo problema (la puerta) visto en tres piezas; el pendiente ya enruta ambas a EP-003, que «puede pedir molde nuevo y regla de flujo». Partirlo repetiría el hueco del 60: la regla sin historia que la respalde |
| La regla es **MAYOR** | MENOR | Obliga a un proyecto al día a hacer algo nuevo en su próximo encargo: aprobar el inventario antes de derivar. Es el corte del CHANGELOG |
| El veredicto del CA-03 va en el resultado de pruebas | Regla nueva de conducta de una vez | Primero el veredicto; si concluye que hay brecha que `F26` no cierra, la extensión del `01` se propone aparte (`02·F20`), no se legisla de contrabando |
| El molde generaliza el caso semilla | Escribirlo de cero | El semilla ya pasó por el uso real y trae lo que el usuario pidió con sus palabras (estados, preguntas, destino de manual) |

### 2.7 Dudas por resolver antes de ejecutar

Ninguna bloqueante: el ID `F26`, el nombre del molde y el corte MAYOR quedan fijados en este plan, que se aprueba.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — El molde

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Escribir `plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md` generalizando el semilla: estados, «lo que el usuario ya definió», preguntas abiertas, destino de manual | `plantillas/` | 2,0 |
| T-02 | Indexarlo en el README de `plantillas/` | `plantillas/README.md` | 0,3 |

### CA-02 — La regla

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Escribir `F26` por el procedimiento del `20` (molde canónico, ejemplo INCORRECTO/CORRECTO, dependencias), correr su checklist y sellarlo | `base/02-flujo-de-trabajo/` | 2,5 |
| T-04 | Registrarla en `reglas-validables.md` con las tres preguntas de `M19` respondidas | `validadores/` | 0,5 |

### CA-03 — El veredicto de conducta

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-05 | Releer `C4`/`C7`/`C17`/`C21` contra el caso y escribir el veredicto con citas | `resultado_pruebas.md` | 1,0 |

### Cierre

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-06 | Ejecutar los casos y registrar | `resultado_pruebas.md` | 1,0 |
| T-07 | Versionar (MAYOR) | CHANGELOG · VERSION | 0,5 |
| T-08 | Cerrar: pendiente 74 a `hecho/` con avisos, cierre de fase y HU | backlog + fase | 1,0 |

**Total: 8 tareas · 8,8 horas.**

---

## 4. Secuencia de ejecución

T-01 → T-02, luego T-03 → T-04; T-05 puede ir en paralelo a T-03. T-06 → T-07 → T-08 cierran.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). Ninguna regla se edita para que una prueba pase.

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método de verificación | Evidencia |
|---|---|---|
| CA-01 | Molde contra el semilla, en las dos direcciones; `validar.py plantilla` | CP-001 |
| CA-02 | La regla publicada con checklist CUMPLE; aplicada al caso histórico (la detiene) y al estado actual (no reabre) | CP-002 |
| CA-03 | El veredicto escrito con citas de las cuatro conductas | CP-003 |

---

## 6. Datos y ambiente de prueba

Este repositorio más la lectura del caso semilla en `shopnest-mesa` (carpeta autorizada de la sesión; solo lectura). Ningún dato real ni credencial.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit. Si la regla hubiera que retirarla después de publicada, no se borra: se deroga (`20·M11`).

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

Los herederos reciben `F26` y el molde con su próxima instalación; el aviso de desfase marca la MAYOR. Nada retroactivo: los planteamientos ya escritos no se reabren, y el aviso de cierre del 74 le dice a `shopnest-mesa` que su inventario sirve tal cual (queda esperando la aprobación del usuario, que su propio documento ya declara).

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`20·M3`](../../../../../base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md), [`20·M4`](../../../../../base/20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md), [`20·M5`](../../../../../base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md), [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md), [`20·M12`](../../../../../base/20-meta-reglas/reglas/M12-antes-de-crear-una-regla-buscar-la-duplicacion-es-el-defecto-mas-caro.md), [`20·M14`](../../../../../base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md), [`20·M17`](../../../../../base/20-meta-reglas/reglas/M17-la-entrada-del-registro-abre-en-castellano-llano.md), [`20·M18`](../../../../../base/20-meta-reglas/reglas/M18-lo-compartido-se-lee-un-instante-antes-de-escribirlo.md), [`20·M19`](../../../../../base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | La regla leída como burocracia en proyectos chicos | Se la saltan | El ejemplo de `F26` muestra el inventario chico (una tabla corta); la puerta es la aprobación, no el tamaño | Abierto |
| R-02 | El molde arrastra dominio del semilla (ITIL, MAGERIT) | Viola `20·M3` | CP-001 lo busca explícitamente | Mitigado por prueba |
| R-03 | El trinquete de marcas en `plantillas/` y `base/` | Rechaza el commit | Molde y regla se escriben sin rayas ni tipografía de máquina | Abierto |

---

## 11. Definition of Done

- [ ] Molde publicado e indexado; `validar.py plantilla` en verde.
- [ ] `F26` publicada con checklist CUMPLE y registrada en `reglas-validables.md` con sus tres preguntas de `M19`.
- [ ] El veredicto del CA-03 escrito con citas.
- [ ] Versión MAYOR subida; pendiente 74 en `hecho/` con sus avisos.
- [ ] `validar.py estandar`, `plantilla`, `pendientes` y `versionado` sin fallas nuevas.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá: vive en el `funcionalidad_implementada.md`. Este plan se queda como se aprobó.
