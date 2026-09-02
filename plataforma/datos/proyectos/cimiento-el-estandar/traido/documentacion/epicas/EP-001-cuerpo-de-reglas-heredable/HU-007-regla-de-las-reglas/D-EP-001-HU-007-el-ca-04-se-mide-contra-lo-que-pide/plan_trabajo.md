# Plan de Trabajo — Fase `D-EP-001-HU-007-el-ca-04-se-mide-contra-lo-que-pide` (módulo Meta-reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `D-EP-001-HU-007-el-ca-04-se-mide-contra-lo-que-pide` |
| **Épica** | [EP-001](../../epica.md) |
| **HU** | [HU-007](../HU-007-regla-de-las-reglas.md) — **una sola** (`F12.1`) |
| **Módulo** | Meta-reglas |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Fecha apertura** | 2026-08-27 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):
- 📝 **Corrige un veredicto que midió otra cosa.** La fase [`A`](../A-EP-001-HU-007-retrodocumentar-el-procedimiento-de-la-regla/resultado_pruebas.md) cerró con «No cumple» por el `CA-04`, citando *«249 de 249 sin dato»*. **Su criterio no pide que las reglas estén revisadas.** Es `S-069`.

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** medir el `CA-04` **contra lo que su criterio pide**, y declarar el veredicto que salga.

**Fuera de alcance:**

- **Revisar reglas.** Cuando se haga, será trabajo normal y no deuda.
- **Tocar la fase `A`.** Su veredicto queda: el rastro del error vale más que la conclusión.
- **Los otros criterios de la historia.** La fase `A` los dio por cumplidos.

---

## 2. Análisis previo — línea base verificada  ·  `02·F17`

> **Medido antes de crear la carpeta de esta fase.**

### 2.0 La línea base

```
121 en total · 32 sin terminar · 89 terminadas,
de las cuales 70 cumplen, 14 no cumplen y 5 no dicen si cumplen
```

### 2.1 Qué pide el criterio, palabra por palabra

> *«Cuando se pregunta qué reglas llevan más tiempo sin revisarse de fondo, entonces se obtiene la **lista ordenada** de la más vieja a la más nueva, y cada una dice **cuándo se revisó** y **cuántos incumplimientos produce hoy**.»*

**No dice en ninguna parte que las reglas tengan que estar revisadas.** Dice que se sepa **cuáles llevan más sin revisarse**.

### 2.2 Y el procedimiento dice que la ausencia es deliberada

[`base/20-meta-reglas/revision-de-vigencia.md`](../../../../../base/20-meta-reglas/revision-de-vigencia.md), en una línea:

> *«Arranca ausente en todas las reglas, a propósito. Ponérsela de una vez a las doscientas habría sido escribir doscientas fechas que no responden por ninguna revisión: el sello vacío que este documento viene a evitar.»*

**Así que `251 de 251 sin fecha` no es una falta: es el diseño.** Tratarlo como deuda habría llevado a sellar 250 reglas sin revisarlas — exactamente lo que ese documento existe para impedir.

### 2.3 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| Los cinco documentos de esta fase | Crear | Documentación | El cierre declara el veredicto |

**No se toca código, ni la historia, ni la fase `A`.**

### 2.4 Punto de entrada

`python validadores/vigencia.py`. Ninguno nuevo.

### 2.5 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Se **corre** `vigencia.py`, no se cita a la fase `A` | Copiar su medición | Una fase que hereda la medición de otra hereda su error |
| El veredicto de la `A` **no se toca** | Corregirlo | `20·M11`, y el error enseña más que la conclusión |
| **El hallazgo de la `A` se conserva** | Descartarlo | Que nadie hubiera revisado ninguna regla era cierto. Lo mal puesto era la factura |
| Esta fase **declara el reemplazo** del veredicto | Dejar el rojo | Es para lo que se construyó la `HU-023` el mismo día |

### 2.6 Dudas por resolver antes de codificar

| # | Duda | Estado |
|---|---|---|
| — | Ninguna. El criterio y el procedimiento se leyeron completos | — |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Correr `vigencia.py` y comprobar que da una lista | Calidad | 0,5 h | — | EV-01 |
| T-02 | Comprobar que dice **cuándo** y **cuántos incumplimientos** | Calidad | 0,5 h | T-01 | EV-01 |
| T-03 | Comprobar que está **ordenada** de la más vieja a la más nueva | Calidad | 0,5 h | T-01 | EV-02 |
| T-04 | Comprobar que **avisa y no corrige** | Calidad | 0,5 h | T-01 | EV-03 |
| T-05 | Declarar el veredicto y el reemplazo | Documentación | 1 h | T-01 a T-04 | EV-04 |

**Total estimado:** 3 h

**Sin cambio de versión:** no se toca `base/` ni `plantillas/`.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-03 → T-05

**La `T-03` es la que puede fallar de verdad.** Que la lista exista es fácil de ver; **que esté ordenada** es lo que el criterio exige y lo que nadie mira.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-04 · se sabe qué reglas llevan más sin revisarse | Correr la comprobación y mirar sus tres exigencias | EV-01, EV-02 | | ☐ |

---

## 6. Datos y ambiente de prueba

El árbol real. **Ninguna prueba usa credenciales** (`00·N6`) y no se edita ningún documento para probar (`08·T4`).

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Nada que desplegar.** Lo que cambia es que la historia deja de arrastrar un rojo que su criterio no sostiene.

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `02·F17` — la línea base, medida antes de crear la carpeta.
- `04·R4` — se corre en vez de citar a quien corrió.
- `20·M11` — nada se borra ni se reescribe.
- `13·DOC5` — lo decidido se registra como señal: `S-069`.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que se herede el error citando a la fase `A` | Se repetiría lo que se corrige | La `T-01` corre la comprobación | Abierto |
| B-02 | Que la lista **no esté ordenada** de verdad | La fase cerraría en rojo, con razón | `T-03`, comprobando la secuencia | Abierto |
| B-03 | Que se lea como «ya no hay que revisar reglas» | Revisar sigue siendo trabajo útil, y el cierre lo dice | Abierto |

---

## 11. Definition of Done

- [ ] El criterio verificado **corriendo la comprobación**
- [ ] El hallazgo de la fase `A` conservado, con su destino corregido
- [ ] La suite completa en verde
- [ ] Rama lista para el commit único
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
