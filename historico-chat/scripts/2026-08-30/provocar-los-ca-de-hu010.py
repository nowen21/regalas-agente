# -*- coding: utf-8 -*-
"""Provoca los CA-02, CA-03 y CA-04 de EP-004 HU-010 en un proyecto de prueba.

Los tres piden que se **reporte** un incumplimiento, y en los proyectos reales
no hay ninguno que sirva: uno tiene las migraciones en un formato que el
programa no lee, y el otro no declara sus entidades. Provocarlos en un proyecto
real esta prohibido por la decision 35 del pendiente 59, asi que se arma uno
temporal, como se hizo con el ajuste que afloja el nucleo.

Cada caso trae **su contraprueba**: el mismo proyecto sin el defecto no debe
reportar nada. Sin eso, un validador que reclamara siempre pasaria igual.
"""
import io
import os
import shutil
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(RAIZ, "validadores"))

import declaracion                                           # noqa: E402
import entidades                                             # noqa: E402
import estructura                                            # noqa: E402

MAPEO = u"""# Mapeo de nombres

## Convenciones

| Clave | Valor |
|---|---|
| `modulos.ruta` | `src/<modulo>` |
| `tablas.caso` | `snake_case` |
| `columnas.caso` | `snake_case` |
| `clases.caso` | `PascalCase` |
| `auditoria.columnas` | `created_at, updated_at` |
| `inmutables.estados` | `borrador, emitida, anulada` |
| `inmutables.anulacion` | `anulada_en, anulada_por` |
| `inmutables.permiso` | `anular_<recurso>` |
"""

DOMINIO = u"""# Dominio

## Entidades del negocio

| Entidad | Tabla | Clave natural | Inmutable | Qué representa |
|---|---|---|---|---|
| Factura | `facturas` | `numero` | sí | Una venta ya emitida |
| Cliente | `clientes` | `documento` | no | Quien compra |

## Módulos

| Módulo | Carpeta | Especificación | Qué hace |
|---|---|---|---|
| `ventas` | `src/ventas` | `documentacion/ventas/spec.md` | Emite facturas |
"""

# La migracion con los tres defectos, uno por criterio.
CON_DEFECTOS = u"""CREATE TABLE clientes (
  id INTEGER PRIMARY KEY,
  documento TEXT NOT NULL,
  nombreCompleto TEXT NOT NULL
);

CREATE TABLE facturas (
  id INTEGER PRIMARY KEY,
  numero TEXT NOT NULL,
  total INTEGER NOT NULL
);
"""

# La misma sin ninguno: es la contraprueba.
SIN_DEFECTOS = u"""CREATE TABLE clientes (
  id INTEGER PRIMARY KEY,
  documento TEXT NOT NULL UNIQUE,
  nombre_completo TEXT NOT NULL,
  created_at TEXT,
  updated_at TEXT
);

CREATE TABLE facturas (
  id INTEGER PRIMARY KEY,
  numero TEXT NOT NULL UNIQUE,
  total INTEGER NOT NULL,
  estado TEXT NOT NULL CHECK (estado IN ('borrador','emitida','anulada')),
  anulada_en TEXT,
  anulada_por INTEGER,
  created_at TEXT,
  updated_at TEXT
);
"""


def _proyecto(migracion, modulos=("ventas",), permiso=False):
    carpeta = tempfile.mkdtemp(prefix="hu010-")
    agente = os.path.join(carpeta, ".agente")
    os.makedirs(agente)
    for nombre, cuerpo in (("mapeo-nombres.md", MAPEO), ("dominio.md", DOMINIO)):
        with io.open(os.path.join(agente, nombre), "w",
                     encoding="utf-8", newline="\n") as f:
            f.write(cuerpo)
    migraciones = os.path.join(carpeta, "database", "migrations")
    os.makedirs(migraciones)
    with io.open(os.path.join(migraciones, "0001_inicial.sql"), "w",
                 encoding="utf-8", newline="\n") as f:
        f.write(migracion)
    for m in modulos:
        os.makedirs(os.path.join(carpeta, "src", m))
        with io.open(os.path.join(carpeta, "src", m, "__init__.py"), "w",
                     encoding="utf-8") as f:
            # El permiso de anular vive en el codigo, y la comprobacion lo
            # busca ahi. Sin el, el proyecto limpio reclamaria igual y la
            # contraprueba no probaria nada.
            f.write(u'PERMISOS = ["anular_factura"]\n' if permiso else u"")
    # **Tiene que ser un repositorio, y con los archivos guardados.** Las
    # comprobaciones solo miran lo versionado, y es a proposito: lo que no esta
    # guardado todavia no es del proyecto. Sin esto no encuentran ni una
    # migracion, y el resultado se lee como si todo estuviera bien.
    import subprocess
    def git(*args):
        subprocess.run(["git"] + list(args), cwd=carpeta,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    git("init", "-q")
    git("config", "user.email", "prueba@local")
    git("config", "user.name", "prueba")
    git("add", "-A")
    git("-c", "core.hooksPath=", "commit", "-q", "-m", "inicial")
    return carpeta


def _mensajes(hallazgos):
    return [h.mensaje for h in hallazgos]


def caso(titulo, criterio, con, sin, aguja):
    """Imprime el resultado de un criterio y su contraprueba."""
    hay = [m for m in con if aguja in m]
    no_hay = [m for m in sin if aguja in m]
    ok = bool(hay) and not no_hay
    print("%-11s %s" % ("CUMPLE" if ok else "NO CUMPLE", titulo))
    print("             criterio:    %s" % criterio)
    print("             con defecto: %s" % (hay[0][:120] if hay else "no se reportó"))
    print("             sin defecto: %s\n"
          % ("se reportó igual, y no debía" if no_hay else "ningún reclamo"))
    return ok


def main():
    con_ruta = _proyecto(CON_DEFECTOS, modulos=("ventas", "cobros"))
    sin_ruta = _proyecto(SIN_DEFECTOS, modulos=("ventas",), permiso=True)
    try:
        con_est = _mensajes(estructura.validar(con_ruta))
        sin_est = _mensajes(estructura.validar(sin_ruta))
        con_ent = _mensajes(entidades.validar(con_ruta))
        sin_ent = _mensajes(entidades.validar(sin_ruta))
    finally:
        shutil.rmtree(con_ruta, ignore_errors=True)
        shutil.rmtree(sin_ruta, ignore_errors=True)

    print("PROVOCACION DE LOS CRITERIOS QUE NO SE VEN EN UN PROYECTO REAL\n")
    r = []
    r.append(caso("CA-02 · un nombre fuera de la convención se reporta",
                  "columnas.caso = snake_case, y la columna es nombreCompleto",
                  con_est + con_ent, sin_est + sin_ent, "nombreCompleto"))
    r.append(caso("CA-03 · una tabla de dominio sin auditoría se reporta",
                  "auditoria.columnas = created_at, updated_at",
                  con_ent, sin_ent, "auditor"))
    r.append(caso("CA-04 · una entidad inmutable sin estados ni permiso se reporta",
                  "inmutables.estados y inmutables.permiso, declarados",
                  con_ent, sin_ent, "inmutable"))
    r.append(caso("CA-05 · un módulo del código sin declarar se reporta",
                  "modulos.ruta = src/<modulo>, y `cobros` no está en el dominio",
                  con_est, sin_est, "cobros"))

    print("-" * 72)
    print("%d de %d criterios provocados y verificados" % (sum(r), len(r)))
    return 0 if all(r) else 1


if __name__ == "__main__":
    sys.exit(main())
