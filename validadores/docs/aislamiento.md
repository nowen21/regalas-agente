# `aislamiento.py`

Revisa que las pruebas del proyecto usen datos de mentira y que den siempre el mismo resultado.

## Qué hace

Una **prueba** es un programa chico que corre el sistema y comprueba que haga lo que debe. Se corren todas juntas, muchas veces al día. Para que sirvan, tienen que cumplir dos condiciones, y las dos se revisan acá.

1. **No tocan los datos de verdad.** Las pruebas escriben y borran a lo bruto, así que tienen que trabajar sobre una base de datos de mentira, que se crea al empezar y se tira al terminar. Se mira el archivo de ajustes de las pruebas: si apunta a una base en la memoria, o a una que tiene «test» en el nombre, está bien; si apunta a otra cosa, se avisa. Si no dice nada pero al lado hay un archivo de ajustes solo para pruebas, tampoco se avisa: el dato está ahí.
2. **Dan siempre el mismo resultado.** Dos cosas. Que las pruebas se corran en orden distinto cada vez, para que ninguna quede dependiendo de otra que corrió antes y le dejó algo servido. Y que no usen el azar ni la hora del reloj: una prueba que a veces pasa y a veces no, no dice nada, y con el tiempo la gente la ignora.

Hay herramientas que ya crean solas la base de mentira; en esos proyectos no hay nada que revisar en el primer punto.

Todo lo que reporta es **aviso**.

## De qué depende y quién lo usa

```
aislamiento.py
   ├── codigo.py ······· archivos(), para buscar en los tests
   ├── instalar.py ····· repositorios_git()
   ├── versionado.py ··· archivos_versionados()
   └── comun.py ········ AVISO, Hallazgo y leer
```

De Python usa `os` y `re`.

Lo usan:

```
aislamiento.py
   ▲
   ├── validar.py ··· cuando alguien pide revisar "aislamiento"
   └── pruebas.py
```

## Qué tiene adentro

### Valores fijos

| Nombre | Qué reconoce |
|---|---|
| `_ENV` | Un dato de ajuste escrito adentro del archivo de las pruebas, con su nombre y su valor. |
| `_EXEC_ORDER` | La opción que dice en qué orden se corren las pruebas. |
| `_ES_TEST` | Que un archivo sea de prueba: está en una carpeta `test`, `tests` o `spec`; o su nombre termina en `Test` o `Spec`; o empieza con `test_`. |
| `_FLAKY` | Algo que cambia de una vez a otra: el azar (`mt_rand`, `rand`, `array_rand`, `shuffle`) o la hora exacta (`microtime`). |

`uniqid` queda fuera a propósito: se usa para que cada dato inventado tenga un nombre distinto, y la prueba sigue dando siempre el mismo resultado.

### Funciones

**`revisar_phpunit(texto, hay_env_testing=False)`**

- **Recibe:** el contenido del archivo de ajustes de las pruebas y si al lado hay un archivo de ajustes solo para pruebas.
- **Hace:** busca el dato que dice a qué base de datos apuntan.
  - Si apunta a la memoria, o el nombre lleva «test», está bien.
  - Si apunta a otra cosa, dice por qué está mal.
  - Si no lo dice, pero hay un archivo de ajustes solo para pruebas, está bien.
  - Si no lo dice y tampoco hay ese archivo, dice por qué está mal.
- **Retorna:** el motivo, o nada si está bien.

**`revisar_orden(texto)`**

- **Recibe:** el contenido del archivo de ajustes de las pruebas.
- **Hace:** busca la opción del orden y mira si dice que sea al azar.
- **Retorna:** el motivo si no lo dice, o nada.

**`revisar_test(texto)`**

- **Recibe:** el contenido de un archivo de prueba.
- **Hace:** lo recorre línea por línea buscando el azar y la hora del reloj.
- **Retorna:** una lista de pares «número de línea, qué se encontró ahí».

Las tres funcionan sobre texto suelto: se pueden probar sin tener un proyecto de verdad.

**`validar(raiz)`**

- **Recibe:** la carpeta del proyecto.
- **Hace:**
  1. Busca los repositorios. Si no hay ninguno, retorna un aviso diciéndolo.
  2. Por cada repositorio busca, entre los archivos que git guarda, los de ajustes de pruebas. Por cada uno mira si en su carpeta hay ajustes solo para pruebas, lo lee y se lo pasa a las dos primeras funciones.
  3. Después le pide a `codigo.archivos` los archivos de código, se queda con los que son de prueba y se los pasa a la tercera.
- **Retorna:** la lista de hallazgos.

## Cómo se ejecuta

```
python validadores/validar.py aislamiento --raiz "C:/ruta/proyecto"
```

Por dentro:

```
validar(carpeta)
   ↓
instalar.repositorios_git() + versionado.archivos_versionados()
   ↓
   por cada archivo de ajustes de pruebas que git guarda:
        ¿hay ajustes solo para pruebas en su carpeta?
        ↓
        revisar_phpunit(texto, hay_ajustes)
             base en la memoria          → bien
             base con "test" en el nombre → bien
             base de produccion          → AVISO
             no lo dice y no hay ajustes → AVISO
        ↓
        revisar_orden(texto)
             el orden es al azar         → bien
             cualquier otra cosa         → AVISO
   ↓
codigo.archivos(carpeta)
   ↓
   por cada archivo que sea de prueba:
        revisar_test(texto)
             rand(), microtime(), shuffle()  → AVISO por cada uno
```

## Ejemplos de lo que retorna

```python
revisar_phpunit('<env name="DB_DATABASE" value=":memory:"/>')
None             # está aislada: así debe ser

revisar_phpunit('<env name="DB_DATABASE" value="pos_test"/>')
None             # tiene "test" en el nombre: también vale

revisar_phpunit('<env name="DB_DATABASE" value="pos_produccion"/>')
'las pruebas apuntan a `DB_DATABASE=pos_produccion`, que no parece efímera ni
 dedicada (T4: usar `:memory:` o una BD de test)'

revisar_phpunit('<phpunit></phpunit>')
'`phpunit.xml` no fija una BD de pruebas aislada; podría usar la real
 (T4: fijar `DB_DATABASE=:memory:` o un `.env.testing`)'

revisar_phpunit('<phpunit></phpunit>', hay_env_testing=True)
None             # el aislamiento va en el .env.testing

revisar_orden('<phpunit executionOrder="random">')
None

revisar_orden('<phpunit>')
'la suite no se corre en orden aleatorio (T3: `executionOrder="random"` para
 que no dependan del orden)'

revisar_test('$id = mt_rand(1, 100);\n$this->assertTrue($ok);\n')
[(1, 'mt_rand')]
#  └─ línea  └─ qué se encontró

revisar_test('$fecha = microtime(true);\nshuffle($items);\n')
[(1, 'microtime'), (2, 'shuffle')]

revisar_test('$id = 42;\n$this->assertEquals(42, $pago->id);\n')
[]               # da el mismo resultado siempre

validar('C:/proyectos/pos')
[Hallazgo(AVISO, 'phpunit.xml', 0,
          'las pruebas apuntan a `DB_DATABASE=pos_produccion`, que no parece
           efímera ni dedicada (T4: usar `:memory:` o una BD de test)'),
 Hallazgo(AVISO, 'phpunit.xml', 0,
          'la suite no se corre en orden aleatorio (T3: `executionOrder="random"`…)'),
 Hallazgo(AVISO, 'tests/Feature/PagoTest.php', 31,
          'fuente de azar/tiempo (`mt_rand`) en una prueba — T3: fijar
           semilla/reloj o usar dobles (evita tests flaky)')]
```
