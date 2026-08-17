# Plan de Pruebas — «Fase A-EP-001-HU-009: clasificar las que faltan»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de la misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-001-HU-009 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-001-HU-009-clasificar-las-que-faltan` |
| **Fecha** | 2026-08-16 |
| **Elaborado por** | El agente |
| **Aprobado por** | El usuario, en la orden de resolver los ocho pendientes `P1` |
| **Estado** | Aprobado |

> Fase de documento: se llenan las secciones **3, 5, 6, 9 y 12**.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Aceptación | Correr el validador de meta-reglas sobre el cuerpo de reglas y contar | El repositorio | Sí, el validador ya existe |

**No se escribe ninguna prueba nueva**, y es a propósito: el programa que mide esto ya está construido y es de EP-004. Escribir otra sería medir dos veces lo mismo.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Aceptación | ☑ | El `CA-02` |
| Revisión humana | ☑ | Que la clasificación no sea cómoda: el riesgo `B-01` |

### 3.3 Técnicas de diseño de casos

- **Antes y después** — el mismo validador, con el mismo comando, contando los hallazgos de «no aparece en el registro».
- **Muestreo contra el criterio** — se toman reglas de las tres listas y se comprueba que cumplen el criterio escrito del registro: *«si un script puede decir sí/no sin opinar → validable»*.

### 3.5 Alcance de la corrida

El validador de meta-reglas sobre `base/`. Ninguna otra suite se toca.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-009 | CA-02 | [CP-001](#cp-001--ninguna-regla-queda-fuera-del-registro) | Aceptación | Alta | Sí | ☐ |
| HU-009 | CA-02 · calidad | [CP-002](#cp-002--la-clasificación-aguanta-el-criterio-escrito) | Revisión | Alta | No | ☐ |
| HU-009 | CA-02 · límites | [CP-003](#cp-003--los-capítulos-opcionales-también-cuentan) | Aceptación | Media | Sí | ☐ |

**Cobertura:** 1 de 1 CA del alcance = 100%.

---

## 6. Casos de prueba

### CP-001 — Ninguna regla queda fuera del registro

| Campo | Valor |
|---|---|
| **HU / CA** | HU-009 / CA-02 |
| **Tipo** | Aceptación |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | El cuerpo de reglas de este repositorio |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Contar los hallazgos de «no aparece en el registro» antes | 33 |
| 2 | Clasificar las 33 | — |
| 3 | Volver a contar | **Cero** |
| 4 | Comprobar que el total de hallazgos bajó en 33 y no en otra cantidad | Bajó exactamente 33 |

**Resultado esperado final:** ninguna regla queda fuera.

> **El paso 4 no sobra.** Si el número total bajara de más, algo se rompió; si bajara de menos, alguna quedó mal escrita y el validador no la reconoce.

---

### CP-002 — La clasificación aguanta el criterio escrito

| Campo | Valor |
|---|---|
| **HU / CA** | HU-009 / CA-02 · calidad |
| **Tipo** | Revisión humana |
| **Prioridad** | Alta |
| **Precondiciones** | El CP-001 pasó |
| **Datos de entrada** | Una muestra de las tres listas |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tomar tres marcadas «no validable» y preguntarse si un script podría decidirlas sin opinar | No podría |
| 2 | Tomar todas las marcadas «validable, falta» y leer qué dice que le falta | Cada una lo dice, y es concreto |
| 3 | Tomar las marcadas «ya son validadores» y buscar el programa que las comprueba | Existe y se puede nombrar |

**Resultado esperado final:** la clasificación no se hizo por comodidad.

> **Es el riesgo `B-01`.** Marcar todo como «no validable» vacía el pendiente 01 sin haber construido nada.

---

### CP-003 — Los capítulos opcionales también cuentan

| Campo | Valor |
|---|---|
| **HU / CA** | HU-009 / CA-02 · límites |
| **Tipo** | Aceptación |
| **Prioridad** | Media |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Los capítulos `18` y `19` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar en el registro una regla del `18` | Está |
| 2 | Buscar una del `19` | Está |

**Resultado esperado final:** ser opcional no exime de aparecer. Es lo que las volvió invisibles.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Alta** | Que el validador siga reportando alguna sin clasificar | Inmediato — está mal escrita la fila |
| **Alta** | Clasificar como «no validable» algo que sí se puede comprobar | Inmediato — el registro mentiría hacia el lado cómodo |
| **Media** | Que el conteo del principio no cuadre con las listas | Antes de cerrar |

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Reglas sin clasificar | 33 → **0** |
| Cada 🟡 dice qué le falta | 100% |
| Reglas cuyo texto se tocó | **0** — esta fase no cambia ninguna regla |

El veredicto va en el `resultado_pruebas.md` de esta fase.
