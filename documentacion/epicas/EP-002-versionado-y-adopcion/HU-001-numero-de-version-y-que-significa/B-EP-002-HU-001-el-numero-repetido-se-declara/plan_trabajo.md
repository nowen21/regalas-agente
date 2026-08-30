# Plan de Trabajo — Fase `B-EP-002-HU-001-el-numero-repetido-se-declara` (módulo Versionado y adopción)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** el criterio antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-002-HU-001-el-numero-repetido-se-declara` |
| **Épica** | [EP-002](../../epica.md) |
| **HU** | [HU-001](../HU-001-numero-de-version-y-que-significa.md), **una sola** (`F12.1`) |
| **Módulo** | Versionado y adopción |
| **Fecha apertura** | 2026-08-30 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- **Cierra el CA-01, que quedó en rojo por una exigencia que el propio registro decidió no cumplir.** La fase [`A`](../A-EP-002-HU-001-retrodocumentar-el-numero-de-version/resultado_pruebas.md) cerró el 2026-08-22 porque `15.4.0` aparece dos veces, del 2026-08-14 y del 2026-08-15. Lo dejaron dos sesiones abiertas a la vez sobre el mismo repositorio, que es el [pendiente 22](../../../../../pendientes/hecho/dos-sesiones-versionando-a-la-vez.md).

**Y el registro ya decidió qué hacer con eso, el mismo 15 de agosto:** no se renumera. Un proyecto pudo haber adoptado `15.4.0`, y cambiarle el número después le mueve el piso sin que se entere. La segunda entrada lleva la marca de repetido y el motivo escrito.

**Entonces lo que estaba mal no era el registro: era la prueba.** Exigía unicidad, una exigencia que la casa decidió no cumplir por un motivo mejor, y por eso llevaba ocho días marcada como fallo esperado. Una prueba así no mide: enseña a ignorar los fallos esperados.

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que la prueba exija lo que de verdad se sostiene —que un número repetido esté declarado, con las dos entradas a la vista— y que salga del fallo esperado.

**Fuera de alcance:**

- **Renumerar la entrada.** Es lo que el registro decidió no hacer, y por buen motivo.
- **Tocar el `CHANGELOG.md`.** No se modifica ni una línea.
- **El aviso de `validar.py versionado`.** Ya dice lo que hay que decir, y se conserva: es lo que hace visible el caso en cada corrida.

---

## 2. Análisis previo, línea base verificada  ·  `02·F17`

> Medida antes de crear la carpeta de esta fase.

### 2.0 La línea base

```
102 cumplen, 7 no cumplen, 5 sin veredicto
```

### 2.1 Qué exige el CA-01 y qué hay

| Pieza | Estado |
|---|---|
| El número existe y sale de un solo archivo | Ya cumplía |
| Las entradas del registro declaran su tipo | Ya cumplía |
| Ningún número identifica dos cambios distintos | **`15.4.0` lo hace, y se decidió dejarlo** |
| La repetición está declarada donde se lee el número | **Sí**, en el encabezado de la entrada del 15 |

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/pruebas.py` | Modificar | Pruebas | La clase `NumeroDeVersion` |
| Los cinco documentos de esta fase | Crear | Documentación | — |
| `HU-001-numero-de-version-y-que-significa.md` | Modificar | Documentación | Su `Estado` y su tabla de fases |

**No se toca `CHANGELOG.md`, ni `VERSION`, ni ningún validador.**

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La prueba exige que lo repetido **se declare** | Exigir unicidad | Es lo que el registro decidió sostener, y con motivo escrito |
| La marca vale en **cualquiera de las dos entradas** | Exigirla en la segunda | Las dos comparten número; lo que importa es que la repetición esté dicha donde se lee |
| Se prueba también el **repetido callado** | Solo el caso real | Sin la contraprueba, la prueba nueva pasaría con un registro que pisa números en silencio |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Leer qué exige el CA-01 y qué decidió el registro | Análisis | 0,25 h | — | EV-01 |
| T-02 | Que la prueba exija lo que se sostiene | Pruebas | 0,75 h | T-01 | EV-02 |
| T-03 | Probar el repetido callado | Pruebas | 0,5 h | T-02 | EV-02 |

**Total estimado:** 1,5 h

**Sin cambio de versión:** no se toca `base/` ni `plantillas/`.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 a T-02 a T-03

La `T-03` no es opcional: sin ella, aceptar el repetido declarado es aceptar cualquier repetido.

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| CA-01, el número dice qué cambió y no se pisa en silencio | La prueba sobre el registro real, y la contraprueba sobre uno inventado | EV-02 | ☑ |

---

## 6. Datos y ambiente de prueba

El `CHANGELOG.md` real, sin tocarlo, y una secuencia inventada dentro de la prueba.

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Nada que desplegar.**

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `20·M10`, todo cambio de regla se versiona y se registra. Es la regla que el número sostiene.
- `20·M11`, lo que ya se publicó no se reescribe. Es el motivo de no renumerar.
- `08·T5`, las pruebas corren y se reporta el número.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Aflojar la prueba para que pase | Sería tapar el defecto en vez de medirlo | `T-03`, la contraprueba | Cerrado |
| B-02 | Que alguien lea esto como permiso para repetir números | Dos cambios con el mismo número, a propósito | La prueba exige la declaración; el aviso de `versionado` sigue saliendo | Cerrado |

---

## 11. Definition of Done

- [x] La prueba, fuera del fallo esperado
- [x] La contraprueba, en verde
- [ ] Autorizado el commit por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
