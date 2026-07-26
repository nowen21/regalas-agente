# Qué es la triangulación de pruebas

Es una forma de **estar seguro de que una prueba dice la verdad**, confirmando el resultado desde **varios lados independientes** que tienen que dar lo mismo. Si todos coinciden, confiás; si uno no coincide, hay un error escondido.

El nombre viene de la topografía: para saber dónde está exactamente un punto, lo medís desde tres lugares conocidos. Si las tres mediciones se cruzan en el mismo punto, ese es el lugar. Un solo ángulo no te da certeza; tres sí.

## El error que evita

Al probar una función que calcula el total de una factura, la trampa común es:

```
esperado = factura.calcularTotal()   // ← saco el "esperado" del mismo código
assert(factura.calcularTotal() == esperado)
```

Esa prueba **siempre pasa**, pero no prueba nada: compara el código consigo mismo. Si el cálculo está mal, la prueba también está mal, y las dos "mienten" igual.

## Cómo se triangula

El resultado esperado sale de **fuentes que no son el código**, y tienen que coincidir. Ejemplo con la factura (subtotal 100, IVA 19%):

1. **La spec dice:** total = 119.
2. **Cálculo a mano:** 100 + (100 × 0.19) = 119.
3. **Una propiedad que siempre debe cumplirse:** total = subtotal + iva.

Las tres apuntan a **119**. Ese es el valor contra el que se prueba:

```
assert(factura.calcularTotal() == 119)   // 119 vino de 3 fuentes que coinciden
```

Si el código diera 118, la prueba falla — y está bien que falle, porque el código está mal.

## Dos frentes

1. **De dónde salen los casos** que se van a probar: no se inventan a ojo, se derivan con método (los límites: 0, el máximo, vacío; las combinaciones raras; las entradas inválidas).
2. **De dónde sale el resultado esperado** de cada caso: de varias fuentes que coincidan, no del propio código.

**En una frase:** triangular es no creerle a una sola fuente —sobre todo no al código que se está probando— sino cruzar varias hasta estar seguro.

---

> La regla formal está en el estándar: [`base/08-pruebas.md`](../base/08-pruebas.md) · `T7 · Triangulación`.
