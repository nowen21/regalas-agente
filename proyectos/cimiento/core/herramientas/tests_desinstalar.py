# -*- coding: utf-8 -*-
"""El estándar se puede desinstalar de un proyecto (`EP-025·HU-021`).

Sin Django: corren con `python -m unittest core.herramientas.tests_desinstalar`
desde `proyectos/cimiento/`, sobre un repositorio git temporal.
"""
import io
import json
import os
import subprocess
import tempfile
import unittest

from ..proyectos import registro
from .desinstalar import Desinstalador
from .instalar import CI_GITHUB, Instalador

AJENO = {"type": "command", "command": "echo hola"}


def _escribir(ruta, texto):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def _leer(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return f.read()


def _foto(raiz):
    """`{ruta relativa: texto}` de todo lo que hay, menos `.git/`."""
    salida = {}
    for carpeta, subcarpetas, archivos in os.walk(raiz):
        subcarpetas[:] = [s for s in subcarpetas if s != ".git"]
        for nombre in archivos:
            ruta = os.path.join(carpeta, nombre)
            salida[os.path.relpath(ruta, raiz)] = _leer(ruta)
        for nombre in subcarpetas:
            salida[os.path.relpath(os.path.join(carpeta, nombre), raiz) + os.sep] = ""
    return salida


class ElEstandarSePuedeDesinstalar(unittest.TestCase):

    def setUp(self):
        carpeta = tempfile.TemporaryDirectory()
        self.addCleanup(carpeta.cleanup)
        self.raiz = os.path.join(carpeta.name, "proyecto")
        os.makedirs(self.raiz)
        subprocess.run(["git", "init", "-q"], cwd=self.raiz, check=True)
        self.instalador = Instalador()
        self.instalador.registro = os.path.join(carpeta.name, "proyectos.md")
        _escribir(self.instalador.registro, "| Proyecto | Ruta | Scope | Stack |\n|---|---|---|---|\n"
                                            "| otro | `C:\\otro` | `proyecto:otro` | x |\n"
                                            "| proyecto | `%s` | `proyecto:proyecto` | por detectar |\n" % self.raiz)
        # Lo del proyecto, antes de instalar.
        _escribir(os.path.join(self.raiz, ".claude", "settings.json"),
                  json.dumps({"hooks": {"Stop": [{"hooks": [AJENO]}]}}))
        _escribir(os.path.join(self.raiz, "CLAUDE.md"), "# El proyecto\n")
        _escribir(os.path.join(self.raiz, ".agente", "stack.md"), "# Stack: Django\n")
        _escribir(os.path.join(self.raiz, "historico-chat", "README.md"), "# Histórico\n")
        _escribir(os.path.join(self.raiz, "documentacion", "x.md"), "# Algo escrito\n")
        _escribir(os.path.join(self.raiz, ".github", "workflows", "otro.yml"), "name: otro\n")
        # La instalación.
        estandar = self.instalador.estandar.replace("\\", "/")
        self.instalador.instalar_git(self.raiz, estandar, True)
        self.instalador.instalar_claude(self.raiz, estandar, True)
        self.instalador.instalar_ci(self.raiz, True, repo="https://ejemplo.invalid/estandar.git")
        self.instalador.instalar_estructura(self.raiz, True)
        _escribir(os.path.join(self.raiz, ".agente", "stack-instalacion.md"), "copia\n")
        _escribir(Instalador.copia_sellada(self.raiz), "plantilla\n")
        self.desinstalador = Desinstalador(self.instalador)

    def hooks_path(self):
        return subprocess.run(["git", "config", "--get", "core.hooksPath"], cwd=self.raiz,
                              capture_output=True, text=True).stdout.strip()

    # CP-001 · Quitar
    def test_quita_los_enganches_y_deja_los_ajenos(self):
        self.assertEqual(".githooks", self.hooks_path())
        self.desinstalador.desinstalar(self.raiz, True)
        self.assertEqual("", self.hooks_path())
        self.assertFalse(os.path.exists(os.path.join(self.raiz, ".githooks")))
        datos = json.loads(_leer(os.path.join(self.raiz, ".claude", "settings.json")))
        self.assertEqual({"hooks": {"Stop": [{"hooks": [AJENO]}]}}, datos)

    def test_un_enganche_de_git_ajeno_deja_el_hookspath(self):
        _escribir(os.path.join(self.raiz, ".githooks", "post-merge"), "#!/bin/sh\necho mio\n")
        self.desinstalador.desinstalar(self.raiz, True)
        self.assertEqual(".githooks", self.hooks_path())
        self.assertEqual(["post-merge"], os.listdir(os.path.join(self.raiz, ".githooks")))

    def test_quita_las_copias_la_ci_y_las_carpetas_vacias(self):
        self.desinstalador.desinstalar(self.raiz, True)
        for rel in (".agente/stack-instalacion.md", ".agente/plantillas-selladas", CI_GITHUB, "proyectos", "prompts"):
            self.assertFalse(os.path.exists(os.path.join(self.raiz, *rel.split("/"))), rel)
        self.assertTrue(os.path.isfile(os.path.join(self.raiz, ".github", "workflows", "otro.yml")))

    def test_sale_del_registro(self):
        self.desinstalador.desinstalar(self.raiz, True)
        texto = _leer(self.instalador.registro)
        self.assertNotIn("proyecto:proyecto", texto)
        self.assertIn("proyecto:otro", texto)

    def test_la_telemetria_se_quita_y_lo_demas_del_usuario_se_queda(self):
        configuracion = os.path.join(self.raiz, "usuario.json")
        _escribir(configuracion, json.dumps({"env": {**self.instalador.telemetria(), "OTRA": "1"}, "tema": "x"}))
        self.assertTrue(self.desinstalador.quitar_telemetria(True, configuracion))
        self.assertEqual({"env": {"OTRA": "1"}, "tema": "x"}, json.loads(_leer(configuracion)))

    def test_quita_el_arranque_del_vigilante(self):
        """`EP-025·HU-011 · CP-002`, paso 3."""
        inicio = os.path.join(self.raiz, "inicio")
        archivo = os.path.join(inicio, Instalador.VIGILANTE + ".cmd")
        _escribir(archivo, "@echo off\n")
        ordenes = []

        def ejecutar(orden, **_):
            ordenes.append(orden)
            return subprocess.CompletedProcess(orden, 0, "detenido el vigilante del consumo (proceso 1)", "")

        self.assertEqual(2, len(self.desinstalador.quitar_vigilante(False, ejecutar, inicio)))
        self.assertTrue(os.path.isfile(archivo))
        self.assertEqual([], ordenes)
        pasos = self.desinstalador.quitar_vigilante(True, ejecutar, inicio)
        self.assertFalse(os.path.exists(archivo))
        self.assertIn("detener el vigilante del consumo", pasos)
        self.assertEqual(["vigilar_consumo", "--parar"], ordenes[0][-2:])

    def test_la_baja_y_su_contraria(self):
        class Filas:
            def __init__(self, filas):
                self.filas = filas

            def filter(self, ruta__iexact, activo):
                return Filas([f for f in self.filas if f["ruta"].lower() == ruta__iexact.lower()
                              and f["activo"] == activo])

            def update(self, activo):
                for f in self.filas:
                    f["activo"] = activo
                return len(self.filas)

        fila = {"ruta": os.path.abspath(self.raiz), "activo": True}

        class Modelo:
            objects = None

        Modelo.objects = type("M", (), {"filter": lambda _s, **k: Filas([fila]).filter(**k)})()
        self.assertTrue(registro.dar_de_baja(Modelo, self.raiz))
        self.assertFalse(fila["activo"])
        self.assertFalse(registro.dar_de_baja(Modelo, self.raiz))
        self.assertTrue(registro.reactivar(Modelo, self.raiz))
        self.assertTrue(fila["activo"])

    # CP-002 · Lo propio se queda
    def test_lo_propio_se_queda(self):
        antes = {rel: _leer(os.path.join(self.raiz, rel)) for rel in
                 ("CLAUDE.md", os.path.join(".agente", "stack.md"), os.path.join("historico-chat", "README.md"),
                  os.path.join("documentacion", "x.md"))}
        self.desinstalador.desinstalar(self.raiz, True)
        self.assertEqual(antes, {rel: _leer(os.path.join(self.raiz, rel)) for rel in antes})

    # CP-003 · Simular y repetir
    def test_sin_aplicar_no_toca_nada(self):
        foto = _foto(self.raiz)
        registro_antes = _leer(self.instalador.registro)
        pasos = self.desinstalador.desinstalar(self.raiz, False)
        self.assertGreater(len(pasos), 4)
        self.assertEqual(foto, _foto(self.raiz))
        self.assertEqual(registro_antes, _leer(self.instalador.registro))
        self.assertEqual(".githooks", self.hooks_path())

    def test_la_segunda_vez_no_hay_nada(self):
        self.desinstalador.desinstalar(self.raiz, True)
        self.assertEqual(["no había nada de la instalación que quitar"],
                         self.desinstalador.desinstalar(self.raiz, True))

    def test_reinstalar_vuelve_a_poner_los_enganches(self):
        self.desinstalador.desinstalar(self.raiz, True)
        estandar = self.instalador.estandar.replace("\\", "/")
        self.instalador.instalar_git(self.raiz, estandar, True)
        self.assertEqual(".githooks", self.hooks_path())


if __name__ == "__main__":
    unittest.main()
