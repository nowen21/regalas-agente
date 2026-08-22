> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC10 · Registra en el catálogo del proyecto toda regla propia

Toda regla que solo vale para este proyecto se escribe en su catálogo, cuya ruta declara la capa 3, numerada `P1`, `P2` y así, para poder citarla; cada `P` que nace o se endurece deja su señal ([`DOC5`](DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)). La que se promueve a `base/` conserva solo su matiz y enlaza a la regla base.

```
INCORRECTO: el usuario dice "de aquí en adelante siempre X" · se aplica · nada
            queda escrito · la próxima sesión no lo sabe
CORRECTO:   se aplica + se crea la `P` en el catálogo + se registra su señal
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

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia · **16**: no tiene excepción. Se corrigieron dos defectos de fondo: citaba `P28` —una regla de capa 3— desde capa 2, que es depender hacia arriba ([`M7`](../../20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md)), y cerraba con una enumeración congelada de IDs citables que ya estaba vieja; lo que garantiza que toda regla se puede citar es [`M4`](../../20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md). El disparador —evaluar si lo que pide el usuario es regla— es [`01·C10`](../../01-conducta.md#c10--lo-que-el-usuario-pide-dos-veces-se-propone-como-regla) y no se repite aquí.

**Recortada al molde el 2026-08-22 (pendiente 19, capítulo `13`):** el sello decía ✅ en la fila 10 con el cuerpo pasado de 320; ahora cabe. Lo que salió era porqué o detalle que ya vive en otro archivo, y queda en [notas/porques-recortados-al-molde.md](../../../notas/porques-recortados-al-molde.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
