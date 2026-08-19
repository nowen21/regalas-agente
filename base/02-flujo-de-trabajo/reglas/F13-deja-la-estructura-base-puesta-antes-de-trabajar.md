> Regla del capítulo [`02 · Flujo de trabajo`](../base.md).

## F13 · Deja la estructura base puesta antes de trabajar

Antes de cualquier paso del flujo —incluso antes de cargar contexto ([`02·F1`](F1-carga-el-contexto-antes-de-actuar.md))— el agente crea las carpetas que la norma exige: `proyectos/` para el código del usuario y, al lado, `.agente/`, `prompts/`, `documentacion/` y `pendientes/`. Crearlas no es decisión suya; **qué va dentro sí**, y ahí no mueve nada.
```
INCORRECTO: existe código suelto en la raíz → el agente crea `proyectos/` y mueve
            el código del usuario adentro
CORRECTO:   existe código suelto en la raíz → el agente crea `proyectos/` vacía,
            avisa que hay código fuera y espera a que el usuario decida si lo mueve
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](../../20-meta-reglas/checklist.md) contra **v23.12.2**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**La fila 10 reprueba, y es la única.** El cuerpo mide **549 caracteres** y el molde da para 320 — casi el doble. (Se medía 631 hasta el 2026-08-18, cuando el conteo dejó de cobrar el marcado de los enlaces; la regla se pasa igual.) La propia fila dice qué hacer cuando no cabe: o son dos reglas, o se está contando el **porqué** y ese va a `notas/`. Acá es lo segundo: el párrafo explica *por qué* crear una carpeta que la norma exige no es una decisión, y *qué* no debe tocar el agente dentro de `proyectos/`. Las dos cosas son el razonamiento, no la exigencia.

**Recortarla es un cambio de regla y no se hace acá.** Va al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md), que es el que junta las reglas que no pasan su propio checklist y las trabaja por capítulo. Este bloque deja escrito **qué** falla, para que quien lo tome no tenga que volver a medirlo.

Las filas **14 a 16** son N/A: la regla nombra a [`02·F1`](F1-carga-el-contexto-antes-de-actuar.md) para decir que va **antes** que ella, y eso es orden de ejecución, no una de las tres dependencias que [`20·M7`](../../20-meta-reglas/reglas/M7-las-dependencias-entre-reglas-se-declaran-y-solo-hay-tres.md) admite. Sin dependencia declarada, la 15 no aplica; y la regla no tiene excepción, así que la 16 tampoco.

La fila **18** pasa —está registrada en [validadores/reglas-validables.md](../../../validadores/reglas-validables.md)— pero allá figuraba con el **título viejo**, de cuando la regla detenía el arranque en vez de dejar la estructura puesta. Se corrigió en la misma pasada.

**Por qué el resultado anterior estaba anulado.** El sello de **v2.5.0**, del **2026-08-07**, dejó de valer al reescribirse la regla en **v5.0.0**: el gate que detenía el arranque pasó a ser una estructura que el instalador deja puesta. Se anotó «a re-aplicar en el próximo repaso» y **nadie volvió a mirarlo durante diez días**, porque nada lo recordaba. Ese olvido es lo que destapó el [pendientes/hecho/el-sello-del-checklist-se-comprueba.md](../../../pendientes/hecho/el-sello-del-checklist-se-comprueba.md), y desde hoy `validar.py metareglas` avisa cuando un sello queda vencido.

**Vuelto a aplicar el 2026-08-18**, porque el texto cambió: entró `pendientes/` a la estructura. Es el [pendiente 61](../../../pendientes/hecho/el-aviso-de-vuelta-llega-a-uno-de-nueve.md) — ocho de nueve proyectos instalados no tenían dónde recibir el aviso de [`02·F24`](F24-el-defecto-del-estandar-se-reporta-no-se-corrige.md), ni dónde escribir un pendiente propio. **Solo se sumó una carpeta a la lista: lo que la regla exige —dejarla puesta antes de trabajar— no cambió.**

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
