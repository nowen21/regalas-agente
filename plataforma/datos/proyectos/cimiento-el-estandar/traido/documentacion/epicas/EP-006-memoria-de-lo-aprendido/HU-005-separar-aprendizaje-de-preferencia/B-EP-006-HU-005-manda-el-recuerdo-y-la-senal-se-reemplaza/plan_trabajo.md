# Plan de Trabajo — Fase `B-EP-006-HU-005-manda-el-recuerdo-y-la-senal-se-reemplaza` (módulo Memoria)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** el criterio antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-006-HU-005-manda-el-recuerdo-y-la-senal-se-reemplaza` |
| **Épica** | [EP-006](../../epica.md) |
| **HU** | [HU-005](../HU-005-separar-aprendizaje-de-preferencia.md), **una sola** (`F12.1`) |
| **Módulo** | Memoria |
| **Fecha apertura** | 2026-08-30 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- **Cierra el CA-01, nada está guardado en los dos sitios diciendo cosas distintas**, que dejó la fase [`A-EP-006-HU-005-retrodocumentar-la-separacion-aprendizaje-preferencia`](../A-EP-006-HU-005-retrodocumentar-la-separacion-aprendizaje-preferencia/resultado_pruebas.md) en «No cumple» el 2026-08-17, porque **una cosa estaba guardada en los dos sitios y las dos versiones ya decían cosas distintas**: el recuerdo de terminología decía «Cimiento» desde el 2026-08-14, y la señal `S-002` seguía diciendo «el agente = Claude Code».

**Manda el recuerdo.** El usuario lo decidió el 2026-08-30 con la frase que zanja el caso: *«el agente (Cimiento) no es Claude Code»*.

**Este rojo no se cerraba midiendo.** Es de los que piden una decisión del usuario, y estuvo trece días esperándola.

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** aplicar la decisión y dejarla escrita donde se lee.

**Fuera de alcance:** los otros criterios de la historia, que ya estaban en verde.

---

## 2. Análisis previo, línea base verificada  ·  `02·F17`

> Medida antes de crear la carpeta de esta fase.

### 2.0 La línea base

```
105 cumplen, 4 no cumplen, 5 sin veredicto
```

### 2.1 Lo que hay, contado

**Por qué manda el recuerdo y no la señal.** El recuerdo es lo que el agente carga al abrir cada sesión: es lo que rige mientras trabaja. La señal es historia de por qué se decidió algo. Cuando las dos se contradicen, la que manda es la que se está leyendo.

**Y la señal no se borra.** El propio [`documentacion/senales.md`](../../../../../documentacion/senales.md) lo tiene escrito en su cabecera desde el principio: *«una señal revertida no se borra: se marca `reemplazada` y se enlaza la nueva»*. Nadie lo había aplicado a esta.

**Lo que hizo daño mientras tanto.** No es hipotético: el 2026-08-13 esa misma frase llevó a responder que el agente maneja machine learning. Quien lo maneja es Claude, que no es el agente. El recuerdo lo cuenta con fecha.

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| Los cinco documentos de esta fase | Crear | Documentación | — |
| `HU-005-separar-aprendizaje-de-preferencia.md` | Modificar | Documentación | Su `Estado` y su tabla de fases |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Manda el recuerdo | Que mande la señal, o decidirlo caso por caso | El recuerdo es lo que el agente carga al abrir sesión: es lo que rige mientras trabaja |
| La señal vieja se marca `reemplazada`, no se borra | Corregirla en su sitio | Reescribirla borraría el rastro de que se creyó lo contrario, y de que eso causó un error |
| La nueva se escribe en la misma base | Marcar la vieja apuntando al recuerdo | Una señal reemplazada por nada deja al lector sin dónde ir |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Medir el estado de los dos sitios | Análisis | 0,5 h | — | EV-01 |
| T-02 | Aplicar la decisión del usuario | Memoria | 0,5 h | T-01 | EV-02 |
| T-03 | Declarar el veredicto que deja atrás | Documentación | 0,25 h | T-02 | EV-02 |

**Total estimado:** 1,25 h

**Sin cambio de versión:** no se toca `base/` ni `plantillas/`.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 a T-02 a T-03

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| CA-01, nada está guardado en los dos sitios diciendo cosas distintas | Contar lo que hay en cada sitio, y comprobar el resultado de aplicar la decisión | EV-01, EV-02 | ☑ |

---

## 6. Datos y ambiente de prueba

El propio repositorio y la base de señales. Ninguna prueba usa credenciales.

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Nada que desplegar.**

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `01·C4`, decidir no es del que ejecuta. Es lo que tuvo detenida esta historia.
- `20·M11`, lo publicado no se reescribe: se deja atrás.
- `04·R4`, se cuenta en vez de afirmar sobre lo leído.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que el agente decidiera esto por su cuenta | Es `01·C4`, y era el motivo del rojo | Se esperó la decisión | Cerrado |
| B-02 | Que aflojar el criterio tape el problema en vez de resolverlo | Un criterio releído sin motivo es un criterio borrado | El motivo queda escrito acá y en el cierre | Cerrado |

---

## 11. Definition of Done

- [x] La decisión, aplicada
- [x] El motivo, escrito
- [ ] Autorizado el commit por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
