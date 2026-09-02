# Plan de Trabajo — Fase `C-EP-004-HU-021-cualquier-encabezado-de-veredicto-se-lee` (módulo Programas de comprobación)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-004-HU-021-cualquier-encabezado-de-veredicto-se-lee` |
| **Épica** | [EP-004](../../epica.md) |
| **HU** | [HU-021](../HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido.md) — **una sola** (`F12.1`) |
| **Módulo** | Programas de comprobación |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Fecha apertura** | 2026-08-27 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):
- 📝 **Corrige un defecto de la fase [`B`](../B-EP-004-HU-021-el-veredicto-se-lee-en-sus-tres-formas/funcionalidad_implementada.md), encontrado media hora después de publicarla.** Aquella declaró que hay **tres formas** de veredicto y **39 fases sin encabezado**. Al enumerar los encabezados de verdad, **sin encabezado hay 2**.

**Cómo se cometió, que es lo que importa:** la fase `B` contó las formas **que ya sabía buscar** — `**Concepto:**`, la tabla, y el encabezado `Veredicto de la fase` — y llamó «sin encabezado» a todo lo demás, sin mirarlo. **Eso es `04·R4`**, afirmar sobre lo que no se leyó, cometido en la fase cuyo tema era exactamente ese.

**Por qué una fase `C` y no reabrir la `B`:** aquella cerró con «Cumple», y lo que comprobó era cierto. **Reescribir un cierre sería borrar el rastro.** Es el mismo camino que la `B` respecto de la `A`.

**CA de la HU que cubre esta fase:** el `CA-03`, otra vez. Sigue contando aparte cosas que sí se pueden leer.

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que el lector reconozca también el encabezado `## N. Veredicto`, **y ninguno más**.

**Fuera de alcance:**

- **Uniformar los 130 resultados.** El molde fija una forma para lo nuevo; reescribir lo cerrado toca el rastro.
- **Las cinco fases que de verdad no lo dicen.** Esas se resuelven escribiendo su veredicto, una por una.
- **Los tres «No cumple» que van a aparecer.** Son trabajo real, y cada uno es su propia fase.

---

## 2. Análisis previo — línea base verificada  ·  `02·F17`

> Medido el 2026-08-27 **enumerando** los encabezados de los 130 resultados, no contando los que ya se reconocían. Los guiones quedaron en [historico-chat/scripts/2026-08-27/](../../../../../historico-chat/scripts/2026-08-27/).

### 2.0 Todos los encabezados que mencionan «veredicto»

| Título del encabezado | Cuántos | ¿Lo sigue la palabra suelta? |
|---|---|---|
| `Veredicto de la fase` | 91 | Ya se lee |
| `Veredicto por criterio de aceptación y requisito no funcional` | 40 | **No.** Lo sigue una tabla |
| **`Veredicto`** | **36** | **15 sí, 21 no** |
| `Veredicto por criterio de aceptación` | 28 | **No.** Lo sigue una tabla |
| `Veredicto final` | 4 | **No.** Lo sigue otra cosa |
| `Veredicto por criterio de la historia` | 1 | No |
| `Veredicto por exigencia` | 1 | No |
| **Sin ningún encabezado de veredicto** | **2** | — |

**El dato que decide el diseño:** de los seis títulos distintos, **`Veredicto` a secas es el único que va seguido de la palabra suelta**, quince veces. Los otros son la **tabla criterio por criterio**, que no es el veredicto de la fase.

**Por eso el patrón no puede ser «cualquier título que empiece por Veredicto».** Setenta encabezados empiezan así y no son el veredicto. Hoy no fallaría —van seguidos de tabla— pero sería **un patrón más ancho que el hecho**, y eso es cómo nació este defecto.

### 2.1 Lo que eso produce

| Qué | Valor verificado |
|---|---|
| La línea de hoy | `56 cumplen, 13 no cumplen, 15 no dicen` |
| Con el encabezado ajustado | **`63 cumplen, 16 no cumplen, 5 no dicen`** |
| Historias que se recuperan | **10** |
| De ellas, **que dicen «No cumple»** | **3** |
| Que de verdad siguen mudas | **5** |

**Tres de las diez dicen que no cumplen.** Es trabajo abierto que hoy no se ve, y es la mitad que importa: recuperar solo las que cumplen dejaría el número **mejor y más falso**.

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/fases.py` | Modificar | Servicio | Un patrón más, con el título exacto |
| `validadores/pruebas.py` | Modificar | Test | Casos por título, y de que **no** lea los «por criterio» |

### 2.2 Matriz de dependencias

| Archivo | Cambio de contrato | Quién depende | Dónde rompe |
|---|---|---|---|
| `validadores/fases.py` | **Ninguno.** `veredicto_de` y `por_veredicto` conservan su firma | `pruebas.py`, con 22 pruebas de las fases `A` y `B` | **No rompen.** Se comprobó midiendo: el patrón nuevo **no cambia ninguna historia que ya tuviera veredicto** |

### 2.3 Rutas / endpoints y control de acceso

**No aplica.**

### 2.4 Punto de entrada

`python validadores/validar.py fases`.

### 2.5 Permisos / roles a sembrar

**Ninguno.**

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El título tiene que ser **exactamente** `Veredicto` | Cualquiera que empiece por «Veredicto» | 70 encabezados empiezan así y son la tabla criterio por criterio. Aceptarlos abre la puerta a leer el primer criterio como veredicto de la fase — **la mentira optimista que la fase `B` evitó** |
| `Veredicto final` **no** entra | Agregarlo «por si acaso» | Sus cuatro casos **no** van seguidos de la palabra suelta. Agregarlo sería otra vez un patrón más ancho que el hecho |
| Un patrón **aparte**, no ampliar el de la fase `B` | Aflojar `_VEREDICTO_BAJO_TITULO` | Aflojarlo arriesga perder los 91 que ya sirven. Sumar no rompe |
| **No se uniforman los 130** | Reescribir todos a un título | El molde ya fija uno para lo nuevo |

### 2.7 Dudas por resolver antes de codificar

| # | Duda | Estado |
|---|---|---|
| — | Ninguna. Los seis títulos y lo que sigue a cada uno están contados | — |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Un patrón para el encabezado cuyo título es exactamente `Veredicto` | Backend | 0,5 h | — | EV-01 |
| T-02 | Un caso por cada uno de los dos títulos que sí se leen | Test | 1 h | T-01 | EV-01 |
| T-03 | Un caso de que **no** lea `Veredicto por criterio de aceptación` | Test | 0,5 h | T-01 | EV-02 |
| T-04 | Un caso de que **no** lea `Veredicto final` ni `Veredicto por exigencia` | Test | 0,5 h | T-01 | EV-02 |
| T-05 | Medir el número antes y después, y **adónde va cada una de las diez** | Documentación | 0,5 h | T-01 | EV-03 |
| T-06 | Que las 22 pruebas de las fases `A` y `B` sigan pasando sin tocarlas | Test | 0,5 h | T-01 | EV-04 |
| T-07 | Sabotear | Calidad | 1 h | — | EV-05 |

**Total estimado:** 4,5 h

**Sin cambio de versión:** no se toca `base/` ni `plantillas/`. `20·M10` no lo alcanza.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-03 → T-05

**T-03 es el caso que decide si esta fase sirve.** Setenta encabezados empiezan por «Veredicto» y no son el veredicto de la fase. Si el patrón los toma, esta fase **empeora** lo que vino a arreglar.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-03 · lo ilegible se cuenta aparte, **y solo lo ilegible** | Los dos títulos que sirven, más los cuatro que no | EV-01, EV-02 | | ☐ |
| Transversal · no regresión | Las 22 pruebas de `A` y `B`, sin tocarlas | EV-04 | | ☐ |

---

## 6. Datos y ambiente de prueba

Árboles de mentira en carpeta temporal. **Ninguna prueba usa credenciales** (`00·N6`), y ningún documento real se edita para probar (`08·T4`).

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

Quien ya tenga el estándar verá bajar sus «no dicen» y **subir tanto las que cumplen como las que no**. Es lo que corresponde: el trabajo abierto también estaba escondido.

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `02·F8` — solo los archivos declarados.
- `02·F17` — los seis títulos se enumeraron; **no se contaron los que ya se reconocían**.
- `04·R4` — no afirmar sobre lo que no se leyó. **Este defecto es esa regla incumplida por el agente**, en la fase que venía a hacerla cumplir.
- `13·DOC5` — lo decidido se registra como señal.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que el patrón tome los 70 «por criterio» | Leería el primer criterio como veredicto de la fase: **miente en la dirección optimista** | Título exacto, y `T-03` con su caso propio | Abierto |
| B-02 | Que vuelva a haber formas sin mirar | Tercera vez lo mismo | Se enumeraron **todos** los encabezados, y el guion que lo hizo quedó guardado | Abierto |
| B-03 | Que aparezcan tres «No cumple» y se traten como regresión | Se descartaría el arreglo por dar peor número | Están contados de antemano: son 3, y se nombran en el resultado | Abierto |

---

## 11. Definition of Done

- [ ] El criterio verificado con los dos títulos que sirven y los cuatro que no
- [ ] Las 22 pruebas de `A` y `B`, pasando sin tocarlas
- [ ] La suite completa en verde, con conteo distinto de cero
- [ ] Las diez recuperadas, nombradas una por una con adónde fueron
- [ ] Señal registrada
- [ ] Rama lista para el commit único
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
