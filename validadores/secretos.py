#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Secretos incrustados en el código — `04·S4` y `00·N6`.

`versionado.py` (G3) mira **nombres** de archivo: que no se suba `.env` ni una
clave `.pem`. Esto es distinto y complementario: mira el **contenido** del código
versionado buscando un secreto escrito a mano —lo que G3 no ve— como
`const API_KEY = "sk_live_…"`.

Dos niveles, según cuánta duda deje la forma:

  FALLA — la forma **es** el secreto: clave AWS, bloque de clave privada, token
          de un proveedor (Stripe live, GitHub, Slack…). No hay lectura sana en
          que eso esté bien en el código. Igual que en G3, un secreto en git no
          se borra editándolo: queda en el historial. Por eso FALLA.
  AVISO — una variable con pinta de secreto asignada a un texto. Puede ser un
          placeholder o un dato de prueba; lo confirma un humano.

Solo lee archivos de **código/config** versionados (la lista `EXTENSIONES`). Los
`.md` quedan fuera a propósito: la documentación muestra secretos de ejemplo —el
propio estándar trae `API_KEY = "sk-live-abc123"` en `00·N6`— y marcarlos sería
ruido. La norma vive en los `.md`; aquí no se reescribe.
"""
import os
import re

import instalar
import versionado
import comun
from comun import AVISO, FALLA, Hallazgo

# Solo se abre esto. Deja fuera binarios, imágenes, lockfiles y documentación.
EXTENSIONES = {
    ".php", ".py", ".js", ".ts", ".jsx", ".tsx", ".vue", ".mjs", ".cjs",
    ".rb", ".go", ".java", ".kt", ".cs", ".rs", ".swift", ".scala",
    ".yml", ".yaml", ".ini", ".conf", ".cfg", ".toml", ".properties",
    ".sh", ".bash", ".ps1", ".xml", ".env",
}

# Nunca se abren, aunque su extensión esté arriba: son de terceros o generados.
SALTAR = re.compile(
    r"(^|/)(vendor|node_modules|dist|build|\.git)/|"
    r"(^|/)(composer\.lock|package-lock\.json|yarn\.lock|pnpm-lock\.yaml)$|"
    r"\.min\.(js|css)$")

# `61` · Lo que existe **para probar este detector** lo dispara siempre.
#
# Son claves falsas puestas a propósito: sin ellas no habría cómo comprobar que
# el detector detecta. Reportarlas es correcto en abstracto y **inservible en la
# práctica** — quien corre esto ve nueve fallas que nunca cambian, y la décima,
# que sí sería un secreto de verdad, se pierde entre ellas.
#
# **Se nombran una por una, no por carpeta.** Exceptuar `tests/` entero dejaría
# ciego al detector sobre todo lo que se escriba ahí mañana, que es exactamente
# el agujero por el que se cuela una clave real.
EXENTOS = (
    "validadores/tests/test_la_clave_no_llega_al_historico.py",
    "validadores/pruebas.py",
)

# FALLA — la forma sola ya delata un secreto real de un proveedor concreto.
SEGUROS = [
    (re.compile(r"AKIA[0-9A-Z]{16}"), "clave de acceso AWS"),
    (re.compile(r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY-----"),
     "bloque de clave privada"),
    (re.compile(r"\bsk_live_[0-9A-Za-z]{16,}"), "clave secreta de Stripe (live)"),
    (re.compile(r"\bSG\.[\w\-]{16,}\.[\w\-]{16,}"), "clave de SendGrid"),
    (re.compile(r"\bxox[baprs]-[0-9A-Za-z\-]{10,}"), "token de Slack"),
    (re.compile(r"\bgh[pousr]_[0-9A-Za-z]{20,}"), "token de GitHub"),
    (re.compile(r"\bglpat-[\w\-]{20,}"), "token de acceso de GitLab"),
    (re.compile(r"\bAIza[0-9A-Za-z_\-]{35}"), "clave de API de Google"),
]

# AVISO — variable con pinta de secreto = un literal de texto.
_ASIGNA = re.compile(
    r"(?i)\b(?P<clave>pass(?:word|wd)?|secret|api[_-]?key|apikey|"
    r"access[_-]?key|client[_-]?secret|auth[_-]?token|private[_-]?key)\b"
    r"\s*[:=]>?\s*(?P<comilla>['\"])(?P<valor>[^'\"]{6,})(?P=comilla)")

# La misma línea, si lee del entorno o de config, NO hardcodea: es lo correcto.
_ENTORNO = re.compile(
    r"(?i)\benv\b|getenv|os\.environ|process\.env|\bconfig\(|\$\{|\bimport\b")

# Valores que son claramente un molde, no un secreto de verdad. Dos formas: el
# valor entero es un molde (`changeme`, `xxxx`, `<...>`) o empieza como uno
# (`your-api-key`, `tu_clave`).
_MOLDE_EXACTO = re.compile(
    r"(?i)^(x{3,}|\.{3,}|\*{3,}|changeme|placeholder|dummy|sample|example|"
    r"ejemplo|null|none|password|secret|test|123456|abc123|<.+>)$")
_MOLDE_PREFIJO = re.compile(
    r"(?i)^(your|tu|my|mi|example|ejemplo|placeholder|sample|dummy|test|x{3,})"
    r"[_\- ]")


def _valor_sospechoso(valor):
    v = valor.strip()
    return not (_MOLDE_EXACTO.match(v) or _MOLDE_PREFIJO.match(v))


def revisar_texto(texto, donde="", hallazgos=None):
    """Núcleo puro: escanea un texto línea por línea. Aislado de git para
    probarlo sin un repositorio real."""
    if hallazgos is None:
        hallazgos = []
    for n, linea in enumerate(texto.splitlines(), 1):
        for patron, motivo in SEGUROS:
            if patron.search(linea):
                hallazgos.append(Hallazgo(
                    FALLA, donde, n, f"posible secreto en el código ({motivo}) · S4/N6"))
                break                       # un motivo por línea basta
        else:
            m = _ASIGNA.search(linea)
            if m and _valor_sospechoso(m.group("valor")) and not _ENTORNO.search(linea):
                hallazgos.append(Hallazgo(
                    AVISO, donde, n,
                    f"`{m.group('clave')}` asignada a un texto fijo — "
                    f"¿debería leerse del entorno? (S4)"))
    return hallazgos


def validar(raiz):
    raiz = os.path.abspath(raiz)
    hallazgos = []
    repos = instalar.repositorios_git(raiz)
    if not repos:
        return [Hallazgo(FALLA, raiz, 0, "no hay repositorios git que revisar")]

    for repo in repos:
        etiqueta = os.path.relpath(repo, raiz).replace("\\", "/")
        prefijo = "" if etiqueta == "." else f"{etiqueta}/"
        for archivo in versionado.archivos_versionados(repo):
            if SALTAR.search(archivo):
                continue
            if archivo.replace("\\", "/") in EXENTOS:
                continue        # `61` · datos de prueba del propio detector
            if os.path.splitext(archivo)[1].lower() not in EXTENSIONES:
                continue
            try:
                with open(os.path.join(repo, archivo),
                          encoding="utf-8", errors="replace") as f:
                    texto = f.read(1_000_000)   # 1 MB basta; más es dato, no código
            except OSError:
                continue
            revisar_texto(texto, f"{prefijo}{archivo}", hallazgos)

    return hallazgos


if __name__ == "__main__":
    # `53` · Un modulo que se ejecuta solo y no imprime nada dice, con su
    # silencio, lo mismo que diria si hubiera comprobado y estuviera todo bien.
    comun.no_es_punto_de_entrada("secretos")
