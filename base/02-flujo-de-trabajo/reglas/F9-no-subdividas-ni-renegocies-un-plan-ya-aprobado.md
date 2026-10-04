> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F9 · No subdividas ni renegocies un plan ya aprobado

Aprobado un plan, se entrega **completo**: no se parte en sub-fases nuevas, no se vuelve a preguntar por decisiones que ya cabían dentro ni se ofrecen opciones sobre detalles ya resueltos con criterio profesional. Si el volumen pide subdividir, se propone **antes** de aprobar (extiende [`02·F3`](F3-ejecuta-seguido-el-plan-aprobado.md)).

**Excepción** — interrumpe el flujo el hallazgo de la épica en curso que, para cerrar la fase, obliga a tocar algo que el plan no declara (condición). Detiene la ejecución y vuelve al análisis, no se ofrece como opción a elegir y no habilita a repartir el trabajo restante; el hallazgo que no obliga a eso se anota con su pendiente donde pertenece y el trabajo sigue (límite). Retomar lo decide el usuario al aprobar el análisis (autoriza).

```
INCORRECTO: usuario aprueba el plan → agente lo divide en 4 sub-fases y vuelve a
            pedir 4 aprobaciones "para hacerlo manejable"
CORRECTO:   si el volumen era problema, la subdivisión se propone ANTES de aprobar;
            después, ejecución continua
```

**Aplica a:** trabajar-cadena

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v52.1.0**, el **2026-10-03**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ ✅ ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 20 ✅ · 0 ❌ · 0 N/A.** La duplicación con [`F3`](F3-ejecuta-seguido-el-plan-aprobado.md), que su propio texto admitía —*"es el enunciado base"*—, quedó declarada como `extiende 02·F3` en vez de repetida ([`M7`](../../20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md)).

**Recortada al molde el 2026-08-22 (pendiente 19, capítulo `02`):** el sello decía ✅ en la fila 10 con el cuerpo pasado de 320; ahora cabe. Lo que salió era porqué o detalle que ya vive en otro archivo, y queda en [notas/porques-recortados-al-molde.md](../../../notas/porques-recortados-al-molde.md).

**Excepción reescrita el 2026-10-03** (`EP-023·HU-004`, fase `B`, análisis 12 del pendiente 103, acuerdo 1): solo detiene el hallazgo que obliga a salirse del plan. Fila 16: condición, límite y quién autoriza siguen declarados. Fila 17: [`13·DOC24`](../../13-documentacion/reglas/DOC24-cierra-el-analisis-en-su-mismo-archivo.md) dice lo mismo desde el análisis.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
