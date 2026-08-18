# 17 · Interfaz y experiencia de usuario  ·  `[CAPA 2 · opt-in]`

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
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

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
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

Cumplía en el análisis del 2026-08-07 y se volvió a contar: 186 de 320.

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

## I3 · Accesibilidad mínima

- Campos con **etiqueta** asociada; imágenes con texto alternativo.
- **Contraste** suficiente entre texto y fondo.
- Navegable por **teclado**, con el **foco visible**.
- No transmitir información **solo** por color.

> El nivel exigido (p. ej. WCAG AA) y si es obligatorio por ley lo declara la capa 3 / `16` (accesibilidad).

---

### Checklist  ·  **NO CUMPLE**

Aplicado el [checklist del estándar](20-meta-reglas/checklist.md) contra **v23.4.0**, el **2026-08-18**.

| Bloque | Filas | Resultado |
|---|---|---|
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ❌ ✅ ✅ N/A ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 15 ✅ · 1 ❌ · 4 N/A.**

**Fila 9 · son cuatro exigencias, y se cumplen por separado.** Etiquetas asociadas, contraste, navegación por teclado y no transmitir información solo por color: una interfaz puede tener las etiquetas impecables y el contraste ilegible. El análisis del 2026-08-07 ya lo decía.

**Y ofrecía la salida buena, que no es partirla en cuatro:** *«partir o declarar checklist»*. Cuatro reglas de una línea cada una llenan el capítulo de ruido; **un checklist de accesibilidad con su regla que obliga a pasarlo** dice lo mismo y se puede comprobar. Es lo mismo que el estándar hace consigo en [base/20-meta-reglas/checklist.md](20-meta-reglas/checklist.md).

Cuál de las dos, y el ejemplo que también le falta, van al [pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

La nota sobre el nivel exigido —WCAG y si es obligatorio por ley— remite bien a la capa 3 y al capítulo `16`: eso no es lo que falla.

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
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

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
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

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
| A · Dónde va | 1–4 | ✅ ✅ ✅ ✅ |
| B · Cómo se identifica | 5–6 | ✅ ✅ |
| C · Cómo está escrita | 7–13 | ✅ ✅ ✅ ✅ ✅ ✅ ✅ |
| D · Cómo se relaciona | 14–17 | N/A N/A N/A ✅ |
| E · Fuera de su texto | 18–20 | ✅ ✅ ✅ |

**20 filas: 17 ✅ · 0 ❌ · 3 N/A.**

**Dos filas reprobaban y las dos se corrigieron en esta pasada. Ninguna cambia qué exige la regla.**

- **Fila 8 · el título manda.** Se llamaba «Adaptable»: **una sola palabra**, que ni ordena ni enuncia nada. Pasa a *Funciona en los tamaños de pantalla que el proyecto soporta*, que es lo que la regla pide y se entiende leyéndolo en un índice.
- **Fila 12 · ejemplo.** No tenía. El que se agregó es el caso concreto que la regla ya nombraba sin mostrar: la tabla ancha que saca una barra de desplazamiento a la página entera.

Es el tercer título de una palabra o de tema que se corrige hoy, después de [`15·IM2`](15-registros-inmutables.md#im2--guarda-los-tres-estados-y-la-trazabilidad-de-quien-anula) y [`12·PR5`](12-privacidad-datos.md#pr5--define-cuánto-se-conservan-y-qué-pasa-después). **Los tres estaban en capítulos que nadie había vuelto a mirar desde julio.**

> Vale mientras el texto de arriba no cambie. Si la regla se edita, este resultado queda **anulado** y se vuelve a aplicar el checklist.

---

Ver: [`01·C8`](01-conducta.md#c8--habla-el-idioma-del-proyecto) (idioma del proyecto), [`05·E3`](05-errores-y-logging.md#e3--mensajes-en-dos-niveles-usuario-y-diagnóstico) (mensajes de error accionables), `16` (accesibilidad/WCAG si aplica). El framework y el sistema de diseño concretos van en la capa 3.
