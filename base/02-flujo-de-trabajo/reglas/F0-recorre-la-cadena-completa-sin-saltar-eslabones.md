> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F0 · Recorre la cadena completa, sin saltar eslabones

Todo desarrollo, nuevo o cambio de comportamiento, recorre `planteamiento → épica → HU → especificación → plan → código`, con un análisis antes de las épicas, de las HU de cada épica y de cada pendiente. Ningún eslabón se salta ni se fusiona; si falta uno, se crea primero (depende de [`02·F2`](F2-sin-especificacion-acordada-no-hay-codigo.md), [`13·DOC15`](../../13-documentacion/reglas/DOC15-crea-la-historia-de-usuario-desde-la-plantilla-central.md), [`13·DOC16`](../../13-documentacion/reglas/DOC16-crea-la-epica-desde-la-plantilla-central.md)).

**Excepción** — lo que **no es desarrollo** queda fuera de la cadena: leer o investigar, configuración local, comandos que el usuario pide, y el arreglo que solo devuelve el código a lo que ya decía la especificación (condición). Cubre ese trabajo puntual; no habilita a construir funcionalidad sin cadena (límite). Si hay duda de si el caso es desarrollo, decide el usuario ([`01·C7`](../../01-conducta.md#c7--ante-dos-lecturas-pregunta)) (autoriza).

```
INCORRECTO: llega una idea → se escribe el plan de trabajo directo
CORRECTO:   idea → análisis → objetivo y alcance → épica → HU → especificación
            → plan → construir
```

**Aplica a:** trabajar-cadena

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v40.0.0**, el **2026-10-01**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ ✅ ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 20 ✅ · 0 ❌ · 0 N/A.** Es el texto corregido que [`estructura-regla.md`](../../20-meta-reglas/estructura-regla.md) ya publicaba como versión conforme; el mapa de siete pasos y el encadenamiento que antes vivían aquí están en [`base.md`](../base.md).

**Recortada al molde el 2026-08-22 (pendiente 19, capítulo `02`):** el sello decía ✅ en la fila 10 con el cuerpo pasado de 320; ahora cabe. Lo que salió era porqué o detalle que ya vive en otro archivo, y queda en [notas/porques-recortados-al-molde.md](../../../notas/porques-recortados-al-molde.md).

**Vuelta a sellar el 2026-10-01 (`EP-023·HU-001`, fase `A`):** el cuerpo suma el análisis en los tres puntos donde algo se reparte (análisis 1 del pendiente 103, conclusión 2). Para que siga cabiendo en 320 caracteres se acortó la redacción, sin cambiar lo que exige. La fila **9** sigue aprobando: el análisis es un eslabón más de la misma cadena.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
