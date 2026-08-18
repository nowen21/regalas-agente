# Plan de Trabajo — Fase A-EP-004-HU-008-la-corrida-completa-en-una-linea (módulo Comprobación automática)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-008](../HU-008-corrida-completa.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-004-HU-008-la-corrida-completa-en-una-linea` |
| **Épica** | [EP-004 Comprobación automática](../../epica.md) |
| **HU** | [HU-008 Correr todas las comprobaciones de una sola vez](../HU-008-corrida-completa.md) — una sola (`F12.1`) |
| **Módulo** | Comprobación automática |
| **Especificación del módulo** | [HU-008](../HU-008-corrida-completa.md). El entregable es un punto de entrada único: sus criterios de aceptación son la especificación |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-004-HU-008-la-corrida-completa-en-una-linea` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 🔀 **Híbrido.** 📄 Retro-documenta lo que existe: [`validar.py`](../../../../../validadores/validar.py) tiene **24 subcomandos**, cada uno con su corrida y su resumen. ✨ Y construye lo que falta: **ninguno los corre todos**. Hoy, para saber cómo está el proyecto, hay que acordarse de los 24 y leer 24 resúmenes. Sale de la fila de HU-008 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-008 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-008-corrida-completa.md#ca-01--una-sola-línea-corre-todo) | Una sola línea corre todo | **No está.** Hay 24 subcomandos y ninguno que los llame a todos |
| [CA-02](../HU-008-corrida-completa.md#ca-02--se-puede-correr-una-sola) | Se puede correr una sola | Cumplido: es lo único que se puede hacer hoy. Se comprueba que la corrida completa no lo rompa |
| [CA-03](../HU-008-corrida-completa.md#ca-03--el-resultado-de-la-corrida-es-uno-solo) | El resultado de la corrida es uno solo | **No está.** Cada subcomando imprime su propio resumen; no hay un veredicto de la corrida entera |

**Por qué una sola fase.** Los tres CA son el mismo punto de entrada: uno lo crea, otro comprueba que no rompa lo que había y el tercero le pone el resumen (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que una sola línea diga cómo está el proyecto, sin que nadie tenga que acordarse de los 24 subcomandos ni leer 24 resúmenes.

**Fuera de alcance:**

- **Escribir comprobaciones nuevas.** La corrida completa llama a las que ya hay.
- **Los enganches,** que son de EP-005: acá se trata de correr a mano.
- **El conteo por regla,** que es [HU-009](../../HU-009-conteo-por-regla/HU-009-conteo-por-regla.md).
- **Darle punto de entrada a los programas que no lo tienen.** Es el pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md), y la corrida completa no puede llamar a lo que no se puede llamar: los declara como saltados con su motivo.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17: `validar.py --help` lista 24 subcomandos, ninguno de ellos «todo».

**Lo que ya existe:** los 24 subcomandos, cada uno con su corrida, su resumen y su código de salida; el formato común del hallazgo, que hace que las salidas se puedan sumar; la distinción ya escrita entre comprobaciones que corren en seco sobre el estándar y las que necesitan un proyecto real; y la advertencia del registro de reglas validables sobre esa diferencia.

**Lo que no existe:**

1. **El punto de entrada único.** Ninguno de los 24 llama a los demás.
2. **El resumen de la corrida entera.** Hoy hay 24 resúmenes y ningún total.
3. **La lista de qué comprobación aplica a qué.** Sin ella, una corrida completa sobre el estándar fallaría en las que piden proyecto real, y sobre un proyecto fallaría en las que solo aplican al estándar.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/validar.py` | Modificar | El subcomando nuevo, con su lista de qué aplica y el resumen único |
| `validadores/docs/validar.md` | Modificar | Le entra qué hace la corrida completa, qué saltea y por qué |
| `validadores/pruebas.py` | Modificar | Las pruebas del CA-02 y del CA-03 |
| `…/A-EP-004-HU-008-…/plan_pruebas.md` | Nuevo | Los casos de los tres CA |
| `…/A-EP-004-HU-008-…/resultado_pruebas.md` | Nuevo | Lo que dieron |
| `HU-008-corrida-completa.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> Ningún validador se toca por dentro: la corrida completa los llama como están.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

| Archivo que cambia | Qué cambia | Quién depende | Dónde |
|---|---|---|---|
| `validadores/validar.py` | Un subcomando nuevo, y nada más | Los enganches que llaman subcomandos por su nombre | Ninguno se renombra ni se quita, así que nada de lo que hoy llama a `validar.py` rompe |

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque son programas de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

**Sí tiene punto de entrada, y es lo que la fase construye:** una línea de comandos nueva. La HU no introduce interfaz gráfica.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La corrida completa llama a los subcomandos que ya hay | Reescribir las comprobaciones dentro de un programa nuevo | Duplicar lógica deja dos verdades sobre lo mismo |
| Lo que no aplica se saltea diciendo por qué | Fallar, o callar | Callar es lo que hace un validador sin punto de entrada, y por eso el pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md) existe |
| El resumen único no reemplaza los 24 | Imprimir solo el total | Quien corre para arreglar necesita el detalle; el total es para saber si se puede cerrar |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién | Estado |
|---|---|---|---|
| 1 | Si la corrida completa incluye las comprobaciones que corren herramientas del proyecto —linter, pruebas, audit—, que son lentas, o si esas van aparte | Usuario | Pendiente |

La duda 1 bloquea T-01. Las pruebas del CA-02 no dependen de ella.

**Decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md). 👤 marca lo que sigue esperando un dato del usuario.

| Duda | Decisión |
|---|---|
| 23 | **No los incluye.** `linter`, `suite` y `audit` ya son subcomandos aparte: se decidió al construirlo. |

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Una sola línea corre todo

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Escribir el subcomando que corre todas las comprobaciones que aplican al proyecto, en orden | `validadores/validar.py` | 3,0 |
| T-02 | Que las que necesitan un proyecto real se salteen con su motivo dicho, en vez de fallar | `validadores/validar.py` | 2,0 |

### CA-02 — Se puede correr una sola

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Prueba: los 24 subcomandos siguen corriendo por separado después del cambio | `validadores/pruebas.py` | 2,0 |

### CA-03 — El resultado de la corrida es uno solo

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-04 | Que la corrida completa termine con un resumen único: cuántas fallas, cuántos avisos y qué comprobaciones se saltearon | `validadores/validar.py` | 2,0 |
| T-05 | Prueba: con una falla en cualquiera de las comprobaciones, el código de salida de la corrida completa es 1 | `validadores/pruebas.py` | 1,5 |

### RNF — Que la corrida se pueda leer de un vistazo

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-06 | Correr las pruebas, escribir el resultado y cerrar la trazabilidad de la HU y del inventario | Cierre | 1,5 |

**Total: 6 tareas · 12,0 horas.**

---

## 4. Secuencia de ejecución

T-03 primero, que fija que lo que hay no se rompa. T-01 → T-02 → T-04 con la duda resuelta. T-05 y T-06 cierran.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Una línea corre todo lo que aplica, con lo saltado dicho | T-01, T-02 |
| CA-02 | Los 24 subcomandos siguen corriendo por separado | T-03 |
| CA-03 | Resumen único y código de salida de la corrida entera | T-04, T-05 |

---

## 6. Datos y ambiente de prueba

Este repositorio y carpetas temporales para los casos negativos. Ningún dato real y ninguna clave: lo que parezca una clave se arma para la prueba.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

El estándar está adoptado por proyectos. El subcomando es **aditivo**: nadie tiene que cambiar lo que ya corre, así que la subida es **MENOR**. Los enganches que llaman subcomandos por su nombre siguen funcionando.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`05`](../../../../../base/05-errores-y-logging.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que la corrida completa tarde tanto que nadie la use | Se vuelve a correr de a una | Es la duda 1: lo lento se separa o se declara aparte |
| R-02 | Que un subcomando que hoy falla deje la corrida completa siempre en rojo | Nadie la mira | El resumen distingue las fallas propias del proyecto de las heredadas, con su cuenta |
| R-03 | Que la lista de qué aplica quede vieja al agregar un validador | La corrida completa deja de ser completa | La lista se arma de los subcomandos registrados, no a mano |

---

## 11. Definition of Done

- [ ] Una sola línea corre todas las comprobaciones que aplican.
- [ ] Lo que se saltea queda dicho, con su motivo.
- [ ] Los 24 subcomandos siguen corriendo por separado, con prueba.
- [ ] La corrida completa termina con un resumen único y el código de salida correcto.
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
