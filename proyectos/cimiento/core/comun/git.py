"""Correr git en un repositorio. Antes estaba copiado en seis validadores, cada uno
con su propio manejo de errores (análisis 1 del pendiente 116)."""
import os
import subprocess


class Git:
    """Un repositorio git, visto desde afuera."""

    def __init__(self, repo, espera=60):
        self.repo = os.path.abspath(repo)
        self.espera = espera

    @staticmethod
    def es_repositorio(ruta):
        return os.path.exists(os.path.join(ruta, ".git"))

    def correr(self, *argumentos):
        """La salida de la orden, o `""` si git no corrió o terminó con error."""
        try:
            r = subprocess.run(["git", "-C", self.repo, *argumentos], capture_output=True,
                               text=True, encoding="utf-8", errors="replace", timeout=self.espera)
        except (OSError, subprocess.SubprocessError):
            return ""
        return r.stdout if r.returncode == 0 else ""

    def lineas(self, *argumentos):
        """La salida partida en líneas, sin las vacías."""
        return [l.strip() for l in self.correr(*argumentos).splitlines() if l.strip()]

    def versionados(self):
        """Lo que git tiene registrado, con `/`."""
        return [l.replace("\\", "/") for l in self.lineas("ls-files")]

    def preparados(self):
        """Lo que entra en el commit que se está por hacer (creado, copiado,
        modificado o renombrado)."""
        return [l.replace("\\", "/") for l in self.lineas("diff", "--cached", "--name-only", "--diff-filter=ACMR")]

    def rama_actual(self):
        salida = self.lineas("rev-parse", "--abbrev-ref", "HEAD")
        return salida[0] if salida else None

    def rama_principal(self):
        """La principal sin suponer cuál es: la que declare el remoto
        (`origin/HEAD`) o el primer nombre habitual que exista."""
        ref = self.lineas("symbolic-ref", "--short", "refs/remotes/origin/HEAD")
        if ref:
            return ref[0].split("/", 1)[-1]
        for candidata in ("main", "master", "trunk", "develop"):
            if self.lineas("rev-parse", "--verify", "--quiet", "refs/heads/" + candidata):
                return candidata
        return None

    def commits_detras(self, principal):
        """Cuántos commits tiene la principal que HEAD no: la local si existe, si no la del remoto."""
        for ref in (principal, "origin/" + principal):
            salida = self.lineas("rev-list", "--count", "HEAD.." + ref)
            if salida:
                try:
                    return int(salida[0])
                except ValueError:
                    return 0
        return 0

    def mensaje(self, revision="HEAD"):
        """El mensaje completo de un commit ya hecho."""
        return self.correr("log", "-1", "--pretty=%B", revision)
