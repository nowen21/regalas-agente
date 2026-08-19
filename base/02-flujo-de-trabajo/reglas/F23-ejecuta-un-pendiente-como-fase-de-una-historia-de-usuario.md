> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F23 · Ejecuta un pendiente como fase de una historia de usuario

Un pendiente del backlog no se implementa desde su archivo: se baja a historia de usuario de la épica que le corresponda y se construye como fase de esa historia ([`02·F12`](F12-relacion-y-nomenclatura-de-fases.md)), con todo lo que una fase lleva (extiende [`02·F0`](F0-recorre-la-cadena-completa-sin-saltar-eslabones.md)).
Que la mejora ya esté acordada y escrita no salta ningún eslabón: el pendiente dice **qué falta**, no cómo se construye ni cómo se comprueba.

```
INCORRECTO: el pendiente dice qué hay que arreglar → se edita el código, se sube
            la versión y se marca hecho; como no hubo fase, nadie escribió el
            plan de pruebas y el arreglo se publicó sin probarse
CORRECTO:   el pendiente baja a HU → fase con su plan y sus pruebas → se
            construye, se prueba, y solo entonces el pendiente se marca hecho
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v20.0.1**, el **2026-08-16**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.** N/A — **16**: no tiene excepción propia. La de [`02·F0`](F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) rige acá porque esta la extiende: el pendiente que solo pide decidir algo, o leer, no es desarrollo y no abre fase.

La fila **2** se buscó por concepto y se leyó el capítulo entero. [`02·F21`](F21-un-incumplimiento-ya-identificado-no-se-repite-en-lo-nuevo.md) también habla de pendientes, pero de otra cosa: aquella dice que lo ya anotado no se vuelve a producir; esta dice por dónde entra al trabajo lo que el pendiente pide. Y [`20·M13`](../../20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md) dice dónde **vive** un pendiente, no cómo se ejecuta.

La fila **9** es una sola exigencia: bajar a HU y construir como fase no se cumplen por separado — una HU que nadie baja a fase no construye nada, y una fase sin HU es el eslabón saltado que la regla prohíbe.

La fila **17** obligó a corregir dos procedimientos que autorizaban lo contrario: el §2 del [`CLAUDE.md`](../../../CLAUDE.md) del estándar y los nueve pasos de [`20 · base.md`](../../20-meta-reglas/base.md), que describían cambiar una regla como *buscar → enrutar → escribir → versionar*, sin cadena. Los dos quedan diciendo que cuando el cambio sale de un pendiente, la cadena va primero.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
