# 21 · Automatización de procesos  ·  `[CAPA 2 · opt-in]`

**Opt-in.** Reglas agnósticas para construir un **proceso que corre solo contra sistemas que no se pueden cambiar** — el que opera aplicaciones por su interfaz porque no ofrecen otra puerta. Aplican a proyectos que automatizan trabajo humano repetitivo; el resto las omite.

**El agente construye el proceso, no lo ejecuta.** Produce el diseño, la configuración, la ficha del proceso y sus pruebas; **quien lo corre es el motor de automatización**, y quién lo lanza en producción lo decide el humano ([`00·N2`](00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada), [`00·N4`](00-nucleo-blindado.md#n4--nada-destructivo-sobre-datos-reales-sin-autorización-de-esa-operación-blindada)). El motor concreto lo declara la capa 3 (`.agente/stack.md`).

**Lo que lo separa del software corriente:** acá el sistema del otro lado **no se puede cambiar ni avisar**. Si la pantalla se mueve, el proceso se rompe y nadie lo sabe hasta que alguien mira. Casi todas estas reglas salen de eso.

---

## AU1 · Lo que el proceso hace se separa de dónde lo hace

La **secuencia de negocio** —qué pasos se dan y en qué orden— vive aparte de **cómo se alcanza cada elemento** de la pantalla. Cuando el sistema del otro lado cambia de aspecto, se toca solo el segundo.

```
INCORRECTO: la secuencia lleva incrustada la posición del botón, y mover
            el botón obliga a reescribir el proceso entero
CORRECTO:   la secuencia dice «confirmar», y en otro sitio está cómo se
            alcanza «confirmar» hoy
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v24.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Es la primera del capítulo porque de ella dependen todas las demás.** Un proceso donde la secuencia y la pantalla están mezcladas no se puede probar, ni reintentar, ni arreglar sin rehacerlo.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## AU2 · El elemento se alcanza por lo que es, no por dónde está

Cada elemento con el que el proceso interactúa se identifica por **algo que lo describa** —su nombre, su etiqueta, su papel en la pantalla—, nunca por su posición ni por una coordenada. La posición cambia con la resolución, el idioma y la versión; lo que el elemento *es*, no.

```
INCORRECTO: hacer clic en la coordenada 340, 512
CORRECTO:   hacer clic en el elemento cuyo nombre es «Guardar»
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v24.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Extiende [`AU1`](#au1--lo-que-el-proceso-hace-se-separa-de-dónde-lo-hace):** aquella separa el *dónde*; esta dice cómo escribir ese *dónde* para que aguante.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## AU3 · El trabajo se toma de una cola y cada ítem se cierra solo

El proceso no recorre una lista en memoria: **toma un ítem de una cola, lo termina y lo marca**, uno por uno. Así se sabe qué se hizo y qué no cuando algo se corta a la mitad, y otro puede seguir desde ahí.

```
INCORRECTO: se leen las 400 facturas al empezar y se procesan en un bucle;
            se corta en la 180 y nadie sabe cuáles quedaron hechas
CORRECTO:   cada factura es un ítem de la cola, y su estado dice si se hizo
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v24.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Extiende [`03·D6`](03-datos.md#d6--la-operación-repetida-no-duplica-su-efecto):** repetir un ítem no puede duplicar su efecto, y acá repetir es lo normal — un corte a mitad de camino se retoma reprocesando lo que quedó abierto.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## AU4 · El fallo del negocio y el fallo del sistema no se tratan igual

El ítem que **no debía procesarse** —le falta un dato, no cumple una condición— se aparta con su motivo y el proceso sigue. El fallo **del sistema** —la pantalla no cargó, se cayó la sesión— se reintenta, y si insiste se detiene. Confundirlos reintenta eternamente lo que nunca iba a funcionar.

```
INCORRECTO: la factura sin cliente hace fallar el proceso entero
CORRECTO:   esa factura se aparta con su motivo y las otras 399 siguen
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v24.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Extiende [`05·E2`](05-errores-y-logging.md#e2--valida-al-entrar-y-aborta-temprano):** aquella dice abortar temprano; acá hay que distinguir **de qué** se aborta — abortar el ítem no es abortar la corrida.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## AU5 · El proceso no guarda con qué entra a ningún sistema

Las credenciales con las que el proceso entra a los sistemas se piden a un **almacén seguro en el momento de usarlas**, y no viven en su configuración, en su código ni en sus registros. Un proceso automático corre sin nadie mirando: si deja una clave escrita, la deja escrita para siempre.

```
INCORRECTO: la clave del sistema va en la configuración del proceso
CORRECTO:   el proceso la pide al almacén cuando la necesita y no la conserva
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v24.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Extiende [`00·N6`](00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada)**, que ya lo prohíbe para cualquier proyecto. Lo que agrega es el **momento**: acá no hay una persona que la escriba al arrancar, así que el proceso tiene que ir a buscarla solo.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## AU6 · Se prueba contra un entorno que no es el de verdad

El proceso se prueba contra **sistemas de prueba y datos inventados**, nunca contra los productivos. Lo que el entorno de prueba no puede reproducir se comprueba a mano y **queda escrito qué se comprobó así**.

```
INCORRECTO: se prueba «con cuidado» contra el sistema real, en horario de poco uso
CORRECTO:   se prueba contra el de prueba, y lo que solo existe en el real
            se verifica a mano y se anota
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v24.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Extiende [`08·T4`](08-pruebas.md#t4--protege-los-datos-reales-al-probar).** Lo propio de acá es que **el proceso actúa como un usuario**: no hay transacción que revertir ni entorno aislado que borrar — lo que tocó, tocado queda.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## AU7 · Cada proceso trae su ficha, y la ficha se mantiene

Todo proceso automatizado lleva una **ficha versionada** que dice qué hace, qué sistemas toca, con qué entra, qué se aparta y qué se reintenta. Se actualiza con el proceso, no después. Sin ella, el día que se rompa nadie sabe qué debía hacer.

```
INCORRECTO: el proceso corre hace un año y lo que hace solo lo sabe quien lo escribió
CORRECTO:   su ficha dice qué hace y qué toca, y se actualizó con el último cambio
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v24.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Extiende [`13·DOC13`](13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)**, que ya pide el catálogo de módulos. Acá el módulo es **un proceso que corre solo**, y lo que hay que saber de él es distinto: qué sistemas ajenos toca y con qué entra.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## AU8 · Una corrida que no se mira no está terminada

Cada corrida deja **cuántos ítems entraron, cuántos se completaron, cuántos se apartaron y por qué**, en un sitio que alguien mire. Un proceso que corre solo y falla en silencio deja de hacer su trabajo sin que nadie se entere, a veces por meses.

```
INCORRECTO: el proceso corre cada noche y nadie sabe que hace tres semanas
            aparta el 90 % de los ítems
CORRECTO:   el resumen de cada corrida queda a la vista, con lo apartado y su motivo
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v24.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | ✅ ✅ N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 19 ✅ · 0 ❌ · 1 N/A.**

**Es la regla que cierra el capítulo, y la que más se incumple.** Un proceso automatizado se instala, funciona, y **se vuelve invisible**: nadie mira lo que no falla ruidosamente. Extiende el capítulo [`19`](19-observabilidad-y-operacion.md), que es opt-in por su cuenta — si este capítulo está encendido, esta regla vale aunque aquel no lo esté.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.
