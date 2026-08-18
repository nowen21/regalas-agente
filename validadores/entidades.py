#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lo que se le exige a una tabla de dominio — `03·D1`, `15·IM2` y `15·IM5`.

`esquema.py` ya comprueba la parte de `D1` que no necesita saber nada del
proyecto: que toda clave foránea declare su política de borrado. Lo que falta de
`D1` —auditoría, `UNIQUE` en la unicidad conceptual, índice en lo que se filtra—
y todo `15` dependen de una pregunta que la base no puede responder: **cuáles de
estas tablas son del dominio y cuáles trae el framework**, y **qué entidad es
inmutable**. Un `sessions` o un `jobs` no llevan auditoría, y exigírsela sería
ruido garantizado.

Eso lo declara el proyecto en `.agente/dominio.md` (qué entidades, qué tabla,
qué clave natural, cuál es inmutable) y en `.agente/mapeo-nombres.md` (cómo se
llaman aquí las columnas de auditoría, los estados y el permiso de anular). Este
validador compara el `CREATE` de cada tabla declarada contra eso.

  D1  · la tabla de dominio lleva las columnas de auditoría declaradas.
  D1  · la clave natural declarada tiene su `UNIQUE`.
  D1  · la clave foránea tiene índice.
  IM2 · la entidad inmutable tiene sus estados y sus campos de anulación.
  IM5 · la entidad inmutable tiene su permiso propio de anular.

Todo **AVISO**. Hay motivos legítimos para cada hallazgo —un estado que vive en
un catálogo, una tabla que hereda la auditoría de otra— y quien los conoce es
una persona, no este script.
"""
import os
import re

import codigo
import declaracion
import esquema
import instalar
import migraciones
import versionado
import comun
from comun import AVISO, Hallazgo, leer

_UNIQUE_PHP = re.compile(r"->\s*unique\s*\(([^)]*)\)")
_UNIQUE_SQL = re.compile(r"(?i)\bUNIQUE\b(?:\s+KEY)?(?:\s+[`\"\w]+)?\s*\(([^)]*)\)")
_INDICE_PHP = re.compile(r"->\s*(?:index|unique|primary|spatialIndex|fullText)"
                         r"\s*\(([^)]*)\)")
_INDICE_SQL = re.compile(r"(?i)\b(?:PRIMARY\s+KEY|UNIQUE(?:\s+KEY)?|KEY|INDEX)\b"
                         r"(?:\s+[`\"\w]+)?\s*\(([^)]*)\)")
_FK_AUTOINDEXADA = re.compile(r"->\s*(?:foreignId|foreignUlid|foreignUuid|"
                              r"constrained)\s*\(")
_FK_PHP = re.compile(r"->\s*foreign\s*\(\s*['\"]([^'\"]+)")
_FK_SQL = re.compile(r"(?i)FOREIGN\s+KEY\s*\(\s*[`\"\[]?(\w+)")


def _palabras(fragmento):
    """Los identificadores de un fragmento `(...)`, sin comillas ni corchetes."""
    return {p.strip(" `\"'[]") for p in fragmento.split(",") if p.strip(" `\"'[]")}


def _grupos(cuerpo, ruta, php, sql):
    ext = os.path.splitext(ruta.lower())[1]
    patron = php if ext == ".php" else sql
    return [_palabras(m.group(1)) for m in patron.finditer(cuerpo)]


def _columnas_sueltas_con(cuerpo, ruta, marca):
    """Columnas que traen la marca en su propia declaración (`->unique()`)."""
    salida = set()
    ext = os.path.splitext(ruta.lower())[1]
    if ext == ".php":
        for linea in cuerpo.splitlines():
            if marca in linea:
                m = re.search(r"->\s*\w+\s*\(\s*['\"]([^'\"]+)", linea)
                if m:
                    salida.add(m.group(1))
    else:
        for linea in cuerpo.splitlines():
            if marca.strip("->()").upper() in linea.upper():
                m = re.match(r"^\s*[`\"\[]?(\w+)[`\"\]]?\s+[A-Za-z]", linea)
                if m:
                    salida.add(m.group(1))
    return salida


def creaciones(raiz, d):
    """`{tabla: (ruta_mostrada, cuerpo, línea, ruta_original)}` de cada `CREATE`."""
    salida = {}
    for repo in instalar.repositorios_git(raiz):
        etiqueta = os.path.relpath(repo, raiz).replace("\\", "/")
        prefijo = "" if etiqueta == "." else f"{etiqueta}/"
        for archivo in versionado.archivos_versionados(repo):
            if not migraciones.es_candidata(archivo):
                continue
            if os.path.splitext(archivo.lower())[1] not in (".php", ".sql"):
                continue
            mostrada = f"{prefijo}{archivo}"
            if d.ignorado(mostrada):
                continue
            try:
                texto = leer(os.path.join(repo, archivo))
            except OSError:
                continue
            for tabla, cuerpo, linea in esquema.tablas_creadas(archivo, texto):
                salida[tabla.lower()] = (mostrada, cuerpo, linea, archivo)
    return salida


def _auditoria(entidad, cuerpo, ruta, mostrada, linea, d):
    declarado = d.convencion("auditoria.columnas")
    if not declarado:
        return []
    if declarado.lower().startswith("mecanismo:"):
        marca = declarado.split(":", 1)[1].strip()
        if marca and marca.lower() in cuerpo.lower():
            return []
        return [Hallazgo(AVISO, mostrada, linea,
                         f"la tabla `{entidad.tabla}` es de dominio y no usa "
                         f"`{marca}`, el mecanismo de auditoría declarado (D1)")]

    columnas = {n.lower() for n, _ in esquema.columnas_de(cuerpo, ruta)}
    faltan = [c for c in d.lista("auditoria.columnas") if c.lower() not in columnas]
    if not faltan:
        return []
    return [Hallazgo(AVISO, mostrada, linea,
                     f"la tabla `{entidad.tabla}` es de dominio y le faltan "
                     f"columnas de auditoría: {', '.join('`%s`' % c for c in faltan)} "
                     f"(D1)")]


def _unicidad(entidad, cuerpo, ruta, mostrada, linea):
    if not entidad.clave_natural:
        return []
    grupos = _grupos(cuerpo, ruta, _UNIQUE_PHP, _UNIQUE_SQL)
    grupos += [{c} for c in _columnas_sueltas_con(cuerpo, ruta, "->unique(")]
    grupos += [{c} for c in _columnas_sueltas_con(cuerpo, ruta, "UNIQUE")]
    clave = {c.lower() for c in entidad.clave_natural}
    for g in grupos:
        if clave <= {x.lower() for x in g}:
            return []
    return [Hallazgo(AVISO, mostrada, linea,
                     f"la clave natural de `{entidad.nombre}` "
                     f"({', '.join('`%s`' % c for c in entidad.clave_natural)}) "
                     f"no tiene `UNIQUE` en la tabla `{entidad.tabla}` (D1)")]


def _indices(entidad, cuerpo, ruta, mostrada, linea):
    ext = os.path.splitext(ruta.lower())[1]
    if ext == ".php":
        fks = {m.group(1) for m in _FK_PHP.finditer(cuerpo)}
    else:
        fks = {m.group(1) for m in _FK_SQL.finditer(cuerpo)}
    if not fks:
        return []
    indexadas = set()
    for g in _grupos(cuerpo, ruta, _INDICE_PHP, _INDICE_SQL):
        indexadas |= {x.lower() for x in g}
    if ext == ".php":
        # `foreignId()` y `constrained()` crean el índice solos: exigirlo otra
        # vez sería pedir un índice duplicado.
        for linea_txt in cuerpo.splitlines():
            if _FK_AUTOINDEXADA.search(linea_txt):
                m = re.search(r"['\"]([^'\"]+)['\"]", linea_txt)
                if m:
                    indexadas.add(m.group(1).lower())
    faltan = sorted(f for f in fks if f.lower() not in indexadas)
    if not faltan:
        return []
    return [Hallazgo(AVISO, mostrada, linea,
                     f"en `{entidad.tabla}`, la clave foránea "
                     f"{', '.join('`%s`' % f for f in faltan)} no tiene índice "
                     f"— D1 pide índice en lo que se filtra")]


def _inmutable(entidad, cuerpo, ruta, mostrada, linea, d):
    hallazgos = []
    estados = d.lista("inmutables.estados")
    if estados:
        vistos = [e for e in estados if re.search(
            r"['\"]" + re.escape(e) + r"['\"]", cuerpo)]
        if not vistos:
            hallazgos.append(Hallazgo(
                AVISO, mostrada, linea,
                f"`{entidad.nombre}` es inmutable y en el esquema de "
                f"`{entidad.tabla}` no aparece ninguno de los estados declarados "
                f"({', '.join(estados)}) — IM2. Si el estado sale de un catálogo, "
                f"no aplica"))
        elif len(vistos) < len(estados):
            faltan = [e for e in estados if e not in vistos]
            hallazgos.append(Hallazgo(
                AVISO, mostrada, linea,
                f"`{entidad.nombre}` es inmutable y le faltan estados en "
                f"`{entidad.tabla}`: {', '.join(faltan)} — IM2 pide los tres"))

    anulacion = d.lista("inmutables.anulacion")
    if anulacion:
        columnas = {n.lower() for n, _ in esquema.columnas_de(cuerpo, ruta)}
        faltan = [c for c in anulacion if c.lower() not in columnas]
        if faltan:
            hallazgos.append(Hallazgo(
                AVISO, mostrada, linea,
                f"`{entidad.nombre}` es inmutable y a `{entidad.tabla}` le faltan "
                f"campos de anulación: {', '.join('`%s`' % c for c in faltan)} "
                f"(IM2: cuándo, quién y por qué)"))
    return hallazgos


def recursos_con_permiso(raiz, patron, d):
    """Los recursos que ya tienen escrito su permiso, según el patrón declarado.

    Se lee el código versionado una sola vez: un `in` por entidad sobre todo el
    repositorio sería un recorrido por cada fila de la tabla de entidades.
    """
    if "<recurso>" not in patron:
        return set()
    regex = re.compile(re.escape(patron).replace(r"\<recurso\>", r"([\w.-]+)"))
    salida = set()
    for ruta, texto in codigo.archivos(raiz):
        if d.ignorado(ruta):
            continue
        for m in regex.finditer(texto):
            salida.add(m.group(1).lower())
    return salida


def validar(raiz):
    raiz = os.path.abspath(raiz)
    d = declaracion.leer_declaracion(raiz)
    if not d.tablas_de_dominio():
        return [Hallazgo(
            AVISO, raiz, 0,
            f"el proyecto no declara sus entidades en `{declaracion.DOMINIO}`: "
            f"el resto de D1 y todo 15 se quedan en criterio del agente")]

    creadas = creaciones(raiz, d)
    hallazgos = []

    for entidad in d.tablas_de_dominio():
        creada = creadas.get(entidad.tabla.lower())
        if not creada:
            hallazgos.append(Hallazgo(
                AVISO, os.path.join(raiz, declaracion.DOMINIO), 0,
                f"`{entidad.nombre}` declara la tabla `{entidad.tabla}` y ninguna "
                f"migración la crea"))
            continue
        mostrada, cuerpo, linea, ruta = creada
        hallazgos += _auditoria(entidad, cuerpo, ruta, mostrada, linea, d)
        hallazgos += _unicidad(entidad, cuerpo, ruta, mostrada, linea)
        hallazgos += _indices(entidad, cuerpo, ruta, mostrada, linea)
        if entidad.inmutable:
            hallazgos += _inmutable(entidad, cuerpo, ruta, mostrada, linea, d)

    patron = d.convencion("inmutables.permiso")
    if patron and d.inmutables():
        con_permiso = recursos_con_permiso(raiz, patron, d)
        for entidad in d.inmutables():
            candidatos = {entidad.nombre.lower(), entidad.tabla.lower()}
            if not (candidatos & con_permiso):
                hallazgos.append(Hallazgo(
                    AVISO, os.path.join(raiz, declaracion.DOMINIO), 0,
                    f"`{entidad.nombre}` es inmutable y no se encuentra su "
                    f"permiso `{patron.replace('<recurso>', entidad.nombre.lower())}` "
                    f"en el código (IM5: anular lleva permiso propio)"))
    return hallazgos


if __name__ == "__main__":
    # `53` · Un modulo que se ejecuta solo y no imprime nada dice, con su
    # silencio, lo mismo que diria si hubiera comprobado y estuviera todo bien.
    comun.no_es_punto_de_entrada()
