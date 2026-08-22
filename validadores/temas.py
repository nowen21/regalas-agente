# -*- coding: utf-8 -*-
"""`EP-005 · HU-001` · El histórico se puede buscar por tema, no solo por fecha.

**El problema, medido el 2026-08-14.** El índice del histórico lista las
sesiones por su nombre, y **una sesión trata varios temas**: la del 2026-08-21
tocó el pendiente 16, la administración de proyectos, el ciclo de vida, el
registro que se vaciaba y tres rondas del capítulo de reglas. Buscar «por qué se
decidió esto» significaba abrir sesión por sesión.

**Dónde están los temas, ya escritos.** En los resúmenes: cada hallazgo abre con
`### H-N · «lo que pasó»`, y ese título **es** el tema. No hay que inventar
ninguna clasificación ni pedirle a nadie que etiquete: se recogen los que ya
están.

**Por qué generado y no a mano.** Un índice temático escrito a mano envejece
igual que cualquier otro mapa, y este envejecería más rápido que ninguno: crece
en cada sesión. Se genera, y una comprobación dice si quedó atrás.

**Lo que no hace, y se declara.** No agrupa temas parecidos ni decide de qué
habla un hallazgo: eso es leer. Junta en un archivo lo que hoy está repartido en
decenas, para que buscar sea buscar en uno.
"""
import os
import re

import comun
from comun import AVISO, FALLA, Hallazgo, leer

RESUMENES = os.path.join("historico-chat", "resumenes")
INDICE = os.path.join(RESUMENES, "indice-tematico.md")

_HALLAZGO = re.compile(r"^###\s+(H-\d+)\s*[·:-]\s*(.+?)\s*$", re.M)
_TITULO = re.compile(r"^#\s+(.+?)\s*$", re.M)

CABECERA = """# Índice temático del histórico

**Qué es.** Todos los hallazgos de todos los resúmenes, en un solo archivo, para
poder buscar por tema en vez de abrir sesión por sesión. Cada línea enlaza al
resumen donde vive.

**Lo genera un programa**, no se escribe a mano: `python validadores/validar.py
temas --aplicar`. Si se edita a mano, el próximo generado lo pisa.

**Qué no es.** No es una clasificación: no agrupa temas parecidos ni dice de qué
habla cada hallazgo. Es lo que ya estaba escrito, junto.

"""


def _resumenes(raiz):
    """[(fecha, archivo_rel, título de la sesión, [(id, tema)])] por resumen."""
    carpeta = os.path.join(raiz, *RESUMENES.split(os.sep))
    salida = []
    if not os.path.isdir(carpeta):
        return salida
    for dia in sorted(os.listdir(carpeta)):
        ruta_dia = os.path.join(carpeta, dia)
        if not os.path.isdir(ruta_dia) or not re.match(r"^\d{4}-\d{2}-\d{2}$", dia):
            continue
        for nombre in sorted(os.listdir(ruta_dia)):
            if not nombre.endswith(".md") or nombre.upper() == "README.MD":
                continue
            texto = leer(os.path.join(ruta_dia, nombre))
            titulo = _TITULO.search(texto)
            hallazgos = _HALLAZGO.findall(texto)
            salida.append((dia, "%s/%s" % (dia, nombre),
                           titulo.group(1).strip() if titulo else nombre[:-3],
                           hallazgos))
    return salida


def generar(raiz=None):
    """El texto del índice, sin escribirlo."""
    raiz = raiz or comun.RAIZ
    datos = _resumenes(raiz)
    total = sum(len(h) for _, _, _, h in datos)
    partes = [CABECERA,
              "**%d hallazgos** en **%d resúmenes**, del %s al %s.\n"
              % (total, len(datos), datos[0][0], datos[-1][0]) if datos
              else "Todavía no hay resúmenes.\n"]
    dia_actual = None
    for dia, rel, titulo, hallazgos in datos:
        if not hallazgos:
            continue
        if dia != dia_actual:
            partes.append("\n## %s\n" % dia)
            dia_actual = dia
        partes.append("\n**[%s](%s)**\n" % (titulo, rel))
        for id_, tema in hallazgos:
            partes.append("- `%s` %s" % (id_, tema))
        partes.append("")
    return "\n".join(partes).replace("\n\n\n", "\n\n").rstrip() + "\n"


def escribir(raiz=None):
    """Escribe el índice y devuelve su ruta."""
    raiz = raiz or comun.RAIZ
    ruta = os.path.join(raiz, *INDICE.split(os.sep))
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(generar(raiz))
    return ruta


def validar(raiz=None):
    """¿El índice existe y dice lo que dicen los resúmenes de hoy?"""
    raiz = raiz or comun.RAIZ
    ruta = os.path.join(raiz, *INDICE.split(os.sep))
    esperado = generar(raiz)
    if not os.path.isfile(ruta):
        return [Hallazgo(AVISO, ruta, 0,
                         "falta el índice temático — se genera con "
                         "`validar.py temas --aplicar`")]
    if leer(ruta) != esperado:
        return [Hallazgo(AVISO, ruta, 0,
                         "el índice temático quedó atrás de los resúmenes — "
                         "se regenera con `validar.py temas --aplicar`")]
    return []


def linea_resumen(raiz=None):
    raiz = raiz or comun.RAIZ
    datos = _resumenes(raiz)
    if not datos:
        return ""
    total = sum(len(h) for _, _, _, h in datos)
    mudos = sum(1 for _, _, _, h in datos if not h)
    return ("Resúmenes: %d · hallazgos indexados: %d · resúmenes sin ningún "
            "hallazgo: %d" % (len(datos), total, mudos))


if __name__ == "__main__":
    comun.no_es_punto_de_entrada("temas")
