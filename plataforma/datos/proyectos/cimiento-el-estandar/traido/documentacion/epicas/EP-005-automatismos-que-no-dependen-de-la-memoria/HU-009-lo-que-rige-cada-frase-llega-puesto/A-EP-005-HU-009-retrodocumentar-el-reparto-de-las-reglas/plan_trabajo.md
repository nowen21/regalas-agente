# Plan de Trabajo — Fase A-EP-005-HU-009-retrodocumentar-el-reparto-de-las-reglas (módulo Automatismos)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en [HU-009](../HU-009-lo-que-rige-cada-frase-llega-puesto.md); el detalle de las pruebas, en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase; lo que dieron al correrlas, en el [resultado_pruebas.md](resultado_pruebas.md); lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** (identificador · [`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-005-HU-009-retrodocumentar-el-reparto-de-las-reglas` |
| **Épica** | [EP-005](../../epica.md) |
| **HU** | [HU-009 Lo que gobierna cada frase llega puesto al abrir la sesión](../HU-009-lo-que-rige-cada-frase-llega-puesto.md) |
| **Módulo** | Automatismos |
| **Especificación del módulo** | [documentacion/automatismos/spec.md](../../../../automatismos/spec.md), escrita el 2026-08-14. Esta fase le agrega el reparto de las reglas, que no está |
| **Fecha apertura** | 2026-08-15 |
| **Rama** | `feature/A-EP-005-HU-009-retrodocumentar-el-reparto-de-las-reglas` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 📄 **Retro-documentación** ([`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md)). El programa existe desde la versión 5.0.0 y hace lo que la HU pide; lo que no existe es qué se le exige. Sale del hallazgo [H-4 del 2026-08-14 · `el-enganche-del-resumen-no-crea-el-resumen`](../../../../../historico-chat/resumenes/2026-08-14/el-enganche-del-resumen-no-crea-el-resumen.md), y del descubrimiento que ese hallazgo dio por cierto sin verificar: que los capítulos `00` y `01` no llegaban puestos. Sí llegan.

**CA de la HU que cubre esta fase**

| CA de HU-009 | Qué valida | Estado hoy, sin haber tocado nada |
|---|---|---|
| [CA-01](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#ca-01--los-capítulos-que-rigen-cada-frase-llegan-con-su-texto) | Los capítulos `00` y `01` llegan con su texto | Se cumple. Falta probarlo y dejarlo escrito |
| [CA-02](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#ca-02--se-dice-qué-llegó-puesto-y-qué-llegó-como-índice) | Se dice qué llegó puesto y qué como índice | Se cumple. Falta probarlo |
| [CA-03](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#ca-03--el-arranque-no-se-vuelve-lento) | El arranque no se vuelve lento | **Sin medir.** Nadie sabe cuánto cuesta hoy |

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que el reparto de las reglas deje de ser una decisión que solo vive en un comentario del programa, y pase a estar exigida, probada y medida.

**Fuera de alcance:**

- **Cambiar el reparto.** Si al medir aparece que hay que cambiarlo, se para y se propone: es otra fase.
- **El capítulo `02` por momento**, que es [HU-010](../../HU-010-la-regla-llega-al-escribir-el-archivo/HU-010-la-regla-llega-al-escribir-el-archivo.md).
- **Comprobar que la regla se cumplió**, que es EP-004.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado contra el programa el 2026-08-15, corriéndolo sobre este repositorio.

**Lo que hace hoy** [`validadores/cargador.py`](../../../../../validadores/cargador.py):

| Qué | Cómo |
|---|---|
| Decide qué va completo | Por el primer tramo de la ruta: lo que empieza por `00-` o `01-` ([línea 35](../../../../../validadores/cargador.py)) |
| Arma el índice del resto | Ruta, peso en KB y título sacado del propio archivo |
| Avisa qué es cada cosa | Dos encabezados: uno dice que lo cargado es obligatorio, el otro que lo demás hay que abrirlo antes de tocar el tema |
| Se detiene | Si el gate [`02·F13`](../../../../../base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md) no pasa, manda solo esa regla y nada más |

**La medición de hoy:** lo que se inyecta pesa **73 KB**. Llegan completos `00-nucleo-blindado.md`, `00-identidad-y-rol/` y `01-conducta.md`. `ID8` llega completa; `F9`, del capítulo `02`, no.

**Lo que no está escrito en ninguna parte:** que ese reparto es una exigencia y no una casualidad. Si alguien cambia esa línea 35, nada avisa.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `documentacion/automatismos/spec.md` | Modificar | Especificación | Le entra el reparto de las reglas: qué va completo, qué va en índice y por qué |
| `validadores/pruebas.py` | Modificar | Pruebas | Los casos de esta fase, que hoy no existen: nadie prueba el cargador |
| `pendientes/25-las-reglas-de-como-se-escribe-van-en-el-indice.md` | Modificar | Documentación | Se corrige: pide algo que ya está hecho |
| `CHANGELOG.md` · `VERSION` | Modificar | Versionado | [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md) |

> **`validadores/cargador.py` no se toca.** Si la medición obliga a cambiarlo, se para y se propone.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: no se cambia ningún contrato. Se agregan pruebas y documentación sobre lo que ya corre.

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

N/A: es un programa de línea de comandos.

### 2.4 Punto de entrada en la UI  ·  `F14` Q7

N/A.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Documentar el reparto como está y probarlo | Cambiarlo de paso, ya que se está mirando | Es lo que prohíbe [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md): lo que aparece fuera del criterio se para y se propone |
| La medición del arranque va contra este repositorio | Un proyecto de prueba con `base/` recortado | El costo real es el de un cuerpo de reglas completo, no el de uno de juguete |
| El pendiente 25 se corrige, no se borra | Borrarlo por estar cumplido | Su valor ahora es otro: deja escrito que el diagnóstico era falso, para que nadie lo repita |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

---

## 3. Desglose de tareas por criterio de aceptación

### [CA-01](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#ca-01--los-capítulos-que-rigen-cada-frase-llegan-con-su-texto) y [CA-02](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#ca-02--se-dice-qué-llegó-puesto-y-qué-llegó-como-índice) — Lo que llega, y que se sepa qué llegó

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Escribir en la especificación del módulo qué va completo, qué va en índice y por qué | `automatismos/spec.md` | 2,0 |
| T-02 | Prueba: los capítulos `00` y `01` llegan con su texto, y un capítulo cualquiera del resto llega como índice | `pruebas.py` | 2,0 |
| T-03 | Prueba: el contexto dice cuál va puesto y cuál hay que abrir | `pruebas.py` | 1,0 |
| T-04 | Prueba de los bordes: sin `base/` no entrega nada, y con el gate sin pasar entrega solo esa regla | `pruebas.py` | 1,5 |

### [CA-03](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#ca-03--el-arranque-no-se-vuelve-lento) — Lo que cuesta

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-05 | Medir el peso de lo que se inyecta y el tiempo del enganche que lo entrega, contra este repositorio | — | 1,0 |
| T-06 | Dejar la medición escrita en el resultado, con la fecha y el tamaño del cuerpo de reglas | `resultado_pruebas.md` | 0,5 |

### Arrastre

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-07 | Corregir el pendiente 25: lo que pedía ya está hecho, y su diagnóstico era falso | `pendientes/25-…` | 1,0 |
| T-08 | Entrada del `CHANGELOG` y subida de `VERSION` | raíz | 0,5 |

**Total: 8 tareas · 9,5 horas.**

---

## 4. Secuencia de ejecución

T-01 → T-02 → T-03 → T-04 → T-05 → T-06 → T-07 → T-08.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). Descubrir uno nuevo → parar, reportar, ampliar el plan con el visto bueno.

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| Exigencia | Método de verificación | Caso |
|---|---|---|
| CA-01 | Correr el cargador sobre este repositorio y buscar el texto de una regla de cada capítulo | CP-001 |
| CA-02 | Leer los dos encabezados del contexto entregado | CP-002 |
| CA-03 | Medir peso y tiempo, y compararlos con el enganche más lento que ya corre | CP-004 |
| Transversales | Sin `base/`, con el gate sin pasar, y comprobando que no escribe nada | CP-003 y CP-005 |

---

## 6. Datos y ambiente de prueba

Este repositorio para la medición, y carpetas temporales para los bordes. Nada se escribe fuera de ellas.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit. No hay cambio de comportamiento que deshacer: solo documentación y pruebas.

---

## 8. Producción y migración incremental  ·  `F10` · `F14` Q12

No aplica: no cambia nada de lo que ya corre en los proyectos instalados.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F2`](../../../../../base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md), [`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md), [`08·T1`](../../../../../base/08-pruebas.md#t1--todo-cambio-con-lógica-lleva-prueba), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Que la medición muestre que el arranque ya es caro | Media | Alto | No se cambia acá: se para, se reporta y se decide en otra fase |
| Que las pruebas nuevas se aten a los títulos de las reglas y se rompan al renombrar una | Media | Medio | Se comprueba el reparto y los encabezados, no el texto de una regla concreta |
| Que otra sesión esté tocando `pruebas.py` | Alta | Medio | Se guarda solo lo propio, como en las fases anteriores |

---

## 11. Definition of Done

- [ ] La especificación del módulo dice qué llega completo, qué llega en índice y por qué.
- [ ] Hay pruebas que fallan si alguien cambia el reparto sin querer.
- [ ] El costo del arranque está medido y escrito.
- [ ] El pendiente 25 dice la verdad.
- [ ] `validar.py estandar` sin fallas propias.

---

## 12. Seguimiento diario

N/A: una sola sesión.

---

## 13. Cierre

Se llena al cerrar, en el `funcionalidad_implementada.md`.
