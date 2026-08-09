# `version.py`

Compara la versión del estándar con la que el proyecto dice estar siguiendo, y avisa si quedó atrás.

## Qué hace

El estándar tiene un archivo `VERSION` con un número como `5.0.0`. Cada proyecto declara en su `CLAUDE.md` qué versión adoptó, en una línea que dice «Versión del estándar adoptada: X.Y.Z».

Este archivo lee las dos y las compara. Si el proyecto quedó atrás, **avisa; no actualiza nada**: subir de versión es decisión del usuario.

Todo lo que reporta es aviso, nunca falla.

## De qué depende y quién lo usa

```
version.py
   └── comun.py ··· AVISO, Hallazgo, RAIZ y leer
```

De Python usa `os` y `re`.

Lo usan:

```
version.py
   ▲
   ├── checklist.py ··· para exigir que el proyecto declare su versión
   ├── instalar.py ···· para escribirla en las marcas de huella
   ├── validar.py ····· cuando alguien pide revisar "version"
   └── pruebas.py
```

## Qué tiene adentro

### Valores fijos

| Nombre | Qué guarda |
|---|---|
| `_ADOPTADA` | La búsqueda que reconoce la línea «Versión del estándar adoptada: X.Y.Z» dentro del `CLAUDE.md`. No distingue mayúsculas ni tildes. |

### Funciones

**`_tupla(v)`**

- **Recibe:** un texto como `"5.0.0"`.
- **Retorna:** los tres números por separado, para poder compararlos como números y no como texto. Si se comparan como texto, `"10.0.0"` parece menor que `"9.0.0"`, porque el `1` va antes que el `9`.

**`version_estandar()`**

- **Recibe:** nada.
- **Hace:** lee el archivo `VERSION` de la raíz del estándar y toma su primera línea.
- **Retorna:** la versión, o nada si el archivo no existe.

**`extraer_adoptada(texto)`**

- **Recibe:** el contenido de un `CLAUDE.md`.
- **Hace:** busca la línea de la versión adoptada.
- **Retorna:** el número encontrado, o nada.

**`comparar(adoptada, estandar)`**

- **Recibe:** la versión que declara el proyecto y la del estándar.
- **Hace:** decide en este orden:
  1. Si el estándar no tiene versión, no hay nada que comparar.
  2. Si el proyecto no declara ninguna, lo dice.
  3. Si la del proyecto es menor, lo dice.
- **Retorna:** el texto del motivo, o nada si está al día.

Está separada del resto para poder probarla sin archivos en disco.

**`validar(raiz)`**

- **Recibe:** la carpeta del proyecto.
- **Hace:** lee el `VERSION` del estándar y el `CLAUDE.md` del proyecto, y los compara.
- **Retorna:** una lista con un aviso, o vacía si está al día. Si no hay `CLAUDE.md`, retorna un aviso diciendo que no se pudo leer la versión.

## Cómo se ejecuta

```
python validadores/validar.py version --raiz "C:/ruta/proyecto"
```

Por dentro:

```
validar(carpeta)
   ↓
version_estandar()          lee VERSION del estándar
   ↓
leer(carpeta/CLAUDE.md)
   ↓
extraer_adoptada(texto)     busca la línea de la versión adoptada
   ↓
comparar(adoptada, estandar)
   ↓
si hay motivo → [Hallazgo(AVISO, "CLAUDE.md", 0, motivo)]
si no          → []
```

## Ejemplos de lo que retorna

```python
_tupla('5.0.0')
(5, 0, 0)

version_estandar()
'5.0.0'          # o None si no hay archivo VERSION

extraer_adoptada('# Proyecto POS\n\nVersión del estándar adoptada: 4.0.0\n')
'4.0.0'

extraer_adoptada('# Proyecto POS\n\nSin declarar nada.\n')
None

comparar('4.0.0', '5.0.0')
'el proyecto declara v4.0.0, el estándar va en v5.0.0: subir es decisión
 del usuario; las fases cerradas quedan selladas'

comparar('5.0.0', '5.0.0')
None             # está al día

comparar(None, '5.0.0')
'el proyecto no declara qué versión del estándar sigue (el estándar va en
 v5.0.0) — fijarla en su CLAUDE.md'

comparar('4.0.0', None)
None             # el estándar no tiene VERSION: no hay contra qué comparar

validar('C:/proyectos/pos')
[Hallazgo(AVISO, 'CLAUDE.md', 0, 'el proyecto declara v4.0.0, el estándar
          va en v5.0.0: ...')]

# impreso:
[AVISO] CLAUDE.md — el proyecto declara v4.0.0, el estándar va en v5.0.0: ...

validar('C:/proyectos/al-dia')
[]
```
