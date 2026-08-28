# -*- coding: utf-8 -*-
"""Escribe los cinco documentos de la fase D de EP-001-HU-007.

La fase A cerro con «No cumple» por el CA-04, citando «249 de 249 sin dato».
Su criterio no pide que las reglas esten revisadas: pide que se sepa cuales
llevan mas sin revisarse. Y el procedimiento dice que la ausencia de fechas es
deliberada.
"""
import io
import os

RAIZ = r"c:\Ing. Jose\ia\agente"
D = os.path.join(RAIZ, "documentacion", "epicas",
                 "EP-001-cuerpo-de-reglas-heredable",
                 "HU-007-regla-de-las-reglas",
                 "D-EP-001-HU-007-el-ca-04-se-mide-contra-lo-que-pide")


def escribir(nombre, texto):
    with io.open(os.path.join(D, nombre), "w", encoding="utf-8",
                 newline="\n") as f:
        f.write(texto)


escribir("plan_trabajo.md", u"""# Plan de Trabajo \u2014 Fase `D-EP-001-HU-007-el-ca-04-se-mide-contra-lo-que-pide` (m\u00f3dulo Meta-reglas)   \u00b7   `[CAPA 3]`

**Para qu\u00e9 sirve este documento.** Dice **qu\u00e9 se va a hacer en esta fase, en qu\u00e9 orden, sobre qu\u00e9 archivos y c\u00f3mo se comprueba** cada criterio de aceptaci\u00f3n antes de darlo por cumplido.

---

## 0. Identificaci\u00f3n y origen  \u00b7  `02\u00b7F14` Q1-Q2 \u00b7 `13\u00b7DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador \u00b7 `02\u00b7F12.6`) | `D-EP-001-HU-007-el-ca-04-se-mide-contra-lo-que-pide` |
| **\u00c9pica** | [EP-001](../../epica.md) |
| **HU** | [HU-007](../HU-007-regla-de-las-reglas.md) \u2014 **una sola** (`F12.1`) |
| **M\u00f3dulo** | Meta-reglas |
| **Especificaci\u00f3n del m\u00f3dulo** | No hay documento aparte. `02\u00b7F19` |
| **Fecha apertura** | 2026-08-27 |
| **Rama** | `main` |

**ORIGEN** (`13\u00b7DOC12`):
- \U0001F4DD **Corrige un veredicto que midi\u00f3 otra cosa.** La fase [`A`](../A-EP-001-HU-007-retrodocumentar-el-procedimiento-de-la-regla/resultado_pruebas.md) cerr\u00f3 con \u00abNo cumple\u00bb por el `CA-04`, citando *\u00ab249 de 249 sin dato\u00bb*. **Su criterio no pide que las reglas est\u00e9n revisadas.** Es `S-069`.

---

## 1. Objetivo y alcance  \u00b7  `02\u00b7F14` Q4

**Objetivo:** medir el `CA-04` **contra lo que su criterio pide**, y declarar el veredicto que salga.

**Fuera de alcance:**

- **Revisar reglas.** Cuando se haga, ser\u00e1 trabajo normal y no deuda.
- **Tocar la fase `A`.** Su veredicto queda: el rastro del error vale m\u00e1s que la conclusi\u00f3n.
- **Los otros criterios de la historia.** La fase `A` los dio por cumplidos.

---

## 2. An\u00e1lisis previo \u2014 l\u00ednea base verificada  \u00b7  `02\u00b7F17`

> **Medido antes de crear la carpeta de esta fase.**

### 2.0 La l\u00ednea base

```
121 en total \u00b7 32 sin terminar \u00b7 89 terminadas,
de las cuales 70 cumplen, 14 no cumplen y 5 no dicen si cumplen
```

### 2.1 Qu\u00e9 pide el criterio, palabra por palabra

> *\u00abCuando se pregunta qu\u00e9 reglas llevan m\u00e1s tiempo sin revisarse de fondo, entonces se obtiene la **lista ordenada** de la m\u00e1s vieja a la m\u00e1s nueva, y cada una dice **cu\u00e1ndo se revis\u00f3** y **cu\u00e1ntos incumplimientos produce hoy**.\u00bb*

**No dice en ninguna parte que las reglas tengan que estar revisadas.** Dice que se sepa **cu\u00e1les llevan m\u00e1s sin revisarse**.

### 2.2 Y el procedimiento dice que la ausencia es deliberada

[`base/20-meta-reglas/revision-de-vigencia.md`](../../../../../base/20-meta-reglas/revision-de-vigencia.md), en una l\u00ednea:

> *\u00abArranca ausente en todas las reglas, a prop\u00f3sito. Pon\u00e9rsela de una vez a las doscientas habr\u00eda sido escribir doscientas fechas que no responden por ninguna revisi\u00f3n: el sello vac\u00edo que este documento viene a evitar.\u00bb*

**As\u00ed que `251 de 251 sin fecha` no es una falta: es el dise\u00f1o.** Tratarlo como deuda habr\u00eda llevado a sellar 250 reglas sin revisarlas \u2014 exactamente lo que ese documento existe para impedir.

### 2.3 Archivos que se crean o modifican  \u00b7  `02\u00b7F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| Los cinco documentos de esta fase | Crear | Documentaci\u00f3n | El cierre declara el veredicto |

**No se toca c\u00f3digo, ni la historia, ni la fase `A`.**

### 2.4 Punto de entrada

`python validadores/vigencia.py`. Ninguno nuevo.

### 2.5 Decisiones t\u00e9cnicas

| Decisi\u00f3n | Alternativa descartada | Justificaci\u00f3n |
|---|---|---|
| Se **corre** `vigencia.py`, no se cita a la fase `A` | Copiar su medici\u00f3n | Una fase que hereda la medici\u00f3n de otra hereda su error |
| El veredicto de la `A` **no se toca** | Corregirlo | `20\u00b7M11`, y el error ense\u00f1a m\u00e1s que la conclusi\u00f3n |
| **El hallazgo de la `A` se conserva** | Descartarlo | Que nadie hubiera revisado ninguna regla era cierto. Lo mal puesto era la factura |
| Esta fase **declara el reemplazo** del veredicto | Dejar el rojo | Es para lo que se construy\u00f3 la `HU-023` el mismo d\u00eda |

### 2.6 Dudas por resolver antes de codificar

| # | Duda | Estado |
|---|---|---|
| \u2014 | Ninguna. El criterio y el procedimiento se leyeron completos | \u2014 |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Correr `vigencia.py` y comprobar que da una lista | Calidad | 0,5 h | \u2014 | EV-01 |
| T-02 | Comprobar que dice **cu\u00e1ndo** y **cu\u00e1ntos incumplimientos** | Calidad | 0,5 h | T-01 | EV-01 |
| T-03 | Comprobar que est\u00e1 **ordenada** de la m\u00e1s vieja a la m\u00e1s nueva | Calidad | 0,5 h | T-01 | EV-02 |
| T-04 | Comprobar que **avisa y no corrige** | Calidad | 0,5 h | T-01 | EV-03 |
| T-05 | Declarar el veredicto y el reemplazo | Documentaci\u00f3n | 1 h | T-01 a T-04 | EV-04 |

**Total estimado:** 3 h

**Sin cambio de versi\u00f3n:** no se toca `base/` ni `plantillas/`.

---

## 4. Secuencia de ejecuci\u00f3n

**Ruta cr\u00edtica:** T-01 \u2192 T-03 \u2192 T-05

**La `T-03` es la que puede fallar de verdad.** Que la lista exista es f\u00e1cil de ver; **que est\u00e9 ordenada** es lo que el criterio exige y lo que nadie mira.

> Solo se tocan los archivos declarados (`02\u00b7F8`).

---

## 5. Verificaci\u00f3n de criterios de aceptaci\u00f3n  \u00b7  `02\u00b7F14` Q10

| CA | M\u00e9todo | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-04 \u00b7 se sabe qu\u00e9 reglas llevan m\u00e1s sin revisarse | Correr la comprobaci\u00f3n y mirar sus tres exigencias | EV-01, EV-02 | | \u2610 |

---

## 6. Datos y ambiente de prueba

El \u00e1rbol real. **Ninguna prueba usa credenciales** (`00\u00b7N6`) y no se edita ning\u00fan documento para probar (`08\u00b7T4`).

---

## 7. Reversi\u00f3n / rollback  \u00b7  `02\u00b7F14` Q11

Se revierte descartando el commit.

---

## 8. Producci\u00f3n y migraci\u00f3n incremental  \u00b7  `02\u00b7F14` Q12

**Nada que desplegar.** Lo que cambia es que la historia deja de arrastrar un rojo que su criterio no sostiene.

---

## 9. Reglas del est\u00e1ndar aplicadas  \u00b7  `02\u00b7F14` Q13

- `02\u00b7F17` \u2014 la l\u00ednea base, medida antes de crear la carpeta.
- `04\u00b7R4` \u2014 se corre en vez de citar a quien corri\u00f3.
- `20\u00b7M11` \u2014 nada se borra ni se reescribe.
- `13\u00b7DOC5` \u2014 lo decidido se registra como se\u00f1al: `S-069`.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acci\u00f3n | Estado |
|---|---|---|---|---|
| B-01 | Que se herede el error citando a la fase `A` | Se repetir\u00eda lo que se corrige | La `T-01` corre la comprobaci\u00f3n | Abierto |
| B-02 | Que la lista **no est\u00e9 ordenada** de verdad | La fase cerrar\u00eda en rojo, con raz\u00f3n | `T-03`, comprobando la secuencia | Abierto |
| B-03 | Que se lea como \u00abya no hay que revisar reglas\u00bb | Revisar sigue siendo trabajo \u00fatil, y el cierre lo dice | Abierto |

---

## 11. Definition of Done

- [ ] El criterio verificado **corriendo la comprobaci\u00f3n**
- [ ] El hallazgo de la fase `A` conservado, con su destino corregido
- [ ] La suite completa en verde
- [ ] Rama lista para el commit \u00fanico
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) \u00a71.2.

---

## 13. Cierre

**No se escribe ac\u00e1.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
""")
print("plan_trabajo escrito")
