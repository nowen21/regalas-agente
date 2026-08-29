# -*- coding: utf-8 -*-
"""Rompe a proposito el corredor, y mira si las pruebas lo cazan.

Una prueba que no falla cuando el codigo esta roto no prueba nada. Esta casa
lleva cinco casos en dos dias: pruebas verdes atadas a un caso que iba a
desaparecer, o que no podian fallar, o que no tocaban la rama que decian tocar
(`S-062`). Y en la fase anterior, un sabotaje que se colo resulto senalar codigo
muerto en vez de una prueba floja (`S-074`).

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
CLASE = "pruebas.LasPruebasQueExistenSeCorren"

SABOTAJES = [
    # -- el critico: cero pruebas leido como verde ------------------------
    ("cero pruebas vuelve a pasar por verde",
     "validadores/corredor.py",
     "    if resultado.testsRun == 0:",
     "    if False:"),

    ("la carpeta que no existe deja de ser roja",
     "validadores/corredor.py",
     "        return (None, [Hallazgo(FALLA, carpeta, 0,",
     "        return (None, [Hallazgo(AVISO, carpeta, 0,"),

    ("un nombre mal escrito se traga en silencio",
     "validadores/corredor.py",
     "        for n in faltantes:",
     "        for n in []:"),

    # -- el conteo, que es lo unico que se lee ----------------------------
    ("deja de decir cuantas corrio",
     "validadores/corredor.py",
     '            "%d prueba(s) en %d archivo(s)',
     '            "corrio (s) en (s) archivo(s)'),

    # -- el sello, que es lo que hace posible el reclamo ------------------
    ("el sello miente: dice cero fallas pase lo que pase",
     "validadores/corredor.py",
     "                              if h.severidad == FALLA]))",
     "                              if False]))"),

    ("sella un subconjunto como si fuera la carpeta entera",
     "validadores/corredor.py",
     "        if not solo:",
     "        if True:"),

    ("el sello vuelve al cajon de las sesiones",
     "validadores/corredor.py",
     'SELLO = os.path.join("historico-chat", ".estado", "internas.txt")',
     'SELLO = os.path.join("historico-chat", ".tocado", "internas.txt")'),

    ("no reclama cuando nunca corrio",
     "validadores/corredor.py",
     "    if sello is None:",
     "    if False:"),

    ("los tres motivos se dicen igual: el aviso se vuelve ruido",
     "validadores/corredor.py",
     '                         "la última corrida de las pruebas del estándar "',
     '                         "las pruebas del estándar nunca corrieron "'),

    # -- un archivo roto no puede llevarse el resto -----------------------
    ("un archivo que no carga tumba la corrida entera",
     "validadores/corredor.py",
     "            continue\n        suite.addTests",
     "            raise SystemExit(1)\n        suite.addTests"),

    # -- la conexion: existe y nadie lo llama -----------------------------
    ("el reclamo queda escrito pero descolgado",
     "validadores/instalar.py",
     'validar.py" internas --reclamo',
     'validar.py" internas-descolgado --reclamo'),

    ("el enganche pasa a correr las 650: un peaje de 10 minutos",
     "validadores/instalar.py",
     '"$ESTANDAR/validadores/validar.py" internas --reclamo || true',
     '"$ESTANDAR/validadores/validar.py" internas || true'),

    # -- las dos suites, separadas a proposito ----------------------------
    ("la corrida de rutina empieza a arrastrar las 650",
     "validadores/validar.py",
     '    "internas": "corre las pruebas del propio estándar y tarda; va aparte",',
     ""),
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
                print("NO APLICA  %-56s (%s)" % (nombre, rel))
                fallos.append(nombre + " -- no aplico")
                continue
            escribir(rel, texto.replace(viejo, nuevo, 1))
            try:
                cazado, resumen = corren_las_pruebas()
            finally:
                shutil.copy2(copias[rel], os.path.join(RAIZ, rel))
            roto = ("SyntaxError" in resumen or "IndentationError" in resumen)
            if roto:
                # `S-068`, con otra forma: si el archivo queda sin compilar, las
                # pruebas fallan por la sintaxis y no por el comportamiento.
                # Eso no es cazar el sabotaje: es no haberlo aplicado.
                marca = "NO VALE"
                fallos.append(nombre + " -- dejo el archivo sin compilar")
            elif cazado:
                marca = "CAZADO"
            else:
                marca = "SE COLO"
                fallos.append(nombre)
            print("%-10s %-56s %s" % (marca, nombre, resumen[-52:]))
    finally:
        for rel, copia in copias.items():
            shutil.copy2(copia, os.path.join(RAIZ, rel))
            os.remove(copia)

    print("")
    if fallos:
        print("SE COLARON %d de %d:" % (len(fallos), len(SABOTAJES)))
        for f in fallos:
            print("   - %s" % f)
        print("")
        print("Dos preguntas, y en este orden (`S-074`):")
        print("  1. ?Falta una prueba?")
        print("  2. ?O sobra el codigo? Si nadie puede observar la diferencia")
        print("     entre romper la linea y dejarla, la linea no hace nada.")
        return 1
    print("Los %d sabotajes fueron cazados." % len(SABOTAJES))
    return 0


if __name__ == "__main__":
    sys.exit(main())
