# Plan de Trabajo — Fase E-EP-001-HU-009-las-que-solo-sobraban-de-largo (módulo Cuerpo de reglas)

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden y sobre qué archivos. El requisito vive en [HU-009](../HU-009-reglas-sin-checklist-al-dia.md); las pruebas, en el [plan_pruebas.md](plan_pruebas.md).

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `E-EP-001-HU-009-las-que-solo-sobraban-de-largo` |
| **Épica** | [EP-001 Cuerpo de reglas heredable](../../epica.md) |
| **HU** | [HU-009 Poner al día las reglas que no pasan su propio checklist](../HU-009-reglas-sin-checklist-al-dia.md) — una sola ([`02·F12.1`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) |
| **Módulo** | Cuerpo de reglas — la fila 10 del checklist |
| **Fecha apertura** | 2026-08-18 |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 🐛 **Defecto.** Quinta fase de la historia.

**De dónde sale:** el [pendiente 19](../../../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md), categoría *«acortar — sobra explicación, no exigencia»*, que es la mayor de las ocho.

**CA que cubre:** el `CA-01` sobre reglas que reprueban **solo la fila 10**, y el transversal de no regresión.

---

## 1. Objetivo y alcance

**Objetivo:** que las reglas cuyo **único** defecto es el largo pasen a CUMPLE sin que cambie una sola exigencia.

**El corte es el que hace la fase posible.** De las 70 que reprueban, **quince fallan solo la fila 10**: no hay que partirlas, ni derogarlas, ni decidir nada — solo sobra texto. Es el trabajo más grande del pendiente 19 y **el único que no depende de una decisión del usuario**.

**Lo que sobra es el porqué, y ya tiene sitio.** [`20·M5`](../../../../../base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md) lo dice en la propia fila 10: *si no cabe, o son dos reglas, o se está contando el porqué —que va a `notas/`—*. En las diez de esta fase era lo segundo.

**Fuera de alcance — cinco de las quince:**

| Regla | Por qué no |
|---|---|
| `03·D8` (1962) · `04·S9` (1278) · `04·S10` (1029) | Lo que sobra es **un procedimiento**, no una explicación: el caso de anexo, que pide convertir el capítulo en carpeta |
| `05·E4` (419) | Su sello ya decidió que la escala de cuatro niveles **se va a un anexo** |
| `02·F13` (549) | Se reescribió hace días y conviene no volver a tocarla en la misma semana |

**Y `04·S9` tiene un motivo propio para no tocarse hoy:** es **el único modelo de excepción completa del cuerpo** —condición, límite y autorizador—, y su sello advierte que al acortarla eso es lo único que hay que preservar entero. Acortarla de paso, entre otras nueve, es la forma de perderlo.

---

## 2. Análisis previo — línea base verificada

**Medido el 2026-08-18, después de las fases `B`, `C` y `D`:**

| Qué | Cuánto |
|---|---|
| Reglas en NO CUMPLE | 70 |
| Que reprueban **solo** la fila 10 | **15** |
| De esas, puro exceso de explicación | **10** |

| Regla | Antes | Sobraba |
|---|---:|---:|
| `01·C13` | 802 | 482 |
| `01·C19` | 533 | 213 |
| `01·C12` | 462 | 142 |
| `01·C11` | 461 | 141 |
| `04·S1` | 437 | 117 |
| `09·G7` | 421 | 101 |
| `17·I1` | 395 | 75 |
| `03·D3` | 378 | 58 |
| `04·S2` | 349 | 29 |
| `09·G9` | 552 | 232 |

### 2.1 Archivos que se crean o modifican

| Archivo | Tipo | Nota |
|---|---|---|
| `base/01-conducta.md` | Modificar | `C11`, `C12`, `C13`, `C19` |
| `base/03-datos.md` | Modificar | `D3` |
| `base/04-seguridad.md` | Modificar | `S1`, `S2` |
| `base/09-git.md` | Modificar | `G7`, `G9` |
| `base/17-interfaz.md` | Modificar | `I1` |
| `pendientes/19-…md` | Modificar | Lo que esta fase cierra |
| `CHANGELOG.md` · `VERSION` | Modificar | **PARCHE** |

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **Se corta el porqué, no la exigencia** | Cortar por donde más rinda | La fila 10 lo dice: si no cabe, o son dos reglas o se está contando el porqué. En las diez era lo segundo |
| Lo que estaba entre paréntesis **enumerando** se va | Conservarlo | Enumerar dónde comprobar o qué cuenta como dato de afuera es ejemplo, y para eso está el bloque INCORRECTO/CORRECTO — que **no cuenta** para la fila 10 |
| **Las excepciones no se tocan** | Acortarlas también | Es lo único de una regla que no se puede resumir sin cambiar qué permite. La de `G9` conserva condición y límite |
| Se resella **con el largo remedido**, no estimado | Escribir el número al ojo | Ya pasó en esta historia: un sello que cita un número sin remedirlo hereda el error de quien midió antes |
| Cada sello dice **qué se fue** | Decir solo que se acortó | Quien lea dentro de un año necesita saber si lo que falta se perdió o se movió |

### 2.7 Dudas por resolver antes de escribir

**Ninguna.** El criterio de qué se corta lo da la propia fila 10.

---

## 3. Desglose de tareas

| ID | Tarea | Est. |
|---|---|:--:|
| T-01 | Listar las que reprueban **solo** la fila 10, por programa | 0,25 h |
| T-02 | Separar las diez de redacción de las cinco de anexo | 0,25 h |
| T-03 | Reescribir las diez | 2 h |
| T-04 | Medir, y volver a cortar las que sigan pasadas | 0,5 h |
| T-05 | Resellar las diez con el largo remedido | 0,75 h |
| T-06 | Versionar y anotar en el 19 | 0,25 h |

**Total estimado:** 4 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-03 → T-04 → T-05.

**T-04 no es un trámite: es el trabajo.** La primera reescritura dejó **cinco de las diez todavía pasadas**, y una de ellas necesitó tres pasadas. Escribir corto no sale a la primera, y el sello no se puede firmar hasta que el número lo diga.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación

| CA | Método | Estado |
|---|---|---|
| CA-01 · las diez pasan a CUMPLE | `validar.py metareglas` | ☑ |
| Ninguna exigencia se pierde | Lectura punto por punto, antes y después | ☑ |
| El conteo baja exactamente diez | 70 → 60 | ☑ |
| No regresión | Las dos suites | ☑ |

---

## 6. Datos y ambiente de prueba

El propio cuerpo de reglas.

---

## 7. Reversión / rollback

Se revierte volviendo el commit atrás.

---

## 8. Producción y migración incremental

**Aditiva.** Ninguna exigencia cambia: un proyecto al día no tiene que hacer nada.

---

## 9. Reglas del estándar aplicadas

[`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), [`20·M5`](../../../../../base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md), [`20·M8`](../../../../../base/20-meta-reglas/reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo | Acción | Estado |
|---|---|---|---|
| B-01 | Cortar una exigencia creyendo que era explicación | Punto por punto, antes y después. En `D3` los tres puntos siguen; en `S1`, los tres; en `I1`, los tres estados | **Cerrado** |
| B-02 | Tocar una excepción y cambiar qué permite | No se tocan. La de `G9` conserva condición y límite | **Cerrado** |
| B-03 | Firmar el sello con un largo estimado | Se remide después de cada corte. Cinco de las diez necesitaron una segunda pasada | **Cerrado** |
| B-04 | Que acortar deje la regla oscura para quien no conoce el tema | **Se acepta y se dice:** lo que se fue es el porqué, y su sitio es `notas/`. Ninguna nota se escribió en esta fase | Abierto |

---

## 11. Definition of Done

- [x] Las diez en CUMPLE, con el largo remedido
- [x] Ninguna exigencia perdida
- [x] El conteo del cuerpo baja exactamente diez
- [x] Versionada
- [ ] Aceptada por el usuario
- [ ] **Falta:** las notas de `notas/` con el porqué que se sacó

---

## 13. Cierre

**No se escribe acá.** Vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md).
