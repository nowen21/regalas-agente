"""`09·G4` · El trabajo va en una rama dedicada y al día con la principal.

Sirve a cualquier proyecto git: el nombre de la principal se detecta (`main`,
`master` o lo que apunte `origin/HEAD`), no se supone.

Todo es aviso: trabajar sobre la principal puede ser deliberado (la capa 3 del
proyecto puede permitirlo), e ir atrás es una señal para sincronizar.
"""
from ..comun import AVISO, Git, Hallazgo
from .base import Validador


class RamaDedicada(Validador):
    """Avisa de HEAD desprendido, del trabajo en la principal y de la rama atrasada."""

    nombre = "rama"
    regla = "09·G4"
    descripcion = "rama dedicada y al día"

    def validar(self):
        repos = self.proyecto.repositorios()
        if not repos:
            return [Hallazgo(AVISO, self.proyecto.raiz, 0, "no hay repositorios git que revisar")]
        hallazgos = []
        for repo in repos:
            git = Git(repo)
            principal = git.rama_principal()
            hallazgos += self.evaluar(git.rama_actual(), principal,
                                      git.commits_detras(principal) if principal else 0,
                                      self.proyecto.prefijo_de(repo) or self.proyecto.raiz)
        return hallazgos

    @staticmethod
    def evaluar(actual, principal, detras, donde=""):
        """El núcleo puro: qué señala G4 dado el estado de las ramas."""
        if actual == "HEAD":
            return [Hallazgo(AVISO, donde, 0, "HEAD desprendido: no se está en una rama (G4)")]
        if principal is None or actual is None:
            return []                       # no se pudo saber: no se opina
        if actual == principal:
            return [Hallazgo(AVISO, donde, 0, "se está trabajando en la rama principal `%s`; G4 pide una "
                                              "rama dedicada (salvo que la capa 3 lo permita)" % actual)]
        if detras > 0:
            return [Hallazgo(AVISO, donde, 0, "la rama `%s` está %d commit(s) detrás de `%s`; G4 pide "
                                              "mantenerla al día" % (actual, detras, principal))]
        return []
