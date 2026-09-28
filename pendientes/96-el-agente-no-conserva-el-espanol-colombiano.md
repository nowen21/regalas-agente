# Pendiente · El agente no conserva el español colombiano

**Estado:** **hecho** el 2026-09-27, en la misma sesión que lo anotó. Lo construyó la fase `A` de HU-039: la regla [`00·ID12`](../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) y su anexo, versión 38.2.0.

| | |
|---|---|
| **Historia de usuario** | [EP-001 · HU-039 · El agente no conserva el español colombiano](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-039-el-agente-no-conserva-el-espanol-colombiano/HU-039-el-agente-no-conserva-el-espanol-colombiano.md) |
| **De dónde sale** | La sesión del 2026-09-27: el usuario preguntó cuál era la regla del español colombiano y ninguna lo decía |
| **Proyecto de origen** | El estándar mismo |

## El problema

Ninguna regla le exige al agente seguir las normas ortográficas, léxicas, gramaticales y de redacción del español de Colombia. Por eso sus textos pueden traer palabras, expresiones o formas de redacción que no son las de aquí, y eso afecta la claridad y la naturalidad de lo que entrega.

Lo que el estándar tiene hoy no alcanza: [`00·ID10`](../base/00-identidad-y-rol/reglas/ID10-escribe-en-el-idioma-del-proyecto-en-tercera-persona-y-en-infinitivo.md) pide escribir en la variedad del idioma del proyecto, pero no dice qué es escribirla bien; y la sección 5 de [`marcadores-de-ia.md`](../base/00-identidad-y-rol/marcadores-de-ia.md#L73) trae palabras de España con su equivalente colombiano, pero como marca de texto generado por máquina, no como norma.

## Por qué importa

El usuario pidió «español colombiano» tres veces antes de que quedara escrito ([pendiente 85](85-las-conversaciones-completas-no-se-pueden-analizar.md#L27)). Hoy un texto sin tildes de pregunta, con *vosotros* o con *eventualmente* por *finalmente* no incumple ninguna regla que se pueda citar: `ID8` solo lo atrapa si coincide con una marca de su lista.

## Qué falta

Una regla del capítulo 00, por el procedimiento del [capítulo 20](../base/20-meta-reglas/base.md). Borrador acordado con el usuario el 2026-09-27:

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

Lo que se decide con ella:

1. Extiende `ID8` (`M7`): usa su mecanismo, releer contra una lista cerrada, y le suma una segunda lista.
2. La condición «si el proyecto declara» la deja entrar en `base/` (`M3`): un proyecto en otro idioma o en otra variedad no queda obligado.
3. El contenido va en un anexo nuevo, `base/00-identidad-y-rol/espanol-de-colombia.md`, porque el cuerpo de `M5` no pasa de cuatro líneas:

   | Sección | Qué lleva |
   |---|---|
   | Ortografía | Tildes de pregunta en *qué*, *cómo*, *dónde*; signos de apertura (¿, ¡); meses y días en minúscula; puntuación |
   | Léxico | La tabla de la sección 5 de `marcadores-de-ia.md`, que se mueve aquí, y los calcos del inglés |
   | Gramática | *Ustedes* y no *vosotros*, pretérito simple, concordancia, régimen de las preposiciones |
   | Redacción | Oraciones completas, con sujeto y verbo |

4. La sección 5 de `marcadores-de-ia.md` queda en una línea que remite al anexo, y la línea 135 cita `ID10` e `ID12`.
5. Validable en parte (`M9`): `validadores/marcas.py` cuenta las tildes de pregunta, los signos de apertura, *vosotros*, *os* y el léxico de España; la concordancia y el régimen de las preposiciones se leen.
6. Versión MENOR: la regla se activa con una declaración que el proyecto ya hace.

## El límite

- No cambia `ID10`: la persona y la forma verbal siguen allá.
- No cubre otras variedades ni otros idiomas; cada una necesita su anexo.
- No cubre el texto que ve el usuario final de un producto, que gobierna `17·I4`.

## Cómo se sabrá que cerró

- `base/00-identidad-y-rol/reglas/ID12-*.md` existe con su checklist en CUMPLE.
- El anexo `espanol-de-colombia.md` existe con sus cuatro secciones, y la sección 5 de `marcadores-de-ia.md` remite a él.
- `python validadores/validar.py metareglas` sigue sin fallas, con `ID12` en `validadores/reglas-validables.md`.
- `CHANGELOG.md` y `VERSION` tienen la entrada MENOR.
