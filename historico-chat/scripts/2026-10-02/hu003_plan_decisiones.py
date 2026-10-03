# -*- coding: utf-8 -*-
"""Plan de la fase A de la HU-003: las dos dudas de 2.7 quedan decididas por el usuario.

- El 103 pasa a `EP-023/pendientes/`: su dueño es EP-023 (análisis 8, punto 15 de «Lo acordado»).
- El índice de pendientes se escribe en `documentacion/pendientes.md`.
"""
import glob
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
FASE = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "HU-003-*", "A-EP-023-HU-003-*"))[0]

T16 = ("| T-16 | Pasar la carpeta del 103 a `EP-023/pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/` "
       "con un guion: mueve la carpeta, corrige los enlaces relativos de sus archivos (un nivel más) y los 127 enlaces "
       "que la nombran en 35 archivos; `origen.py` toma como épica la carpeta que contiene `pendientes/` | "
       "`documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/`, `validadores/origen.py` | CA-08 | "
       "Los 35 archivos que enlazan el 103; solo cambia la ruta | 1 h | T-11 | CP-008 |")

CAMBIOS = {
    "plan_trabajo.md": [
        ("### 2.7 Dudas por resolver antes de codificar\n\n"
         "1. **Dónde queda el índice que arma el programa.**",
         "### 2.7 Dudas por resolver antes de codificar\n\n"
         "Ninguna. Las dos de la primera redacción las decidió el usuario el 2026-10-02, y quedan en 2.6.\n\n"
         "<!-- decididas -->\n\n1. **Dónde queda el índice que arma el programa.**"),
        ("| La versión sube a 45.0.0, MAYOR | MENOR |",
         "| El índice de pendientes se escribe en `documentacion/pendientes.md`, que el programa reescribe completo cada vez; `pendientes/README.md` queda como historia | Escribirlo dentro de `pendientes/` | Lo decidió el usuario; `pendientes/` ya no recibe nada nuevo |\n"
         "| El 103 pasa a `EP-023/pendientes/`, y el validador de fases acepta la carpeta `pendientes/` dentro de una épica, de una HU o de un resumen del día, y nada más | Aceptar el 103 suelto en la épica | Su dueño es EP-023, y el análisis 8 (punto 15 de «Lo acordado») pide `pendientes/` y nada más; se pasa ahora porque se está trabajando |\n"
         "| La versión sube a 45.0.0, MAYOR | MENOR |"),
        ("y la carpeta de un pendiente según lo que se decida en 2.7 |", "y nada más (2.6) |"),
        ("lo escribe donde se decida en 2.7 |", "lo escribe en `documentacion/pendientes.md` (2.6) |"),
        ("| `validadores/fases.py` | Modificar | Validador | Acepta `pendientes/` y las carpetas de pendiente |",
         "| `validadores/fases.py` | Modificar | Validador | Acepta `pendientes/` dentro de una épica, una HU o un resumen del día |\n"
         "| `validadores/origen.py` | Modificar | Validador | La épica de un pendiente que vive en `pendientes/` |\n"
         "| `documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/103-cada-documento-de-la-cadena-sale-del-anterior/` | Mover | Documentación | A `EP-023/pendientes/`, con sus enlaces |\n"
         "| `documentacion/pendientes.md` | Nuevo | Documentación | El índice, que escribe el programa |"),
        ("| `fases.py` acepta `pendientes/` | La revisión de épicas y HU | Las carpetas de pendiente no se tratan como HU ni como fase |",
         "| `fases.py` acepta `pendientes/` | La revisión de épicas y HU | Las carpetas de pendiente no se tratan como HU ni como fase |\n"
         "| El 103 cambia de carpeta | 35 archivos con 127 enlaces, entre ellos fases cerradas y los análisis aprobados del 103; `origen.py`, que agrupa los análisis por épica | Un guion corrige solo la ruta; `origen.py` sube un nivel cuando la carpeta del pendiente está en `pendientes/` |"),
        ("| T-14 | El pendiente nuevo nace", T16 + "\n| T-14 | El pendiente nuevo nace"),
        ("| `validadores/fases.py` | CA-08 | La revisión de épicas y HU | 1 h | Ninguna | CP-008 |",
         "| `validadores/fases.py` | CA-08 | La revisión de épicas y HU | 1 h | Ninguna | CP-008 |"),
        ("Luego el índice y el andamio: T-13 y T-14.", "Luego el traslado del 103, el índice y el andamio: T-16, T-13 y T-14."),
        ("| T-15 | Regenerar", "| T-15 | Regenerar"),
        ("| 2 h | T-01 a T-14 | CP-001 a CP-009 |", "| 2 h | T-01 a T-14 y T-16 | CP-001 a CP-009 |"),
        ("| Las dudas de 2.7 | La fase no arranca hasta que el usuario las decida |",
         "| Que un enlace al 103 quede roto al pasarlo | El guion cuenta los enlaces antes y después, y `validar.py estandar` revisa los rotos |"),
    ],
    "plan_pruebas.md": [
        ("| 2 | Correrlo sobre el repositorio | Ya no falla por el 103 ni por `HU-036/pendientes` |",
         "| 2 | Correrlo sobre el repositorio | Ya no falla por el 103, que vive en `EP-023/pendientes/`, ni por `HU-036/pendientes` |\n"
         "| 2a | Buscar enlaces rotos con `validar.py estandar` y correr `validar.py origen` | Ninguno roto; `origen` lee los análisis del 103 en su lugar nuevo |"),
        ("| 4 | Correr el programa del índice | Lista todos, con su número, dónde viven y si su plan cerró |",
         "| 4 | Correr el programa del índice | Escribe `documentacion/pendientes.md` con todos, su número, dónde viven y si su plan cerró |"),
        ("| **Precondiciones** | T-11 a T-14 terminadas |", "| **Precondiciones** | T-11 a T-14 y T-16 terminadas |"),
    ],
    "estado-fase.md": [
        ("☐ Escritos; esperan las dos dudas de 2.7 y la aprobación", "☐ Escritos; esperan la aprobación"),
        ("**Hechas:** 0 de 15. **Bloqueadas:** todas, hasta que se decidan las dudas de 2.7.",
         "**Hechas:** 0 de 16. **Bloqueadas:** todas, hasta que se aprueben los planes."),
        ("- Dónde queda el índice de pendientes (plan, 2.7).\n"
         "- Si el validador de fases acepta la carpeta del 103 directamente en la épica (plan, 2.7).\n", ""),
    ],
}


def main():
    for nombre, pares in CAMBIOS.items():
        ruta = os.path.join(FASE, nombre)
        with open(ruta, encoding="utf-8") as f:
            t = f.read()
        for viejo, nuevo in pares:
            assert t.count(viejo) == 1, (nombre, viejo[:70])
            t = t.replace(viejo, nuevo)
        if nombre == "plan_trabajo.md":
            i = t.index("<!-- decididas -->")
            j = t.index("### 2.8")
            t = t[:i].rstrip("\n") + "\n\n" + t[j:]
        with open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(t)


if __name__ == "__main__":
    main()
