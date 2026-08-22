# Plan de Trabajo — Fase B-EP-004-HU-004-el-encuadre-de-la-plantilla-sobrevive-al-llenado (módulo Programas de comprobación)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Se escribe **antes** de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-004-HU-004-el-encuadre-de-la-plantilla-sobrevive-al-llenado` |
| **Épica** | `EP-004` Comprobación automática |
| **HU** | `HU-004` Forma de los documentos — **una sola** (`F12.1`) |
| **Módulo** | Programas de comprobación |
| **Especificación del módulo** | [epica.md](../../epica.md) |
| **Fecha apertura** | 2026-08-22 |
| **Rama** | `main` |

**ORIGEN:**

- ✨ **Funcionalidad nueva:** la comprobación que pide el [pendiente 77](../../../../../pendientes/hecho/el-planteamiento-conserva-su-encuadre.md). Sale del hallazgo H-2 de [2026-08-22 · sesión 2](../../../../../historico-chat/resumenes/2026-08-22/sesion-2.md): el planteamiento de este repositorio se escribió con una nota de procedencia en el lugar del encuadre, y nada lo detuvo.

**CA de la HU que cubre esta fase:**

| CA de `HU-004` que cierra esta fase | Estado |
|---|---|
| [CA-05](../HU-004-forma-de-los-documentos.md#ca-05--el-texto-fijo-de-la-plantilla-sobrevive-al-llenado) | ☐ |

---

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que `validar.py plantilla` repruebe un documento al que le borraron o le reemplazaron el texto fijo que su plantilla pone antes del primer separador.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| [CA-05](../HU-004-forma-de-los-documentos.md#ca-05--el-texto-fijo-de-la-plantilla-sobrevive-al-llenado) | El encuadre se borró o se reemplazó | Funcional | Media |

**Fuera de alcance:**

- Juzgar si el encuadre **dice lo correcto**. Se comprueba que esté y que instruya, no su redacción. Es lo que el pendiente 77 declara en su límite.
- Corregir el molde del planteamiento para que declare su encuadre como texto fijo. Eso es la [fase C de EP-003 · HU-002](../../../EP-003-documentos-modelo-y-procedimientos/HU-002-modelos-del-encargo/C-EP-003-HU-002-el-planteamiento-se-reconstruye-igual/plan_trabajo.md), que sigue esperando aprobación. Esta fase se diseñó para no depender de ella.
- Meter la comprobación en una corrida de barrido. `validar.py plantilla` se corre contra un documento a la vez, y así se queda.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Verificado el 2026-08-22:**

1. [`validadores/plantillas.py`](../../../../../validadores/plantillas.py) tiene 208 líneas y su `validar()` hace cuatro comprobaciones: marcadores sin llenar (falla), notas de la plantilla sin borrar (aviso), secciones ausentes (aviso) y reglas de negocio sin origen (falla, solo en la especificación de módulo).
2. `deducir_plantilla()` ya resuelve `*planteamiento*` contra `plantillas/ciclo-vida-proyectos/01-planteamiento.md` por la tabla `POR_NOMBRE`.
3. El encabezado del módulo declara que la plantilla es la fuente de verdad y que **nada se codifica** en el validador. La RN-01 de la HU dice lo mismo. El diseño de esta fase se ata a eso.
4. En `plantillas/ciclo-vida-proyectos/01-planteamiento.md`, entre el H1 y el primer `---` hay dos cosas: el recuadro de instrucciones, que son líneas de cita `>`, y una línea suelta en negrita que es el encuadre. Esa línea cita cuatro reglas.
5. En `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md`, en ese mismo lugar hay una línea fija equivalente que **no cita ninguna regla**. Sirve de contraejemplo: lo que se le exige al documento tiene que salir de su plantilla, no de una idea fija del programa.
6. Las pruebas de los validadores viven en [`validadores/tests/`](../../../../../validadores/tests/), un archivo por tema, y se corren con `python -m pytest validadores/tests`.

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/plantillas.py` | Modificar | Validador | La comprobación nueva |
| `validadores/tests/test_encuadre_de_la_plantilla.py` | Nuevo | Prueba | Los casos del plan de pruebas |
| `CHANGELOG.md` | Modificar | Versionado | Entrada de la versión |
| `VERSION` | Modificar | Versionado | Sube el dígito menor |
| `documentacion/epicas/EP-004-comprobacion-automatica/HU-004-forma-de-los-documentos/HU-004-forma-de-los-documentos.md` | Modificar | Historia | Ya hecho: CA-05, RN-07, RN-08 y la fila de la fase |

### 2.2 Matriz de dependencias del refactor

No aplica: la comprobación se **agrega** a `validar()`. No cambia la firma de ninguna función existente ni el contrato de las cuatro que ya están.

### 2.3 Rutas / endpoints y control de acceso

No aplica porque no hay nada servido por red.

### 2.4 Punto de entrada en la UI

No aplica. El punto de entrada es la línea de comandos que ya existe: `python validadores/validar.py plantilla <documento>`.

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El texto fijo se identifica **por posición**: lo que no es cita `>` ni encabezado, entre el H1 y el primer `---` o el primer `##` | Buscar la etiqueta «Encuadre para el agente» | La etiqueta ya cambió una vez esta misma semana. Un validador atado a una redacción reprueba lo que está bien la primera vez que alguien corrija el molde, que es el caso borde que el planteamiento nombra en §8 |
| La exigencia de citar una regla **se hereda de la plantilla**: solo se pide si la plantilla cita alguna ahí | Exigirla siempre | El plan de trabajo tiene texto fijo y no cita reglas. Exigirlo siempre reprobaría todos los planes del repositorio |
| Falla, no avisa | Aviso | Un aviso más en una corrida que ya trae 43 no lo lee nadie. Y el daño es el que la HU describe: aprobar como insumo algo que perdió la instrucción de que es insumo |
| Se comprueba que **esté** y que **instruya**, no que diga lo correcto | Comparar el texto contra el de la plantilla | Es el límite que el pendiente 77 se puso. Comparar el texto obliga a copiarlo literal y prohíbe adaptarlo, y el molde dice explícitamente que se adapta |

### 2.7 Dudas por resolver antes de codificar

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | ¿Se construye antes o después de la fase C de EP-003 · HU-002, de la que el pendiente 77 decía depender? | usuario | Resuelta: el usuario ordenó ejecutar el pendiente ahora, así que se diseñó sin depender de ella. Por eso la identificación es por posición y no por etiqueta |

---

## 3. Desglose de tareas por criterio de aceptación

### [CA-05](../HU-004-forma-de-los-documentos.md#ca-05--el-texto-fijo-de-la-plantilla-sobrevive-al-llenado) — El texto fijo de la plantilla sobrevive al llenado

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Escribir `bloque_fijo(texto)`: devuelve las líneas que no son cita ni encabezado entre el H1 y el primer `---` o `##` | Validador | 1 h | — | EV-01 |
| T-02 | Agregar a `validar()` la comprobación de que el documento tiene bloque fijo cuando su plantilla lo tiene | Validador | 1 h | T-01 | EV-01 |
| T-03 | Agregar la segunda mitad: si la plantilla cita reglas en su bloque fijo, el documento debe citar alguna | Validador | 1 h | T-02 | EV-01 |
| T-04 | Escribir las pruebas del plan de pruebas | Prueba | 2 h | T-03 | EV-02 |
| T-05 | Correr la comprobación contra los documentos reales del repositorio y confirmar que no reprueba ninguno que esté bien | Prueba | 1 h | T-03 | EV-03 |
| T-06 | Sumar la entrada al `CHANGELOG.md` y subir `VERSION` | Versionado | 0,5 h | T-05 | EV-04 |

**Total estimado:** 6,5 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-04 → T-06
**Paralelizables:** T-05 puede correr apenas termine T-03, sin esperar a las pruebas.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| [CA-05](../HU-004-forma-de-los-documentos.md#ca-05--el-texto-fijo-de-la-plantilla-sobrevive-al-llenado) | Pruebas automatizadas más una corrida contra los documentos reales | EV-01 a EV-03 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | El código | `validadores/plantillas.py` |
| EV-02 | Las pruebas en verde | `validadores/tests/test_encuadre_de_la_plantilla.py` |
| EV-03 | Corrida contra documentos reales | `resultado_pruebas.md` de esta carpeta |
| EV-04 | Entrada de versión | `CHANGELOG.md` y `VERSION` |

---

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | El repositorio, en la máquina del usuario. Ningún dato real ([`00·N4`](../../../../../base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)) |
| Usuarios de prueba | Ninguno |
| Datos precargados | Documentos escritos dentro de la prueba, en carpeta temporal. Los reales solo se leen, en T-05 |

---

## 7. Reversión / rollback  ·  Q11

Revertir el commit de la fase. La comprobación se agrega dentro de `validar()` y no toca las cuatro que ya estaban, así que quitarla las deja como estaban.

---

## 8. Producción y migración incremental  ·  Q12

Aditivo, con una salvedad que hay que decir: es una comprobación **nueva que falla**, así que un documento que hoy pasa puede empezar a reprobar. Eso es lo que se pidió. Por eso T-05 corre contra los documentos reales antes de cerrar: si aparece alguno que reprueba y está bien, el defecto es del validador y se corrige antes de publicar.

---

## 9. Reglas del estándar y del proyecto aplicadas  ·  Q13

- [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), porque el pendiente 77 se ejecuta como fase y no desde su archivo.
- [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), por los cinco archivos de §2.1.
- `20·M10`, porque el cambio se versiona y se registra.
- [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md), sobre lo que se escriba acá.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que la comprobación repruebe documentos que están bien | Enseña a ignorar los veredictos, que es el caso borde del planteamiento §8 | T-05 corre contra los documentos reales antes de cerrar | Abierto |
| R-02 | Que un documento sin `---` ni `##` se tome entero como bloque fijo | Falso negativo silencioso | La región termina en el primero de los dos, y si no hay ninguno el documento no tiene forma de plantilla y no se comprueba | Abierto |

---

## 11. Definition of Done

- [ ] CA-05 verificado con evidencia (§5)
- [ ] Pruebas de la fase en verde ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md))
- [ ] Ningún documento real del repositorio reprobado por esta comprobación estando bien
- [ ] Trazabilidad HU → fase escrita en los dos lados
- [ ] `CHANGELOG.md` y `VERSION` al día
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario  ·  *(opcional — equipo)*

No aplica.

---

## 13. Cierre

**No se escribe acá.** Va en el `funcionalidad_implementada.md` de esta carpeta.
