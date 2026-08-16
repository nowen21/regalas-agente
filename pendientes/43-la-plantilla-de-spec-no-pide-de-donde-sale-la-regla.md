# Pendiente · La plantilla de especificación no pide de dónde sale una regla de negocio

**Estado:** abierto · anotado 2026-08-16.

| | |
|---|---|
| **Proyecto de origen** | **`shopnest-mesa`** · `C:/DesarrollosClaude/personales/shopnest-mesa` |
| **Su pendiente de seguimiento** | [`pendientes/05-la-plantilla-de-spec-no-pide-la-fuente.md`](../../../../DesarrollosClaude/personales/shopnest-mesa/pendientes/05-la-plantilla-de-spec-no-pide-la-fuente.md) — queda **abierto allá** hasta que este se corrija |
| **A quién avisar al cerrar** | a `shopnest-mesa`, para que cierre el suyo |

El proyecto no tocó nada del estándar: reportó y siguió con lo suyo.

## El problema

El §4 de [`plantillas/plantilla-spec-modulo.md`](../plantillas/plantilla-spec-modulo.md) pide esto:

```
## 4. Reglas de negocio

[[Las invariantes que el código debe garantizar y que no se ven leyendo un archivo suelto — regla `13`·DOC2.]]

1. «Regla — por qué existe.»
```

Pide **el porqué**. Nunca **el de dónde**.

Una regla de negocio no se inventa en la especificación de un módulo: baja desde un requisito o una historia de usuario. Pero la plantilla no lo pregunta, así que una regla con buena justificación y ninguna procedencia entra sin resistencia y sin dejar rastro de que entró.

## El caso que lo destapó

En `shopnest-mesa`, `documentacion/problemas/spec.md` traía como regla 5:

> **Un problema no se cierra sin causa raíz ni solución definitiva.** Cerrar un problema es afirmar que ya no va a volver, y eso no se puede afirmar sin saber por qué pasaba ni qué se hizo.

Impecable como justificación. Y no la pide nadie: ni el enunciado del taller (que enumera cinco reglas y esta no es ninguna), ni `requisitos.md` —cuyo RF-13 manda *registrar* esos campos, no exigirlos al cerrar—, ni la épica, ni la historia de usuario de las reglas. **Nació en la especificación del módulo.**

De ahí bajó sola a una decisión (`D-22`), una fila de trazabilidad, dos escenarios de prueba y un criterio de aceptación. Iba camino al código. Se retiró el 2026-08-16, y el pendiente que la tenía en espera se cerró: no había a quién preguntarle, porque la regla no era de nadie.

**Tardó un día en verse**, y solo porque alguien preguntó de dónde salía. Nada del proceso lo preguntaba.

## Por qué la plantilla ya sabe hacerlo, pero solo para los campos

En el mismo proyecto, la tabla de campos de `spec.md` §5.1 lleva una columna **Origen**, con valores como `Molde · RF-13` y notas explícitas como **«no estaba en el taller»**. Ahí sí se ve de un vistazo qué vino del enunciado y qué agregó el equipo.

Esa columna **no está en la plantilla**: el proyecto la inventó por su cuenta. Para los campos resolvió el problema; para las reglas, nadie lo pensó. Es la misma necesidad y la solución ya está probada en el terreno.

## Qué falta

**1 · El §4 de la plantilla pide las dos cosas.** El molde de cada regla pasa a ser algo como:

```
1. «Regla — de dónde sale (requisito, HU o decisión con su identificador) — por qué existe.»
```

Con la nota de que una regla sin procedencia **no se escribe acá**: se sube a la historia que corresponda y baja desde allá.

**2 · La comprobación.** Una regla de §4 sin identificador de origen es detectable. Encaja con lo que ya hace `validadores/trazabilidad.py`; conviene mirar si es ahí o en `validadores/plantillas.py`.

**3 · Mirar los demás §4 ya escritos.** El estándar no reabre lo cerrado, pero conviene saber cuántas especificaciones vivas tienen reglas sin fuente. En `shopnest-mesa` fue una de seis en el primer módulo que se miró.

## Con qué se cruza

- **[30 · El checklist no ve la cadena](30-el-checklist-no-ve-la-cadena.md)** y **[38 · El validador de la F22 se escribió sin su fase](38-el-validador-de-la-f22-se-escribio-sin-su-fase.md)** son el mismo hueco por otro lado: allá el código se saltó la cadena hacia arriba, acá una regla se la saltó hacia abajo. **Conviene mirarlos juntos**, porque una comprobación de cadena que mire en las dos direcciones los cubre a los tres.

## Cómo se sabe que cerró

El §4 de la plantilla pide la procedencia, una regla sin ella reprueba en un validador, y `shopnest-mesa` recibió el aviso.
