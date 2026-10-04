> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F29 · El reporte de un proyecto se corrige para todos

Lo que un proyecto reporta al estándar es un defecto que ya está en todos los proyectos que lo usan. Se analiza buscando su causa en el estándar, se revisa en cada proyecto registrado y se corrige en la raíz. Antes de avisar, se comprueba en el proyecto que lo reportó, en el escenario donde se presentó (complementa [`02·F24`](F24-el-defecto-del-estandar-se-reporta-no-se-corrige.md)).

```
INCORRECTO: scilit reporta que el andamio no sirve desde un proyecto → se
            arregla para que funcione en scilit
CORRECTO:   se busca por qué el andamio supone estar dentro del estándar, se
            corrige ahí, se prueba en una copia de scilit y después se le avisa
```

**Aplica a:** trabajar-cadena

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v53.3.0**, el **2026-10-04**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.** N/A, **16**: no tiene excepción. Fila 4: va en el `02`, junto a `F24`, porque dice qué paso del flujo sigue a un reporte. Fila 6: `F29` es el siguiente consecutivo libre. Fila 9: la exigencia es una sola, corregir el reporte en la raíz para todos los proyectos. Fila 17: `F24` dice cómo reporta el proyecto; esta, cómo lo atiende el estándar.

**No validable:** saber si una corrección se pensó para todos los proyectos es criterio. Lo que sí se comprueba son sus pruebas, que corren desde un proyecto de prueba.

Nace del análisis 1 del pendiente 110 (acuerdos 1 y 7), que reunió los cinco reportes de scilit del 2026-10-03.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
