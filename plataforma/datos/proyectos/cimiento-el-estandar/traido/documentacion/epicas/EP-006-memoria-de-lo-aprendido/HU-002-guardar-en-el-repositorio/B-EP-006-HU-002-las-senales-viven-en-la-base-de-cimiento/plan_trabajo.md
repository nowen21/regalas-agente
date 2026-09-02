# Plan de Trabajo — Fase `B-EP-006-HU-002-las-senales-viven-en-la-base-de-cimiento` (módulo Memoria)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** el criterio antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-006-HU-002-las-senales-viven-en-la-base-de-cimiento` |
| **Épica** | [EP-006](../../epica.md) |
| **HU** | [HU-002](../HU-002-guardar-en-el-repositorio.md), **una sola** (`F12.1`) |
| **Módulo** | Memoria |
| **Fecha apertura** | 2026-08-30 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- **Cierra el CA-01, lo guardado vive en el repositorio con su historial**, que dejó la fase [`A-EP-006-HU-002-retrodocumentar-el-guardado-en-el-repositorio`](../A-EP-006-HU-002-retrodocumentar-el-guardado-en-el-repositorio/resultado_pruebas.md) en «No cumple» el 2026-08-17, porque las **237 señales** no estaban versionadas: `memoria/senales.db` está en `.gitignore` a propósito y no tiene ningún historial. Los 18 recuerdos sí cumplían.

**Las señales se quedan en su propia base, la de Cimiento.** Cimiento es la línea base de todos los proyectos, y su memoria es de todos: hoy la base guarda **268 señales**, de las cuales **186 son de siete proyectos distintos** y 82 son de organización. Meterla al control de versiones de este repositorio la ataría a uno solo de los proyectos que sirve.

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

**Por qué el criterio se relee y no se incumple.** El `CA-01` se escribió pensando en un solo repositorio, cuando la memoria era una carpeta de archivos. Al crecer resultaron ser dos cosas con dueños distintos:

- **Los recuerdos** son de este repositorio y de quien trabaja en él. Viven en `historico-chat/memory/`, versionados, y ahí el criterio se cumple entero: 23 archivos con su índice.
- **Las señales** son de Cimiento, que es la línea base de todos los proyectos. Su base es compartida, y por eso no puede vivir dentro del control de versiones de uno.

Lo que este repositorio sí versiona de señales es [`documentacion/senales.md`](../../../../../documentacion/senales.md), las suyas: 85 al cerrar esta fase.

**Y lo que no se decidió acá:** cómo se respalda esa base. Que no vaya al control de versiones de este repositorio no significa que no tenga que tener respaldo, y eso es de Cimiento como producto.

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| Los cinco documentos de esta fase | Crear | Documentación | — |
| `HU-002-guardar-en-el-repositorio.md` | Modificar | Documentación | Su `Estado` y su tabla de fases |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Las señales se quedan en la base de Cimiento | Versionar el `.db` en este repositorio | Es binario, dos sesiones se lo pisan sin fusión posible, y 186 de sus 268 señales son de otros proyectos |
| El criterio se relee, no se incumple | Dejar la historia en rojo para siempre | Fue escrito cuando la memoria era una carpeta de un solo repositorio. Lo que cambió es el alcance, no la exigencia |

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
| CA-01, lo guardado vive en el repositorio con su historial | Contar lo que hay en cada sitio, y comprobar el resultado de aplicar la decisión | EV-01, EV-02 | ☑ |

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
