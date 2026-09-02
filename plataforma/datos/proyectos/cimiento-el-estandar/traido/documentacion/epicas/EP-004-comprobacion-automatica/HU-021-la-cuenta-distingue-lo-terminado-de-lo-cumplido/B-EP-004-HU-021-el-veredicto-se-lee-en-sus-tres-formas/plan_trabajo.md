# Plan de Trabajo — Fase `B-EP-004-HU-021-el-veredicto-se-lee-en-sus-tres-formas` (módulo Programas de comprobación)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-004-HU-021-el-veredicto-se-lee-en-sus-tres-formas` |
| **Épica** | [EP-004](../../epica.md) |
| **HU** | [HU-021](../HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido.md) — **una sola** (`F12.1`) |
| **Módulo** | Programas de comprobación |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Fecha apertura** | 2026-08-27 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):
- 📝 **Corrige un defecto de la fase [`A`](../A-EP-004-HU-021-la-cuenta-mira-el-veredicto/funcionalidad_implementada.md), encontrado diez minutos después de cerrarla.** El lector del veredicto reconoce dos de las tres formas en que está escrito, y por eso siete historias se contaban como «no dicen si cumplen» **cuando sí lo dicen**.

**Por qué una fase `B` y no reabrir la `A`:** aquella cerró con «Cumple», y ese veredicto era cierto para lo que se comprobó. **Reescribir un cierre sería borrar el rastro.** El repositorio ya tiene el hábito: tres fases `B` de esta misma jornada nacieron así.

**CA de la HU que cubre esta fase:** el `CA-03`, que exige que lo que no se puede leer se cuente aparte. **Se cumplía de más:** contaba aparte cosas que sí se podían leer.

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que el lector del veredicto reconozca las tres formas en que está escrito en el repositorio, sin inventar ninguna.

**Fuera de alcance:**

- **Uniformar cómo se escribe el veredicto en las 129 fases.** El molde ya fija una sola forma para lo nuevo; reescribir lo cerrado sería tocar el rastro.
- **Las 39 fases sin encabezado de veredicto.** Esas de verdad no lo dicen, y se siguen contando aparte.

---

## 2. Análisis previo — línea base verificada  ·  `02·F17`

> Medido el 2026-08-27, recorriendo las 129 fases.

### 2.0 Las tres formas, y cuál falla

| Forma | Cuántas fases | ¿La lee hoy? |
|---|---|---|
| `**Concepto:** Cumple` | **67** | Sí |
| Tabla con `\| **Concepto** \| Cumple \|` | **16** | Sí |
| `**Cumple.**` bajo el encabezado, sin rótulo | **7** | **No** |
| Sin encabezado de veredicto | 39 | No, **y es correcto**: no lo dicen |

**Solo falta una forma, y son siete fases.** Se comprobó una por una que la de tabla sí se lee, en vez de suponerlo.

### 2.1 Lo que eso produce

| Qué | Valor verificado |
|---|---|
| La línea de hoy | `117 en total · 32 sin terminar · 85 terminadas, de las cuales 52 cumplen, 11 no cumplen y 22 no dicen si cumplen` |
| Historias contadas como «no dicen» que **sí dicen** | **7** |
| Historias que de verdad no lo dicen | 15 |

**El número está mal en la dirección pesimista**, que es la menos dañina de las dos — pero mal igual.

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/fases.py` | Modificar | Servicio | `_VEREDICTO` reconoce la tercera forma |
| `validadores/pruebas.py` | Modificar | Test | Un caso por forma, y uno que las cuente todas |

### 2.2 Matriz de dependencias

| Archivo | Cambio de contrato | Quién depende | Dónde rompe |
|---|---|---|---|
| `validadores/fases.py` | **Ninguno.** `veredicto_de` y `por_veredicto` conservan su firma | `pruebas.py`, con 14 pruebas | **No rompen**: lo que cambia es cuántas formas reconoce |

### 2.3 Rutas / endpoints y control de acceso

**No aplica.**

### 2.4 Punto de entrada

`python validadores/validar.py fases`. La línea dirá otros números.

### 2.5 Permisos / roles a sembrar

**Ninguno.**

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Se agrega **la forma que existe**, no las que podrían existir | Un lector laxo que acepte cualquier cosa | Un lector que adivina termina leyendo veredictos donde no los hay. Se midió cuáles hay: son tres |
| El veredicto debe estar **bajo su encabezado**, no en cualquier parte | Buscar «Cumple» en todo el documento | En un resultado la palabra aparece en cada fila de criterio. Sin el encabezado se leería el primer criterio en vez del veredicto |
| **No se uniforman las 129** | Reescribir todas a una forma | El molde ya fija una para lo nuevo. Reescribir lo cerrado toca el rastro |

### 2.7 Dudas por resolver antes de codificar

| # | Duda | Estado |
|---|---|---|
| — | Ninguna. Las formas se contaron una por una | — |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Que `_VEREDICTO` reconozca la forma bajo el encabezado | Backend | 1 h | — | EV-01 |
| T-02 | Que siga exigiendo el encabezado, y no lea el primer criterio | Backend | 0,5 h | T-01 | EV-02 |
| T-03 | Un caso por cada una de las tres formas | Test | 1,5 h | T-01 | EV-01 |
| T-04 | Un caso de que **no** lea un «Cumple» suelto sin encabezado | Test | 0,5 h | T-02 | EV-02 |
| T-05 | Medir el número antes y después | Documentación | 0,5 h | T-01 | EV-03 |
| T-06 | Que las 14 pruebas de la fase `A` sigan pasando sin tocarlas | Test | 0,5 h | T-01 | EV-04 |
| T-07 | Sabotear | Calidad | 1 h | — | EV-05 |

**Total estimado:** 5,5 h

**Sin cambio de versión:** no se toca `base/` ni `plantillas/`. Es un defecto de un programa, y `20·M10` no lo alcanza.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-05

**T-02 no es un detalle.** Un lector que busque «Cumple» sin exigir su encabezado leería la primera fila de criterios de cualquier resultado, y **daría por cumplida una fase que no lo está**. El arreglo tiene que ampliar sin aflojar.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-03 · lo ilegible se cuenta aparte, **y solo lo ilegible** | Las tres formas, más el caso de que no lea de más | EV-01, EV-02 | | ☐ |
| Transversal · no regresión | Las 14 pruebas de la fase `A`, sin tocarlas | EV-04 | | ☐ |

---

## 6. Datos y ambiente de prueba

Árboles de mentira en carpeta temporal. **Ninguna prueba usa credenciales** (`00·N6`), y ningún documento real se edita para probar (`08·T4`).

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit. No hay estado ni versión que deshacer.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Quien ya tenga el estándar** verá su número de «no dicen si cumplen» bajar, y el de «cumplen» subir. **No cambió nada de su trabajo**: cambió cuántas formas sabe leer el programa.

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `02·F8` — solo los archivos declarados.
- `02·F17` — las tres formas se contaron una por una, no se supusieron.
- `04·R4` — no afirmar sobre lo que no se leyó. **Este defecto es justamente eso**, cometido por el programa.
- `13·DOC5` — lo decidido se registra como señal.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que el lector quede tan laxo que lea veredictos donde no los hay | Contaría por cumplidas fases que no lo dicen | T-02 y su caso propio: exige el encabezado | Abierto |
| B-02 | Que existan más formas y esta fase deje otras sin leer | Volvería a pasar lo mismo | Se contaron las 129: hay tres, y 39 sin encabezado | Abierto |

---

## 11. Definition of Done

- [ ] El criterio verificado con las tres formas
- [ ] Las 14 pruebas de la fase `A`, pasando sin tocarlas
- [ ] La suite completa en verde, con conteo distinto de cero
- [ ] Señal registrada
- [ ] Rama lista para el commit único
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
