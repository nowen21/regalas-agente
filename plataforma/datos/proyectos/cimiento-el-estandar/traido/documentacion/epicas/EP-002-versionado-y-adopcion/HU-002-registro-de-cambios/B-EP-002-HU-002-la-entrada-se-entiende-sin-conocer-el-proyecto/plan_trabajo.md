# Plan de Trabajo — Fase B-EP-002-HU-002-la-entrada-se-entiende-sin-conocer-el-proyecto

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-002-HU-002-la-entrada-se-entiende-sin-conocer-el-proyecto` |
| **Épica / HU** | [EP-002](../../epica.md) · [HU-002](../HU-002-registro-de-cambios.md) |
| **Módulo** | El registro de cambios |
| **Fecha apertura** | 2026-08-18 |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 🐛 **Defecto**, y encontrado ejecutando el `CA-03` de la propia historia.

**De dónde sale:** se le mostró al usuario la entrada de la `15.2.0` y respondió **«no entendí nada»**.

---

## 1. Objetivo y alcance

Que la entrada del registro se entienda sin haber seguido el trabajo, que es lo que el `CA-03` exige desde que la historia se escribió y **nunca se había comprobado con un lector de verdad**.

**Fuera de alcance: reescribir las 83 entradas anteriores.** [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md) dice que un cambio de norma no reabre lo cerrado. Lo que urgía era que la próxima naciera legible.

---

## 2. Línea base

**Medido el 2026-08-18 sobre las 83 entradas:**

| | |
|---|---:|
| Citan una ruta de archivo | **74** |
| Citan un identificador de regla | **43** |
| Con dos marcas de jerga o menos | **0** |

**No era una entrada mala: eran todas.** Están escritas para quien ya trabaja adentro.

### 2.1 Archivos que se tocan

| Archivo | Qué |
|---|---|
| `base/20-meta-reglas/reglas/M17-…md` | La regla, con su checklist |
| `base/20-meta-reglas/base.md` · `validadores/reglas-validables.md` | Índice y clasificación |
| `validadores/metareglas.py` | La comprobación |
| `validadores/tests/test_la_entrada_del_registro_se_entiende.py` | Los casos |
| `CHANGELOG.md` · `VERSION` | **MENOR** |

### 2.6 Decisiones

| Decisión | Por qué |
|---|---|
| La regla va al capítulo **`20`** y no al `00` | Escribir para que se entienda ya lo pide `00·ID7`; esta fija **la forma de un documento concreto**, y el dueño del registro es `M10` (fila 4) |
| Se comprueba **el primer párrafo**, no la entrada entera | El detalle con identificadores y rutas es útil, y sacarlo empobrece. Lo que se arregla es **por dónde abre** |
| Se comprueba **solo la versión vigente** | Reportar las 83 sepultaría la única que se puede arreglar |
| Se cuenta lo mecánico, no la comprensión | Que se entienda lo decide quien lee. Lo que se cuenta es lo que la volvía ilegible |

### 2.7 Dudas

Ninguna: la prueba la contestó el usuario.

---

## 3. Tareas

| ID | Tarea |
|---|---|
| T-01 | Correr la prueba del `CA-03` con un lector real |
| T-02 | Medir las 83 entradas |
| T-03 | Escribir `M17` con su checklist, indexarla y clasificarla |
| T-04 | La comprobación y sus casos |
| T-05 | Reescribir la entrada vigente y versionar |

---

## 5. Verificación

| Qué | Cómo | Estado |
|---|---|---|
| `CA-03` · se entiende sin haber seguido | Prueba con lector real | ☑ salió **No cumple**, y de ahí sale todo |
| La entrada vigente abre en llano | `validar.py metareglas` | ☑ |
| El detalle no se pierde | El identificador y la ruta siguen, más abajo | ☑ |
| No regresión | Las dos suites | ☑ |

---

## 7. Reversión

Volviendo el commit atrás.

---

## 9. Reglas aplicadas

[`00·ID7`](../../../../../base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md), [`20·M5`](../../../../../base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md), [`20·M14`](../../../../../base/20-meta-reglas/reglas/M14-ninguna-regla-nace-fuera-del-procedimiento.md).

---

## 10. Riesgos

| ID | Riesgo | Acción | Estado |
|---|---|---|---|
| B-01 | Que sacar la jerga empobrezca la entrada | Solo se mueve: el detalle baja, no desaparece | **Cerrado** |
| B-02 | Que la comprobación reporte las 83 y se apague | Solo la versión vigente. Con caso | **Cerrado** |
| B-03 | Dar por comprobada la comprensión con un programa | **No se comprueba.** Se cuenta lo mecánico y está dicho | **Cerrado** |

---

## 11. Definition of Done

- [x] `M17` escrita, indexada, clasificada y en CUMPLE
- [x] La comprobación con sus diez casos
- [x] La entrada vigente reescrita, y la 23.8.0 también
- [x] Versionada
- [ ] Aceptada por el usuario

---

## 13. Cierre

En el [funcionalidad_implementada.md](funcionalidad_implementada.md).
