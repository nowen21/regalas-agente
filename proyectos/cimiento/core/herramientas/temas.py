"""`EP-005·HU-001` · El histórico se puede buscar por tema, no solo por fecha.

**El problema, medido el 2026-08-14.** El índice del histórico lista las
sesiones por su nombre, y una sesión trata varios temas: buscar «por qué se
decidió esto» era abrir sesión por sesión.

**Los temas ya están escritos**, en los resúmenes: cada hallazgo abre con
`### H-N · «lo que pasó»`, y ese título es el tema. No hay que inventar ninguna
clasificación: se recogen los que están.

**Generado y no a mano**: un índice temático escrito a mano envejece más rápido
que ningún otro mapa, porque crece en cada sesión. Se genera, y la comprobación
dice si quedó atrás. **No agrupa ni decide** de qué habla un hallazgo: eso es
leer. Junta en un archivo lo que está repartido en decenas.
"""
import os
import re

from ..comun import AVISO, Hallazgo, Proyecto
from ..validadores.base import Validador

RESUMENES = os.path.join("historico-chat", "resumenes")
INDICE = os.path.join(RESUMENES, "indice-tematico.md")

_HALLAZGO = re.compile(r"^###\s+(H-\d+)\s*[·:-]\s*(.+?)\s*$", re.M)
_TITULO = re.compile(r"^#\s+(.+?)\s*$", re.M)
_DIA = re.compile(r"^\d{4}-\d{2}-\d{2}$")

CABECERA = """# Índice temático del histórico

**Qué es.** Todos los hallazgos de todos los resúmenes, en un solo archivo, para
poder buscar por tema en vez de abrir sesión por sesión. Cada línea enlaza al
resumen donde vive.

**Lo genera un programa**, no se escribe a mano: `python validadores/validar.py
temas --aplicar`. Si se edita a mano, el próximo generado lo pisa.

**Qué no es.** No es una clasificación: no agrupa temas parecidos ni dice de qué
habla cada hallazgo. Es lo que ya estaba escrito, junto.

"""


class IndiceTematico(Validador):
    """El índice temático del histórico: lo genera, lo escribe y dice si quedó atrás."""

    nombre = "temas"
    regla = "EP-005·HU-001"
    descripcion = "índice temático del histórico · buscar por tema, no por fecha"

    def __init__(self, proyecto=None, archivos=None):
        super().__init__(proyecto or Proyecto.estandar(), archivos)

    @property
    def ruta(self):
        return os.path.join(self.proyecto.raiz, *INDICE.split(os.sep))

    def _leer(self, ruta):
        return self.archivos.leer(ruta)

    def _resumenes(self):
        """`[(fecha, archivo relativo, título de la sesión, [(id, tema)])]` por resumen."""
        carpeta = os.path.join(self.proyecto.raiz, *RESUMENES.split(os.sep))
        salida = []
        if not os.path.isdir(carpeta):
            return salida
        for dia in sorted(os.listdir(carpeta)):
            ruta_dia = os.path.join(carpeta, dia)
            if not os.path.isdir(ruta_dia) or not _DIA.match(dia):
                continue
            for nombre in sorted(os.listdir(ruta_dia)):
                if not nombre.endswith(".md") or nombre.upper() == "README.MD":
                    continue
                texto = self._leer(os.path.join(ruta_dia, nombre))
                titulo = _TITULO.search(texto)
                salida.append((dia, "%s/%s" % (dia, nombre),
                               titulo.group(1).strip() if titulo else nombre[:-3],
                               _HALLAZGO.findall(texto)))
        return salida

    def generar(self):
        """El texto del índice, sin escribirlo."""
        datos = self._resumenes()
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

    def escribir(self):
        """Escribe el índice y devuelve su ruta."""
        ruta = self.ruta
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(self.generar())
        return ruta

    def validar(self):
        """¿El índice existe y dice lo que dicen los resúmenes de hoy?"""
        ruta = self.ruta
        esperado = self.generar()
        if not os.path.isfile(ruta):
            return [Hallazgo(AVISO, ruta, 0,
                             "falta el índice temático — se genera con "
                             "`validar.py temas --aplicar`")]
        if self._leer(ruta) != esperado:
            return [Hallazgo(AVISO, ruta, 0,
                             "el índice temático quedó atrás de los resúmenes — "
                             "se regenera con `validar.py temas --aplicar`")]
        return []

    def linea_resumen(self):
        datos = self._resumenes()
        if not datos:
            return ""
        total = sum(len(h) for _, _, _, h in datos)
        mudos = sum(1 for _, _, _, h in datos if not h)
        return ("Resúmenes: %d · hallazgos indexados: %d · resúmenes sin ningún "
                "hallazgo: %d" % (len(datos), total, mudos))
