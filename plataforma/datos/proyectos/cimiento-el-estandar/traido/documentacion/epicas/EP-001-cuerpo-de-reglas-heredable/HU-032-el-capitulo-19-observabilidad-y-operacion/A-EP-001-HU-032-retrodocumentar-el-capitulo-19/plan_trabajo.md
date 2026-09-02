# Plan de Trabajo — Fase `A-EP-001-HU-032-retrodocumentar-el-capitulo-19`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Lo que se pide vive en la [HU-032](../HU-032-el-capitulo-19-observabilidad-y-operacion.md); con qué casos se comprueba, en el [plan_pruebas.md](plan_pruebas.md).

> **Una de veintiuna, con el molde aprobado el 2026-08-28.** `EP-001` tiene una historia por cada capítulo de `base/`, y las veintiuna piden lo mismo con distinto número. El molde se aprobó una vez, en la fase del capítulo `02`: **veintiuna aprobaciones de un documento idéntico convierten la puerta en trámite, y una puerta que es trámite deja de mirar.** Lo que cambia entre una y otra son **las cifras de este capítulo, medidas acá**.

---

## 1. Qué se va a hacer

**Dejar comprobado que el capítulo `19` tiene historia dueña declarada, y que un cambio suyo tiene por dónde bajarse.**

- 📄 **Es retro-documentación** (`13·DOC6`): el capítulo existe, se usa y ya nombra su historia. Esta fase **no lo reescribe**: comprueba y deja escrito lo que hoy es cierto y nadie había verificado.

### 1.1 Fuera de alcance

- **Reescribir reglas del capítulo.** Si al leerlo aparece algo mal, se anota como hallazgo; corregirlo es otra fase (`02·F20`).
- **Los checklists vencidos** de sus reglas: eso es `EP-001·HU-009`.
- **La comprobación automática** de esas reglas: eso es `EP-004`.
- **Las otras veinte historias de capítulo.** Cada una es su propia fase (`02·F12.1`).

---

## 2. Análisis previo  ·  `02·F17`

### 2.1 La línea base, medida

**Corrida, no citada** — es la lección de la `HU-021`: una medición vieja no es una medición.

| Qué | Cuánto | Con qué se midió |
|---|---|---|
| Historias de `EP-001` que son «un capítulo cada una» | **21** | `t00-las-22-historias-de-capitulo.py` |
| De ellas, con el `CA-01` **ya cumplido** | **21 de 21** | el mismo |
| Reglas del capítulo `19` | **6** | `metareglas.reglas()`, no contadas a mano |
| Forma del capítulo en el disco | archivo suelto | `retrodocumentar-los-capitulos.py` |
| Fases que tenía la HU-032 antes de esta | **0** | `validar.py fases` |



### 2.2 Lo que ya existe y no se rehace

| Pieza | Estado | Qué hace |
|---|---|---|
| El capítulo `base/19-observabilidad-y-operacion.md` | **Existe** | No se toca |
| Su cabecera con la historia dueña enlazada | **Ya está** | Es el `CA-01`, cumplido |
| La [HU-032](../HU-032-el-capitulo-19-observabilidad-y-operacion.md) | **Escrita** | Es el `CA-02`: el sitio donde baja un cambio |
| `validar.py enlaces` | **Existe** | Comprueba que el enlace de la cabecera no esté roto |

### 2.3 Qué se va a tocar

| Archivo | Qué se le hace |
|---|---|
| Los cinco documentos de esta carpeta | Se llenan |
| `HU-032-el-capitulo-19-observabilidad-y-operacion.md` §8 | La fila de la fase, y el estado |
| **Nada de `base/`** | El capítulo se lee, no se escribe |

### 2.4 Matriz de dependencias

| Archivo | Cambio de contrato | Quién depende | Dónde rompe |
|---|---|---|---|
| Ninguno | **Ninguno.** La fase no cambia código ni norma | — | No rompe nada |

### 2.5 Punto de entrada

Ninguno. Lo que esta fase comprueba se lee en la cabecera del capítulo.

### 2.6 Permisos / roles a sembrar

**Ninguno.**

### 2.7 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **Una fase por historia** | Una sola que cubra las veintiuna | `02·F12.1`: una fase pertenece a una sola historia. Juntarlas dejaría veinte historias sin dónde bajar sus cambios, que es lo que el `CA-02` pide |
| **Las cifras se miden, no se copian** | Repetir las del capítulo `02` en las veintiuna | Copiar ciento cinco documentos es la forma más segura de que uno diga algo falso sin que nadie lo note |
| **No se toca `base/`** | Arreglar de paso lo que se vea | Cambiar el capítulo para acomodar la fase es al revés |

### 2.8 Dudas por resolver antes de codificar

**Ninguna.** La única —¿el `CA-01` se cumple o hay que construirlo?— se resolvió midiendo antes de abrir la carpeta: **21 de 21**.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|:--:|---|---|---|
| T-00 | **Antes de abrir la carpeta:** medir el `CA-01` en las 21 | Calidad | — | — | EV-00 |
| T-01 | Comprobar que la cabecera del `19` nombra su historia **y el enlace resuelve** | Test | 0,3 h | T-00 | EV-01 |
| T-02 | Comprobar que la HU-032 existe y su §8 admite la fila | Test | 0,2 h | — | EV-02 |
| T-03 | Escribir el resultado de pruebas | Documentación | 0,5 h | T-01, T-02 | EV-03 |
| T-04 | Escribir el cierre y la fila en la §8 | Documentación | 0,5 h | T-03 | EV-03 |

**Total estimado:** 1,5 h.

**Versión: no sube.** No cambia `base/` ni `plantillas/`, así que `20·M10` no aplica.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-00 → T-01 → T-03 → T-04

**La `T-00` va primero por una razón:** si hubiera dado este capítulo sin su historia dueña, la fase no sería retro-documentación sino construcción, y su plan sería otro.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Evidencia | Resultado | Estado |
|---|---|---|---|---|
| CA-01 · el capítulo nombra su historia dueña | El programa sobre las 21, y el enlace resuelto | EV-00, EV-01 | Nombra la HU-032 | ☑ |
| CA-02 · un cambio tiene dónde bajarse | La historia existe y su §8 recibe la fila | EV-02 | Recibe la fila | ☑ |

---

## 6. Datos y ambiente de prueba

El repositorio real. **Ninguna prueba usa credenciales** (`00·N6`) y **ninguna escribe en `base/`**.

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte borrando la carpeta de la fase y su fila en la §8. **Nada más se tocó.**

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**No aplica:** no cambia nada que se instale ni que se despliegue.

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `13·DOC6` — retro-documentación: se documenta lo que ya existe.
- `02·F12.1` — una fase, una historia.
- `02·F17` — la línea base medida antes de planear, no citada.
- `02·F8` — solo los archivos declarados.
- `04·R4` — no se afirma sobre lo que no se leyó.

---

## 10. Riesgos

| # | Riesgo | Qué pasa si ocurre | Qué lo controla |
|---|---|---|---|
| R-01 | Que veintiuna fases idénticas vuelvan la aprobación un trámite | Una puerta que no mira deja de ser puerta | El molde se aprobó **una vez**, declarado |
| R-02 | Que la fase parezca terminada por tener sus cinco archivos | Es `H-40` | El comprobador rechaza los moldes sin llenar |
| R-03 | Que las cifras se copien de otra fase | Un documento que afirma sobre un capítulo que no miró | **Se miden acá**, capítulo por capítulo |

---

## 11. Aprobación

| Rol | Estado |
|---|---|
| Usuario | **Aprobado** el 2026-08-28, con el molde de las veintiuna |
