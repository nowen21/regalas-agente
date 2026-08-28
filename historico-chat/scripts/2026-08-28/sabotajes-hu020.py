# -*- coding: utf-8 -*-
"""Rompe a proposito el registro del turno, y mira si las pruebas lo cazan.

Una prueba que no falla cuando el codigo esta roto no prueba nada. En dos dias
pasaron cinco veces: pruebas verdes atadas a un caso que iba a desaparecer, o
que no podian fallar, o que no tocaban la rama que decian tocar (`S-062`).

DISCIPLINA, escrita porque cada linea salio de un error real:

  - Se restaura CON COPIA, nunca con git: git se llevaria por delante lo demas.
  - Se restaura en `try/finally`: si el guion revienta, el codigo vuelve igual.
  - No se corre por una tuberia: el codigo de salida seria el de la tuberia,
    no el de las pruebas (`S-060`).
  - Se imprime solo ASCII: la consola de Windows tumba el guion con el codigo
    roto puesto.
  - La guardia acepta `OK` y `OK (...)` pero rechaza `OK:`, porque unittest
    escribe `OK (expected failures=4)` en una corrida limpia (`S-068`).
"""
import os
import re
import shutil
import subprocess
import sys

RAIZ = r"c:\Ing. Jose\ia\agente"
CLASE = "pruebas.ElTurnoAnotaLoQueCambio"

SABOTAJES = [
    ("la primera vuelta reclama el arbol entero",
     "validadores/sesiones.py",
     "    if desde is None:\n        return []",
     "    if desde is None:\n        desde = 0"),

    ("no filtra por fecha: reclama lo de antes del turno",
     "validadores/sesiones.py",
     "            if os.path.getmtime(completa) > desde:",
     "            if os.path.getmtime(completa) > 0:"),

    ("pierde los borrados",
     "validadores/sesiones.py",
     "    salida = list(borradas)",
     "    salida = []"),

    ("no arranca el reloj: nunca anota nada",
     "validadores/sesiones.py",
     '        io.open(ruta, "a", encoding="utf-8").close()',
     "        pass"),

    ("escribe en una raiz que no existe",
     "validadores/sesiones.py",
     "    if not os.path.isdir(raiz):",
     "    if False:"),

    ("el enganche queda escrito pero descolgado",
     "validadores/instalar.py",
     '"hook_turno.py"',
     '"hook_turno_descolgado.py"'),

    ("el enganche revienta con entrada rota",
     "adaptadores/claude-code/hook_turno.py",
     "    except (json.JSONDecodeError, ValueError):\n        return 0",
     "    except (json.JSONDecodeError, ValueError):\n        pass"),
]


def leer(rel):
    with open(os.path.join(RAIZ, rel), encoding="utf-8") as f:
        return f.read()


def escribir(rel, texto):
    with open(os.path.join(RAIZ, rel), "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def corren_las_pruebas():
    """`(cazado, resumen)`. Sin tuberia: el codigo de salida es de unittest."""
    r = subprocess.run(
        [sys.executable, "-m", "unittest", CLASE],
        cwd=os.path.join(RAIZ, "validadores"),
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    texto = (r.stdout or "") + (r.stderr or "")
    limpio = texto.encode("ascii", "replace").decode("ascii")
    ultimas = [l.strip() for l in limpio.splitlines() if l.strip()][-3:]
    return (r.returncode != 0, " | ".join(ultimas))


def guardia():
    """Antes de romper nada: si ya esta en rojo, el resultado no dice nada."""
    cazado, resumen = corren_las_pruebas()
    verde = re.search(r"^OK(\s*\(|\s*$)", resumen.split("|")[-1].strip(),
                      re.MULTILINE)
    if cazado or not verde:
        print("PARAR: las pruebas no arrancan en verde -> %s" % resumen)
        return False
    return True


def main():
    if not guardia():
        return 1

    copias = {}
    for _, rel, _, _ in SABOTAJES:
        if rel not in copias:
            origen = os.path.join(RAIZ, rel)
            copia = origen + ".copia-sabotaje"
            shutil.copy2(origen, copia)
            copias[rel] = copia

    fallos = []
    try:
        for nombre, rel, viejo, nuevo in SABOTAJES:
            texto = leer(rel)
            if viejo not in texto:
                print("NO APLICA  %-52s (%s)" % (nombre, rel))
                fallos.append(nombre + " -- no aplico")
                continue
            escribir(rel, texto.replace(viejo, nuevo, 1))
            try:
                cazado, resumen = corren_las_pruebas()
            finally:
                shutil.copy2(copias[rel], os.path.join(RAIZ, rel))
            print("%-10s %-52s %s"
                  % ("CAZADO" if cazado else "SE COLO", nombre, resumen[-70:]))
            if not cazado:
                fallos.append(nombre)
    finally:
        for rel, copia in copias.items():
            shutil.copy2(copia, os.path.join(RAIZ, rel))
            os.remove(copia)

    print("")
    if fallos:
        print("SE COLARON %d de %d:" % (len(fallos), len(SABOTAJES)))
        for f in fallos:
            print("   - %s" % f)
        return 1
    print("Los %d sabotajes fueron cazados." % len(SABOTAJES))
    return 0


if __name__ == "__main__":
    sys.exit(main())
