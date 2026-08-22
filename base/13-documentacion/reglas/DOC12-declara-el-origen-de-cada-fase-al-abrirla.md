> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC12 · Declara el ORIGEN de cada fase al abrirla

Toda fase nueva abre declarando de dónde sale, en una de tres formas: **modifica** fases anteriores, nombrándolas; **agrega** lo que no existía; o **ambas**. El formato del bloque está en [`plantillas/ciclo-vida-proyectos/05-fase.md`](../../../plantillas/ciclo-vida-proyectos/05-fase.md) y la carpeta de la fase repite el ORIGEN de su especificación.

**Excepción** — una fase **ya cerrada** no se reabre para ponerle ORIGEN (condición): queda inmutable y su origen se infiere del historial; no habilita a abrir fases nuevas sin declararlo (límite). Si hay duda de si una fase está cerrada, decide el usuario ([`01·C7`](../../01-conducta.md#c7--ante-dos-lecturas-pregunta)) (autoriza).

```
INCORRECTO: "Fase 7 — cambios menores" · quien lee no sabe si continúa la 6
            o reacciona a un análisis
CORRECTO:   ORIGEN declarado: qué fase modifica y qué defecto retoma, o qué agrega
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v30.8.0**, el **2026-08-22**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A ✅ ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 18 ✅ · 0 ❌ · 2 N/A.** N/A — **14** y **15**: no declara dependencia. Fila 16: la excepción tenía condición pero no límite ni autorizador; ahora los tres. Fila 10: el formato canónico del bloque de fase, que ocupaba media regla, pasó a la plantilla.

**Recortada al molde el 2026-08-22 (pendiente 19, capítulo `13`):** el sello decía ✅ en la fila 10 con el cuerpo pasado de 320; ahora cabe. Lo que salió era porqué o detalle que ya vive en otro archivo, y queda en [notas/porques-recortados-al-molde.md](../../../notas/porques-recortados-al-molde.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
