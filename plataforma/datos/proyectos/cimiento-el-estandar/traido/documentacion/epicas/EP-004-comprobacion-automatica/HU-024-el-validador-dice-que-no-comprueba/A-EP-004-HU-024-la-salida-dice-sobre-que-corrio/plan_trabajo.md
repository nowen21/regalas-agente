# Plan de Trabajo — Fase `A-EP-004-HU-024-la-salida-dice-sobre-que-corrio` (módulo Programas de comprobación)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-024-la-salida-dice-sobre-que-corrio` |
| **Épica** | [EP-004](../../epica.md) |
| **HU** | [HU-024](../HU-024-el-validador-dice-que-no-comprueba.md), **una sola** (`F12.1`) |
| **Módulo** | Programas de comprobación |
| **Fecha apertura** | 2026-08-30 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- **Defecto, y lo cobró el propio agente.** El 2026-08-30 corrió `validar.py marcas` sobre veinticinco documentos nuevos de `documentacion/`, obtuvo cero, y escribió en el cuerpo de un commit que el validador no reportaba ninguna línea de esos archivos. El enganche del commit, que sí lee lo que entra al índice, encontró **trece avisos** en esos mismos archivos. La afirmación falsa quedó publicada. Sale del [pendiente 91](../../../../../pendientes/91-el-validador-de-marcas-no-dice-que-no-comprueba.md).

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que la salida diga sobre qué corrió y qué partes de la norma no cuenta, para que un cero no se pueda leer como un aprobado.

**Fuera de alcance:**

- **Ampliar el recorrido a `documentacion/`.** Es más trabajo, produciría ruido de entrada porque esa carpeta arrastra deuda vieja, y es una decisión aparte.
- Construir la comprobación de las marcas que hoy se leen a mano.

---

## 2. Análisis previo, línea base verificada  ·  `02·F17`

> Medida antes de crear la carpeta de esta fase.

### 2.0 La línea base

```
119 cumplen, 0 no cumplen, 0 sin veredicto
```

### 2.1 Los dos filos del mismo cero

| Filo | Qué pasa |
|---|---|
| El alcance | El subcomando recorre `base/` y `plantillas/`. Sobre cualquier otra carpeta devuelve cero **porque no mira** |
| La cobertura | Cuenta las marcas mecánicas y deja para la lectura las que hay que juzgar. Su cero tampoco lo dice |

**Los dos se ven igual desde el resultado**, y por eso el primero engañó.

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/marcas.py` | Modificar | Comprobación | `alcance()`, y que `validar()` cuente lo que mira |
| `validadores/validar.py` | Modificar | Comprobación | Que el subcomando imprima las dos frases |
| `validadores/tests/test_el_validador_dice_sobre_que_corrio.py` | Crear | Pruebas | Cinco casos |
| Los cinco documentos de esta fase | Crear | Documentación | — |
| `HU-024-el-validador-dice-que-no-comprueba.md` | Modificar | Documentación | Su `Estado` y su tabla de fases |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El alcance sale de **lo que la corrida recorrió** | Escribir la frase a mano | Una frase aparte envejece sin avisar, y este defecto nació de creerle a un número |
| Se nombra la carpeta **y cuántos archivos** | Solo la carpeta | El número es lo que deja ver que se miró algo, y distingue el árbol vacío |
| «No había nada que mirar» es una frase distinta | Dejar el mismo cero | Son dos respuestas y se imprimían igual |
| Las dos frases van **después** del resultado | Antes | Lo primero que se lee tiene que ser el veredicto; el alcance lo califica |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Que la corrida cuente qué archivos miró | Comprobación | 0,5 h | — | EV-01 |
| T-02 | Armar las dos frases con ese dato | Comprobación | 0,5 h | T-01 | EV-01 |
| T-03 | Distinguir «no había nada» de «no hay marcas» | Comprobación | 0,25 h | T-02 | EV-01 |
| T-04 | Que el subcomando las imprima | Comprobación | 0,25 h | T-03 | EV-02 |

**Total estimado:** 1,5 h

**Sin cambio de versión:** no se toca `base/` ni `plantillas/`.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 a T-02 a T-03 a T-04

La `T-01` va primero porque es la que hace honesto lo demás: sin contar, la
frase sería un texto escrito aparte, que es lo que se quiere evitar.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| CA-01 · la salida nombra sobre qué corrió | Un árbol con archivos dentro y fuera del alcance | CP-001, CP-002 | ☑ |
| CA-02 · nombra qué no cuenta | La segunda frase, sobre un árbol limpio | CP-004 | ☑ |
| CA-03 · sin nada que mirar lo dice | Un árbol sin archivos en el alcance | CP-003 | ☑ |

---

## 6. Datos y ambiente de prueba

Árboles temporales que la propia prueba arma y borra.

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Nada que desplegar.** Se nota la próxima vez que alguien corra el comando.

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `00·ID8`, las marcas que este validador comprueba.
- `04·R4`, se ejecuta en vez de afirmar sobre lo leído. Es la regla que el defecto rompió.
- `08·T5`, las pruebas corren y se reporta el número.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que la frase y el recorrido se separen con el tiempo | Volvería el mismo defecto por otra puerta | `CP-005` compara la frase con las carpetas que el programa recorre | Cerrado |
| B-02 | Que la salida se alargue tanto que nadie la lea | Dos líneas al final, y solo lo que cambia la lectura del número | — | Cerrado |

---

## 11. Definition of Done

- [x] Las dos frases, saliendo de lo recorrido
- [x] Cinco pruebas en verde
- [ ] Autorizado el commit por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
