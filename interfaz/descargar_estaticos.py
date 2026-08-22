# -*- coding: utf-8 -*-
"""Descarga los estáticos de terceros del visor, pineados por versión y huella.

**Por qué existe.** La estructura estándar de un proyecto Django prohíbe copiar
terceros al repositorio (`plantillas/estructura-proyecto-django.md`): se
declaran y se instalan. Bootstrap, AdminLTE, los iconos y Chart.js dejaron de
estar versionados; este programa los trae una vez, a `terceros/`, carpeta ignorada por
git que `collectstatic` junta con lo propio de `static/`, y el visor sigue funcionando sin internet después de instalado.

**Nada se acepta sin verificar.** Cada archivo declara su huella SHA-256; si lo
descargado no coincide, se descarta y el programa falla diciendo cuál.

Se corre una vez tras clonar:  python interfaz/descargar_estaticos.py
"""
import hashlib
import io
import os
import sys
import urllib.request

AQUI = os.path.dirname(os.path.abspath(__file__))
DESTINO = os.path.join(AQUI, "terceros")

# (ruta relativa bajo terceros/, url pineada, sha256 esperado)
ESTATICOS = (
    ("bootstrap/bootstrap.min.css",
     "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css",
     "3c8f27e6009ccfd710a905e6dcf12d0ee3c6f2ac7da05b0572d3e0d12e736fc8"),
    ("bootstrap/bootstrap.bundle.min.js",
     "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js",
     "0833b2e9c3a26c258476c46266e6877fc75218625162e0460be9a3a098a61c6c"),
    ("adminlte/adminlte.min.css",
     "https://cdn.jsdelivr.net/npm/admin-lte@4.1.0/dist/css/adminlte.min.css",
     "9ea5b8ec3e86306dfc1133879e232da7208e1015971118a007dcfd9f7fd1327a"),
    ("adminlte/adminlte.min.js",
     "https://cdn.jsdelivr.net/npm/admin-lte@4.1.0/dist/js/adminlte.min.js",
     "20b5413d034e94c54a55238fa5636bcca71110b141fbe08a5f33dd13f7855f28"),
    ("bootstrap-icons/bootstrap-icons.min.css",
     "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css",
     "f643d6fe7e679f9de3e16311600c5ef5cd6b098f7a3a8828fcc29255d2b33e62"),
    ("bootstrap-icons/fonts/bootstrap-icons.woff",
     "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/fonts/bootstrap-icons.woff",
     "bb1de989b83970f6f4e54de1cd974c5cba55b73582da5e1b225a6d0edf029483"),
    ("bootstrap-icons/fonts/bootstrap-icons.woff2",
     "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/fonts/bootstrap-icons.woff2",
     "476adf42b40325098fcfa8b36ab3e769186bb4f6ce6a249753e2e1a9c22bf99e"),
    ("chartjs/chart.umd.min.js",
     "https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js",
     "d2af8974e95271638772e9e9524db5b9a6f58d6ec2d5d781400447b4a31c681e"),
)


def descargar(destino=DESTINO):
    """Trae los que falten o no coincidan. Devuelve cuántos descargó."""
    traidos = 0
    for rel, url, esperado in ESTATICOS:
        ruta = os.path.join(destino, *rel.split("/"))
        if os.path.isfile(ruta):
            actual = hashlib.sha256(io.open(ruta, "rb").read()).hexdigest()
            if actual == esperado:
                print(f"  ya está  {rel}")
                continue
        datos = urllib.request.urlopen(url, timeout=60).read()
        actual = hashlib.sha256(datos).hexdigest()
        if actual != esperado:
            raise SystemExit(
                f"HUELLA DISTINTA en {rel}: se esperaba {esperado} y llegó "
                f"{actual}. No se escribió nada de ese archivo.")
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with io.open(ruta, "wb") as f:
            f.write(datos)
        print(f"  traído   {rel}")
        traidos += 1
    return traidos


if __name__ == "__main__":
    print("Estáticos del visor (pineados por versión y huella):")
    n = descargar()
    print(f"Listo: {n} descargado(s), {len(ESTATICOS) - n} ya estaban.")
    sys.exit(0)
