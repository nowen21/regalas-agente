> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F15 · No saltes ni reordenes las once etapas de la fase

Toda fase recorre las once etapas del ciclo —declaración macro, disparo, diseño del plan, pausa, aprobación, ejecución, pruebas, cierre documental, commit, reporte y publicación— en ese orden (extiende [`02·F4`](F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md) · deroga [`02·F4.2`](F4.2-no-saltes-ni-reordenes-las-once-etapas-de-la-fase.md)). Quién actúa y qué hito cierra cada una: [`base.md`](../base.md).

**Excepción** — un trabajo trivial (arreglo de una línea, corrección ortográfica) puede seguir un flujo abreviado si la capa 3 del proyecto lo permite **por escrito** (condición). No alcanza a cambios con lógica ni a los que tocan datos o permisos, que van por las once (límite). Lo autoriza el usuario al aprobar esa regla de capa 3 (autoriza).

```
INCORRECTO: usuario dice "arranque con Fase X" → agente empieza a implementar
            (se salta las etapas 3, 4 y 5: plan, pausa y aprobación)
CORRECTO:   disparo → plan detallado → pausa y presentación → OK del usuario
            → ejecución
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v3.1.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ✅ ✅ ✅ ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 20 ✅ · 0 ❌ · 0 N/A.** Toma el contenido de [`F4.2`](F4.2-no-saltes-ni-reordenes-las-once-etapas-de-la-fase.md), cuyo ID decimal no admitía [`M4`](../../20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md) — era su único ❌.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
