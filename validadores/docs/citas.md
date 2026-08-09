# `citas.py`

Hace que cada regla citada por su código lleve un enlace al sitio exacto donde está escrita. Las busca, las enlaza y comprueba que no quede ninguna suelta.

## Qué hace

Cada regla del estándar tiene un código corto, y las reglas se nombran entre ellas por ese código: `09·G2`, `M5`, `04·S4`. Si el código va suelto, quien lee tiene que salir a buscar la regla: abrir el capítulo, encontrar el título. Con enlace, llega de un clic.

Este archivo hace tres cosas:

1. **Anota** dónde está escrita cada regla, leyendo la carpeta `base/`. Lo que vale es lo que dicen los archivos, no una tabla que alguien mantiene a mano.
2. **Enlaza** los códigos que van sueltos, y de paso los deja todos escritos de la misma forma.
3. **Comprueba** que no quede ninguno suelto y que ningún enlace lleve a algo que no existe.

Lo que está adentro de un bloque de código no se toca: ahí los códigos son ejemplos que muestran cómo se escribe una regla.

Es el único validador que además de revisar puede **cambiar** los archivos, y solo cuando se lo piden con `--aplicar`.

## De qué depende y quién lo usa

```
citas.py
   └── comun.py ··· AVISO, FALLA, Hallazgo, RAIZ, leer, recorrer_md y relativo
```

De Python usa `os` y `re`.

Lo usan:

```
citas.py
   ▲
   ├── validar.py ··· cuando alguien pide revisar "estandar"
   └── pruebas.py
```

También se puede correr solo, con `python validadores/citas.py`.

## Qué tiene adentro

### Valores fijos

| Nombre | Qué guarda |
|---|---|
| `BASE` | `base`, la carpeta donde viven las reglas. |
| `_REGLA` | Reconoce el título de una regla: uno o dos `#`, el código, un `·` y el título. |
| `_REGLA_M` | La misma búsqueda, aplicada sobre el archivo entero. |
| `_SUBREGLA` | Reconoce una regla más chica, numerada y en negrita, que vive adentro del archivo de la regla grande a la que pertenece. |
| `_ID` | Qué forma tiene un código de regla: de una a cuatro letras, un número y, si acaso, un punto y otro número. |
| `_CITA` | Reconoce la forma normal de nombrar una regla. |
| `_CITA_PARTIDA` | Reconoce la forma en que el capítulo y el código van separados. |
| `_DEPENDENCIA` | Reconoce cuando una regla dice de cuál otra depende: «(extiende 09·G6)». |
| `_CITA_ENLAZADA` | Reconoce un código que ya tiene su enlace, para poder mirar a dónde lleva. |
| `_CERCA` | Reconoce la línea que abre o cierra un bloque de código. |

Se reconocen tres formas de nombrar una regla porque las tres conviven hoy en `base/`: la normal, y dos en que el capítulo va entre comillas y el código afuera, con espacio en medio o sin él.

### Funciones

**`ancla(titulo_completo)`**

- **Recibe:** el título completo de una regla.
- **Hace:** lo pasa a minúsculas, le quita los signos y cambia **cada** espacio por un guion.
- **Retorna:** el pedazo del enlace que va después del `#`. Eso es lo que hace que el enlace caiga en el título exacto y no al comienzo del archivo.

Lo de «cada espacio» importa: el `·` que separa el código del título tiene un espacio a cada lado, así que al quitarlo quedan dos espacios seguidos, y eso son dos guiones. Poner uno solo daría un enlace que no lleva a ninguna parte.

**`indice(raiz=None)`**

- **Recibe:** opcionalmente la carpeta del estándar.
- **Hace:** recorre todos los `.md` de `base/`, salta lo que está adentro de bloques de código y anota cada título de regla. Si una regla vive sola en su archivo, no hace falta apuntar al título: el enlace al archivo ya lleva a ella. Después busca las reglas más chicas escritas en negrita y las apunta al archivo de la regla grande a la que pertenecen.
- **Retorna:** una lista de «código de regla → en qué archivo está y en qué título».

**`destino(origen, id, idx)`**

- **Recibe:** el archivo desde donde se nombra la regla, el código de la regla y esa lista.
- **Retorna:** la dirección que hay que escribir, contada desde el archivo que nombra; o texto vacío si esa regla no existe.

**`enlazar(texto, origen, idx)`**

- **Recibe:** el contenido de un archivo, dónde está y la lista de reglas.
- **Hace:** recorre el texto línea por línea, saltando los bloques de código y los títulos, y le pone enlace a cada código que iba suelto. Si esa regla no existe, lo deja como estaba: un enlace roto es peor que ninguno. Tampoco enlaza una regla consigo misma.
- **Retorna:** un par «texto nuevo, cuántos códigos se enlazaron».

El orden importa: primero se atiende la forma partida, porque su capítulo entre comillas también encajaría a medias en las otras dos y quedarían mal.

**`reparar(texto, origen, idx)`**

- **Recibe:** el contenido, dónde está y la lista de reglas.
- **Hace:** busca los códigos que ya tienen enlace y mira a dónde llevan. Si el archivo de esa regla se movió, corrige la dirección.
- **Retorna:** un par «texto nuevo, cuántas se corrigieron».

Sin esto, la exigencia de enlazar duraría hasta la primera vez que alguien mueva una carpeta de sitio.

**`validar(raiz=None)`**

- **Recibe:** opcionalmente la carpeta del estándar.
- **Hace:** recorre `base/` y por cada línea que no esté adentro de un bloque de código ni sea un título:
  - Enlace a una regla que no existe → **falla**.
  - Enlace que lleva a un archivo distinto del que le toca → **aviso**.
  - Código suelto, sin enlace, de una regla que sí existe y vive en otro archivo → **aviso**.
- **Retorna:** la lista de hallazgos.

**`aplicar(raiz=None, escribir=False)`**

- **Recibe:** opcionalmente la carpeta del estándar y si se escriben los cambios.
- **Hace:** por cada archivo de `base/` corre `enlazar` y después `reparar`. Si hubo cambios y `escribir` es verdadero, guarda el archivo.
- **Retorna:** una lista de tríos «archivo, cuántas enlazadas, cuántas reparadas».

### Bloque final

Cuando se corre este archivo directamente, muestra cuántas reglas encontró, qué archivos tocaría y cuántos cambios haría. Sin `--aplicar` no escribe nada: solo dice qué haría.

## Cómo se ejecuta

Para revisar:

```
python validadores/validar.py estandar
```

Para enlazar de verdad:

```
python validadores/citas.py             simula
python validadores/citas.py --aplicar   escribe los cambios
```

Por dentro:

```
indice(raiz)
   ↓ recorre base/ y anota dónde está cada regla
   ↓ {"G2": ("base/09-git.md", "g2--primera-linea"), ...}
   ↓
por cada archivo de base/:
   enlazar()  → les pone enlace a los códigos que iban sueltos
   reparar()  → corrige los enlaces que llevaban a otro sitio
   ↓
si se pidió --aplicar → se guarda el archivo
```

## Ejemplos de lo que retorna

```python
ancla('G2 · Mensaje de commit')
'g2--mensaje-de-commit'
#   └─ dos guiones: el · desaparece y quedan sus dos espacios

ancla('F13 · Detente si el proyecto no tiene su estructura base')
'f13--detente-si-el-proyecto-no-tiene-su-estructura-base'

indice()
{'G2':    ('c:\…\base\09-git.md', 'g2--mensaje-de-commit'),
 'G3':    ('c:\…\base\09-git.md', 'g3--que-no-se-versiona'),
 'F13':   ('c:\…\base\02-flujo-de-trabajo\reglas\F13-….md', ''),
 'F12.1': ('c:\…\base\02-flujo-de-trabajo\reglas\F12-….md', '')}
#  └─ código  └─ en qué archivo está        └─ el ancla; vacía si la regla
#                                              tiene el archivo para ella sola

destino('c:\…\base\13-documentacion\base.md', 'G2', idx)
'../09-git.md#g2--mensaje-de-commit'

destino('c:\…\base\13-documentacion\base.md', 'NO-EXISTE', idx)
''

enlazar('Se versiona como dice `09·G3`.', origen, idx)
('Se versiona como dice [`09·G3`](../09-git.md#g3--que-no-se-versiona).', 1)
#  └─ el texto ya con el enlace                                          └─ cuántas

enlazar('Se versiona como dice `09·XX9`.', origen, idx)
('Se versiona como dice `09·XX9`.', 0)
#  la regla no existe: se deja igual y el validador la reporta

enlazar('```\nEjemplo: `09·G3`\n```', origen, idx)
('```\nEjemplo: `09·G3`\n```', 0)
#  lo que está entre ``` no se toca

reparar('Ver [`09·G3`](../viejo/09-git.md).', origen, idx)
('Ver [`09·G3`](../09-git.md#g3--que-no-se-versiona).', 1)
#  el archivo se había movido: se corrige la dirección

validar()
[Hallazgo(FALLA, 'c:\…\base\05-errores.md', 22,
          'la cita `XX9` enlaza a una regla que no existe'),
 Hallazgo(AVISO, 'c:\…\base\07-calidad.md', 8,
          'la cita `G3` apunta a «../viejo/09-git.md» y la regla está en
           «../09-git.md#g3--que-no-se-versiona»'),
 Hallazgo(AVISO, 'c:\…\base\08-pruebas.md', 15,
          'la cita `Q6` no lleva enlace — quien lea tiene que ir a buscarla')]

aplicar(escribir=False)
[('c:\…\base\05-errores.md', 3, 0),
 ('c:\…\base\07-calidad.md', 0, 2)]
#  └─ archivo                   └─ enlazadas  └─ reparadas

# y en pantalla, al correr `python validadores/citas.py`:
285 reglas indexadas en base/

  3 enlazadas                  base/05-errores.md
  2 reparadas                  base/07-calidad.md

3 enlazadas · 2 reparadas · 2 archivos (simulado; agrega --aplicar)
```
