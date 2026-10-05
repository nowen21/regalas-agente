"""HU-027 · Con qué texto de cada regla, y con qué ajuste, `02·F4` sale entre las
parecidas a `02·F25`. Imprime, por variante, el puesto de F4, el reparto de los
parecidos y las seis primeras.

Se corre desde la raíz del estándar: python historico-chat/scripts/2026-10-05/medir_reglas_parecidas.py
"""
import os
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "proyectos", "cimiento"))
sys.path.insert(0, os.path.join(RAIZ, "memoria"))

import numpy as np  # noqa: E402
import semantica  # noqa: E402
from core.comun import Proyecto  # noqa: E402
from core.validadores.metareglas import CuerpoDeReglas  # noqa: E402

reglas = [r for r in CuerpoDeReglas.leer(Proyecto.estandar()) if not getattr(r, "derogada", False)]
ids = [r.id for r in reglas]


def cuerpo(r):
    return " ".join(t for _, t in r.cuerpo)


VARIANTES = {
    "titulo": lambda r: r.titulo,
    "titulo+cuerpo": lambda r: r.titulo + ". " + cuerpo(r),
    "cuerpo": cuerpo,
}

for nombre, texto in VARIANTES.items():
    crudos = np.array(semantica.embed([texto(r) for r in reglas]), dtype=float)
    for centrar in (False, True):
        m = crudos - crudos.mean(0) if centrar else crudos
        m = m / np.linalg.norm(m, axis=1, keepdims=True)
        s = m @ m.T
        i = ids.index("F25")
        orden = [j for j in np.argsort(-s[i]) if j != i]
        puesto = [ids[j] for j in orden].index("F4") + 1
        pares = s[np.triu_indices(len(ids), 1)]
        print("%-14s %-8s F4 puesto %3d (%.2f) | mediana %.2f, p99 %.2f | %s" % (
            nombre, "centrado" if centrar else "crudo", puesto, s[i, ids.index("F4")],
            np.percentile(pares, 50), np.percentile(pares, 99),
            ", ".join("%s %.2f" % (ids[j], s[i, j]) for j in orden[:6])))

# Con título y cuerpo, sin centrar: cuántas parecidas le tocan a cada regla según el umbral.
crudos = np.array(semantica.embed([VARIANTES["titulo+cuerpo"](r) for r in reglas]), dtype=float)
m = crudos / np.linalg.norm(crudos, axis=1, keepdims=True)
s = m @ m.T
np.fill_diagonal(s, 0)
for umbral in (0.80, 0.82, 0.83, 0.84, 0.85):
    vecinas = (s >= umbral).sum(1)
    print("umbral %.2f: con alguna %3d de %d reglas, media %.1f, máximo %d" % (
        umbral, (vecinas > 0).sum(), len(ids), vecinas.mean(), vecinas.max()))
