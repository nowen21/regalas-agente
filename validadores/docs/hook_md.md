# `hook_md.py`

Arranca solo después de escribir o cambiar un archivo y, si era un documento del proyecto, revisa que no hayan quedado enlaces rotos.

## Qué hace

Lee el aviso que manda Claude Code cada vez que el agente escribe o cambia un archivo, y decide:

- Si no es un `.md`, o es un `.md` que está fuera de la carpeta que se está revisando, no hace nada.
- Si lo es, corre las dos comprobaciones de `enlaces.py`: enlaces rotos e índices a los que les falta algo.

Si el cambio rompió algo, le retorna el detalle al agente para que lo arregle ahí mismo, sin esperar a que alguien lo note después.

De todos los programas que arrancan solos, este es el único que puede terminar mal a propósito:

| Cómo termina | Qué significa |
|---|---|
| `0` | Todo bien, o no había nada que revisar. |
| `2` | Hay fallas. Claude Code se las retorna al agente para que las arregle. |

## De qué depende y quién lo usa

```
hook_md.py
   ├── enlaces.py ··· validar_enlaces() y validar_indices()
   └── comun.py ····· FALLA, RAIZ y preparar_salida
```

De Python usa `json`, `os` y `sys`.

Ningún archivo lo usa a él. Lo llama Claude Code después de cada archivo que se escribe o se cambia.

## Qué tiene adentro

**`raiz_pedida(argv)`**

- **Recibe:** lo que se escribió en la consola.
- **Hace:** busca `--raiz` y toma lo que viene después.
- **Retorna:** esa carpeta, o la del estándar si no se dijo ninguna.

**`archivo_editado(datos)`**

- **Recibe:** lo que manda Claude Code.
- **Hace:** busca dónde está el archivo en tres sitios: primero en lo que se le pidió a la herramienta, y después en dos formas distintas de la respuesta.
- **Retorna:** esa dirección, o texto vacío.

**`es_md_de(ruta, raiz)`**

- **Recibe:** la dirección de un archivo y la carpeta que se está revisando.
- **Hace:** comprueba que termine en `.md` y que esté adentro de esa carpeta. Si están en discos distintos ni siquiera se pueden comparar, así que responde que no.
- **Retorna:** verdadero o falso.

**`main()`**

- **Recibe:** nada.
- **Hace:**
  1. Deja la pantalla lista y averigua qué carpeta hay que revisar.
  2. Lee lo que le mandaron. Si viene mal escrito, termina bien y no hace nada.
  3. Si el archivo que se tocó no es un `.md` de esa carpeta, termina bien.
  4. Corre las dos comprobaciones de enlaces y se queda solo con las fallas.
  5. Si no hay fallas, termina bien.
  6. Si las hay, las escribe aparte y termina con `2`.
- **Retorna:** `0` o `2`.

## Cómo se ejecuta

Lo deja puesto `instalar.py` en el archivo de ajustes `.claude/settings.json`, para que arranque después de escribir o cambiar un archivo:

```
python "<estandar>/validadores/hook_md.py" --raiz "<proyecto>"
```

Por dentro:

```
el agente escribe o cambia un archivo
        ↓
hook_md.py --raiz <proyecto>
        ↓
lee lo que le manda Claude Code
        ↓
archivo_editado(datos)  →  dónde está el archivo
        ↓
es_md_de(ruta, carpeta)
     no es un .md, o está afuera → termina bien
     sí ↓
enlaces.validar_enlaces(carpeta) + enlaces.validar_indices(carpeta)
        ↓
¿hay alguna FALLA?
     no → termina bien
     sí → escribe el detalle y termina con 2
          Claude Code se lo retorna al agente para que lo arregle
```

## Ejemplos de lo que retorna

```python
raiz_pedida(['--raiz', 'C:/proyectos/pos'])
'C:\proyectos\pos'

raiz_pedida([])
'c:\Ing. Jose\ia\agente'      # la carpeta del estándar

archivo_editado({'tool_input': {'file_path': 'c:/…/base/09-git.md'}})
'c:/…/base/09-git.md'

archivo_editado({'tool_response': {'filePath': 'c:/…/base/09-git.md'}})
'c:/…/base/09-git.md'

archivo_editado({})
''

es_md_de('c:/Ing. Jose/ia/agente/base/09-git.md', 'c:\Ing. Jose\ia\agente')
True

es_md_de('c:/Ing. Jose/ia/agente/validadores/comun.py', 'c:\Ing. Jose\ia\agente')
False            # no es un .md

es_md_de('D:/otra/parte/notas.md', 'c:\Ing. Jose\ia\agente')
False            # está en otro disco

main()
0                # todo bien, o no aplicaba
2                # hay enlaces rotos
```

Cuando todo está bien no imprime nada. Cuando encuentra enlaces rotos escribe esto aparte y termina con `2`:

```
La edición dejó enlaces rotos:
  [FALLA] notas/decisiones.md:14 — enlace roto: ../base/09-git-viejo.md
  [FALLA] pendientes/README.md — el índice no menciona pendientes/10-ideas.md
```

Ese `2` es la señal para que Claude Code le devuelva el texto al agente y lo corrija ahí mismo.
