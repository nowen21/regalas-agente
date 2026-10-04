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
