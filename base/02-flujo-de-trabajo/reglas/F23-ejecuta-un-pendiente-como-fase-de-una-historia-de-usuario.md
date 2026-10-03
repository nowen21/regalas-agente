> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F23 · Ejecuta un pendiente como fase de una historia de usuario

Un hallazgo se anota como pendiente; el pendiente aprobado pasa por su análisis, baja a una historia de usuario hija de su épica y se construye como fase de esa historia. Que la mejora ya esté escrita no salta ningún eslabón: el pendiente dice **qué falta**, no cómo se construye ni se comprueba (extiende [`02·F0`](F0-recorre-la-cadena-completa-sin-saltar-eslabones.md)).

```
INCORRECTO: el pendiente dice qué hay que arreglar → se edita el código, se sube
            la versión y se marca hecho; como no hubo fase, nadie escribió el
            plan de pruebas y el arreglo se publicó sin probarse
CORRECTO:   el pendiente baja a HU → fase con su plan y sus pruebas → se
            construye, se prueba, y solo entonces el pendiente se marca hecho
```

**Aplica a:** trabajar-cadena

**Autoriza escribir:** `**/pendientes/*/pendiente.md`

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v51.0.0**, el **2026-10-03**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.** N/A — **16**: no tiene excepción propia. La de [`02·F0`](F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) rige acá porque esta la extiende: el pendiente que solo pide decidir algo, o leer, no es desarrollo y no abre fase.

**Recortada al molde el 2026-08-22 (pendiente 19, capítulo `02`):** el sello decía ✅ en la fila 10 con el cuerpo pasado de 320; ahora cabe. Lo que salió era porqué o detalle que ya vive en otro archivo, y queda en [notas/porques-recortados-al-molde.md](../../../notas/porques-recortados-al-molde.md).

La fila **2** se buscó por concepto y se leyó el capítulo entero. [`02·F21`](F21-un-incumplimiento-ya-identificado-no-se-repite-en-lo-nuevo.md) también habla de pendientes, pero de otra cosa: aquella dice que lo ya anotado no se vuelve a producir; esta dice por dónde entra al trabajo lo que el pendiente pide. Y [`20·M13`](../../20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md) dice dónde **vive** un pendiente, no cómo se ejecuta.

**Precisada el 2026-09-27 (`EP-005·HU-022`):** el cuerpo nombra el tramo que faltaba, de hallazgo a pendiente, y dice que el pendiente baja a HU cuando está aprobado. Hasta entonces el orden completo, hallazgo, pendiente, HU y fase, no estaba escrito en ninguna regla, y `andamio.py` obligaba a crear la HU antes que el pendiente.

La fila **10** sigue aprobando: el cuerpo nuevo cabe en el molde de 320 caracteres leídos.

La fila **9** es una sola exigencia, el orden de la cadena de principio a fin: sus eslabones no se cumplen por separado. Una HU que nadie baja a fase no construye nada, una fase sin HU es el eslabón saltado, y una HU creada antes que su pendiente fija el alcance antes de que alguien lo apruebe.

La fila **17** obligó a corregir dos procedimientos que autorizaban lo contrario: el §2 del [`CLAUDE.md`](../../../CLAUDE.md) del estándar y los nueve pasos de [`20 · base.md`](../../20-meta-reglas/base.md), que describían cambiar una regla como *buscar → enrutar → escribir → versionar*, sin cadena. Los dos quedan diciendo que cuando el cambio sale de un pendiente, la cadena va primero.

**Precisada el 2026-10-01 (`EP-023·HU-001`, fase `A`):** el pendiente aprobado pasa por su análisis antes de bajar a la HU (análisis 1 del pendiente 103, punto 15). Para que siga cabiendo en 320 caracteres se acortó la redacción, sin cambiar lo que exige.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
