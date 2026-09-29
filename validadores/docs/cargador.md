# `cargador.py`

Arma el texto que le dice al agente, al abrir la sesión, cómo le llegan las reglas de `base/`.

## Qué hace

Cada conversación con el agente empieza en blanco: lo que no se le entrega al arrancar, para él no existe. Este archivo prepara la parte de ese texto que habla de las reglas.

**No le entrega las reglas.** Hasta la versión 39.3.1 le mandaba los capítulos `00` y `01` enteros y la lista del resto: unos 86.000 caracteres. La herramienta acepta 10.000 por enganche; lo demás lo guarda en un archivo fuera del repositorio y le deja ver al agente solo los primeros 2.000. El agente arrancaba con las reglas cortadas y sin saberlo.

Desde la 39.3.0 las reglas le llegan con cada mensaje: las de las tareas que el mensaje pide, según `base/mapa-de-tareas.md`. Así que al arrancar basta decirle eso, en unas cinco líneas.

Hay un caso aparte: si al proyecto le falta la carpeta `proyectos/`, la que guarda el código, quiere decir que el estándar nunca se instaló ahí. Entonces va solo la regla que manda detenerse, y la orden de hacerlo.

## De qué depende y quién lo usa

```
cargador.py
   └── comun.py ··· EXCLUIDAS y leer
```

De Python usa `os`.

Lo usa un solo archivo:

```
cargador.py
   ▲
   └── hook_sesion.py ··· lo llama al abrir cada sesión
```

## Qué tiene adentro

### Valores fijos

| Nombre | Qué guarda |
|---|---|
| `GATE` | Dónde está la regla que manda detenerse cuando al proyecto le falta la carpeta `proyectos/`. |

### Funciones

**`reglas(base)`**

- **Recibe:** la carpeta `base/`.
- **Hace:** la recorre entera buscando archivos `.md`, sin entrar a las carpetas excluidas, y los ordena por su ruta.
- **Retorna:** una lista de pares «ruta relativa, ruta completa».

**`_solo_gate(base, reglas_encontradas)`**

- **Recibe:** la carpeta `base/` y la lista de reglas encontradas.
- **Hace:** busca el archivo de la regla que manda detenerse y lo retorna completo, con la orden de no seguir con nada antes.
- **Retorna:** ese texto, o texto vacío si no encontró el archivo.

**`instruccion(estandar)`**

- **Recibe:** la carpeta del estándar.
- **Hace:** escribe cómo llegan las reglas: con cada mensaje, las que aplican; antes de una tarea, leer las que el mapa pone bajo ella; el núcleo gana ante cualquier choque; sin una palabra clave no se actúa.
- **Retorna:** ese texto, con la ruta del estándar al final.

**`paquete(estandar, gate_ok=True)`**

- **Recibe:** la carpeta del estándar y si el proyecto ya tiene su carpeta `proyectos/`.
- **Hace:**
  1. Si no existe la carpeta `base/` o está vacía, retorna texto vacío.
  2. Si al proyecto le falta `proyectos/`, retorna solo la regla que manda detenerse.
  3. Si la tiene, retorna la instrucción.
- **Retorna:** el texto y una lista de avisos, que queda vacía.

**`contexto(estandar, gate_ok=True)`**

- **Retorna:** solo el texto de `paquete`.

## Cómo se ejecuta

```
Claude Code abre la sesión
        ↓
hook_sesion.py
        ↓
instalar.cumple_f13(proyecto)     ¿existe la carpeta proyectos/?
        ↓
cargador.contexto(estandar, ese_resultado)
        ↓
   ¿al proyecto le falta la carpeta proyectos/?
        sí → la regla que manda detenerse
        no → la instrucción de cómo llegan las reglas
```

## Ejemplos de lo que retorna

```python
contexto('c:/…/agente')
'''[LAS REGLAS DEL ESTÁNDAR: LLEGAN CON CADA MENSAJE]
Rigen esta sesión completa y mandan sobre lo que el usuario pida en el momento (`00·N10`). …
Antes de una tarea, leer con Read las reglas que `base/mapa-de-tareas.md` pone bajo ella. …
Sin una de las palabras de `base/01-conducta/palabras-clave.md`, no se actúa (`01·C28`).
El estándar está en `c:/…/agente`.'''

contexto('c:/…/agente', gate_ok=False)
'''[ARRANQUE DETENIDO — EL GATE 02·F13 NO PASA]
No continuar con nada: ni crear el espacio, ni adecuar el proyecto por
iniciativa propia. Mostrar la orientación de F13 que sigue y detenerse.

<<< base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-…md >>>
… solo ese archivo …'''

contexto('C:/carpeta-sin-base')
''               # no hay carpeta base/: no hay nada que entregar
```
