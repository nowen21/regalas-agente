> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F8 · Edita solo los archivos que el plan aprobado declara

Se editan únicamente los archivos de la tabla del plan aprobado ([`02·F14`](F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md), pregunta 9). Descubrir a mitad que hace falta otro **detiene la ejecución** y vuelve al análisis: el plan pasa a su versión siguiente con aprobación nueva. Que el cambio sea obvio no autoriza; la aprobación sí ([`base.md`](../base.md)).

```
INCORRECTO: durante la ejecución el agente descubre que también hay que editar el
            archivo Y → lo edita en el mismo commit "porque era necesario"
CORRECTO:   descubre Y → se detiene → vuelve al análisis → el plan pasa a
            su versión siguiente y el usuario la aprueba → sigue
```

**Excepción** — una herramienta del proceso (`validadores/`, `adaptadores/`) que bloquea el trabajo se corrige sin abrir análisis cuando el usuario lo ordena con «Corrija» (condición). Vale solo en esa respuesta y solo para esas carpetas, y lo corregido se anota en el resumen de la sesión (límite). Lo autoriza la palabra del usuario.

**Aplica a:** trabajar-cadena, escribir-documento, cambiar-codigo

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v53.2.0**, el **2026-10-03**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A ✅ ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 18 ✅ · 0 ❌ · 2 N/A.** N/A — **14** y **15**: no declara dependencia; sus citas son referencia. Fila **16**: la excepción declara condición, límite y quién la autoriza.

**Excepción agregada el 2026-10-03** (análisis 16 del pendiente 103, acuerdo 2): corregir las herramientas del proceso con «Corrija» no abre análisis. De los 16 análisis del pendiente 103, 13 nacieron de fallas de esas herramientas o de no poder corregirlas sin uno. La valida `proyectos/cimiento/core/enganches/freno.py`.

**Recortada al molde el 2026-08-22 (pendiente 19, capítulo `02`):** el sello decía ✅ en la fila 10 con el cuerpo pasado de 320; ahora cabe. Lo que salió era porqué o detalle que ya vive en otro archivo, y queda en [notas/porques-recortados-al-molde.md](../../../notas/porques-recortados-al-molde.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
