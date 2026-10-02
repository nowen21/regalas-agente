# -*- coding: utf-8 -*-
"""Pasa los puntos 1 a 8 y 10 de «Lo que se tiene que hacer» del análisis 8 a sus HU y a la épica.

El punto 9 (subir la corrección del H-9 con su versión) se cumple en el commit.
"""
import glob
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
EP = os.path.join(RAIZ, "documentacion", "epicas", "EP-023-lo-que-se-construye-es-lo-que-se-analizo")
A8 = "[análisis 8](../103-cada-documento-de-la-cadena-sale-del-anterior/analisis-8.md)"
BITACORA = ("| 2026-10-02 | Claude, por pedido de Ing. José Dúmar Jiménez Ruíz | %s, según el análisis 8. "
            "La aprobación queda sin efecto hasta que se revise |")
PENDIENTE = "| **Estado** | Pendiente: cambió por el análisis 8 y espera la revisión del usuario |"


def hu(n):
    return glob.glob(os.path.join(EP, "HU-%03d-*" % n, "HU-%03d-*.md" % n))[0]


def leer(ruta):
    with open(ruta, encoding="utf-8") as f:
        return f.read()


def escribir(ruta, texto):
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def una(texto, viejo, nuevo):
    assert texto.count(viejo) == 1, viejo[:70]
    return texto.replace(viejo, nuevo)


def cierre(texto, cambio):
    texto = una(texto, "| **Estado** | Lista: aprobada el 2026-10-01 |", PENDIENTE)
    filas = [l for l in texto.split("\n") if l.startswith("| 2026-")]
    return una(texto, filas[-1], filas[-1] + "\n" + BITACORA % cambio)


def criterio(numero, titulo, punto, gherkin, validar, aprobado):
    return ("### CA-%02d · %s\n\n**Sale de:** análisis 8, punto %d.\n\n```gherkin\n%s\n```\n\n"
            "**Cómo validarlo:**\n%s\n\n**Aprobado cuando:** %s\n\n" % (numero, titulo, punto, gherkin, validar, aprobado))


def hu001():
    ruta = hu(1)
    t = leer(ruta)
    t = una(t, "del [análisis 4](../103-cada-documento-de-la-cadena-sale-del-anterior/analisis-4.md) (punto 2). Los campos",
            "del [análisis 4](../103-cada-documento-de-la-cadena-sale-del-anterior/analisis-4.md) (punto 2) y del " + A8 + " (puntos 2, 3, 5, 7 y 8). Los campos")
    nuevos = (
        criterio(17, "El análisis abre todas las posibilidades", 2,
                 "Dada la plantilla del análisis\nCuando se lee\nEntonces trae la sección «Dónde más puede pasar», con el caso, dónde se presenta, el riesgo si queda sin cubrir y lo que lo cubre\nY el validador no deja cerrar un análisis con un caso sin cubrir ni razón",
                 "1. Abrir la plantilla del análisis.\n2. Correr el validador sobre un análisis aprobado con un caso sin cubrir.",
                 "la sección está y el análisis del paso 2 no cierra.")
        + criterio(18, "Las HU salen con su dependencia y su orden", 3,
                   "Dada la tabla de HU de la propuesta final del análisis\nEntonces lleva de qué HU depende cada una, su orden de ejecución y por qué\nY la hoja de ruta de la épica copia ese orden\nY el validador detiene una HU que va antes de una de la que depende, o un puesto sin razón",
                   "1. Abrir la plantilla del análisis y la de la épica.\n2. Correr el validador sobre una tabla con una HU antes de la que depende.",
                   "las dos plantillas lo piden y el validador detiene el paso 2.")
        + criterio(19, "Las recomendaciones del análisis", 5,
                   "Dado el archivo de recomendaciones del análisis\nEntonces cada recomendación dice qué se hace, por qué y de qué análisis sale\nY hay dos niveles: las de Cimiento y las de cada proyecto\nY la plantilla del análisis abre con una sección que lo enlaza y dice cuáles aplican\nY el validador revisa el origen, que no haya repetidas y que el análisis aprobado diga cuáles consultó\nY el archivo arranca con las que dejaron las lecciones de los análisis 1 a 8",
                   "1. Abrir el archivo de recomendaciones y la plantilla del análisis.\n2. Correr el validador sobre una recomendación sin origen y otra repetida.",
                   "el archivo y la sección existen, las de arranque están y el validador detiene el paso 2.")
        + criterio(20, "El análisis principal al día", 7,
                   "Dado el análisis principal\nEntonces su lista de cambios tiene las líneas de los análisis 6, 7 y 8\nY el validador avisa cuando un análisis aprobado cambia una HU y no aparece en esa lista",
                   "1. Leer la lista de cambios del análisis principal.\n2. Correr el validador con un análisis aprobado que no aparece en ella.",
                   "las tres líneas están y el validador avisa en el paso 2.")
        + criterio(21, "Medir la respuesta antes de entregarla", 8,
                   "Dadas las recomendaciones de arranque\nEntonces una dice que la respuesta se mide contra 00·ID9 antes de entregarla",
                   "1. Leer las recomendaciones de arranque.",
                   "la recomendación está, con su origen.")
        + criterio(22, "Las secciones nuevas no reabren los análisis aprobados", 11,
                   "Dado un análisis aprobado antes de la versión que trae las secciones nuevas\nCuando corre el validador\nEntonces no le exige esas secciones\nY a uno aprobado desde esa versión sí",
                   "1. Correr el validador sobre los análisis 1 a 7 y sobre uno nuevo sin las secciones.",
                   "los análisis 1 a 7 pasan y el nuevo no.")
    )
    t = una(t, "---\n\n## 5. Requisitos no funcionales", nuevos + "---\n\n## 5. Requisitos no funcionales")
    escribir(ruta, cierre(t, "Nacen los CA-17 a CA-22, para la fase D"))


def hu003():
    ruta = hu(3)
    t = leer(ruta)
    t = una(t, "puntos 7, 10, 11, 12, 19, 20 y 21. Los campos",
            "puntos 7, 10, 11, 12, 19, 20 y 21, y del " + A8 + ", punto 10. Los campos")
    nuevo = criterio(8, "La carpeta `pendientes/` vive dentro de lo que origina cada pendiente", 10,
                     "Dado un pendiente\nEntonces vive en una carpeta pendientes/ dentro de lo que lo origina: una épica, una HU o el resumen del día mientras su análisis no decide a dónde va\nY dentro de ella, en su propia carpeta, con pendiente.md y sus análisis\nY el número es uno solo en todo el proyecto\nY un programa arma el índice de todos, con su número, dónde viven y si su plan cerró\nY el validador de fases acepta pendientes/ dentro de una épica, de una HU o de un resumen del día\nY los pendientes abiertos de la carpeta pendientes/ de la raíz y el 103 se trasladan, con sus enlaces al día\nY los cerrados no se tocan (CA-07)",
                     "1. Correr el validador de fases.\n2. Correr el programa del índice.\n3. Buscar los pendientes abiertos y el 103 en su lugar nuevo.",
                     "el validador de fases pasa, el índice lista todos y los abiertos están en su lugar con los enlaces sanos.")
    t = una(t, "---\n\n## 5. Requisitos no funcionales", nuevo + "---\n\n## 5. Requisitos no funcionales")
    escribir(ruta, cierre(t, "Nace el CA-08, sobre la carpeta `pendientes/` dentro de lo que origina cada pendiente"))


def hu006():
    ruta = hu(6)
    t = leer(ruta)
    t = una(t, "punto 9. Los campos", "punto 9, y del " + A8 + ", punto 6. Los campos")
    nuevo = criterio(2, "Las lecciones alimentan las recomendaciones", 6,
                     "Dada la tabla de lecciones del análisis\nEntonces cada lección dice si complementa una recomendación, crea una nueva o no aplica\nY antes de crear una se busca si ya existe",
                     "1. Abrir la tabla de lecciones de la plantilla del análisis.\n2. Llenarla con una lección que complementa una recomendación.",
                     "la columna existe y la recomendación queda complementada, sin una nueva repetida.")
    t = una(t, "---\n\n## 5. Requisitos no funcionales", nuevo + "---\n\n## 5. Requisitos no funcionales")
    t = una(t, "| Dependencia | HU-001: las demás HU se apoyan en el análisis | Bloqueante |",
            "| Dependencia | HU-001: las demás HU se apoyan en el análisis | Bloqueante |\n"
            "| Dependencia | HU-001, fase D: crea las recomendaciones que las lecciones alimentan | Bloqueante |")
    escribir(ruta, cierre(t, "Nace el CA-02, las lecciones alimentan las recomendaciones; depende de la fase D de la HU-001"))


def hu007():
    ruta = hu(7)
    t = leer(ruta)
    t = una(t, "puntos 25, 26, 27 y 31. Los campos", "puntos 25, 26, 27 y 31, y del " + A8 + ", punto 1. Los campos")
    viejo = t[t.index("### CA-02 · "):t.index("### CA-03 · ")]
    nuevo = criterio(2, "El freno detiene lo que no está en el plan ni autorizado, por cualquier canal", 1,
                     "Dado un plan aprobado en la fase activa\nCuando se va a escribir, borrar, ejecutar o publicar algo que no coincide con el plan, por cualquier canal de la herramienta\nEntonces el freno lo detiene antes de actuar, lo encuentra después comparando el estado de git con el plan, lo rechaza al guardar el commit o lo detiene en la integración continua\nY anota el hallazgo en el resumen y vuelve al análisis\nY si una regla ya lo autoriza, según la lista donde cada entrada cita su regla, no lo frena\nY cada adaptador declara qué capas cubre en su herramienta y por qué no las demás",
                     "1. Con un plan aprobado, intentar escribir fuera del plan con la herramienta de escritura, con una redirección de la consola, con un programa y en segundo plano.\n2. Leer el contrato del adaptador.\n3. Intentar escribir algo que la lista de lo autorizado incluye.",
                     "cada intento del paso 1 se detiene en alguna capa con su hallazgo anotado, el contrato dice qué capa cubre cada canal y el paso 3 pasa. Las fases que hagan falta las reparte el plan.")
    nuevo = nuevo.replace("**Sale de:** análisis 8, punto 1.", "**Sale de:** análisis 1, punto 26, y análisis 8, punto 1.")
    t = t.replace(viejo, nuevo)
    t = una(t, "| Dependencia | HU-004: define qué pasa con un hallazgo | Bloqueante |",
            "| Dependencia | HU-004: define qué pasa con un hallazgo | Bloqueante |\n"
            "| Dependencia | HU-003: da la forma del hallazgo que el freno anota | Bloqueante |")
    escribir(ruta, cierre(t, "El CA-02 pasa a la versión siguiente: el freno en cuatro capas, por cualquier canal; depende también de la HU-003"))


def epica():
    ruta = os.path.join(EP, "epica.md")
    t = leer(ruta)
    viejo = t[t.index("## 15. Hoja de ruta"):t.index("## 16. ")]
    nuevo = """## 15. Hoja de ruta

El número identifica a la HU y no cambia; el orden de ejecución sale de las dependencias ([análisis 8](103-cada-documento-de-la-cadena-sale-del-anterior/analisis-8.md), conclusiones 5 y 8).

| Orden | HU | Depende de | Por qué en ese orden | Estado |
|---|---|---|---|---|
| 1 | HU-001, fases A a C | Ninguna | Las demás se apoyan en el análisis | Hecha |
| 2 | HU-005 | HU-001 | Es pequeña y ataca la causa más directa | Hecha |
| 3 | HU-002 | HU-001 | Cada documento sale del anterior | Hecha |
| 4 | HU-001, fase D | Ninguna | Todo análisis que venga usa la plantilla | Por hacer |
| 5 | HU-003 | HU-001 | Da la forma del hallazgo y del pendiente que usan la HU-004 y la HU-007, y resuelve las fallas de `fases` y de `pendientes` | Por hacer |
| 6 | HU-006 | HU-001, fase D | Las lecciones alimentan las recomendaciones que crea la fase D | Por hacer |
| 7 | HU-004 | HU-003 | Detener la ejecución necesita la forma del hallazgo | Por hacer |
| 8 | HU-007 | HU-003, HU-004 | El freno anota el hallazgo y vuelve al análisis | Por hacer |

Las fechas se fijan al planear cada HU.

"""
    escribir(ruta, t.replace(viejo, nuevo))


if __name__ == "__main__":
    hu001()
    hu003()
    hu006()
    hu007()
    epica()
