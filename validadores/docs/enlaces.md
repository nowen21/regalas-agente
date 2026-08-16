# `enlaces.py`

Revisa que los enlaces de los documentos lleven a algo que existe, y que cada índice nombre todos los archivos de su carpeta.

## Qué hace

Dos comprobaciones sobre este repositorio:

1. **Enlaces rotos.** Cada enlace que se pueda comprobar tiene que llevar a un archivo o una carpeta que exista de verdad.
2. **Índices que quedaron viejos.** En las carpetas que tienen un `README.md` haciendo de índice, cada documento de la carpeta tiene que estar nombrado ahí.

No comprueba todos los enlaces. Deja fuera tres clases:

- Los que llevan `<` o `>` en el texto o en la dirección: son ejemplos de cómo se escribe un enlace, no enlaces a algo.
- Los que no llevan a un `.md` ni a una carpeta: llevan a código de un proyecto, que no vive en este repositorio.
- Los que están adentro de una conversación guardada en `historico-chat/`: esos archivos copian el chat tal cual, y en el chat los enlaces se escriben contados desde el comienzo del proyecto y no desde esa carpeta, así que parecerían rotos sin estarlo. El `README.md` de esa carpeta sí se revisa, porque ese lo escribe una persona.

## De qué depende y quién lo usa

```
enlaces.py
   └── comun.py ··· AVISO, FALLA, Hallazgo, RAIZ, enlaces, leer,
                    recorrer_md y relativo
```

De Python usa `os`.

Ojo: `enlaces` es a la vez el nombre de este archivo y el de una función de `comun.py`. Son cosas distintas; este archivo trae esa función y la usa adentro.

Lo usan:

```
enlaces.py
   ▲
   ├── hook_md.py ··· lo corre cada vez que se cambia un documento
   ├── validar.py ··· cuando alguien pide revisar "estandar"
   └── pruebas.py
```

## Qué tiene adentro

### Valores fijos

| Nombre | Qué guarda |
|---|---|
| `HISTORICO` | `historico-chat`, la carpeta donde se guardan las conversaciones. |
| `CON_INDICE` | Las carpetas cuyo `README.md` tiene que nombrar todos sus documentos: `pendientes`, `notas` e `historico-chat`. |
| `EXTERNOS` | Los comienzos de dirección que no se comprueban, porque llevan fuera del computador: `http://`, `https://`, `mailto:`, `ftp://` y `//`. |

### Funciones de apoyo

**`_es_interno(destino)`**

- **Recibe:** la dirección de un enlace.
- **Retorna:** verdadero si lleva a algo de este repositorio; o sea, si no sale del computador y no empieza con `#`, que es como se salta a otra parte del mismo documento.

**`_comprobable(texto, destino)`**

- **Recibe:** el texto que se ve del enlace y la dirección a la que lleva.
- **Hace:** deja fuera los que llevan `<` o `>` y los que no terminan en `.md` ni en `/`.
- **Retorna:** verdadero si se puede ir a buscar al disco lo que el enlace promete.

**`_es_transcripcion(archivo)`**

- **Recibe:** la dirección de un archivo.
- **Retorna:** verdadero si es una conversación guardada: está justo adentro de `historico-chat/` y no es el `README.md`.

### Funciones principales

**`validar_enlaces(raiz=None)`**

- **Recibe:** opcionalmente la carpeta a revisar. Por defecto, la del estándar.
- **Hace:**
  1. Recorre todos los `.md` de la carpeta.
  2. Salta las conversaciones guardadas.
  3. Por cada enlace que se pueda comprobar, arma la dirección contándola desde la carpeta donde está el archivo, y mira si existe. Lo que va después de un `#` no se comprueba: se mira el archivo, no en qué parte de él cae.
- **Retorna:** una lista de fallas, una por enlace roto.

**El enlace que empieza con `«RUTA-ESTANDAR»` es la excepción, y se cuenta desde otra parte.** Ese marcador lo llevan las plantillas para citar una regla, y lo rellena el instalador cuando la plantilla se copia a un proyecto. Cuando todavía está sin llenar, la dirección se cuenta desde **la carpeta donde vive el estándar**, no desde la que se está revisando.

Suena a detalle y no lo es. Este programa vive en el estándar y se le pasa el proyecto como parámetro, así que las dos carpetas casi nunca son la misma: contándolo desde la que se revisa, iría a buscar `«proyecto»/base/…` — una carpeta que ningún proyecto tiene, porque las reglas no se copian, se enganchan por su dirección completa. El enlace bueno saldría roto y el roto también, o sea que el resultado dependería de desde dónde se corriera el programa.

**`validar_indices(raiz=None, carpetas=None)`**

- **Recibe:** opcionalmente la carpeta a revisar y la lista de carpetas con índice.
- **Hace:** por cada carpeta con índice:
  1. Si no hay `README.md`, la salta.
  2. Lee los enlaces del índice y arma la lista de lo que está nombrado.
  3. Por cada documento de la carpeta que no sea el propio README, comprueba que esté nombrado en el índice. Si no, es una **falla**.
  4. Al revés: si el índice nombra un archivo de esa misma carpeta que ya no existe, es un **aviso**.
- **Retorna:** la lista de hallazgos.

## Cómo se ejecuta

Cada vez que se escribe o se cambia un documento:

```
el agente escribe o cambia un .md
        ↓
hook_md.py
        ↓
   ¿es un .md dentro de este repositorio?
        no → no hace nada
        sí ↓
enlaces.validar_enlaces(raiz) + enlaces.validar_indices(raiz)
        ↓
   ¿hay alguna FALLA?
        sí → se le retorna el detalle al agente para que lo corrija ahí mismo
        no → no dice nada
```

A mano:

```
python validadores/validar.py estandar
```

## Ejemplos de lo que retorna

```python
_es_interno('../base/09-git.md')
True
_es_interno('https://github.com/algo')
False
_es_interno('#seccion')
False

_comprobable('Ver la regla', '../base/09-git.md')
True
_comprobable('Ver', 'interfaz/')
True
_comprobable('<ruta legible>', 'otro.md')
False            # es un ejemplo de formato, no un enlace
_comprobable('PagoService', 'app/PagoService.php')
False            # apunta a código de un proyecto, que no vive acá

_es_transcripcion('x/historico-chat/2026-08-09-sesion.md')
True
_es_transcripcion('x/historico-chat/README.md')
False            # el índice sí se comprueba

validar_enlaces()
[Hallazgo(FALLA, 'c:\…\notas\decisiones.md', 14,
          'enlace roto: ../base/09-git-viejo.md')]

# impreso:
[FALLA] notas/decisiones.md:14 — enlace roto: ../base/09-git-viejo.md

validar_enlaces()          # cuando está todo bien
[]

validar_indices()
[Hallazgo(FALLA, 'c:\…\pendientes\README.md', 0,
          'el índice no menciona pendientes/10-ideas.md'),
 Hallazgo(AVISO, 'c:\…\notas\README.md', 0,
          'el índice menciona notas/borrada.md, que ya no existe')]

# impreso:
[FALLA] pendientes/README.md — el índice no menciona pendientes/10-ideas.md
[AVISO] notas/README.md — el índice menciona notas/borrada.md, que ya no existe
```
