# Plan de Trabajo — Fase A-EP-005-HU-002-enmascarar-la-clave-antes-de-escribirla (módulo Automatismos)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar. El requisito vive en [HU-002](../HU-002-enmascarar-claves.md); las pruebas, en el `plan_pruebas.md` de esta fase; lo que dieron, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-005-HU-002-enmascarar-la-clave-antes-de-escribirla` |
| **Épica** | [EP-005 Automatismos que no dependen de la memoria](../../epica.md) |
| **HU** | [HU-002 Enmascarar una clave antes de que quede escrita](../HU-002-enmascarar-claves.md) — una sola (`F12.1`) |
| **Módulo** | Automatismos |
| **Especificación del módulo** | [documentacion/automatismos/spec.md](../../../../automatismos/spec.md). Existe desde el 2026-08-14 y crece por incrementos; esta fase le agrega el suyo (`02·F2`) |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `feature/A-EP-005-HU-002-enmascarar-la-clave-antes-de-escribirla` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): ✨ **Funcionalidad nueva.** Buscado en todo el repositorio el 2026-08-17: **ningún programa enmascara**. [`secretos.py`](../../../../../validadores/secretos.py) **detecta** claves ya escritas en el código; nada tapa una clave antes de que quede escrita. Y el enganche que escribe la transcripción la copia tal cual. Sale de la fila de HU-002 en el pendiente [48](../../../../../pendientes/48-inventario-hu.md).

**CA de la HU que cubre esta fase**

| CA de HU-002 | Qué exige | Estado hoy |
|---|---|---|
| [CA-01](../HU-002-enmascarar-claves.md#ca-01--una-clave-pegada-en-el-chat-no-queda-escrita-en-claro) | Una clave pegada en el chat no queda escrita en claro | **No está.** Es también el CA-02 de [EP-001 · HU-003](../../../EP-001-cuerpo-de-reglas-heredable/HU-003-nucleo-que-no-se-sobrescribe/HU-003-nucleo-que-no-se-sobrescribe.md), que quedó cumplido a medias por esto mismo: la prohibición está escrita en `00·N6` y el enmascarado no existe |
| [CA-02](../HU-002-enmascarar-claves.md#ca-02--el-texto-sigue-siendo-legible) | El texto sigue siendo legible | **No está**, y es lo que decide si el enmascarado sirve: si tapa de más, la transcripción deja de servir como rastro |

**Por qué una sola fase.** Los dos CA son el mismo programa: uno tapa y el otro comprueba que no tape de más (`02·F12.10`).

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que una clave pegada en el chat no quede escrita en claro en ninguna parte, sin que la transcripción deje de servir como rastro.

**Fuera de alcance:**

- **Detectar claves ya escritas en el código,** que es [EP-004 · HU-007](../../../EP-004-comprobacion-automatica/HU-007-claves-y-datos-sensibles/HU-007-claves-y-datos-sensibles.md) y ya corre.
- **Reescribir las transcripciones viejas.** Si en alguna quedó una clave, es un incidente: se reporta al usuario y se decide aparte. Reescribir el rastro por cuenta propia es peor que el problema.
- **Enmascarar en el resumen o en los documentos que escribe el agente.** Empieza por la transcripción, que es donde entra lo que el usuario pega.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado el 2026-08-17: `grep` de «enmascar» en todo `validadores/` da un solo archivo, y no es de esto.

**Lo que ya existe:** el reconocimiento de claves de `secretos.py`, que es la mitad del trabajo; el enganche de la transcripción, que es donde hay que llamarlo; la regla blindada que lo exige, `00·N6`; y el acuerdo del usuario de no usar secretos literales en los datos de prueba, que le da al programa un caso claro de lo que **no** debe tapar.

**Lo que no existe:**

1. **El programa que enmascara.** Nada.
2. **La llamada desde el enganche.** La transcripción se escribe tal cual llega.
3. **El criterio de qué se tapa y qué no.** Sin él, el enmascarado tapa de más y la transcripción se vuelve ilegible, o tapa de menos y no sirve.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/enmascarar.py` | Nuevo | El programa: reconoce con lo que ya sabe `secretos.py` y tapa |
| `validadores/hook_historico.py` | Modificar | Lo llama antes de escribir el mensaje |
| `validadores/docs/enmascarar.md` | Nuevo | Qué se tapa, qué no y con qué marca |
| `validadores/pruebas.py` | Modificar | Los casos de los dos CA |
| `documentacion/automatismos/spec.md` | Modificar | El incremento del enmascarado |
| `validadores/reglas-validables.md` | Modificar | Lo que aporta a `00·N6` |
| `…/A-EP-005-HU-002-…/plan_pruebas.md` · `resultado_pruebas.md` | Nuevo | Los casos y lo que dieron |
| `HU-002-enmascarar-claves.md` | Modificar | §7 nombra esta fase; §1 cambia de estado al cerrar |
| `pendientes/48-inventario-hu.md` | Modificar | Las casillas de su fila |

> `secretos.py` no se toca: se le pide lo que ya sabe reconocer.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

| Archivo que cambia | Qué cambia | Quién depende | Dónde |
|---|---|---|---|
| `validadores/hook_historico.py` | Pasa a escribir el texto enmascarado | El histórico entero y la fase A de HU-001, que lo prueba | Si el enmascarado falla, la transcripción no se escribe: el enganche tiene que seguir escribiendo aunque el enmascarado se caiga, y eso va probado |
| `validadores/secretos.py` | No cambia, se le importa | El programa nuevo | Si su reconocimiento cambia, el enmascarado cambia con él — y eso es lo que se quiere |

### 2.3 Rutas / endpoints y control de acceso  ·  `F14` Q6

No aplica porque son enganches de línea de comandos.

### 2.4 Punto de entrada en la interfaz  ·  `F14` Q7

**Sí tiene punto de entrada, y no hace falta pedirlo:** corre dentro del enganche de la transcripción, con cada mensaje.

### 2.5 Permisos / roles a sembrar  ·  `F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El enmascarado usa el reconocimiento de `secretos.py` | Escribir su propio reconocedor | Dos reconocedores distintos taparían y detectarían cosas distintas, y el peor caso es que uno tape y el otro no |
| Si el enmascarado se cae, la transcripción se escribe igual | Que no se escriba nada | Perder el rastro de la sesión por un fallo del enmascarado es cambiar un riesgo por otro peor |
| La marca dice que hubo una clave, no cuál | Borrar el fragmento sin marca | Sin marca, quien lea la transcripción no entiende el mensaje; con la clave, no sirvió de nada |
| Las transcripciones viejas no se reescriben | Limpiarlas de paso | Reescribir el rastro es lo que prohíbe el capítulo de registros inmutables; si hay una clave vieja, es un incidente y lo decide el usuario |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién | Estado |
|---|---|---|---|
| 1 | Con qué marca se tapa, para que se vea que hubo algo y no se confunda con texto del usuario | Usuario | Pendiente |
| 2 | Qué se hace si aparece una clave en una transcripción vieja: se reporta y se espera, o hay un procedimiento | Usuario | Pendiente |

La duda 1 bloquea T-04. La duda 2 no bloquea nada de esta fase: define qué hacer si el hallazgo aparece.

**Decididas el 2026-08-18**, en el [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md). 👤 marca lo que sigue esperando un dato del usuario.

| Duda | Decisión |
|---|---|
| 29 | **`«enmascarado»`**, la misma marca que el estándar usa para el espacio por llenar. |
| 30 | **La vieja se enmascara igual, y queda dicho en el archivo.** El bloque no se borra: borrar pierde lo dicho. |

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — Una clave pegada en el chat no queda escrita en claro

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Escribir el enmascarado, reusando lo que `secretos.py` ya sabe reconocer como clave | `validadores/` | 3,0 |
| T-02 | Que el enganche de la transcripción lo llame antes de escribir | `validadores/hook_historico.py` | 2,0 |
| T-03 | Caso de prueba: una clave armada, pegada en el chat, no aparece en claro en el archivo | `plan_pruebas.md` | 2,0 |

### CA-02 — El texto sigue siendo legible

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-04 | Que la marca diga qué se tapó y deje el resto del mensaje intacto | `validadores/` | 2,0 |
| T-05 | Caso de prueba: un mensaje con una clave en medio queda legible, y se ve dónde estaba | `plan_pruebas.md` | 1,5 |
| T-06 | Caso de prueba: un ejemplo o un dato de prueba no se tapa | `plan_pruebas.md` | 1,5 |

### RNF — Que la transcripción siga sirviendo de rastro

| # | Tarea | Categoría | Horas |
|---|---|---|---|
| T-07 | Correr las pruebas, escribir el incremento de la especificación y cerrar la trazabilidad de la HU y del inventario | Cierre | 2,0 |

**Total: 7 tareas · 14,0 horas.**

---

## 4. Secuencia de ejecución

T-01 primero. T-02 después, con la prueba de que el enganche sigue escribiendo si el enmascarado falla. T-04 con la duda 1. T-03, T-05, T-06 y T-07 al final.

> Solo se tocan los archivos de §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método | Evidencia |
|---|---|---|
| CA-01 | Clave armada pegada en el chat, ausente del archivo | T-01, T-02, T-03 |
| CA-02 | Mensaje legible con la marca, y el ejemplo que no se tapa | T-04, T-05, T-06 |

---

## 6. Datos y ambiente de prueba

Carpetas temporales para los casos, y este repositorio para las corridas. Ningún dato real y ninguna clave: lo que parezca una clave se arma para la prueba.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

El estándar está en producción y este enganche corre en cada proyecto instalado. El cambio **obliga**: la transcripción pasa a escribirse distinto. Subida **MAYOR** con su marca, y la entrada del registro tiene que decir que las transcripciones viejas no se tocan.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`08·T1`](../../../../../base/08-pruebas.md), [`13·DOC6`](../../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`00·N6`](../../../../../base/00-nucleo-blindado.md), [`04`](../../../../../base/04-seguridad.md), [`12`](../../../../../base/12-privacidad-datos.md), [`15`](../../../../../base/15-registros-inmutables.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | La duda 1 sin resolver | Bloquea la marca | Se presenta al usuario |
| R-01 | Que el enmascarado tape de más | La transcripción deja de servir | El CA-02 es exactamente esa prueba, y va antes de dar la fase por buena |
| R-02 | Que el enmascarado se caiga y se pierda la transcripción | Se perdería el rastro de la sesión | Va probado: si el enmascarado falla, se escribe igual y queda dicho que falló |
| R-03 | Que al probar aparezca una clave real en una transcripción vieja | Incidente de verdad | Se para, se reporta al usuario y no se reescribe nada por cuenta propia |

---

## 11. Definition of Done

- [ ] Una clave pegada en el chat no queda en claro, con prueba.
- [ ] El mensaje sigue legible y se ve dónde estaba la clave.
- [ ] Un ejemplo o un dato de prueba no se tapa.
- [ ] Si el enmascarado falla, la transcripción se escribe igual y lo dice.
- [ ] `CHANGELOG.md` con su entrada y `VERSION` subida, con su marca de que obliga.
- [ ] `validar.py estandar`, `fases`, `trazabilidad` y `flujo` sin fallas nuevas.
- [ ] §7 de la HU nombra esta fase, y la fila del inventario está marcada.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá. El cierre vive en el `funcionalidad_implementada.md` de esta fase.
