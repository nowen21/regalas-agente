# -*- coding: utf-8 -*-
"""Análisis 9, turnos 212 a 214: a los análisis 1 a 8 y al de la forma anterior se les agregan,
una sola vez, las secciones que les faltan. Todo sale de sus propias conclusiones; nada se decide de nuevo.

- «Lo acordado»: las conclusiones, una por línea con su origen, generadas desde la tabla.
- «Dónde más puede pasar»: los casos que sus conclusiones ya cubren.
- «Lo que aporta al análisis principal»: resultado, qué y qué cambia en el principal.
"""
import glob
import os
import re

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
CARPETA = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "103-*"))[0]
VIEJO = os.path.join(RAIZ, "analisis", "base-2026-08-07-cumplimiento-meta-reglas.md")
NOTA = "> Se agregó en el piloto, por el [análisis 9](%s), a partir de las conclusiones de este análisis; no decide nada nuevo."

DONDE = {
    1: [("Hallazgo que aparece al ejecutar el plan", "Cualquier proyecto", "Se abre otro pendiente y el trabajo se duplica", "Conclusiones 10 y 18"),
        ("Pendiente que nace de una conversación", "Cualquier proyecto", "No se sabe dónde vive", "Conclusión 11"),
        ("Cambia la necesidad", "Cualquier documento de la cadena", "Se corrige abajo y arriba sigue lo viejo", "Conclusión 8"),
        ("Punto sin origen", "Cualquier documento de la cadena", "Entra lo que no se pidió", "Conclusión 39")],
    2: [("Turnos que no son del análisis", "Cualquier sesión", "Entra al análisis lo que no se decidió ahí", "Conclusión 4"),
        ("Dos análisis abiertos", "Cualquier proyecto", "Quedan dos análisis sobre lo mismo", "Conclusión 6"),
        ("Etiquetas que la herramienta pone al mensaje", "Cualquier herramienta", "Se copian palabras que el usuario no dijo", "Conclusión 10"),
        ("Otro proyecto que hereda", "Cualquier proyecto", "La conversación hay que pasarla a mano", "Conclusión 8")],
    3: [("Error del agente al leer un análisis", "Cualquier análisis", "Se toma como hallazgo lo que no lo es", "Conclusiones 3 y 8"),
        ("Orden entre HU", "Cualquier épica", "Se construye en un orden que no se decidió", "Conclusión 5"),
        ("Una HU que necesita algo de otra", "Cualquier épica", "Se construye antes de tiempo", "Conclusión 6")],
    4: [("HU que sale directo de un pendiente", "Cualquier proyecto", "El contexto repite o no dice el problema", "Conclusión 5"),
        ("HU que sale de una épica", "Cualquier épica", "Cada HU repite el problema completo", "Conclusiones 2 y 3")],
    5: [("Criterio que pide una regla con dos exigencias", "Cualquier HU", "La regla no pasa su checklist", "Conclusión 2"),
        ("Archivo que el plan no declara", "Cualquier fase", "Se edita fuera del plan", "Conclusión 4"),
        ("Regla que no cabe en su largo", "Cualquier regla que cambia", "La regla queda fuera del molde", "Conclusión 5")],
    6: [("Reglas que citan una regla que se deroga", "Cualquier derogación", "Quedan apoyadas en lo que no rige", "Conclusiones 2 y 3"),
        ("Lo que exige una regla y el CA no nombra", "Cualquier HU", "Se deja de cumplir la regla", "Conclusión 5"),
        ("Ejemplo de una regla que choca con otra", "Cualquier regla", "Dos reglas dicen lo contrario", "Conclusión 6")],
    7: [("Plantilla sin el campo que una regla nueva exige", "Cualquier plantilla", "El documento hecho con la plantilla incumple la regla", "Conclusiones 2 y 3")],
}

APORTA = {
    1: ("Cambia lo que se construye y modifica la idea",
        "Antes de repartir el trabajo hay un análisis, cada documento sale del anterior, un hallazgo detiene la ejecución y nada se escribe fuera del plan; nace EP-023",
        "«Qué se construye hoy»: EP-023 y sus siete HU. «Lo que está definido»: el análisis va antes de repartir el trabajo"),
    2: ("Cambia lo que se construye",
        "La conversación pasa sola al análisis, y se prende, se pausa y se aprueba con tres palabras; hay un solo análisis abierto a la vez",
        "«Qué se construye hoy»: el enganche del análisis"),
    3: ("Aclara",
        "De un análisis pasan a trabajo la propuesta final y «Lo que se tiene que hacer»; la conversación es contexto. El H-1 no era hallazgo, sino un error de lectura",
        "«Lo que está definido»: qué pasa a trabajo desde un análisis"),
    4: ("Aclara",
        "El contexto de una HU que sale de una épica es la parte del problema que le toca, con el enlace a la épica",
        "«Lo que está definido»: qué va en el contexto de una HU"),
    5: ("Modifica la idea",
        "La regla que reemplaza el cierre en un archivo aparte se parte en dos: `13·DOC24` para el análisis individual y `13·DOC25` para el principal",
        "«Qué se construye hoy»: `DOC24` y `DOC25` en lugar de una sola regla"),
    6: ("Modifica la idea",
        "Lo pedido es el criterio de aceptación más lo que exigen las reglas; `01·C15` y `00·ID1` dejan de apoyarse en `01·C14`, y el ejemplo de `02·F19` cambia",
        "«Lo que está definido»: qué es lo pedido"),
    7: ("Cambia lo que se construye",
        "Cada criterio de la plantilla de la HU lleva «Sale de»",
        "«Qué se construye hoy»: la plantilla de la HU con «Sale de»"),
    8: ("Cambia lo que se construye y amplía la idea",
        "El freno de las escrituras cubre todos los canales en cuatro capas; el análisis abre todos los casos, ordena las HU por su dependencia y consulta recomendaciones; los pendientes viven dentro de lo que los origina",
        "«Qué se construye hoy»: el freno, las secciones nuevas del análisis y la carpeta `pendientes/` dentro de su origen. «Lo que está definido»: Cimiento es la base de todos los proyectos, y el análisis considera todos los casos"),
}

APORTA_VIEJO = ("Aclara",
                "El cuerpo de reglas frente a las meta-reglas: el 28 % cumplía, el 41 % cumplía con observaciones y el 31 % incumplía; la norma estaba bien definida y se cumplía a medias",
                "«Lo que está definido»: cómo estaba el cuerpo de reglas frente a sus meta-reglas el 2026-08-07")


def enlace_a9(ruta):
    return os.path.relpath(os.path.join(CARPETA, "analisis-9.md"), os.path.dirname(ruta)).replace(os.sep, "/")


def seccion_aporta(ruta, datos):
    resultado, que, cambia = datos
    return ("\n## Lo que aporta al análisis principal\n\n" + NOTA % enlace_a9(ruta) + "\n\n"
            "| Resultado | Qué | Qué cambia en el análisis principal |\n|---|---|---|\n"
            "| %s | %s | %s |\n" % (resultado, que, cambia))


def conclusiones(texto):
    m = re.search(r"^## Conclusiones.*$", texto, re.M)
    fin = re.search(r"^## ", texto[m.end():], re.M)
    bloque = texto[m.end():m.end() + fin.start()]
    salida = []
    for linea in bloque.split("\n"):
        f = re.match(r"^\| *(\d+) *\|(.*)\|\s*$", linea)
        if f:
            celdas = [c.strip() for c in f.group(2).split("|")]
            salida.append((int(f.group(1)), celdas[0], celdas[1], celdas[-1]))
    return salida


def seccion_acordado(ruta, texto):
    lineas = ["%d. %s: %s (%s)." % (n, tema, conclusion.rstrip("."), origen)
              for n, tema, conclusion, origen in conclusiones(texto)]
    return ("## Lo acordado\n\n" + NOTA % enlace_a9(ruta) + "\n\n" + "\n".join(lineas) + "\n\n---\n\n")


def seccion_donde(ruta, casos):
    filas = "\n".join("| %s | %s | %s | %s |" % c for c in casos)
    return ("### Dónde más puede pasar\n\n" + NOTA % enlace_a9(ruta) + "\n\n"
            "| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |\n|---|---|---|---|\n" + filas + "\n\n")


def main():
    for n in range(1, 9):
        ruta = os.path.join(CARPETA, "analisis-%d.md" % n)
        with open(ruta, encoding="utf-8") as f:
            t = f.read()
        assert "## Lo que aporta al análisis principal" not in t
        if n in DONDE:
            m = re.search(r"^(---\n\n)?## Conclusiones", t, re.M)
            t = t[:m.start()] + seccion_donde(ruta, DONDE[n]) + t[m.start():]
        i = t.index("## Lo que aportó cada parte")
        t = t[:i] + seccion_acordado(ruta, t) + t[i:]
        t = t.rstrip("\n") + "\n" + seccion_aporta(ruta, APORTA[n])
        with open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(t)
    with open(VIEJO, encoding="utf-8") as f:
        t = f.read()
    assert "## Lo que aporta al análisis principal" not in t
    with open(VIEJO, "w", encoding="utf-8", newline="\n") as f:
        f.write(t.rstrip("\n") + "\n" + seccion_aporta(VIEJO, APORTA_VIEJO))


if __name__ == "__main__":
    main()
