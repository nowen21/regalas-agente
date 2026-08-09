# `plantillas.py`

Compara un documento con el molde del que salió y marca lo que quedó sin llenar.

## Qué hace

Los documentos de trabajo no se escriben desde cero: se copian de un molde que está en la carpeta `plantillas/`. Este archivo comprueba que la copia se haya llenado de verdad y no haya quedado a medias.

El molde es la única referencia: **acá no hay ninguna regla escrita**. El validador abre el molde, mira qué partes y qué huecos tiene, y compara. Si el molde cambia, la comprobación cambia con él sin que nadie toque el código.

Tres comprobaciones:

1. **Huecos sin llenar** — falla. Hay líneas que quedaron iguales a las del molde.
2. **Instrucciones sin borrar** — aviso. Las líneas que empiezan con `>` explican cómo llenar el documento y deberían desaparecer al llenarlo.
3. **Partes que no están** — aviso. Los moldes dicen que se pueden borrar las partes que no apliquen, así que faltar no es lo mismo que estar mal.

Además sabe averiguar solo de qué molde salió cada documento.

## De qué depende y quién lo usa

```
plantillas.py
   └── comun.py ··· AVISO, FALLA, Hallazgo, RAIZ, encabezados,
                    leer, lineas_utiles y marcadores
```

De Python usa `os` y `re`.

Lo usan:

```
plantillas.py
   ▲
   ├── validar.py ··· cuando alguien pide revisar "plantilla"
   └── pruebas.py
```

## Qué tiene adentro

### Valores fijos

| Nombre | Qué guarda |
|---|---|
| `POR_PREFIJO` | Cómo averiguar el molde por cómo empieza el título: `HU-` es una historia de usuario y sale de `plantillas/HU.md`; `EP-` es una épica, que agrupa varias historias; `ADR-` es una decisión de arquitectura escrita para que después se sepa por qué se eligió eso. |
| `POR_NOMBRE` | Cómo averiguarlo por el nombre del archivo, cuando el título no lo dice. Cubre `brief`, `dominio`, `stack`, `fase`, `plan_trabajo`, `plan_pruebas`, `funcionalidad_implementada`, `estado-fase` y once más. |
| `_H1` | Reconoce el título principal del documento. |
| `_MARCADOR_EN_TITULO` | Reconoce un hueco metido dentro de un título. |

### Funciones

**`_ruta(relativa)`**

- **Recibe:** una dirección escrita con barras `/`.
- **Retorna:** la dirección completa dentro del estándar, con la barra que use este sistema: Windows las escribe al revés que los demás.

**`deducir_plantilla(ruta_documento, texto)`**

- **Recibe:** dónde está el documento y qué dice.
- **Hace:**
  1. Busca el título principal y mira si empieza por alguno de los comienzos conocidos.
  2. Si no, busca el nombre del archivo en la tabla de nombres.
- **Retorna:** dónde está el molde, o nada si no se pudo averiguar.

**`_notas(texto)`**

- **Recibe:** el contenido de un documento.
- **Hace:** busca las líneas que empiezan con `>`, saltando los bloques de código.
- **Retorna:** una lista de pares «número de línea, texto de la línea».

**`validar(ruta_documento, ruta_plantilla)`**

- **Recibe:** la ruta del documento y la de su plantilla.
- **Hace:** las tres comprobaciones.

  **Huecos sin llenar:** junta todas las líneas del molde, busca en el documento las líneas que tienen un hueco y mira si la línea entera es igualita a una del molde. Se compara la línea entera y no el hueco solo, porque hay etiquetas que el documento conserva a propósito: el molde trae `- [ ] [Backend] …` y el documento escribe `- [ ] **T1** · [Backend] Interpretación del Markdown`. Ahí la tarea está llena y `[Backend]` es una etiqueta, no un hueco.

  **Instrucciones sin borrar:** compara las líneas que empiezan con `>` del documento contra las del molde, y avisa por cada una que siga igual.

  **Partes que no están:** compara los títulos del molde contra los del documento. Salta los títulos que llevan un hueco adentro, porque son ejemplos cuyo nombre cambia en cada documento.

- **Retorna:** la lista de hallazgos.

## Cómo se ejecuta

```
python validadores/validar.py plantilla proyectos/pos/HU-014.md
python validadores/validar.py plantilla doc.md --contra plantillas/epica.md
```

Por dentro:

```
validar.py cmd_plantilla
   ↓
   ¿existe el documento?
        no → se detiene
   ↓
   ¿dijeron con --contra cuál es el molde?
        no → deducir_plantilla(ruta, texto)
                mira el título principal → HU-014 → plantillas/HU.md
                si no, busca por el nombre del archivo
   ↓
plantillas.validar(documento, molde)
   ↓
   1. líneas iguales a las del molde y con un hueco adentro → FALLA
   2. instrucciones sin borrar                              → AVISO
   3. partes del molde que no están                         → AVISO
   ↓
comun.reportar(hallazgos)
```

## Ejemplos de lo que retorna

```python
_ruta('plantillas/HU.md')
'c:\Ing. Jose\ia\agente\plantillas\HU.md'

deducir_plantilla('proyectos/pos/HU-014.md', '# HU-014 — Registrar cliente\n')
'c:\…\agente\plantillas\HU.md'          # lo dedujo del título

deducir_plantilla('…/A-EP-001-HU-003-x/plan_trabajo.md', '# Plan de trabajo\n')
'c:\…\agente\plantillas\planes\trabajo.md'    # lo dedujo del nombre

deducir_plantilla('notas/cualquier-cosa.md', '# Apuntes sueltos\n')
None             # no se sabe de qué molde salió

_notas('> Escriba acá el nombre.\ntexto normal\n> Borre esta línea.\n')
[(1, '> Escriba acá el nombre.'), (3, '> Borre esta línea.')]

validar('proyectos/pos/HU-014.md', 'plantillas/HU.md')
[Hallazgo(FALLA, 'proyectos/pos/HU-014.md', 9,
          'línea sin llenar, igual que en la plantilla: - [ ] [Criterio de
           aceptación]'),
 Hallazgo(AVISO, 'proyectos/pos/HU-014.md', 4,
          'nota de la plantilla sin borrar: > Escriba acá qué necesita el
           usuario y por qué...'),
 Hallazgo(AVISO, 'proyectos/pos/HU-014.md', 0,
          'sección de la plantilla ausente: «Criterios de aceptación» —
           confirma que no aplica')]

# impreso:
[FALLA] proyectos/pos/HU-014.md:9 — línea sin llenar, igual que en la plantilla: …
[AVISO] proyectos/pos/HU-014.md:4 — nota de la plantilla sin borrar: …
[AVISO] proyectos/pos/HU-014.md — sección de la plantilla ausente: «Criterios…»

validar('proyectos/pos/HU-015.md', 'plantillas/HU.md')
[]               # el documento está bien llenado
```
