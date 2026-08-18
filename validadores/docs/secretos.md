# `secretos.py`

Busca contraseñas y claves escritas dentro del código, donde las ve cualquiera que abra el archivo.

## Qué hace

Trabaja de a dos con `versionado.py`. Aquel mira **nombres** de archivo: que no se suba un `.env` ni una clave. Este abre los archivos y mira **lo que dicen adentro**, buscando una clave escrita a mano, como `const API_KEY = "sk_live_..."`.

Reporta de dos formas, según qué tan seguro esté:

- **Falla** cuando lo encontrado ya es la clave misma: una clave de acceso de Amazon, un bloque de clave privada, o una de esas claves con forma reconocible que entregan servicios conocidos. No hay forma de que eso esté bien puesto ahí, y borrarlo después no arregla nada: queda guardado en la historia de git para siempre.
- **Aviso** cuando hay algo que se llama como una clave y tiene un texto guardado. Puede ser un ejemplo o un dato de prueba, así que decide una persona.

Solo abre archivos de código y de ajustes que git esté guardando. Los `.md` quedan fuera: la documentación muestra claves de mentira a propósito.

## De qué depende y quién lo usa

```
secretos.py
   ├── instalar.py ····· repositorios_git()
   ├── versionado.py ··· archivos_versionados()
   └── comun.py ········ AVISO, FALLA y Hallazgo
```

De Python usa `os` y `re`.

Lo usan:

```
secretos.py
   ▲
   ├── validar.py ··· cuando alguien pide revisar "secretos"
   └── pruebas.py
```

Recorre los archivos por su cuenta y no con `codigo.py` por dos razones: necesita abrir más clases de archivo, y no quiere que se salten `public/` ni `static/` — una clave escrita ahí también es una clave escrita.

## Qué tiene adentro

### Valores fijos

| Nombre | Qué guarda |
|---|---|
| `EXTENSIONES` | Qué archivos se abren, por cómo termina su nombre. Además del código: `.yml`, `.yaml`, `.ini`, `.conf`, `.cfg`, `.toml`, `.properties`, `.sh`, `.bash`, `.ps1`, `.xml` y `.env`. |
| `SALTAR` | Lo que nunca se abre: `vendor`, `node_modules`, `dist`, `build`, `.git`, los archivos que fijan la versión de cada programa de afuera, y los que una herramienta comprimió dejándolos en una sola línea. |
| `SEGUROS` | Las ocho formas que ya son una clave, cada una con su motivo. |
| `_ASIGNA` | Reconoce algo que se llama como una clave y tiene guardado un texto de seis caracteres o más. |
| `_ENTORNO` | Reconoce que la línea, en vez de escribir la clave, la va a buscar afuera al arrancar. Eso es lo correcto. |
| `_MOLDE_EXACTO` | Reconoce un valor que claramente es de mentira: `xxxx`, `changeme`, `placeholder`, `dummy`, `sample`, `example`, `ejemplo`, `null`, `none`, `password`, `secret`, `test`, `123456`, `abc123` o algo entre `<` y `>`. |
| `_MOLDE_PREFIJO` | Reconoce un valor que empieza como los de mentira: `your-`, `tu_`, `my-`, `mi-`, `example-`, `ejemplo-`, `placeholder-`, `sample-`, `dummy-`, `test-`. |

Las ocho formas que son falla. Cada servicio le da a sus claves un comienzo propio, y por ese comienzo se reconocen:

| Cómo se reconoce | Qué es |
|---|---|
| `AKIA` y 16 caracteres más | clave de acceso de Amazon |
| `-----BEGIN ... PRIVATE KEY-----` | una clave privada escrita completa |
| `sk_live_` y 16 caracteres o más | clave de Stripe, la de cobros de verdad |
| `SG.` con dos tramos largos | clave de SendGrid, que manda los correos |
| `xoxb-`, `xoxa-`, `xoxp-`, `xoxr-`, `xoxs-` | permiso de entrada a Slack |
| `ghp_`, `gho_`, `ghu_`, `ghs_`, `ghr_` | permiso de entrada a GitHub |
| `glpat-` | permiso de entrada a GitLab |
| `AIza` y 35 caracteres más | clave de un servicio de Google |

### Funciones

**`_valor_sospechoso(valor)`**

- **Recibe:** el texto que quedó guardado.
- **Retorna:** falso si es de mentira, verdadero si podría ser una clave de verdad.

**`revisar_texto(texto, donde="", hallazgos=None)`**

- **Recibe:** el contenido de un archivo, cómo nombrarlo al reportar y, si se quiere, una lista donde ir juntando lo encontrado.
- **Hace:** recorre el texto línea por línea:
  1. Prueba las ocho formas que son falla. Si alguna aparece, anota la falla y **salta a la línea siguiente**: con un motivo por línea alcanza.
  2. Si no apareció ninguna, busca algo que se llame como una clave y tenga un texto guardado. Anota un aviso solo si ese texto no parece de mentira y la línea no va a buscar el valor afuera.
- **Retorna:** la lista de hallazgos.

No toca el disco, así que se puede probar sin necesidad de tener un proyecto de verdad.

**`validar(raiz)`**

- **Recibe:** la carpeta del proyecto.
- **Hace:**
  1. Busca los repositorios. Si no hay ninguno, retorna una falla diciéndolo.
  2. Por cada repositorio recorre los archivos que git guarda, y descarta los que caen en `SALTAR` y los que no terminan como pide la lista.
  3. Lee hasta 1 MB de cada uno, sin detenerse si aparece algún carácter raro.
  4. Se los pasa a `revisar_texto`.
- **Retorna:** la lista de hallazgos.

## Cómo se ejecuta

```
python validadores/validar.py secretos --raiz "C:/ruta/proyecto"
```

Por dentro:

```
validar(carpeta)
   ↓
instalar.repositorios_git()
   ↓
versionado.archivos_versionados()   ← git ls-files
   ↓
   se descarta lo de SALTAR y lo que no está en EXTENSIONES
   ↓
lee hasta 1 MB del archivo
   ↓
revisar_texto(texto, ruta)
   ↓
   por cada línea:
      ¿aparece alguna de las 8 formas? → FALLA, siguiente línea
      ¿hay "password = '...'"?
           ¿el valor parece de mentira?      → no se dice nada
           ¿la línea lo busca afuera?        → no se dice nada
           si no                              → AVISO
```

## Ejemplos de lo que retorna

```python
_valor_sospechoso('sk_live_<24 caracteres más>')   →  True
_valor_sospechoso('changeme')                           →  False
_valor_sospechoso('your-api-key')                       →  False
_valor_sospechoso('<TU_CLAVE_ACA>')                     →  False

revisar_texto('AWS_KEY = "AKIA<16 caracteres más>"\n', 'config/aws.py')
[Hallazgo(FALLA, 'config/aws.py', 1,
          'posible secreto en el código (clave de acceso AWS) · S4/N6')]

revisar_texto('const token = "ghp_<36 caracteres>";\n', 'src/api.js')
[Hallazgo(FALLA, 'src/api.js', 1,
          'posible secreto en el código (token de GitHub) · S4/N6')]

revisar_texto('$password = "Bogota2026*";\n', 'app/Conexion.php')
[Hallazgo(AVISO, 'app/Conexion.php', 1,
          '`password` asignada a un texto fijo — ¿debería leerse del entorno? (S4)')]

revisar_texto('$password = env("DB_PASSWORD");\n', 'app/Conexion.php')
[]               # lee del entorno: así debe ser

revisar_texto('$password = "changeme";\n', 'app/Conexion.php')
[]               # es un valor de mentira

revisar_texto('API_KEY = "AKIA<16 caracteres más>"  # y también password="x123456"\n',
              'config.py')
[Hallazgo(FALLA, 'config.py', 1,
          'posible secreto en el código (clave de acceso AWS) · S4/N6')]
# un solo hallazgo por línea: la falla gana y no se busca más ahí

validar('C:/proyectos/pos')
[Hallazgo(FALLA, 'app/Servicios/Pasarela.php', 47,
          'posible secreto en el código (clave secreta de Stripe (live)) · S4/N6'),
 Hallazgo(AVISO, 'config/database.php', 12,
          '`password` asignada a un texto fijo — ¿debería leerse del entorno? (S4)')]

validar('C:/carpeta-sin-git')
[Hallazgo(FALLA, 'C:/carpeta-sin-git', 0, 'no hay repositorios git que revisar')]
```

---

## Qué se considera clave y qué se considera ejemplo — desde la 23.2.1

> Escrito el 2026-08-17 en la fase [`A-EP-004-HU-007`](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-007-claves-y-datos-sensibles/A-EP-004-HU-007-retrodocumentar-la-comprobacion-de-secretos/resultado_pruebas.md). Estaba en dos expresiones del código y en ningún documento, así que nadie podía saber qué escribir para no disparar un falso positivo.

**Lo que se reporta como falla:** un secreto con **forma reconocible** —clave de AWS, bloque de clave privada, token de proveedor—. No hace falta que sea válido: si tiene la forma, se reporta. Un secreto de mentira con forma real bloquea el envío a GitHub igual que uno de verdad.

**Lo que se reporta como aviso:** una asignación del tipo `clave = "algo"` donde la clave se llama `password`, `secret`, `api_key`, `access_key`, `client_secret`, `auth_token` o `private_key`, y el valor tiene seis caracteres o más.

**Lo que NO se reporta, y por qué:**

| Caso | Ejemplo | Por qué no |
|---|---|---|
| **El valor entero es un molde** | `changeme` · `placeholder` · `dummy` · `sample` · `example` · `ejemplo` · `null` · `none` · `password` · `secret` · `test` · `123456` · `abc123` · `xxxx…` · `….` · `****` · `<lo que sea>` | Nadie pone eso en producción |
| **El valor empieza como molde** | `your-api-key` · `tu_clave` · `my-secret` · `mi_token` · `example-…` · `placeholder_…` · `sample …` · `dummy-…` · `test_…` | Es la forma normal de escribir un ejemplo |
| **La línea lee del entorno** | `os.environ[…]` · `getenv(…)` · `process.env…` · `config(…)` · `${…}` · una línea con `import` | Leer del entorno **es lo correcto**: marcarlo enseñaría lo contrario |
| **Los archivos `.md`** | Toda la documentación | La documentación muestra secretos de ejemplo a propósito. Reportarlos obligaría a escribir la documentación torcida |

**Cómo escribir un ejemplo que no dispare nada:** que el valor empiece por `your`, `tu`, `mi`, `example`, `ejemplo`, `placeholder`, `sample`, `dummy` o `test`, o que vaya entre `<` y `>`. Y en las pruebas, **armar el literal en tiempo de ejecución** —`"AKIA" + "…"`— en vez de escribirlo entero.

**Los tres bordes, y qué hace con cada uno:**

| Borde | Qué hace |
|---|---|
| Archivo **binario** | Lo lee con `errors="replace"`: no revienta, y lo que salga no coincide con ningún patrón |
| Archivo **enorme** | Lee **1 MB** y para. Más que eso es dato, no código |
| Archivo **sin permisos** o ilegible | Lo salta y sigue con el siguiente. La corrida no se pierde por uno |

**El hallazgo nunca reproduce el secreto.** Dice el archivo, la línea, el motivo y —en el aviso— el **nombre** de la clave, nunca su valor. Un informe que copiara el secreto sería una segunda filtración, y encima en un archivo que se versiona.
