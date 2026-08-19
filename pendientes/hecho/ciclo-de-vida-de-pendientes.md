# Hecho · Ciclo de vida de pendientes y deuda

Origen: pendiente 03. Lo que el agente **difiere** (deuda técnica, preguntas abiertas) ya tiene cierre: se registra como señal y se cierra cuando una fase lo resuelve, sobre la misma `memoria/senales.db`.

Cerrado el 2026-08-06.

---

## Qué se hizo

**Esquema (`memoria/esquema.sql` + `migrar()`)**
- `estado` admite `cerrada` (deuda/pregunta resuelta), aparte de `archivada` (poda del 02).
- Columnas `cerrada_en` (ISO date) y `cierra_ref` (commit / fase / HU que la cerró). La migración las agrega idempotente en bases previas (el gancho que dejó el 02).

**Comandos (`memoria/memoria.py`)**
- `pendientes [--scope modulo:X]` → lista lo abierto: señales activas de tipo `deuda-tecnica` o `pregunta-abierta`, las más viejas primero (con marca de vigencia del 02).
- `cerrar <id> --ref "<fase / commit>"` → `estado='cerrada'` con fecha y referencia. Sale de `search` y de `pendientes`; se conserva (nunca se borra).

**Enganches en el flujo** (documentados en `skills/usar-memoria/SKILL.md`): registrar la señal al declarar `§Fuera-de-scope`/`gap`; `pendientes` al abrir fase; `cerrar` al cerrar fase.

**Pruebas:** en `memoria/pruebas.py` (11 verdes en total). Base real migrada.

## Lo que no se mecanizó

Comprobar que **todo `§Fuera-de-scope` tenga su señal** registrada sería un validador del [01](validadores-de-codigo-de-proyecto.md), pero cae en el grupo fuzzy (cruzar el spec con las señales, como `F2`): queda anotado ahí, no forzado. El enganche vive como guía de flujo en el skill.
