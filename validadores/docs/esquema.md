# `esquema.py`

Revisa los archivos que cambian la base de datos y busca tres descuidos que dejan datos rotos.

## Qué hace

Los datos de un sistema viven en **tablas**, que son como cuadros con filas y columnas. Cuando hay que cambiar la forma de esas tablas —agregar una columna, crear una tabla nueva— no se hace a mano: se escribe un archivo con el cambio, para que se aplique igual en todas partes. Ese archivo se llama **migración**.

Tres comprobaciones sobre esos archivos:

1. **Una columna que apunta a otra tabla, sin decir qué pasa si lo apuntado se borra.** Por ejemplo, cada factura apunta a un cliente. Si alguien borra ese cliente, hay que haber dicho antes qué pasa con sus facturas: si se borran también, o si el borrado se impide. Si no se dijo, quedan facturas apuntando a nadie.
2. **Una columna nueva obligatoria y sin valor por defecto.** Si una tabla ya tiene mil filas y se le agrega una columna que no puede quedar vacía, esas mil filas quedan mal: ninguna tiene ese dato. Solo se revisa cuando la migración **cambia** una tabla que ya existe; en una tabla recién creada no hay filas que romper.
3. **Un nombre demasiado largo.** Un nombre de tabla, de columna o de índice de más de 64 caracteres: casi todas las bases de datos lo rechazan o lo cortan por la mitad.

Reconoce las dos formas más usadas de escribir una migración. Hay una tercera que no hace falta revisar en el primer punto, porque ella misma obliga a decirlo.

Todo lo que reporta es **aviso**.

## De qué depende y quién lo usa

```
esquema.py
   ├── codigo.py ······· solo linea_de()
   ├── instalar.py ····· repositorios_git()
   ├── migraciones.py ·· es_candidata()
   ├── versionado.py ··· archivos_versionados()
   └── comun.py ········ AVISO, Hallazgo y leer
```

De Python usa `os` y `re`.

Es el validador de código que más piezas de la casa necesita.

Lo usan:

```
esquema.py
   ▲
   ├── validar.py ··· cuando alguien pide revisar "esquema"
   └── pruebas.py
```

## Qué tiene adentro

### Valores fijos

Para las columnas que apuntan a otra tabla:

| Nombre | Qué reconoce |
|---|---|
| `_FK_LARAVEL` | Dónde se declara que una columna apunta a otra tabla: `foreign`, `foreignId`, `foreignIdFor` o `constrained`. |
| `_POLITICA_LARAVEL` | Que se haya dicho qué pasa al borrar lo apuntado, en cualquiera de sus formas (`onDelete`, `cascadeOnDelete`). |
| `_REFERENCES` | Lo mismo, escrito directamente en el lenguaje de la base: la palabra `REFERENCES`. |
| `_ON_DELETE_SQL` | Y su respuesta al borrado: `ON DELETE`. |

Para las columnas nuevas:

| Nombre | Qué reconoce |
|---|---|
| `_COLUMNA_LARAVEL` | Dónde se declara una columna, con sus treinta clases posibles. |
| `_D3_SEGURO` | Lo que hace que esa columna no rompa las filas que ya existen: que pueda quedar vacía, que traiga un valor por defecto, o que sea un cambio a una columna que ya estaba. |
| `_ADD_NOT_NULL_SQL` | Una columna nueva obligatoria, escrita en el lenguaje de la base. |
| `_DEFAULT_SQL` | Que esa columna traiga un valor por defecto. |

Para los nombres:

| Nombre | Qué guarda |
|---|---|
| `_LIMITE` | `64`. Hasta cuántos caracteres aguanta un nombre. |
| `_IDENTIFICADOR` | Reconoce un nombre entre comillas que pase ese límite. |

### Funciones

**`_limites_sentencia(texto, pos)`**

- **Recibe:** el texto y un punto dentro de él.
- **Hace:** busca el punto y coma de antes y el de después. Entre esos dos está una orden completa.
- **Retorna:** dónde empieza y dónde termina la orden que contiene ese punto.

Sirve para buscar la respuesta al borrado en la misma orden donde se declaró que la columna apunta a otra tabla, y para no reportar dos veces la misma orden.

**`revisar_esquema(ruta, texto)`**

- **Recibe:** dónde está el archivo y qué dice.
- **Hace:** depende de cómo termine el nombre del archivo:

  **Si es `.php`:** primero mira si la migración cambia una tabla que ya existe o crea una nueva. Después, por cada columna que apunta a otra tabla mira si en esa misma orden se dijo qué pasa al borrar; si no, avisa. Si la tabla ya existía, por cada columna nueva mira si en esa orden hay algo que la haga segura; si no, avisa. En los dos casos anota qué órdenes ya reportó, para no repetirse.

  **Si es `.sql`:** por cada `REFERENCES` mira si hay un `ON DELETE` en los 140 caracteres siguientes. Por cada columna nueva obligatoria mira si en la misma orden hay un valor por defecto.

  **En cualquiera de los dos:** busca nombres que pasen del límite de caracteres.

- **Retorna:** una lista de pares «número de línea, qué pasa ahí».

No toca el disco ni git, así que se puede probar sin tener un proyecto de verdad.

**`validar(raiz)`**

- **Recibe:** la carpeta del proyecto.
- **Hace:**
  1. Busca los repositorios. Si no hay ninguno, retorna un aviso diciéndolo.
  2. Por cada repositorio recorre los archivos que git guarda y se queda con los que `migraciones.es_candidata` reconoce como migración y además terminan en `.php` o `.sql`.
  3. Lee cada uno y se lo pasa a `revisar_esquema`.
- **Retorna:** la lista de hallazgos.

## Cómo se ejecuta

```
python validadores/validar.py esquema --raiz "C:/ruta/proyecto"
```

Por dentro:

```
validar(carpeta)
   ↓
instalar.repositorios_git() + versionado.archivos_versionados()
   ↓
migraciones.es_candidata(ruta)  y  ¿es .php o .sql?
   ↓
revisar_esquema(ruta, texto)
   ↓
   .php:
      ¿la migración cambia una tabla que ya existe?
      por cada columna que apunta a otra tabla:
           ¿se dijo qué pasa al borrar?      → si no, AVISO
      si la tabla ya existía, por cada columna nueva:
           ¿puede quedar vacía o trae valor? → si no, AVISO
   ↓
   .sql:
      REFERENCES sin ON DELETE cerca         → AVISO
      columna nueva obligatoria sin DEFAULT  → AVISO
   ↓
   en los dos:
      nombre entre comillas de más de 64     → AVISO
```

## Ejemplos de lo que retorna

```python
_limites_sentencia('$t->foreignId("cliente_id")->constrained();  $t->string("x");', 20)
(0, 43)          # desde el comienzo hasta el punto y coma que la cierra

revisar_esquema('database/migrations/2026_08_09_crea_pagos.php',
                '$table->foreignId("cliente_id")->constrained();')
[(1, 'clave foránea sin política de borrado explícita (D1: FK con `onDelete`)')]
#  └─ línea

revisar_esquema('…/crea_pagos.php',
                '$table->foreignId("cliente_id")->constrained()->onDelete("cascade");')
[]               # tiene la política: así debe ser

revisar_esquema('…/agrega_estado.php',
                'Schema::table("pagos", function ($t) {\n'
                '    $t->string("estado");\n});')
[(2, 'columna nueva obligatoria sin `default` en un ALTER (D3: rompe las filas
      existentes)')]

revisar_esquema('…/agrega_estado.php',
                'Schema::table("pagos", function ($t) {\n'
                '    $t->string("estado")->default("pendiente");\n});')
[]

revisar_esquema('…/crea_pagos.php',
                'Schema::create("pagos", function ($t) {\n'
                '    $t->string("estado");\n});')
[]               # es una tabla nueva: no hay filas que romper

revisar_esquema('db/esquema.sql',
                'FOREIGN KEY (cliente_id) REFERENCES clientes(id)')
[(1, '`REFERENCES` sin `ON DELETE` (D1: FK con política de borrado)')]

revisar_esquema('db/cambios.sql', 'ALTER TABLE pagos ADD estado VARCHAR(20) NOT NULL;')
[(1, '`ADD ... NOT NULL` sin `DEFAULT` (D3: rompe las filas existentes)')]

revisar_esquema('…/crea_x.php', '$t->index("idx_pagos_cliente_fecha_estado_…_muy_largo");')
[(1, 'identificador de 71 caracteres, sobre el límite habitual de 64 (EST2: longitud)')]

validar('C:/proyectos/pos')
[Hallazgo(AVISO, 'database/migrations/2026_08_01_crea_pagos.php', 14,
          'clave foránea sin política de borrado explícita (D1: FK con `onDelete`)'),
 Hallazgo(AVISO, 'database/migrations/2026_08_05_agrega_estado.php', 11,
          'columna nueva obligatoria sin `default` en un ALTER (D3: rompe las
           filas existentes)')]

validar('C:/carpeta-sin-git')
[Hallazgo(AVISO, 'C:/carpeta-sin-git', 0, 'no hay repositorios git que revisar')]
```
