# `mapa_tareas.py`

Escribe, a partir de las reglas de `base/`, el mapa de qué reglas aplican a cada tarea y un archivo por tarea con esas reglas completas.

## Qué hace

Cada regla dice a qué tareas aplica con su línea `**Aplica a:**`. Este programa las lee y escribe dos cosas:

| Qué escribe | Dónde | Para qué |
|---|---|---|
| El mapa | `base/mapa-de-tareas.md` | Ver de un vistazo qué reglas tiene cada tarea, con el enlace a cada una |
| Las reglas completas de cada tarea | `base/reglas-por-tarea/` | Que el agente las lea enteras antes de hacer la tarea |

Los archivos por tarea son copias de las reglas: por eso `comun.EXCLUIDAS` saca esa carpeta de los recorridos de `base/`, y así los validadores no las cuentan como reglas repetidas. Si una tarea pasa de 25.000 caracteres se parte en varios archivos, para que cada uno llegue entero en la salida de un comando, que se corta pasados 30.000. Los enlaces de cada regla se reescriben para que sigan funcionando desde la carpeta nueva.

También lee la lista cerrada de tareas, `base/tareas.md`: las palabras clave que piden cada tarea y las acciones que la señalan.

## Cómo se ejecuta

```
python validadores/mapa_tareas.py
```

`python validadores/validar.py tareas` falla si el mapa o algún archivo por tarea no coincide con lo que dicen las reglas, si sobra un archivo, si una regla no dice sus tareas o si nombra una que no está en la lista. Corre solo antes de cada publicación.

## Qué tiene adentro

| Función | Qué retorna |
|---|---|
| `tareas()` | Los nombres de la lista cerrada |
| `palabras_clave()` | `{tarea: palabras clave}` de la tercera columna |
| `siempre()` | Las tareas que van en todo mensaje |
| `acciones()` | `{tarea: [(clase, valores)]}` de la cuarta columna |
| `reglas_por_tarea()` | `{tarea: [regla]}` |
| `cuerpo(regla)` | El texto de la regla sin su sello |
| `armar()` y `armar_por_tarea()` | El texto del mapa y el de cada archivo por tarea |
| `archivos_de(tarea)` | Las rutas de los archivos de esa tarea |
| `validar()` | Lo que no coincide |
| `escribir()` | Escribe todo y borra lo que sobra |
