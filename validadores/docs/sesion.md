# `sesion.py`

Cuando alguien empieza a trabajar en un proyecto, revisa si el estándar quedó bien puesto: las carpetas, el `CLAUDE.md` y los enganches de git.

Un **enganche** es un programa que arranca solo cuando pasa algo, sin que nadie lo llame.

## Qué hace

Responde tres preguntas:

1. ¿Existe la carpeta `proyectos/`? Si no existe, el proyecto nunca se instaló y revisar lo demás no tiene sentido todavía.
2. ¿El `CLAUDE.md` del proyecto está al día con el molde central?
3. ¿Los enganches de git están puestos y apuntan a este estándar y no a otro?

Retorna una lista de hallazgos y sabe resumirla en una línea para mostrarla en pantalla.

## De qué depende y quién lo usa

```
sesion.py
   ├── instalar.py ··· cumple_f13(), repositorios_git() y la lista HOOKS
   └── comun.py ······ AVISO, FALLA, Hallazgo, encabezados y leer
```

De Python usa `os` y `re`.

Lo usan:

```
sesion.py
   ▲
   ├── hook_sesion.py ··· lo corre al abrir cada sesión
   └── checklist.py ····· reutiliza revisar_claude_md y revisar_enganches
```

## Qué tiene adentro

### Valores fijos

| Nombre | Qué guarda |
|---|---|
| `PLANTILLA_CLAUDE` | La ruta de la plantilla central: `plantillas/CLAUDE.md.plantilla`. |
| `_SIN_LLENAR` | Reconoce un hueco sin llenar, escrito entre comillas angulares. Deja fuera el caso «…», que no es un hueco sino la forma de nombrar a los huecos cuando el texto habla de ellos. |
| `_ESTANDAR_EN_HOOK` | Reconoce, dentro de un enganche de git, la línea que declara a qué estándar apunta. |

### Funciones

**`_ruta_plantilla(estandar)`**

- **Recibe:** la carpeta del estándar.
- **Retorna:** la ruta completa de la plantilla del `CLAUDE.md`.

**`revisar_claude_md(proyecto, estandar)`**

- **Recibe:** la carpeta del proyecto y la del estándar.
- **Hace:**
  1. Si no existe el `CLAUDE.md` del proyecto, retorna una falla.
  2. Si no existe la plantilla central, retorna un aviso.
  3. Compara los títulos de los dos y avisa por cada sección que el molde tiene y el proyecto no.
  4. Busca huecos sin llenar y reporta cada uno como falla, con su número de línea.
  5. Si el molde central se cambió después del `CLAUDE.md` del proyecto, avisa que hay que mirar si algo cambió.
- **Retorna:** la lista de hallazgos.

Solo informa lo que **falta**. Que el proyecto tenga secciones propias de más no se cuestiona.

**`revisar_enganches(proyecto, estandar)`**

- **Recibe:** la carpeta del proyecto y la del estándar.
- **Hace:** por cada repositorio git del proyecto y por cada enganche esperado, mira si el archivo existe en `.githooks/` y si la línea que declara el estándar apunta a esta carpeta.
- **Retorna:** la lista de avisos, uno por enganche que falte o que apunte a otro sitio.

Se compara contra esa línea y no contra la dirección completa del validador, porque adentro del enganche esa dirección está partida en dos: primero se guarda con un nombre y más abajo se usa por ese nombre.

**`revisar(proyecto, estandar)`**

- **Recibe:** la carpeta del proyecto y la del estándar.
- **Hace:** primero comprueba que exista la carpeta `proyectos/`. Si no existe, retorna una sola falla diciendo que el proyecto no está instalado y no revisa nada más. Si existe, junta el resultado de las dos funciones anteriores.
- **Retorna:** la lista de hallazgos.

**`resumen(proyecto, hallazgos)`**

- **Recibe:** la carpeta y la lista de hallazgos.
- **Hace:** cuenta fallas y avisos y toma los tres primeros mensajes.
- **Retorna:** una línea para mostrar en pantalla. Si no hay hallazgos: «Estándar cargado · nombre · F13 ok · CLAUDE.md al día · enganches puestos».

## Cómo se ejecuta

Al abrir una sesión:

```
Claude Code abre la sesión
        ↓
hook_sesion.py
        ↓
sesion.revisar(proyecto, estandar)
        ↓
   ¿existe proyectos/?
        no → una sola FALLA y termina
        sí ↓
   revisar_claude_md()   → secciones que faltan, huecos sin llenar, fecha
   revisar_enganches()   → enganches de git puestos y apuntando bien
        ↓
sesion.resumen(...)  → la línea que ve el usuario
```

## Ejemplos de lo que retorna

```python
_ruta_plantilla('c:/…/agente')
'c:/…/agente\plantillas\CLAUDE.md.plantilla'

revisar_claude_md('C:/proyectos/pos', 'c:/…/agente')
[Hallazgo(AVISO, 'C:/proyectos/pos\CLAUDE.md', 0,
          'la plantilla central tiene «4 · Antes de commitear» y este CLAUDE.md
           no — C18: agregar la sección vacía, sin pisar lo escrito'),
 Hallazgo(FALLA, 'C:/proyectos/pos\CLAUDE.md', 7,
          'quedó sin reemplazar: «NOMBRE-PROYECTO»'),
 Hallazgo(AVISO, 'C:/proyectos/pos\CLAUDE.md', 0,
          'la plantilla central cambió después de este CLAUDE.md — C18: revisar
           si hay algo nuevo que agregar')]

revisar_claude_md('C:/proyectos/al-dia', 'c:/…/agente')
[]

# si ni siquiera existe el archivo:
revisar_claude_md('C:/proyectos/vacio', 'c:/…/agente')
[Hallazgo(FALLA, 'C:/proyectos/vacio\CLAUDE.md', 0,
          'no existe el CLAUDE.md del proyecto')]

revisar_enganches('C:/proyectos/pos', 'c:/…/agente')
[Hallazgo(AVISO, 'pos-back/', 0,
          'falta el enganche pre-commit — correr validadores/instalar.py'),
 Hallazgo(AVISO, 'pos-front/', 0,
          'el enganche commit-msg apunta a «c:/viejo/agente» y no a este
           estándar — reinstalar')]

revisar('C:/proyectos/sin-instalar', 'c:/…/agente')
[Hallazgo(FALLA, 'C:/proyectos/sin-instalar', 0,
          'falta la carpeta `proyectos/` (02·F13): este proyecto no está
           instalado — correr validadores/instalar.py --aplicar')]
# cuando falta esto, no revisa nada más

revisar('C:/proyectos/pos', 'c:/…/agente')
[ ... lo de revisar_claude_md  +  lo de revisar_enganches ... ]

resumen('C:/proyectos/pos', [])
'Estándar cargado · pos · F13 ok · CLAUDE.md al día · enganches puestos'

resumen('C:/proyectos/pos', hallazgos)
'Estándar cargado · pos · 1 falla(s) y 2 aviso(s): quedó sin reemplazar:
 «NOMBRE-PROYECTO»; falta el enganche pre-commit — correr …; la plantilla
 central cambió después de este CLAUDE.md — …'
```
