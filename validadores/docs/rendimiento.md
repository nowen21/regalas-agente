# `rendimiento.py`

Busca dos formas de pedirle a la base de datos mucho más de lo necesario, que hacen que el programa se vuelva lento.

## Qué hace

Dos búsquedas sobre el código del proyecto:

1. **`SELECT *`.** Es la forma de pedirle a la base **todas** las columnas de una tabla. Si solo se necesitan el nombre y la fecha, traer las otras treinta es tiempo y memoria tirados.
2. **Una consulta metida adentro de algo que se repite.** Un **bucle** es un pedazo de código que se repite una vez por cada elemento de una lista. Si adentro hay una consulta, con mil elementos se hacen mil consultas, una por una, en vez de una sola que las traiga todas. Con pocos datos no se nota; con muchos, el programa se arrastra.

Reconoce las dos formas de escribir un bucle: la que encierra el contenido entre llaves y la que lo marca dejándolo más adentro en la línea.

Todo lo que reporta es **aviso**: puede ser una consulta que se arma en pedazos, o un caso donde está bien así.

## De qué depende y quién lo usa

```
rendimiento.py
   ├── codigo.py ··· archivos() y linea_de()
   └── comun.py ···· AVISO y Hallazgo
```

De Python usa `re`.

Lo usan:

```
rendimiento.py
   ▲
   ├── validar.py ··· cuando alguien pide revisar "rendimiento"
   └── pruebas.py
```

## Qué tiene adentro

### Valores fijos

| Nombre | Qué reconoce |
|---|---|
| `_SELECT_ESTRELLA` | El texto `SELECT *`, esté en mayúsculas o en minúsculas. |
| `_BUCLE_LLAVES` | Dónde empieza un bucle de los que encierran su contenido entre llaves. |
| `_BUCLE_PYTHON` | Dónde empieza un bucle de Python, anotando cuánto se corrió hacia la derecha. |
| `_CONSULTA` | Una línea que de verdad **va** a la base de datos, no una que solo prepara la pregunta para después. Reconoce las formas más comunes en varios lenguajes: `get`, `first`, `find`, `count`, `paginate`, `DB::`, `.objects.`, y las genéricas `query`, `execute`, `fetchall` y `fetchone`. |

### Funciones

**`_cuerpo_llaves(texto, desde)`**

- **Recibe:** el texto y desde dónde empieza la condición del bucle.
- **Hace:** primero se salta la condición, contando paréntesis que abren y que cierran hasta emparejarlos. Después toma todo lo que va entre la llave que abre y la que cierra, contándolas igual para no cortar en una llave de más adentro.
- **Retorna:** un par «lo que hay adentro del bucle, dónde termina»; o nada, si ese bucle no usa llaves.

**`_cuerpo_python(lineas, desde, sangria)`**

- **Recibe:** las líneas del archivo, desde qué línea mirar y cuánto se corrió hacia la derecha el bucle.
- **Hace:** junta las líneas siguientes mientras estén más a la derecha que el bucle. Cuando una vuelve al margen del bucle, el bucle terminó ahí.
- **Retorna:** lo que hay adentro del bucle, como texto.

**`revisar_texto(texto, donde="", hallazgos=None)`**

- **Recibe:** el contenido de un archivo, cómo nombrarlo al reportar y, si se quiere, una lista donde ir juntando lo encontrado.
- **Hace:**
  1. Busca `SELECT *` en todo el texto y anota un aviso por cada uno.
  2. Por cada bucle con llaves saca lo que hay adentro y, si ahí hay una consulta, anota un aviso señalando la línea donde empieza el bucle.
  3. Con los bucles de Python hace lo mismo, mirando hasta dónde llega lo que está corrido a la derecha.
- **Retorna:** la lista de hallazgos.

**`validar(raiz)`**

- **Recibe:** la carpeta del proyecto.
- **Hace:** le pide a `codigo.archivos` los archivos de código que git guarda, y pasa cada uno por `revisar_texto`.
- **Retorna:** la lista de hallazgos.

## Cómo se ejecuta

```
python validadores/validar.py rendimiento --raiz "C:/ruta/proyecto"
```

Por dentro:

```
validar(carpeta)
   ↓
codigo.archivos(carpeta)
   ↓
revisar_texto(texto, ruta)
   ↓
   busca "SELECT *" en todo el texto            → AVISO por cada uno
   ↓
   por cada bucle con llaves:
        _cuerpo_llaves()  → lo que hay entre { y }
        ¿hay ->get(), ::find(), DB::table(...)? → AVISO
   ↓
   por cada bucle de Python:
        _cuerpo_python()  → las líneas corridas a la derecha
        ¿hay .objects.filter(), .execute()?     → AVISO
```

## Ejemplos de lo que retorna

```python
_cuerpo_llaves('foreach ($x as $y) { hacer($y); }', 18)
('{ hacer($y); }', 32)
#  └─ el cuerpo del bucle   └─ dónde termina

_cuerpo_llaves('for ($i=0; $i<3; $i++) hacer();', 3)
(None, 3)        # no tiene bloque con llaves

_cuerpo_python(['for f in facturas:', '    print(f)', 'otra_cosa()'], 1, 0)
'    print(f)'

revisar_texto('$sql = "SELECT * FROM pagos";\n', 'app/Pago.php')
[Hallazgo(AVISO, 'app/Pago.php', 1,
          '`SELECT *` — R2 pide traer solo las columnas necesarias')]

revisar_texto('$sql = "SELECT id, total FROM pagos";\n', 'app/Pago.php')
[]

revisar_texto('foreach ($facturas as $f) {\n    $c = Cliente::find($f->cliente_id);\n}\n',
              'app/Reporte.php')
[Hallazgo(AVISO, 'app/Reporte.php', 1,
          'consulta dentro de un bucle — R1: posible N+1 (usar eager loading)')]

revisar_texto('for f in facturas:\n    c = Cliente.objects.get(id=f.cliente_id)\n',
              'app/reporte.py')
[Hallazgo(AVISO, 'app/reporte.py', 1,
          'consulta dentro de un bucle — R1: posible N+1 (usar eager loading)')]

revisar_texto('foreach ($facturas as $f) {\n    echo $f->total;\n}\n', 'app/Reporte.php')
[]               # el bucle no consulta nada

validar('C:/proyectos/pos')
[Hallazgo(AVISO, 'app/Reportes/Ventas.php', 18,
          '`SELECT *` — R2 pide traer solo las columnas necesarias'),
 Hallazgo(AVISO, 'app/Reportes/Ventas.php', 40,
          'consulta dentro de un bucle — R1: posible N+1 (usar eager loading)')]
```
