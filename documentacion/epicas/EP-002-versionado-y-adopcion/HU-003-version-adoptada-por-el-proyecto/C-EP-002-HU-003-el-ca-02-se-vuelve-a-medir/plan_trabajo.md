# Plan de Trabajo — Fase `C-EP-002-HU-003-el-ca-02-se-vuelve-a-medir` (módulo Programas de comprobación)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** el criterio antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-002-HU-003-el-ca-02-se-vuelve-a-medir` |
| **Épica** | [EP-002](../../epica.md) |
| **HU** | [HU-003](../HU-003-version-adoptada-por-el-proyecto.md) — **una sola** (`F12.1`) |
| **Módulo** | Programas de comprobación |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Fecha apertura** | 2026-08-29 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- **Cierra un rojo que dejó de ser cierto.** La fase [`A-EP-002-HU-003-retrodocumentar-la-version-adoptada`](../A-EP-002-HU-003-retrodocumentar-la-version-adoptada/resultado_pruebas.md) cerró con «No cumple» el 2026-08-22 por **CA-02 · Una versión que no existe se detecta**: `99.9.9` pasaba en silencio y, **por ser mayor que la vigente, apagaba el aviso de desfase**: declarar una versión falsa hacia adelante callaba la única comprobación que había. **Era cierto entonces.** Lo resolvió después `B-EP-002-HU-003-la-version-declarada-se-comprueba`.

**Por qué hace falta una fase y no basta con anotarlo:** el veredicto de la fase roja **no se toca** (`20·M11`) —reescribirlo borraría el rastro de que el criterio estuvo en rojo—, y **nadie vuelve a mirar un rojo por su cuenta** (`S-061`). El mecanismo que lo permite es `EP-004·HU-023`: la fase que cumple **declara** qué veredicto deja atrás, y el conteo lo lee.

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** comprobar, ejecutando, que **CA-02 hoy se cumple**, y dejarlo declarado donde se lee.

**Fuera de alcance:**

- **Construir nada.** El trabajo ya está hecho; lo que falta es que alguien vuelva a mirarlo.
- **Tocar la fase `A-EP-002-HU-003-retrodocumentar-la-version-adoptada`.** Su veredicto fue cierto el día que se escribió.
- **Los otros rojos de la cuenta.** Cada uno tiene su medición y su fase.

---

## 2. Análisis previo — línea base verificada  ·  `02·F17`

> **Medida antes de crear la carpeta de esta fase**, porque abrirla mueve el número.

### 2.0 La línea base

```
96 cumplen · 13 no cumplen · 5 sin veredicto
```

### 2.1 Cómo se comprueba el criterio

Se arma un proyecto de prueba en una carpeta temporal cuyo `CLAUDE.md` declara `99.9.9`, y se corre `version.validar` sobre él. Tiene que salir una **falla**, no un silencio.

**Y por qué la medición no se da por buena de más.** Se mide sobre una carpeta temporal y no sobre un proyecto real, como manda la decisión 35 del pendiente 59: tocar el `CLAUDE.md` de un proyecto vivo para probar es cambiarle el estado a alguien más.

**Resultado de la medición:** el proyecto declara la v99.9.9, que no existe en el registro de cambios del estándar — mientras el número sea falso, el aviso de desfase no dice nada

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| Los cinco documentos de esta fase | Crear | Documentación | El cierre declara el veredicto |
| `HU-003-version-adoptada-por-el-proyecto.md` | Modificar | Documentación | Su `Estado` nombra el criterio en rojo |

**No se toca código.** Esta fase **comprueba y declara**.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Una fase que **declara**, sin tocar la roja | Reescribir aquel veredicto | Fue cierto el día que se escribió; reescribirlo borra el rastro (`20·M11`) |
| El reemplazo **se declara**, no se deduce del orden | Dar por cumplido el rojo porque hay una fase posterior | Está medido: de las ocho historias con fase posterior, solo dos habían vuelto a verificar el criterio rojo. Deducirlo taparía rojos vivos con trabajo ajeno |
| Las cifras las **mide un programa** | Copiar el documento de la fase anterior | Nadie relee el número veinte de una serie, y ahí es donde entra el dato falso |

### 2.7 Dudas por resolver antes de codificar

| # | Duda | Estado |
|---|---|---|
| — | Ninguna. La medición se corrió antes de escribir esto | — |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Ejecutar el criterio que quedó en rojo | Calidad | 0,5 h | — | EV-01 |
| T-02 | Comprobar que la medición no se da por buena de más | Calidad | 0,5 h | T-01 | EV-02 |
| T-03 | Poner al día el `Estado` de la historia | Documentación | 0,25 h | T-02 | EV-03 |
| T-04 | Declarar el veredicto que deja atrás | Documentación | 0,25 h | T-03 | EV-03 |

**Total estimado:** 1,5 h

**Sin cambio de versión:** no se toca `base/` ni `plantillas/`. `20·M10` no lo alcanza.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-04

La `T-02` no es un adorno de la `T-01`: una medición que solo mira el caso bueno
da verde sobre cualquier cosa.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| CA-02 · Una versión que no existe se detecta | Ejecutar el criterio, con su contraprueba | EV-01, EV-02 | ☑ |

---

## 6. Datos y ambiente de prueba

Carpetas temporales, creadas y borradas por la medición. **Ninguna prueba usa
credenciales** (`00·N6`), y no se toca ningún proyecto real.

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit. No hay estado ni versión que deshacer.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Nada que desplegar.** Lo que cambia es que la historia deja de arrastrar un
rojo que ya no existe.

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `02·F17` — la línea base, medida antes de crear la carpeta.
- `04·R4` — se ejecuta en vez de afirmar sobre lo leído.
- `13·DOC5` — lo decidido se registra como señal.
- `20·M11` — el veredicto viejo no se borra: se deja atrás.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que se dé por cumplido leyendo el código en vez de corriéndolo | Sería declarar cumplido un rojo vivo | `T-01` ejecuta | Cerrado |
| B-02 | Que la medición pase por mirar solo el caso bueno | Verde sobre cualquier cosa | `T-02` | Cerrado |
| B-03 | Que abrir esta fase mueva la medición | `S-053` | La línea base está en el §2.0 | Cerrado |

---

## 11. Definition of Done

- [x] El criterio, **ejecutado**
- [x] La contraprueba, ejecutada
- [ ] El `Estado` de la historia, al día
- [ ] Autorizado el commit por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el
[funcionalidad_implementada.md](funcionalidad_implementada.md).
