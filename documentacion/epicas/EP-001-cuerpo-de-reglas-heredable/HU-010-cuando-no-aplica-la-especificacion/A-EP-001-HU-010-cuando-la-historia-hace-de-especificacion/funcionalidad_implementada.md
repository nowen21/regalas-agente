# Funcionalidad implementada — Fase «A-EP-001-HU-010-cuando-la-historia-hace-de-especificacion»   ·   `[CAPA 3]`

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-001-HU-010-cuando-la-historia-hace-de-especificacion` |
| **Épica / HU** | [EP-001](../../epica.md) · [HU-010](../HU-010-cuando-no-aplica-la-especificacion.md) |
| **Versión** | 23.9.0 → **23.10.0** (MENOR) |
| **Fecha de cierre** | 2026-08-18 |

---

## 1. Qué quedó

[`02·F2`](../../../../../base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md) dice ahora de qué está hecha la especificación cuando lo que se construye no es código:

> **Si el entregable no es código, la especificación es la historia con sus criterios de aceptación.**

Cierra el [pendiente 20](../../../../../pendientes/hecho/cuando-la-historia-hace-de-especificacion.md).

---

## 2. No es una excepción, y esa es la decisión

El pendiente dejaba dos caminos, y la diferencia no es de forma:

> **Una excepción dice cuándo la regla no rige. Esto dice dónde vive lo que la regla exige.**

Con el camino elegido, `F2` sigue exigiendo especificación acordada **en todos los casos**. Lo único que cambia es de qué está hecha cuando el entregable es texto normativo, documentación o un programa corto.

**Y `F2` ya tenía una excepción.** Abrirle la segunda a una regla que ya trae una es la puerta que después nadie cierra: `08·T1` es el ejemplo vivo — su excepción deja al agente autorizándose a sí mismo a no probar.

---

## 3. Lo que ordena

Dos fases de este repositorio se habían abierto declarando que no tienen especificación aparte porque su entregable es texto normativo. **Hasta hoy eso era un incumplimiento silencioso de `F2`; ahora es lo que la regla dice.**

---

## 4. Qué se tocó

| Archivo | Qué |
|---|---|
| `base/02-flujo-de-trabajo/reglas/F2-…md` | La frase nueva, y el checklist reaplicado — 294 caracteres, entra en el molde |
| `pendientes/20-…md` | Cerrado |
| `CHANGELOG.md` · `VERSION` | 23.10.0 |

**Se acortó la primera frase para que quepa**, y se fue *«sin especificación, el código es opinión del agente»*: es el porqué, y su sitio es `notas/`.
