# Pendiente · La norma del español de Colombia no tiene regla

**Estado:** abierto, anotado el 2026-09-27.

| | |
|---|---|
| **Historia de usuario** | Por asignar: nace al aprobarse este pendiente, como hija de [EP-001 · Cuerpo de reglas heredable](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/epica.md) |
| **De dónde sale** | La sesión del 2026-09-27: el usuario preguntó cuál era la regla del español colombiano y no había una que lo dijera |
| **Proyecto de origen** | El estándar mismo |

## El problema

[`00·ID10`](../base/00-identidad-y-rol/reglas/ID10-escribe-en-el-idioma-del-proyecto-en-tercera-persona-y-en-infinitivo.md) fija tres cosas: la variedad del idioma del proyecto, la tercera persona y el infinitivo. **No fija cómo se escribe bien en esa variedad.** La ortografía, el léxico, la gramática y la redacción del español colombiano no están exigidos por ninguna regla.

Lo que hay está repartido y a medias:

- La sección 5 de [`marcadores-de-ia.md`](../base/00-identidad-y-rol/marcadores-de-ia.md#L73), «El español que no es de acá», trae léxico y algo de gramática colombianos, pero como marcas de generación automática. Ortografía no trae.
- El cierre del mismo anexo, en la [línea 135](../base/00-identidad-y-rol/marcadores-de-ia.md#L135), dice que exigir «norma correcta y variedad colombiana necesita su propia regla, y todavía no existe». La mitad de la variedad ya la cubre `ID10`, así que la frase quedó a medio desactualizar.
- El [pendiente 93](93-la-norma-de-redaccion-vive-dentro-de-dos-plantillas.md) dejó la ortografía y la gramática fuera a propósito, en su sección «El límite»: «son otra regla».

## Por qué importa

El usuario tuvo que pedir «español colombiano» **tres veces** antes de que quedara escrito como recuerdo del repositorio ([pendiente 85](85-las-conversaciones-completas-no-se-pueden-analizar.md#L27)). Una corrección que se repite es una regla que falta.

Sin la regla, un texto sin tildes de pregunta, con *vosotros* o con *eventualmente* por *finalmente* no incumple nada que se pueda citar. `ID8` lo atrapa solo si coincide con una marca de su lista, y la lista no trata la norma.

## Qué falta

Una regla nueva en el capítulo 00, por el procedimiento de las meta-reglas del [capítulo 20](../base/20-meta-reglas/base.md). Borrador acordado con el usuario el 2026-09-27:

```markdown
## ID12 · Escribe con la norma del español de Colombia

Si el proyecto declara español de Colombia, lo que el agente entrega sigue
la norma culta colombiana en ortografía, léxico, gramática y redacción, y se
relee contra el anexo `espanol-de-colombia.md` igual que contra la lista de
marcas. Rige también la respuesta del chat (extiende `00·ID8`).

INCORRECTO: "Vale, os he dejado el fichero en el ordenador; eventualmente
            se revisara"
CORRECTO:   "Listo, les dejé el archivo en el computador. El equipo lo
            revisa el viernes."
```

Las piezas que se deciden con ella:

1. **Se apoya en `ID8` con `extiende`** (`M7`). Usa el mismo mecanismo de `ID8`, releer contra una lista cerrada, y le agrega una segunda lista.
2. **«Si el proyecto declara» es lo que la deja entrar en `base/`** (`M3`). Un proyecto en otro idioma o en otra variedad no queda obligado a nada.
3. **El contenido va en un anexo nuevo**, `base/00-identidad-y-rol/espanol-de-colombia.md`, porque el cuerpo de `M5` no pasa de cuatro líneas. El anexo tiene cuatro secciones:

   | Sección | Qué lleva |
   |---|---|
   | Ortografía | Tildes en palabras como *qué*, *cómo* y *dónde* cuando preguntan, signos de apertura (¿, ¡), mayúsculas (meses y días en minúscula), puntuación |
   | Léxico | La tabla de la sección 5 de `marcadores-de-ia.md`, que se mueve aquí, más los calcos del inglés |
   | Gramática | *Ustedes* y no *vosotros*, pretérito simple, concordancia, régimen de las preposiciones |
   | Redacción | Oraciones con sujeto y verbo, un solo trato (*usted* o *tú*) de principio a fin, sin *se* impersonal para las acciones |

4. **La sección 5 de `marcadores-de-ia.md`** queda en una línea que remite al anexo nuevo, y la línea 135 cita `ID10` e `ID12`.
5. **Validable en parte** (`M9`): las tildes de pregunta, los signos de apertura, *vosotros* y *os*, y el léxico de España se cuentan en `validadores/marcas.py`. La concordancia y el tono se leen. Se registra en `validadores/reglas-validables.md`.
6. **Versión:** MENOR, porque la regla se activa con una declaración que el proyecto ya hace.

## El límite

- No cambia `ID10`: la persona y la forma verbal siguen allá.
- No cubre otras variedades del español ni otros idiomas. Si un proyecto declara otra, necesita su propio anexo.
- No cubre el texto que ve el usuario final de un producto, que gobierna `17·I4`.

## Cómo se sabrá que cerró

- `base/00-identidad-y-rol/reglas/ID12-*.md` existe con su checklist en **CUMPLE**.
- El anexo `espanol-de-colombia.md` existe con sus cuatro secciones, y la sección 5 de `marcadores-de-ia.md` remite a él.
- `python validadores/validar.py metareglas` sigue en verde con `ID12` clasificada en `validadores/reglas-validables.md`.
- `CHANGELOG.md` y `VERSION` tienen la entrada MENOR.
