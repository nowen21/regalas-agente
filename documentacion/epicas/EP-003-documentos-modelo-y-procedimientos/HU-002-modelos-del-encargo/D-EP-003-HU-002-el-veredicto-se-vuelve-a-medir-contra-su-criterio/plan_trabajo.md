# Plan de Trabajo — Fase `D-EP-003-HU-002-el-veredicto-se-vuelve-a-medir-contra-su-criterio` (módulo Documentos modelo)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `D-EP-003-HU-002-el-veredicto-se-vuelve-a-medir-contra-su-criterio` |
| **Épica** | [EP-003](../../epica.md) |
| **HU** | [HU-002](../HU-002-modelos-del-encargo.md) — **una sola** (`F12.1`) |
| **Módulo** | Documentos modelo |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Fecha apertura** | 2026-08-27 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):
- 📝 **Corrige un veredicto que midió otra cosa.** La fase [`A`](../A-EP-003-HU-002-retrodocumentar-los-modelos-del-encargo/resultado_pruebas.md) cerró con «No cumple» el 2026-08-17 porque *«el planteamiento de esta casa está vacío»*. **Su `CA-01` no pide eso**: pide que existan los tres modelos y que la cadena se recorra en los dos sentidos. Está en `S-063`.

**La diferencia con el otro rojo revisado el mismo día:** aquel —`EP-005·HU-001`— **fue cierto** y dejó de serlo. Este **nunca lo fue**.

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** volver a medir el `CA-01` **contra lo que está escrito en el criterio**, y declarar el veredicto que salga.

**Fuera de alcance:**

- **Tocar la fase `A`.** Su veredicto queda como está: reescribirlo borraría el rastro de que el error existió, y **el error enseña más que la conclusión**.
- **Descartar su hallazgo.** Que la casa no tuviera su planteamiento **era cierto y valía**. Lo que se corrige es **dónde se cobra**, no que se haya encontrado.
- **Los otros criterios de la historia.** La fase `A` los dio por cumplidos y no se reabren.

---

## 2. Análisis previo — línea base verificada  ·  `02·F17`

> **Medido antes de crear la carpeta de esta fase**, porque abrirla mueve el número.

### 2.0 La línea base

```
119 en total · 32 sin terminar · 87 terminadas,
de las cuales 66 cumplen, 16 no cumplen y 5 no dicen si cumplen
```

### 2.1 Qué pide el criterio, palabra por palabra

> *«Dado que se va a documentar un encargo, cuando se buscan los modelos, entonces **existen el de la necesidad, el de la épica y el de la historia**, y cada uno tiene dónde nombrar al de arriba y a los de abajo.»*
>
> **Aprobado cuando:** *«la cadena se puede recorrer de arriba abajo y de abajo arriba».*

**No dice nada del planteamiento de este repositorio.** Dice que **el modelo** exista.

### 2.2 Qué encontró la propia fase `A`

| Lo que midió | Resultado |
|---|---|
| Los tres modelos existen | **Sí** |
| El encadenamiento en los dos sentidos | **Sí** |
| Fallas de trazabilidad en 68 historias | **Ninguna** |
| El modelo del planteamiento existe | **Sí**, y lo dice con su ruta |
| El planteamiento **de esta casa**, lleno | **No** — y por esto se puso «No cumple» |

**La fase midió su criterio, le dio verde, y se reprobó por otra cosa.**

### 2.3 Cómo se cuela, que es lo que hay que dejar escrito

El criterio dice *«existen los tres modelos»*, y el del planteamiento existía. Lo que faltaba era **el documento que ese modelo produce en este repositorio**.

**Son dos cosas: el molde, y lo que se llena con él.** La fase encontró un hueco real —la casa no tenía su planteamiento, y lo anotó bien, con su pendiente— **y lo cobró en la factura equivocada**.

### 2.4 Y el hueco que sí encontró, hoy

| Qué | Estado |
|---|---|
| El pendiente que abrió | **Cerrado** el 2026-08-22 |
| El planteamiento de esta casa | **Escrito**, en `prompts/cimiento-planteamiento.md` |

**Así que ni siquiera queda pendiente lo que la fase señaló.** Se comprueba en esta fase en vez de darlo por hecho.

### 2.4.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| Los cinco documentos de esta fase | Crear | Documentación | El cierre declara el veredicto |

**No se toca código, ni la historia, ni la fase `A`.**

### 2.5 Matriz de dependencias

**Ninguna.** Esta fase no cambia contrato de nada.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Una fase que **vuelve a medir**, sin tocar la `A` | Corregir el veredicto de la `A` | El error importa más que la conclusión que traía. Es lo que se hizo con `H-34` el 2026-08-26 |
| **El hallazgo se conserva**, y se dice dónde debía cobrarse | Borrarlo por estar mal ubicado | Era cierto y valía. Lo mal puesto era la factura |
| Se recorre la cadena **de verdad**, no se cita a la fase `A` | Copiar su medición | Una fase que se apoya en la medición de otra hereda su error. Y hoy mismo se afirmó tres veces sobre lo que no se ejecutó |

### 2.7 Dudas por resolver antes de codificar

| # | Duda | Estado |
|---|---|---|
| — | Ninguna. El criterio se leyó completo, incluida su línea de «aprobado cuando» | — |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Comprobar que los tres modelos existen | Calidad | 0,5 h | — | EV-01 |
| T-02 | Recorrer la cadena hacia abajo y hacia arriba, **corriéndola** | Calidad | 0,5 h | T-01 | EV-02 |
| T-03 | Comprobar que el hueco que la `A` señaló ya no existe | Calidad | 0,5 h | — | EV-03 |
| T-04 | Declarar el veredicto, y dónde debía cobrarse el hallazgo | Documentación | 1 h | T-01 a T-03 | EV-04 |

**Total estimado:** 2,5 h

**Sin cambio de versión:** no se toca `base/` ni `plantillas/`. `20·M10` no lo alcanza.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-04

**La `T-02` se corre, no se cita.** Apoyarse en la medición de la fase `A` heredaría su error de raíz — y el punto de esta fase es **no** heredarlo.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 · los tres modelos existen y se encadenan | Buscarlos, y correr la comprobación de trazabilidad sobre el árbol real | EV-01, EV-02 | | ☐ |

---

## 6. Datos y ambiente de prueba

El árbol real del repositorio. **Ninguna prueba usa credenciales** (`00·N6`) y no se edita ningún documento para probar (`08·T4`).

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Nada que desplegar.** Lo que cambia es que la historia deja de arrastrar un rojo que su criterio no sostiene.

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `02·F17` — la línea base, medida antes de crear la carpeta.
- `04·R4` — se recorre la cadena en vez de citar a quien la recorrió.
- `13·DOC5` — lo decidido se registra como señal: `S-063`.
- `20·M11` — nada se borra: el veredicto de la `A` queda, y esta fase dice qué midió mal.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que se herede el error citando a la fase `A` | Se repetiría el defecto que se corrige | La `T-02` corre la comprobación | Abierto |
| B-02 | Que al «cerrar» el rojo se pierda el hallazgo que la `A` encontró | Se perdería algo cierto y útil | El cierre lo conserva y dice dónde debía cobrarse | Abierto |
| B-03 | Que la cadena **de verdad** falle hoy | La fase cerraría en rojo, y con razón | Se corre antes de escribir el veredicto | Abierto |
| B-04 | Que abrir esta fase mueva la medición | `S-053` | La línea base está anotada en el §2.0 | Abierto |

---

## 11. Definition of Done

- [ ] El criterio verificado **corriendo la comprobación**, no citando
- [ ] El hallazgo de la fase `A` conservado, con su destino corregido
- [ ] La suite completa en verde, con conteo distinto de cero
- [ ] Rama lista para el commit único
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
