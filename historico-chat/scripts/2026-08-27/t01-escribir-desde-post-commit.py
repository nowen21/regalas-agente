# -*- coding: utf-8 -*-
"""T-01: que pasa al escribir un archivo del repositorio DESDE un post-commit.

Es la duda declarada en el plan §2.7, y se resuelve midiendo en un repositorio
de mentira antes de escribir una linea de codigo. El plan dice: si el resultado
no se puede explicar en una linea, se para y se replantea el diseno.

Tres cosas que hay que ver, no suponer:
  1. Al terminar el commit, el archivo queda modificado y SIN guardar?
  2. El commit se hizo igual?
  3. Que dice `git status` justo despues?
"""
import io
import os
import shutil
import subprocess
import tempfile

TMP = tempfile.mkdtemp(prefix="t01_")


def git(*args, **kw):
    return subprocess.run(["git"] + list(args), cwd=kw.get("cwd", TMP),
                          capture_output=True, text=True,
                          encoding="utf-8", errors="replace")


git("init", "-q")
git("config", "user.name", "prueba")          # LOCAL, nunca global (00-N1)
git("config", "user.email", "prueba@local")
git("config", "core.hooksPath", ".githooks")

os.makedirs(os.path.join(TMP, ".githooks"))
io.open(os.path.join(TMP, "estado-fase.md"), "w", encoding="utf-8",
        newline="\n").write("| 12 | Commit | autorizado | PENDIENTE |\n")

# El enganche: escribe el hash del commit recien hecho en el archivo.
gancho = os.path.join(TMP, ".githooks", "post-commit")
io.open(gancho, "w", encoding="utf-8", newline="\n").write(
    "#!/bin/sh\n"
    "h=$(git rev-parse --short HEAD)\n"
    "sed -i \"s/PENDIENTE/$h/\" estado-fase.md\n")
os.chmod(gancho, 0o755)

git("add", "-A")
r = git("commit", "-m", "prueba")
print("1. El commit se hizo:", r.returncode == 0)
print("   salida:", (r.stdout or r.stderr or "").strip().splitlines()[-1:])
print()

texto = io.open(os.path.join(TMP, "estado-fase.md"), encoding="utf-8").read()
print("2. El archivo despues del commit:")
print("   ", texto.strip())
print()

estado = git("status", "--porcelain")
print("3. git status justo despues:")
print("   ", repr(estado.stdout.strip()) or "(limpio)")
print()

log = git("log", "--oneline")
print("4. git log:")
print("   ", log.stdout.strip())
print()

guardado = git("show", "HEAD:estado-fase.md")
print("5. Lo que quedo GUARDADO en el commit:")
print("   ", guardado.stdout.strip())
print()

print("LECTURA:")
sucio = bool(estado.stdout.strip())
print("   El commit se hace:            ", r.returncode == 0)
print("   El archivo se modifica:       ", "PENDIENTE" not in texto)
print("   Queda sin guardar tras hacerlo:", sucio)
print()
if sucio:
    print("   -> El enganche escribe DESPUES de que el commit se cerro, asi que")
    print("      el hash queda en el arbol de trabajo y NO dentro de ese commit.")
    print("      Hay que decidir: se deja sucio para el siguiente commit, o el")
    print("      enganche lo agrega el mismo. Lo segundo reescribe el commit.")

shutil.rmtree(TMP, ignore_errors=True)
print()
print("   (repositorio de prueba borrado, sin rastros)")
