# 17 · Interfaz y experiencia de usuario  ·  `[CAPA 2 · opt-in]`

> **Historia dueña del texto:** [EP-001 HU-030](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-030-el-capitulo-17-interfaz-y-experiencia-de-usuario/HU-030-el-capitulo-17-interfaz-y-experiencia-de-usuario.md). Todo cambio de este capítulo baja por ella ([`02·F23`](02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md)).

**Opt-in.** Reglas agnósticas para lo que ve y usa el **usuario final**. Aplican a proyectos con interfaz (web, escritorio, móvil); un proyecto sin UI (librería, servicio backend, CLI) las omite. El framework, el sistema de diseño y el estándar de accesibilidad concretos los declara la capa 3.

---

## I1 · Toda vista resuelve sus tres estados

Ninguna pantalla queda en blanco ni muestra un error crudo. Los tres se definen siempre:

- **Vacío** → un mensaje claro y, si aplica, la acción que lo llena.
- **Cargando** → un indicador, no una pantalla congelada.
- **Error** → un mensaje entendible y accionable, **nunca** una traza ([`05·E3`](05-errores-y-logging.md#e3--mensajes-en-dos-niveles-usuario-y-diagnóstico)).

```
INCORRECTO: la tabla aparece vacía sin explicar si no hay datos o si falló la carga
CORRECTO:   estado vacío ("no hay registros"), estado cargando, y estado de error diferenciados
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.7.5**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**La fila 10 reprobaba y se corrigió en esta pasada: de 395 caracteres a 293**, para un molde de 320. Se fue la explicación de cada estado —cuándo ocurre— y quedó qué hay que mostrar. Los tres estados eran una sola exigencia y siguen siéndolo.

**No cambia qué exige.** Lo que se fue era explicación, no norma.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## I2 · Feedback de validación claro

Cuando el usuario se equivoca en un formulario, se le dice **qué campo** y **qué falta**, en su idioma ([`01·C8`](01-conducta.md#c8--habla-el-idioma-del-proyecto)), antes o al enviar. No se rechaza en silencio ni con un mensaje genérico.

```
INCORRECTO: "Error al guardar" sin decir qué campo está mal
CORRECTO:   "El correo no es válido" junto al campo correspondiente
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

Cumplía en el análisis del 2026-08-07 y se volvió a contar: 186 de 320.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## I3 · Accesibilidad mínima

La interfaz cumple el **mínimo de accesibilidad**: esta lista cerrada, entera y no a medias.

- Campos con **etiqueta** asociada; imágenes con texto alternativo.
- **Contraste** suficiente entre texto y fondo.
- Navegable por **teclado**, con el **foco visible**.
- Ninguna información transmitida **solo** por color.

> El grado exigido y si la ley lo obliga lo declara la capa 3, con el capítulo [`16`](16-cumplimiento-y-calidad.md).

```
INCORRECTO: la pantalla tiene etiquetas impecables y se entrega como accesible,
            con el texto en gris claro sobre blanco y el estado de cada fila
            indicado solo con un punto de color
CORRECTO:   los cuatro puntos de la lista, comprobados juntos antes de entregar
```

---

### Checklist  ·  **CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v30.8.0**, el **2026-08-22**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1-4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5-6 | ✅ ✅ |
| C · Cómo está escrita | 7-13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14-17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18-20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Resuelta el 2026-08-22, con la salida que eligió el usuario (pendiente 19):** de las dos que el pendiente dejó escritas, **una regla que exige el mínimo con la lista como su contenido**, no cuatro reglas. Era la última de las 26 candidatas a partirse.

**Por qué la fila 9 pasa a ✅.** El sello traía dos lecturas opuestas escritas una debajo de la otra: la del 2026-08-07 decía «son cuatro exigencias y se cumplen por separado» y la del 2026-08-18 decía que son la definición de una sola. Con la decisión del usuario queda una: **el mínimo se cumple entero o no se cumple**, y el cuerpo ahora lo dice con esas palabras, en vez de dejarlo a la interpretación de quien lea la lista.

**Y gana el ejemplo que le faltaba** (fila 12, que estaba N/A): una pantalla con las etiquetas perfectas y el contraste ilegible es exactamente el caso que la regla rechaza.

**Mirada el 2026-08-18 para partirla, y se decidió que no.** Sus cuatro puntos —etiqueta, contraste, teclado, color— parecen cuatro exigencias, pero **son la definición de una sola**: qué es el mínimo. Partirlas daría cuatro reglas que nadie citaría por separado, y dejaría sin dueño la pregunta que importa —*«¿cuál es el mínimo?»*—, que es justo lo que esta contesta.

**La prueba de la fila 9 es si se cumplen por separado.** Acá no: una interfaz con etiquetas y sin contraste no cumple «la accesibilidad mínima» a medias — **no la cumple**. Es una lista cerrada, como la escala de [`05·E4`](05-errores-y-logging.md#e4--loguea-con-niveles-y-con-propósito), no una acumulación de exigencias.

Del [pendiente 19](../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md).


> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## I4 · Texto para el usuario, no jerga

Lo que el usuario lee se entiende sin ser del oficio: **claro, directo, que hasta un niño lo entienda**. Sin siglas internas, sin códigos de sistema, sin jerga técnica. (Es el mismo estándar de [`00·ID7`](00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md) llevado a la pantalla del producto; lo que se suma acá es que no asomen siglas ni códigos internos.)

```
INCORRECTO: "Error 422: constraint violation en FK proyecto_id"
CORRECTO:   "No se pudo guardar: primero elegí un proyecto"
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

Cumplía en el análisis del 2026-08-07, que además anota algo útil: **es la regla que fija la frontera de qué se le escribe al usuario y qué al registro**, y por eso el capítulo `20` la cita al explicar cómo se redacta.

Se volvió a contar: 303 de 320. **Pasa raspando**, y queda dicho.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## I5 · Consistencia con el sistema de diseño

Usar los componentes y patrones que el proyecto ya tiene (el sistema de diseño lo declara la capa 3) antes de inventar unos nuevos. Una pantalla nueva se parece a las demás: mismos componentes, misma ubicación de las acciones, mismos estados.

```
INCORRECTO: la pantalla nueva trae su propio botón, su propio modal y las
            acciones a la izquierda, porque «quedaba mejor»
CORRECTO:   los componentes que ya existen, y las acciones donde el usuario
            ya sabe buscarlas
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

**La fila 12 reprobaba y se corrigió en esta pasada:** no tenía ejemplo. El que se agregó es el error de verdad —la pantalla nueva con su propio botón y las acciones donde no van, «porque quedaba mejor»—. **No cambia qué exige la regla.**

La fila **9** pasa: usar los componentes que ya existen y que la pantalla nueva se parezca a las demás son la misma exigencia dicha desde el medio y desde el resultado.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## I6 · Funciona en los tamaños de pantalla que el proyecto soporta

La interfaz se ve y funciona en los tamaños de pantalla que el proyecto soporta (declarados en capa 3). El contenido ancho (tablas, diagramas) no rompe el layout: se desplaza en su propio contenedor.

```
INCORRECTO: una tabla de doce columnas que empuja el layout y saca una barra
            de desplazamiento a la página entera
CORRECTO:   la tabla se desplaza dentro de su contenedor; la página no
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

**Dos filas reprobaban y las dos se corrigieron en esta pasada. Ninguna cambia qué exige la regla.**

- **Fila 8 · el título manda.** Se llamaba «Adaptable»: **una sola palabra**, que ni ordena ni enuncia nada. Pasa a *Funciona en los tamaños de pantalla que el proyecto soporta*, que es lo que la regla pide y se entiende leyéndolo en un índice.
- **Fila 12 · ejemplo.** No tenía. El que se agregó es el caso concreto que la regla ya nombraba sin mostrar: la tabla ancha que saca una barra de desplazamiento a la página entera.

Es el tercer título de una palabra o de tema que se corrige hoy, después de [`15·IM2`](15-registros-inmutables.md#im2--el-registro-tiene-tres-estados-y-solo-uno-es-editable) y [`12·PR5`](12-privacidad-datos.md#pr5--define-cuánto-se-conservan-y-qué-pasa-después). **Los tres estaban en capítulos que nadie había vuelto a mirar desde julio.**

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

---

Ver: [`01·C8`](01-conducta.md#c8--habla-el-idioma-del-proyecto) (idioma del proyecto), [`05·E3`](05-errores-y-logging.md#e3--mensajes-en-dos-niveles-usuario-y-diagnóstico) (mensajes de error accionables), `16` (accesibilidad/WCAG si aplica). El framework y el sistema de diseño concretos van en la capa 3.
