# Resultado de Pruebas — Fase `D-EP-003-HU-002-el-veredicto-se-vuelve-a-medir-contra-su-criterio`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `D-EP-003-HU-002-el-veredicto-se-vuelve-a-medir-contra-su-criterio` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-27 |
| **Ciclo** | 2. **El primero activó el criterio de suspensión** |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** el `CA-01` se midió **contra lo que su criterio pide** y quedó verde en sus dos mitades: los tres modelos existen y se encadenan, y la cadena se recorre en los dos sentidos **sin una sola falla sobre 11 épicas y 119 historias**.

**Y el hallazgo de la fase `A` se conserva:** que la casa no tuviera su planteamiento era cierto y valía. Lo que estaba mal era **dónde se cobraba**.

| Métrica | Meta | Real |
|---|---|---|
| Casos ejecutados | 3 de 3 | 3 de 3 |
| **Mediciones heredadas de la fase `A`** | 0 | **0** |
| Fallas de enlace bidireccional | 0, y dicho sobre cuántas | **0**, sobre 11 épicas y 119 historias |

---

## 3. Resultado por caso

### CP-001 — Los tres modelos existen

| Modelo | Archivo | Está |
|---|---|---|
| La necesidad | `01-planteamiento.md` | Sí |
| La épica | `03-epica.md` | Sí |
| La historia | `04-HU.md` | Sí |

El molde de la historia **nombra su épica**; el de la épica **lista sus historias**.

### CP-002 — La cadena se recorre en los dos sentidos

**Corrida sobre el árbol real, no citada.**

| Medición | Valor |
|---|---|
| Épicas | **11** |
| Historias | **119** |
| Fallas de enlace bidireccional | **0** |

**Ciclo 1: no era cero.** Está en el §4.1.

### CP-003 — El hueco que la fase `A` señaló

| Qué se comprobó | Resultado |
|---|---|
| El planteamiento de esta casa existe | **Sí** — `prompts/cimiento-planteamiento.md` |
| No es el molde en blanco | 120 líneas, **1 marcador** |
| El pendiente que la fase `A` citó | **Cerrado**, en `pendientes/hecho/` |

**No es parte del `CA-01`, y por eso se comprueba aparte.** El hallazgo de la fase `A` valía; lo que se corrige es dónde se cobraba, no que se hubiera encontrado. Y hoy **ni siquiera queda abierto**.

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 El criterio de suspensión se activó, y encontró algo que no se buscaba

El plan decía: *«se suspende si la cadena falla hoy»*. **Falló**: una historia no estaba en la tabla de su épica.

```
EP-001 — la épica no lista la HU-036 que cuelga de ella (DOC16)
```

**Y no era la única.** El mismo día habían aparecido `HU-017` y `HU-018` sin su fila en `EP-005`, encontradas por casualidad al agregar otra. **Tres en una jornada.**

**Se paró, se reportó, y el usuario amplió el alcance** para arreglar la fila en vez de dejarla anotada: *«¿para qué dejar pendientes si se puede solucionar?»*. Con eso la cadena quedó en **cero**, y el `CA-01` se pudo medir.

**Archivo tocado que el plan no declaraba** (`02·F8`): `documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/epica.md`, **una fila**, con la autorización del usuario y dicho acá.

### 4.2 Lo que destapó el hallazgo, y por qué no fue casualidad

**Lo encontró una regla del plan**, no la suerte: *«se corre, no se cita»*. Apoyarse en la medición de la fase `A` habría heredado su resultado de hace diez días —cuando la cadena sí estaba limpia— y **la falla de hoy habría pasado invisible**.

**Una medición vieja no es una medición.** Está en `S-064`.

### 4.3 Por qué la fase `A` se equivocó, dicho sin adornos

Su `CA-01` pide que **existan los tres modelos** y que la cadena se recorra en los dos sentidos. Su línea de aprobación dice: *«la cadena se puede recorrer de arriba abajo y de abajo arriba»*.

**La propia fase `A` midió eso y le dio verde** — escribió que los tres existen y que no había una sola falla en 68 historias. Y aun así se puso «No cumple», porque *«el planteamiento de esta casa está vacío»*.

**Cómo se coló:** el criterio dice «existen los tres modelos», y el del planteamiento existía. Lo que faltaba era **el documento que ese modelo produce en este repositorio**. Son dos cosas — **el molde, y lo que se llena con él**.

**Lo que la fase `A` hizo bien:** encontró el hueco, lo describió, y le abrió su pendiente. **Lo único mal puesto fue la factura.**

### 4.4 El veredicto de la fase `A` no se toca

Queda como está (`20·M11`). Reescribirlo borraría el rastro de que el error existió, **y el error enseña más que la conclusión** — es lo mismo que se decidió con `H-34` el 2026-08-26.

### 4.5 Rastros

Ninguno. No se editó ningún documento para probar (`08·T4`).

### 4.6 Ninguna prueba usa credenciales

Ni reales ni inventadas (`00·N6`).

---

## 5. Defectos encontrados

| # | Qué | Severidad | Estado |
|---|---|---|---|
| DEF-01 | `HU-036` no estaba en la tabla de `EP-001`: la cadena no se recorría de arriba abajo | Alta | **Corregido**, con el alcance ampliado por el usuario |

**No es de esta fase ni de la `A`:** es el patrón de `S-064` — una historia se crea, se le hace su carpeta, y nadie vuelve a la tabla de su épica.

---

## 6. Evidencias

- El guion que volvió a medir, en [historico-chat/scripts/2026-08-27/](../../../../../historico-chat/scripts/2026-08-27/)
- `validar.py trazabilidad` sobre el árbol real: **0 fallas** de enlace bidireccional
- El `CA-01` transcrito palabra por palabra en el §2.1 del [plan de trabajo](plan_trabajo.md)
