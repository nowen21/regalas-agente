> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC5 · Registra como señal lo que no se recupera del código — *opt-in*

Lo que no se reconstruye leyendo el código —una decisión y su motivo, un error resuelto, un supuesto, una alternativa descartada— se registra como **señal**: qué pasó · por qué · dónde · qué se aprendió, con su tipo y a quién sirve. La revertida no se borra: se marca reemplazada y enlaza a la nueva.

```
INCORRECTO: "elegimos X y no Y porque Z" queda solo en el chat → se pierde al compactar
CORRECTO:   se registra como señal de tipo decisión, con qué / por qué / dónde / qué se aprendió
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

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia · **16**: no tiene excepción; la marca `*opt-in*` no es una excepción, es una regla que el proyecto enciende o no. Fila 5: se quitaron el motor de base de datos, el nombre de la herramienta y la carpeta concreta que traía — eso lo declara la capa 3. El porqué del diseño está en [`notas/memoria-por-senales.md`](../../../notas/memoria-por-senales.md).

**Recortada al molde el 2026-08-22 (pendiente 19, capítulo `13`):** el sello decía ✅ en la fila 10 con el cuerpo pasado de 320; ahora cabe. Lo que salió era porqué o detalle que ya vive en otro archivo, y queda en [notas/porques-recortados-al-molde.md](../../../notas/porques-recortados-al-molde.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
