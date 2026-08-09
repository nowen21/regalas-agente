# `seguridad.py`

Busca cuatro descuidos por los que alguien de afuera podría meterse: preguntas a la base de datos y órdenes al sistema armadas pegando texto, datos que entran sin control, y la sesión desprotegida.

## Qué hace

Cuatro búsquedas sobre el código del proyecto:

1. **Pregunta a la base de datos armada pegando texto.** Un texto que empieza con `SELECT`, `INSERT INTO`, `UPDATE`, `DELETE FROM` o `REPLACE INTO` y al que, en la misma línea, se le pega algo que escribió el usuario. Así, alguien puede escribir en un formulario algo que la base entiende como una orden y ejecuta.
2. **Orden al sistema armada igual.** Una llamada del estilo `exec`, `system`, `os.system` o `subprocess.run` a la que se le pega texto en la misma línea. Mismo riesgo, pero la orden se la come el computador entero.
3. **Datos que entran sin control.** Decir que ningún campo está protegido, o pasar de golpe todo lo que llegó del formulario a la base. Alguien puede mandar de más un campo que no le tocaba, como «soy administrador».
4. **Sesión desprotegida.** Apagar a propósito una de las dos protecciones de la sesión: la que impide que un código de la página lea la sesión, o la que impide que viaje sin cifrar.

Todo lo que reporta es **aviso**. Busca por parecido, y un texto de consulta con el nombre de la tabla escrito fijo no es ningún peligro.

## De qué depende y quién lo usa

```
seguridad.py
   ├── codigo.py ··· archivos() y linea_de()
   └── comun.py ···· AVISO y Hallazgo
```

De Python usa `re`.

Lo usan:

```
seguridad.py
   ▲
   ├── validar.py ··· cuando alguien pide revisar "seguridad"
   └── pruebas.py
```

## Qué tiene adentro

### Valores fijos

| Nombre | Qué reconoce |
|---|---|
| `_SQL_EN_CADENA` | Un texto que **empieza** con una de esas palabras. Que empiece, para no confundirse con la palabra «select» metida adentro de un nombre cualquiera, como `form-select`. |
| `_CONCAT_VAR` | Que a ese texto se le esté pegando algo, en las dos formas más comunes de escribirlo. |
| `_SHELL` | Una orden al sistema: `exec`, `shell_exec`, `system`, `passthru`, `popen`, `proc_open`, `os.system`, `subprocess.call`, `subprocess.run` o `subprocess.Popen`. |
| `_CONCAT_O_INTERP` | Que se le esté pegando o metiendo texto adentro. |
| `_GUARDED_VACIO` | La línea que deja todos los campos abiertos a que los llene cualquiera. |
| `_TODO_AL_MODELO` | Pasar de golpe todo lo que llegó del formulario a `create`, `update`, `fill`, `forceCreate` o `forceFill`. |
| `_COOKIE_INSEGURA` | Una de las protecciones de la sesión —`http_only`, `httponly`, `secure`, `cookie_httponly`, `cookie_secure`— puesta en falso o en cero. |

### Funciones

**`revisar_texto(texto, donde="", hallazgos=None)`**

- **Recibe:** el contenido de un archivo, cómo nombrarlo al reportar y, si se quiere, una lista donde ir juntando lo encontrado.
- **Hace:**
  1. Recorre el texto línea por línea. Si en una misma línea hay una consulta y algo que se le pega → aviso. Si hay una orden al sistema y algo que se le pega → aviso.
  2. Después busca en el texto completo las otras tres cosas: los campos abiertos, el formulario entero pasado de golpe y la sesión desprotegida. Cada una se señala en su línea con `codigo.linea_de`.
- **Retorna:** la lista de hallazgos.

Las dos primeras se miran línea por línea porque hacen falta las dos mitades juntas para que sea un problema. Las otras tres se miran en el texto completo porque pueden quedar repartidas en varias líneas.

**`validar(raiz)`**

- **Recibe:** la carpeta del proyecto.
- **Hace:** le pide a `codigo.archivos` los archivos de código que git guarda, y pasa cada uno por `revisar_texto`.
- **Retorna:** la lista de hallazgos.

## Cómo se ejecuta

```
python validadores/validar.py seguridad --raiz "C:/ruta/proyecto"
```

Por dentro:

```
validar(carpeta)
   ↓
codigo.archivos(carpeta)   ← los archivos de código que git guarda
   ↓
revisar_texto(texto, ruta)
   ↓
   línea por línea:
       "SELECT ..." junto a  . $variable     → AVISO
       exec(...)    con texto pegado         → AVISO
   ↓
   en el texto completo:
       $guarded = []                         → AVISO
       ->create($request->all())             → AVISO
       'http_only' => false                  → AVISO
```

## Ejemplos de lo que retorna

```python
revisar_texto('$sql = "SELECT * FROM pagos WHERE id = " . $id;\n', 'app/Pago.php')
[Hallazgo(AVISO, 'app/Pago.php', 1,
          'consulta SQL armada por concatenación — S3: usar parámetros/ORM')]

revisar_texto('DB::select("SELECT id FROM pagos WHERE id = ?", [$id]);\n', 'app/Pago.php')
[]               # va parametrizada: así debe ser

revisar_texto('exec("convert " . $archivo . " salida.png");\n', 'app/Img.php')
[Hallazgo(AVISO, 'app/Img.php', 1,
          'comando de shell armado con entrada — S3: separar comando y argumentos')]

revisar_texto('protected $guarded = [];\n', 'app/Models/Factura.php')
[Hallazgo(AVISO, 'app/Models/Factura.php', 1,
          'asignación masiva sin freno (`$guarded = []`) — S3')]

revisar_texto('Factura::create($request->all());\n', 'app/Http/FacturaController.php')
[Hallazgo(AVISO, 'app/Http/FacturaController.php', 1,
          'todo el payload al modelo (`->…($req->all())`) — S3: declarar asignables')]

revisar_texto("'http_only' => false,\n", 'config/session.php')
[Hallazgo(AVISO, 'config/session.php', 1,
          'flag de cookie de sesión apagado (`HttpOnly`/`Secure`) — S5')]

revisar_texto("'http_only' => true,\n", 'config/session.php')
[]

validar('C:/proyectos/pos')
[Hallazgo(AVISO, 'app/Repositorios/PagoRepo.php', 33,
          'consulta SQL armada por concatenación — S3: usar parámetros/ORM'),
 Hallazgo(AVISO, 'app/Models/Factura.php', 14,
          'asignación masiva sin freno (`$guarded = []`) — S3')]
```
