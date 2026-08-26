# Plan de Trabajo — Fase A-EP-005-HU-006-la-bateria-antes-de-publicar (módulo Automatismos)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-006](../HU-006-bateria-antes-de-publicar.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-005-HU-006-la-bateria-antes-de-publicar` |
| **Épica** | [EP-005 Automatismos que no dependen de la memoria](../../epica.md) |
| **HU** | [HU-006 Correr la batería completa antes de publicar](../HU-006-bateria-antes-de-publicar.md) — una sola (`F12.1`) |
| **Módulo** | Automatismos |
| **Especificación del módulo** | [documentacion/automatismos/spec.md](../../../../automatismos/spec.md). Existe desde el 2026-08-14 y crece por incrementos; esta fase le agrega el suyo (`02·F2`) |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-005-HU-006-la-bateria-antes-de-publicar` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): ✨ **Funcionalidad nueva.** No hay batería que correr: [EP-004 · HU-008](../../../EP-004-comprobacion-automatica/HU-008-corrida-completa/HU-008-corrida-completa.md) es la que crea la corrida completa, y esta HU es la que la dispara antes de publicar. Lo que existe hoy es [`ci.py`](../../../../../validadores/ci.py), que comprueba que **el proyecto tenga** un pipeline con pruebas y linter — no que se haya corrido. Sale de la fila de HU-006 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-006 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-006-bateria-antes-de-publicar.md#ca-01--antes-de-publicar-corre-todo) | Antes de publicar corre todo | **No está**, y depende de que exista la corrida completa |
| [CA-02](../HU-006-bateria-antes-de-publicar.md#ca-02--un-incumplimiento-claro-detiene-la-publicación) | Un incumplimiento claro detiene la publicación | **No está.** Y hay que separar: publicar lo autoriza y lo corre una persona (`00·N2`), así que lo que la batería hace es negar el visto bueno, no impedir la acción de nadie |

**Por qué una sola fase.** Los dos CA son la misma batería: una la corre y el otro la interpreta (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que nadie publique sin saber cómo está el proyecto, y que un incumplimiento claro quede dicho antes y no después.

**Fuera de alcance:**

- **Construir la corrida completa,** que es [EP-004 · HU-008](../../../EP-004-comprobacion-automatica/HU-008-corrida-completa/HU-008-corrida-completa.md) y va antes.
- **Publicar.** Lo autoriza y lo corre una persona: `00·N2` es blindada y esta fase no la toca.
- **El pipeline del proyecto,** que ya revisa `ci.py`.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17: `validar.py ci` comprueba que exista el pipeline; ningún programa corre una batería antes de publicar, y no hay batería completa que correr.

**Lo que ya existe:** los 24 subcomandos, que son las piezas de la batería; la comprobación de que el proyecto tenga su pipeline; la regla blindada de que publicar lo autoriza una persona; y el capítulo de despliegue, que ya dice que el agente produce los artefactos y no ejecuta el despliegue.

**Lo que no existe:**

1. **La batería.** Es la corrida completa de EP-004 · HU-008, y todavía no está.
2. **El disparo antes de publicar.** Nada lo corre.
3. **El veredicto.** Sin un resultado único no hay con qué decir «se puede publicar» o «no».

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/` | Modificar | El disparo de la batería antes de publicar, apoyado en la corrida completa |
| `validadores/docs/` | Modificar | Qué corre, cuándo y qué significa su veredicto |
| `validadores/pruebas.py` | Modificar | Los casos de los dos CA |
| `documentacion/automatismos/spec.md` | Modificar | El incremento |
| `…/A-EP-005-HU-006-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos y lo que dieron |
| `HU-006-bateria-antes-de-publicar.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `CHANGELOG.md` · `VERSION` | Modificar | Entrada y subida |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> Nada de `00` se toca: el visto bueno de publicar sigue siendo del usuario.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

| Archivo que cambia | Qué cambia | Quién depende | Dónde |
|---|---|---|---|
| La batería | Depende de la corrida completa de EP-004 · HU-008 | Esta fase entera | Sin esa corrida, acá no hay nada que disparar: es la duda 1 |

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque son enganches de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

El veredicto se ve en la salida de la batería, en la línea de comandos. No hay interfaz gráfica, y la publicación la sigue haciendo una persona.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La batería niega el visto bueno, no impide la acción | Que el programa bloquee la publicación | Publicar lo corre una persona: un programa que dice que bloquea lo que no controla miente |
| El veredicto dice qué falló y qué se saltó | Un sí o un no | Un no sin motivo se ignora o se fuerza |
| Se apoya en la corrida completa en vez de rearmarla | Correr los 24 subcomandos desde acá | Dos formas de correr todo dan dos verdades |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién | Estado |
|---|---|---|---|
| 1 | Si esta fase espera a que exista la corrida completa de EP-004 · HU-008, o si arranca con una lista propia y después se apoya en ella | Usuario | **Resuelta el 2026-08-18**, decisión 40 del pendiente 59: publicar es subir al repositorio compartido; el despliegue es del capítulo `18`, que es opt-in y nadie tiene encendido |
| 2 | Qué cuenta como «publicar» en un proyecto: el commit a la rama principal, el despliegue, o los dos | Usuario | **Resuelta el 2026-08-18**, decisión 40 del pendiente 59: publicar es subir al repositorio compartido; el despliegue es del capítulo `18`, que es opt-in y nadie tiene encendido |

Las dos bloquean T-01. **Ninguna tarea de construcción arranca con una duda abierta que la bloquee.**

**Decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/hecho/las-42-dudas-que-detenian-26-fases.md). 👤 marca lo que sigue esperando un dato del usuario.

| Duda | Decisión |
|---|---|
| 33 | **No espera:** la corrida completa ya está construida. |
| 40 | **Publicar es subir al repositorio compartido.** El despliegue es del capítulo `18`, opt-in y apagado. |

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Antes de publicar corre todo

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Que antes de publicar se corra la batería completa, con lo que aplique al proyecto | `validadores/` | 3,0 |
| T-02 | Caso de prueba: al pedir publicar, la batería corre y su resultado queda escrito | `plan_pruebas.md` | 2,0 |

### CA-02 — Un incumplimiento claro detiene la publicación

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Que una falla deje la publicación sin visto bueno, y que un aviso no | `validadores/` | 2,0 |
| T-04 | Caso de prueba: con una falla, el veredicto es que no se puede publicar, con el motivo | `plan_pruebas.md` | 1,5 |

### RNF — Que el paso no se saltee

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-05 | Correr las pruebas, escribir el incremento de la especificación y cerrar la trazabilidad de la HU y del inventario | Cierre | 2,0 |

**Total: 5 tareas · 10,5 horas.**

---

## 4. Secuencia de ejecución

Nada arranca sin la duda 1. Después T-01 → T-02 → T-03 → T-04, y T-05 cierra.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Pedido de publicar con la batería corriendo y su resultado escrito | T-01, T-02 |
| CA-02 | Falla que niega el visto bueno, y aviso que no lo niega | T-03, T-04 |

---

## 6. Datos y ambiente de prueba

Carpetas temporales para los casos, y este repositorio para las corridas. Ningún dato real y ninguna clave: lo que parezca una clave se arma para la prueba.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

El estándar está en producción. Un paso nuevo antes de publicar **obliga**: subida **MAYOR** con su marca. Los proyectos que no se actualicen siguen publicando como hoy.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`00·N2`](../../../../../base/00-nucleo-blindado.md), [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md), [`09`](../../../../../base/09-git.md), [`18`](../../../../../base/18-despliegue-e-infraestructura.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Las dos dudas sin resolver | Bloquean toda la fase | Se presentan al usuario |
| R-01 | Que la batería tarde tanto que se saltee siempre | Un paso que se saltea es peor que ninguno | Se hereda la separación de lo lento que decida EP-004 · HU-008 |
| R-02 | Que el veredicto se lea como que el programa bloqueó la publicación | Se le atribuye un poder que no tiene | El texto lo dice: niega el visto bueno; publicar lo hace una persona |
| R-03 | Que la fase se construya antes de la corrida completa y haya que rehacerla | Trabajo doble | Es la duda 1 |

---

## 11. Definition of Done

- [ ] La batería corre antes de publicar y su resultado queda escrito.
- [ ] Una falla deja la publicación sin visto bueno, con el motivo.
- [ ] Está dicho qué cuenta como publicar.
- [ ] `CHANGELOG.md` con su entrada y `VERSION` subida.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
