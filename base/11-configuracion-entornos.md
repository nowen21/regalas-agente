# 11 · Configuración y entornos  ·  `[CAPA 2]`

> **Historia dueña del texto:** [EP-001 HU-024](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-024-el-capitulo-11-configuracion-y-entornos/HU-024-el-capitulo-11-configuracion-y-entornos.md). Todo cambio de este capítulo baja por ella (`02·F23`).

Lo que cambia entre entornos (local, pruebas, producción) y lo que se configura sin tocar código. La capa 3 declara los entornos y el mecanismo concretos.

---

## CFG1 · La configuración vive fuera del código

Lo que cambia entre entornos (credenciales, URLs, claves, flags de entorno) se lee de la **configuración de entorno**. El mismo código corre en todos lados; cambia la config que recibe. Secretos, nunca en el código ([`00·N6`](00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada), [`04·S4`](04-seguridad.md#s4--guarda-los-secretos-fuera-del-código-y-rota-el-que-se-expuso)).

> Esto es config de **infraestructura**. Los valores **del negocio** que un admin cambiaría (umbrales, listas, textos) van a **catálogo en la BD** ([`03·D4`](03-datos.md#d4--lo-que-puede-cambiar-por-decisión-de-alguien-va-a-catálogo)).

```
INCORRECTO: la URL del servicio de pago en el código con un if por entorno
CORRECTO:   leerla de la configuración; cada entorno trae la suya
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**El análisis del 2026-08-07 la marcaba en amarillo por dueño**, porque solapa con [`04·S4`](04-seguridad.md#s4--guarda-los-secretos-fuera-del-código-y-rota-el-que-se-expuso). Se revisó: **no la repite, la enlaza** — la regla dice que la configuración vive fuera del código y remite a `S4` para el secreto en sí. Eso es exactamente lo que pide la fila 4 cuando dos capítulos se rozan, y lo que la 11 prohíbe es copiar el cuerpo, no nombrar al vecino.

La nota que la separa de [`03·D4`](03-datos.md#d4--lo-que-puede-cambiar-por-decisión-de-alguien-va-a-catálogo) —config de infraestructura contra valores de negocio— es lo que evita el choque de la fila 17, y el propio análisis la daba por «bien resuelta».

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## CFG2 · El entorno real no se versiona; sí una plantilla

El archivo con valores reales está **ignorado** ([`09·G3`](09-git.md#g3--deja-fuera-del-control-de-versiones-los-secretos-y-lo-generado)). Se versiona una **plantilla de ejemplo** con todas las variables **sin valores**, y se documenta qué es cada una y cuáles son obligatorias.

```
INCORRECTO: versionar el archivo de entorno con las claves reales
CORRECTO:   versionar la plantilla vacía; el real queda en cada entorno
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

Mismo caso que `CFG1`: el análisis la marcaba por solapar con [`09·G3`](09-git.md#g3--deja-fuera-del-control-de-versiones-los-secretos-y-lo-generado) y con `04·S4`, y **las enlaza en vez de repetirlas**. `G3` dice qué no se versiona; esta dice qué se versiona **en su lugar** —la plantilla sin valores— y qué hay que documentar de ella. Son dos caras, no una copia.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## CFG3 · Los entornos se parecen lo suficiente para que probar signifique algo

El entorno donde se prueba corre **las mismas versiones y la misma configuración estructural** que el de producción. Sin eso, «funciona en mi máquina» no dice nada, y lo que no se puede reproducir se cubre con comprobaciones manuales escritas ([`08·T4`](08-pruebas.md#t4--protege-los-datos-reales-al-probar)).

```
INCORRECTO: se prueba contra una versión distinta del motor «porque es lo que hay»
CORRECTO:   se iguala la versión, o se anota qué queda sin probar y cómo se comprueba
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.22.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Partida el 2026-08-18.** Decía dos cosas: que los entornos se parezcan, y que lo que producción necesita se documente. **Se cumplen por separado** — se pueden tener entornos idénticos y seguir aplicando cambios de producción de memoria. La segunda es ahora [`CFG5`](#cfg5--lo-que-producción-necesita-se-escribe-antes-de-aplicarlo). Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## CFG5 · Lo que producción necesita se escribe antes de aplicarlo

Todo cambio que haya que hacer en producción —una variable, un permiso, un paso de instalación— queda **escrito antes de aplicarse**, no se hace de memoria (extiende [`11·CFG3`](#cfg3--los-entornos-se-parecen-lo-suficiente-para-que-probar-signifique-algo)).

```
INCORRECTO: «también hay que subirle la variable nueva, me acuerdo cuando toque»
CORRECTO:   el paso queda escrito con su valor y quién lo aplica
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.22.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Nace el 2026-08-18 de partir [`CFG3`](#cfg3--los-entornos-se-parecen-lo-suficiente-para-que-probar-signifique-algo).** Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**Por qué merece regla propia.** `CFG3` es sobre **el parecido** entre entornos; esta es sobre **lo que no se puede parecer** y hay que arrastrar a mano. Es la que se incumple: el parecido se nota al probar, y el paso olvidado se nota al desplegar.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## CFG4 · Cambios de comportamiento tras banderas

Funcionalidad que conviene activar/desactivar sin desplegar (en progreso, arriesgada, de un cliente) va tras una **bandera** (feature flag): permite apagar rápido sin revertir código. Limpia las banderas obsoletas — una eterna es deuda.

```
INCORRECTO: la bandera se enciende al liberar y nadie la quita; dos años después
            nadie sabe si el código de abajo se ejecuta
CORRECTO:   la bandera nace con la fecha en que se retira, y al retirarla se borra
            también la rama que ya no se usa
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**La fila 12 reprobaba y se corrigió en esta pasada.** No tenía ejemplo, y el análisis del 2026-08-07 decía por qué hacía falta: *«la bandera eterna es error frecuente»*. Una regla que nombra un error frecuente no entra en la excepción de «evidente y no se puede malinterpretar».

El ejemplo que se agregó es el error de verdad —la bandera que se enciende al liberar y nadie quita—, no uno exagerado, que es lo que la fila pide. **No cambia qué exige la regla.**

La fila **9** pasa: limpiar las banderas obsoletas no es una exigencia aparte sino la otra mitad de la misma —poner una bandera sin retirarla deja el código en un estado que nadie sabe leer.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

---

Ver: `00` N6 (secretos), `04` S4, `09` G3 (plantilla versionada), `03` D4 (negocio → catálogo), `08` T4 / `13` (diferencias documentadas).
