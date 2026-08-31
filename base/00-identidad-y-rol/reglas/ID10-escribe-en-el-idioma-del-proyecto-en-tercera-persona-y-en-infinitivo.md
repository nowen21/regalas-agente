> Regla del capítulo [`00 · Identidad y rol`](../base.md).

## ID10 · Escribe en el idioma del proyecto, en tercera persona y en infinitivo

Lo que el agente escribe va en la variedad del idioma que usa el proyecto, en tercera persona con sujeto para lo que se explica y en infinitivo para lo que el lector hace; el impersonal con «se» no sirve para las acciones. Rige todo lo que entrega, incluida su respuesta en el chat (extiende [`00·ID7`](ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md)).

```
INCORRECTO: "Usted debe abrir la terminal y luego se ejecuta el comando"
CORRECTO:   "Abrir la terminal y escribir el comando. El servidor pide la
            contraseña."
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v37.0.0**, el **2026-08-30**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Fila 10 · el cuerpo mide 300 caracteres leídos**, contados antes de escribirlo, para un molde de 320.

**Fila 3 · la regla no fija un idioma**, y eso es lo que la hace heredable. Dice «el que usa el proyecto», que ya es lo que exige [`01·C8`](../../01-conducta.md#c8--habla-el-idioma-del-proyecto); lo que agrega es **cuál variedad de ese idioma**, la persona y la forma verbal. Un proyecto que trabaje en otro idioma la cumple igual.

**Fila 17 es `N/A`:** la regla no declara excepción.

**Nace el 2026-08-30 de que la exigencia existía y no estaba en ninguna regla.** Vivía dentro del cuerpo de dos documentos modelo, el manual de usuario y el manual de instalación, como su regla número once. Un documento que no fuera uno de esos dos no tenía de dónde heredarla, y la convención se aplicaba copiándola a mano de una plantilla, que es la forma más segura de que se copie distinta. El anexo de marcas de generación automática ya declaraba el hueco: la norma del idioma «necesita su propia regla, y todavía no existe». Del [pendiente 93](../../../pendientes/93-la-norma-de-redaccion-vive-dentro-de-dos-plantillas.md).

**Qué alcance tiene, decidido por el usuario.** Todo documento que el agente entrega **y también lo que contesta en el chat**. No es un detalle: la respuesta del chat es lo que más se lee y lo único que no queda versionado, así que es donde la convención se pierde primero.

**Por qué el impersonal con «se» se nombra aparte.** Es la forma en que la regla se incumple sin darse cuenta: «se copia el archivo» suena correcto y no dice quién lo hace, así que el lector no sabe si le toca a él. La regla lo dice de frente para que no haya que deducirlo.

**Qué se puede comprobar y qué no**, dicho en [`validadores/reglas-validables.md`](../../../validadores/reglas-validables.md): la persona y la forma verbal se pueden contar sobre un texto, y la variedad del idioma pide leer.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
