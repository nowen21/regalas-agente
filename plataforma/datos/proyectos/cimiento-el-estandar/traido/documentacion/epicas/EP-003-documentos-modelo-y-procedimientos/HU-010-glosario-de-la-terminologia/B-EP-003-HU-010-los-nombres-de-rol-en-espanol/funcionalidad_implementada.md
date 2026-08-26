# Funcionalidad implementada — Fase «B-EP-003-HU-010-los-nombres-de-rol-en-espanol»   ·   `[CAPA 3]`

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-003-HU-010-los-nombres-de-rol-en-espanol` |
| **Épica / HU** | [EP-003](../../epica.md) · [HU-010](../HU-010-glosario-de-la-terminologia.md) |
| **Versión** | 23.7.5 → **23.8.0** (MENOR) |
| **Fecha de cierre** | 2026-08-18 |

---

## 1. Qué quedó

Ningún término con traducción usada queda en inglés en lo que se hereda: **211 apariciones en 39 archivos**, y cuatro archivos renombrados con sus **149 citas arrastradas**.

Era la segunda mitad del [pendiente 21](../../../../../pendientes/hecho/los-nombres-de-rol-en-espanol.md), abierta desde el 2026-08-14. La fase `A` había entregado el glosario y dejado el inventario; esta lo ejecutó.

[`00·ID6`](../../../../../base/00-identidad-y-rol/reglas/ID6-toma-el-rol-especializado-que-pide-la-etapa.md) se reselló: editar el texto de una regla anula su checklist **aunque el cambio sea de idioma**.

---

## 2. El orden importaba

Primero el texto, después los nombres de archivo. Al revés, el reemplazo de texto rompe las rutas que acaban de cambiar — y por eso el reemplazo aparta los nombres de archivo antes de tocar nada.

---

## 3. Lo que no hace

- **La carpeta `skills/generar-spec-modulo/` no se toca.** El nombre de una skill es **cómo se la invoca**: renombrarla cambia comportamiento, no solo texto.
- **Los doce términos sin traducción usada se quedan** —commit, push, endpoint, log, stack— y el glosario ya dice por qué cada uno.
- **El arrastre de citas no ve las rutas con `«RUTA-ESTANDAR»`.** Dejó ocho enlaces rotos que hubo que arreglar a mano, y va a volver a pasar en el próximo renombre.
