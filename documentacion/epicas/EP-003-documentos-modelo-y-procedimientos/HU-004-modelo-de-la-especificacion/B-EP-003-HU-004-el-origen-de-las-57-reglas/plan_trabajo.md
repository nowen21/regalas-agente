# Plan de Trabajo — Fase B-EP-003-HU-004-el-origen-de-las-57-reglas

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-003-HU-004-el-origen-de-las-57-reglas` |
| **Épica / HU** | [EP-003](../../epica.md) · [HU-004](../HU-004-modelo-de-la-especificacion.md) |
| **Módulo** | Las dos especificaciones de esta casa |
| **Fecha apertura** | 2026-08-18 |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 🐛 **Defecto.** El [pendiente 47](../../../../../pendientes/47-las-reglas-de-negocio-del-estandar-no-dicen-de-donde-bajan.md), que salió de correr por primera vez el validador del 43 sobre esta casa.

---

## 1. Objetivo y alcance

Que cada regla de negocio de las dos especificaciones diga **de qué historia baja**, con el identificador que un programa puede seguir.

**Fuera de alcance — y es la parte incómoda del pendiente:** decidir que una regla **no hace falta y se borra**. El pendiente dice que alguna seguramente no la pidió nadie, y eso es cierto; pero borrar una regla vigente quita algo del estándar, y esa decisión no es del agente.

---

## 2. Línea base

**Medido el 2026-08-18:** 57 reglas sin origen, no 31. El pendiente contó el 2026-08-16; desde entonces se escribieron más.

| Especificación | Sin origen |
|---|---:|
| `documentacion/automatismos/spec.md` | 30 |
| `documentacion/documentos-modelo/spec.md` | 27 |

**El origen ya estaba escrito, pero una vez por sección y no por regla.** Cada `### 4.N` declara en qué fase se escribió, así que **la procedencia no hubo que inventarla: hubo que bajarla de la sección a la regla.**

### 2.1 Archivos que se tocan

Las dos especificaciones, y `pendientes/47-…md`.

### 2.6 Decisiones

| Decisión | Por qué |
|---|---|
| El origen se saca **del propio documento** | Cada `### 4.N` ya dice de qué fase salió. Inventarlo sería justo lo que la regla del 43 vino a impedir |
| Las nueve primeras de cada archivo, que no tienen sección | Bajan de la historia del tramo donde viven, declarada en su §1 |
| **No se borra ninguna regla** | Es la tercera salida del pendiente y quita algo del estándar |
| Se escribe el enlace, no solo el identificador | [`20·M15`](../../../../../base/20-meta-reglas/reglas/M15-toda-cita-a-otra-regla-lleva-su-enlace.md) |

### 2.7 Dudas

Ninguna para lo que se hizo. La que queda es del usuario: **cuáles de las 57 no las pidió nadie.**

---

## 3. Tareas

| ID | Tarea |
|---|---|
| T-01 | Medir cuántas son hoy, por archivo |
| T-02 | Sacar de cada `### 4.N` la historia de la que baja |
| T-03 | Escribir el origen en cada regla que no lo tenga |
| T-04 | Comprobar que el validador da cero, y anotar en el 47 lo que no se hizo |

---

## 5. Verificación

| Qué | Cómo | Estado |
|---|---|---|
| Ninguna regla sin origen | `plantillas.reglas_sin_origen` | ☑ 0 y 0 |
| El origen no se inventó | Cada uno sale de la sección que ya lo declaraba | ☑ |
| Sin enlaces rotos | `validar.py estandar` | ☑ |
| No regresión | Las dos suites | ☑ |

---

## 7. Reversión

Volviendo el commit atrás.

---

## 9. Reglas aplicadas

[`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), [`20·M15`](../../../../../base/20-meta-reglas/reglas/M15-toda-cita-a-otra-regla-lleva-su-enlace.md).

---

## 10. Riesgos

| ID | Riesgo | Acción | Estado |
|---|---|---|---|
| B-01 | Inventar un origen para que el validador calle | El origen sale del propio documento, sección por sección | **Cerrado** |
| B-02 | Dar por buenas 57 reglas que nadie pidió | **No se resuelve acá y se dice.** Que una regla tenga procedencia no la vuelve necesaria | Abierto — es del usuario |

---

## 11. Definition of Done

- [x] Las 57 con su origen y su enlace
- [x] El validador en cero sobre las dos especificaciones
- [ ] Aceptada por el usuario
- [ ] **Falta la decisión:** cuáles de las 57 no las pidió nadie

---

## 13. Cierre

En el [funcionalidad_implementada.md](funcionalidad_implementada.md).
