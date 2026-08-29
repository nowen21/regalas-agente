# Plan de Trabajo — Fase `A-EP-001-HU-015-retrodocumentar-el-capitulo-02`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Lo que se pide vive en la [HU-015](../HU-015-el-capitulo-02-flujo-de-trabajo.md); con qué casos se comprueba, en el [plan_pruebas.md](plan_pruebas.md).

> **Esta fase es el molde de veintiuna.** `EP-001` tiene una historia por cada capítulo de `base/`, y las veintiuna piden lo mismo con distinto número. Lo que se apruebe acá se repite para las otras veinte, cambiando el capítulo y sus cifras. **Se dice de frente para que la aprobación se dé una vez y no veintiuna.**

---

## 1. Qué se va a hacer

**Dejar comprobado que el capítulo `02` tiene historia dueña declarada, y que un cambio suyo tiene por dónde bajarse.**

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
| Reglas del capítulo `02` | **32** | la propia HU §3 |
| Fases que tiene hoy la `HU-015` | **0** | `validar.py fases` |

**La segunda fila es la que decide qué clase de fase es esta.** Si el capítulo ya nombra su historia, no hay nada que construir: hay algo que **comprobar y dejar escrito**. Y si la medición hubiera dado alguno en «no», ese sería trabajo de verdad y esta fase cambiaría de forma.

### 2.2 Lo que ya existe y no se rehace

| Pieza | Estado | Qué hace |
|---|---|---|
| El capítulo `base/02-flujo-de-trabajo/` | **Existe, con 32 reglas** | No se toca |
| Su cabecera con la historia dueña enlazada | **Ya está** | Es el `CA-01`, cumplido |
| La [HU-015](../HU-015-el-capitulo-02-flujo-de-trabajo.md) | **Escrita** | Es el `CA-02`: el sitio donde baja un cambio |
| `validar.py enlaces` | **Existe** | Comprueba que el enlace de la cabecera no esté roto |

### 2.3 Qué se va a tocar

| Archivo | Qué se le hace |
|---|---|
| Los cinco documentos de esta carpeta | Se llenan |
| `HU-015-…md` §8 | La fila de la fase, y el estado |
| **Nada de `base/`** | El capítulo no se toca: se comprueba |

### 2.4 Matriz de dependencias

| Archivo | Cambio de contrato | Quién depende | Dónde rompe |
|---|---|---|---|
| Ninguno | **Ninguno.** La fase no cambia código ni norma | — | No rompe nada: solo se escribe documentación de fase |

### 2.5 Punto de entrada

Ninguno. Lo que esta fase comprueba se lee en la cabecera del capítulo.

### 2.6 Permisos / roles a sembrar

**Ninguno.**

### 2.7 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **Una fase por historia**, veintiuna en total | Una sola fase que cubra las veintiuna | `02·F12.1` pide que una fase pertenezca a una sola historia. Juntarlas dejaría veinte historias sin dónde bajar sus cambios, que es justo lo que el `CA-02` pide |
| **El `CA-01` se comprueba con un programa, no leyendo** | Abrir los 21 capítulos a ojo | Leer 21 cabeceras a ojo da un «sí» que nadie puede repetir. El programa deja la lista con nombres |
| **No se toca `base/`** | Aprovechar y arreglar lo que se vea | Cambiar el capítulo para acomodar la fase es al revés. Lo que aparezca se anota |
| **Se dice que es el molde de veintiuna** | Presentar cada una como si fuera nueva | Veintiuna aprobaciones de un documento idéntico convierten la puerta en un trámite, y una puerta que es trámite deja de mirar |

### 2.8 Dudas por resolver antes de codificar

**Ninguna.** La única que había —¿el `CA-01` se cumple o hay que construirlo?— se resolvió midiendo antes de abrir la carpeta: **21 de 21**.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|:--:|---|---|---|
| T-00 | **Antes de abrir la carpeta:** medir el `CA-01` en las 21 | Calidad | 0,5 h | — | EV-00 |
| T-01 | Comprobar que la cabecera del `02` nombra su historia **y el enlace resuelve** | Test | 0,3 h | T-00 | EV-01 |
| T-02 | Comprobar que la `HU-015` existe y su §8 admite la fila de una fase | Test | 0,2 h | — | EV-02 |
| T-03 | Escribir el resultado de pruebas | Documentación | 0,5 h | T-01, T-02 | EV-03 |
| T-04 | Escribir el cierre y la fila en la §8 de la HU | Documentación | 0,5 h | T-03 | EV-03 |

**Total estimado:** 2 h. **Y ese número importa más que de costumbre:** por veintiuna son **42 horas**, y es lo que hay que saber antes de decidir seguir.

**Versión: no sube.** No cambia `base/` ni `plantillas/`, así que `20·M10` no aplica: es documentación de fase.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-00 → T-01 → T-03 → T-04

**La `T-00` ya está corrida y va primero por eso:** si hubiera dado algún capítulo sin su historia dueña, esta fase no sería retro-documentación sino construcción, y su plan sería otro.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Evidencia | Resultado | Estado |
|---|---|---|---|---|
| CA-01 · el capítulo nombra su historia dueña | El programa sobre las 21, y el enlace resuelto | EV-00, EV-01 | | ☐ |
| CA-02 · un cambio tiene dónde bajarse | La historia existe y su §8 recibe la fila | EV-02 | | ☐ |

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
| R-01 | Que veintiuna fases idénticas vuelvan la aprobación un trámite | Una puerta que no mira deja de ser puerta | **Se declara de frente** en la caja de arriba: se aprueba el molde una vez |
| R-02 | Que la fase parezca terminada por tener sus cinco archivos, sin decir nada | Es `H-40`: un molde sin llenar contando como documento | El comprobador ya rechaza los moldes sin llenar |
| R-03 | Que al leer el capítulo aparezca algo mal y se corrija de paso | La fase se vuelve otra cosa, sin plan | `02·F20`: se anota como hallazgo |

---

## 11. Aprobación

| Rol | Estado |
|---|---|
| Usuario | **Aprobado** el 2026-08-28, **como molde de las veintiuna** |
