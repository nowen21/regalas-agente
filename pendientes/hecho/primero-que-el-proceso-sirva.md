# Pendiente · Primero que el proceso sirva, después se automatiza

**Estado:** abierto · anotado 2026-08-13.

| | |
|---|---|
| **Historia de usuario** | [EP-001 · HU-007 — La regla que gobierna cómo se escriben las reglas](../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/HU-007-regla-de-las-reglas.md) — «no se automatiza hasta que se sepa que sirve» es meta-regla: gobierna a las demás |

Agregarle al [pendiente 09](autonomia-sin-ia.md) un criterio que hoy le falta, y dejarlo escrito como meta-regla: **una regla no se automatiza hasta que se sepa que sirve.**

## El problema

El pendiente 09 tiene un solo criterio para decidir qué se automatiza:

> Si el resultado depende de leer, entender o decidir, lo hace la IA. Si se puede escribir como una comparación, una plantilla o un disparo, lo hace un programa.

Ese criterio contesta **si se puede** automatizar. No contesta **si conviene**. Y son preguntas distintas: una regla mal escrita se puede automatizar perfectamente, y el resultado es que ahora falla sola, en cada commit, sin que nadie la haya vuelto a leer.

El propio pendiente 09 ya tropezó con esto sin nombrarlo. El ítem 06 (la puerta `F2`) es de prioridad alta y quedó de penúltimo, porque sin las piezas 04 y 12 su tasa de falsos positivos lo vuelve inservible. Eso es exactamente lo que este criterio predice: el proceso todavía no está listo, así que automatizarlo produce ruido. Lo que pasó fue que se descubrió caso por caso en vez de aplicarse como regla.

## De dónde sale

De los apuntes del diplomado, módulo 1, clase del 06 de agosto. El orden que la clase deja escrito es:

> Eficiencia → Agilidad → Automatización

En ese orden y no en otro, porque automatizar un proceso ineficiente y con datos malos multiplica el error a velocidad de máquina.

Es el mismo hallazgo del módulo 2, dicho para el mundo de las empresas: los tres retos de implementar IA son sistemas heredados, calidad de datos y aceptación del personal, y ninguno se resuelve comprando el modelo. La automatización llega de última porque es la que menos perdona lo que venía mal.

## Qué habría que hacer

**1. La pregunta previa.** Antes de promover cualquiera de los 16 ítems del 09 a pendiente propio, contestar tres cosas por escrito:

- ¿La regla se cumple hoy a mano, y produce el resultado que se buscaba?
- ¿Cuántas veces se incumplió, y por descuido o porque estaba mal escrita?
- Si se automatiza tal como está, ¿cuántas falsas alarmas va a dar la primera semana?

Si la segunda respuesta es «porque estaba mal escrita», lo que toca es arreglar la regla, no construir el validador. Automatizarla es congelar el error y ponerlo a repetirse.

**2. La meta-regla.** El capítulo `20` ya tiene `M9`, que decide si una regla es validable. Le falta el paso siguiente: que sea validable no significa que ya se deba validar. Puede ser una regla nueva o un renglón dentro de `M9`, y eso se resuelve al escribirla ([`20·M12`](../../base/20-meta-reglas/reglas/M12-antes-de-crear-una-regla-buscar-la-duplicacion-es-el-defecto-mas-caro.md) manda buscar antes de crear).

**3. El dato que hace falta.** La segunda pregunta no se puede contestar hoy: nadie cuenta cuántas veces falla cada regla. Ese conteo es el ítem 11 del 09, y con este criterio deja de ser una métrica bonita y pasa a ser entrada obligatoria de la decisión. Vale adelantarlo por eso.

## El riesgo de este criterio

Que se use como excusa para no automatizar nunca, porque siempre se puede decir que el proceso todavía no está maduro. El corte es concreto: si la regla se viene cumpliendo bien a mano y lo que falla es acordarse, se automatiza ya. Una regla que se cumple cuando alguien se acuerda, no se cumple, y esa frase también es del 09.

---

# Dónde encalla de verdad — medido el 2026-08-18

**No es que falte una fase: es que falta el criterio.**

Este pendiente está enrutado a [EP-001 · HU-007](../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/HU-007-regla-de-las-reglas.md) porque es «la regla de las reglas». Pero sus tres criterios de aceptación son:

| | Qué exige |
|---|---|
| `CA-01` | una regla nueva se enruta al capítulo correcto |
| `CA-02` | una regla atada a un stack no entra |
| `CA-03` | una regla que exige dos cosas se parte antes de entrar |

**Ninguno cubre lo que este pendiente pide.** Y por [`02·F19`](../../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md) la redacción del CA **es** la especificación: construir fuera de ella es lo que [`02·F20`](../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md) manda proponer, no hacer.

**Así que hace falta una de dos, y las dos son del usuario:**

1. **Un criterio nuevo en `HU-007`.** Cambia la historia, que ya tiene una fase cerrada contra los tres actuales.
2. **Una historia propia.** Más limpio, y deja `HU-007` como está.

> **Es el mismo hueco del [pendiente 60](cada-capitulo-tiene-su-historia.md), un piso más abajo.** Allá ningún capítulo tiene historia que lo escriba; acá la historia existe y **sus criterios no llegan**. Enrutar un pendiente a una historia no lo deja construible: hay que mirar si algún criterio lo cubre.
