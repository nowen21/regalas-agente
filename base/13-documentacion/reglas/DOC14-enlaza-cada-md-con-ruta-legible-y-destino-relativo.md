> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC14 · Enlaza cada `.md` con ruta legible y destino relativo

Toda referencia de un `.md` a otro `.md` del proyecto es un enlace de dos partes: como **texto**, la ruta completa desde la raíz —para saber dónde vive sin abrirlo—; como **destino**, la ruta relativa desde el archivo actual.
**Excepción** — el enlace a un archivo de **la misma carpeta** lleva solo su nombre (condición): quien lee ya está parado ahí y el propósito está cumplido. No vale para ninguna otra ruta (límite), y lo fija esta regla (autorizador).

```
INCORRECTO: [plan_trabajo.md](../../otra/carpeta/plan_trabajo.md)
            — el texto no dice dónde vive
INCORRECTO: `documentacion/area/unidad/plan_trabajo.md`
            — dice dónde vive pero no se puede abrir
CORRECTO:   [documentacion/area/unidad/plan_trabajo.md](../../area/unidad/plan_trabajo.md)
```

No aplica a los nombres cortos usados como identificador en medio de una frase, cuando quien lee ya sabe dónde viven.

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v23.18.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A ✅ ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 18 ✅ · 0 ❌ · 2 N/A.** N/A — **14** y **15**: no declara dependencia.

**Vuelto a aplicar el 2026-08-18, al escribirle la excepción del vecino.** La regla pedía la ruta desde la raíz también para el archivo de al lado, y eso daba textos de unos 130 caracteres para nombrar algo que está en la misma carpeta — **747 enlaces del repositorio**, la mayoría de los documentos de una fase citando a sus hermanos.

**La excepción sale del propio texto de la regla, no de la incomodidad.** Dice que el texto lleva la ruta completa *«para saber dónde vive sin abrirlo»*. **Para el vecino ese propósito ya está cumplido**: quien lee está parado ahí. Exigirla igual es pedir el trámite después de que el motivo se agotó.

**El límite es estrecho a propósito:** la misma carpeta, y nada más. Un enlace a la carpeta de al lado sigue llevando su ruta entera, porque ahí el lector sí necesita saber adónde va. Era la regla más larga del capítulo (58 líneas) y reprobaba tres filas: nombraba visor de repositorio, editor, código de error y "route" (fila 5), traía **rutas reales de un cliente** en los ejemplos (fila 5) y pedía dos cosas —el formato del enlace y una pieza de infraestructura del proyecto— (fila 9). Los ejemplos son ahora ficticios y el montaje del render local quedó como anexo del capítulo, [`render-local-de-md.md`](../render-local-de-md.md), que no es norma: es una receta que el proyecto adopta si quiere.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
