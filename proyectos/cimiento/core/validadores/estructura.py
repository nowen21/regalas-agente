"""`14·EST1` y `14·EST2` · Dónde vive el código y cómo se llama.

Las dos reglas piden que el nombre y la ubicación sean **adivinables**. Ninguna
se comprueba contra un gusto propio: el proyecto declara su convención en
`.agente/mapeo-nombres.md` y su dominio en `.agente/dominio.md`, y se compara el
código contra eso.

  EST1 · cada módulo declarado existe donde la convención dice, y ningún módulo
         del código queda sin declarar.
  EST2 · tablas, columnas, clases, claves foráneas, booleanos y fechas de evento
         siguen la convención declarada.

Sin declaración no corre; una clave en `libre` apaga su comprobación, y lo que
cae en `legacy.ignorar` (`14·EST3`) no se mira. Todo es aviso.
"""
import os
import re

from ..comun import AVISO, Git, Hallazgo
from .base import Validador
from .codigo import RecorridoDeCodigo
from .declaracion import DOMINIO, CONVENCIONES, Declaracion
from .esquema import LEGIBLES, LectorDeEsquema
from .migraciones import RecorridoDeMigraciones

CASOS = {
    "snake_case": re.compile(r"^[a-z][a-z0-9]*(_[a-z0-9]+)*$"),
    "SCREAMING_SNAKE": re.compile(r"^[A-Z][A-Z0-9]*(_[A-Z0-9]+)*$"),
    "camelCase": re.compile(r"^[a-z][a-zA-Z0-9]*$"),
    "PascalCase": re.compile(r"^[A-Z][a-zA-Z0-9]*$"),
    "kebab-case": re.compile(r"^[a-z][a-z0-9]*(-[a-z0-9]+)*$"),
}

_CLASE = re.compile(
    r"(?m)^\s*(?:export\s+)?(?:public\s+|final\s+|abstract\s+|sealed\s+|"
    r"internal\s+|static\s+)*(?:class|interface|trait|enum|struct)\s+([A-Za-z_]\w*)")
_FK_PHP = re.compile(r"->\s*(?:foreignId|foreignUlid|foreignUuid)\s*\(\s*['\"]([^'\"]+)")
_FK_PHP_EXPLICITA = re.compile(r"->\s*foreign\s*\(\s*['\"]([^'\"]+)")
_FK_SQL = re.compile(r"(?i)FOREIGN\s+KEY\s*\(\s*[`\"\[]?(\w+)")
_TIPOS_BOOL = {"boolean", "bool", "tinyint"}
_TIPOS_FECHA = {"timestamp", "timestamptz", "datetime", "dateTime", "dateTimeTz", "timestampTz"}


def _ni(valores, forma):
    return " ni ".join(forma % v for v in valores)


class ConvencionDeNombres(Validador):
    """Compara nombres y ubicaciones contra la convención que el proyecto declaró."""

    nombre = "estructura"
    regla = "14·EST1, 14·EST2"
    descripcion = "módulos y nombres según la convención declarada"

    def validar(self):
        d = Declaracion.leer(self.proyecto, self.archivos)
        if not d.hay_algo():
            return [Hallazgo(AVISO, self.proyecto.raiz, 0,
                             "el proyecto no declara su convención en `%s` ni su dominio en `%s`: "
                             "EST1 y EST2 se quedan en criterio del agente" % (CONVENCIONES, DOMINIO))]
        return self._modulos(d) + self._migraciones(d) + self._clases(d)

    @staticmethod
    def cumple_caso(nombre, caso):
        """¿`nombre` está escrito en ese caso? Un caso que no se reconoce da `True`:
        el problema es la declaración, y eso lo reporta el validador de declaración."""
        patron = CASOS.get(caso)
        return True if not patron else bool(patron.match(nombre))

    def _modulos_en_el_codigo(self, patron):
        """`{nombre en minúsculas: ruta mostrada}` de los módulos que tiene el código,
        leídos de lo versionado: lo que git no conoce no es del proyecto todavía."""
        partes = patron.replace("\\", "/").strip("/").split("/")
        if "<modulo>" not in partes:
            return {}
        indice = partes.index("<modulo>")
        prefijo = partes[:indice]
        encontrados = {}
        for repo in self.proyecto.repositorios():
            marca = self.proyecto.prefijo_de(repo)
            for archivo in Git(repo).versionados():
                trozos = archivo.split("/")
                if len(trozos) > indice and trozos[:indice] == prefijo:
                    encontrados.setdefault(trozos[indice].lower(), marca + "/".join(trozos[:indice + 1]))
        return encontrados

    def _modulos(self, d):
        patron = d.convencion("modulos.ruta")
        if not patron:
            return []
        dominio = self.proyecto.ruta(DOMINIO)
        en_codigo = self._modulos_en_el_codigo(patron)
        declarados = {m.nombre.lower(): m for m in d.modulos}
        hallazgos = []
        for nombre, modulo in sorted(declarados.items()):
            if nombre not in en_codigo:
                hallazgos.append(Hallazgo(AVISO, dominio, 0,
                                          "el módulo `%s` está declarado pero no tiene código en `%s` (EST1)"
                                          % (modulo.nombre, patron.replace("<modulo>", modulo.nombre))))
            elif modulo.carpeta and modulo.carpeta.strip("/") not in en_codigo[nombre]:
                hallazgos.append(Hallazgo(AVISO, dominio, 0,
                                          "el módulo `%s` declara la carpeta `%s` y su código está en `%s` (EST1)"
                                          % (modulo.nombre, modulo.carpeta, en_codigo[nombre])))
        hallazgos += [Hallazgo(AVISO, ruta, 0, "`%s` encaja con la convención de módulos y no está "
                                               "declarado en `%s` (EST1 · 13·DOC13)" % (ruta, DOMINIO))
                      for nombre, ruta in sorted(en_codigo.items()) if nombre not in declarados]
        return hallazgos

    @staticmethod
    def _fks_de(cuerpo, ruta):
        if os.path.splitext(ruta.lower())[1] == ".php":
            return ([m.group(1) for m in _FK_PHP.finditer(cuerpo)]
                    + [m.group(1) for m in _FK_PHP_EXPLICITA.finditer(cuerpo)])
        return [m.group(1) for m in _FK_SQL.finditer(cuerpo)]

    def _migraciones(self, d):
        caso_tabla, caso_columna = d.convencion("tablas.caso"), d.convencion("columnas.caso")
        sufijos_fk, prefijos_bool = d.lista("fk.sufijo"), d.lista("booleanos.prefijo")
        sufijos_fecha = d.lista("timestamps.sufijo")
        if not any((caso_tabla, caso_columna, sufijos_fk, prefijos_bool, sufijos_fecha)):
            return []
        hallazgos = []
        for mostrada, ruta, texto, _ in RecorridoDeMigraciones(self.proyecto, self.archivos).migraciones(LEGIBLES):
            if d.ignorado(mostrada):
                continue
            for tabla, cuerpo, linea in LectorDeEsquema.tablas_creadas(ruta, texto):
                aviso = lambda mensaje: hallazgos.append(Hallazgo(AVISO, mostrada, linea, mensaje))
                if caso_tabla and not self.cumple_caso(tabla, caso_tabla):
                    aviso("la tabla `%s` no sigue `%s`, la convención declarada (EST2)" % (tabla, caso_tabla))
                fks = {n.lower() for n in self._fks_de(cuerpo, ruta)}
                for nombre, tipo in LectorDeEsquema.columnas_de(cuerpo, ruta):
                    if caso_columna and not self.cumple_caso(nombre, caso_columna):
                        aviso("la columna `%s.%s` no sigue `%s` (EST2)" % (tabla, nombre, caso_columna))
                    es_fk = nombre.lower() in fks or tipo.lower().startswith("foreign")
                    if es_fk and sufijos_fk and not nombre.endswith(tuple(sufijos_fk)):
                        aviso("la clave foránea `%s.%s` no termina en %s (EST2)"
                              % (tabla, nombre, _ni(sufijos_fk, "`%s`")))
                    if tipo.lower() in _TIPOS_BOOL and prefijos_bool and not nombre.startswith(tuple(prefijos_bool)):
                        aviso("la columna booleana `%s.%s` no empieza por %s (EST2)"
                              % (tabla, nombre, _ni(prefijos_bool, "`%s`")))
                    if (tipo in _TIPOS_FECHA or tipo.lower() in _TIPOS_FECHA) and sufijos_fecha \
                            and not nombre.endswith(tuple(sufijos_fecha)):
                        aviso("la fecha de evento `%s.%s` no termina en %s (EST2)"
                              % (tabla, nombre, _ni(sufijos_fecha, "`%s`")))
        return hallazgos

    def _clases(self, d):
        caso = d.convencion("clases.caso")
        if not caso:
            return []
        return [Hallazgo(AVISO, ruta, RecorridoDeCodigo.linea_de(texto, m.start(1)),
                         "la clase `%s` no sigue `%s`, la convención declarada (EST2)" % (m.group(1), caso))
                for ruta, texto in RecorridoDeCodigo(self.proyecto, self.archivos).archivos()
                if not d.ignorado(ruta)
                for m in _CLASE.finditer(texto) if not self.cumple_caso(m.group(1), caso)]
