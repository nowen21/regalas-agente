# Funcionalidad implementada — Fase «A-EP-005-HU-011-donde-termina-el-estandar»   ·   `[CAPA 3]`

| Campo | Valor |
|---|---|
| **Épica / HU** | [EP-005](../../epica.md) · [HU-011](../HU-011-donde-termina-el-estandar.md) |
| **Versión** | 23.16.0 · **Cierre** 2026-08-18 |

---

## 1. Qué quedó

**El mapa de qué sobrevive si mañana el agente es otro**, y la comprobación de que no envejezca:

- [`anatomia/que-esta-amarrado-a-la-herramienta.md`](../../../../../anatomia/que-esta-amarrado-a-la-herramienta.md) — **54 piezas: 18 amarradas, 36 libres**, todas por su nombre.
- [`validadores/amarre.py`](../../../../../validadores/amarre.py), en `validar.py amarre`.

---

## 2. Lo que contesta, y no se podía contestar antes

**Si el usuario deja esta herramienta, ¿qué se cae?** Se cae el adaptador: los ocho `hook_*` y `instalar.py`, que los enchufa. **Se queda todo lo demás** — las reglas son texto, y 36 de los 54 programas solo leen y escriben archivos.

---

## 3. Se comprueba por los dos lados

| Qué | Cómo se ve |
|---|---|
| Pieza que existe y el mapa no nombra | **falla** |
| Pieza que el mapa nombra y ya no existe | **aviso** |

**El segundo no lo pedía la historia.** Se agregó porque un mapa envejece de las dos formas, y uno que promete clasificar algo borrado miente igual que uno incompleto.

---

## 4. Lo que no hace

- **No mueve el adaptador a una carpeta propia** — punto 2 del [pendiente 15](../../../../../pendientes/hecho/el-estandar-depende-de-una-sola-herramienta.md).
- **No escribe el contrato** de qué necesita el estándar de cualquier agente — punto 3.
- **No dice si la clasificación es acertada.** Eso se lee.

**Ninguno de los dos primeros lo cubre un criterio de esta historia**, y por eso no se hicieron acá.
