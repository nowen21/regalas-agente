# Funcionalidad implementada — Fase «B-EP-002-HU-002-la-entrada-se-entiende-sin-conocer-el-proyecto»   ·   `[CAPA 3]`

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-002-HU-002-la-entrada-se-entiende-sin-conocer-el-proyecto` |
| **Épica / HU** | [EP-002](../../epica.md) · [HU-002](../HU-002-registro-de-cambios.md) |
| **Versión** | 23.8.0 → **23.9.0** (MENOR) |
| **Fecha de cierre** | 2026-08-18 |

---

## 1. Qué quedó

**Las entradas del registro abren ahora explicando qué cambió y por qué, en dos frases que se entienden sin conocer el proyecto.** El detalle —identificadores, rutas, enlaces— sigue estando, debajo.

Nace [`20·M17`](../../../../../base/20-meta-reglas/reglas/M17-la-entrada-del-registro-abre-en-castellano-llano.md) y `validar.py metareglas` lo comprueba sobre la versión vigente.

---

## 2. La prueba la hizo una persona, y falló

El `CA-03` de esta historia exige que la entrada se entienda sin haber seguido el trabajo. **Estaba escrito desde el principio y nunca se había comprobado con un lector de verdad.**

Se le mostró al usuario la entrada de la `15.2.0` y respondió **«no entendí nada»**.

**No era una entrada mala: eran todas.** De las 83, **74 citan una ruta de archivo, 43 un identificador de regla, y ninguna tiene menos de tres marcas de jerga**.

> **Quien escribe una entrada ya sabe de qué habla**, así que releerla uno mismo no comprueba nada. Es lo que hizo que el criterio sobreviviera meses sin cumplirse.

---

## 3. Lo que el programa hace y lo que no

**No decide si se entiende** — eso lo decide quien lee, y está declarado en la clasificación.

**Cuenta lo que la volvía ilegible:** que el primer párrafo abra con un identificador de regla, una ruta o las palabras de la casa. Su primer hallazgo fue **la entrada escrita unas horas antes**, por quien acababa de medir el problema.

**Y solo mira la versión vigente.** Reportar las 83 sepultaría la única que todavía se puede arreglar — y una salida sepultada se deja de leer.

---

## 4. Lo que no hace

- **No reescribe las 83 anteriores.** `20·M10`: un cambio de norma no reabre lo cerrado.
- **No responde la pregunta más grande:** si el registro estaba escrito para adentro, probablemente otros documentos también. `00·ID7` lo exige para todo lo que el agente entrega, y hasta hoy nadie lo había comprobado con un lector real.
