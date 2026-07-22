# 07 · Calidad de código

> **Capa 2 · agnóstica al stack.** Cómo se escribe el código para que otro (u otro modelo, meses después) lo entienda y lo cambie sin miedo. La regla rectora: **el código se lee muchas más veces de las que se escribe**; optimizar para el lector. La capa 3 declara el linter, el formateador y el estilo concreto.

---

## Q1 · Escribir código que se lea como el que lo rodea

El código nuevo **imita el código existente** del módulo: misma densidad de comentarios, mismas convenciones de nombres, mismos idiomas (ver `01-conducta.md` C8). Un archivo no debería delatar que lo escribió otra mano.

- Seguir el estilo vigente aunque uno preferiría otro; la consistencia vale más que la preferencia personal.
- No introducir un paradigma o patrón ajeno al del módulo sin acordarlo.

```
INCORRECTO: el módulo usa un estilo y el archivo nuevo trae otro completamente distinto
CORRECTO:   el archivo nuevo se mimetiza con las convenciones del código vecino
```

---

## Q2 · Nombres que revelan la intención

- Nombres **descriptivos y directos**: una variable, función o clase se nombra por lo que representa o hace, no por su tipo ni con abreviaturas crípticas.
- Evitar nombres genéricos (`data`, `temp`, `hacer`, `proceso`) cuando hay uno específico disponible.
- Las funciones se nombran con un verbo; los booleanos, como una afirmación (`estaActivo`, `tienePermiso`).
- Un nombre bien puesto ahorra un comentario.

```
INCORRECTO: function proc(d) { ... }
CORRECTO:   function calcularSaldoDisponible(cuenta) { ... }
```

---

## Q3 · Funciones pequeñas y con una sola responsabilidad

- Cada función hace **una cosa** y opera a **un solo nivel de abstracción**.
- Si una función necesita comentarios que separan "bloques", esos bloques suelen ser funciones que piden nacer.
- Limitar el anidamiento profundo: retornos tempranos y extracción de sub-funciones antes que pirámides de `if`.

```
INCORRECTO: una función de 200 líneas que valida, calcula, guarda, notifica y responde
CORRECTO:   una función que orquesta llamando a validar(), calcular(), guardar(), notificar()
```

---

## Q4 · No repetir (DRY), pero sin abstraer de más

- Lógica de negocio duplicada en varios lugares se **extrae** a un punto único (servicio, función, helper). Un cambio de regla debe tocarse en un solo sitio.
- **Pero:** no crear abstracciones prematuras. Dos usos parecidos no siempre son el mismo concepto; abstraer de más acopla cosas que debían evolucionar por separado. Duplicar una vez y esperar a ver el patrón es válido.

```
INCORRECTO: la misma regla de cálculo copiada en tres componentes → se corrige en dos y se olvida el tercero
CORRECTO:   la regla vive en un servicio; los tres componentes lo llaman
```

---

## Q5 · Comentar el porqué, no el qué

- El código dice **qué** hace; el comentario explica **por qué**, cuando no es obvio (una decisión no evidente, un workaround, una restricción externa).
- No comentar lo que el código ya dice con claridad (ruido que se desactualiza).
- Las decisiones de diseño no obvias van a la documentación (`13-documentacion.md`), no solo a un comentario que nadie relee.

```
INCORRECTO: i = i + 1 // incrementa i
CORRECTO:   // se reintenta hasta 3 veces porque el servicio externo falla de forma intermitente
```

---

## Q6 · Linter y formateador automáticos

El estilo (indentación, comillas, orden de imports) lo resuelve una **herramienta automática**, no la discusión ni el criterio manual. El código se entrega formateado y sin advertencias del linter. Esto elimina ruido en las revisiones y mantiene el diff enfocado en lo que importa.

> El agente no desactiva reglas del linter para "que pase" (mismo espíritu que núcleo `00` · N3); si una regla estorba de verdad, se discute y se ajusta la configuración, no se silencia caso por caso.

---

## Q7 · Dejar el código mejor, pero dentro del alcance

Al tocar un archivo, está bien corregir algo pequeño y cercano si es seguro. Pero **no** refactorizar de más ni "mejorar de paso" código fuera del alcance de la tarea (ver `01-conducta.md` C3): eso infla el diff, mezcla intenciones y dificulta la revisión. Si algo cercano merece mejora, se menciona y se deja para su propia tarea.

---

## Relación con el resto del estándar

- **`01-conducta.md` C3/C8** — no salir del alcance; respetar idioma y estilo del proyecto.
- **`06-rendimiento.md` R6** — no sacrificar legibilidad por optimizaciones sin impacto medible.
- **`13-documentacion.md`** — las decisiones no obvias se documentan, no solo se comentan.
- **`14-estructura-codigo.md`** — dónde vive cada archivo y cómo se nombra.
