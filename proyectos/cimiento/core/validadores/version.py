"""Desfase de versión del estándar (pendiente 04).

Compara la versión del estándar (su archivo `VERSION`) con la que **declara** el
proyecto en su `CLAUDE.md`. Si el proyecto quedó por detrás, **avisa** y no
migra: subir es decisión del usuario, y las fases cerradas quedan selladas con
su versión.

El desfase a secas es AVISO. La excepción es `02·F22`: con una regla
**derogada** sin adoptar dentro del desfase, el proyecto no abre ni cierra fase,
y eso sí es FALLA. Esa parte es `validar_fase`, que llama el recorrido de fases.
"""
import os
import re

from ..comun import AVISO, FALLA, Hallazgo, Proyecto
from .base import Validador

# 'X.Y.Z' en la línea "Versión del estándar adoptada: X.Y.Z".
_ADOPTADA = re.compile(
    r"(?i)versi[oó]n\s+del\s+est[aá]ndar\s+adoptada[^\n]*?(\d+\.\d+\.\d+)")

# `## 31.9.0 — 2026-08-22`: la cabecera de una entrada del registro.
_ENTRADA_DEL_REGISTRO = re.compile(r"^##\s+(\d+\.\d+\.\d+)\b", re.M)

# La entrada con su tipo y su título, **en cualquiera de los dos órdenes**: el
# registro se escribió primero con el tipo delante y después con el título
# delante (`M17`). Leyendo una sola forma, el lector dejó de ver todo lo
# posterior a la 34.2.0 y el aviso de qué cambió salía vacío.
_ENTRADA_CON_TIPO = re.compile(
    r"^##\s+(\d+\.\d+\.\d+)\b[^\n]*\n+"
    r"(?:\*\*(MAYOR|MENOR|PARCHE)\*\*[^\n]*\n+\*\*([^*]{10,90})"
    r"|\*\*([^*]{10,90})[^\n]*(?:\n(?!##\s)[^\n]*)*?\*\*(MAYOR|MENOR|PARCHE)\*\*)",
    re.M)

_NOMBRE_DE_ADOPCION = re.compile(r"^\d{4}-\d{2}-\d{2}-(\d+\.\d+\.\d+)\.md$")

# El encabezado de una regla derogada (`20·M11`). Solo la línea del encabezado:
# las tablas de los índices y los ejemplos del molde repiten la marca y no son reglas.
_ENCABEZADO_DEROGADA = re.compile(
    r"^##\s+(\S+)\s*·[^\n]*?\[DEROGADA\s+en\s+(\d+\.\d+\.\d+)\s*(?:→|->)\s*ver\s+([^\]`]+)\]",
    re.M)


def _leer(ruta):
    try:
        with open(ruta, encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError:
        with open(ruta, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def _de_la_base(estandar):
    """`EP-026·HU-008` · Las versiones del estándar en la base si está congelado; si no, o sin base, []."""
    from ..enganches.niveles import BaseSinRespuesta
    from ..estandar import congelado

    if not estandar or not congelado.congelada(estandar):
        return []
    try:
        return congelado.versiones_en_la_base(estandar)
    except BaseSinRespuesta:
        return []


def _tupla(v):
    return tuple(int(x) for x in v.split("."))


class VersionDelEstandar(Validador):
    """La versión que el proyecto declara, contra el estándar y su registro."""

    nombre = "version"
    regla = "02·F22"
    descripcion = "la versión del estándar que declara el proyecto"

    def __init__(self, proyecto, archivos=None, estandar=None):
        super().__init__(proyecto, archivos)
        self.estandar = estandar or Proyecto.estandar()

    # ── lo que se lee del estándar ───────────────────────────────────────

    @staticmethod
    def vigente(estandar=None):
        """La versión del estándar (primer renglón de `VERSION`), o None. Con el
        estándar congelado (`EP-026·HU-008`), la última de la base."""
        estandar = estandar or Proyecto.estandar()
        en_base = _de_la_base(estandar)
        if en_base:
            return en_base[0]
        cabeza = _leer(os.path.join(estandar, "VERSION")).strip().splitlines()
        return cabeza[0].strip() if cabeza else None

    def version_estandar(self):
        return self.vigente(self.estandar)

    def versiones_publicadas(self):
        """Las versiones que el `CHANGELOG.md` publica: `{"31.9.0", ...}`.

        **Del registro y no de `VERSION`**: la pregunta no es cuál es la última
        sino si el número que un proyecto declara existió alguna vez.
        """
        ruta = os.path.join(self.estandar, "CHANGELOG.md")
        # `EP-026·HU-008` · Con el estándar congelado, también las de la base.
        en_base = set(_de_la_base(self.estandar))
        if not os.path.isfile(ruta):
            return en_base
        return set(_ENTRADA_DEL_REGISTRO.findall(_leer(ruta))) | en_base

    def derogaciones(self, base=None):
        """Las reglas derogadas: `[(versión, regla, reemplazo)]`.

        Se leen de la marca del encabezado (`20·M11`), que es dato estructurado;
        nombrar la palabra en el `CHANGELOG.md` no deroga nada.
        """
        base = base or os.path.join(self.estandar, "base")
        encontradas = []
        for carpeta, subcarpetas, archivos in os.walk(base):
            subcarpetas[:] = [s for s in subcarpetas if not s.startswith(".")]
            for nombre in archivos:
                if not nombre.endswith(".md"):
                    continue
                for regla, version, reemplazo in _ENCABEZADO_DEROGADA.findall(
                        _leer(os.path.join(carpeta, nombre))):
                    entrada = (version, regla, reemplazo.strip())
                    if entrada not in encontradas:
                        encontradas.append(entrada)
        return sorted(encontradas, key=lambda e: (_tupla(e[0]), e[1]))

    def tramo(self, adoptada, estandar, raiz_estandar=None):
        """Qué versiones separan a las dos: `[(version, tipo, titulo)]`.

        **Al nivel de entrada del registro**: versión, tipo y título (decisión 24
        del pendiente de las 42 dudas). Menos no ayuda a decidir; más obligaría
        a mantener dos textos que dicen lo mismo.
        """
        ruta = os.path.join(raiz_estandar or self.estandar, "CHANGELOG.md")
        if not (adoptada and estandar and os.path.isfile(ruta)):
            return []
        desde, hasta = _tupla(adoptada), _tupla(estandar)
        salida = []
        for encontrada in _ENTRADA_CON_TIPO.finditer(_leer(ruta)):
            version = encontrada.group(1)
            # La forma que no casó deja sus grupos vacíos: se toma la que tenga algo.
            tipo = encontrada.group(2) or encontrada.group(5) or ""
            titulo = encontrada.group(3) or encontrada.group(4) or ""
            if desde < _tupla(version) <= hasta:
                salida.append((version, tipo, titulo.strip()))
        return salida

    # ── núcleo puro ──────────────────────────────────────────────────────

    @staticmethod
    def extraer_adoptada(texto):
        """La versión que el `CLAUDE.md` declara adoptada, o None (o sin llenar)."""
        m = _ADOPTADA.search(texto)
        return m.group(1) if m else None

    @staticmethod
    def comparar(adoptada, estandar):
        """Motivo del desfase, o None si está al día."""
        if not estandar:
            return None
        if not adoptada:
            return (f"el proyecto no declara qué versión del estándar sigue "
                    f"(el estándar va en v{estandar}) — fijarla en su CLAUDE.md")
        if _tupla(adoptada) < _tupla(estandar):
            return (f"el proyecto declara v{adoptada}, el estándar va en v{estandar}: "
                    f"subir es decisión del usuario; las fases cerradas quedan selladas")
        return None

    @staticmethod
    def sin_adoptar(adoptada, estandar, derogadas):
        """Las derogaciones publicadas **después** de la versión declarada y
        hasta la vigente. Sin versión declarada no se puede decidir: vacío."""
        if not adoptada or not estandar:
            return []
        desde, hasta = _tupla(adoptada), _tupla(estandar)
        return [d for d in derogadas if desde < _tupla(d[0]) <= hasta]

    @staticmethod
    def ultima_adopcion(raiz):
        """La versión del último registro de `documentacion/versiones/`, o ""."""
        carpeta = os.path.join(os.path.abspath(raiz), "documentacion", "versiones")
        if not os.path.isdir(carpeta):
            return ""
        encontradas = [m.group(1) for m in map(_NOMBRE_DE_ADOPCION.match, os.listdir(carpeta)) if m]
        return max(encontradas, key=_tupla) if encontradas else ""

    @staticmethod
    def resumen_del_tramo(entradas):
        """El tramo en una línea. **Primero si alguna obliga a migrar**, que es
        lo único que cambia qué hacer; después cuántas van y los títulos de las
        tres más recientes."""
        if not entradas:
            return ""
        mayores = [v for v, tipo, _ in entradas if tipo.upper() == "MAYOR"]
        partes = []
        if mayores:
            partes.append("**%d obliga%s a migrar** (v%s)" % (
                len(mayores), "" if len(mayores) == 1 else "n", ", v".join(mayores[:3])))
        partes.append("van %d" % len(entradas) if len(entradas) != 1 else "va una versión")
        titulos = "; ".join(t.rstrip(".") for _, _, t in entradas[:3])
        if len(entradas) > 3:
            titulos += "; y %d más" % (len(entradas) - 3)
        return ". Qué cambió: %s. Lo último: %s" % (", ".join(partes), titulos)

    # ── las comprobaciones ───────────────────────────────────────────────

    def validar(self):
        raiz = self.proyecto.raiz
        est = self.version_estandar()
        claude = os.path.join(raiz, "CLAUDE.md")
        if not os.path.isfile(claude):
            return [Hallazgo(AVISO, raiz, 0,
                             "no se encontró CLAUDE.md; no se puede leer la versión adoptada")]
        adoptada = self.extraer_adoptada(_leer(claude))
        hallazgos = []

        # **Que la versión declarada exista.** Un número inventado mayor que la
        # vigente hacía concluir «al día» y apagaba el aviso (pendiente 82).
        publicadas = self.versiones_publicadas()
        if adoptada and publicadas and adoptada not in publicadas:
            hallazgos.append(Hallazgo(
                FALLA, "CLAUDE.md", 0,
                f"el proyecto declara la v{adoptada}, que no existe en el registro "
                f"de cambios del estándar — mientras el número sea falso, el aviso "
                f"de desfase no dice nada"))

        # **Que coincida con el último registro de adopción**: si no, una de las
        # dos está mal y no se sabe cuál sin mirar.
        ultima = self.ultima_adopcion(raiz)
        if adoptada and ultima and adoptada != ultima:
            hallazgos.append(Hallazgo(
                FALLA, "CLAUDE.md", 0,
                f"el proyecto declara la v{adoptada} y su último registro de "
                f"adopción dice v{ultima} — una de las dos está mal, y el aviso de "
                f"desfase se calcula sobre la declarada"))

        motivo = self.comparar(adoptada, est)
        if motivo:
            # **Y qué cambió entre las dos**, para poder decidir si subir.
            hallazgos.append(Hallazgo(AVISO, "CLAUDE.md", 0,
                                      motivo + self.resumen_del_tramo(self.tramo(adoptada, est))))
        return hallazgos

    def validar_fase(self):
        """`02·F22`: con una derogación sin adoptar, el proyecto no avanza de fase.
        Se cobra al abrir y al cerrar una fase, no en cualquier momento."""
        claude = os.path.join(self.proyecto.raiz, "CLAUDE.md")
        if not os.path.isfile(claude):
            return []
        pendientes = self.sin_adoptar(self.extraer_adoptada(_leer(claude)),
                                      self.version_estandar(), self.derogaciones())
        if not pendientes:
            return []
        detalle = " · ".join(f"{regla} (derogada en {ver} → {reemplazo})"
                             for ver, regla, reemplazo in pendientes)
        return [Hallazgo(
            FALLA, "CLAUDE.md", 0,
            f"hay derogaciones sin adoptar y ninguna fase se abre ni se cierra hasta "
            f"adoptarlas (F22): {detalle}. Se abre una fase por cada HU que implementaba "
            f"la regla derogada, y al cerrarla se sube la versión declarada")]
