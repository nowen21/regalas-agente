# Pendiente · El checklist da por faltantes enganches que sí están, por la mayúscula de la letra de unidad

**Estado:** abierto · anotado 2026-08-20.

| | |
|---|---|
| **Historia de usuario** | EP-007 (instalación) — es el validador de la instalación el que reprueba; la HU concreta la asigna el estándar |
| **Proyecto de origen** | **matematica** · `C:\wamp64\www\proyectos\personales\matematica` |
| **Su pendiente de seguimiento** | `pendientes/01-esperando-correccion-checklist-mayusculas.md` — queda **abierto allá** hasta que este se corrija |
| **A quién avisar al cerrar** | a **todos los instalados** — cualquier proyecto en Windows puede invocar el validador con otra capitalización; la lista está en [plantillas/proyectos.md](../plantillas/proyectos.md) |

## El problema

`validar.py checklist` reprueba el componente `enganches-claude` aunque los 16 enganches estén correctamente escritos en `.claude/settings.json`. La causa está en `_enganches_claude` (`validadores/checklist.py`, líneas 199 a 219): reconstruye el comando esperado de cada enganche usando **tal cual** las rutas `--raiz` y la del estándar con que se invocó, y lo compara como **texto literal** contra el `command` guardado. En Windows las rutas no distinguen mayúsculas: si el instalador escribió `C:/wamp64/...` y el checklist se corre con `--raiz "c:\wamp64\..."`, ningún comando coincide y los 16 enganches se reportan como «sin poner o vencidos».

## Cómo se reproduce

Proyecto `matematica`, 2026-08-20, estándar v28.0.0:

1. `python validadores/instalar.py "c:\wamp64\www\proyectos\personales\matematica" --aplicar` — escribe los enganches con `C:/wamp64/...` (normaliza la unidad a mayúscula).
2. `python validadores/validar.py checklist --raiz "c:\wamp64\www\proyectos\personales\matematica"` (unidad en minúscula) → `[FALTA] enganches-claude` con los 16 guiones listados.
3. El mismo comando con `--raiz "C:\wamp64\..."` (mayúscula) → `[ok] enganches-claude`.

## Por qué importa

No bloquea el trabajo, pero hace que la instalación se reporte **incompleta estando completa**: el agente, obedeciendo el estándar, anuncia en cada respuesta una falta que no existe, y un usuario (o el propio agente) puede intentar «repararla» duplicando o reescribiendo enganches sanos. Un validador que da falsos negativos enseña a desconfiar de todos sus veredictos.

## Qué falta

Normalizar antes de comparar. Dos salidas:

1. **Comparar rutas normalizadas** (`os.path.normcase`/`os.path.abspath` sobre ambos lados, o comparar el comando tras normalizar las rutas embebidas) — corrige la causa para cualquier capitalización y también para `/` vs `\`. Es la que conviene.
2. Normalizar solo la letra de unidad al construir `esperado` — más barato pero deja vivo el resto de diferencias de capitalización que Windows tolera.

Revisar de paso si otros componentes del checklist comparan rutas como texto literal (por ejemplo `_registro` ya usa `normcase`; `_enganches_claude` no).

## El límite

Este pendiente cubre solo la comparación del checklist. No cubre defectos de escritura del instalador (los enganches quedan bien escritos) ni la comparación de enganches de git (`_enganches_git`), que no mostró el defecto en este caso.

## Cómo se sabrá que cerró

En cualquier proyecto instalado en Windows, correr `validar.py checklist --raiz` con la letra de unidad en **minúscula** y en **mayúscula**: ambas invocaciones deben dar `[ok] enganches-claude` sin haber tocado `settings.json`.
