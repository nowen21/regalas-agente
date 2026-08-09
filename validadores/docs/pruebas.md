# `pruebas.py`

Las pruebas de todos los validadores. Se corren a mano.

## Qué hace

Comprueba que los validadores hagan lo que dicen. Prueba dos cosas distintas:

- Que cuando algo está mal, lo detecten.
- Que cuando todo está bien, **no digan nada**. Esto último ocupa la mitad del archivo. Un validador que se queja de cosas que están bien termina ignorado, y muchas de estas pruebas nacieron justamente de una queja injusta encontrada revisando este repositorio.

Usa `unittest`, que ya viene con Python. No hace falta instalar nada.

Es el archivo más grande de la carpeta: unas 1.800 líneas, repartidas en 30 grupos de pruebas.

## De qué depende y quién lo usa

Trae 27 archivos de la carpeta: todos los validadores, `instalar.py`, `historico.py`, `recuerdos.py`, `checklist.py`, `versiones.py` y `comun.py`. Quedan fuera los cinco `hook_*.py` y `cargador.py`.

```
pruebas.py
   └── los 27 archivos que prueba
```

De Python usa `json`, `os`, `sys`, `tempfile` y `unittest`.

No lo usa ningún archivo.

## Qué tiene adentro

### Funciones de apoyo

**`_claude_md_completo(proyecto="demo")`**

- **Recibe:** un nombre de proyecto.
- **Hace:** lee el molde central del `CLAUDE.md` y lo llena con los datos que pondría el instalador.
- **Retorna:** el texto que queda.

**`severidades(hallazgos)`**

- **Recibe:** una lista de hallazgos.
- **Retorna:** solo sus etiquetas: si cada uno fue falla o aviso. Sirve para escribir pruebas cortas del estilo «esto tiene que dar una sola falla».

**`mensajes(hallazgos)`**

- **Recibe:** una lista de hallazgos.
- **Retorna:** sus textos unidos por barras. Sirve para que, cuando una prueba falle, se vea en pantalla qué fue lo que se encontró.

### Los grupos de pruebas

Cada grupo junta las pruebas de un tema. Estos son, en el orden en que aparecen:

| Grupo | Qué prueba |
|---|---|
| `Comun` | Que no se mire adentro de los bloques de ejemplo, y que los huecos sin llenar no se confundan con enlaces ni con casillas para marcar. |
| `Commits` | Los mensajes con que se guardan los cambios: el ejemplo bueno, los vacíos, la línea en blanco que falta, la firma de herramienta. |
| `Enlaces` | Qué enlaces se comprueban y cuáles no; y que este repositorio no tenga enlaces rotos ni índices viejos. |
| `Plantillas` | Huecos sin llenar, etiquetas que sí se conservan, partes que faltan, y averiguar de qué molde salió un documento. |
| `Fases` | Las carpetas de épica, historia y fase: los nombres, los números, las letras repetidas y las letras que faltan. |
| `Trazabilidad` | Que la épica y la historia se nombren entre sí, que el plan diga de dónde salió, y que al cerrar quede su tabla. |
| `Versionado` | Cómo se clasifica cada archivo: contraseñas, moldes vacíos, código copiado a propósito, archivos de base de datos. |
| `Secretos` | Las formas que ya son una clave, los valores de mentira, y las líneas que van a buscar el dato afuera. |
| `Dependencias` | Proyectos con y sin la lista de qué versión exacta se instaló. |
| `Errores` | Errores atrapados y tirados a la basura, en sus varias formas, y contraseñas escritas en el diario del programa. |
| `Rendimiento` | Consultas que traen de más y consultas metidas adentro de algo que se repite. |
| `Esquema` | Columnas que apuntan a otra tabla, columnas nuevas obligatorias y nombres demasiado largos. |
| `Migraciones` | El camino de vuelta, en las seis formas de escribir una migración. |
| `Rama` | Trabajar en una rama aparte, en la principal, con la rama atrasada, y sin estar en ninguna. |
| `Version` | Leer qué versión dice seguir el proyecto y compararla con la del estándar. |
| `CI` | Encontrar el archivo de lo que corre solo, y que ahí se nombren las pruebas y el revisor de estilo. |
| `Seguridad` y `Seguridad_S5` | Texto pegado a una consulta, datos que entran sin control y la sesión desprotegida. |
| `Flujo` y `FlujoF0` | El plan completo, las partes que faltan, las dudas sueltas y los documentos de los que depende una fase. |
| `Plantillas_docs` | Averiguar el molde de los documentos de un proyecto. |
| `Calidad` | Funciones largas y cortas, en las dos formas de escribirlas. |
| `Aislamiento` | La base de datos de mentira, el orden al azar y lo que hace que una prueba cambie de resultado. |
| `Herramientas` | Averiguar con qué lenguaje está hecho el proyecto. |
| `Instalador` | La lista de proyectos, encontrar los repositorios, reemplazar un enganche viejo, y que lo que el proyecto llenó a mano no se pise. |
| `Historico` | Crear el archivo, numerar los mensajes, mantener el índice, y que una respuesta no quede escrita dos veces. |
| `Recuerdos` | Mover los recuerdos, los nombres ya ocupados, la carpeta que es la misma, y las mayúsculas. |
| `Checklist` | Que la lista y las comprobaciones no se separen, y que el aviso se escriba y se borre solo. |
| `Citas` | Los enlaces a un título exacto, las tres formas de nombrar una regla, lo que no se toca, y que no quede ningún código suelto. |
| `Versiones` | Las huellas, el registro de cada actualización y su índice. |
| `EnlacesDelHistorico` | Que los enlaces de una conversación guardada no se comprueben, pero sí los de su índice. |

Varios grupos crean carpetas de mentira antes de empezar y arman ahí lo que necesitan, para no depender de ningún proyecto de verdad.

### Pruebas que revisan este mismo repositorio

Cuatro pruebas no usan datos inventados, sino el repositorio del estándar:

- Que no haya enlaces rotos.
- Que los índices estén al día.
- Que no quede ninguna regla nombrada sin su enlace.
- Que la lista de piezas de `checklist.py` sea la misma de `plantillas/stack-instalacion.md`. Si se separaran, el checklist diría que todo está bien callándose lo que no revisó.

## Cómo se ejecuta

```
python validadores/pruebas.py
```

Muestra el nombre de cada prueba y si pasó o no.

## Ejemplos de lo que retorna

```python
_claude_md_completo('demo')
'# demo — Instrucciones del agente\n\nVersión del estándar adoptada: 5.0.0\n
 Ruta del estándar: `c:/Ing. Jose/ia/agente`\n…'
# el molde ya lleno, sin ningún hueco sin reemplazar

severidades([Hallazgo(FALLA, 'a.md', 1, '…'), Hallazgo(AVISO, 'a.md', 2, '…')])
['FALLA', 'AVISO']

severidades([])
[]

mensajes([Hallazgo(FALLA, 'a.md', 1, 'enlace roto: x.md'),
          Hallazgo(AVISO, 'b.md', 2, 'sección ausente')])
'enlace roto: x.md | sección ausente'
```

Y esto es lo que sale al correrlo:

```
test_no_mira_dentro_de_bloques_de_codigo (__main__.Comun) ... ok
test_marcador_ignora_enlaces_y_casillas (__main__.Comun) ... ok
test_ejemplo_correcto_de_g2_pasa (__main__.Commits) ... ok
test_asunto_sin_contenido (__main__.Commits) ... ok
…
----------------------------------------------------------------------
Ran 214 tests in 8.431s

OK
```

Cuando una prueba falla, muestra qué esperaba y qué encontró:

```
======================================================================
FAIL: test_el_estandar_no_tiene_enlaces_rotos (__main__.Enlaces)
----------------------------------------------------------------------
AssertionError: Lists differ: [Hallazgo(...)] != []
: enlace roto: ../base/09-git-viejo.md
----------------------------------------------------------------------
Ran 214 tests in 8.502s

FAILED (failures=1)
```

El programa termina bien si pasaron todas, y mal si falló alguna. Eso es lo que permite que las pruebas se corran solas en un servidor y avisen sin que nadie las mire.
