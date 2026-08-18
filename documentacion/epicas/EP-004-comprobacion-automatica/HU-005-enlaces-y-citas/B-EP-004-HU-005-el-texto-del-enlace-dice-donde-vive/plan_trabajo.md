# Plan de Trabajo — Fase B-EP-004-HU-005-el-texto-del-enlace-dice-donde-vive (módulo Enlaces y citas)

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden y sobre qué archivos. El requisito vive en [HU-005](../HU-005-enlaces-y-citas.md); las pruebas, en el [plan_pruebas.md](plan_pruebas.md).

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-004-HU-005-el-texto-del-enlace-dice-donde-vive` |
| **Épica** | [EP-004 Comprobación automática](../../epica.md) |
| **HU** | [HU-005 Comprobar los enlaces y las citas a reglas](../HU-005-enlaces-y-citas.md) |
| **Módulo** | Enlaces y citas (`validadores/enlaces.py`) |
| **Fecha apertura** | 2026-08-18 |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 🐛 **Defecto.** Es la deuda del `RN-03` de la historia.

**De dónde sale:** el [pendiente 18](../../../../../pendientes/18-los-enlaces-del-estandar-no-cumplen-doc14.md). Su punto 2 dice *«corregirlos: es mecánico — el validador ya dice, enlace por enlace, qué texto debería tener»*. Faltaba escribirlo.

**CA que cubre:** el `RN-03` —`13·DOC14` palabra por palabra— en su parte reparable.

---

## 1. Objetivo y alcance

**Objetivo:** que el arreglo lo haga el programa, no la mano. El validador ya calculaba el texto correcto de cada enlace; lo que faltaba era escribirlo de vuelta.

**Corregir mil enlaces a mano es como se cometen los errores que este arreglo viene a quitar.**

**Fuera de alcance, y cada exclusión declarada:**

| Qué | Por qué |
|---|---|
| Las transcripciones de `historico-chat/` | Se copian literales del chat |
| `prompts/` | Son palabras del usuario: reescribirle un enlace ahí es editarle la frase |
| **El vecino de la misma carpeta** | Ver §2.6 — es lo que esta fase descubrió, y necesita una decisión |
| El enlace de texto descriptivo | La propia regla lo permite |

---

## 2. Análisis previo — línea base verificada

**Medido el 2026-08-18.** El pendiente contaba **354** el 2026-08-14; hoy son **1031**, y el crecimiento es de los documentos de fase escritos desde entonces.

| | Cuántos |
|---|---:|
| Total fuera de transcripciones y de `prompts/` | **1031** |
| De los cuales, **vecino de la misma carpeta** | **747** |
| **Entre carpetas** — lo que esta fase arregla | **284** |

### 2.1 Archivos que se crean o modifican

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/enlaces.py` | Modificar | `reparar_formato`, `_texto_esperado`, `_es_vecino`, `_es_del_usuario` |
| `validadores/tests/test_el_texto_del_enlace_dice_donde_vive.py` | Nuevo | Los casos |
| 89 `.md` del repositorio | Modificar | Solo el **texto** de 284 enlaces |
| `pendientes/18-…md` | Modificar | Lo medido y la decisión que falta |

**No se toca `base/` ni `plantillas/`:** no hay versión que subir. La regla no cambia — lo que cambia es que ahora se puede cumplir sin escribirla a mano.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **El destino no se toca nunca** | Normalizarlo también | Ya funciona, y tocarlo es la única forma de romper un enlace que hoy anda |
| **El que reporta y el que arregla comparten el criterio** (`_texto_esperado`) | Dos funciones parecidas | Si miran distinto, el arreglo deja hallazgos vivos o toca lo que nadie reportó. Hay dos casos que lo fijan |
| **El vecino de la misma carpeta se deja fuera** | Aplicar la regla literal | Se aplicó y se revirtió: ver abajo |
| `prompts/` se excluye por nombre, no por criterio | Repararlos también | Son palabras del usuario |

**El vecino se probó y se revirtió, y conviene decir qué se vio.** `DOC14` pide la ruta desde la raíz *«para saber dónde vive sin abrirlo»*. Para el archivo de al lado ese propósito **ya está cumplido**: quien lee está parado ahí. Aplicándolo igual, la tabla de contenidos de una fase quedaba así:

```
| [documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/E-EP-001-HU-009-las-que-solo-sobraban-de-largo/plan_trabajo.md](plan_trabajo.md) | Qué se va a hacer |
```

**132 caracteres de media para nombrar al vecino.** Se revirtieron los 347 archivos y se dejó el caso aparte: **si la regla distingue al vecino es un cambio de la regla, y eso lo decide el usuario.**

### 2.7 Dudas por resolver antes de escribir

**Una, y es la que queda abierta:** si `DOC14` exceptúa al vecino de la misma carpeta. Se resolvió **no** decidirla acá.

---

## 3. Desglose de tareas

| ID | Tarea | Est. |
|---|---|:--:|
| T-01 | Medir cuántos son hoy y de qué tipo | 0,25 h |
| T-02 | `reparar_formato`, compartiendo criterio con el validador | 0,75 h |
| T-03 | Los casos | 0,75 h |
| T-04 | Aplicar, y comprobar que ningún enlace se rompió | 0,25 h |
| T-05 | Anotar en el 18 lo medido y la decisión que falta | 0,25 h |

**Total estimado:** 2,25 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-04.

**T-03 va antes que T-04**, y los casos encontraron dos defectos reales antes de tocar el repositorio: la exclusión de `prompts/` se contaba contra la raíz equivocada, y el texto entre comillas invertidas nunca se veía.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación

| CA | Método | Estado |
|---|---|---|
| `RN-03` · el texto dice la ruta desde la raíz | Los 284 entre carpetas, en cero | ☑ |
| Ningún enlace se rompe | `validar.py estandar` | ☑ |
| Las exclusiones son declaradas, no olvidos | Un caso por cada una | ☑ |
| No regresión | Las dos suites | ☑ |

---

## 6. Datos y ambiente de prueba

Repositorios de mentira en carpetas temporales, más una prueba sobre el repositorio real que exige **cero entre carpetas** — no cero total, porque los vecinos esperan la decisión.

---

## 7. Reversión / rollback

Se revierte volviendo el commit atrás. Ya se hizo una vez en esta misma fase, y salió limpio.

---

## 8. Producción y migración incremental

**Aditiva.** La regla no cambia; lo que llega es la herramienta que la hace cumplible.

---

## 9. Reglas del estándar aplicadas

[`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md), [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), [`13·DOC14`](../../../../../base/13-documentacion/reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Acción | Estado |
|---|---|---|---|
| B-01 | Romper un enlace que hoy funciona | El destino no se toca. `validar.py estandar` lo confirma | **Cerrado** |
| B-02 | Reescribir palabras del usuario | `prompts/` excluido, con caso | **Cerrado** |
| B-03 | Que el arreglo y el reporte se separen | Comparten `_texto_esperado`, con dos casos | **Cerrado** |
| B-04 | Que aplicar la regla literal empeore la lectura | **Pasó.** Se revirtió y se dejó aparte el caso del vecino | **Cerrado, con decisión pendiente** |
| B-05 | El texto entre comillas invertidas no se ve | Es de `comun.enlaces()` y toca a todo el repositorio. **Queda declarado en un caso**, no arreglado acá | Abierto |

---

## 11. Definition of Done

- [x] `reparar_formato` con sus casos
- [x] Los 284 entre carpetas, arreglados
- [x] Ningún enlace roto
- [x] Las exclusiones con caso propio
- [ ] Aceptada por el usuario
- [ ] **Falta la decisión:** si `DOC14` exceptúa al vecino de la misma carpeta

---

## 13. Cierre

**No se escribe acá.** Vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
