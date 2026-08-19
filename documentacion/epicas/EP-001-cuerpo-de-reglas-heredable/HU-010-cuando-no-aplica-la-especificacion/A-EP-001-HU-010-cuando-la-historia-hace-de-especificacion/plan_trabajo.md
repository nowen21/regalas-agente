# Plan de Trabajo — Fase A-EP-001-HU-010-cuando-la-historia-hace-de-especificacion (módulo Cuerpo de reglas)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en [HU-010](../HU-010-cuando-no-aplica-la-especificacion.md); el detalle de las pruebas, en el `plan_pruebas.md` de esta misma fase; lo que dieron al correrlas, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** (identificador · [`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-001-HU-010-cuando-la-historia-hace-de-especificacion` |
| **Épica** | [EP-001 Cuerpo de reglas heredable y en capas](../../epica.md) |
| **HU** | [HU-010 Cuándo no aplica la exigencia de especificación](../HU-010-cuando-no-aplica-la-especificacion.md) — una sola (`F12.1`) |
| **Módulo** | Cuerpo de reglas |
| **Especificación del módulo** | [HU-010](../HU-010-cuando-no-aplica-la-especificacion.md) — y es el caso que esta fase viene a resolver: hoy una fase de texto normativo se apoya en su historia porque la regla no dice si eso vale |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-001-HU-010-cuando-la-historia-hace-de-especificacion` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): ✨ **Funcionalidad nueva.** A diferencia de las demás fases de esta épica, acá **no hay nada construido que retro-documentar**: [`02·F2`](../../../../../base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md) sigue escrita como si todo entregable fuera código de un módulo, y el caso del entregable que no es código nunca se escribió. Baja del pendiente [20](../../../../../pendientes/hecho/cuando-la-historia-hace-de-especificacion.md) por la vía que pide [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), y su fila en el inventario es la de HU-010 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-010 | Qué exige | Estado hoy, sin haber tocado nada |
|---|---|---|
| [CA-01](../HU-010-cuando-no-aplica-la-especificacion.md#ca-01--la-regla-dice-cuándo-no-aplica) | La regla dice cuándo no aplica | **No está.** `F2` no nombra el caso, y cada sesión lo resuelve por criterio propio |
| [CA-02](../HU-010-cuando-no-aplica-la-especificacion.md#ca-02--las-dos-fases-abiertas-quedan-resueltas) | Las dos fases abiertas quedan resueltas | **No están resueltas, y ya no son dos.** Contadas el 2026-08-17: **nueve** fases se apoyan en su historia de usuario como especificación y **ocho** declararon que no existe y la anotaron como deuda |

**Por qué una sola fase para los dos CA.** El CA-02 es aplicar lo que decida el CA-01: separarlos daría una fase que escribe la regla y otra que la aplica el mismo día (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que quien abre una fase sepa, leyendo solo la regla, si su entregable necesita especificación aparte — y que ninguna fase quede en el limbo.

**Fuera de alcance:**

- **Escribir las especificaciones que faltan.** Las ocho fases que declararon la deuda la siguen debiendo; lo que esta fase decide es si esa deuda es legítima o no, no la paga.
- **La retro-documentación de módulos sin especificación,** que es [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md) y tiene su propio procedimiento.
- **Reabrir fases cerradas.** La RN-05 de la HU ya lo dice: lo que se decida vale hacia adelante.
- **Cambiar el programa que comprueba la especificación** ([`validadores/flujo.py`](../../../../../validadores/flujo.py)), salvo que la decisión del CA-01 lo exija; si lo exige, se declara acá antes de tocarlo.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado contra el repositorio el 2026-08-17, leyendo la casilla de especificación de las veinticinco fases que hay y corriendo `validar.py flujo`.

**Lo que dice la regla hoy:** [`02·F2`](../../../../../base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md) exige una especificación acordada antes de tocar código, y no nombra ningún caso en que no aplique.

**Lo que hacen las fases:**

| Cómo llenan la casilla de especificación | Cuántas | Ejemplos |
|---|---|---|
| Se apoyan en su historia de usuario, porque el entregable es texto normativo o un programa corto | 9 | [`A-EP-001-HU-001`](../../HU-001-formato-unico-de-regla/A-EP-001-HU-001-molde-de-regla/plan_trabajo.md), [`A-EP-001-HU-002`](../../HU-002-capas-y-precedencia/A-EP-001-HU-002-capas-y-precedencia/plan_trabajo.md), [`A-EP-004-HU-010`](../../../EP-004-comprobacion-automatica/HU-010-convencion-declarada-por-el-proyecto/A-EP-004-HU-010-declaracion-y-comprobacion/plan_trabajo.md) |
| Declaran que no existe y la anotan como deuda | 8 | las fases de EP-005 y EP-007 |
| Nombran una especificación que existe | 5 | las de `documentos-modelo` y `automatismos` |

**Lo que dice el programa:** [`flujo.py`](../../../../../validadores/flujo.py) da por cumplida la exigencia si la casilla trae un enlace a un archivo que existe. Con eso, una fase que enlaza su propia historia **pasa**, y una que escribe «no existe» **avisa**. El programa no está decidiendo el caso de fondo: solo mira si el archivo está.

**Lo que no existe:**

1. **El texto de la regla para este caso.** Ni como excepción con sus tres partes ([`20·M8`](../../../../../base/20-meta-reglas/reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md)) ni como aclaración de que la historia hace de especificación.
2. **El criterio para la fase mezclada,** que entrega texto normativo y código a la vez. Es un criterio transversal de la propia HU y hoy nadie lo tiene escrito.
3. **La cuenta al día.** El pendiente 20 habla de dos fases; hoy son diecisiete las que no nombran una especificación aparte.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md` | Modificar | Cuerpo de reglas | Le entra lo que decida la duda 1, con su bloque de checklist rehecho ([`20·M14`](../../../../../base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md)) |
| `pendientes/20-f2-no-dice-cuando-no-aplica.md` | Modificar | Documentación | Se cierra cuando la regla lo diga, y se corrige la cuenta: no son dos fases |
| `documentacion/epicas/EP-001-…/HU-010-…/A-EP-001-HU-010-…/plan_pruebas.md` | Nuevo | Documentación | Los casos de los dos CA |
| `documentacion/epicas/EP-001-…/HU-010-…/A-EP-001-HU-010-…/resultado_pruebas.md` | Nuevo | Documentación | Lo que dieron, con la tabla de las diecisiete fases |
| `documentacion/epicas/EP-001-…/HU-010-…/HU-010-cuando-no-aplica-la-especificacion.md` | Modificar | Documentación | §7 nombra esta fase; el CA-02 se corrige en su cuenta; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Documentación | Las casillas de la fila de HU-010 |
| `CHANGELOG.md` · `VERSION` | Modificar | Versionado | Cambia una regla de `base/`: entrada y subida ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)) |

### 2.2 Matriz de dependencias del refactor  ·  `F17`

| Archivo que cambia | Qué cambia | Quién depende y podría romper | Dónde |
|---|---|---|---|
| `F2-sin-especificacion-acordada-no-hay-codigo.md` | Le entra un caso en que la exigencia no aplica | [`validadores/flujo.py`](../../../../../validadores/flujo.py), que hoy da por cumplida la exigencia con que el archivo exista | Si la decisión exige distinguir «enlaza su historia» de «enlaza una especificación», el programa hay que ajustarlo, y eso se declara antes de tocarlo |
| El mismo | La casilla de las fases pasa a tener una forma esperada | Las diecisiete fases que hoy la llenan a su manera | Ninguna se reabre si ya cerró (RN-05); las abiertas se ajustan en el CA-02 |

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque el entregable es texto normativo y, si la decisión lo pide, un ajuste de un programa de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

No aplica. La regla se lee al abrir una fase, y el capítulo `02` llega como índice al abrir la sesión.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La cuenta del pendiente 20 se corrige con lo medido, y el pendiente no se borra | Cerrarlo diciendo que eran dos casos | Un pendiente con la cuenta vieja hace decidir sobre un dato falso: hoy son diecisiete fases, no dos |
| Lo que se decida vale hacia adelante y ninguna fase cerrada se reabre | Revisar las veinticinco y ajustarlas todas | Es la RN-05 de la propia historia, y reabrir cerrado desordena la trazabilidad de fases ya selladas |
| El caso de la fase mezclada se escribe, aunque hoy no haya ninguna | Dejarlo para cuando aparezca | Es criterio transversal de la HU, y el primero que se lo encuentre lo va a resolver por su cuenta si no está escrito |

**Cuál de los dos caminos toma la regla no lo decide esta fase:** es la duda 1, y la decide el usuario.

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | Cuál de los dos caminos del pendiente 20: escribirle la excepción a `F2` con sus tres partes, o aceptar en la regla que la historia hace de especificación cuando el entregable no es código | Usuario | Pendiente |
| 2 | Si el caso cubre solo el estándar mismo o cualquier proyecto cuyo entregable no sea código | Usuario | Pendiente |
| 3 | Si `flujo.py` tiene que distinguir las dos formas de llenar la casilla, o le basta con que el archivo exista | Usuario | Pendiente |

Las tres bloquean T-01. **Ninguna tarea de construcción arranca con una duda abierta que la bloquee.**

**Decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md). 👤 marca lo que sigue esperando un dato del usuario.

| Duda | Decisión |
|---|---|
| 18 | **El camino 2 del [pendiente 20](../../../../../pendientes/hecho/cuando-la-historia-hace-de-especificacion.md):** la historia hace de especificación cuando el entregable no es código. Abrirle una excepción a `F2` es la puerta que después nadie cierra. |
| 19 | **Cualquier proyecto cuyo entregable no sea código**, no solo el estándar (`20·M3`). |
| 20 | **Le basta con que el archivo exista.** Distinguir las dos formas es criterio. |

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — La regla dice cuándo no aplica

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Escribir en `F2` lo que decida la duda 1, recorriendo el procedimiento del capítulo `20` | `base/02-…/F2-…md` | 2,5 |
| T-02 | Rehacer el bloque de checklist de `F2` contra la versión nueva, porque el sello anterior queda anulado al cambiar el texto | `base/02-…/F2-…md` | 1,5 |
| T-03 | Escribir el criterio de la fase mezclada, que entrega texto normativo y código a la vez | `base/02-…/F2-…md` | 1,0 |
| T-04 | Caso de prueba: alguien que no participó de la decisión lee solo la regla y responde si su fase necesita especificación | `plan_pruebas.md` | 1,0 |

### CA-02 — Las dos fases abiertas quedan resueltas

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-05 | Levantar la tabla de las diecisiete fases con la forma en que llenan la casilla, y marcar cuáles quedan cubiertas por la regla nueva | `resultado_pruebas.md` | 2,0 |
| T-06 | Caso de prueba: correr `validar.py flujo` y comprobar que no reporta falta de especificación donde la regla exime | `plan_pruebas.md` | 1,0 |
| T-07 | Corregir la cuenta del pendiente 20 y cerrarlo si la regla ya lo resuelve | `pendientes/20-…md` | 1,0 |
| T-08 | Corregir el CA-02 de la HU, que habla de dos fases cuando son diecisiete | `HU-010-…md` | 0,5 |

### RNF — Claridad y no regresión

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-09 | Comprobar que la exigencia sigue en pie para el código de un módulo, con un caso que la use | No regresión | 1,0 |
| T-10 | Versionar, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 10 tareas · 15,0 horas.**

---

## 4. Secuencia de ejecución

T-05 se puede levantar de entrada: es medición y no depende de la decisión. Todo lo demás espera las tres dudas: T-01 → T-02 → T-03 → T-04, después T-06 → T-07 → T-08, y T-09 y T-10 al final.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). Si la duda 3 obliga a tocar `flujo.py`, se amplía el plan antes de editarlo.

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método de verificación | Evidencia |
|---|---|---|
| CA-01 | Lectura de la regla por alguien ajeno a la decisión, que responde sin preguntar | Caso de T-04 |
| CA-02 | Tabla de las diecisiete fases contra la regla nueva, y corrida de `validar.py flujo` | T-05 y el caso de T-06 |
| RNF | Caso de una fase que sí entrega código de un módulo: sigue necesitando especificación | T-09 |

---

## 6. Datos y ambiente de prueba

Este repositorio. La prueba del CA-01 necesita una persona que no participó de la decisión; la del CA-02 se corre con el revisor sobre las fases reales. Ningún dato real y ninguna clave.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. Devuelve el texto de `F2`, su checklist anterior, el pendiente y la HU. Si además se tocó `flujo.py`, el revert lo devuelve con lo demás, porque va en el mismo commit.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

El estándar está adoptado por proyectos, así que se asume que está en producción. Según lo que decida la duda 1, la subida es:

- **MENOR** si la regla solo aclara un caso que ya se resolvía así, sin obligar a nadie a hacer algo nuevo.
- **MAYOR** si obliga a un proyecto al día a llenar la casilla de otra forma o a escribir una especificación que antes se saltaba.

Cuál de las dos se declara al cerrar, no antes: depende del texto que entre. Un proyecto que no se actualice sigue con la `F2` de siempre, y `validar.py versiones` le avisa que quedó atrás.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F2`](../../../../../base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md), [`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`13·DOC17`](../../../../../base/13-documentacion/reglas/DOC17-manten-un-readme-en-cada-nivel-del-arbol-de-trabajo.md), [`20·M8`](../../../../../base/20-meta-reglas/reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md), [`20·M14`](../../../../../base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Las tres dudas de §2.7 sin resolver | Bloquean todo menos la medición | Se presentan al usuario con lo que deja cada camino, y se espera | Abierto |
| R-01 | Que la regla nueva vuelva incumplidoras a fases ya cerradas | Trazabilidad sellada que se reabriría | La RN-05 lo prohíbe, y el texto lo dice: vale hacia adelante | Abierto |
| R-02 | Que la exención se vuelva la puerta por donde se salta la especificación siempre | La regla quedaría vacía | Si es excepción, lleva sus tres partes: condición, límite y quién autoriza | Abierto |
| R-03 | Que tocar `flujo.py` rompa alguna de las 246 pruebas | Suite roja | Solo se toca si la duda 3 lo pide, con el plan ampliado, y se corre la suite completa | Abierto |
| R-04 | Que la cuenta de diecisiete cambie mientras se trabaja, porque se abren fases nuevas | La tabla del CA-02 nace vieja | La tabla se levanta al final, en T-05, y dice contra qué día se contó | Abierto |

---

## 11. Definition of Done

- [ ] `F2` dice si el caso del entregable que no es código está cubierto, y con qué condición.
- [ ] El criterio de la fase mezclada está escrito.
- [ ] Alguien ajeno a la decisión respondió leyendo solo la regla.
- [ ] Las diecisiete fases están en la tabla, cada una marcada como cubierta o con lo que le falta.
- [ ] La exigencia sigue en pie para el código de un módulo.
- [ ] El pendiente 20 dice la verdad, y se cerró si la regla ya lo resuelve.
- [ ] `CHANGELOG.md` con su entrada y `VERSION` subida, con el tipo que corresponda.
- [ ] §7 de la HU nombra esta fase, y la fila de HU-010 del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase. Este plan se queda como se aprobó, para poder comparar lo que se dijo contra lo que pasó.
