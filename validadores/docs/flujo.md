# `flujo.py`

Revisa que cada fase de trabajo tenga arriba los documentos de los que depende, y que su plan esté completo y sin dudas sin resolver.

## Qué hace

Recorre las mismas carpetas que `fases.py` —`documentacion/epicas/`— y comprueba tres cosas:

1. **Existe lo de arriba.** Una fase va adentro de una historia de usuario, y esa historia adentro de una épica. Si la historia tiene fases, tiene que tener su documento; si la épica tiene fases colgando, también. No alcanza con que exista la carpeta vacía.
2. **El plan responde las trece preguntas.** El molde del plan las numera de la 0 a la 13. Acá se mira cuáles no están.
3. **El plan no deja dudas.** Frases como `TBD`, `por definir`, `(o similar)`, `(o donde esté)`, `(o parecido)` o `(o equivalente)` quieren decir que algo se dio por supuesto sin ir a comprobarlo.
4. **No hay una regla jubilada sin adoptar.** Si el estándar jubiló una regla después de la versión que el proyecto declara, el proyecto no puede abrir ni cerrar fases hasta ponerse al día (`02·F22`). Esto se pregunta acá, y no en cualquier momento, porque acá es donde están las fases. Lo responde `version.py`.

Lo del plan no lo juzga: mira si está y si hay dudas sueltas, y todo eso lo reporta como **aviso**, porque un plan que todavía se está escribiendo puede estar incompleto a propósito. Lo único que **falla** es el punto 4.

## De qué depende y quién lo usa

```
flujo.py
   ├── fases.py ····· le pide _subcarpetas para recorrer las carpetas
   ├── version.py ··· le pregunta si hay reglas jubiladas sin adoptar
   └── comun.py ····· AVISO, FALLA, Hallazgo y leer
```

De Python usa `os` y `re`.

Lo usan:

```
flujo.py
   ▲
   ├── validar.py ··· cuando alguien pide revisar "flujo"
   └── pruebas.py
```

## Qué tiene adentro

### Valores fijos

| Nombre | Qué guarda |
|---|---|
| `CARPETA` | `documentacion/epicas`. |
| `_SECCIONES` | Los números de las partes que tiene que traer el plan: del 0 al 13. |
| `_ENCABEZADO` | Reconoce un título numerado adentro del plan, del estilo `## 5.`. |
| `_INCERTIDUMBRE` | Reconoce las frases que delatan una duda: `TBD`, `por definir`, `(o similar)`, `(o donde esté)`, `(o parecido)` y `(o equivalente)`. |

### Funciones

**`_texto(ruta)`**

- **Recibe:** la ruta de un archivo.
- **Retorna:** su contenido, o texto vacío si no se puede leer.

**`revisar_plan(texto)`**

- **Recibe:** el contenido de un `plan_trabajo.md`.
- **Hace:** busca los títulos numerados y los compara con la lista de partes que debería traer. Después recorre el texto línea por línea buscando frases de duda.
- **Retorna:** dos cosas: los números de las partes que faltan, y una lista de «en qué línea está y qué dice» por cada duda encontrada.

Está separada del resto para poder probarla sin archivos en disco.

**`validar(proyecto)`**

- **Recibe:** la carpeta del proyecto.
- **Hace:**
  1. Si no existe `documentacion/epicas/`, retorna una sola falla.
  2. Por cada épica anota si tiene documento, y empieza sin saber todavía si tiene fases abajo.
  3. Por cada historia mira si tiene fases. Si las tiene y le falta su documento → **aviso**.
  4. Por cada fase, si hay plan de trabajo, lo revisa con `revisar_plan`: un aviso con las partes que faltan, y un aviso por cada duda con la línea donde está.
  5. Al terminar la épica, si tenía fases abajo y le falta su documento → **aviso**.
- **Retorna:** la lista de hallazgos.

## Cómo se ejecuta

```
python validadores/validar.py flujo --raiz "C:/ruta/proyecto"
```

Por dentro:

```
documentacion/epicas/
   │
   ├── EP-001-facturacion/
   │      ├── epica.md   ← si hay fases abajo y esto falta → AVISO
   │      │
   │      └── HU-003-registrar/
   │             ├── HU-003-registrar.md  ← si hay fases y falta → AVISO
   │             │
   │             └── A-EP-001-HU-003-configuracion/
   │                    └── plan_trabajo.md
   │                            ↓
   │                       revisar_plan(texto)
   │                            ↓
   │              ¿están las partes 0 a 13?      → las que faltan, un AVISO
   │              ¿hay TBD, "(o similar)", ...?  → un AVISO por cada una
```

## Ejemplos de lo que retorna

```python
revisar_plan(texto_de_un_plan_completo)
([], [])
#  └─ nada falta   └─ ninguna duda suelta

revisar_plan('## 0. Contexto\n## 1. Objetivo\n## 2. Alcance\n')
([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [])
#  └─ los números de las partes que faltan

revisar_plan('## 0. Contexto\nSe guarda en `app/Pagos.php` (o donde esté).\n'
             'La fecha queda TBD.\n')
([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
 [(2, '(o donde esté)'), (3, 'TBD')])
#                         └─ línea  └─ la marca de duda encontrada

validar('C:/proyectos/pos')          # todo bien
[]

validar('C:/proyectos/sin-documentacion')
[Hallazgo(FALLA, 'C:/proyectos/sin-documentacion', 0,
          'no existe `documentacion/epicas` (F12.13)')]

validar('C:/proyectos/pos')          # con problemas
[Hallazgo(AVISO, 'documentacion/epicas/EP-001-facturacion/HU-003-registrar', 0,
          'hay fases pero la HU no tiene su documento (F0: falta el padre)'),

 Hallazgo(AVISO, 'documentacion/epicas/EP-001-facturacion', 0,
          'hay fases pero la épica no tiene su documento (F0: falta el padre)'),

 Hallazgo(AVISO, '…/A-EP-001-HU-003-configuracion/plan_trabajo.md', 0,
          'al plan le faltan secciones de las 13 preguntas (F14): 7, 9, 11'),

 Hallazgo(AVISO, '…/A-EP-001-HU-003-configuracion/plan_trabajo.md', 24,
          'marca de incertidumbre `(o similar)` en el plan — F17 pide la
           línea base verificada')]
```
