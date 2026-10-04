"""`08·T4` y `08·T3` · Pruebas aisladas y deterministas.

T4: las pruebas corren contra una base efímera o dedicada, nunca contra datos
reales. T3: corren en cualquier orden y dan siempre lo mismo: nada de azar ni
reloj sin fijar.

En Laravel se comprueba en `phpunit.xml` (la base y el orden) y en los archivos
de prueba (las fuentes de azar). Django y pytest crean la base de prueba de
fábrica, así que su aislamiento lo garantiza el marco. Todo es aviso.
"""
import os
import re

from ..comun import AVISO, Git, Hallazgo
from .codigo import ValidadorDeCodigo

_ENV = re.compile(r'<env\s+name="([^"]+)"\s+value="([^"]*)"')
_EXEC_ORDER = re.compile(r'executionOrder\s*=\s*"([^"]*)"')
_ES_PRUEBA = re.compile(r"(^|/)(tests?|spec)/|(Test|Spec)\.[a-z]+$|(^|/)test_[^/]+\.py$")
# `uniqid` queda fuera a propósito: da datos únicos y la prueba sigue siendo
# determinista. Se marcan el azar de valores y el reloj, que sí rompen lo esperado.
_AZAR = re.compile(r"\b(mt_rand|rand|array_rand|microtime|shuffle)\s*\(")


class PruebasAisladas(ValidadorDeCodigo):
    """Avisa de pruebas contra una base real, sin orden aleatorio o con azar sin fijar."""

    nombre = "aislamiento"
    regla = "08·T3, 08·T4"
    descripcion = "pruebas aisladas y deterministas"

    def validar(self):
        repos = self.proyecto.repositorios()
        if not repos:
            return [Hallazgo(AVISO, self.proyecto.raiz, 0, "no hay repositorios git que revisar")]
        hallazgos = []
        for repo in repos:
            hallazgos += self._revisar_phpunit_de(repo)
        return hallazgos + super().validar()

    def aplica_a(self, donde):
        return bool(_ES_PRUEBA.search(donde))

    def revisar_texto(self, texto, donde=""):
        return [Hallazgo(AVISO, donde, n,
                         "fuente de azar/tiempo (`%s`) en una prueba — T3: fijar semilla/reloj "
                         "o usar dobles (evita pruebas inestables)" % fuente)
                for n, fuente in self.fuentes_de_azar(texto)]

    @staticmethod
    def fuentes_de_azar(texto):
        """`[(línea, fuente)]` de azar o reloj en un archivo de prueba."""
        return [(n, m.group(1)) for n, linea in enumerate(texto.splitlines(), 1)
                for m in [_AZAR.search(linea)] if m]

    @staticmethod
    def motivo_de_la_base(texto, hay_env_testing=False):
        """Por qué el `phpunit.xml` no asegura una base efímera, o `None`."""
        base = dict(_ENV.findall(texto)).get("DB_DATABASE")
        if base is not None:
            if base == ":memory:" or "test" in base.lower():
                return None
            return ("las pruebas apuntan a `DB_DATABASE=%s`, que no parece efímera ni dedicada "
                    "(T4: usar `:memory:` o una BD de test)" % base)
        if hay_env_testing:
            return None
        return ("`phpunit.xml` no fija una BD de pruebas aislada; podría usar la real "
                "(T4: fijar `DB_DATABASE=:memory:` o un `.env.testing`)")

    @staticmethod
    def motivo_del_orden(texto):
        """Por qué la suite no corre en orden aleatorio, o `None`."""
        m = _EXEC_ORDER.search(texto)
        if m and "random" in m.group(1).lower():
            return None
        return ("la suite no se corre en orden aleatorio "
                "(T3: `executionOrder=\"random\"` para que no dependan del orden)")

    def _revisar_phpunit_de(self, repo):
        etiqueta = os.path.relpath(repo, self.proyecto.raiz).replace("\\", "/")
        prefijo = "" if etiqueta == "." else etiqueta + "/"
        versionados = set(Git(repo).versionados())
        hallazgos = []
        for relativa in versionados:
            if os.path.basename(relativa).lower() != "phpunit.xml":
                continue
            carpeta = os.path.dirname(relativa)
            hay_env = ("%s/.env.testing" % carpeta).lstrip("/") in versionados \
                or os.path.isfile(os.path.join(repo, carpeta, ".env.testing"))
            texto = self.archivos.leer(os.path.join(repo, relativa))
            for motivo in (self.motivo_de_la_base(texto, hay_env), self.motivo_del_orden(texto)):
                if motivo:
                    hallazgos.append(Hallazgo(AVISO, prefijo + relativa, 0, motivo))
        return hallazgos
