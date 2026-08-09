# `hook_sesion.py`

Arranca solo cuando alguien empieza a trabajar: revisa cómo quedó puesto el estándar y le entrega al agente lo que, recién llegado, no puede saber.

## Qué hace

Dos cosas distintas:

**Avisa.** Corre la revisión de `sesion.py` y retorna una línea de resumen que Claude Code le muestra al usuario en pantalla.

**Carga.** Le entrega al agente tres cosas:

| Qué le entrega | De dónde sale | Cuánto |
|---|---|---|
| Las reglas | `cargador.py` | Los capítulos `00` y `01` enteros; del resto, solo la lista. |
| Los recuerdos del proyecto | `recuerdos.py` | El índice completo, que dice de qué trata cada uno. |
| Las conversaciones anteriores | `historico.py` | La lista de las últimas cuarenta, con el tema de cada una. |

De los recuerdos y de las conversaciones va la lista y no el contenido: cada conversación guardada es larguísima, y el agente puede tener a la vista solo una cantidad limitada de texto. Con la lista le alcanza para saber cuál abrir si la necesita.

Los recuerdos y las conversaciones se cargan **también cuando se trabaja en el estándar mismo**: ahí no hay instalación que revisar, pero los recuerdos y las conversaciones son igual de necesarios.

Siempre termina bien, aunque encuentre problemas. Esto avisa, no traba: que no se pueda empezar a trabajar porque al `CLAUDE.md` le falta una sección sería peor que el problema que resuelve.

## De qué depende y quién lo usa

```
hook_sesion.py
   ├── cargador.py ···· contexto() con las reglas base
   ├── recuerdos.py ··· contexto() con el índice de la memoria
   ├── historico.py ··· contexto() con el índice de sesiones
   ├── sesion.py ······ revisar() y resumen()
   ├── instalar.py ···· cumple_f13()
   └── comun.py ······· RAIZ y preparar_salida
```

De Python usa `json`, `os` y `sys`.

Ningún archivo lo usa a él. Lo llama Claude Code cuando se abre una sesión, con la orden que `instalar.py` dejó escrita en el archivo de ajustes.

## Qué tiene adentro

**`raiz_pedida(argv)`**

- **Recibe:** lo que se escribió en la consola.
- **Hace:** busca `--raiz` y toma lo que viene después.
- **Retorna:** esa carpeta, o la carpeta donde se está parado si no se dijo ninguna.

**`_del_proyecto(proyecto)`**

- **Recibe:** la carpeta del proyecto.
- **Hace:** llama a `recuerdos.contexto` y a `historico.contexto`. Si alguno se rompe, en vez de tumbar todo deja escrito que eso no se pudo cargar.
- **Retorna:** los dos textos unidos.

**`main()`**

- **Recibe:** nada.
- **Hace:**
  1. Deja la pantalla lista y averigua sobre qué carpeta hay que trabajar.
  2. Carga los recuerdos y las conversaciones anteriores.
  3. Si esa carpeta es la del estándar mismo, responde solo con eso y termina.
  4. Si no, corre la revisión. Si se rompe, responde con el error y termina.
  5. Carga las reglas, diciéndole a `cargador` si el proyecto ya tiene su carpeta `proyectos/`. Si se rompe, deja escrito que no se pudieron cargar.
  6. Responde con el resumen, lo que encontró y todo el texto cargado.
- **Retorna:** siempre `0`, o sea que terminó bien.

Las reglas se cargan aunque la revisión encuentre problemas: que el `CLAUDE.md` esté viejo no es razón para trabajar sin reglas.

**`_responder(resumen, hallazgos, reglas)`**

- **Recibe:** la línea de resumen, la lista de hallazgos y el texto de las reglas.
- **Hace:** escribe la respuesta con dos partes:
  - una que Claude Code le muestra al usuario en pantalla: solo el resumen;
  - otra que le llega al agente: el resumen con su detalle, más todo lo cargado.
- **Retorna:** nada.

Se usan las dos porque la primera depende de que la pantalla la dibuje, y podría no verse. Las reglas van solo por la segunda: en pantalla serían decenas de miles de caracteres tapándolo todo.

## Cómo se ejecuta

Lo deja puesto `instalar.py` en el archivo de ajustes `.claude/settings.json`, para que arranque al abrir una sesión:

```
python "<estandar>/validadores/hook_sesion.py" --raiz "<proyecto>"
```

Por dentro:

```
Claude Code abre la sesión
        ↓
hook_sesion.py --raiz <proyecto>
        ↓
_del_proyecto(proyecto)
     recuerdos.contexto()  → el índice de los recuerdos
     historico.contexto()  → la lista de las últimas 40 conversaciones
        ↓
¿la carpeta es la del estándar mismo?
     sí → responde solo con eso y termina
     no ↓
sesion.revisar(proyecto, estandar)
     ¿existe proyectos/?  ¿el CLAUDE.md está al día?  ¿los enganches?
        ↓
cargador.contexto(estandar, cumple_f13)
     las reglas 00 y 01 enteras + la lista del resto
        ↓
_responder(...)
     una parte → la línea que ve el usuario en pantalla
     otra      → todo el texto que recibe el agente
        ↓
termina bien, siempre
```

## Ejemplos de lo que retorna

```python
raiz_pedida(['--raiz', 'C:/proyectos/pos'])
'C:\proyectos\pos'

raiz_pedida([])
'c:\Ing. Jose\ia\agente'      # la carpeta donde está parado

_del_proyecto('C:/proyectos/pos')
'''[MEMORIA DEL AGENTE — ÍNDICE, OBLIGATORIA]
… el índice de los recuerdos …

[HISTÓRICO DE SESIONES — NO ESTÁ CARGADO, SOLO EL ÍNDICE]
… la lista de las últimas 40 conversaciones …'''

_del_proyecto('C:/proyectos/nuevo')
''               # todavía no hay recuerdos ni conversaciones

main()
0                # siempre
```

Y esto es lo que imprime, que es lo que Claude Code lee:

```json
{
  "systemMessage": "Estándar cargado · pos · F13 ok · CLAUDE.md al día · enganches puestos",
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "[Revisión de arranque del estándar]\nEstándar cargado · pos · …\n\n[REGLAS BASE DEL ESTÁNDAR — CARGADAS, OBLIGATORIAS]\n… las reglas 00 y 01 enteras …\n\n[MEMORIA DEL AGENTE — ÍNDICE, OBLIGATORIA]\n…\n\n[HISTÓRICO DE SESIONES — NO ESTÁ CARGADO, SOLO EL ÍNDICE]\n…"
  }
}
```

Cuando algo no está bien puesto, el resumen cambia y se agrega el detalle:

```json
{
  "systemMessage": "Estándar cargado · pos · 1 falla(s) y 2 aviso(s): quedó sin reemplazar: «NOMBRE-PROYECTO»; …",
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "[Revisión de arranque del estándar]\nEstándar cargado · pos · 1 falla(s)…\n  - [FALLA] CLAUDE.md:7 — quedó sin reemplazar: «NOMBRE-PROYECTO»\n  - [AVISO] pos-back/ — falta el enganche pre-commit — correr validadores/instalar.py\n\n[REGLAS BASE…]"
  }
}
```
