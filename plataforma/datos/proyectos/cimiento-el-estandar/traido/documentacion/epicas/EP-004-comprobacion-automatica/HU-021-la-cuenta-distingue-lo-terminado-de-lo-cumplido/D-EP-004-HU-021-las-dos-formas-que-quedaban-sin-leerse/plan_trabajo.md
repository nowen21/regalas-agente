# Plan de Trabajo — Fase `D-EP-004-HU-021-las-dos-formas-que-quedaban-sin-leerse` (módulo Programas de comprobación)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** el criterio antes de darlo por cumplido.

---

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `D-EP-004-HU-021-las-dos-formas-que-quedaban-sin-leerse` |
| **Épica** | [EP-004](../../epica.md) |
| **HU** | [HU-021](../HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido.md), **una sola** (`F12.1`) |
| **Módulo** | Programas de comprobación |
| **Fecha apertura** | 2026-08-30 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`):

- **Quedaban cinco historias contadas como «no dicen si cumplen», y las cinco lo dicen.** Al listarlas una por una aparecieron dos formas de escribir el veredicto que el lector no reconoce, después de tres fases dedicadas justamente a eso.

---

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que el lector reconozca las dos formas que faltaban, sin ampliar dónde busca.

**Fuera de alcance:**

- **Tocar los cinco resultados.** Son fases cerradas: se corrige el lector, no lo leído (`20·M11`).
- Aceptar títulos que empiecen por «Veredicto» y sean la tabla criterio por criterio. Eso es lo que la fase `C` dejó cerrado a propósito.

---

## 2. Análisis previo, línea base verificada  ·  `02·F17`

> Medida antes de crear la carpeta de esta fase.

### 2.0 La línea base

```
109 cumplen, 0 no cumplen, 5 sin veredicto
```

### 2.1 Las dos formas, y en cuántas fases está cada una

| Forma | Dónde | Cuántas |
|---|---|---|
| `**Concepto: Cumple.**`, con los dos puntos **dentro** de la negrita | Bajo `## 6. Veredicto de la fase` | 3 |
| `## 6. Concepto final` y la palabra debajo | El título dice «Concepto», no «Veredicto» | 2 |

**La primera es la que más engaña:** `**Concepto: Cumple.**` y `**Concepto:** Cumple` se leen igual y solo se diferencian en dónde cierran los asteriscos. El lector pedía los asteriscos justo después de «Concepto:».

**La segunda ya se aceptaba con la otra palabra.** La fase `B` leía la palabra sola bajo `## N. Veredicto de la fase`; estas dos usan `## N. Concepto final`, que es el otro término del glosario para lo mismo.

### 2.1.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/fases.py` | Modificar | Comprobación | Dos patrones más, y su uso |
| `validadores/pruebas.py` | Modificar | Pruebas | Tres casos: los dos nuevos y el que impide leer de más |
| Los cinco documentos de esta fase | Crear | Documentación | — |
| `HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido.md` | Modificar | Documentación | Su tabla de fases |

**No se toca ninguno de los cinco resultados que quedaban mudos.**

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Se corrige el lector | Reescribir los cinco resultados | Son fases cerradas: `20·M11` |
| Se amplía **qué título vale**, no dónde se busca | Buscar la palabra suelta | En un resultado «Cumple» aparece en cada fila de criterio |
| El título nuevo se acepta con `[^\n]*` detrás | Exigir «Concepto final» exacto | «Concepto» y «Concepto final» son la misma sección; lo que se exige es que sea un encabezado |

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Leer las cinco que quedaban mudas | Análisis | 0,5 h | — | EV-01 |
| T-02 | Ampliar el lector | Comprobación | 0,5 h | T-01 | EV-02 |
| T-03 | Probar que no lee de más | Pruebas | 0,5 h | T-02 | EV-03 |
| T-04 | Declarar el resultado | Documentación | 0,25 h | T-03 | EV-03 |

**Total estimado:** 1,75 h

**Sin cambio de versión:** no se toca `base/` ni `plantillas/`.

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 a T-02 a T-03 a T-04

La `T-01` va primero y no es trámite: **si las cinco no dijeran su veredicto, esto no sería un defecto del lector sino trabajo de cinco fases.**

> Solo se tocan los archivos declarados (`02·F8`).

---

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| La tercera cuenta dice la verdad: lo que declara su veredicto se lee | Contar antes y después, y probar el caso que no debe leerse | EV-01, EV-03 | ☑ |

---

## 6. Datos y ambiente de prueba

Árboles temporales que la propia prueba arma y borra, y el árbol real para la
línea base.

---

## 7. Reversión / rollback  ·  `02·F14` Q11

Se revierte descartando el commit.

---

## 8. Producción y migración incremental  ·  `02·F14` Q12

**Nada que desplegar.** Lo que cambia es que el número deja de contar cinco
historias como mudas.

---

## 9. Reglas del estándar aplicadas  ·  `02·F14` Q13

- `20·M11`, lo cerrado no se reescribe: se arregla quien lo lee.
- `04·R4`, se ejecuta en vez de afirmar sobre lo leído.
- `08·T5`, las pruebas corren y se reporta el número.

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que el lector tome la fila de un criterio por el veredicto | Daría por cumplida una fase que no lo está: la mentira peor | `T-03` lo prueba | Cerrado |
| B-02 | Que la línea base se mueva al abrir la fase | `S-053` | Está anotada en el §2.0 | Cerrado |

---

## 11. Definition of Done

- [x] Las cinco, leídas antes de tocar nada
- [x] El lector, ampliado
- [x] Las 35 pruebas de la clase en verde
- [ ] Autorizado el commit por el usuario

---

## 12. Seguimiento diario

El avance en vivo va en el [estado-fase.md](estado-fase.md) §1.2.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
