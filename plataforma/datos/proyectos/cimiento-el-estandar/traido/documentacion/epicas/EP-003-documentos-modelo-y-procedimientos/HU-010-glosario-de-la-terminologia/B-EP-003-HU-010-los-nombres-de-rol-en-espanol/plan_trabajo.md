# Plan de Trabajo — Fase B-EP-003-HU-010-los-nombres-de-rol-en-espanol

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-003-HU-010-los-nombres-de-rol-en-espanol` |
| **Épica / HU** | [EP-003](../../epica.md) · [HU-010](../HU-010-glosario-de-la-terminologia.md) |
| **Módulo** | Terminología del estándar |
| **Fecha apertura** | 2026-08-18 |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 🐛 **Defecto.** Segunda mitad del [pendiente 21](../../../../../pendientes/hecho/los-nombres-de-rol-en-espanol.md); la fase `A` entregó el glosario y dejó el inventario de lo que faltaba traducir.

---

## 1. Objetivo y alcance

Que ningún término con traducción usada quede en inglés en lo que se hereda. [`01·C20`](../../../../../base/01-conducta.md#c20--la-palabra-de-otro-idioma-se-traduce-y-si-no-se-puede-se-explica) lo pide desde el 2026-08-14.

**Fuera de alcance:** los doce términos sin traducción usada —commit, push, endpoint, log, stack— que el glosario ya declara y explica. Y la carpeta `skills/generar-spec-modulo/`: el nombre de una skill es **cómo se la invoca**, así que renombrarla cambia comportamiento y no solo texto.

---

## 2. Línea base

**Medido el 2026-08-18**, sobre el inventario que dejó la fase `A`: trece nombres de rol y la palabra «spec», en `base/`, `plantillas/`, `skills/` y `notas/`.

### 2.1 Archivos que se tocan

| Archivo | Qué |
|---|---|
| `base/00-identidad-y-rol/reglas/ID6-…md` | Los nombres en el cuerpo, y **resellar su checklist** |
| `base/glosario.md` | La tabla de «falta traducirlos» pasa a lo hecho |
| `plantillas/`, `skills/`, `notas/` | El texto |
| Cuatro archivos | Renombrados: `02·F2`, `13·DOC3`, `13·DOC6` y la plantilla de especificación |
| `CHANGELOG.md` · `VERSION` | **MENOR** |

### 2.6 Decisiones

| Decisión | Por qué |
|---|---|
| El reemplazo va **de más largo a más corto** | «Épica Writer» antes que cualquier «Writer» suelto |
| Con borde de palabra | Para no tocar rutas ni palabras que contengan el término |
| Los nombres de archivo se apartan antes de traducir el texto | Si no, `plantilla-spec-modulo.md` se convierte en un nombre que no existe |
| Renombrar va con [`cerrar.mover`](../../../../../validadores/cerrar.py) | Arrastra las citas; a mano son 149 enlaces |
| La carpeta de la skill **no se toca** | Su nombre es cómo se la invoca |

### 2.7 Dudas

Ninguna. El glosario ya traía qué se traduce y qué no, con su motivo.

---

## 3. Tareas

| ID | Tarea |
|---|---|
| T-01 | Los trece nombres de rol, en texto |
| T-02 | «spec» en texto, apartando los nombres de archivo |
| T-03 | Renombrar los cuatro archivos con `cerrar.mover` |
| T-04 | Las referencias que `mover` no resuelve — las que llevan `«RUTA-ESTANDAR»` |
| T-05 | Resellar `ID6`, actualizar el glosario, versionar |

---

## 4. Secuencia

**T-01 → T-02 → T-03 → T-04.** El texto antes que los nombres de archivo: al revés, el reemplazo de texto rompe las rutas que acaban de cambiar.

---

## 5. Verificación

| Qué | Cómo | Estado |
|---|---|---|
| Ningún término del inventario queda en inglés | Búsqueda con borde de palabra | ☑ |
| Ningún enlace roto | `validar.py estandar` | ☑ |
| `ID6` con su checklist al día | `validar.py metareglas` | ☑ |
| No regresión | Las dos suites | ☑ |

---

## 7. Reversión

Volviendo el commit atrás.

---

## 9. Reglas aplicadas

[`01·C20`](../../../../../base/01-conducta.md#c20--la-palabra-de-otro-idioma-se-traduce-y-si-no-se-puede-se-explica), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md).

---

## 10. Riesgos

| ID | Riesgo | Acción | Estado |
|---|---|---|---|
| B-01 | Que un renombre rompa las citas | `cerrar.mover` las arrastra | **Cerrado** |
| B-02 | Que el reemplazo toque rutas | Los nombres de archivo se apartan antes | **Cerrado** |
| B-03 | Que `ID6` quede con el sello anulado | Reaplicado, 284 caracteres, sigue en CUMPLE | **Cerrado** |
| B-04 | Las referencias con `«RUTA-ESTANDAR»` | **Pasó:** ocho enlaces rotos que `mover` no ve. A mano | **Cerrado** |

---

## 11. Definition of Done

- [x] Los trece nombres y «spec», traducidos
- [x] Los cuatro archivos renombrados, sin enlaces rotos
- [x] `ID6` resellada · glosario al día · versionada
- [ ] Aceptada por el usuario

---

## 13. Cierre

En el [funcionalidad_implementada.md](funcionalidad_implementada.md).
