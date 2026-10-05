"""`10·DEP2` · El lockfile está y está versionado.

Es el complemento de `09·G3`, que pide no versionar lo **instalado**: acá se
pide versionar la **declaración** que lo reconstruye. Si hay un manifiesto
versionado (`composer.json`, `package.json`…), su lockfile hermano también.

Todo es aviso: un paquete sin dependencias o un `pyproject.toml` que es solo
configuración de construcción no necesitan lockfile.
"""
import os

from ..comun import AVISO, Git, Hallazgo
from .base import Validador

# Manifiesto, lockfiles que lo satisfacen (basta uno) y ecosistema.
ECOSISTEMAS = [
    ("composer.json", ("composer.lock",), "Composer/PHP"),
    ("package.json", ("package-lock.json", "yarn.lock", "pnpm-lock.yaml"), "npm/Node"),
    ("Pipfile", ("Pipfile.lock",), "Pipenv"),
    ("pyproject.toml", ("poetry.lock", "pdm.lock", "uv.lock"), "Python"),
    ("Gemfile", ("Gemfile.lock",), "Bundler/Ruby"),
    ("go.mod", ("go.sum",), "Go"),
    ("Cargo.toml", ("Cargo.lock",), "Cargo/Rust"),
]


def _es_instalado(ruta):
    """El manifiesto de una dependencia instalada no es la raíz del proyecto."""
    return any(c in "/" + ruta for c in ("/vendor/", "/node_modules/"))


class LockfileVersionado(Validador):
    """Avisa del manifiesto que no tiene su lockfile versionado al lado."""

    nombre = "dependencias"
    regla = "10·DEP2"
    descripcion = "lockfile presente y versionado"

    def validar(self):
        repos = self.proyecto.repositorios()
        if not repos:
            return [Hallazgo(AVISO, self.proyecto.raiz, 0, "no hay repositorios git que revisar")]
        hallazgos = []
        for repo in repos:
            hallazgos += self.revisar(Git(repo).versionados(), self.proyecto.prefijo_de(repo))
        return hallazgos

    @staticmethod
    def revisar(versionados, prefijo=""):
        """El núcleo puro: dados los archivos versionados, ¿falta algún lockfile?"""
        versionados = set(versionados)
        hallazgos = []
        for ruta in sorted(versionados):
            if _es_instalado(ruta):
                continue
            carpeta, nombre = os.path.split(ruta)
            for manifiesto, locks, ecosistema in ECOSISTEMAS:
                if nombre != manifiesto:
                    continue
                esperados = [os.path.join(carpeta, l).replace("\\", "/") for l in locks]
                if not any(e in versionados for e in esperados):
                    hallazgos.append(Hallazgo(AVISO, prefijo + ruta, 0,
                                              "%s: hay `%s` pero no un lockfile versionado (%s) · DEP2"
                                              % (ecosistema, manifiesto, " o ".join(locks))))
                break
        return hallazgos
