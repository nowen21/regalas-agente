> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC16 · Crea la Épica desde la plantilla central

Toda épica se parte de [`plantillas/ciclo-vida-proyectos/03-epica.md`](../../../plantillas/ciclo-vida-proyectos/03-epica.md), leída del estándar cada vez, y se guarda donde fija [`02·F12`](../../02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md), punto 13. Sus criterios son de resultado, no de pantalla, y el enlace con cada HU se escribe en los dos lados (depende de [`02·F0`](../../02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md)).

```
INCORRECTO: la épica lista sus HU, pero ninguna HU declara a qué épica pertenece
CORRECTO:   la épica lista sus HU y cada HU nombra su épica · al mover una, se
            actualizan los dos
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v30.8.0**, el **2026-08-22**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.** N/A — **16**: no tiene excepción. Fila 10: pasó de 18 líneas a cuatro; la nomenclatura y la ruta ya las fija [`02·F12`](../../02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md), punto 13 y el índice por nivel es [`DOC17`](DOC17-manten-un-readme-en-cada-nivel-del-arbol-de-trabajo.md), así que se enlazan en vez de repetirse (fila 11).

**Recortada al molde el 2026-08-22 (pendiente 19, capítulo `13`):** el sello decía ✅ en la fila 10 con el cuerpo pasado de 320; ahora cabe. Lo que salió era porqué o detalle que ya vive en otro archivo, y queda en [notas/porques-recortados-al-molde.md](../../../notas/porques-recortados-al-molde.md).

**Vuelta a sellar el 2026-08-22 (pendiente 19):** cambió solo la cita a `02·F12`, que ya no tiene sub-identificadores de regla: los `F12.N` son puntos del anexo de nomenclatura. La exigencia no cambió.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
