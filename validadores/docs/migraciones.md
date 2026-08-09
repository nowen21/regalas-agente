# `migraciones.py`

Revisa que cada cambio a la base de datos venga con la forma de deshacerlo.

## Qué hace

Los datos viven en tablas, y cuando hay que cambiarles la forma no se hace a mano: se escribe un archivo con el cambio para que se aplique igual en todas partes. Ese archivo se llama **migración**.

La regla pide que cada migración traiga también el camino de vuelta. Si el cambio sale mal en producción, hay que poder dejar todo como estaba; sin ese camino escrito, hay que inventarlo con el sistema caído.

Este archivo no da por hecho ninguna herramienta. Reconoce la migración por cómo termina su nombre y por lo que dice adentro, y le pide lo que corresponde en cada caso:

| Cómo está escrita | Qué se le pide |
|---|---|
| En PHP | Si hay un `function up`, que haya un `function down`. |
| En Python, con Alembic | Si hay un `def upgrade`, que haya un `def downgrade`. |
| En Python, con Django | Cuando el cambio corre código propio o una orden escrita a mano, que traiga su contrario. El resto lo sabe deshacer Django solo. |
| En Ruby | Vale un `def change`, que se deshace solo; o un `def up` con su `def down`. |
| En JavaScript o TypeScript | Si hay un `up`, que haya un `down`. |
| En dos archivos sueltos | Un archivo `X.up.sql` tiene que tener su `X.down.sql`. |

Todo lo que reporta es **aviso**: hay cambios que no se pueden deshacer, y eso puede estar decidido a propósito y escrito en algún lado.

## De qué depende y quién lo usa

```
migraciones.py
   ├── instalar.py ····· repositorios_git()
   ├── versionado.py ··· archivos_versionados()
   └── comun.py ········ AVISO, Hallazgo y leer
```

De Python usa `os` y `re`.

Lo usan:

```
migraciones.py
   ▲
   ├── esquema.py ··· le pide es_candidata() para saber qué archivos revisar
   ├── validar.py ··· cuando alguien pide revisar "migraciones"
   └── pruebas.py
```

## Qué tiene adentro

### Valores fijos

| Nombre | Qué guarda |
|---|---|
| `_CARPETAS` | En qué carpetas se guardan las migraciones, use lo que use el proyecto: `migrations`, `migrate` y `versions`. |
| `_EXTENSIONES` | Cómo puede terminar el nombre de una migración: `.php`, `.py`, `.rb`, `.js`, `.ts`, `.mjs`, `.cjs` y `.sql`. |
| `_SALTAR` | Descarta lo que está en `vendor/` o `node_modules/`, que es código que vino de afuera. |

### Funciones

**`es_candidata(ruta)`**

- **Recibe:** dónde está un archivo que git guarda.
- **Hace:** decide si parece una migración. Vale por dos motivos: porque el nombre termina en `.up.sql` o `.down.sql`, o porque está en una de las carpetas conocidas y termina como pide la lista.
- **Retorna:** verdadero o falso.

La usa también `esquema.py`, para no revisar archivos que no son migraciones.

**`revisar_migracion(ruta, texto, hermanos=())`**

- **Recibe:** dónde está el archivo, qué dice, y los nombres de los archivos que lo acompañan en la misma carpeta.
- **Hace:** según cómo termine el nombre y qué diga adentro, pide lo que corresponde:
  - Si el nombre termina en `.up.sql`, busca su pareja `.down.sql` entre los que lo acompañan.
  - Si termina en `.down.sql`, no dice nada: de esa pareja se encarga el otro archivo.
  - Si es `.py`, primero mira si está escrita con Django; si no, si está escrita con Alembic.
  - Si es `.rb`, acepta `def change`; si no, pide que el `def up` tenga su `def down`.
  - Si es `.php`, pide que el `function up` tenga su `function down`.
  - Si es de JavaScript o TypeScript, pide que el `up` tenga su `down`.
- **Retorna:** por qué falta el camino de vuelta, o nada si está bien.

No toca el disco ni git, así que se puede probar sin tener un proyecto de verdad.

**`validar(raiz)`**

- **Recibe:** la carpeta del proyecto.
- **Hace:**
  1. Busca los repositorios. Si no hay ninguno, retorna un aviso diciéndolo.
  2. Por cada repositorio se queda con los archivos que git guarda y parecen migraciones.
  3. Los junta por carpeta, para poder buscar las parejas de archivos sueltos.
  4. Lee cada uno y se lo pasa a `revisar_migracion`.
- **Retorna:** la lista de hallazgos.

## Cómo se ejecuta

```
python validadores/validar.py migraciones --raiz "C:/ruta/proyecto"
```

Por dentro:

```
validar(carpeta)
   ↓
instalar.repositorios_git()
   ↓
versionado.archivos_versionados()
   ↓
es_candidata(ruta)   ← ¿está en migrations/, migrate/ o versions/?
   ↓                   ¿o el nombre termina en .up.sql / .down.sql?
   junta los nombres por carpeta (para encontrar las parejas)
   ↓
revisar_migracion(ruta, texto, los_que_acompañan)
   ↓
   .php → ¿function up sin su function down?       → AVISO
   .py  → ¿corre código propio sin su contrario?   → AVISO
          ¿upgrade sin su downgrade?               → AVISO
   .rb  → ¿up sin down y sin change?               → AVISO
   .js  → ¿up sin down?                            → AVISO
   .sql → ¿falta el archivo .down.sql?             → AVISO
```

## Ejemplos de lo que retorna

```python
es_candidata('database/migrations/2026_08_09_crea_pagos.php')   →  True
es_candidata('db/migrate/20260809_add_estado.rb')               →  True
es_candidata('alembic/versions/a3f9_crea_pagos.py')             →  True
es_candidata('db/0001_crea_pagos.up.sql')                       →  True
es_candidata('app/Models/Factura.php')                          →  False
es_candidata('vendor/paquete/migrations/x.php')                 →  False

revisar_migracion('…/crea_pagos.php', 'public function up() { … }')
'`up` sin `down` (D2)'

revisar_migracion('…/crea_pagos.php',
                  'public function up() { … }  public function down() { … }')
None             # tiene el camino de vuelta

revisar_migracion('alembic/versions/a3f9.py', 'def upgrade(): …')
'Alembic: `upgrade` sin `downgrade` (D2)'

revisar_migracion('migrations/0002_datos.py',
                  'from django.db import migrations\n'
                  'operations = [migrations.RunPython(cargar)]')
'migración Django no reversible: RunPython sin reverse_code (D2)'

revisar_migracion('migrations/0003_campo.py',
                  'from django.db import migrations\n'
                  'operations = [migrations.AddField(…)]')
None             # Django revierte solo este tipo de cambio

revisar_migracion('db/migrate/20260809_x.rb', 'def change\n  …\nend')
None             # `change` se revierte solo

revisar_migracion('db/migrate/20260809_x.rb', 'def up\n  …\nend')
'Rails: `up` sin `down` ni `change` (D2)'

revisar_migracion('migrations/001_crea.js', 'exports.up = function (knex) { … }')
'`up` sin `down` (D2)'

revisar_migracion('db/0001_crea.up.sql', 'CREATE TABLE pagos (…);',
                  hermanos={'0001_crea.up.sql'})
'falta el archivo de reversión `0001_crea.down.sql` (D2)'

revisar_migracion('db/0001_crea.up.sql', 'CREATE TABLE pagos (…);',
                  hermanos={'0001_crea.up.sql', '0001_crea.down.sql'})
None

revisar_migracion('db/0001_crea.down.sql', 'DROP TABLE pagos;')
None             # la pareja la evalúa el archivo .up.sql

validar('C:/proyectos/pos')
[Hallazgo(AVISO, 'database/migrations/2026_08_01_crea_pagos.php', 0,
          '`up` sin `down` (D2)'),
 Hallazgo(AVISO, 'db/0004_indices.up.sql', 0,
          'falta el archivo de reversión `0004_indices.down.sql` (D2)')]
```
