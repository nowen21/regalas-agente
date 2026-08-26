# HU-012 — Hacer cumplir lo que hoy solo se recuerda

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-012 |
| **Épica / Feature** | [EP-005 Automatismos que no dependen de la memoria](../epica.md) |
| **Módulo / Componente** | Automatismos — enganches |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | `shopnest-mesa`, que lo reportó |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Pendiente |
---

## 2. Narrativa

- **Como** quien escribió una regla de núcleo
- **Quiero** que la regla diga cómo se hace cumplir, o diga que no tiene forma de hacerse cumplir
- **Para** no confundir una regla que rige con una que solo está escrita

---

## 3. Contexto y descripción

[base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md](../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) es núcleo y no se relaja. **Nada la mide y nada la hace cumplir.** Depende por completo de que el agente se acuerde — que es literalmente lo que el estándar ya escribió sobre el histórico en [plantillas/historico-chat.md](../../../../plantillas/historico-chat.md):

> *una instrucción escrita **informa**, un enganche **ejecuta**.*

El histórico tiene su enganche. `ID9` no.

**La evidencia.** En `shopnest-mesa` el usuario pidió «menos es más» **siete veces en tres días**: una el 2026-08-15, cinco el 2026-08-16 y una el 2026-08-17. Cada vez se anotó el caso en un recuerdo del proyecto, con su porqué y su ejemplo. Anotarlo no cambió nada: el registro se volvió el sustituto de cumplir la regla, y a la séptima el usuario lo dijo así — *«¿de qué le sirve anotarlo tanto si no lo está cumpliendo?»*. Siete incumplimientos de una regla de núcleo, todos documentados, ninguno prevenido.

**El proyecto no lo puede arreglar.** Los enganches viven en `.claude/settings.json`, que lo escribe [validadores/instalar.py](../../../../validadores/instalar.py) y está en el `.gitignore` del proyecto. Lo que un proyecto agregue ahí lo pisa la siguiente instalación, que es idempotente y regenera esa configuración. El canal es del estándar, no del proyecto.

**El límite técnico, para que no se diseñe la pieza equivocada.** Un enganche de cierre no puede acortar una respuesta ya emitida: cuando corre, el texto ya salió. Lo único que puede hacer es medirlo y devolverlo para que se reescriba, y eso le cuesta al usuario ver la respuesta larga primero y la corta después.

**El caso general.** `ID9` es el caso que dolió, pero la historia no es sobre `ID9`: es sobre que una regla de núcleo pueda existir sin decir cómo se hace cumplir. Esa es la parte que sí es un defecto, y la que se arregla acá. Se cruza con el [pendientes/hecho/el-defecto-del-estandar-se-reporta-y-se-avisa-de-vuelta.md](../../../../pendientes/hecho/el-defecto-del-estandar-se-reporta-y-se-avisa-de-vuelta.md): las dos son reglas que existen en el papel y no tienen quién las ejecute.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Toda regla de núcleo declara cómo se hace cumplir: qué pieza la ejecuta, o que no tiene forma de ejecutarse |
| RN-02 | «No tiene forma de ejecutarse» es una declaración válida, y se escribe con su motivo |
| RN-03 | Una regla de núcleo sin ninguna de las dos declaraciones se reporta |
| RN-04 | El proyecto no puede agregar enganches por su cuenta: el canal es el instalador del estándar |
| RN-05 | Medir sin bloquear cuenta como forma de hacer cumplir, si la medición queda a la vista de quien revisa |

### 3.2 Supuestos

- El instalador sigue siendo el único que escribe la configuración de enganches del proyecto.

### 3.3 Fuera de alcance

- Decidir con cuál de las tres salidas se hace cumplir `ID9`. Es decisión del usuario y está planteada en su pendiente; esta historia exige que la decisión quede escrita, no cuál sea.
- Extender la exigencia a las reglas que no son de núcleo. Se hará si el caso se repite fuera del núcleo.

---

## 4. Criterios de aceptación

### CA-01 — Una regla de núcleo sin forma de cumplirse se reporta

```gherkin
Dado que una regla de núcleo no declara qué pieza la hace cumplir
Y tampoco declara que no tiene forma de hacerse cumplir
Cuando se corre la comprobación
Entonces se reporta esa regla con su identificador
Y la corrida termina con error
```

**Cómo validarlo:**

1. Correr la comprobación sobre el núcleo tal como está hoy. Resultado esperado: reporta `ID9`, que es el caso conocido.
2. Escribir en `ID9` cuál de las dos declaraciones aplica.
3. Volver a correr. Resultado esperado: ya no la reporta.
- **Aprobado cuando:** la regla sin declaración se reporta y la que la tiene no.

### CA-02 — «No se puede hacer cumplir» vale, pero con motivo

```gherkin
Dado que una regla declara que no tiene forma de hacerse cumplir
Cuando esa declaración trae su motivo escrito
Entonces la comprobación no la reporta
Pero cuando el motivo está vacío
Entonces sí la reporta
```

**Cómo validarlo:**

1. En una regla de prueba, declarar que no se puede hacer cumplir, con su motivo. Correr. Resultado esperado: no la reporta.
2. Borrar el motivo dejando la declaración sola. Correr. Resultado esperado: la reporta.
- **Aprobado cuando:** la declaración con motivo pasa y la declaración vacía no. Una casilla marcada sin motivo no es una decisión: es una casilla marcada.

### CA-03 — La pieza declarada existe

```gherkin
Dado que una regla declara qué pieza la hace cumplir
Cuando esa pieza no existe en el repositorio
Entonces la comprobación lo reporta y nombra la pieza que no resolvió
```

**Cómo validarlo:**

1. En una regla de prueba, declarar como pieza un archivo inventado. Correr. Resultado esperado: reporta que no existe.
2. Cambiarlo por un validador real. Correr. Resultado esperado: no reporta nada.
- **Aprobado cuando:** la pieza inventada se reporta y la real no.

### CA-04 — `ID9` queda con su decisión escrita

```gherkin
Dado que ID9 es el caso que originó esta historia
Cuando se lee la regla después del cambio
Entonces dice cuál de las tres salidas se tomó, o que no se puede hacer cumplir
```

**Cómo validarlo:**

1. Abrir `ID9` y buscar la declaración.
2. Resultado esperado: dice cuál se tomó, con su motivo.
3. Avisarle a `shopnest-mesa` para que cierre su pendiente 22.
- **Aprobado cuando:** la declaración está escrita y el aviso salió.

### Criterios de aceptación transversales

- [ ] **Límites** — una regla derogada, y una que declara dos piezas, tienen comportamiento definido.
- [ ] **No regresión** — las comprobaciones que ya corrían sobre el núcleo siguen dando lo mismo.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Claridad** | El mensaje dice qué falta declarar y dónde escribirlo, no solo que algo está mal |
| RNF-02 | **Determinismo** | El mismo cuerpo de reglas da el mismo resultado |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/epica.md](../epica.md).
- **Regla relacionada:** `20·M9`, que ya exige que toda regla declare si es validable. Esta es su hermana: declarar si es **ejecutable**, que no es lo mismo — una regla se puede comprobar después del hecho sin que nada la impida antes.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Fijar dónde se declara, en el molde de la regla.
- [ ] Comprobación que recorre el núcleo y reporta la regla sin declaración.
- [ ] Comprobar que la pieza declarada existe.
- [ ] Escribir la declaración de `ID9` con la decisión del usuario.
- [ ] Avisarle a `shopnest-mesa`.
- [ ] Versionar el cambio (`20·M10`).

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase (`02·F12.6`) | CA que cubre | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|
| — | — | — | — | — | Sin empezar |

**De dónde sale esta historia:** el [pendientes/hecho/nada-hace-cumplir-id9.md](../../../../pendientes/hecho/nada-hace-cumplir-id9.md), reportado por `shopnest-mesa`.

**Qué documento responde qué**, para no buscar en el que no es:

| Pregunta | Documento |
|---|---|
| Qué se pide y cuándo se da por aceptado | Esta HU |
| Qué se va a hacer, en qué orden y sobre qué archivos | `plan_trabajo.md` de la fase |
| Con qué casos se comprueba cada CA | `plan_pruebas.md` de la fase |
| Qué se ejecutó, con qué resultado, y si el CA quedó cumplido | `resultado_pruebas.md` de la fase |
| En qué estación va y qué la tiene detenida | `estado-fase.md` de la fase |
| Qué quedó hecho al final | `funcionalidad_implementada.md` de la fase |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Bloqueo | La decisión de cuál de las tres salidas aplica a `ID9`. Es del usuario y no la puede tomar el agente | Alto — detiene el CA-04, no los otros tres |
| Riesgo | Que se construya un enganche que devuelve la respuesta larga y el usuario termine viendo dos versiones de todo | El límite técnico está escrito en §3 para que la pieza no se diseñe a ciegas |
| Riesgo | Que la declaración se llene con «no se puede» en todas las reglas y la exigencia quede vacía | El CA-02 obliga al motivo, y el motivo lo lee una persona |

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas
- [ ] Decidida la salida para `ID9` (solo bloquea el CA-04)

## 11. Definition of Done (DoD)

- [ ] Los cuatro criterios de aceptación verificados
- [ ] `ID9` con su declaración escrita
- [ ] `shopnest-mesa` avisado, para que cierre su pendiente 22
- [ ] Versionada (`20·M10`)
- [ ] El pendiente 58 cerrado nombrando la fase

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | El CA-04 espera una decisión del usuario; los otros tres no |
| **N**egociable | Sí | Dónde se declara y cómo se llama el campo |
| **V**aliosa | Sí | Separa la regla que rige de la que solo está escrita |
| **E**stimable | Sí | El alcance lo fija el número de reglas de núcleo |
| **S**mall (pequeña) | Sí | Un campo y una comprobación |
| **T**esteable | Sí | Se cuenta cuántas reglas de núcleo quedan sin declaración |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-17 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU, para que el pendiente 58 deje de estar suelto |
