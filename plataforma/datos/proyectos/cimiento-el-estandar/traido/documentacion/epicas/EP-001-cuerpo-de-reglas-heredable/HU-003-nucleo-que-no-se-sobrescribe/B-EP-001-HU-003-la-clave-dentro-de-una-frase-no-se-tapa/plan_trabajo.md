# Plan de Trabajo — Fase `B-EP-001-HU-003-la-clave-dentro-de-una-frase-no-se-tapa` (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** el criterio antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-001-HU-003-la-clave-dentro-de-una-frase-no-se-tapa` |
| **Épica** | [EP-001](../../epica.md) |
| **HU** | [HU-003](../HU-003-nucleo-que-no-se-sobrescribe.md), **una sola** (`F12.1`) |
| **Módulo** | Cuerpo de reglas |
| **Fecha apertura** | 2026-08-30 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- **Cierra el CA-02, la clave no queda en claro**, que dejó la fase [`A-EP-001-HU-003-retrodocumentar-el-nucleo-blindado`](../A-EP-001-HU-003-retrodocumentar-el-nucleo-blindado/resultado_pruebas.md) en «No cumple» el 2026-08-22, porque de seis formas de escribir una clave, **tres se enmascaran y tres no**. Las tres que no son las que dicen la clave dentro de una frase normal: «mi clave es Patito2026».

**No se tapa la clave dicha dentro de una frase, y queda declarado.** Lo decidió el usuario el 2026-08-30.

**Este rojo no se cerraba midiendo.** Medirlo otra vez daba el mismo resultado todos los días: el dato no cambiaba, faltaba saber qué se quería hacer con él.

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** aplicar la decisión, comprobarla ejecutando, y dejar escrito qué queda cubierto y qué no.

**Fuera de alcance:** los otros criterios de la historia, que ya estaban en verde.

---

## 2. Análisis previo, línea base verificada  ·  `02·F17`

> Medida antes de crear la carpeta de esta fase.

### 2.0 La línea base

```
107 cumplen, 2 no cumplen, 5 sin veredicto
```

### 2.1 Por qué la decisión es esta

**Por qué no se intenta.** Para tapar «mi clave es Patito2026» habría que suponer que la palabra que sigue a «clave» es la clave. Con esa misma suposición se tapa «la clave del asunto es que el proceso sirva», que es una frase corriente.

**Y el daño de tapar de más no es un falso positivo:** es que un enmascarado que estorba se apaga. Apagado no tapa ninguna de las seis, así que intentar tapar tres más pone en riesgo las tres que hoy sí se tapan.

**Lo que sí queda cubierto**, medido ejecutándolo: las tres formas en que la clave va pegada a su nombre, que son las que salen de un archivo de configuración, de un registro o de un comando pegado. Son las que aparecen sin que nadie las escriba a propósito.

**Lo que queda descubierto, dicho sin adorno:** si alguien escribe su clave dentro de una frase, queda escrita. La defensa ahí no es el programa: es `00·N6`, que prohíbe escribirla.

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| Los cinco documentos de esta fase | Crear | Documentación | — |
| `HU-003-nucleo-que-no-se-sobrescribe.md` | Modificar | Documentación | Su `Estado` y su tabla de fases |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| No se tapa la clave dicha dentro de una frase | Ampliar el enmascarado a la frase | Habría que suponer que la palabra siguiente a «clave» es la clave, y con eso se tapa «la clave del asunto es que sirva» |
| El límite se escribe, no se calla | Cerrar el criterio sin nombrarlo | Un criterio que se da por cumplido escondiendo lo que no cubre es la mentira optimista que esta cuenta existe para impedir |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Ejecutar el criterio y su contraprueba | Calidad | 0,5 h | — | EV-01 |
| T-02 | Aplicar la decisión del usuario | Implementación | 0,5 h | T-01 | EV-02 |
| T-03 | Declarar el veredicto que deja atrás | Documentación | 0,25 h | T-02 | EV-02 |

**Total estimado:** 1,25 h

**Sin cambio de versión:** no se toca `base/` ni `plantillas/`.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 a T-02 a T-03

La contraprueba de la `T-01` no es adorno: es la que sostiene la decisión.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| CA-02, la clave no queda en claro | Ejecutar el criterio con su contraprueba | EV-01, EV-02 | ☑ |

---

## 6. Datos y ambiente de prueba

Carpetas y valores de prueba que la propia prueba arma y borra. Ninguna
credencial real (`00·N6`).

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Nada que desplegar.**

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `01·C4`, decidir no es del que ejecuta. Es lo que tuvo detenida esta historia.
- `04·R4`, se ejecuta en vez de afirmar sobre lo leído.
- `20·M11`, lo publicado no se reescribe: se deja atrás.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Cerrar el criterio escondiendo lo que no cubre | Es la mentira optimista que esta cuenta existe para impedir | El límite queda escrito en el cierre | Cerrado |
| B-02 | Que el agente decidiera esto por su cuenta | Es `01·C4` | Se esperó la decisión | Cerrado |

---

## 11. Definition of Done

- [x] El criterio y su contraprueba, ejecutados
- [x] La decisión, aplicada
- [x] El límite, escrito
- [ ] Autorizado el commit por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
