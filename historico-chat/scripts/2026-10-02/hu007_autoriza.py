# -*- coding: utf-8 -*-
"""Fase A de la HU-007: T-01 (la plantilla del plan), T-03 (el formato de la línea «Autoriza escribir») y T-04
(la línea en las diez reglas que autorizan escribir sin plan, con su sello contra 48.0.0). La autoriza la regla
(análisis 1 del pendiente 103, turno 106 y conclusión 46)."""
import os
import re

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SELLO = "contra **v48.0.0**, el **2026-10-02**."
_SELLO = re.compile(r"contra \*\*v[\d.]+\*\*, el \*\*[\d-]+\*\*\.")

# (archivo, título de la regla si vive en un capítulo, rutas que autoriza)
REGLAS = [
    ("base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md", None,
     ["historico-chat/*.md", "historico-chat/resumenes/**"]),
    ("base/13-documentacion/reglas/DOC24-cierra-el-analisis-en-su-mismo-archivo.md", None,
     ["**/pendientes/*/analisis-*.md"]),
    ("base/13-documentacion/reglas/DOC25-reescribe-el-analisis-principal-con-su-lista-de-cambios.md", None,
     ["**/analisis/*-analisis-principal.md"]),
    ("base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md", None,
     ["documentacion/senales.md", "memoria/senales.db"]),
    ("base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md", None,
     ["CHANGELOG.md", "VERSION"]),
    ("base/20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md", None,
     ["documentacion/pendientes.md"]),
    ("base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md", None,
     ["documentacion/epicas/*/HU-*/*/*.md"]),
    ("base/04-seguridad.md", "## S18 ·", ["historico-chat/scripts/**"]),
    ("base/01-conducta.md", "## C19 ·", ["historico-chat/memory/**"]),
    ("base/01-conducta.md", "## C28 ·", ["base/mapa-de-tareas.md", "base/reglas-por-tarea/*.md"]),
]

FORMATO = """
### 7 · Lo que autoriza escribir — **solo la regla que lo autoriza**

Hay archivos que se escriben siempre, sin que ningún plan los nombre: la
transcripción, el resumen, el análisis, los guiones de apoyo. La regla que los
pide es la que los autoriza, y lo dice en una línea que va **justo después de
`**Aplica a:**`**:

```
**Autoriza escribir:** `historico-chat/resumenes/**` · `historico-chat/*.md`
```

Cada ruta va entre comillas invertidas, desde la raíz del proyecto; `*` vale por
un tramo del nombre y `**` por cualquier cantidad de carpetas. La lee
[`validadores/autorizado.py`](../../validadores/autorizado.py), y con ella el
`pre-commit` y el freno dejan pasar lo que una regla ya autoriza (análisis 1 del
pendiente 103, conclusión 46). La regla propia de un proyecto usa la misma línea
en `.agente/reglas-proyecto.md`.

La regla que no autoriza escribir nada no lleva la línea.
"""


def leer(r):
    with open(os.path.join(RAIZ, *r.split("/")), encoding="utf-8") as f:
        return f.read()


def escribir(r, t):
    with open(os.path.join(RAIZ, *r.split("/")), "w", encoding="utf-8", newline="\n") as f:
        f.write(t)


def linea(rutas):
    return "**Autoriza escribir:** " + " · ".join("`%s`" % r for r in rutas)


def reglas():
    for archivo, titulo, rutas in REGLAS:
        t = leer(archivo)
        if titulo:
            i = t.index(titulo)
            fin = t.find("\n## ", i + 3)
            fin = len(t) if fin < 0 else fin
        else:
            i, fin = 0, len(t)
        seccion = t[i:fin]
        m = re.search(r"^\*\*Aplica a:\*\*.*$", seccion, re.M)
        assert m, archivo
        assert "**Autoriza escribir:**" not in seccion, archivo
        seccion = seccion[:m.end()] + "\n\n" + linea(rutas) + seccion[m.end():]
        assert len(_SELLO.findall(seccion)) == 1, (archivo, titulo)
        seccion = _SELLO.sub(SELLO, seccion)
        escribir(archivo, t[:i] + seccion + t[fin:])


def formato():
    r = "base/20-meta-reglas/estructura-regla.md"
    t = leer(r)
    ancla = "comprueba es que la pieza de verdad la ejecute: eso se lee.\n"
    assert t.count(ancla) == 1
    escribir(r, t.replace(ancla, ancla + FORMATO))
    r = "plantillas/reglas-proyecto.md"
    t = leer(r)
    ancla = "- **Señal asociada:** «id o enlace en la memoria"
    assert t.count(ancla) == 1
    t = t.replace(ancla, "- **Autoriza escribir:** «solo si la regla autoriza escribir algo sin plan: las rutas entre comillas invertidas, como en [`20·M5`](«RUTA-ESTANDAR»/base/20-meta-reglas/estructura-regla.md); si no, se borra la línea»\n" + ancla)
    escribir(r, t)


def plantilla_plan():
    r = "plantillas/ciclo-vida-proyectos/07-plan-trabajo.md"
    t = leer(r)
    ancla = "| **Fecha apertura** | AAAA-MM-DD |\n"
    assert t.count(ancla) == 1
    t = t.replace(ancla, ancla + "| **Aprobación** ([`02·F4`](../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | «quién», el «AAAA-MM-DD», con la versión «X.Y.Z» |\n")
    m = re.search(r"^### 2\.1 .*\n\n(> .*\n)", t, re.M)
    assert m
    t = t[:m.end()] + ("> Cada fila lleva una o más rutas exactas entre comillas invertidas, separadas por coma. "
                       "No valen comodines (`*`), carpetas (`ruta/`) ni descripciones: lo que una regla ya autoriza "
                       "escribir no se lista acá ([`02·F8`](../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).\n") + t[m.end():]
    escribir(r, t)


if __name__ == "__main__":
    plantilla_plan()
    formato()
    reglas()
