# Plan de Trabajo — Fase D-EP-001-HU-009-enlazar-en-vez-de-repetir (módulo Cuerpo de reglas)

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden y sobre qué archivos. El requisito vive en [HU-009](../HU-009-reglas-sin-checklist-al-dia.md); las pruebas, en el [plan_pruebas.md](plan_pruebas.md).

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `D-EP-001-HU-009-enlazar-en-vez-de-repetir` |
| **Épica** | [EP-001 Cuerpo de reglas heredable](../../epica.md) |
| **HU** | [HU-009 Poner al día las reglas que no pasan su propio checklist](../HU-009-reglas-sin-checklist-al-dia.md) — una sola ([`02·F12.1`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) |
| **Módulo** | Cuerpo de reglas — la fila 11 del checklist |
| **Fecha apertura** | 2026-08-18 |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 🐛 **Defecto.** Fase `D` de la historia; las tres anteriores cerraron el `CA-02`, los sellos y la fila 5.

**De dónde sale:** el [pendiente 19](../../../../../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md), categoría *«dejar de repetir al vecino»*.

**CA que cubre:** el `CA-01` sobre reglas que reprueban **la fila 11**, y el transversal de no regresión.

---

## 1. Objetivo y alcance

**Objetivo:** que las dos reglas que **enlazaban y además copiaban** a su vecina se queden solo con lo suyo.

**La fila 11 no pide enlazar: pide enlazar *en vez de* copiar.** Las dos cumplían la mitad fácil —el enlace estaba puesto— y por eso el defecto se leía como correcto. Un enlace delante de un texto repetido parece diligencia.

**Fuera de alcance:**

- **`12·PR3`.** No exige nada propio: sus cuatro frases remiten al capítulo `04`. O se queda con lo que `04` no dice, **o se deroga**, y eso lo decide quien define el estándar.
- **`01·C16`.** También repite —a `01·C2`, y lo admite por escrito—, pero su arreglo pasa por normalizar el bloque `Encadenamiento` en cuatro reglas a la vez, no por retocar una.
- **`04·S7` y `10·DEP3`.** El arreglo que sus propios sellos prescriben es **derogar `S7`**, y una derogación obliga a adoptarla ([`02·F22`](../../../../../base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md)): eso es del usuario, no de esta fase.

---

## 2. Análisis previo — línea base verificada

**Medido el 2026-08-18:**

| Regla | Repetía a | Qué era suyo |
|---|---|---|
| [`07·Q7`](../../../../../base/07-calidad-de-codigo.md#q7--deja-el-código-mejor-pero-en-tu-alcance) | [`01·C3`](../../../../../base/01-conducta.md#c3--quédate-en-tu-tarea) | una frase: decirlo y dejarlo para su tarea |
| [`12·PR4`](../../../../../base/12-privacidad-datos.md#pr4--no-los-expongas-en-logs-errores-ni-mensajes) | [`05·E5`](../../../../../base/05-errores-y-logging.md#e5--nunca-registres-secretos-ni-datos-sensibles), que a su vez reformula [`00·N6`](../../../../../base/00-nucleo-blindado.md#n6--secretos-y-datos-sensibles-nunca-se-exponen-blindada) | pantallas y reportes, que `E5` no cubre |

**`Q7` tenía su modelo al lado, en el mismo cuerpo.** [`14·EST3`](../../../../../base/14-estructura-codigo.md#est3--respeta-el-legacy--la-convención-es-para-lo-nuevo) toma de `C3` **el mismo criterio** y está en CUMPLE: la nombra entre paréntesis como el motivo, y todo lo demás es suyo. La diferencia entre cumplir la fila 11 y no cumplirla estaba escrita, en dos reglas que se podían leer juntas.

**`PR4` eran tres capas del mismo criterio** —`N6` blindada, `E5` en errores, `PR4` en privacidad—, y lo que la salva de derogarse es la mitad que ninguna otra dice: **`E5` habla de logs, no de pantallas.**

### 2.1 Archivos que se crean o modifican

| Archivo | Tipo | Nota |
|---|---|---|
| `base/07-calidad-de-codigo.md` | Modificar | Cuerpo y sello de `Q7` |
| `base/12-privacidad-datos.md` | Modificar | Cuerpo, ejemplo y sello de `PR4` |
| `pendientes/19-…md` | Modificar | Lo que esta fase cierra |
| `CHANGELOG.md` · `VERSION` | Modificar | **PARCHE** |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| `Q7` se escribe **al molde de `EST3`** | Inventar una forma | El cuerpo ya tenía el caso resuelto, en CUMPLE y sobre la misma regla prestada |
| `PR4` **declara `depende de 05·E5`** | Dejar la relación sin declarar | Es una de las tres formas de [`20·M7`](../../../../../base/20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md). La relación existía; lo que faltaba era decirla |
| El ejemplo de `PR4` **cambia con ella** | Dejarlo | El de antes era de logs, que ya no es de esta regla. Un ejemplo que ilustra lo que la regla dejó de decir es peor que ninguno |
| **No se tocan `PR3`, `C16` ni `S7`** | Cerrar la categoría entera | Dos piden derogar —y derogar obliga a adoptar— y la tercera pide cambiar cuatro reglas a la vez |

### 2.7 Dudas por resolver antes de escribir

**Ninguna.** Las dos salidas estaban escritas en los sellos y en el análisis del 2026-08-07.

---

## 3. Desglose de tareas

| ID | Tarea | Est. |
|---|---|:--:|
| T-01 | Separar lo prestado de lo propio en las dos | 0,5 h |
| T-02 | Reescribir `Q7` al molde de `EST3` | 0,25 h |
| T-03 | Reescribir `PR4` y su ejemplo | 0,5 h |
| T-04 | Resellar las dos, remidiendo el largo | 0,5 h |
| T-05 | Versionar y anotar en el 19 | 0,25 h |

**Total estimado:** 2 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02/03 → T-04.

**T-01 es el trabajo real.** Reescribir es fácil una vez decidido qué frase es de quién; el riesgo está en quitar de más y dejar la regla sin exigencia.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación

| CA | Método | Estado |
|---|---|---|
| CA-01 · las dos dejan de repetir | `validar.py metareglas`: las dos en CUMPLE | ☑ |
| Transversal · no regresión | Las dos suites, y el conteo de NO CUMPLE baja exactamente 2 | ☑ |
| Lo que exigían se conserva | Lectura frase por frase | ☑ |

---

## 6. Datos y ambiente de prueba

El propio cuerpo de reglas.

---

## 7. Reversión / rollback

Se revierte volviendo el commit atrás.

---

## 8. Producción y migración incremental

**Aditiva.** Ninguna exigencia desaparece: lo que se fue de cada regla sigue rigiendo por la vecina que ya lo decía.

---

## 9. Reglas del estándar aplicadas

[`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), [`20·M5`](../../../../../base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md), [`20·M7`](../../../../../base/20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Acción | Estado |
|---|---|---|---|
| B-01 | Quitar de más y dejar la regla sin exigencia propia | Se separó frase por frase antes de escribir. `PR4` conserva pantallas y reportes; `Q7`, la frase de dejarlo para su tarea | **Cerrado** |
| B-02 | Que el ejemplo quede ilustrando lo que la regla ya no dice | El de `PR4` se cambió con ella | **Cerrado** |
| B-03 | Que se lea como que la exigencia desapareció | Lo que se fue sigue rigiendo por `C3` y por `E5`, y cada sello lo dice | **Cerrado** |
| B-04 | La categoría queda a medias: `PR3`, `C16` y `S7` siguen repitiendo | **Se dice, no se tapa.** Dos piden derogar y una pide cambiar cuatro reglas a la vez | Abierto — es el 19 |

---

## 11. Definition of Done

- [x] `Q7` y `PR4` sin texto prestado, en CUMPLE
- [x] `PR4` declara su dependencia en una de las tres formas
- [x] El ejemplo de `PR4` corresponde a lo que dice hoy
- [x] El conteo de NO CUMPLE baja exactamente 2
- [x] Versionada
- [ ] Aceptada por el usuario

---

## 13. Cierre

**No se escribe acá.** Vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
