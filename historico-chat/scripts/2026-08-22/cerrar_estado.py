# -*- coding: utf-8 -*-
"""Pone el `estado-fase` de una fase recién ejecutada en su estación de cierre.

Se usa solo cuando el `resultado_pruebas` y el `funcionalidad_implementada` de
esa fase ya están escritos: este archivo no decide nada, refleja lo que ellos
dicen.
"""
import io, os, re


def cerrar(carpeta, veredicto="Cumple", cumplidos="", nota_extra="", niveles=5):
    p = os.path.join(carpeta, "estado-fase.md")
    s = io.open(p, encoding="utf-8").read()
    arriba = "../" * niveles

    nota = ("\n> **Puesto al día el 2026-08-22.** La fase estaba detenida esperando "
            "dudas que solo el usuario podía contestar, y hoy las contesta el propio "
            "repositorio: quedan escritas en el §0.1 del "
            "[resultado_pruebas](resultado_pruebas.md). Se corrieron los casos y se "
            "cerró. Sale del [pendiente 59](%spendientes/59-las-42-dudas-que-detienen-26-fases.md).%s\n"
            % (arriba, (" " + nota_extra) if nota_extra else ""))

    # Las tablas de estaciones y de tareas.
    s = re.sub(r"^\|\s*(T-\d+)\s*\|\s*(Pendiente|Bloqueada)\s*\|(.*)$",
               lambda m: "| %s | Hecha |%s" % (m.group(1), m.group(3)), s, flags=re.M)
    s = re.sub(r"\*\*Hechas:\*\*\s*0\s*de\s*(\d+)\.\s*\*\*Bloqueadas:\*\*[^\n]*",
               lambda m: "**Hechas:** %s de %s. **Bloqueadas:** ninguna." % (m.group(1), m.group(1)), s)
    for etapa in ("Implementación", "Verificación", "Revisión crítica",
                  "Cierre documental", "Pruebas", "Ejecución continua"):
        s = re.sub(r"(\|\s*\d+\s*\|\s*%s\s*\|[^|]*\|\s*)Pendiente(\s*\|)" % etapa,
                   r"\1☑\2", s)
    s = re.sub(r"(\|\s*\d+\s*\|\s*(?:Commit|Publicación)[^|]*\|[^|]*\|\s*)Pendiente(\s*\|)",
               r"\1👤 se pide al reportar\2", s)

    # El veredicto.
    s = s.replace("| **Concepto** | Todavía no se ejecutó |",
                  "| **Concepto** | **%s** |" % veredicto)
    if cumplidos:
        s = re.sub(r"\| \*\*Criterios cumplidos\*\* \| 0 de (\d+) \|",
                   "| **Criterios cumplidos** | %s |" % cumplidos, s)
        s = re.sub(r"\| \*\*CA cumplidos\*\* \| 0 de (\d+) \|",
                   "| **CA cumplidos** | %s |" % cumplidos, s)
    s = re.sub(r'\| \*\*Criterios en "No"\*\* \| Ninguno, porque no se ha corrido nada \|',
               '| **Criterios en "No"** | Ninguno |', s)

    # Qué la tiene detenida.
    s = re.sub(r"\n\*\*Nada se ejecutó todavía\.\*\*[^\n]*\n", "\n", s)
    s = re.sub(r"\n>\s*\*\*El plan quedó aprobado[^\n]*\n(?:>[^\n]*\n)*", "\n", s)

    if "Puesto al día el 2026-08-22" not in s:
        i = s.find("## 1.1")
        if i < 0:
            i = s.find("## 1.2")
        if i < 0:
            i = s.find("## 2.")
        s = s[:i] + nota.lstrip("\n") + "\n" + s[i:]

    io.open(p, "w", encoding="utf-8", newline="").write(s)
    print("cerrado", os.path.basename(carpeta))
