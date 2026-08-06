# Hecho · Vigencia y poda de la memoria

Origen: pendiente 02. La memoria por señales (`memoria/senales.db`) ya no solo crece: cada señal tiene **vigencia** y se puede **podar** sin perder historia.

Cerrado el 2026-08-06.

---

## Qué se hizo

**Esquema (`memoria/esquema.sql` + migración idempotente en `memoria.py`)**
- Columna nueva `revisada` (fecha de última revisión, distinta de `creada`). En bases previas se agrega con `ALTER TABLE` y se rellena con `creada`.
- `estado` admite `archivada` (podada): se conserva en la tabla, fuera de `search`. Una sola tabla, una sola consulta (la decisión que anotaba el pendiente).

**Comandos (`memoria/memoria.py`)**
- `add` → la señal nace `revisada = hoy`.
- `search`/`list` → marca `⚠ sin verificar hace Nm` pasados **6 meses** (`--meses`); a igualdad de relevancia léxica, la más reciente primero (recencia + relevancia).
- `revisar <id>` → confirma la señal (revisada = hoy).
- `revisar --viejas --scope X` → el **ritual**: lista las activas más viejas para confirmar / reemplazar / archivar.
- `archivar <id>` → poda: `estado='archivada'`. Nunca borra; para `decision`/`restriccion` avisa que son historia.

**Pruebas:** `memoria/pruebas.py` (7 verdes, base temporal, no toca la real). La base real se migró (197 señales, `revisada` rellena).

## Lo que se movió al 05

La **detección de contradicciones** (dos señales activas del mismo scope que se contradicen) **no** se hizo aquí: contradecir es semántico, no léxico —un detector por palabras miente en las dos direcciones—. Se movió al [05 · memoria semántica](../05-memoria-semantica.md), que es donde se puede hacer bien. Mientras tanto, la cubre el ritual humano de `revisar --viejas`.
