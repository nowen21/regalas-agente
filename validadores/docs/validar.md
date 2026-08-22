# `validar.py`

Es la puerta de entrada: junta los veinticuatro validadores detrás de una sola orden que se escribe en la consola.

## Qué hace

No revisa nada por su cuenta. Su trabajo es:

1. Leer lo que se escribió en la consola.
2. Llamar al validador que toque.
3. Pasarle el resultado a `comun.reportar`, que lo muestra en pantalla y decide cómo termina el programa.

La orden se escribe en dos partes: primero el archivo y después qué se quiere revisar —`validar.py secretos`, `validar.py fases`—. A esa segunda palabra se le dice **subcomando**, y hay uno por cada validador.

Cuando el programa termina, deja un número que dice cómo le fue: `0` si no hubo ninguna falla y `1` si hubo al menos una. Otro programa puede mirar ese número y decidir si sigue o se detiene. Los avisos no lo cambian.

## De qué depende y quién lo usa

Trae veinticuatro validadores y `comun.py`:

```
validar.py
   ├── comun.py ········· RAIZ, leer, preparar_salida, relativo, reportar
   │
   ├── enlaces.py ······· subcomando estandar
   ├── citas.py ········· subcomando estandar
   ├── plantillas.py ···· subcomando plantilla
   ├── commits.py ······· subcomando commit
   ├── fases.py ········· subcomando fases
   ├── trazabilidad.py ·· subcomando trazabilidad
   ├── flujo.py ········· subcomando flujo
   ├── versionado.py ···· subcomando versionado
   ├── secretos.py ······ subcomando secretos
   ├── dependencias.py ·· subcomando dependencias
   ├── rama.py ·········· subcomando rama
   ├── migraciones.py ··· subcomando migraciones
   ├── esquema.py ······· subcomando esquema
   ├── errores.py ······· subcomando errores
   ├── rendimiento.py ··· subcomando rendimiento
   ├── seguridad.py ····· subcomando seguridad
   ├── calidad.py ······· subcomando calidad
   ├── aislamiento.py ··· subcomando aislamiento
   ├── ci.py ············ subcomando ci
   ├── herramientas.py ·· subcomandos linter, suite y audit
   ├── version.py ······· subcomando version
   ├── checklist.py ····· subcomando checklist
   ├── versiones.py ····· subcomando versiones
   ├── expediente.py ···· subcomando expediente
   └── instalar.py ······ repositorios_git(), para el subcomando versionado
```

De Python usa `argparse`, `os` y `sys`.

Ningún archivo de la carpeta lo usa a él. Sí lo llaman los dos programas que git arranca solo, y que instala `instalar.py`.

Antes de traer nada, agrega su propia carpeta a la lista de sitios donde Python busca. Así los archivos se encuentran, sin importar desde dónde se lo haya llamado.

## Qué tiene adentro

### Una función por subcomando

Todas están hechas igual: reciben lo que se escribió en la consola, llaman a su validador y retornan el número con que termina el programa.

| Función | Subcomando | Qué llama |
|---|---|---|
| `cmd_estandar` | `estandar` | `enlaces.validar_enlaces`, `enlaces.validar_indices` y `citas.validar`. |
| `cmd_plantilla` | `plantilla` | `plantillas.deducir_plantilla` y `plantillas.validar`. |
| `cmd_fases` | `fases` | `fases.validar`. |
| `cmd_trazabilidad` | `trazabilidad` | `trazabilidad.validar`. |
| `cmd_versionado` | `versionado` | `instalar.repositorios_git` y `versionado.validar` por cada repositorio. |
| `cmd_secretos` | `secretos` | `secretos.validar`. |
| `cmd_dependencias` | `dependencias` | `dependencias.validar`. |
| `cmd_rama` | `rama` | `rama.validar`. |
| `cmd_migraciones` | `migraciones` | `migraciones.validar`. |
| `cmd_errores` | `errores` | `errores.validar`. |
| `cmd_rendimiento` | `rendimiento` | `rendimiento.validar`. |
| `cmd_esquema` | `esquema` | `esquema.validar`. |
| `cmd_flujo` | `flujo` | `flujo.validar`. |
| `cmd_ci` | `ci` | `ci.validar`. |
| `cmd_seguridad` | `seguridad` | `seguridad.validar`. |
| `cmd_calidad` | `calidad` | `calidad.validar`. |
| `cmd_aislamiento` | `aislamiento` | `aislamiento.validar`. |
| `cmd_linter` | `linter` | `herramientas.linter`. |
| `cmd_suite` | `suite` | `herramientas.suite`. |
| `cmd_auditoria` | `audit` | `herramientas.auditoria`. |
| `cmd_version` | `version` | `version.validar`. |
| `cmd_commit` | `commit` | `commits.leer_de_git` o la lectura de un archivo, y `commits.validar`. |

Tres son distintas, porque en vez de una lista de hallazgos muestran su propio informe:

**`cmd_plantilla`** — si el documento no existe, se detiene. Si no le dijeron con `--contra` de qué molde salió, lo averigua; si tampoco lo logra, se detiene explicando cómo indicárselo.

**`cmd_checklist`** — muestra cómo quedó cada pieza de la instalación, después el resumen y, si falta algo, el detalle de cómo se arregla. Al final agrega, aparte, lo que diga `version.validar`. Termina en `1` si falta algo.

**`cmd_versiones`** — muestra cómo está cada documento que vino del estándar, la última versión anotada, los últimos cinco registros y, si hace falta, la línea que pone todo al día. Termina en `1` si algo quedó viejo o si el registro no coincide.

### `main()`

- **Recibe:** nada; lee lo que se escribió en la consola.
- **Hace:**
  1. Llama a `preparar_salida`, que deja la pantalla lista para las tildes y las eñes.
  2. Arma la lista de los veinticinco subcomandos. Cada uno trae su explicación y sus opciones, y queda unido a la función que lo atiende.
  3. Mira qué se pidió y llama a esa función.
  4. Termina el programa con el número que ella retornó.

Casi todos aceptan `--raiz` para decirles en qué carpeta trabajar; si no se dice, trabajan sobre la del estándar. `versionado` acepta además `--preparados`, para mirar solo lo que entra en el cambio que se está por guardar.

## Cómo se ejecuta

```
python validadores/validar.py estandar
python validadores/validar.py plantilla proyectos/pos/HU-014.md
python validadores/validar.py commit --archivo .git/COMMIT_EDITMSG
python validadores/validar.py secretos --raiz "C:/ruta/proyecto"
python validadores/validar.py checklist --raiz "C:/ruta/proyecto"
```

Por dentro:

```
main()
   ↓
preparar_salida()
   ↓
lee qué se pidió revisar y con qué opciones
   ↓
llama a cmd_<lo que se pidió>(opciones)
   ↓
   <el validador>.validar(carpeta)  →  [Hallazgo, Hallazgo, ...]
   ↓
comun.reportar(hallazgos, titulo)
   ↓
   muestra las fallas, después los avisos, después el conteo
   ↓
retorna 0 (sin fallas) o 1 (con fallas)
   ↓
el programa termina con ese número
```

## Ejemplos de lo que retorna

Cada función de subcomando retorna el **número con que termina el programa**: `0` si no hubo ninguna falla, `1` si hubo al menos una.

```python
cmd_estandar(argumentos)
0
# y en pantalla:
== Coherencia del estándar ==
OK: sin incumplimientos.

cmd_estandar(argumentos)          # con problemas
1
# y en pantalla:
== Coherencia del estándar ==
[FALLA] pendientes/README.md — el índice no menciona pendientes/10-ideas.md

1 falla(s), 0 aviso(s).

cmd_plantilla(argumentos)
0
# y en pantalla:
== proyectos/pos/HU-014.md contra plantillas/ciclo-vida-proyectos/04-HU.md ==
[AVISO] proyectos/pos/HU-014.md — sección de la plantilla ausente: «Riesgos»

0 falla(s), 1 aviso(s).
# retorna 0 porque los avisos no reprueban

cmd_commit(argumentos)
1
# y en pantalla:
== Mensaje de commit HEAD ==
[FALLA] commit HEAD:1 — asunto sin contenido: «wip» — G2 pide qué y por qué

1 falla(s), 0 aviso(s).

cmd_checklist(argumentos)
1
# y en pantalla:
== Instalación del agente · pos ==
  [ok] f13 — La estructura base del proyecto
  [ok] claude-md — El CLAUDE.md del proyecto
  [FALTA] gitignore — al .gitignore le faltan: CLAUDE.md, .agente/

INSTALACIÓN INCOMPLETA · pos · 12 de 13 · falta: gitignore

- **gitignore** — al .gitignore le faltan: CLAUDE.md, .agente/
  Se arregla así: correr validadores/instalar.py --aplicar

Al margen: el proyecto declara v4.0.0, el estándar va en v5.0.0: …

cmd_versiones(argumentos)
1
# y en pantalla:
== Documentos heredados del estándar · pos ==
  [ok] claude-md — CLAUDE.md
  [VIEJO] stack-instalacion — `.agente/stack-instalacion.md` quedó viejo: la
          plantilla cambió en el estándar (a3f9c21b04de → ff01ab77cc10)

Última actualización registrada: 4.0.0
  2026-08-01  4.0.0      2026-08-01-4.0.0.md

Se pone al día con:
  python "c:/Ing. Jose/ia/agente/validadores/instalar.py" "C:/proyectos/pos" --aplicar

main()
# no retorna: termina el programa con el número de la función que corrió
```

Códigos con que termina el programa:

| Número | Cuándo |
|---|---|
| `0` | No hubo ninguna falla. Puede haber avisos. |
| `1` | Hubo al menos una falla, o al checklist le falta algo. |
