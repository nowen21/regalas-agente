# Plan de Trabajo — Fase B-EP-005-HU-001-la-transcripcion-duplicada-del-15

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-005-HU-001-la-transcripcion-duplicada-del-15` |
| **Épica / HU** | [EP-005](../../epica.md) · [HU-001](../HU-001-transcripcion-de-la-sesion.md) |
| **Módulo** | Transcripción de la sesión |
| **Fecha apertura** | 2026-08-18 |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 🐛 **Defecto.** Punto 1 del [pendiente 29](../../../../../pendientes/hecho/la-transcripcion-duplicada-del-15.md), el único que quedaba.

---

## 1. Objetivo y alcance

Dejar legible la transcripción del 2026-08-15, que quedó escrita dos veces: el enganche con la hora del reloj, y el agente además a mano con horas estimadas.

**Fuera de alcance:** las otras transcripciones. Las cuatro copias a mano que aparecieron el 2026-08-16 ya se borraron, y el defecto de origen —que el `CLAUDE.md` pidiera escribirla a mano— se cerró ese mismo día.

---

## 2. Línea base

**Medido el 2026-08-18:** 57 bloques de usuario para una sesión de unos treinta mensajes. 32 llevan la marca del enganche; 25, no.

### 2.1 Archivos que se tocan

`historico-chat/2026-08-15-la-plantilla-del-resultado-de-pruebas.md` y `pendientes/29-…md`.

### 2.6 Decisiones

| Decisión | Por qué |
|---|---|
| **No se aplica lo que el pendiente decía** | Borrar todo lo que no lleva la marca destruía **dieciséis mensajes reales del usuario** |
| Se quitan solo los **duplicados literales** | Nueve bloques repetidos palabra por palabra en otro que sí lleva marca |
| Los 16 sin pareja **se quedan**, aunque no lleven marca | Son mensajes que el enganche no escribió, o escribió sin marca. No se sabe cuál, y borrarlos pierde lo dicho |
| Se deja una nota arriba | **Las horas no se pueden leer en orden**, y quien abra el archivo tiene que saberlo antes de fiarse de ellas |

### 2.7 Dudas

Ninguna. La medición resolvió la única que había.

---

## 3. Tareas

| ID | Tarea |
|---|---|
| T-01 | Contar los bloques y separar los que llevan marca |
| T-02 | Ver cuáles de los sin marca están repetidos, y cuáles no |
| T-03 | Quitar los duplicados literales y renumerar |
| T-04 | La nota de cabecera, y el pendiente al día |

---

## 4. Secuencia

**T-02 antes que T-03**, y es lo que salvó el archivo: sin medir, T-03 habría borrado los 25.

---

## 5. Verificación

| Qué | Cómo | Estado |
|---|---|---|
| Ningún mensaje del usuario se pierde | Cada bloque quitado tiene su gemelo con marca | ☑ |
| El archivo queda numerado seguido | 1 a 48 | ☑ |
| Sin enlaces rotos | `validar.py estandar` | ☑ |

---

## 7. Reversión

Volviendo el commit atrás. El archivo entero está en el historial.

---

## 9. Reglas aplicadas

[`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md).

---

## 10. Riesgos

| ID | Riesgo | Acción | Estado |
|---|---|---|---|
| B-01 | Borrar un mensaje del usuario | **Casi pasa.** Solo se quitan los que tienen gemelo literal | **Cerrado** |
| B-02 | Que las horas se lean como si fueran del reloj | La nota de cabecera lo dice | **Cerrado** |

---

## 11. Definition of Done

- [x] Nueve duplicados quitados, 48 bloques renumerados
- [x] Ningún mensaje del usuario perdido
- [x] La nota que advierte de las horas
- [ ] Aceptada por el usuario

---

## 13. Cierre

En el [funcionalidad_implementada.md](funcionalidad_implementada.md).
