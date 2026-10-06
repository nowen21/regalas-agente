"""Validadores que **corren la herramienta del ecosistema**: `07·Q6`, `08·T5`, `10·DEP3`.

Los otros validadores leen archivos y deciden solos; estos invocan una
herramienta externa y reportan su resultado:

  Q6   · linter o formateador sin advertencias (pint, eslint, ruff…)
  T5   · las pruebas se corren y se reporta (phpunit, npm test, pytest…)
  DEP3 · auditoría de vulnerabilidades (composer, npm, pip audit…)

Por eso **no van en el enganche automático**: dependen de lo instalado, tardan
y tienen efectos (T5 toca la base de datos, DEP3 va a la red). Se corren a
demanda.

Multiproyecto **por detección de stack**: cada manifiesto versionado dice qué
herramienta corre y en qué carpeta, sin suponer un marco. Si no hay
herramienta, se avisa; no se inventa nada. La norma no se duplica: la define y
la ejecuta la herramienta del ecosistema, y aquí solo se traduce su salida.
"""
import os
import shutil
import subprocess

from ..comun import AVISO, FALLA, Git, Hallazgo
from .base import Validador

# Manifiesto versionado y su ecosistema. Un proyecto puede tener varios.
MANIFIESTOS = [
    ("composer.json", "php"),
    ("package.json", "node"),
    ("pyproject.toml", "python"),
    ("requirements.txt", "python"),
    ("Pipfile", "python"),
    ("Gemfile", "ruby"),
    ("go.mod", "go"),
]

_INSTALADO = ("vendor/", "node_modules/")


class HerramientaDelEcosistema(Validador):
    """Lo común a los tres: encontrar cada manifiesto, elegir el comando y correrlo.
    Cada subclase dice qué comando elige, si un error es falla y cuánto espera."""

    falla_si_rc = False
    espera = 300

    @staticmethod
    def stack_de_manifiesto(nombre):
        """Ecosistema de un manifiesto por su nombre, o None."""
        for manif, stack in MANIFIESTOS:
            if nombre == manif:
                return stack
        return None

    @staticmethod
    def es_instalado(ruta):
        return (ruta.startswith(_INSTALADO) or "/vendor/" in f"/{ruta}"
                or "/node_modules/" in f"/{ruta}")

    @classmethod
    def proyectos(cls, repo):
        """`(carpeta_absoluta, stack)` por cada manifiesto versionado del repositorio."""
        hallados = set()
        for ruta in Git(repo).versionados():
            if cls.es_instalado(ruta):
                continue
            stack = cls.stack_de_manifiesto(os.path.basename(ruta))
            if stack:
                hallados.add((os.path.normpath(os.path.join(repo, os.path.dirname(ruta))), stack))
        return sorted(hallados)

    @staticmethod
    def bin_local(carpeta, nombre):
        """Un ejecutable instalado por el proyecto (`vendor/bin`, `node_modules/.bin`).
        En Windows van primero `.bat`, `.cmd` y `.exe`: el archivo sin extensión es
        el guion de unix y no corre como programa nativo."""
        exts = (".bat", ".cmd", ".exe", "") if os.name == "nt" else ("", ".bat", ".cmd", ".exe")
        for sub in ("vendor/bin", "node_modules/.bin"):
            for ext in exts:
                p = os.path.join(carpeta, sub.replace("/", os.sep), nombre + ext)
                if os.path.isfile(p):
                    return p
        return None

    @staticmethod
    def correr(carpeta, args, espera):
        """`(código, salida)`, o `(None, motivo)` si no se pudo correr."""
        exe = args[0]
        if os.sep not in exe and "/" not in exe:
            # Nombre pelado (composer, npm): `shutil.which` respeta PATHEXT en
            # Windows y encuentra el `.bat` o `.cmd` real.
            resuelto = shutil.which(exe)
            if not resuelto:
                return None, "herramienta no encontrada"
            args = [resuelto] + list(args[1:])
        try:
            r = subprocess.run(args, cwd=carpeta, capture_output=True, text=True,
                               encoding="utf-8", errors="replace", timeout=espera)
            return r.returncode, ((r.stdout or "") + (r.stderr or "")).strip()
        except FileNotFoundError:
            return None, "herramienta no encontrada"
        except subprocess.TimeoutExpired:
            return None, f"tiempo agotado ({espera}s)"
        except OSError as e:
            return None, str(e)

    @staticmethod
    def resumen(salida, lineas=2, tope=200):
        """Las últimas líneas útiles, acotadas: contexto sin volcar todo."""
        utiles = [l.strip() for l in salida.splitlines() if l.strip()]
        texto = " · ".join(utiles[-lineas:]) if utiles else "sin salida"
        return texto if len(texto) <= tope else texto[:tope] + "… (correr la herramienta para el detalle)"

    def comando(self, carpeta, stack):
        """`(nombre, argumentos)` de la herramienta, o `(None, None)`."""
        raise NotImplementedError

    def validar(self):
        raiz = self.proyecto.raiz
        # Aquí y no arriba: el instalador importa los validadores (fila 23
        # del análisis 1 del pendiente 116).
        from ..herramientas.instalar import Instalador
        repos = Instalador.repositorios_git(raiz)
        if not repos:
            return [Hallazgo(AVISO, raiz, 0, "no hay repositorios git que revisar")]

        regla = self.regla.split("·")[-1]
        hallazgos = []
        for repo in repos:
            for carpeta, stack in self.proyectos(repo):
                donde = os.path.relpath(carpeta, raiz).replace("\\", "/")
                nombre, args = self.comando(carpeta, stack)
                if not nombre:
                    hallazgos.append(Hallazgo(AVISO, donde, 0,
                                              f"{stack}: no se encontró herramienta para {regla}"))
                    continue
                rc, salida = self.correr(carpeta, args, self.espera)
                if rc is None:
                    hallazgos.append(Hallazgo(AVISO, donde, 0,
                                              f"no se pudo correr {nombre}: {salida} ({regla})"))
                elif rc != 0:
                    hallazgos.append(Hallazgo(
                        FALLA if self.falla_si_rc else AVISO, donde, 0,
                        f"{nombre} reporta problemas — {self.resumen(salida)} ({regla})"))
        return hallazgos


class Linter(HerramientaDelEcosistema):
    """`07·Q6` · El linter o formateador del stack, sin advertencias."""

    nombre = "linter"
    regla = "07·Q6"
    descripcion = "el linter o formateador del stack"

    def comando(self, carpeta, stack):
        b = self.bin_local
        if stack == "php":
            if b(carpeta, "pint"):
                return "pint", [b(carpeta, "pint"), "--test"]
            if b(carpeta, "phpstan"):
                return "phpstan", [b(carpeta, "phpstan"), "analyse", "--no-progress"]
            if b(carpeta, "php-cs-fixer"):
                return "php-cs-fixer", [b(carpeta, "php-cs-fixer"), "fix", "--dry-run"]
        if stack == "node":
            if b(carpeta, "eslint"):
                return "eslint", [b(carpeta, "eslint"), "."]
            if b(carpeta, "prettier"):
                return "prettier", [b(carpeta, "prettier"), "--check", "."]
        if stack == "python":
            if b(carpeta, "ruff"):
                return "ruff", [b(carpeta, "ruff"), "check"]
            if b(carpeta, "flake8"):
                return "flake8", [b(carpeta, "flake8")]
        return None, None


class Suite(HerramientaDelEcosistema):
    """`08·T5` · Las pruebas se corren y se reporta. Un rojo es falla."""

    nombre = "suite"
    regla = "08·T5"
    descripcion = "la suite de pruebas del proyecto"
    falla_si_rc = True
    espera = 600

    def comando(self, carpeta, stack):
        b = self.bin_local
        if stack == "php" and b(carpeta, "phpunit"):
            return "phpunit", [b(carpeta, "phpunit"), "--no-coverage"]
        if stack == "node":
            return "npm test", ["npm", "test", "--silent"]
        if stack == "python" and b(carpeta, "pytest"):
            return "pytest", [b(carpeta, "pytest"), "-q"]
        return None, None


class Auditoria(HerramientaDelEcosistema):
    """`10·DEP3` · La auditoría de vulnerabilidades de las dependencias."""

    nombre = "audit"
    regla = "10·DEP3"
    descripcion = "la auditoría de vulnerabilidades"
    espera = 180

    def comando(self, carpeta, stack):
        if stack == "php":
            return "composer audit", ["composer", "audit", "--no-interaction", "--format=plain"]
        if stack == "node":
            return "npm audit", ["npm", "audit"]
        if stack == "python" and self.bin_local(carpeta, "pip-audit"):
            return "pip-audit", [self.bin_local(carpeta, "pip-audit")]
        return None, None
