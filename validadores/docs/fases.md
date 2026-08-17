# `fases.py`

Revisa que las carpetas donde se planea el trabajo estén bien nombradas, en el sitio que les toca y con sus documentos adentro.

## Qué hace

El trabajo se planea por escrito antes de programarlo, y se guarda en carpetas de tres niveles, uno dentro de otro:

- **Épica** — un bloque grande de trabajo. Su carpeta se llama `EP-001-facturacion`.
- **Historia de usuario** — una necesidad concreta de quien va a usar el sistema. Va adentro de una épica y su carpeta se llama `HU-003-registrar`.
- **Fase** — un pedazo de esa historia, de los que se hacen uno tras otro. Va adentro de la historia y su carpeta empieza con una letra que dice el orden: `A-`, `B-`, `C-`.

Este archivo recorre `documentacion/epicas/` y comprueba:

- Que el nombre de cada carpeta esté escrito como corresponde.
- Que una fase diga que pertenece a la misma épica e historia en cuyas carpetas está guardada.
- Que dos fases de la misma historia no se llamen con la misma letra.
- Que las letras vayan A, B, C… sin saltarse ninguna.
- Que cada fase tenga sus cuatro documentos.
- Que cada épica y cada historia tengan el suyo.

Sobre el nombre exige el guion —`EP-001`, `HU-003`— porque así lo dice la regla, pero **no** exige que el número tenga siempre la misma cantidad de cifras: la regla nunca lo dijo, y los proyectos escriben tanto `HU-01` como `HU-013`.

## De qué depende y quién lo usa

```
fases.py
   └── comun.py ··· AVISO, FALLA y Hallazgo
```

De Python usa `os` y `re`.

Lo usan:

```
fases.py
   ▲
   ├── flujo.py ········· le pide _subcarpetas para recorrer las carpetas
   ├── trazabilidad.py ·· le pide _EPICA, _HU, _FASE, _numero y _subcarpetas
   ├── validar.py ······· cuando alguien pide revisar "fases"
   └── pruebas.py
```

Acá está escrito cómo se leen estas carpetas. Los otros dos validadores que las recorren se apoyan en este para no repetir lo mismo tres veces.

## Qué tiene adentro

### Valores fijos

| Nombre | Qué guarda |
|---|---|
| `CARPETA` | `documentacion/epicas`, donde empieza todo. |
| `DOCUMENTOS` | Los cuatro documentos que lleva cada fase: `plan_trabajo.md`, `plan_pruebas.md`, `funcionalidad_implementada.md` y `estado-fase.md`. |
| `_EPICA` | Reconoce el nombre de una carpeta de épica: `EP-<número>-<de qué se trata>`. |
| `_HU` | Reconoce el nombre de una carpeta de historia: `HU-<número>-<de qué se trata>`. |
| `_FASE` | Reconoce el nombre de una carpeta de fase: la letra del orden (de una a tres letras), a veces otra letra que la acompaña, y después `-EP-<número>-HU-<número>-<de qué se trata>`. |

### Funciones de apoyo

**`_numero(texto)`**

- **Recibe:** el número escrito como texto.
- **Retorna:** ese número. Así `002` y `2` cuentan como la misma épica.

**`_orden_letras(letras)`**

- **Recibe:** la letra que marca el orden de una fase.
- **Hace:** la convierte en número: A vale 1, B vale 2, hasta Z que vale 26; después AA vale 27, AB vale 28.
- **Retorna:** ese número, para poder ponerlas en orden.

**`_subcarpetas(ruta)`**

- **Recibe:** una carpeta.
- **Retorna:** la lista ordenada de sus subcarpetas. Lista vacía si la carpeta no existe.

Lo usan también `flujo.py` y `trazabilidad.py`.

### Funciones principales

**`validar(proyecto)`**

- **Recibe:** la carpeta del proyecto.
- **Hace:**
  1. Si no existe `documentacion/epicas/`, retorna una sola falla.
  2. Por cada subcarpeta comprueba que el nombre sea el de una épica. Si no lo es → **falla** y sigue con la siguiente.
  3. Comprueba que la épica tenga su documento, aceptando dos nombres: `epica.md` o el nombre de la carpeta más `.md`. Si no → **aviso**.
  4. Por cada subcarpeta de la épica comprueba que sea una historia de usuario. Si no lo es → **falla**.
  5. Comprueba que la historia tenga su documento. Si no → **aviso**.
  6. Llama a `_validar_fases` para el resto.
- **Retorna:** la lista de hallazgos.

**`_validar_fases(ruta_hu, donde_hu, num_epica, num_hu)`**

- **Recibe:** la carpeta de la historia, cómo mostrarla en los mensajes, y los números de la épica y la historia.
- **Hace:**
  1. Si la historia no tiene fases → **aviso** y termina. Es aviso y no falla porque una historia recién abierta todavía no tiene ninguna.
  2. Por cada fase comprueba cómo está escrito el nombre. Si está mal → **falla** y sigue con la siguiente.
  3. Comprueba que la épica que dice el nombre sea la carpeta donde está guardada. Si no → **falla**.
  4. Lo mismo con la historia. Si no → **falla**.
  5. Comprueba que ninguna otra fase esté usando la misma letra. Si la está usando → **falla**.
  6. Comprueba que estén los cuatro documentos. Si falta alguno → **aviso**.
  7. Al final comprueba que las letras vayan A, B, C sin saltos. Si falta una → **aviso**, porque una fase que se dejó para después deja ese hueco a propósito.
- **Retorna:** la lista de hallazgos.

## Cómo se ejecuta

```
python validadores/validar.py fases --raiz "C:/ruta/proyecto"
```

Por dentro:

```
documentacion/epicas/
   │
   ├── EP-001-facturacion/           ← ¿el nombre está escrito EP-<n>-<de qué>?
   │      ├── epica.md               ← ¿existe el documento de la épica?
   │      │
   │      └── HU-003-registrar/      ← ¿el nombre está escrito HU-<n>-<de qué>?
   │             ├── HU-003-registrar.md   ← ¿existe el documento?
   │             │
   │             ├── A-EP-001-HU-003-configuracion/
   │             │      ├── plan_trabajo.md            ← los cuatro
   │             │      ├── plan_pruebas.md               documentos
   │             │      ├── funcionalidad_implementada.md
   │             │      └── estado-fase.md
   │             │
   │             └── B-EP-001-HU-003-implementacion/
   │                    ...
   │
   │      ¿la fase dice EP-001 y HU-003, que es donde está guardada?
   │      ¿las letras A, B van sin repetirse y sin saltos?
```

## Ejemplos de lo que retorna

```python
_numero('002')
2

_orden_letras('A')      →  1
_orden_letras('C')      →  3
_orden_letras('AA')     →  27

_subcarpetas('C:/proyectos/pos/documentacion/epicas')
['EP-001-facturacion', 'EP-002-inventario']

_subcarpetas('C:/ruta/que/no/existe')
[]

validar('C:/proyectos/pos')          # todo bien
[]

validar('C:/proyectos/sin-documentacion')
[Hallazgo(FALLA, 'C:/proyectos/sin-documentacion', 0,
          'no existe `documentacion/epicas` — F12.13 la exige')]

validar('C:/proyectos/pos')          # con problemas
[Hallazgo(FALLA, 'documentacion/epicas/facturacion', 0,
          'no parece una épica: se espera `EP-<número>-<slug>` (F12.13)'),

 Hallazgo(AVISO, 'documentacion/epicas/EP-001-facturacion', 0,
          'sin documento de épica (`epica.md` o `EP-001-facturacion.md`)'),

 Hallazgo(FALLA, 'documentacion/epicas/EP-001-facturacion/notas', 0,
          'dentro de una épica solo van HU — se espera `HU-<número>-<slug>` (F12.11)'),

 Hallazgo(AVISO, 'documentacion/epicas/EP-001-facturacion/HU-003-registrar', 0,
          'sin documento `HU-003-registrar.md`'),

 Hallazgo(AVISO, 'documentacion/epicas/EP-001-facturacion/HU-004-anular', 0,
          'sin fases — F12.2 pide al menos una'),

 Hallazgo(FALLA, '…/HU-003-registrar/configuracion-inicial', 0,
          'el nombre no sigue F12.6 — se espera `<consecutivo>-EP-<número>-HU-
           <número>-<descripción>`, p. ej. `A-EP-001-HU-003-Configuración inicial`'),

 Hallazgo(FALLA, '…/HU-003-registrar/A-EP-002-HU-003-configuracion', 0,
          'declara la épica 002 pero está guardada en la 1 (F12.1)'),

 Hallazgo(FALLA, '…/HU-003-registrar/B-EP-001-HU-003-pruebas', 0,
          'el consecutivo «B» ya lo usa «B-EP-001-HU-003-implementacion» (F12.7)'),

 Hallazgo(AVISO, '…/HU-003-registrar/A-EP-001-HU-003-configuracion', 0,
          'faltan documentos de la fase (F12.13): plan_pruebas.md, estado-fase.md'),

 Hallazgo(AVISO, '…/HU-003-registrar', 0,
          'el consecutivo de fases no es A, B, C… sin huecos (F12.5): A, C')]
```

## La comprobación del veredicto — desde la v23.1.0

**`veredicto(ruta_fase, donde)`**

- **Hace:** compara lo que dicen el `resultado_pruebas.md` y el `estado-fase.md` de la misma fase, y reporta como **falla** tres cosas: que el concepto no coincida, que la fase se dé por cumplida con una exigencia en «No» en el §5 del resultado, y que los dos cuenten criterios distintos.
- **Por qué existe.** El veredicto se escribe **dos veces a mano**, y el `estado-fase` es el que se mira para pasar la puerta de verificación: si dice «cumple», la fase pasa sin que nadie abra el resultado, que es donde está la verdad. Ya pasó una vez.
- **Qué no hace:** decir si el veredicto es **cierto**. Eso no lo puede saber un programa.
- **Los dos límites.** Si falta uno de los dos documentos, calla: una fase a medio escribir no es una contradicción. Y una salvedad al lado del concepto —«Cumple, con una salvedad»— tampoco lo es: se comparan conceptos normalizados.
