# Revisar si una regla todavía sirve

**Una regla equivocada se comporta exactamente igual que una correcta.** No se rompe nada: sigue ahí, sigue pasando su checklist, y el agente la sigue obedeciendo. Mientras tanto cambia la herramienta que nombraba, cambia la práctica que daba por buena, o el problema que venía a evitar deja de ocurrir.

**El sello no cubre esto.** Dice *«vale mientras el texto de arriba no cambie»*: protege contra que cambie **la regla**, no contra que cambie **el mundo**.

## Las tres preguntas

Son tres y son cortas a propósito: **revisar no puede costar más que escribir**, o no se revisa.

1. **¿Sigue existiendo el problema que esta regla evita?**
2. **¿Lo que manda hacer sigue siendo la mejor forma de evitarlo?**
3. **¿Alguien la incumplió en este período, y por qué?**

La tercera es la que más enseña. Un incumplimiento repetido casi nunca es descuido: es la regla pidiendo otra redacción, o pidiendo partirse.

## Qué se hace con cada respuesta

| Si la revisión dice esto | Entonces |
|---|---|
| Sigue sirviendo tal cual | Se le pone la fecha y ya |
| Sirve, pero está mal dicha | Se reescribe, y eso **anula su sello**: se le vuelve a aplicar el checklist |
| Manda dos cosas | Se parte, con un identificador nuevo al final del capítulo ([`M4`](reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md)) |
| El problema ya no existe | Se deroga ([`M11`](reglas/M11-las-reglas-no-se-borran-se-derogan.md)); **no se borra** |

## Dónde queda la fecha

Una línea al final del bloque de checklist de la regla:

```
> Revisada contra la realidad el 2026-08-19.
```

**Arranca ausente en todas las reglas, a propósito.** Ponérsela de una vez a las doscientas habría sido escribir doscientas fechas que no responden por ninguna revisión: el sello vacío que este documento viene a evitar. La fecha aparece cuando la revisión ocurre.

## Qué lista pedir

```
python validadores/vigencia.py
```

Las ordena de la que lleva más tiempo sin mirarse a la que menos, y al lado dice **cuántos incumplimientos produce hoy cada una**.

**Ese segundo número se lee en las dos direcciones.** Una regla vieja que falla todo el tiempo se revisa primero. Una regla vieja que **no ha fallado nunca** hay que mirarla por el motivo contrario: puede que ya nadie la esté aplicando.

## No hay umbral, y es una decisión

**Un umbral inventado produce una alarma que se aprende a ignorar**, que es el defecto más caro de este repositorio. Cada cuánto conviene revisar se decide **después** de mirar la lista unas cuantas veces, no antes de tenerla.
