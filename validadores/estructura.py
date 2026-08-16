#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dónde vive el código y cómo se llama — `14·EST1` y `14·EST2`.

Las dos reglas dicen lo mismo en el fondo: que el nombre y la ubicación sean
**adivinables**. Ninguna de las dos se puede comprobar sobre la base, porque la
base es agnóstica (`20·M3`) y no sabe si aquí las tablas van en `snake_case` ni
si los módulos viven en `app/Modules/`. Eso lo declara el proyecto en
`.agente/mapeo-nombres.md` y en `.agente/dominio.md`, y este validador compara
el código contra esa declaración — no contra un gusto propio.

  EST1 · cada módulo declarado existe donde la convención dice, y ningún módulo
         del código se queda sin declarar.
  EST2 · tablas, columnas, clases, claves foráneas, booleanos y fechas de evento
         siguen la convención declarada.

**Sin declaración no corre.** Una clave en `libre` apaga su comprobación, y lo
que caiga en `legacy.ignorar` (`14·EST3`) no se mira: la convención es para lo
nuevo, y marcar el legacy que nadie va a renombrar es la forma más rápida de que
el validador se vuelva ruido.

Todo **AVISO**: el nombre puede tener un motivo que el script no ve (una tabla
impuesta por un sistema externo, una clase que exige el framework).
"""
import os
import re

import codigo
import declaracion
import esquema
import instalar
import migraciones
import versionado
from comun import AVISO, Hallazgo, leer

CASOS = {
    "snake_case": re.compile(r"^[a-z][a-z0-9]*(_[a-z0-9]+)*$"),
    "SCREAMING_SNAKE": re.compile(r"^[A-Z][A-Z0-9]*(_[A-Z0-9]+)*$"),
    "camelCase": re.compile(r"^[a-z][a-zA-Z0-9]*$"),
    "PascalCase": re.compile(r"^[A-Z][a-zA-Z0-9]*$"),
    "kebab-case": re.compile(r"^[a-z][a-z0-9]*(-[a-z0-9]+)*$"),
}

# Una declaración de tipo, en cualquiera de los lenguajes que se recorren.
_CLASE = re.compile(
    r"(?m)^\s*(?:export\s+)?(?:public\s+|final\s+|abstract\s+|sealed\s+|"
    r"internal\s+|static\s+)*(?:class|interface|trait|enum|struct)\s+"
    r"([A-Za-z_]\w*)")

# Claves foráneas, booleanos y fechas de evento, por cómo se declaran.
_FK_PHP = re.compile(r"->\s*(?:foreignId|foreignUlid|foreignUuid)\s*\(\s*['\"]([^'\"]+)")
_FK_PHP_EXPLICITA = re.compile(r"->\s*foreign\s*\(\s*['\"]([^'\"]+)")
_FK_SQL = re.compile(r"(?i)FOREIGN\s+KEY\s*\(\s*[`\"\[]?(\w+)")

_TIPOS_BOOL = {"boolean", "bool", "tinyint"}
_TIPOS_FECHA = {"timestamp", "timestamptz", "datetime", "dateTime", "dateTimeTz",
                "timestampTz"}


def cumple_caso(nombre, caso):
    """¿`nombre` está escrito en ese caso? True si el caso no se reconoce.

    Devolver True ante un caso desconocido es deliberado: si el proyecto declara
    algo que este validador no sabe leer, el problema es la declaración, y eso
    lo reporta `declaracion.py`. Marcar todos los nombres del proyecto por un
    valor mal escrito sería peor que no mirar.
    """
    patron = CASOS.get(caso)
    return True if not patron else bool(patron.match(nombre))


def _nombres_de_clase(texto):
    """`[(nombre, posición)]` de cada tipo declarado en el archivo."""
    return [(m.group(1), m.start(1)) for m in _CLASE.finditer(texto)]


def _fks_de(cuerpo, ruta):
    ext = os.path.splitext(ruta.lower())[1]
    if ext == ".php":
        return ([m.group(1) for m in _FK_PHP.finditer(cuerpo)]
                + [m.group(1) for m in _FK_PHP_EXPLICITA.finditer(cuerpo)])
    return [m.group(1) for m in _FK_SQL.finditer(cuerpo)]


def _carpetas_de_modulo(raiz, patron):
    """Los módulos que el **código** tiene, según el patrón declarado.

    Devuelve `{nombre_en_minúsculas: ruta mostrada}`. Se leen de los archivos
    versionados y no del disco: una carpeta que git no conoce no es del
    proyecto todavía.
    """
    partes = patron.replace("\\", "/").strip("/").split("/")
    if "<modulo>" not in partes:
        return {}
    indice = partes.index("<modulo>")
    prefijo = partes[:indice]

    encontrados = {}
    for repo in instalar.repositorios_git(raiz):
        etiqueta = os.path.relpath(repo, raiz).replace("\\", "/")
        marca = "" if etiqueta == "." else f"{etiqueta}/"
        for archivo in versionado.archivos_versionados(repo):
            trozos = archivo.replace("\\", "/").split("/")
            if len(trozos) <= indice or trozos[:indice] != prefijo:
                continue
            nombre = trozos[indice]
            encontrados.setdefault(nombre.lower(),
                                   marca + "/".join(trozos[:indice + 1]))
    return encontrados


def _est1(raiz, d):
    hallazgos = []
    patron = d.convencion("modulos.ruta")
    if not patron:
        return hallazgos

    en_codigo = _carpetas_de_modulo(raiz, patron)
    declarados = {m.nombre.lower(): m for m in d.modulos}

    for nombre, modulo in sorted(declarados.items()):
        esperada = patron.replace("<modulo>", modulo.nombre)
        if nombre not in en_codigo:
            hallazgos.append(Hallazgo(
                AVISO, os.path.join(raiz, declaracion.DOMINIO), 0,
                f"el módulo `{modulo.nombre}` está declarado pero no tiene "
                f"código en `{esperada}` (EST1)"))
            continue
        real = en_codigo[nombre]
        if modulo.carpeta and modulo.carpeta.strip("/") not in real.replace("\\", "/"):
            hallazgos.append(Hallazgo(
                AVISO, os.path.join(raiz, declaracion.DOMINIO), 0,
                f"el módulo `{modulo.nombre}` declara la carpeta "
                f"`{modulo.carpeta}` y su código está en `{real}` (EST1)"))

    for nombre, ruta in sorted(en_codigo.items()):
        if nombre not in declarados:
            hallazgos.append(Hallazgo(
                AVISO, ruta, 0,
                f"`{ruta}` encaja con la convención de módulos y no está "
                f"declarado en `{declaracion.DOMINIO}` (EST1 · 13·DOC13)"))
    return hallazgos


def _est2_migraciones(raiz, d):
    hallazgos = []
    caso_tabla = d.convencion("tablas.caso")
    caso_columna = d.convencion("columnas.caso")
    sufijos_fk = d.lista("fk.sufijo")
    prefijos_bool = d.lista("booleanos.prefijo")
    sufijos_fecha = d.lista("timestamps.sufijo")
    if not any((caso_tabla, caso_columna, sufijos_fk, prefijos_bool, sufijos_fecha)):
        return hallazgos

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
                if caso_tabla and not cumple_caso(tabla, caso_tabla):
                    hallazgos.append(Hallazgo(
                        AVISO, mostrada, linea,
                        f"la tabla `{tabla}` no sigue `{caso_tabla}`, la "
                        f"convención declarada (EST2)"))

                fks = {n.lower() for n in _fks_de(cuerpo, archivo)}
                for nombre, tipo in esquema.columnas_de(cuerpo, archivo):
                    if caso_columna and not cumple_caso(nombre, caso_columna):
                        hallazgos.append(Hallazgo(
                            AVISO, mostrada, linea,
                            f"la columna `{tabla}.{nombre}` no sigue "
                            f"`{caso_columna}` (EST2)"))
                    es_fk = (nombre.lower() in fks
                             or tipo.lower().startswith("foreign"))
                    if es_fk and sufijos_fk and not nombre.endswith(tuple(sufijos_fk)):
                        hallazgos.append(Hallazgo(
                            AVISO, mostrada, linea,
                            f"la clave foránea `{tabla}.{nombre}` no termina en "
                            f"{' ni '.join('`%s`' % s for s in sufijos_fk)} (EST2)"))
                    if (tipo.lower() in _TIPOS_BOOL and prefijos_bool
                            and not nombre.startswith(tuple(prefijos_bool))):
                        hallazgos.append(Hallazgo(
                            AVISO, mostrada, linea,
                            f"la columna booleana `{tabla}.{nombre}` no empieza "
                            f"por {' ni '.join('`%s`' % p for p in prefijos_bool)} "
                            f"(EST2)"))
                    if (tipo in _TIPOS_FECHA or tipo.lower() in _TIPOS_FECHA) and \
                            sufijos_fecha and not nombre.endswith(tuple(sufijos_fecha)):
                        hallazgos.append(Hallazgo(
                            AVISO, mostrada, linea,
                            f"la fecha de evento `{tabla}.{nombre}` no termina en "
                            f"{' ni '.join('`%s`' % s for s in sufijos_fecha)} (EST2)"))
    return hallazgos


def _est2_clases(raiz, d):
    caso = d.convencion("clases.caso")
    if not caso:
        return []
    hallazgos = []
    for ruta, texto in codigo.archivos(raiz):
        if d.ignorado(ruta):
            continue
        for nombre, pos in _nombres_de_clase(texto):
            if not cumple_caso(nombre, caso):
                hallazgos.append(Hallazgo(
                    AVISO, ruta, codigo.linea_de(texto, pos),
                    f"la clase `{nombre}` no sigue `{caso}`, la convención "
                    f"declarada (EST2)"))
    return hallazgos


def validar(raiz):
    raiz = os.path.abspath(raiz)
    d = declaracion.leer_declaracion(raiz)
    if not d.hay_algo():
        return [Hallazgo(
            AVISO, raiz, 0,
            f"el proyecto no declara su convención en `{declaracion.CONVENCIONES}` "
            f"ni su dominio en `{declaracion.DOMINIO}`: EST1 y EST2 se quedan "
            f"en criterio del agente")]
    return _est1(raiz, d) + _est2_migraciones(raiz, d) + _est2_clases(raiz, d)
