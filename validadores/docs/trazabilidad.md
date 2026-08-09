# `trazabilidad.py`

Revisa que la épica y la historia de usuario se nombren entre sí, que el plan declare de dónde salió y que el documento de cierre traiga su tabla.

## Qué hace

Recorre las mismas carpetas que `fases.py` y comprueba que los documentos se nombren unos a otros, para poder ir de uno a otro sin perderse:

1. **Cada historia dice a qué épica pertenece**, nombrándola en su documento.
2. **Cada épica nombra sus historias** en el suyo.
3. **El plan de trabajo dice `ORIGEN`**, o sea de dónde salió esa fase.
4. **El documento de lo que quedó hecho trae su tabla.** Y si en esa tabla hay cosas marcadas con ❌, avisa para que una persona confirme que hay razón para dejarlas así.

No juzga qué dicen los documentos: solo mira si los nombres aparecen y si la tabla está. Casi todo es **aviso**, porque un documento recién abierto todavía no lo tiene todo.

## De qué depende y quién lo usa

```
trazabilidad.py
   ├── fases.py ····· le pide _EPICA, _HU, _FASE, _numero y _subcarpetas
   └── comun.py ····· AVISO, FALLA, Hallazgo, leer y lineas_utiles
```

De Python usa `os` y `re`.

Lo usan:

```
trazabilidad.py
   ▲
   ├── validar.py ··· cuando alguien pide revisar "trazabilidad"
   └── pruebas.py
```

Se apoya en `fases.py` a propósito: las carpetas con el nombre mal escrito ya las reporta aquel, así que acá se saltan y no se avisa dos veces de lo mismo.

## Qué tiene adentro

### Valores fijos

| Nombre | Qué guarda |
|---|---|
| `CARPETA` | `documentacion/epicas`. |

### Funciones

**`_texto(ruta)`**

- **Recibe:** la ruta de un archivo.
- **Retorna:** su contenido, o texto vacío si no se puede leer.

**`_sin_codigo(texto)`**

- **Recibe:** el contenido de un documento.
- **Hace:** le quita todo lo que está adentro de bloques de código, que son los pedazos de ejemplo.
- **Retorna:** el resto.

Así un ejemplo no cuenta como si el documento hubiera nombrado de verdad a la épica.

**`_menciona(texto, prefijo, numero)`**

- **Recibe:** el contenido, con qué empieza el nombre (`EP` o `HU`) y el número.
- **Hace:** lo busca sin exigir una forma exacta: `EP-2`, `EP-002` y `EP2` valen igual.
- **Retorna:** verdadero o falso.

**`validar(proyecto)`**

- **Recibe:** la carpeta del proyecto.
- **Hace:**
  1. Si no existe `documentacion/epicas/`, retorna una sola falla.
  2. Por cada épica bien nombrada, lee su documento sin los bloques de código.
  3. Por cada historia bien nombrada, lee el suyo igual.
  4. Si el documento de la historia existe y no nombra su épica → **aviso**.
  5. Si el documento de la épica existe y no nombra esa historia → **aviso**.
  6. Por cada fase bien nombrada:
     - si hay plan de trabajo y no dice `ORIGEN` en mayúsculas → **aviso**;
     - si existe el documento de lo que quedó hecho y no tiene ni una barra vertical —o sea, ninguna tabla— → **aviso**;
     - si tiene ❌ → **aviso**, para que alguien confirme por qué quedó así.
- **Retorna:** la lista de hallazgos.

`ORIGEN` se busca en mayúsculas a propósito: así se llama el campo. Buscándolo en minúsculas, cualquier frase que hablara del origen de algo pasaría por bueno.

## Cómo se ejecuta

```
python validadores/validar.py trazabilidad --raiz "C:/ruta/proyecto"
```

Por dentro:

```
EP-001-facturacion/
   │
   ├── epica.md ───────────── ¿nombra a HU-003?  ← si no, AVISO
   │                                 ▲
   │                                 │ se miran en los dos sentidos
   │                                 ▼
   └── HU-003-registrar/
          ├── HU-003-registrar.md ── ¿nombra a EP-001?  ← si no, AVISO
          │
          └── A-EP-001-HU-003-configuracion/
                 ├── plan_trabajo.md ──────────── ¿dice ORIGEN?  ← si no, AVISO
                 └── funcionalidad_implementada.md
                            ¿trae tabla?   ← si no, AVISO
                            ¿tiene ❌?     ← si sí, AVISO
```

## Ejemplos de lo que retorna

```python
_texto('C:/…/EP-001-facturacion/epica.md')
'# EP-001 — Facturación\n\nHistorias: HU-003, HU-004.\n'

_texto('C:/ruta/que/no/existe.md')
''

_sin_codigo('Texto real.\n```\nEP-999 de ejemplo\n```\nMás texto.')
'Texto real.\nMás texto.'

_menciona('Cuelga de EP-1.', 'EP', 1)      →  True
_menciona('Cuelga de EP-001.', 'EP', 1)    →  True     # el ancho no importa
_menciona('Cuelga de EP1.', 'EP', 1)       →  True     # el guion tampoco
_menciona('Cuelga de EP-002.', 'EP', 1)    →  False

validar('C:/proyectos/pos')          # todo bien
[]

validar('C:/proyectos/sin-documentacion')
[Hallazgo(FALLA, 'C:/proyectos/sin-documentacion', 0,
          'no existe `documentacion/epicas` (F12.13)')]

validar('C:/proyectos/pos')          # con problemas
[Hallazgo(AVISO, 'documentacion/epicas/EP-001-facturacion/HU-003-registrar', 0,
          'la HU no declara su épica EP-1 (DOC16 · enlace bidireccional)'),

 Hallazgo(AVISO, 'documentacion/epicas/EP-001-facturacion', 0,
          'la épica no lista la HU-3 que cuelga de ella (DOC16)'),

 Hallazgo(AVISO, '…/HU-003-registrar/A-EP-001-HU-003-configuracion', 0,
          'el plan_trabajo no declara ORIGEN (DOC12)'),

 Hallazgo(AVISO, '…/HU-003-registrar/A-EP-001-HU-003-configuracion', 0,
          'la funcionalidad_implementada no trae tabla de trazabilidad (DOC11)'),

 Hallazgo(AVISO, '…/HU-003-registrar/B-EP-001-HU-003-implementacion', 0,
          'hay ítems ❌ en la trazabilidad — confirmar que estén justificados (DOC11)')]
```
