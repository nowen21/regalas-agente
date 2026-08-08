> Regla del capítulo [`13 · Documentación`](../base.md).

## DOC5 · Registra como señal lo que no se recupera del código — *opt-in*

Lo que no se puede reconstruir leyendo el código —una decisión y su motivo, un error ya resuelto, un supuesto, una alternativa descartada— se registra como **señal**: qué pasó · por qué · dónde · qué se aprendió, más su tipo y a quién sirve. Una señal revertida no se borra: se marca reemplazada y se enlaza la nueva. La capa 3 declara **un solo** sitio donde viven y con qué se operan; sin esa declaración, la regla no está activada.

```
INCORRECTO: "elegimos X y no Y porque Z" queda solo en el chat → se pierde al compactar
CORRECTO:   se registra como señal de tipo decisión, con qué / por qué / dónde / qué se aprendió
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v3.2.0**, el **2026-08-07**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.** N/A — **14** y **15**: no declara dependencia · **16**: no tiene excepción; la marca `*opt-in*` no es una excepción, es una regla que el proyecto enciende o no. Fila 5: se quitaron el motor de base de datos, el nombre de la herramienta y la carpeta concreta que traía — eso lo declara la capa 3. El porqué del diseño está en [`notas/memoria-por-senales.md`](../../../notas/memoria-por-senales.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
