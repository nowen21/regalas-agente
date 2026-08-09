# `commits.py`

Revisa el mensaje con que se guarda un cambio en git: que diga algo, que esté bien armado y que no lleve la firma de ninguna herramienta.

## Qué hace

Guardar un cambio en git se llama hacer un **commit**, y cada uno lleva un mensaje que cuenta qué se hizo. Ese mensaje tiene dos partes: la primera línea, que es el **asunto** y resume todo, y el **cuerpo**, que es lo que va debajo y lo explica.

Este archivo comprueba cuatro cosas:

- Que el mensaje no esté vacío.
- Que el asunto diga algo. Uno que solo dice «cambios», «fix» o «wip» no cuenta: dentro de un año nadie sabrá qué pasó ahí.
- Que, si hay cuerpo, haya una línea en blanco entre él y el asunto. Sin esa línea, git los junta y los lee como una sola cosa.
- Que el mensaje no diga que lo escribió una herramienta.

Y avisa por dos cosas más: que el asunto termine en punto y que pase de 72 caracteres, porque más largo se corta al mostrarlo.

## De qué depende y quién lo usa

```
commits.py
   └── comun.py ··· AVISO, FALLA y Hallazgo
```

De Python usa `re` y `subprocess` (para leer un cambio ya guardado).

Lo usan:

```
commits.py
   ▲
   ├── validar.py ··· cuando alguien pide revisar "commit"
   └── pruebas.py
```

Y a través de `validar.py`, el `commit-msg`: un programa que git arranca solo —a eso se le dice **enganche**— para revisar el mensaje antes de aceptar el cambio.

## Qué tiene adentro

### Valores fijos

| Nombre | Qué guarda |
|---|---|
| `LARGO_MAXIMO` | `72`. Hasta cuántos caracteres debería tener el asunto. |
| `VACIOS` | Los asuntos que no dicen nada: `cambios`, `cambio`, `fix`, `wip`, `update`, `actualizacion`, `actualización`, `varios`, `arreglo`, `arreglos`, `ajustes`, `ajuste`, `commit`, `misc`, `temp`, `prueba`, `test`. |
| `PROHIBIDOS` | Las dos firmas de herramienta que no pueden aparecer: `Co-Authored-By:` y «Generated with Claude Code». |

Al buscar `Co-Authored-By` se aceptan espacios y tabulaciones alrededor, pero no saltos de línea. Si se aceptaran, el problema quedaría señalado una línea más arriba de donde está.

### Funciones

**`leer_de_git(revision="HEAD")`**

- **Recibe:** opcionalmente cuál cambio guardado se quiere leer. Si no se dice cuál, el último.
- **Hace:** le pide a git ese mensaje con `git log -1`.
- **Retorna:** el mensaje completo.

**`validar(mensaje, origen="(mensaje)")`**

- **Recibe:** el texto del mensaje y, si se quiere, de dónde salió, para poder decirlo al reportar.
- **Hace:**
  1. Bota las líneas que empiezan con `#`, que git no guarda, y las líneas vacías del final.
  2. Si no queda nada, retorna una falla y termina.
  3. Toma la primera línea como asunto.
  4. Si el asunto es uno de los que no dicen nada → **falla**.
  5. Si termina en punto → **aviso**.
  6. Si pasa de 72 caracteres → **aviso**.
  7. Si la segunda línea tiene texto → **falla**: falta la línea en blanco.
  8. Por cada firma de herramienta que aparezca → **falla**, señalando su línea.
- **Retorna:** la lista de hallazgos.

Lo que no se comprueba, porque un programa no puede juzgarlo, es que el cuerpo arranque contando la idea del usuario.

## Cómo se ejecuta

Antes de aceptar un commit:

```
git commit
        ↓
.githooks/commit-msg
        ↓
validar.py commit --archivo .git/COMMIT_EDITMSG
        ↓
commits.validar(mensaje, origen)
        ↓
   ¿hay alguna FALLA?
        sí → el cambio no se guarda
        no → el cambio se guarda
```

A mano:

```
python validadores/validar.py commit                          revisa el último
python validadores/validar.py commit --archivo <ruta>         revisa un archivo
python validadores/validar.py commit --revision <commit>      revisa otro cambio
```

## Ejemplos de lo que retorna

```python
leer_de_git('HEAD')
'estandar: la instalación se hace sola y CLAUDE.md es el setup\n\nEl usuario
 pidió que instalar no dependa de pasos manuales.\n'

validar('Corrige el saldo cuando hay documentos anulados\n\n'
        'Se sumaban al total; ahora se excluyen en la consulta.\n')
[]               # el mensaje está bien

validar('\n\n')
[Hallazgo(FALLA, '(mensaje)', 1, 'el mensaje está vacío')]

validar('wip')
[Hallazgo(FALLA, '(mensaje)', 1,
          'asunto sin contenido: «wip» — G2 pide qué y por qué')]

validar('Corrige el saldo con documentos anulados\nSe sumaban al total.\n')
[Hallazgo(FALLA, '(mensaje)', 2,
          'falta la línea en blanco entre el asunto y el cuerpo')]

validar('Corrige el saldo.')
[Hallazgo(AVISO, '(mensaje)', 1, 'el asunto no lleva punto final')]

validar('C' * 100)
[Hallazgo(AVISO, '(mensaje)', 1,
          'asunto de 100 caracteres; G2 lo pide breve (referencia: 72)')]

validar('Corrige el saldo\n\nSe sumaban al total.\n\n'
        'Co-Authored-By: Alguien <a@b.c>\n')
[Hallazgo(FALLA, '(mensaje)', 5,
          'el mensaje incluye Co-Authored-By — G8 no firma con la herramienta')]

# el mismo mensaje, ya impreso por validar.py:
== Mensaje de commit HEAD ==
[FALLA] commit HEAD:5 — el mensaje incluye Co-Authored-By — G8 no firma …

1 falla(s), 0 aviso(s).
```
