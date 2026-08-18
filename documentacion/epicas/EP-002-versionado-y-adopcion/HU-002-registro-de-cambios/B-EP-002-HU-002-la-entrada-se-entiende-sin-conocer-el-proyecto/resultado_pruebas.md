# Resultado de Pruebas — Fase B-EP-002-HU-002: la entrada se entiende sin conocer el proyecto

| Campo | Valor |
|---|---|
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md) v1.0 · **Ciclo** 1 · **Fecha** 2026-08-18 |

---

## 1. Casos

| Caso | Veredicto | Qué dio |
|---|---|---|
| CP-001 · un lector real lee una entrada | ❌ **Falla** | **«No entendí nada»** — y de ahí sale toda la fase |
| CP-002 · lo que se reporta | ✅ **Pasa** | Los tres motivos, y el mensaje los junta |
| CP-003 · lo que no se reporta | ✅ **Pasa** | La llana, y la que lleva el detalle debajo |
| CP-004 · las viejas no se reportan | ✅ **Pasa** | Solo la vigente |
| CP-005 · no regresión | ✅ **Pasa** | `tests/` **197 · OK** · `pruebas.py` 357 · `estandar` limpio |

**5 ejecutados. El primero falló, y era el que importaba.**

---

## 2. La prueba que falló, y lo que destapó

Se le mostró al usuario la entrada de la **`15.2.0`**, del 14 de agosto, y se le preguntó qué cambió y por qué. Respondió **«no entendí nada»**.

**Al mirar por qué, no era una entrada mala.** Daba por sabido todo lo necesario para entenderla: nunca dice qué es un «caso de prueba», ni que hay dos documentos —el plan y el resultado—, ni qué significa MENOR. Y la frase que parecía explicar —*«no es una prueba: es un recuerdo»*— suena bien y no explica nada a quien no sabe de qué se habla.

**Entonces se midieron las 83:**

| | |
|---|---:|
| Citan una ruta de archivo | **74** |
| Citan un identificador de regla | **43** |
| Con dos marcas de jerga o menos | **0** |

**Ninguna se salva.** El registro entero está escrito para adentro.

---

## 3. Qué se construyó

Nace [`20·M17`](../../../../../base/20-meta-reglas/reglas/M17-la-entrada-del-registro-abre-en-castellano-llano.md), con su checklist en CUMPLE: **la entrada abre con qué cambió y por qué, en dos frases sin identificadores, sin rutas y sin las palabras de la casa. El detalle va debajo.**

`validar.py metareglas` lo comprueba sobre **la versión vigente**, y su primer hallazgo fue la entrada de hoy — escrita unas horas antes por quien acababa de medir el problema.

**Lo que el programa no hace es decidir si se entiende.** Eso lo decide quien lee, y está declarado. Lo que cuenta es lo mecánico: por dónde abre.

---

## 4. Lo que queda abierto · [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)

**Las 83 entradas anteriores se quedan como están.** [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md): un cambio de norma no reabre lo cerrado. Reescribirlas es un trabajo aparte, y no urge.

**Y hay una pregunta más grande que esta fase no toca:** si el registro estaba escrito para adentro, es probable que otros documentos también. `00·ID7` lo exige para todo lo que el agente entrega, y nadie lo ha comprobado con un lector real más que hoy, una vez.

---

## 5. Veredicto

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** — el `CA-03` falló, y arreglarlo era el objeto de la fase |
| **Defectos abiertos aceptados** | dos: las 83 viejas, y si el resto de documentos tiene el mismo problema |
| **Ciclos** | 1 |
