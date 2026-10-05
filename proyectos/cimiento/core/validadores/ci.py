"""`09·G6` · Las pruebas y el linter corren solos en un pipeline.

Lo comprobable: existe un archivo de pipeline y menciona correr pruebas y
linter. Se reconocen los más comunes por su ubicación, sin suponer el lenguaje.

Es aviso: puede haber CI en un sistema que no se reconoce, o un pipeline que
llama a un guion propio.
"""
import os
import re

from ..comun import AVISO, Git, Hallazgo
from .base import Validador

ARCHIVO_DE_CI = re.compile(
    r"(^|/)\.github/workflows/[^/]+\.ya?ml$|(^|/)\.gitlab-ci\.yml$|"
    r"(^|/)(azure-pipelines|bitbucket-pipelines)\.yml$|(^|/)Jenkinsfile$|"
    r"(^|/)\.circleci/config\.yml$|(^|/)\.drone\.yml$|(^|/)\.travis\.yml$")
_CORRE_PRUEBAS = re.compile(
    r"(?i)\b(test|tests|pruebas|phpunit|pytest|jest|vitest|artisan\s+test|npm\s+test|go\s+test)\b")
_CORRE_LINTER = re.compile(
    r"(?i)\b(lint|linter|pint|phpstan|psalm|eslint|prettier|ruff|flake8|rubocop|golangci)\b")


class IntegracionContinua(Validador):
    """Avisa si no hay pipeline, o si no corre las pruebas o el linter."""

    nombre = "ci"
    regla = "09·G6"
    descripcion = "pipeline de integración continua"

    def validar(self):
        repos = self.proyecto.repositorios()
        if not repos:
            return [Hallazgo(AVISO, self.proyecto.raiz, 0, "no hay repositorios git que revisar")]
        hallazgos = []
        for repo in repos:
            donde = self.proyecto.prefijo_de(repo) or self.proyecto.raiz
            textos = [self.archivos.leer(os.path.join(repo, a))
                      for a in Git(repo).versionados() if ARCHIVO_DE_CI.search(a)]
            hallazgos += [Hallazgo(AVISO, donde, 0, motivo) for motivo in self.motivos(textos)]
        return hallazgos

    @staticmethod
    def motivos(textos):
        """El núcleo puro: qué le falta al CI, dados los textos de sus archivos."""
        if not textos:
            return ["no se ve un pipeline de CI (G6): pruebas y linter deberían correr solos en cada cambio"]
        junto = "\n".join(textos)
        faltan = []
        if not _CORRE_PRUEBAS.search(junto):
            faltan.append("el CI no parece correr las pruebas (G6)")
        if not _CORRE_LINTER.search(junto):
            faltan.append("el CI no parece correr el linter (G6)")
        return faltan
