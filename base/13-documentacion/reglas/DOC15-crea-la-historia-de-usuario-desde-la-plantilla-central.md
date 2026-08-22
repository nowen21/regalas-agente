> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC15 · Crea la Historia de Usuario desde la plantilla central

Toda HU se parte de [`plantillas/ciclo-vida-proyectos/04-HU.md`](../../../plantillas/ciclo-vida-proyectos/04-HU.md), leída del estándar **cada vez** —no de memoria ni de una copia local, que envejece—, y se guarda versionada en la ubicación que fija [`02·F12`](../../02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md), punto 13. Se rellena con contenido real: rol concreto, criterios que cubran camino feliz, error y caso borde, y sin secciones a medio llenar.

```
INCORRECTO: escribir la HU de memoria, o copiar la plantilla dentro del proyecto
            "para tenerla a mano" — la copia queda vieja y nadie se entera
CORRECTO:   leer la plantilla central → rellenarla con datos reales → guardarla
            donde manda la nomenclatura de fases
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v30.8.0**, el **2026-08-22**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia · **16**: no tiene excepción. Fila 9: la regla traía enterrada una segunda exigencia de otra naturaleza —un `README.md` índice en cada nivel del árbol—, que [`DOC16`](DOC16-crea-la-epica-desde-la-plantilla-central.md) ya citaba como si fuera regla propia. Ahora lo es: [`DOC17`](DOC17-manten-un-readme-en-cada-nivel-del-arbol-de-trabajo.md).

**Vuelta a sellar el 2026-08-22 (pendiente 19):** cambió solo la cita a `02·F12`, que ya no tiene sub-identificadores de regla: los `F12.N` son puntos del anexo de nomenclatura. La exigencia no cambió.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
