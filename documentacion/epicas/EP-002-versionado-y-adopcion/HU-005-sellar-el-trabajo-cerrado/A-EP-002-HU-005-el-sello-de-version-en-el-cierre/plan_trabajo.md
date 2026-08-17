# Plan de Trabajo — Fase A-EP-002-HU-005-el-sello-de-version-en-el-cierre (módulo Versionado y adopción)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-005](../HU-005-sellar-el-trabajo-cerrado.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-002-HU-005-el-sello-de-version-en-el-cierre` |
| **Épica** | [EP-002 Versionado y adopción](../../epica.md) |
| **HU** | [HU-005 Sellar el trabajo cerrado con su versión](../HU-005-sellar-el-trabajo-cerrado.md) — una sola (`F12.1`) |
| **Módulo** | Versionado y adopción |
| **Especificación del módulo** | [HU-005](../HU-005-sellar-el-trabajo-cerrado.md). El entregable es una regla de retroactividad y un campo en los modelos de cierre: sus criterios de aceptación son la especificación |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-002-HU-005-el-sello-de-version-en-el-cierre` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 🔀 **Híbrido.** 📄 Retro-documenta la regla, que existe: la retroactividad está escrita en la cabecera del [`CHANGELOG`](../../../../../CHANGELOG.md) —un cambio de norma no reabre lo cerrado— y el aviso de desfase lo repite. ✨ Y construye lo que falta: **ningún modelo de cierre pide la versión**. Hoy el sello se escribe cuando alguien se acuerda, a mano, en la §8 de la HU. Sale de la fila de HU-005 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-005 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-005-sellar-el-trabajo-cerrado.md#ca-01--lo-cerrado-queda-sellado) | Lo cerrado queda sellado | **A medias.** Ni [`plantillas/estado-fase.md`](../../../../../plantillas/estado-fase.md) ni [`plantillas/funcionalidad-implementada.md`](../../../../../plantillas/funcionalidad-implementada.md) piden la versión |
| [CA-02](../HU-005-sellar-el-trabajo-cerrado.md#ca-02--un-cambio-de-reglas-no-reabre-lo-cerrado) | Un cambio de reglas no reabre lo cerrado | Escrito en el `CHANGELOG` y en el aviso de desfase. Sin prueba |

**Por qué una sola fase.** El CA-02 es la regla y el CA-01 es dónde se escribe: separarlos daría dos fases sobre el mismo párrafo (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que el sello deje de depender de que alguien se acuerde — que el modelo de cierre lo pida — y que la regla de no reabrir quede probada sobre una fase ya cerrada.

**Fuera de alcance:**

- **Sellar hacia atrás las fases ya cerradas.** Si el sello falta en alguna, se anota: reabrir lo cerrado es justo lo que la HU prohíbe.
- **El sello del checklist de cada regla,** que caduca con el texto y es el pendiente [52](../../../../../pendientes/52-el-sello-del-checklist-caduca-con-el-texto.md).
- **El registro de adopciones del proyecto,** que es [HU-003](../../HU-003-version-adoptada-por-el-proyecto/HU-003-version-adoptada-por-el-proyecto.md).
- **La derogación sin adoptar,** que es la excepción de `F22` y ya está retro-documentada en EP-004.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17 buscando la versión en los modelos de cierre y leyendo la cabecera del registro.

**Lo que ya existe:** la regla de retroactividad, escrita en la cabecera del `CHANGELOG` y repetida en el aviso de desfase que devuelve `version.py`; el historial de adopciones por proyecto, en `documentacion/versiones/`, que existe justamente para poder mirar bajo qué reglas se trabajó en cada momento; la costumbre de anotar la versión al cerrar, visible en la §8 de [HU-009](../../../EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/HU-009-reglas-sin-checklist-al-dia.md), que dice «Cerrada 2026-08-16 (v23.1.1)».

**Lo que no existe:**

1. **El campo del sello en los modelos.** Buscado en `plantillas/`: ni el modelo del estado de la fase ni el del cierre piden la versión del estándar. La única plantilla que la nombra es la del stack de instalación, por otro motivo.
2. **La prueba del CA-02.** Que un cambio de reglas no reabra lo cerrado está escrito y nadie lo comprobó contra una fase cerrada de verdad.
3. **La revisión de qué fases cerradas quedaron sin sello.**

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `plantillas/funcionalidad-implementada.md` | Modificar | Le entra el campo del sello: bajo qué versión del estándar cerró la fase |
| `plantillas/estado-fase.md` | Modificar | Igual, para que el sello esté puesto desde antes del cierre |
| `validadores/plantillas.py` | Modificar | Que el campo nuevo se revise cuando se compara un documento contra su modelo |
| `…/A-EP-002-HU-005-…/plan_pruebas.md` | Nuevo | Los casos de los dos CA |
| `…/A-EP-002-HU-005-…/resultado_pruebas.md` | Nuevo | Lo que dieron, con la lista de fases cerradas sin sello |
| `HU-005-sellar-el-trabajo-cerrado.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `CHANGELOG.md` · `VERSION` | Modificar | Cambia `plantillas/`: entrada y subida ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)) |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

### 2.2 Matriz de dependencias del refactor  ·  `F17`

| Archivo que cambia | Qué cambia | Quién depende | Dónde |
|---|---|---|---|
| `plantillas/funcionalidad-implementada.md` y `plantillas/estado-fase.md` | Un campo obligatorio nuevo | [`validadores/plantillas.py`](../../../../../validadores/plantillas.py), que compara documento contra modelo | Los documentos de las fases ya cerradas quedarían sin ese campo: el campo se exige **hacia adelante**, y eso se declara en la regla y en el validador |

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque el entregable son modelos de documento y un programa de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

No aplica. El sello se lee abriendo el documento de cierre de la fase.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El sello se escribe en el documento de la fase, no en un registro aparte | Un archivo central que liste fase y versión | Un registro central se desincroniza de las fases; el sello vive donde se lee el cierre |
| El campo se exige hacia adelante | Exigirlo a todas las fases cerradas | La RN-02 y la regla de retroactividad prohíben reabrir lo cerrado |
| El sello se pone también en el estado de la fase, no solo al cerrar | Solo en el cierre | La RN-04 pide que el sello se escriba al cerrar y no después; tenerlo desde el estado evita reconstruirlo de memoria |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién | Estado |
|---|---|---|---|
| 1 | Si el campo del sello entra en los dos modelos o solo en el del cierre | Usuario | Pendiente |
| 2 | Si el validador lo exige o solo lo avisa cuando falta | Usuario | Pendiente |

Las dos bloquean T-01 a T-03. El CA-02 no depende de ellas.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Lo cerrado queda sellado

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Escribir el campo del sello en el modelo del cierre | `plantillas/funcionalidad-implementada.md` | 1,5 |
| T-02 | Escribir el campo en el modelo del estado de la fase, si la duda 1 lo resuelve así | `plantillas/estado-fase.md` | 1,0 |
| T-03 | Que el validador de modelos vea el campo nuevo, con el alcance que decida la duda 2 | `validadores/plantillas.py` | 2,0 |
| T-04 | Caso de prueba: un cierre sin sello se detecta; uno con sello pasa | `plan_pruebas.md` | 1,5 |
| T-05 | Listar las fases cerradas que quedaron sin sello, sin tocarlas | `resultado_pruebas.md` | 1,0 |

### CA-02 — Un cambio de reglas no reabre lo cerrado

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-06 | Caso de prueba: sobre una fase cerrada bajo una versión anterior, comprobar que ninguna corrida la reporta como incumplida por reglas posteriores | `plan_pruebas.md` | 2,0 |
| T-07 | Caso de prueba de la excepción: si en el desfase hay una derogación sin adoptar, la fase en curso sí se detiene | `plan_pruebas.md` | 1,0 |

### RNF — Que el sello se escriba al cerrar y no después

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-08 | Versionar el cambio de modelos, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 2,0 |

**Total: 8 tareas · 12,0 horas.**

---

## 4. Secuencia de ejecución

T-06 → T-07 primero: no dependen de dudas. T-01 → T-02 → T-03 → T-04 detrás de las dos dudas. T-05 y T-08 cierran.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Un cierre con sello y otro sin sello, revisados contra el modelo | T-04, y la lista de T-05 |
| CA-02 | Una fase cerrada bajo versión anterior, revisada con las reglas de hoy | T-06, T-07 |
| RNF | El sello presente desde el estado de la fase, no reconstruido al final | T-02 |

---

## 6. Datos y ambiente de prueba

Este repositorio: las veinticinco fases que ya existen son el material de prueba. Documentos de mentira en carpeta temporal para el caso negativo. Ningún dato real y ninguna clave.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. Devuelve los dos modelos, el validador y `VERSION`, todo en el mismo commit. Los documentos de fase ya escritos no cambian: el campo se exige hacia adelante.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

Se asume que el estándar está en producción. Un campo obligatorio nuevo en un modelo **obliga** a quien cierre una fase de aquí en adelante: la subida es **MAYOR**, con su marca de que obliga a migrar. Si la duda 2 resuelve que el validador solo avise, es **MENOR**. Las fases cerradas no se tocan.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F6`](../../../../../base/02-flujo-de-trabajo/reglas/F6-persiste-el-trabajo-y-las-decisiones-antes-de-cerrar-la-fase.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`02·F22`](../../../../../base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`15`](../../../../../base/15-registros-inmutables.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Las dos dudas sin resolver | Bloquean el CA-01 | Se presentan al usuario: cambiar modelos sube versión | Abierto |
| R-01 | Que el campo nuevo deje en falta a las veinticinco fases existentes | Ruido en cada corrida | El validador lo exige hacia adelante, con la fecha de corte escrita | Abierto |
| R-02 | Que el sello se escriba a mano y quede mal | Un sello falso es peor que ninguno | El modelo pide de dónde se copió el número, que es `VERSION` | Abierto |
| R-03 | Que otra sesión esté tocando `plantillas/` o `VERSION` | Dos numeraciones vivas, como el pendiente [22](../../../../../pendientes/22-dos-sesiones-versionando-a-la-vez.md) | Se comprueba `VERSION` justo antes de subirla | Abierto |

---

## 11. Definition of Done

- [ ] El modelo del cierre pide bajo qué versión cerró la fase.
- [ ] Un cierre sin sello se detecta.
- [ ] Está probado que un cambio de reglas no reabre lo cerrado, y que la derogación sin adoptar sí detiene lo en curso.
- [ ] Las fases cerradas sin sello están listadas, sin haberlas tocado.
- [ ] `CHANGELOG.md` con su entrada y `VERSION` subida, con el tipo que corresponda.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase — que, si esta fase sale bien, va a ser el primero en llevar su propio sello.
