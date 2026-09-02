# Plan de Trabajo — Fase `A-EP-001-HU-037-la-norma-sube-al-cuerpo-de-reglas` (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-001-HU-037-la-norma-sube-al-cuerpo-de-reglas` |
| **Épica** | [EP-001](../../epica.md) |
| **HU** | [HU-037](../HU-037-la-norma-de-redaccion-del-agente.md), **una sola** (`F12.1`) |
| **Módulo** | Cuerpo de reglas |
| **Fecha apertura** | 2026-08-30 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- **La exigencia existía y no estaba en ninguna regla.** El usuario pidió que un documento se redactara en español colombiano, en tercera persona y en infinitivo, y no hubo regla que citar: vivía dentro del cuerpo de dos documentos modelo, como su regla número once. Sale del [pendiente 93](../../../../../pendientes/93-la-norma-de-redaccion-vive-dentro-de-dos-plantillas.md).

**El anexo de marcas ya declaraba el hueco**: la norma del idioma «necesita su propia regla, y todavía no existe».

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que la norma viva donde rige, y que los modelos la citen en vez de repetirla.

**Fuera de alcance:**

- **La ortografía y la gramática.** El anexo las nombra como pendientes suyas y son otra regla: una cosa es cómo se conjuga y otra si el texto está bien escrito.
- El texto que ve el usuario final de un producto, que ya tiene su regla.
- **Construir la comprobación.** Se dice qué mitad es contable y cuál pide leer; no se escribe el programa acá.

---

## 2. Análisis previo, línea base verificada  ·  `02·F17`

> Medida antes de crear la carpeta de esta fase.

### 2.0 La línea base

```
121 cumplen, 0 no cumplen, 0 sin veredicto · versión 36.0.3
```

### 2.1 Dónde vivía la norma, y por qué eso no alcanza

Estaba escrita como la regla once de dos modelos: el de manual de usuario y el de manual de instalación. **Solo la hereda quien llene uno de esos dos documentos.** Todo lo demás que el agente entrega quedaba sin ella, y la convención se aplicaba copiándola a mano de una plantilla.

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `base/00-identidad-y-rol/reglas/ID10-…md` | Crear | Estándar | La regla, con su checklist |
| `base/00-identidad-y-rol/base.md` | Modificar | Estándar | Su fila en el índice del capítulo |
| `validadores/reglas-validables.md` | Modificar | Estándar | Qué mitad se comprueba y cuál no |
| `plantillas/manual-instalacion.md` | Modificar | Estándar | Que cite la regla en vez de repetirla |
| `CHANGELOG.md` y `VERSION` | Modificar | Estándar | `37.0.0`, mayor |
| Los cinco documentos de esta fase | Crear | Documentación | — |
| `HU-037-la-norma-de-redaccion-del-agente.md` | Modificar | Documentación | Su `Estado` y su tabla de fases |

**`plantillas/manual-usuario.md` no se toca**, y se declara: tiene cambios sin guardar de otra sesión, y editarlo sería llevarse trabajo ajeno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Va en el capítulo de identidad y rol | En el de documentación | Ahí ya viven las dos reglas de cómo escribe el agente, y esta es la tercera |
| **Rige también lo que contesta en el chat** | Solo los documentos | Lo decidió el usuario. La respuesta del chat es lo que más se lee y lo único que no queda versionado: es donde la convención se pierde primero |
| No fija un idioma | Escribir «español colombiano» | Un proyecto en otro idioma tiene que poder cumplirla; lo que se fija es la variedad **del proyecto** |
| El impersonal con «se» se nombra aparte | Dejarlo implícito en «tercera persona» | Es la forma en que la regla se incumple sin darse cuenta |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Decidir el alcance con el usuario | Análisis | — | — | EV-01 |
| T-02 | Escribir la regla con su checklist | Estándar | 1 h | T-01 | EV-02 |
| T-03 | Clasificarla, diciendo qué mitad no se comprueba | Estándar | 0,5 h | T-02 | EV-02 |
| T-04 | Que los modelos la citen en vez de repetirla | Estándar | 0,5 h | T-02 | EV-03 |

**Total estimado:** 2 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 a T-02 a T-03, con la T-04 después.

La `T-01` no la hace el agente: es la decisión que tuvo la historia detenida, y sin ella el texto de la regla no se puede escribir.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| CA-01 · la regla existe, con su checklist | `validar.py metareglas` | CP-001 | ☑ |
| CA-02 · los modelos la citan | Buscar el texto repetido en los dos | CP-003 | ☑ a medias |
| CA-03 · dice el idioma del proyecto, no uno fijo | Leer el cuerpo | CP-002 | ☑ |

---

## 6. Datos y ambiente de prueba

El propio repositorio.

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit. La regla no se deroga: nunca llegó a regir.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Obliga a migrar.** Un proyecto al día tiene que escribir así de aquí en adelante. Los documentos ya escritos no se reabren.

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `20·M5`, el formato canónico de la regla, con una sola exigencia y su ejemplo.
- `20·M9`, se decide si es comprobable, y se dice qué mitad no lo es.
- `20·M10`, todo cambio de regla se versiona y se registra.
- `20·M12`, se buscó antes de crear: la exigencia estaba, la regla no.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Fijar un idioma y volverla inservible fuera de acá | El estándar dejaría de ser heredable | El `CA-03` lo comprueba | Cerrado |
| B-02 | Tocar el modelo de manual de usuario, que otra sesión tiene abierto | Es el caso de las 712 líneas | No se toca, y se declara | Abierto y declarado |

---

## 11. Definition of Done

- [x] La regla escrita, con su checklist
- [x] Clasificada en el registro de comprobables
- [x] Un modelo la cita; el otro queda declarado
- [ ] Autorizado el commit por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
