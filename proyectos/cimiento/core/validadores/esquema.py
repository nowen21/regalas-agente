"""`03·D1`, `03·D3` y `14·EST2` · Integridad del esquema en las migraciones.

  D1   · toda clave foránea con política de borrado explícita.
  D3   · una columna obligatoria nueva en una tabla existente trae `default`.
  EST2 · ningún identificador pasa el límite del motor (típico 64 en MySQL).

Se leen migraciones Laravel y SQL crudo. Django no se revisa para D1 porque su
ORM exige `on_delete` de fábrica. Todo es aviso: puede haber un motivo legítimo.

`LectorDeEsquema` sabe qué tablas crea una migración y con qué columnas; lo usan
también los validadores de nombres y de entidades.
"""
import os
import re

from ..comun import AVISO, Hallazgo
from .base import Validador
from .codigo import RecorridoDeCodigo
from .migraciones import RecorridoDeMigraciones

LEGIBLES = (".php", ".sql")

# D1
_FK_LARAVEL = re.compile(r"->\s*(foreign|foreignId|foreignIdFor|constrained)\b")
_POLITICA_LARAVEL = re.compile(r"(?i)on_?delete")
_REFERENCES = re.compile(r"(?i)\breferences\b")
_ON_DELETE_SQL = re.compile(r"(?i)\bon\s+delete\b")

# D3 · solo en un ALTER (`Schema::table` sin `Schema::create`): en una tabla nueva
# NOT NULL está bien, porque no hay filas que romper.
_COLUMNA_LARAVEL = re.compile(
    r"->\s*(string|char|text|longText|mediumText|integer|tinyInteger|"
    r"smallInteger|mediumInteger|bigInteger|unsignedBigInteger|unsignedInteger|"
    r"boolean|date|dateTime|dateTimeTz|timestamp|time|year|decimal|float|double|"
    r"json|jsonb|enum|uuid|ulid|foreignId|foreignUlid|ipAddress|binary)\s*\(")
_D3_SEGURO = re.compile(r"->\s*(nullable|default|change|useCurrent|autoIncrement)\b")
_ADD_NOT_NULL_SQL = re.compile(r"(?i)\bADD\b(?:\s+COLUMN)?\b[^;,]*\bNOT\s+NULL\b")
_DEFAULT_SQL = re.compile(r"(?i)\bDEFAULT\b")

# EST2
_LIMITE = 64
_IDENTIFICADOR = re.compile(r"['\"]([a-z_][a-z0-9_]{%d,})['\"]" % _LIMITE)

# Lectura del CREATE
_CREATE_LARAVEL = re.compile(r"Schema::create\(\s*['\"]([^'\"]+)['\"]")
_BLOQUE_LARAVEL = re.compile(r"Schema::\w+\(")
_CREATE_SQL = re.compile(
    r"(?is)\bCREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?[`\"\[]?([\w.]+)[`\"\]]?\s*\((.*?)\)[^;()]*;")
_COLUMNA_PHP = re.compile(r"->\s*([A-Za-z]+)\s*\(\s*['\"]([^'\"]+)['\"]")
_SIN_NOMBRE_PHP = re.compile(r"->\s*(timestamps|timestampsTz|softDeletes|"
                             r"softDeletesTz|rememberToken|id|ulid|uuid)\s*\(\s*\)")
_EXPANDIDAS = {
    "timestamps": [("created_at", "timestamp"), ("updated_at", "timestamp")],
    "timestampsTz": [("created_at", "timestamp"), ("updated_at", "timestamp")],
    "softDeletes": [("deleted_at", "timestamp")],
    "softDeletesTz": [("deleted_at", "timestamp")],
    "rememberToken": [("remember_token", "string")],
    "id": [("id", "bigIncrements")],
    "ulid": [("ulid", "ulid")],
    "uuid": [("uuid", "uuid")],
}
_NO_ES_COLUMNA = {
    "default", "comment", "index", "unique", "primary", "constrained", "on",
    "references", "onDelete", "onUpdate", "after", "change", "nullable",
    "unsigned", "charset", "collation", "storedAs", "virtualAs", "from", "table",
}
_CONSTRAINT_SQL = re.compile(r"(?i)^\s*(PRIMARY|UNIQUE|KEY|INDEX|CONSTRAINT|FOREIGN|CHECK|FULLTEXT|SPATIAL)\b")
_COLUMNA_SQL = re.compile(r"^\s*[`\"\[]?(\w+)[`\"\]]?\s+([A-Za-z]+)")


def _extension(ruta):
    return os.path.splitext(ruta.lower())[1]


class LectorDeEsquema:
    """Qué tablas crea una migración y con qué columnas. Solo el `CREATE`: un
    `ALTER` dice qué le cambió a la tabla, no qué tiene."""

    @staticmethod
    def tablas_creadas(ruta, texto):
        """`[(tabla, cuerpo, línea)]`; el cuerpo es donde se definen sus columnas."""
        salida = []
        if _extension(ruta) == ".php":
            for m in _CREATE_LARAVEL.finditer(texto):
                siguiente = _BLOQUE_LARAVEL.search(texto, m.end())
                fin = siguiente.start() if siguiente else len(texto)
                salida.append((m.group(1), texto[m.end():fin], RecorridoDeCodigo.linea_de(texto, m.start())))
        elif _extension(ruta) == ".sql":
            for m in _CREATE_SQL.finditer(texto):
                salida.append((m.group(1), m.group(2), RecorridoDeCodigo.linea_de(texto, m.start())))
        return salida

    @staticmethod
    def columnas_de(cuerpo, ruta):
        """`[(nombre, tipo)]`. Las que el marco agrega sin nombrarlas
        (`timestamps()`, `softDeletes()`) se expanden: si no, una tabla que las
        usa parecería no tener auditoría."""
        salida = []
        if _extension(ruta) == ".php":
            salida += [(m.group(2), m.group(1)) for m in _COLUMNA_PHP.finditer(cuerpo)
                       if m.group(1) not in _NO_ES_COLUMNA]
            for m in _SIN_NOMBRE_PHP.finditer(cuerpo):
                salida += _EXPANDIDAS[m.group(1)]
        elif _extension(ruta) == ".sql":
            for linea in cuerpo.splitlines():
                if not _CONSTRAINT_SQL.match(linea):
                    m = _COLUMNA_SQL.match(linea)
                    if m:
                        salida.append((m.group(1), m.group(2).lower()))
        return salida


class IntegridadDeEsquema(Validador):
    """Avisa de claves foráneas sin política, columnas obligatorias sin `default`
    e identificadores demasiado largos."""

    nombre = "esquema"
    regla = "03·D1, 03·D3, 14·EST2"
    descripcion = "FK con política de borrado, default y longitud"

    def validar(self):
        if not self.proyecto.repositorios():
            return [Hallazgo(AVISO, self.proyecto.raiz, 0, "no hay repositorios git que revisar")]
        return [Hallazgo(AVISO, mostrada, linea, motivo)
                for mostrada, ruta, texto, _ in RecorridoDeMigraciones(self.proyecto, self.archivos).migraciones(LEGIBLES)
                for linea, motivo in self.revisar(ruta, texto)]

    @staticmethod
    def _sentencia(texto, posicion):
        """La sentencia PHP que contiene `posicion`, entre `;` y `;`."""
        inicio = texto.rfind(";", 0, posicion) + 1
        fin = texto.find(";", posicion)
        return inicio, (fin if fin != -1 else len(texto))

    @classmethod
    def revisar(cls, ruta, texto):
        """El núcleo puro: `[(línea, motivo)]` de una migración."""
        linea_de = RecorridoDeCodigo.linea_de
        hallazgos = []
        if _extension(ruta) == ".php":
            es_alter = "Schema::table(" in texto and "Schema::create(" not in texto
            vistas_fk, vistas_d3 = set(), set()
            for m in _FK_LARAVEL.finditer(texto):
                inicio, fin = cls._sentencia(texto, m.start())
                if inicio in vistas_fk:
                    continue                        # una sentencia, un hallazgo
                vistas_fk.add(inicio)
                if not _POLITICA_LARAVEL.search(texto[inicio:fin]):
                    hallazgos.append((linea_de(texto, m.start()),
                                      "clave foránea sin política de borrado explícita (D1: FK con `onDelete`)"))
            if es_alter:
                for m in _COLUMNA_LARAVEL.finditer(texto):
                    inicio, fin = cls._sentencia(texto, m.start())
                    if inicio in vistas_d3:
                        continue
                    vistas_d3.add(inicio)
                    if not _D3_SEGURO.search(texto[inicio:fin]):
                        hallazgos.append((linea_de(texto, m.start()),
                                          "columna nueva obligatoria sin `default` en un ALTER "
                                          "(D3: rompe las filas existentes)"))
        elif _extension(ruta) == ".sql":
            for m in _REFERENCES.finditer(texto):
                if not _ON_DELETE_SQL.search(texto[m.end():m.end() + 140]):
                    hallazgos.append((linea_de(texto, m.start()),
                                      "`REFERENCES` sin `ON DELETE` (D1: FK con política de borrado)"))
            for m in _ADD_NOT_NULL_SQL.finditer(texto):
                if not _DEFAULT_SQL.search(m.group(0)):
                    hallazgos.append((linea_de(texto, m.start()),
                                      "`ADD ... NOT NULL` sin `DEFAULT` (D3: rompe las filas existentes)"))
        for m in _IDENTIFICADOR.finditer(texto):
            hallazgos.append((linea_de(texto, m.start()),
                              "identificador de %d caracteres, sobre el límite habitual de %d "
                              "(EST2: longitud)" % (len(m.group(1)), _LIMITE)))
        return hallazgos
