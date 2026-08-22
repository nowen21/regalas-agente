> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F5 · Corre solo las suites que la fase toca

La ejecución que cierra una fase alcanza la suite del módulo de la fase, las suites que la fase refactorizó y las que dependen de los archivos tocados según la matriz de [`02·F17`](F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md) — no la suite completa del proyecto (extiende [`08·T5`](../../08-pruebas.md#t5--ejecuta-y-reporta), que ya obliga a correrlas y a reportar el conteo).

**Excepción** — la ejecución global se hace cuando se declara **explícitamente** como "regresión total pre-release" (condición). No entra en el flujo normal de fase (límite) y la pide el usuario (autoriza).

```
INCORRECTO: al terminar la fase, correr toda la suite del proyecto "por si acaso"
            → cientos de pruebas, minutos de espera y rojos que ya existían antes
CORRECTO:   correr la suite del módulo + las declaradas en el plan + las que la
            matriz de dependencias señala
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v30.8.0**, el **2026-08-22**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ ✅ ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 20 ✅ · 0 ❌ · 0 N/A.**

**Vuelta a aplicar el 2026-08-22 (pendiente 19):** la fila 4 reprobaba por dueño del tema. Releída: `08·T5` es la dueña de *que las pruebas se corran y se reporten*, y `F5` declara que la extiende y dice solo lo suyo, **cuáles** suites toca una fase, que es alcance del flujo y no del capítulo de pruebas. El texto duplicado ya se había reemplazado por el enlace; lo que faltaba era volver a juzgar la fila con el texto nuevo.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
