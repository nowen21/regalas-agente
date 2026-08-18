# `pendientes.py`

Comprueba la numeración de la carpeta `pendientes/` y que cuadre con su índice.

## Qué hace

Un pendiente se numera por el orden en que conviene ejecutarlo. Ese número **no se reutiliza nunca**: los pendientes se citan entre sí por número —«hermano del 33», «el punto 2 del 53»—, así que abrir uno con un número ya tomado rompe esas citas **sin que nadie se entere**, porque los dos archivos existen y ninguno pisa al otro.

Este archivo responde tres preguntas:

1. **¿Cuál es el próximo número libre?**, para no tener que revisar la carpeta a ojo.
2. **¿Hay algún número repetido?**
3. **¿La carpeta y el índice dicen lo mismo?**

## El detalle que hace falta saber: al cerrarse, un pendiente pierde su número

Cuando un pendiente se cierra, su archivo se mueve a `hecho/` **y se renombra**: `02-vigencia-y-poda.md` pasa a ser `vigencia-y-poda-de-memoria.md`. Mirando solo los archivos, el número 02 **parece libre** — y no lo está.

Lo único que conserva la numeración completa es el **índice**, con sus filas tachadas: `| ~~02~~ | — | **hecho** → … |`. Por eso el próximo número libre se calcula leyendo **la carpeta y el índice juntos**, y no solo la carpeta.

Medido el 2026-08-17 en este repositorio: **39 pendientes con archivo, 54 números tomados**. Quince números existen solo en el índice.

## De qué depende y quién lo usa

Solo de `comun.py`, y ni siquiera de su función de lectura: usa una propia que devuelve texto vacío cuando el archivo no está, porque tiene que poder correr sobre una carpeta que todavía no tiene índice.

```
pendientes.py
   └── comun.py  (solo para Hallazgo y las severidades)
```

Lo usa `validar.py` en el subcomando `pendientes`.

## Qué tiene adentro

| Función | Qué retorna |
|---|---|
| `numerados(proyecto)` | `{numero: [nombres]}` de los archivos numerados, abiertos y cerrados |
| `numeros_del_indice(proyecto)` | Los números que el índice registra, **incluidos los ya cerrados** |
| `tomados(proyecto)` | La unión de los dos: todo número que no se puede reutilizar |
| `sin_numero(proyecto)` | Los `.md` de la carpeta que no empiezan por número |
| `proximo_libre(proyecto)` | El siguiente al mayor tomado |
| `validar(proyecto)` | La lista de hallazgos |
| `linea_proximo(proyecto)` | La línea que se imprime al final de la corrida |

**Por qué el siguiente al mayor y no el primer hueco.** El índice dice que «el número no se reutiliza ni se renumeran los demás: los huecos son historia». Entregar un hueco haría que «el 02» apuntara a dos cosas distintas según cuándo se leyera.

## Severidades

| Qué | Severidad | Por qué |
|---|---|---|
| Un número tomado por dos archivos | **Falla** | Rompe citas y no hay forma de resolverlo leyendo |
| Un archivo que no empieza por número | Aviso | Un archivo suelto no puede invalidar la comprobación de los otros cuarenta |
| Un pendiente sin línea en el índice, o al revés | Aviso | Se arregla editando un `.md`, y no rompe nada mientras tanto |
| No existe la carpeta `pendientes/` | **Falla** | No hay nada que comprobar |

## Cómo se ejecuta

```
python validadores/validar.py pendientes
```

```
== Numeración de pendientes · . ==
OK: sin incumplimientos.
Pendientes: 39 con archivo · 54 números tomados · el próximo libre es el 59 (HU-018)
```

La última línea sale **siempre**, haya hallazgos o no: es la pregunta que se hace quien va a abrir un pendiente, no un incumplimiento.
