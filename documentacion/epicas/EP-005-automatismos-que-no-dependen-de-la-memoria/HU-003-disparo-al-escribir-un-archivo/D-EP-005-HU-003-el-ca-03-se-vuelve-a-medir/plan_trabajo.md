# Plan de Trabajo — Fase `D-EP-005-HU-003-el-ca-03-se-vuelve-a-medir` (módulo Automatismos — enganches)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** el criterio antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `D-EP-005-HU-003-el-ca-03-se-vuelve-a-medir` |
| **Épica** | [EP-005](../../epica.md) |
| **HU** | [HU-003](../HU-003-disparo-al-escribir-un-archivo.md) — **una sola** (`F12.1`) |
| **Módulo** | Automatismos — enganches |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Fecha apertura** | 2026-08-29 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- **Cierra un rojo que dejó de ser cierto.** La fase [`A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir`](../A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir/resultado_pruebas.md) cerró con «No cumple» el 2026-08-17 por **CA-03 · El hallazgo grave detiene, y el resto avisa**: el disparo corría en el momento y callaba con lo que no le tocaba, pero **todo avisaba**: nada distinguía el hallazgo grave del que solo informa. **Era cierto entonces.** Lo resolvió después `B-EP-005-HU-003-el-hallazgo-grave-detiene`.

**Por qué hace falta una fase y no basta con anotarlo:** el veredicto de la fase roja **no se toca** (`20·M11`) —reescribirlo borraría el rastro de que el criterio estuvo en rojo—, y **nadie vuelve a mirar un rojo por su cuenta** (`S-061`). El mecanismo que lo permite es `EP-004·HU-023`: la fase que cumple **declara** qué veredicto deja atrás, y el conteo lo lee.

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** comprobar, ejecutando, que **CA-03 hoy se cumple**, y dejarlo declarado donde se lee.

**Fuera de alcance:**

- **Construir nada.** El trabajo ya está hecho; lo que falta es que alguien vuelva a mirarlo.
- **Tocar la fase `A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir`.** Su veredicto fue cierto el día que se escribió.
- **Los otros rojos de la cuenta.** Cada uno tiene su medición y su fase.

---

## 2. Análisis previo — línea base verificada  ·  `02·F17`

> **Medida antes de crear la carpeta de esta fase**, porque abrirla mueve el número.

### 2.0 La línea base

```
96 cumplen · 13 no cumplen · 5 sin veredicto
```

### 2.1 Cómo se comprueba el criterio

El enganche de escritura se corre **dos veces**, con un documento que deja un enlace roto y con uno sano. Las dos respuestas tienen que ser distintas: 2 y 0.

**Y por qué la medición no se da por buena de más.** Comprobar solo el caso grave no dice nada: un enganche que devuelve 2 siempre también lo pasaría, y detendría el trabajo en cada edición hasta que alguien lo apague.

**Resultado de la medición:** el enlace roto devuelve 2 y el documento sano devuelve 0

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| Los cinco documentos de esta fase | Crear | Documentación | El cierre declara el veredicto |
| `HU-003-disparo-al-escribir-un-archivo.md` | Modificar | Documentación | Su `Estado` nombra el criterio en rojo |

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
| CA-03 · El hallazgo grave detiene, y el resto avisa | Ejecutar el criterio, con su contraprueba | EV-01, EV-02 | ☑ |

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
