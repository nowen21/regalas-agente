# 07 · Calidad de código

El código se lee más veces de las que se escribe: optimiza para el lector. La capa 3 declara linter, formateador y estilo.

---

## Q1 · Escribe como el código que lo rodea

El código nuevo imita al vecino: mismas convenciones, mismos nombres, mismo idioma (`01` · C8). No metas un paradigma ajeno sin acordarlo. La consistencia vale más que la preferencia personal.

```
INCORRECTO: el archivo nuevo trae un estilo distinto al del módulo
CORRECTO:   se mimetiza con el código vecino
```

## Q2 · Nombres que dicen la intención

Nombres descriptivos por lo que representan o hacen, no por su tipo ni abreviados. Evita genéricos (`data`, `temp`, `proceso`). Funciones con verbo; booleanos como afirmación (`estaActivo`, `tienePermiso`). Un buen nombre ahorra un comentario.

```
INCORRECTO: function proc(d) { ... }
CORRECTO:   function calcularSaldoDisponible(cuenta) { ... }
```

## Q3 · Funciones pequeñas, una responsabilidad

Cada función hace **una cosa**, a un solo nivel de abstracción. Si necesita comentarios que separan bloques, esos bloques son funciones. Usa retornos tempranos en vez de pirámides de `if`.

```
INCORRECTO: una función de 200 líneas que valida, calcula, guarda y notifica
CORRECTO:   una que orquesta validar(), calcular(), guardar(), notificar()
```

## Q4 · No repitas (DRY), pero no abstraigas de más

Lógica de negocio duplicada se extrae a un punto único. **Pero** no abstraigas prematuro: dos usos parecidos no siempre son el mismo concepto. Duplicar una vez y esperar el patrón es válido.

```
INCORRECTO: la misma regla copiada en tres lados → se corrige en dos y se olvida el tercero
CORRECTO:   la regla en un servicio; los tres lo llaman
```

## Q5 · Comenta el porqué, no el qué

El código dice **qué**; el comentario, **por qué** (una decisión no obvia, un workaround). No comentes lo que el código ya dice. Las decisiones de diseño van a la documentación (`13`), no a un comentario que nadie relee.

```
INCORRECTO: i = i + 1 // incrementa i
CORRECTO:   // reintenta 3 veces porque el servicio externo falla intermitente
```

## Q6 · Linter y formateador automáticos

El estilo lo resuelve una **herramienta**, no el criterio manual. Entrega el código formateado y sin advertencias del linter. No desactives reglas para "que pase" (`00` · N3); si una estorba, ajusta la config, no la silencies caso por caso.

## Q7 · Deja el código mejor, pero en tu alcance

Corregir algo pequeño y cercano está bien. Refactorizar de más o "mejorar de paso" fuera de la tarea, no (`01` · C3): infla el diff y mezcla intenciones. Si algo cercano merece mejora, dilo y déjalo para su tarea.

---

Ver: `01` C3/C8 (alcance, idioma), `06` R6 (legibilidad), `13` (documentar decisiones), `14` (estructura y nombres).
