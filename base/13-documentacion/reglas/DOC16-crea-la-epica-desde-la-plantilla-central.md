> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC16 · Crea la Épica desde la plantilla central

Toda épica se parte de [`plantillas/epica.md`](../../../plantillas/epica.md), leída del estándar cada vez, y se guarda versionada donde fija [`02·F12.13`](../../02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md). Sus criterios son de resultado, no de pantalla —el comportamiento vive en las HU—, y el enlace con cada HU se escribe en los dos lados. Toda HU pertenece a una épica, aunque la épica agrupe una sola (depende de [`02·F0`](../../02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md)).

```
INCORRECTO: la épica lista sus HU, pero ninguna HU declara a qué épica pertenece
CORRECTO:   la épica lista sus HU y cada HU nombra su épica · al mover una, se
            actualizan los dos
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v3.2.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.** N/A — **16**: no tiene excepción. Fila 10: pasó de 18 líneas a cuatro; la nomenclatura y la ruta ya las fija [`02·F12.13`](../../02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md) y el índice por nivel es [`DOC17`](DOC17-manten-un-readme-en-cada-nivel-del-arbol-de-trabajo.md), así que se enlazan en vez de repetirse (fila 11).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
