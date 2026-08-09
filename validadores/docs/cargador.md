# `cargador.py`

Arma el texto con las reglas de `base/` que se le entrega al agente al abrir la sesión.

## Qué hace

Cada conversación con el agente empieza en blanco: lo que no se le entrega al arrancar, para él no existe. Este archivo prepara ese texto.

Las reglas viven en la carpeta `base/`, repartidas por tema en **capítulos numerados**: `00 · Identidad y rol`, `01 · Conducta`, `04 · Seguridad`, `13 · Documentación`, y así hasta el `20`. El número va adelante del nombre, y por eso los capítulos siempre se leen en el mismo orden.

No se le entregan todos enteros. Juntos pesan alrededor de 162 KB, y el agente puede tener a la vista solo una cantidad limitada de texto a la vez. Así que se reparten en dos:

- Los capítulos `00` y `01` van **enteros**, porque mandan siempre, sin importar de qué se esté hablando: quién es el agente y cómo se porta.
- De los demás va solo la **lista**: dónde está cada archivo, cuánto pesa y cómo se titula, con la orden de abrirlo y leerlo entero antes de tocar ese tema. Las reglas de seguridad no hacen falta hasta que se toca la seguridad.

Hay un caso aparte: si al proyecto le falta la carpeta `proyectos/` —la que guarda el código— quiere decir que el estándar nunca se instaló ahí. Entonces no se cargan las reglas de trabajo: se carga solo la regla que manda detenerse, y la orden de hacerlo.

## De qué depende y quién lo usa

```
cargador.py
   └── comun.py ··· EXCLUIDAS, leer y lineas_utiles
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
| `NUCLEO` | Qué capítulos se le entregan enteros al agente: los que empiezan por `00-` y los que empiezan por `01-`. De los demás solo se le manda la lista. |
| `GATE` | Dónde está la regla que manda detenerse cuando al proyecto le falta la carpeta `proyectos/`. |

**Sobre `NUCLEO`: se mira la dirección entera, no el nombre del archivo.** Un capítulo puede estar guardado de dos maneras: como un archivo suelto, o como una carpeta con un archivo por regla. Si se mirara solo el nombre del archivo, el segundo caso se escaparía.

| Dirección del archivo | Cómo está guardado | ¿Empieza por `00-` o `01-`? | Resultado |
|---|---|---|---|
| `01-conducta.md` | archivo suelto | Sí | va completo |
| `00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md` | carpeta | Sí, la dirección empieza por `00-` | va completo |
| `13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md` | carpeta | No | va solo su línea de la lista |

En la segunda fila está el motivo: el **archivo** se llama `ID7-…`, que no empieza por `00-`. Lo que empieza por `00-` es la **carpeta** que lo contiene. Mirando solo el nombre del archivo, esa regla del núcleo se quedaría fuera.

### Funciones

**`reglas(base)`**

- **Recibe:** la carpeta `base/`.
- **Hace:** la recorre entera buscando archivos `.md`, sin entrar a las carpetas excluidas, y los ordena por su ruta.
- **Retorna:** una lista de pares «ruta relativa, ruta completa».

El orden alfabético de la ruta ya es el orden de importancia: `00` antes que `01`, y el índice de un capítulo antes que sus reglas.

**`_titulo(texto)`**

- **Recibe:** el contenido de un archivo de regla.
- **Hace:** busca el título principal. Si el archivo contiene una sola regla no tiene título principal, así que usa el primer subtítulo.
- **Retorna:** el título, o «(sin título)» si no encuentra ninguno.

Se saca del archivo y no de una tabla escrita a mano para que el índice no envejezca.

**`_kb(texto)`**

- **Recibe:** un texto.
- **Retorna:** su tamaño en kilobytes, redondeado, con mínimo 1.

**`_solo_gate(base, reglas_encontradas)`**

- **Recibe:** la carpeta `base/` y la lista de reglas encontradas.
- **Hace:** busca el archivo de la regla que manda detenerse y lo retorna completo, con la orden de no seguir con nada antes.
- **Retorna:** ese texto, o texto vacío si no encontró el archivo.

**`contexto(estandar, gate_ok=True)`**

- **Recibe:** la carpeta del estándar y si el proyecto ya tiene su carpeta `proyectos/`.
- **Hace:**
  1. Si no existe la carpeta `base/` o está vacía, retorna texto vacío.
  2. Si al proyecto le falta `proyectos/`, retorna solo la regla que manda detenerse.
  3. Si la tiene, reparte los archivos en dos grupos: los de `00-` y `01-` van completos; del resto va una línea con dónde está, cuánto pesa y cómo se titula.
  4. Arma el texto final con sus títulos y advertencias.
- **Retorna:** el texto completo que se le entrega al agente al arrancar.

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
        sí → retorna solo esa regla y la orden de detenerse
        no ↓
   recorre base/
        ↓
   ¿el nombre empieza por 00- o 01-?
        sí → el archivo completo
        no → una línea: dónde está, cuánto pesa y cómo se titula
        ↓
texto final → se le entrega al agente al arrancar
```

## Ejemplos de lo que retorna

```python
reglas('c:/…/agente/base')
[('00-nucleo-blindado.md',                        'c:\…\base\00-nucleo-blindado.md'),
 ('01-identidad-y-rol/base.md',                   'c:\…\base\01-identidad-y-rol\base.md'),
 ('02-flujo-de-trabajo/base.md',                  'c:\…\base\02-flujo-de-trabajo\base.md'),
 ('02-flujo-de-trabajo/reglas/F13-deja-la-…md',   'c:\…\F13-deja-la-…md'),
 ('09-git.md',                                    'c:\…\base\09-git.md')]
#  └─ ruta corta, ya ordenada          └─ ruta completa para abrirlo

_titulo('# 09 · Git\n\n## G2 · Mensaje de commit\n')
'09 · Git'

_titulo('## M4 · El ID no lleva el prefijo del capítulo\n\nTexto.\n')
'M4 · El ID no lleva el prefijo del capítulo'      # no tenía título principal

_titulo('Solo texto suelto.\n')
'(sin título)'

_kb('a' * 3000)
3

contexto('c:/…/agente')
'''[REGLAS BASE DEL ESTÁNDAR — CARGADAS, OBLIGATORIAS]
Rigen esta sesión completa. Ante cualquier choque gana el núcleo.

<<< base/00-nucleo-blindado.md >>>
# 00 · Núcleo blindado
… el archivo entero …

<<< base/01-identidad-y-rol/base.md >>>
… el archivo entero …

[EL RESTO DE LAS REGLAS — NO ESTÁN CARGADAS, SOLO EL ÍNDICE]
Antes de tocar cualquiera de estos temas, leer el archivo completo con Read. …

  base/02-flujo-de-trabajo/base.md  (14 KB) — 02 · Flujo de trabajo
  base/09-git.md                    (6 KB)  — 09 · Git
  base/13-documentacion/base.md     (22 KB) — 13 · Documentación'''

contexto('c:/…/agente', gate_ok=False)
'''[ARRANQUE DETENIDO — EL GATE 02·F13 NO PASA]
No continuar con nada: ni crear el espacio, ni adecuar el proyecto por
iniciativa propia. Mostrar la orientación de F13 que sigue y detenerse.

<<< base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-…md >>>
… solo ese archivo …'''

contexto('C:/carpeta-sin-base')
''               # no hay carpeta base/: no hay nada que entregar
```
