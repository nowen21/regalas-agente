"""`04·S3` y `04·S5` · Nada se arma pegando entrada, y la sesión no se debilita.

S3: consultas y comandos no se construyen concatenando entrada, y no se vuelca
todo el payload al modelo. S5 (lo comprobable): nadie apaga a mano `HttpOnly`
o `Secure` de la cookie de sesión.

Todo es aviso y heurístico: una cadena SQL con una tabla fija no es inyección;
lo confirma una persona.
"""
import re

from ..comun import AVISO, Hallazgo
from .codigo import RecorridoDeCodigo, ValidadorDeCodigo

# SQL de verdad: la cadena empieza con un verbo de consulta y se concatena con
# una variable (no el punto de una frase en un comentario).
_SQL_EN_CADENA = re.compile(
    r"(?i)['\"]\s*(SELECT|INSERT\s+INTO|UPDATE|DELETE\s+FROM|REPLACE\s+INTO)\b")
_CONCAT_VAR = re.compile(r"['\"]\s*\.\s*\$\w|\$\w+\s*\.\s*['\"]|['\"]\s*\+\s*\w")

# Llamada a shell y, en la misma línea, una concatenación o interpolación.
_SHELL = re.compile(
    r"\b(exec|shell_exec|system|passthru|popen|proc_open)\s*\(|"
    r"\bos\.system\s*\(|\bsubprocess\.\s*(call|run|Popen)\s*\(")
_CONCAT_O_INTERP = re.compile(r"[.+]\s*\$?\w|f['\"]|\$\{")

_GUARDED_VACIO = re.compile(r"\$guarded\s*=\s*\[\s*\]")
_TODO_AL_MODELO = re.compile(
    r"(->|::)\s*(create|update|fill|forceCreate|forceFill)\s*\(\s*\$\w+->\s*all\(\)")
_COOKIE_INSEGURA = re.compile(
    r"(?i)['\"]?(http_?only|secure|cookie_httponly|cookie_secure)['\"]?\s*(=>|:|=)\s*(false|0)\b")

_EN_EL_TEXTO = (
    (_GUARDED_VACIO, "asignación masiva sin freno (`$guarded = []`) — S3"),
    (_TODO_AL_MODELO, "todo el payload al modelo (`->…($req->all())`) — S3: declarar asignables"),
    (_COOKIE_INSEGURA, "flag de cookie de sesión apagado (`HttpOnly`/`Secure`) — S5"),
)


class InyeccionYSesion(ValidadorDeCodigo):
    """Avisa de SQL y shell armados por concatenación, asignación masiva y cookies débiles."""

    nombre = "seguridad"
    regla = "04·S3, 04·S5"
    descripcion = "concatenación, asignación masiva y cookies de sesión"

    def revisar_texto(self, texto, donde=""):
        hallazgos = []
        for n, linea in enumerate(texto.splitlines(), 1):
            if _SQL_EN_CADENA.search(linea) and _CONCAT_VAR.search(linea):
                hallazgos.append(Hallazgo(
                    AVISO, donde, n, "consulta SQL armada por concatenación — S3: usar parámetros/ORM"))
            if _SHELL.search(linea) and _CONCAT_O_INTERP.search(linea):
                hallazgos.append(Hallazgo(
                    AVISO, donde, n, "comando de shell armado con entrada — S3: separar comando y argumentos"))
        for patron, motivo in _EN_EL_TEXTO:
            for m in patron.finditer(texto):
                hallazgos.append(Hallazgo(AVISO, donde, RecorridoDeCodigo.linea_de(texto, m.start()), motivo))
        return hallazgos
