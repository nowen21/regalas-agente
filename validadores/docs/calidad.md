# `calidad.py`

Marca las funciones que pasan de sesenta líneas.

## Qué hace

Una **función** es un pedazo de código con nombre, que hace un trabajo y se puede llamar desde otros lados. La regla dice que cada una debe hacer **una sola cosa**. Eso un programa no lo puede juzgar, pero el **largo** sí se puede medir, y una función muy larga casi siempre está haciendo varias.

Este archivo cuenta las líneas de cada una y señala las que pasan de sesenta. No dice que estén mal: dice que vale la pena mirarlas. Por eso todo lo que reporta es **aviso**.

Reconoce dos formas de escribir una función:

- Las que llevan la palabra `function` y encierran su contenido entre llaves.
- Las que empiezan con `def`, en Python.

Los lenguajes que no usan ninguna de esas dos palabras, como Java o C#, quedan fuera.

## De qué depende y quién lo usa

```
calidad.py
   ├── codigo.py ··· archivos() y linea_de()
   └── comun.py ···· AVISO y Hallazgo
```

De Python usa `re`.

Lo usan:

```
calidad.py
   ▲
   ├── validar.py ··· cuando alguien pide revisar "calidad"
   └── pruebas.py
```

## Qué tiene adentro

### Valores fijos

| Nombre | Qué guarda |
|---|---|
| `TOPE` | `60`. Cuántas líneas puede tener una función antes de que se la señale. |
| `_FUNC_LLAVES` | Reconoce dónde empieza una función escrita con la palabra `function`: su nombre, sus paréntesis y la llave que abre. |
| `_DEF_PYTHON` | Reconoce dónde empieza una función de Python, anotando cuánto se corrió hacia la derecha. |

### Funciones

**`_cuerpo_llaves(texto, abre)`**

- **Recibe:** el texto y dónde está la llave que abre.
- **Hace:** avanza contando llaves hasta dar con la que cierra esa misma. Si contara solo la primera que aparece, se cortaría en cualquier llave de más adentro.
- **Retorna:** todo el contenido, con las llaves incluidas. Si no encuentra el cierre, retorna el resto del archivo.

**`_largo_cuerpo_python(lineas, desde, sangria)`**

- **Recibe:** las líneas del archivo, desde cuál mirar y cuánto se corrió a la derecha la función.
- **Hace:** cuenta las líneas siguientes que estén más a la derecha, sin contar las vacías.
- **Retorna:** cuántas líneas tiene la función.

**`revisar_texto(texto, donde="", hallazgos=None)`**

- **Recibe:** el contenido de un archivo, cómo nombrarlo al reportar y, si se quiere, una lista donde ir juntando lo encontrado.
- **Hace:**
  1. Por cada función con llaves busca la llave que abre, saca el contenido y cuenta sus líneas, restando la del cierre. Si pasa de sesenta, anota un aviso.
  2. Por cada función de Python cuenta las líneas por lo corrido que estén a la derecha. Si pasa de sesenta, anota un aviso.
- **Retorna:** la lista de hallazgos.

**`validar(raiz)`**

- **Recibe:** la carpeta del proyecto.
- **Hace:** le pide a `codigo.archivos` los archivos de código que git guarda, y pasa cada uno por `revisar_texto`.
- **Retorna:** la lista de hallazgos.

## Cómo se ejecuta

```
python validadores/validar.py calidad --raiz "C:/ruta/proyecto"
```

Por dentro:

```
validar(carpeta)
   ↓
codigo.archivos(carpeta)
   ↓
revisar_texto(texto, ruta)
   ↓
   por cada "function ... {":
        _cuerpo_llaves()  → todo el contenido
        cuenta las líneas
        ¿pasa de 60?  → AVISO en la línea donde empieza
   ↓
   por cada "def ...:":
        _largo_cuerpo_python()  → cuenta lo corrido a la derecha
        ¿pasa de 60?  → AVISO en la línea donde empieza
```

## Ejemplos de lo que retorna

```python
TOPE
60

_cuerpo_llaves('function f() { uno(); dos(); }', 13)
'{ uno(); dos(); }'

_largo_cuerpo_python(['def f():', '    uno()', '', '    dos()', 'otra()'], 1, 0)
2                # las dos líneas con contenido; la vacía no cuenta

revisar_texto('function corta() {\n    return 1;\n}\n', 'app/Util.php')
[]               # 1 línea de cuerpo: muy por debajo del tope

revisar_texto(codigo_con_una_funcion_de_140_lineas, 'app/Servicios/Cierre.php')
[Hallazgo(AVISO, 'app/Servicios/Cierre.php', 22,
          'función de ~140 líneas (tope 60) — Q3: una función, una cosa')]
#                'app/Servicios/Cierre.php', 22  ← la línea donde se declara

revisar_texto(codigo_python_con_un_def_de_75_lineas, 'app/informes.py')
[Hallazgo(AVISO, 'app/informes.py', 9,
          'función de ~75 líneas (tope 60) — Q3: una función, una cosa')]

validar('C:/proyectos/pos')
[Hallazgo(AVISO, 'app/Servicios/Cierre.php', 22,
          'función de ~140 líneas (tope 60) — Q3: una función, una cosa'),
 Hallazgo(AVISO, 'app/Http/Controllers/PagoController.php', 88,
          'función de ~72 líneas (tope 60) — Q3: una función, una cosa')]
```
