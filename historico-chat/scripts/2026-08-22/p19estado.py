# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, r"C:/Users/user/AppData/Local/Temp/claude/c--Ing--Jose-ia-agente/563dc2f9-c782-46f9-af82-c9bc948b3566/scratchpad")
import p19lib as L
os.chdir(r"c:\Ing. Jose\ia\agente")

c = L.leer("CHANGELOG.md")
mal = "**Ninguna regla del estándar se pasa ya del largo que ella misma fija.** Era la última deuda de la fila 10 del checklist: quince"
bien = "**Ninguna regla del estándar se pasa ya del largo que ella misma fija.** El estándar le da cuatro líneas a cada regla, y quince"
assert mal in c
L.escribir("CHANGELOG.md", c.replace(mal, bien, 1))

p = "pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md"
s = L.leer(p)
s = s.replace("**Estado:** abierto, con la primera ronda del arreglo hecha (v30.8.0) y la partición de las 26 por delante",
              "**Estado:** abierto solo por **dos decisiones del usuario** (`17·I3` y `12·PR3`); el resto del arreglo está hecho (v30.8.0 a v30.9.0)", 1)
s += """
## Segunda ronda hecha: nadie se pasa del molde  ·  2026-08-22 (v30.8.1 a v30.9.0)

Se recorrió capítulo por capítulo, con su verificación y su publicación cada uno:

| Versión | Capítulo | Qué se hizo |
|---|---|---|
| 30.8.1 | `00` | `ID5`, `ID7`, `ID8`, `ID9` al molde; el glosario decía seis reglas del núcleo y son nueve |
| 30.8.2 | `01` | `C5`, `C21`, `C22` al molde |
| 30.8.3 | `02` | las doce largas al molde, sin tocar excepciones ni ejemplos |
| 30.9.0 | `03`, `13`, `20` | quince al molde; `13·DOC11` y `20·M6` ganan [anexo](../base/13-documentacion/tabla-de-trazabilidad.md) porque su contenido era una tabla y una lista de pasos |

```
$ python validadores/validar.py metareglas
0 falla(s), 1 aviso(s).
```

**Ni una falla y ni un aviso de largo.** El único aviso que queda es del registro de cambios, no de una regla.

### Las 26 particiones: 23 ya estaban hechas

Al ir a partirlas se encontró que la tabla de arriba venía de la medición vieja. Estaban hechas desde el 2026-08-18: `N7`, `N8`, `N9`, `C24`, `C25`, `C26`, `S12` a `S16`, `E6`, `T8`, `G10`, `G11`, `CFG5`, `IM6`, `IM7` y `F25`. Y dos se resolvieron **sin partirse**, con la partida escrita en su propio sello: `14·EST2` (lo que parecía la segunda exigencia era una advertencia sobre el motor, que además nombraba tecnología) y `12·PR3` (no tenía dos exigencias: no tenía ninguna propia, y se reescribió para que tuviera la suya).

### Lo que queda, y es del usuario

| Qué | Por qué no lo decide el agente |
|---|---|
| **`17·I3` · accesibilidad mínima** | Es la única de las 26 que sigue sin partirse. Su cuerpo son cuatro puntos sueltos (etiqueta, contraste, teclado, color) y el pendiente dejó dos salidas escritas: **una** regla que exige el mínimo, con la lista como su contenido, o **cuatro** reglas. Las dos cumplen el checklist |
| **`12·PR3` · derogarla** | El usuario dijo que sí el 2026-08-22, pero esa pregunta venía del diagnóstico del 2026-08-14, cuando `PR3` era «un índice con forma de regla». El 2026-08-18 se reescribió y hoy exige algo que **no dice ninguna otra**: que el dato personal es sensible por defecto, sin esperar a que el proyecto lo declare. Derogarla ahora perdería esa exigencia |
"""
L.escribir(p, s)

r = L.leer("historico-chat/resumenes/2026-08-21/que-es-memory-y-trazas.md")
h9 = """### H-9 · Ninguna regla se pasa ya del molde, y las particiones que faltaban casi todas estaban hechas

**Qué se encontró.** La segunda ronda del pendiente 19 iba a partir 26 reglas y recortar 37. Al abrir capítulo por capítulo apareció que **23 de las 26 particiones ya se habían hecho el 2026-08-18** y que dos más se habían resuelto sin partirse, dejándolo escrito en su propio sello. Lo que quedaba de verdad era el largo: 34 reglas con el sello diciendo ✅ en la fila 10 y el cuerpo de hasta el doble.

**Qué se decidió.** Recortar dejando la exigencia y mandar los porqués a [notas/porques-recortados-al-molde.md](../../../notas/porques-recortados-al-molde.md). Y para dos que no se podían recortar sin perder su contenido —la tabla de trazabilidad de `13·DOC11` y los seis pasos del desempate de `20·M6`— repetir la salida que el usuario ya había aprobado para `02·F12`: **anexo del capítulo**, con el texto entero.

**Dónde queda.** v30.8.1 a v30.9.0, cinco publicaciones, una por capítulo. `validar.py metareglas`: cero fallas y ningún aviso de largo. La ronda queda escrita en el [pendiente 19](../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**Abierto, y es del usuario:** `17·I3` (una regla con la lista, o cuatro reglas) y `12·PR3` (el sí a derogarla venía del diagnóstico viejo; hoy la regla exige algo propio que se perdería).

---

## ¿Se puede cerrar la sesión?"""
r = r.replace("---\n\n## ¿Se puede cerrar la sesión?", h9, 1)
L.escribir("historico-chat/resumenes/2026-08-21/que-es-memory-y-trazas.md", r)
print("ok")
