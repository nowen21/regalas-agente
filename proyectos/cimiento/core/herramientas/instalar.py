"""Deja instalado y operativo el agente en un proyecto que usa el estándar.

    python validadores/instalar.py                    # muestra el registro
    python validadores/instalar.py C:/ruta/proyecto   # simula (no toca nada)
    python validadores/instalar.py C:/ruta --aplicar  # instala de verdad
    python validadores/instalar.py --todos --aplicar  # en todos los del registro

**Una sola línea instala todo**: la estructura base, el `CLAUDE.md` con las rutas
de esta máquina, el `.gitignore`, `.agente/`, el histórico, la memoria, los
enganches de git y de la herramienta, el registro central y el de versión. Al
final comprueba el resultado y dice si algo quedó fuera.

**Es idempotente.** Lo que ya está al día no se toca, no se duplica y no se
pisa: los documentos que llena el proyecto solo se crean si faltan, y después
solo se les agrega lo que el estándar sumó.

**No pregunta.** Lo que ya está decidido se aplica; solo se reporta como
pendiente lo que exige una decisión del usuario.

**Por defecto solo simula.** Instalar cambia el comportamiento de un repositorio
ajeno, así que hay que pedirlo con `--aplicar`.

Las reglas y los validadores **no se copian**: los enganches los llaman en su
sitio, por ruta absoluta. Una sola copia del estándar sirve a todos los
proyectos. Los textos que se generan apuntan a `$ESTANDAR/validadores/`, que
sigue siendo la entrada de los enganches.
"""
import argparse
import importlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from datetime import datetime

from ..comun import Proyecto
from ..comun.consola import preparar_salida
from ..enganches.recuerdos import CARPETA as CARPETA_RECUERDOS
from ..enganches.recuerdos import INDICE as INDICE_RECUERDOS
from ..enganches.recuerdos import Recuerdos
from ..validadores.version import VersionDelEstandar
from ..validadores.versiones import POR_ID, CARPETA as CARPETA_VERSIONES
from ..validadores.versiones import DocumentosHeredados, RegistroDeVersiones, Sello

# Fila del registro: | Nombre | `ruta` | scope | stack |
_FILA = re.compile(r"^\|([^|]+)\|([^|]+)\|")

MARCA = "# generado por validadores/instalar.py del estándar del agente"

# Preámbulo común: localizar el intérprete y el estándar, o fallar diciendo por
# qué. Un enganche que calla cuando no puede correr es peor que no tenerlo.
_PREAMBULO = """#!/bin/sh
{marca}
# {descripcion}
#
# Se activa con:    git config core.hooksPath .githooks
# Se desactiva con: git config --unset core.hooksPath

ESTANDAR="{estandar}"

if command -v python > /dev/null 2>&1; then
    PY=python
elif command -v python3 > /dev/null 2>&1; then
    PY=python3
else
    echo "{nombre}: no se encontró Python; no se pudo revisar." >&2
    echo "Instala Python o desactiva: git config --unset core.hooksPath" >&2
    exit 1
fi

if [ ! -f "$ESTANDAR/validadores/validar.py" ]; then
    echo "{nombre}: no se encontró el estándar en $ESTANDAR" >&2
    echo "Reinstala el enganche o desactiva: git config --unset core.hooksPath" >&2
    exit 1
fi
"""

PLANTILLA_COMMIT_MSG = _PREAMBULO + """
"$PY" "$ESTANDAR/validadores/validar.py" commit --archivo "$1" || {{
    echo "" >&2
    echo "Commit rechazado: corrige el mensaje y vuelve a intentar." >&2
    exit 1
}}
"""

PLANTILLA_PRE_COMMIT = _PREAMBULO + """
# Solo lo que entra en ESTE commit — no el repositorio entero. Ver G3.
"$PY" "$ESTANDAR/validadores/validar.py" versionado --raiz "$(pwd)" --preparados || {{
    echo "" >&2
    echo "Commit rechazado: saca del commit lo que no debe versionarse." >&2
    exit 1
}}
# `00·ID8` · **Trinquete**: no bloquea las marcas que ya están, bloquea que
# suban. Bloquear todas rechazaría casi todos los commits, y un enganche que
# rechaza siempre se apaga en una tarde.
"$PY" "$ESTANDAR/validadores/validar.py" marcas --raiz "$(pwd)" --preparados || {{
    echo "" >&2
    echo "Commit rechazado: quita las marcas nuevas y vuelve a intentar." >&2
    exit 1
}}
# `EP-023 - HU-007` - Lo que entra en el commit contra el plan aprobado de la
# fase que toca. Solo compara los planes aprobados desde 48.0.0.
"$PY" "$ESTANDAR/validadores/validar.py" plan --raiz "$(pwd)" --preparados || {{
    echo "" >&2
    echo "Commit rechazado: el plan no declara ese archivo ni una regla lo autoriza." >&2
    exit 1
}}
# `80` - Que el commit no se lleve el trabajo de otra sesion. **Avisa y deja
# pasar**: retomar lo que otra dejo a medias a veces es lo correcto; hacerlo
# sin darse cuenta, no. Por eso no lleva `|| exit`.
"$PY" "$ESTANDAR/validadores/validar.py" sesiones --raiz "$(pwd)" || true
"""

# `09·08` · **Publicar es lo que no se deshace**: la batería completa corre antes
# de publicar y no en cada commit, donde costaría minutos por vez y alguien
# apagaría el enganche. Solo lo que se comprueba en seco: linter, suite y audit
# fallarían en cualquier repositorio que no los tenga.
PLANTILLA_PRE_PUSH = _PREAMBULO + """
echo "pre-push: corriendo la batería antes de publicar…"

# Lo que **detiene**: enlaces rotos, índices desactualizados, que lo que se
# publica esté versionado, que ninguna regla del núcleo se publique sin decir
# quién la hace cumplir, y que ninguna regla se publique sin decir a qué tareas
# aplica. Son defectos nuevos, y salen del trabajo de hoy.
#
# `ejecutable` y `tareas` no le cuestan nada a un proyecto: miran `base/`, que
# solo existe en el estándar. Donde no hay reglas, no hay nada que reportar.
FALLO=0
for SUB in estandar versionado ejecutable tareas; do
    "$PY" "$ESTANDAR/validadores/validar.py" "$SUB" --raiz "$(pwd)" || FALLO=1
done

# Lo que **informa y no detiene**: el cuerpo de reglas contra su propio molde.
# Un estándar con deuda conocida —reglas publicadas que no pasan su checklist—
# no puede impedir publicar cualquier otra cosa: eso convierte el enganche en
# un obstáculo permanente, y a la semana alguien lo apaga con --no-verify.
# **Se ve, y no bloquea**, hasta que la deuda se cierre.
"$PY" "$ESTANDAR/validadores/validar.py" metareglas --raiz "$(pwd)" ||     echo "pre-push: hay reglas que no pasan su propio checklist (no detiene)."

# **Reclama, no corre.** Las pruebas del propio estándar tardan ~10 minutos y
# este repositorio hace 16 commits por día: correrlas acá costaría 39 horas
# cada dos semanas, y un peaje así se apaga en una tarde. Esto solo mira una
# fecha y dice si hay commits que esas pruebas no vieron.
"$PY" "$ESTANDAR/validadores/validar.py" internas --reclamo || true

if [ "$FALLO" -ne 0 ]; then
    echo "" >&2
    echo "Push rechazado: la batería encontró fallas." >&2
    echo "Corrígelas, o salta el enganche a propósito con --no-verify." >&2
    exit 1
fi
"""

# `EP-005·HU-019` · **El hash del commit se anota solo**, después del commit
# porque antes no existe. El archivo queda modificado y entra en el commit
# siguiente: reescribir el commit se muerde la cola y un segundo commit
# automático cruza `00·N1`. **Nunca falla el commit**: ya está hecho.
PLANTILLA_POST_COMMIT = _PREAMBULO + """
"$PY" "$ESTANDAR/adaptadores/claude-code/hook_estacion.py" --raiz "$(pwd)" || true
exit 0
"""

HOOKS = [
    ("commit-msg", PLANTILLA_COMMIT_MSG,
     "Revisa el mensaje del commit antes de aceptarlo (09-git.md · G2, G8)."),
    ("pre-commit", PLANTILLA_PRE_COMMIT,
     "Revisa que no entren secretos ni artefactos (09-git.md · G3)."),
    ("pre-push", PLANTILLA_PRE_PUSH,
     "Corre la batería antes de publicar (09-git.md · G6 · 00-nucleo-blindado.md · N2)."),
    ("post-commit", PLANTILLA_POST_COMMIT,
     "Anota el hash en la fase que el commit cierra (EP-005·HU-019). Nunca falla."),
]

# Enganches de Claude Code: (evento, matcher, guion, mensaje, argumentos).
# `matcher` en None = el evento no filtra por herramienta (SessionStart).
# `argumentos` deja que un mismo guion sirva a dos eventos con papeles distintos,
# como el histórico: uno anota al usuario y el otro al agente.
HOOKS_CLAUDE = [
    ("PostToolUse", "Write|Edit", "hook_md.py",
     "Revisando los enlaces del proyecto...", ""),
    ("SessionStart", None, "hook_sesion.py",
     "Revisando el estándar...", ""),
    ("UserPromptSubmit", None, "hook_historico.py",
     "Anotando en el histórico...", "--modo usuario"),
    ("Stop", None, "hook_historico.py",
     "Anotando en el histórico...", "--modo agente"),
    # `EP-023 · HU-001 · fase B`: la conversación pasa sola al análisis
    # prendido. Al cerrar el turno no hay enganche propio: la respuesta la pasa
    # `hook_historico.py` apenas la escribe, porque dos enganches del mismo
    # evento corren a la vez y el del análisis copiaba antes de que la
    # respuesta existiera (H-9 de la sesión del 2026-10-01).
    ("UserPromptSubmit", None, "hook_analisis.py",
     "Revisando el análisis en curso...", "--modo mensaje"),
    ("UserPromptSubmit", None, "hook_checklist.py",
     "Revisando la instalación del agente...", ""),
    # Al abrir la sesión no se cargan las reglas: la herramienta acepta 10.000
    # caracteres por enganche (`EP-005 · HU-009 · CA-04`). Este enganche
    # entrega con cada mensaje las reglas de las tareas que pide
    # (`recuperar.py`), recuerda las de cada turno, y devuelve al turno
    # siguiente la cuenta que `hook_redaccion.py` imprime donde nadie la ve.
    ("UserPromptSubmit", None, "hook_reglas.py",
     "Recordando las reglas de cada turno...", ""),
    # `EP-023 · HU-002 · CA-04`: los acuerdos de la fase en curso y del
    # análisis prendido llegan con cada mensaje, en un enganche propio porque
    # el tope es por enganche y el de las reglas va casi lleno.
    ("UserPromptSubmit", None, "hook_acuerdos.py",
     "Trayendo los acuerdos de lo que se trabaja...", ""),
    ("SessionStart", None, "hook_recuerdos.py",
     "Recogiendo la memoria del agente...", ""),
    ("PostToolUse", "Write|Edit", "hook_recuerdos.py",
     "Recogiendo la memoria del agente...", ""),
    ("SessionStart", None, "hook_resumen.py",
     "Preparando el resumen de la sesión...", "--modo inicio"),
    ("UserPromptSubmit", None, "hook_resumen.py",
     "Revisando el resumen de la sesión...", "--modo aviso"),
    ("UserPromptSubmit", None, "hook_senales.py",
     "Revisando las señales del proyecto...", ""),
    ("PostToolUse", "Write|Edit", "hook_relacionadas.py",
     "Buscando las reglas relacionadas...", ""),
    # `EP-005 · HU-020`: al terminar el turno, el registro anota lo que
    # cambió, mire quien lo mire, para que la comprobación de sesiones no tenga
    # el hueco por el que entraban líneas ajenas.
    ("Stop", None, "hook_turno.py",
     "Anotando lo que tocó este turno...", ""),
    # `EP-005·HU-012`: al cerrar el turno, se mide como quedo escrito lo que
    # el agente acaba de decir. Tres reglas del nucleo hablan de eso y ninguna
    # tenia quien la hiciera cumplir. Mide y no detiene: cuando esto corre, el
    # texto ya salio, asi que lo unico que se puede hacer es dejarlo a la vista.
    ("Stop", None, "hook_redaccion.py",
     "Midiendo como quedo escrito el turno...", ""),
    ("Stop", None, "hook_presupuesto.py",
     "Sumando el consumo de la sesión...", ""),
    ("UserPromptSubmit", None, "hook_presupuesto.py",
     "Midiendo el consumo de la sesión...", "--modo aviso"),
    ("PostToolUse", "Write|Edit", "hook_checkpoint.py",
     "Revisando el checkpoint de la fase...", ""),
    ("PostToolUse", "Write|Edit", "hook_veredicto.py",
     "Copiando el veredicto de la fase...", ""),
    # `EP-005 · HU-018`: avisa si el archivo cayó fuera del proyecto. La regla
    # ya existía (`04·S9`) y se incumplió cuatro días seguidos, porque la
    # herramienta ofrece una carpeta temporal y la nombra como el sitio
    # recomendado: el camino cómodo apunta al lado contrario.
    ("PostToolUse", "Write|Edit", "hook_rutas.py",
     "Mirando dónde quedó lo que se escribió...", ""),
    # El portero (`EP-005 · HU-015`): lo que llega de afuera llega marcado.
    # El filtro es regex; el programa vuelve a decidir por si deja pasar de más.
    ("PostToolUse", "WebFetch|WebSearch|Read|mcp__.*", "hook_externo.py",
     "Marcando lo que llegó de afuera...", ""),
    # `EP-005 · HU-023 · RN-10`: ninguna escritura sale del proyecto. Obligar a
    # leer las reglas antes de actuar se quitó el 2026-09-29: llenaba la
    # conversación de lecturas y no hacía cumplir nada.
    # `EP-023 · HU-007 · CA-02`: el freno corre antes de toda acción, sin filtro
    # de herramienta, y después de cada orden de consola compara lo que cambió.
    ("PreToolUse", None, "hook_antes.py",
     "Revisando la acción contra el plan y lo autorizado...", "--modo accion"),
    ("PostToolUse", "Bash|PowerShell", "hook_despues.py",
     "Comparando lo que cambió con el plan...", ""),
]

# **Dónde vive el adaptador de esta herramienta.** `validadores/` es lo que sirve
# con cualquier agente; esto existe porque esta herramienta lo llama. Cambiar la
# ruta vence el enganche de todos los proyectos instalados, y el checklist lo
# reporta en el primer mensaje de la siguiente sesión.
ADAPTADOR = "adaptadores/claude-code"

TEXTO_RESUMENES = """# Lo que dejó cada sesión

Una carpeta por día y un archivo por sesión: `AAAA-MM-DD/«tema».md`. Las crea el
enganche del resumen en el primer mensaje de la sesión, con el modelo del
estándar puesto.

**Se arranca por acá, no por la transcripción.** La transcripción de
`historico-chat/` guarda lo que se dijo, y es larga. Acá queda lo que la sesión
**dejó**: los hallazgos, qué se decidió en cada uno y qué quedó abierto.

Llenarlo es del agente: reconocer un hallazgo es criterio, y el programa solo
deja el hueco a la vista.
"""

# `02·F13`: el código del usuario en `proyectos/`, y al lado el espacio del
# agente. Se crean vacías: qué va adentro lo decide el usuario. `pendientes/`
# ya no va (`EP-023·HU-003`): cada pendiente vive dentro de lo que lo origina, y
# la de la raíz queda como historia donde ya existe.
CARPETAS_BASE = ["proyectos", "documentacion", "prompts"]

# Los 4 archivos de configuración del proyecto. La lista vive acá porque es el
# instalador quien los pone; el checklist la lee de acá (`20·M2`).
CONFIG_AGENTE = ["stack.md", "dominio.md", "mapeo-nombres.md",
                 "marco-normativo.md"]

# Lo que no es del repositorio: configuración local y el estado de trabajo que
# escriben los enganches. El checklist lee esta lista de acá (`20·M2`).
IGNORADOS = ["CLAUDE.md", ".agente/", "historico-chat/.tocado/"]

# Los ajustes del punto 5 del `CLAUDE.md` son del proyecto y no se tocan ni por
# error; el resto tampoco se pisa a ciegas (ver `sincronizar_secciones`).
SECCIONES_DEL_PROYECTO = ("5.1", "5.2")

# Lo que la plantilla deja marcado para que lo llene el instalador: sale de esta
# máquina, de la carpeta del proyecto y del `VERSION` del estándar.
_MARCADOR = re.compile(r"«(?!…»)[^»\n]+»")

# `EP-023·HU-007·CA-02` · La integración continua revisa que lo que trae cada
# cambio esté en el plan aprobado. Se agrega donde el proyecto ya tiene
# integración continua; de dónde se descarga Cimiento es un dato del proyecto y
# el instalador no lo vuelve a tocar.
CI_GITHUB = ".github/workflows/cimiento.yml"
CI_GITLAB = ".cimiento-ci.yml"
_CI_OTROS = ("azure-pipelines.yml", "bitbucket-pipelines.yml", "Jenkinsfile",
             ".circleci/config.yml", ".drone.yml", ".travis.yml")
_CI_AVISO = """# Lo escribió el instalador de Cimiento (EP-023, HU-007, CA-02): revisa que lo
# que trae cada cambio esté en el plan aprobado de su fase.
# CIMIENTO_REPO dice de dónde se descarga Cimiento. Es un dato del proyecto: se
# cambia aquí, y el instalador no lo vuelve a tocar.
"""
_CI_DESDE = ('if [ -z "$DESDE" ] || ! git cat-file -e "$DESDE^{commit}" 2>/dev/null; '
             'then DESDE="$(git rev-list --max-parents=0 HEAD | tail -1)"; fi')
PLANTILLA_CI_GITHUB = _CI_AVISO + """name: Cimiento
on: [push, pull_request]
jobs:
  plan:
    runs-on: ubuntu-latest
    env:
      CIMIENTO_REPO: __REPO__
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: Descargar Cimiento
        run: git clone --depth 1 "$CIMIENTO_REPO" "$RUNNER_TEMP/cimiento"
      - name: Lo que trae el cambio contra el plan
        run: |
          DESDE="${{ github.event.pull_request.base.sha || github.event.before }}"
          __DESDE__
          python3 "$RUNNER_TEMP/cimiento/validadores/validar.py" plan --raiz "$GITHUB_WORKSPACE" --rango "$DESDE..HEAD"
"""
PLANTILLA_CI_GITLAB = _CI_AVISO + """cimiento-plan:
  image: python:3.12
  variables:
    CIMIENTO_REPO: __REPO__
    GIT_DEPTH: 0
  script:
    - git clone --depth 1 "$CIMIENTO_REPO" /tmp/cimiento
    - DESDE="${CI_MERGE_REQUEST_DIFF_BASE_SHA:-$CI_COMMIT_BEFORE_SHA}"
    - __DESDE__
    - python3 /tmp/cimiento/validadores/validar.py plan --raiz "$CI_PROJECT_DIR" --rango "$DESDE..HEAD"
"""


def _leer(ruta):
    try:
        with open(ruta, encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError:
        with open(ruta, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def _mandar_git(ruta, *args):
    return subprocess.run(["git", "-C", ruta, *args],
                          capture_output=True, text=True, encoding="utf-8")


def _escribir(ruta, texto):
    os.makedirs(os.path.dirname(ruta) or ".", exist_ok=True)
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


class Plantillas:
    """Lo que el instalador hace con el texto: rellenar marcadores, partir por
    secciones y sincronizar sin pisar lo que escribió el proyecto."""

    @staticmethod
    def slug(texto):
        """`Proyecto de grado` da `proyecto-de-grado`. Sin tildes ni espacios."""
        plano = unicodedata.normalize("NFKD", texto)
        plano = plano.encode("ascii", "ignore").decode("ascii")
        return re.sub(r"[^a-z0-9]+", "-", plano.lower()).strip("-") or "proyecto"

    @staticmethod
    def partir(texto):
        """`(preámbulo, [(título, líneas)])`, partido por cada `##` o menor.

        El preámbulo (el H1 y lo de antes del primer `##`) va aparte porque lleva
        el nombre del proyecto y nunca coincide con la plantilla.
        """
        preambulo = []
        salida = []
        dentro_de_codigo = False
        for linea in texto.splitlines():
            if linea.lstrip().startswith("```"):
                dentro_de_codigo = not dentro_de_codigo
            m = None if dentro_de_codigo else re.match(r"^(#{2,6})\s+(.*)$", linea)
            if m:
                salida.append((m.group(2).strip(), [linea]))
            elif salida:
                salida[-1][1].append(linea)
            else:
                preambulo.append(linea)
        return preambulo, salida

    @classmethod
    def secciones(cls, texto):
        """`[(título, líneas)]` por cada encabezado `##` o menor. Ignora el H1."""
        return cls.partir(texto)[1]

    @classmethod
    def completar_secciones(cls, local, plantilla):
        """Agrega al final las secciones que la plantilla tiene y el local no.

        `01·C18` es aditiva: nunca se pisa, se reordena ni se borra. La sección
        va **con su texto**, para que la instalación quede operativa.
        """
        presentes = {t for t, _ in cls.secciones(local)}
        faltan = [(t, cuerpo) for t, cuerpo in cls.secciones(plantilla) if t not in presentes]
        if not faltan:
            return local, []
        partes = [local.rstrip("\n")]
        for _, cuerpo in faltan:
            partes.append("\n".join(cuerpo).rstrip("\n"))
        return "\n\n".join(partes) + "\n", [t for t, _ in faltan]

    @staticmethod
    def es_del_proyecto(titulo):
        return titulo.lstrip().startswith(SECCIONES_DEL_PROYECTO)

    @staticmethod
    def mismo_texto(a, b):
        return [l.rstrip() for l in a] == [l.rstrip() for l in b]

    @classmethod
    def sincronizar_secciones(cls, local, plantilla, base):
        """Pone al día el texto del estándar sin pisar lo que el proyecto escribió.

        Comparación de tres vías: `base` es la plantilla contra la que se selló la
        vez pasada. Una sección se reemplaza solo si el proyecto **no la tocó**
        (su texto local sigue igual a la base). Sin base no se reemplaza nada:
        ante la duda manda el proyecto (`01·C18`).

        Devuelve `(texto, [puestas al día], [las que el proyecto tocó y quedaron viejas])`.
        """
        pre_local, secciones_local = cls.partir(local)
        de_plantilla = dict(cls.partir(plantilla)[1])
        de_base = dict(cls.partir(base)[1]) if base else {}

        al_dia, a_mano = [], []
        cuerpo = []
        for titulo, lineas in secciones_local:
            nueva = de_plantilla.get(titulo)
            vieja = de_base.get(titulo)
            cambio_la_plantilla = (vieja is not None and nueva is not None
                                   and not cls.mismo_texto(vieja, nueva))
            if nueva is None or cls.es_del_proyecto(titulo) or cls.mismo_texto(lineas, nueva):
                cuerpo.extend(lineas)
            elif vieja is not None and cls.mismo_texto(lineas, vieja):
                cuerpo.extend(nueva)
                al_dia.append(titulo)
            else:
                cuerpo.extend(lineas)
                # Solo se avisa de lo que la plantilla cambió y no se pudo
                # aplicar: lo demás es asunto del proyecto, y avisarlo en cada
                # corrida es el ruido que apaga los avisos de verdad.
                if cambio_la_plantilla:
                    a_mano.append(titulo)

        if not al_dia:
            return local, [], a_mano
        return "\n".join(pre_local + cuerpo).rstrip("\n") + "\n", al_dia, a_mano


class Instalador:
    """El instalador del estándar que vive en `estandar` (por defecto, este)."""

    def __init__(self, estandar=None):
        self.estandar = estandar or Proyecto.estandar()
        self.registro = os.path.join(self.estandar, "plantillas", "proyectos.md")
        self.plantilla_historico = os.path.join(self.estandar, "plantillas", "historico-chat.md")
        self.plantilla_memoria = os.path.join(self.estandar, "plantillas", "memoria.md")

    # ── lo que se sabe sin instalar nada ─────────────────────────────────

    def proyectos_registrados(self):
        """Lee `plantillas/proyectos.md` y devuelve `[(nombre, ruta), ...]`."""
        if not os.path.isfile(self.registro):
            return []
        salida = []
        for linea in _leer(self.registro).splitlines():
            m = _FILA.match(linea.strip())
            if not m:
                continue
            nombre, ruta = m.group(1).strip(), m.group(2).strip()
            # Se saltan el encabezado y la línea de guiones de la tabla.
            if not ruta.startswith("`") or nombre.lower() == "proyecto":
                continue
            salida.append((nombre, ruta.strip("`").strip()))
        return salida

    @staticmethod
    def cumple_f13(ruta):
        """El arranque de `02·F13`: ¿existe la carpeta `proyectos/`? Si falta, el
        instalador la crea vacía; qué va adentro es del usuario."""
        return os.path.isdir(os.path.join(ruta, "proyectos"))

    def es_el_estandar(self, ruta):
        """¿`ruta` es la carpeta del propio estándar? No tiene `proyectos/`, y su
        `CLAUDE.md` se versiona: ignorarlo borraría el instructivo del estándar."""
        return os.path.normcase(os.path.abspath(ruta)) == os.path.normcase(self.estandar)

    @staticmethod
    def es_repositorio_git(ruta):
        """¿`ruta` es la raíz de un repositorio (no una subcarpeta de otro)?"""
        return os.path.isdir(os.path.join(ruta, ".git"))

    @classmethod
    def repositorios_git(cls, ruta):
        """La raíz si es repositorio, más cada repositorio de `proyectos/`: según
        `02·F13` el código puede ser uno o varios repositorios independientes."""
        encontrados = [ruta] if cls.es_repositorio_git(ruta) else []
        proyectos = os.path.join(ruta, "proyectos")
        if os.path.isdir(proyectos):
            for nombre in sorted(os.listdir(proyectos)):
                sub = os.path.join(proyectos, nombre)
                if os.path.isdir(sub) and cls.es_repositorio_git(sub):
                    encontrados.append(sub)
        return encontrados

    @staticmethod
    def enganches_enchufados():
        """Los guiones del adaptador que la instalación conecta, por los dos
        canales: `.claude/settings.json` y los enganches de git. Se deriva de las
        mismas plantillas que se escriben, no de una lista aparte (`S-091`)."""
        salida = {g for _e, _m, g, _msg, _a in HOOKS_CLAUDE}
        for _nombre, plantilla, _desc in HOOKS:
            salida |= set(re.findall(r"adaptadores/claude-code/(\w+\.py)", plantilla))
        return sorted(salida)

    @staticmethod
    def hook_claude(estandar, proyecto, guion, mensaje, argumentos=""):
        extra = f"{argumentos} " if argumentos else ""
        return {
            "type": "command",
            "command": (f'python "{estandar}/{ADAPTADOR}/{guion}" '
                        f'{extra}--raiz "{proyecto}"'),
            "statusMessage": mensaje,
        }

    def version_estandar(self):
        return VersionDelEstandar.vigente(self.estandar)

    # ── los enganches ────────────────────────────────────────────────────

    def instalar_git(self, ruta, estandar, aplicar):
        """Escribe los enganches en `.githooks/` y apunta `core.hooksPath` ahí."""
        pasos = []
        carpeta = os.path.join(ruta, ".githooks")

        actual = _mandar_git(ruta, "config", "--get", "core.hooksPath").stdout.strip()
        if actual and actual != ".githooks":
            return [f"OMITIDO: core.hooksPath ya apunta a «{actual}» — "
                    f"no se pisa; revísalo a mano"]

        for nombre, plantilla, descripcion in HOOKS:
            archivo = os.path.join(carpeta, nombre)
            contenido = plantilla.format(marca=MARCA, estandar=estandar,
                                         nombre=nombre, descripcion=descripcion)
            if os.path.isfile(archivo) and _leer(archivo) == contenido:
                pasos.append(f"{nombre} ya estaba al día")
                continue
            pasos.append(f"escribir {os.path.join('.githooks', nombre)}")
            if aplicar:
                os.makedirs(carpeta, exist_ok=True)
                with open(archivo, "w", encoding="utf-8", newline="\n") as f:
                    f.write(contenido)
                os.chmod(archivo, 0o755)

        if actual == ".githooks":
            pasos.append("core.hooksPath ya estaba puesto")
        else:
            pasos.append("git config core.hooksPath .githooks")
            if aplicar:
                _mandar_git(ruta, "config", "core.hooksPath", ".githooks")

        return pasos + self.rutas_largas(ruta, aplicar)

    @staticmethod
    def rutas_largas(ruta, aplicar):
        """`EP-007·HU-009` · `core.longpaths`, sin pisar lo que alguien decidió.

        En Windows una ruta de más de 260 caracteres detiene el guardado, y
        ningún cambio de nombres crea la holgura que falta. Se pone en cualquier
        sistema (fuera de Windows es inerte). No viaja al clonar: vive en
        `.git/config`, y por eso el documento de despliegue dice qué hacer.
        """
        actual = _mandar_git(ruta, "config", "--get", "core.longpaths").stdout.strip().lower()
        if actual == "false":
            # Quien lo puso así tendrá su motivo: la misma cortesía que con
            # `core.hooksPath`.
            return ["OMITIDO: core.longpaths está en «false» — no se pisa. "
                    "Sin él, en Windows una ruta de más de 260 caracteres detiene "
                    "el guardado"]
        if actual == "true":
            return ["core.longpaths ya estaba puesto"]
        if aplicar:
            _mandar_git(ruta, "config", "core.longpaths", "true")
        return ["git config core.longpaths true"]

    def instalar_claude(self, ruta, estandar, aplicar):
        """Agrega los enganches de Claude Code al `.claude/settings.json`."""
        pasos = []
        carpeta = os.path.join(ruta, ".claude")
        archivo = os.path.join(carpeta, "settings.json")
        destino = os.path.join(".claude", "settings.json")

        datos = {}
        if os.path.isfile(archivo):
            try:
                datos = json.loads(_leer(archivo))
            except (json.JSONDecodeError, ValueError):
                return ["OMITIDO: .claude/settings.json tiene JSON inválido — "
                        "no se toca; arréglalo a mano"]

        cambios = False
        for evento, matcher, guion, mensaje, argumentos in HOOKS_CLAUDE:
            nuevo = self.hook_claude(estandar, ruta.replace("\\", "/"), guion, mensaje, argumentos)

            # Se respeta lo que ya hubiera; solo se toca el grupo propio.
            ganchos = datos.setdefault("hooks", {}).setdefault(evento, [])

            # Un guion vive en un solo grupo por evento: si cambió su filtro, la
            # entrada vieja sale del grupo anterior en vez de correr dos veces.
            for otro in [g for g in ganchos if g.get("matcher") != matcher]:
                antes = len(otro.get("hooks", []))
                otro["hooks"] = [h for h in otro.get("hooks", []) if guion not in (h.get("command") or "")]
                if len(otro["hooks"]) != antes:
                    pasos.append(f"quitar el enganche {evento} viejo de {destino}")
                    cambios = True
            ganchos[:] = [g for g in ganchos if g.get("hooks")]
            grupo = next((g for g in ganchos if g.get("matcher") == matcher), None)
            if grupo is None:
                grupo = {"hooks": []}
                if matcher:
                    grupo["matcher"] = matcher
                ganchos.append(grupo)

            # Un enganche propio se reconoce por el guion al que llama, no por el
            # comando exacto: así una versión anterior se reemplaza y no queda
            # duplicada corriendo en paralelo.
            propios = [i for i, h in enumerate(grupo["hooks"]) if guion in (h.get("command") or "")]
            if len(propios) == 1 and grupo["hooks"][propios[0]] == nuevo:
                pasos.append(f"enganche {evento} ya estaba puesto")
                continue
            if propios:
                for i in reversed(propios):
                    grupo["hooks"].pop(i)
                pasos.append(f"reemplazar el enganche {evento} en {destino}")
            else:
                pasos.append(f"agregar enganche {evento} a {destino}")
            grupo["hooks"].append(nuevo)
            cambios = True

        if cambios and aplicar:
            os.makedirs(carpeta, exist_ok=True)
            with open(archivo, "w", encoding="utf-8") as f:
                json.dump(datos, f, indent=2, ensure_ascii=False)
                f.write("\n")
        return pasos

    # ── los documentos heredados ─────────────────────────────────────────

    def instalar_stack(self, ruta, aplicar):
        """Copia el stack de instalación a `.agente/`, sellado con su huella.

        Esta copia **sí** se pisa: no la llena nadie, es el retrato de lo que el
        estándar exige hoy. Comparar su huella con la del original delata que
        hay componentes nuevos.
        """
        # Aquí y no arriba: el checklist usa al instalador, y sería un ciclo.
        from ..validadores.checklist import Checklist

        original = Checklist.ruta_plantilla(self.estandar)
        if not os.path.isfile(original):
            return ["OMITIDO: falta plantillas/stack-instalacion.md en el estándar"]

        destino = os.path.join(ruta, ".agente", "stack-instalacion.md")
        if Checklist.huella_instalada(ruta) == Checklist.huella(self.estandar):
            # "Al día" es contra la plantilla, y una copia puede estar al día y
            # mal escrita a la vez.
            return (self.reparar_marcadores(destino, ruta, aplicar, ".agente/stack-instalacion.md")
                    or ["stack de instalación ya estaba al día"])

        if aplicar:
            os.makedirs(os.path.dirname(destino), exist_ok=True)
            cuerpo = self.rellenar(_leer(original), self.rellenos(ruta))
            with open(destino, "w", encoding="utf-8", newline="\n") as f:
                f.write(cuerpo + Checklist.sello(self.estandar))
        return ["copiar .agente/stack-instalacion.md"]

    def instalar_historico(self, ruta, aplicar):
        """Crea `historico-chat/` con su README desde la plantilla del estándar.

        Va aquí y no en un enganche: crear carpetas por su cuenta sorprende; el
        instalador se corre a propósito y dice qué hace. Si el README existe no
        se pisa, pero se le agrega lo que la plantilla sumó (`01·C18`, aditivo)
        y se le refresca el sello.
        """
        comp = POR_ID["historico"]
        carpeta = os.path.join(ruta, "historico-chat")
        archivo = os.path.join(carpeta, "README.md")

        if not os.path.isfile(self.plantilla_historico):
            return ["OMITIDO: falta plantillas/historico-chat.md en el estándar"]

        if not os.path.isfile(archivo):
            if aplicar:
                os.makedirs(carpeta, exist_ok=True)
                self.escribir_sellado(archivo, _leer(self.plantilla_historico), comp)
            return ["crear historico-chat/README.md"] + self.instalar_resumenes(ruta, aplicar)

        cuerpo = Sello.quitar(_leer(archivo))
        cuerpo, agregadas = Plantillas.completar_secciones(
            cuerpo, Sello.quitar(_leer(self.plantilla_historico)))
        if agregadas:
            if aplicar:
                self.escribir_sellado(archivo, cuerpo, comp)
            return (["agregar a historico-chat/README.md lo que la plantilla sumó: "
                     + ", ".join(agregadas),
                     "sellar historico-chat/README.md contra la plantilla"]
                    + self.instalar_resumenes(ruta, aplicar))

        return (self.refrescar_sello(archivo, comp, ruta, aplicar, "historico-chat/README.md")
                + self.instalar_resumenes(ruta, aplicar))

    @staticmethod
    def instalar_resumenes(ruta, aplicar):
        """Deja puesta `historico-chat/resumenes/` con su índice: sin ella el
        enganche del resumen queda mudo. Si ya existe, no se pisa."""
        carpeta = os.path.join(ruta, "historico-chat", "resumenes")
        archivo = os.path.join(carpeta, "README.md")
        if os.path.isfile(archivo):
            return []
        if aplicar:
            os.makedirs(carpeta, exist_ok=True)
            with open(archivo, "w", encoding="utf-8", newline="\n") as f:
                f.write(TEXTO_RESUMENES)
        return ["crear historico-chat/resumenes/README.md"]

    def instalar_recuerdos(self, ruta, aplicar):
        """Crea `historico-chat/memory/` y vacía ahí la memoria de la herramienta.

        Van juntas: no sirve declarar dónde va la memoria si lo escrito se queda
        donde no debe. El índice se crea sellado y **no se pisa**. Con el almacén
        enlazado y el índice puesto, no se escribe una línea.
        """
        comp = POR_ID["recuerdos"]
        memoria = Recuerdos(ruta)
        archivo = memoria.ruta_indice()

        if not os.path.isfile(self.plantilla_memoria):
            return ["OMITIDO: falta plantillas/memoria.md en el estándar"]

        etiqueta = f"{CARPETA_RECUERDOS.replace(os.sep, '/')}/{INDICE_RECUERDOS}"

        if memoria.enlazada() and memoria.indice_presente():
            # Rellenar un marcador que se coló al copiar no es escribir memoria,
            # es terminar la copia.
            return (self.reparar_marcadores(archivo, ruta, aplicar, etiqueta)
                    + ["memoria enlazada a `historico-chat/memory/`: ya cumple, "
                       "no se toca"])

        if not memoria.indice_presente():
            pasos = [f"crear {etiqueta}"]
            if aplicar:
                os.makedirs(os.path.dirname(archivo), exist_ok=True)
                self.escribir_sellado(
                    archivo, self.rellenar(_leer(self.plantilla_memoria), self.rellenos(ruta)), comp)
        else:
            pasos = self.refrescar_sello(archivo, comp, ruta, aplicar, etiqueta)

        return pasos + Recuerdos.pasos(memoria.migrar(aplicar))

    def escribir_sellado(self, archivo, texto, componente):
        """Escribe `texto` en `archivo` con el sello de su plantilla al día."""
        sellado = Sello.poner(texto, Sello.huella_central(componente, self.estandar),
                              self.version_estandar())
        with open(archivo, "w", encoding="utf-8", newline="\n") as f:
            f.write(sellado)

    def refrescar_sello(self, archivo, componente, proyecto, aplicar, etiqueta):
        """Pone al día solo el sello de un archivo que el proyecto llena. No toca
        una línea del contenido: lo único que el estándar escribe ahí es contra
        qué plantilla se sincronizó."""
        pasos = self.reparar_marcadores(archivo, proyecto, aplicar, etiqueta)

        actual = Sello.huella_central(componente, self.estandar)
        sellada, ver = Sello.leer(archivo)
        if sellada == actual and ver == (self.version_estandar() or "?"):
            return pasos or [f"{etiqueta} ya estaba sellado al día"]

        if aplicar:
            texto = Sello.poner(_leer(archivo), actual, self.version_estandar())
            with open(archivo, "w", encoding="utf-8", newline="\n") as f:
                f.write(texto)
        return pasos + [f"sellar {etiqueta} contra la plantilla "
                        f"({sellada or 'sin sello'} → {actual})"]

    # ── los marcadores ───────────────────────────────────────────────────

    def rellenos(self, ruta):
        """Qué valor le corresponde a cada marcador de la plantilla. Nada de esto
        es decisión del usuario: preguntarlo sería preguntar lo que ya se sabe."""
        nombre = os.path.basename(os.path.abspath(ruta).rstrip("\\/")) or "proyecto"
        slug = Plantillas.slug(nombre)
        estandar = self.estandar.replace("\\", "/")
        proyecto = os.path.abspath(ruta).replace("\\", "/")
        ver = self.version_estandar() or "?"
        hoy = datetime.now().strftime("%Y-%m-%d")

        return {
            "«NOMBRE-PROYECTO»": nombre,
            "«SLUG-PROYECTO»": slug,
            "«RUTA-ESTANDAR»": estandar,
            "«RUTA-PROYECTO»": proyecto,
            "«VERSION-ESTANDAR»": ver,
            "«FECHA»": hoy,
            # Marcadores de plantillas anteriores: se traducen igual, para que un
            # proyecto viejo converja en vez de quedarse con huecos que
            # reprueban el checklist para siempre.
            "«NOMBRE DEL PROYECTO»": nombre,
            "«slug-proyecto»": slug,
            "«slug»": slug,
            "«ruta-al-estandar»": estandar,
            "«ruta-de-este-proyecto»": proyecto,
            "«X.Y.Z»": ver,
            "«YYYY-MM-DD»": hoy,
            "«español»": "español",
            "«sí / no»": "no",
            "«Otro ajuste: número de regla (01–19) + qué cambia + por qué»": "ninguno",
            "«ninguna por ahora / ver ./.agente/reglas-proyecto.md»":
                "ninguna por ahora",
        }

    def rellenar(self, texto, rellenos, proyecto=None):
        for marcador, valor in rellenos.items():
            texto = texto.replace(marcador, valor)
        return self.al_estandar(texto, proyecto) if proyecto else texto

    def al_estandar(self, texto, proyecto):
        """Los enlaces `](../…)` de una plantilla suben a la raíz del estándar;
        copiada en `.agente/` de un proyecto, esa subida llega al proyecto, donde
        `base/` no existe. El enlace pasa a apuntar al estándar si el archivo no
        está en el proyecto (análisis 1 del pendiente 110, acuerdo 2)."""
        if os.path.normcase(os.path.abspath(proyecto)) == os.path.normcase(os.path.abspath(self.estandar)):
            return texto
        estandar = self.estandar.replace("\\", "/")

        def cambio(m):
            resto = m.group(1)
            archivo = resto.split("#")[0]
            if os.path.exists(os.path.join(proyecto, *archivo.split("/"))):
                return m.group(0)
            return "](" + estandar + "/" + resto + ")"
        return re.sub(r"\]\(\.\./(?!\.\.)([^)\s]+)\)", cambio, texto)

    def reparar_marcadores(self, archivo, ruta, aplicar, etiqueta):
        """Rellena en sitio los marcadores que quedaron crudos en una copia vieja.

        Arreglar el punto de copia solo alcanza a lo que se instale desde ahora;
        por eso toda copia que ya existe pasa por aquí. **No reescribe el
        archivo: sustituye marcadores**, y solo los que el instalador sabe
        calcular; los huecos que llena el proyecto salen intactos. Sin nada que
        sustituir, no se escribe ni se reporta.
        """
        if not os.path.isfile(archivo):
            return []
        original = _leer(archivo)
        reparado = self.rellenar(original, self.rellenos(ruta), ruta)
        if reparado == original:
            return []
        if aplicar:
            with open(archivo, "w", encoding="utf-8", newline="\n") as f:
                f.write(reparado)
        return [f"rellenar los marcadores que quedaron crudos en {etiqueta}"]

    # ── el `CLAUDE.md` ───────────────────────────────────────────────────

    @staticmethod
    def copia_sellada(ruta):
        """Dónde se guarda la plantilla contra la que se selló el `CLAUDE.md`: en
        `.agente/`, que es local; es el punto de comparación del instalador."""
        return os.path.join(ruta, ".agente", "plantillas-selladas", "CLAUDE.md")

    def _guardar_copia_sellada(self, ruta, limpio, aplicar):
        if not aplicar:
            return
        copia = self.copia_sellada(ruta)
        os.makedirs(os.path.dirname(copia), exist_ok=True)
        with open(copia, "w", encoding="utf-8", newline="\n") as f:
            f.write(limpio)

    def instalar_claude_md(self, ruta, aplicar):
        """Deja el `CLAUDE.md` del proyecto puesto, lleno y sellado.

          - **no existe**: se genera desde la plantilla con las rutas de esta
            máquina, el nombre, el slug y la versión del estándar;
          - **con marcadores sin llenar**: se llenan los que se saben calcular;
          - **la plantilla ganó secciones**: se agregan al final;
          - **la plantilla cambió una sección**: se pone al día si el proyecto no
            le escribió encima (ver `Plantillas.sincronizar_secciones`).

        Poner al día el punto 1 mueve también la **versión adoptada**: correr la
        instalación es la decisión de adoptar, y el registro de versiones ya se
        escribía solo. El sello es la huella de la plantilla, no del archivo.
        """
        comp = POR_ID["claude-md"]
        plantilla = comp.ruta_plantilla(self.estandar)
        archivo = os.path.join(ruta, "CLAUDE.md")

        if not os.path.isfile(plantilla):
            return ["OMITIDO: falta plantillas/CLAUDE.md.plantilla en el estándar"]

        rellenos = self.rellenos(ruta)
        molde = self.rellenar(_leer(plantilla), rellenos)
        limpio = Sello.quitar(molde)

        if not os.path.isfile(archivo):
            if aplicar:
                self.escribir_sellado(archivo, molde, comp)
            self._guardar_copia_sellada(ruta, limpio, aplicar)
            return ["crear CLAUDE.md desde la plantilla, con las rutas y la "
                    "versión de esta máquina"]

        original = _leer(archivo)
        cuerpo = Sello.quitar(self.rellenar(original, rellenos))

        pasos = []
        if _MARCADOR.search(original) and not _MARCADOR.search(cuerpo):
            pasos.append("llenar en CLAUDE.md los marcadores que quedaban sin valor")
        cuerpo, agregadas = Plantillas.completar_secciones(cuerpo, limpio)
        if agregadas:
            pasos.append("agregar a CLAUDE.md lo que la plantilla sumó: " + ", ".join(agregadas))
        copia = self.copia_sellada(ruta)
        base = _leer(copia) if os.path.isfile(copia) else ""
        cuerpo, al_dia, a_mano = Plantillas.sincronizar_secciones(cuerpo, limpio, base)
        if al_dia:
            pasos.append("poner al día en CLAUDE.md lo que la plantilla cambió: " + ", ".join(al_dia))
        if a_mano:
            pasos.append("AVISO: en CLAUDE.md la plantilla cambió una sección que "
                         "este proyecto tiene escrita a su manera, así que no se "
                         "tocó: " + ", ".join(a_mano))
        if base != limpio:
            self._guardar_copia_sellada(ruta, limpio, aplicar)

        if not pasos:
            return self.refrescar_sello(archivo, comp, ruta, aplicar, "CLAUDE.md")

        if aplicar:
            self.escribir_sellado(archivo, cuerpo, comp)
        return pasos + ["sellar CLAUDE.md contra la plantilla"]

    # ── lo que el proyecto necesita tener ────────────────────────────────

    @staticmethod
    def instalar_estructura(ruta, aplicar):
        """Crea la estructura base de `02·F13`. La carpeta se crea; el contenido
        no se inventa, y lo que ya esté adentro no se mueve."""
        pasos = []
        for nombre in CARPETAS_BASE:
            destino = os.path.join(ruta, nombre)
            if os.path.isdir(destino):
                continue
            pasos.append(f"crear {nombre}/")
            if aplicar:
                os.makedirs(destino, exist_ok=True)
        return pasos or ["la estructura base ya estaba"]

    @staticmethod
    def instalar_gitignore(ruta, aplicar):
        """Agrega al `.gitignore` lo que no es del repositorio. Solo agrega: el
        `.gitignore` es del proyecto."""
        archivo = os.path.join(ruta, ".gitignore")
        texto = _leer(archivo) if os.path.isfile(archivo) else ""
        puestas = {l.strip() for l in texto.splitlines()}
        faltan = [x for x in IGNORADOS if x not in puestas]
        if not faltan:
            return ["el .gitignore ya ignoraba la configuración local"]

        if aplicar:
            if texto and not texto.endswith("\n"):
                texto += "\n"
            bloque = ("\n# Configuración local del agente — no es del repositorio.\n"
                      + "\n".join(faltan) + "\n")
            with open(archivo, "w", encoding="utf-8", newline="\n") as f:
                f.write(texto + bloque)
        return [f"agregar al .gitignore: {', '.join(faltan)}"]

    def instalar_agente_config(self, ruta, aplicar):
        """Pone los 4 archivos de `.agente/` desde las plantillas. Solo si faltan:
        los llena el proyecto, y pisarlos borraría lo único que el estándar no sabe."""
        pasos = []
        carpeta = os.path.join(ruta, ".agente")
        rellenos = self.rellenos(ruta)
        for nombre in CONFIG_AGENTE:
            destino = os.path.join(carpeta, nombre)
            if os.path.isfile(destino):
                # No se pisa, pero un enlace muerto no es contenido del proyecto:
                # es un hueco que se escapó al copiarlo.
                pasos += self.reparar_marcadores(destino, ruta, aplicar, f".agente/{nombre}")
                continue
            origen = os.path.join(self.estandar, "plantillas", nombre)
            if not os.path.isfile(origen):
                pasos.append(f"OMITIDO: falta plantillas/{nombre} en el estándar")
                continue
            pasos.append(f"crear .agente/{nombre} desde su plantilla")
            if aplicar:
                os.makedirs(carpeta, exist_ok=True)
                with open(destino, "w", encoding="utf-8", newline="\n") as f:
                    f.write(self.rellenar(_leer(origen), rellenos, ruta))
        return pasos or ["los 4 archivos de .agente/ ya estaban"]

    def _registro_real(self):
        estandar = Proyecto.estandar() or self.estandar
        real = os.path.join(estandar, "plantillas", "proyectos.md")
        return os.path.normcase(os.path.abspath(self.registro)) == os.path.normcase(os.path.abspath(real))

    def registrar_en_cimiento(self, nombre, ruta, scope):
        """El alta va también al registro de Cimiento (`manage.py registrar`)
        si Cimiento tiene su ambiente. `proyectos.md` se sigue escribiendo
        aparte: lleva la memoria y el stack, que el registro no guarda.

        Solo contra el registro real: una prueba que apuntó el registro a una
        carpeta temporal nunca llega a la base de verdad.
        """
        if not self._registro_real():
            return False
        cimiento = os.path.join(self.estandar, "proyectos", "cimiento")
        manage = os.path.join(cimiento, "manage.py")
        python = self.python_de_cimiento(cimiento)
        if not (os.path.isfile(manage) and python):
            return False
        r = subprocess.run(
            [python, manage, "registrar", "--nombre", nombre, "--ruta", ruta, "--scope", scope],
            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
        return r.returncode == 0

    def instalar_registro(self, ruta, aplicar):
        """Anota el proyecto en `plantillas/proyectos.md`, la lista única. El
        stack queda «por detectar»: es un dato y lo completa el agente."""
        if not os.path.isfile(self.registro):
            return ["OMITIDO: falta plantillas/proyectos.md en el estándar"]

        # Un proyecto en la carpeta temporal del sistema es de una prueba: las
        # pruebas dejaron 860 así en la base real (pendiente 110, acuerdo 3).
        temporal = os.path.normcase(os.path.realpath(tempfile.gettempdir())) + os.sep
        if self._registro_real() and os.path.normcase(os.path.realpath(ruta)).startswith(temporal):
            return ["es una carpeta temporal: no va al registro de proyectos"]

        esperado = os.path.normcase(os.path.abspath(ruta))
        for _, registrada in self.proyectos_registrados():
            if os.path.normcase(os.path.abspath(registrada)) == esperado:
                return ["el proyecto ya estaba en el registro central"]

        nombre = os.path.basename(os.path.abspath(ruta).rstrip("\\/"))
        scope = f"proyecto:{Plantillas.slug(nombre)}"
        fila = f"| {nombre} | `{os.path.abspath(ruta)}` | `{scope}` | por detectar |\n"
        en_cimiento = aplicar and self.registrar_en_cimiento(nombre, os.path.abspath(ruta), scope)
        if aplicar:
            texto = _leer(self.registro)
            if not texto.endswith("\n"):
                texto += "\n"
            with open(self.registro, "w", encoding="utf-8", newline="\n") as f:
                f.write(texto + fila)
        if en_cimiento:
            return [f"anotar «{nombre}» en plantillas/proyectos.md y en el registro de Cimiento"]
        return [f"anotar «{nombre}» en plantillas/proyectos.md"]

    def repo_del_estandar(self):
        """De dónde se descarga Cimiento: el remoto del estándar instalado."""
        return _mandar_git(self.estandar, "remote", "get-url", "origin").stdout.strip()

    def instalar_ci(self, ruta, aplicar, repo=None):
        """Agrega la revisión del plan a la integración continua que el proyecto ya tiene."""
        workflows = os.path.join(ruta, ".github", "workflows")
        github = os.path.isdir(workflows) and any(
            n.endswith((".yml", ".yaml")) and n != os.path.basename(CI_GITHUB)
            for n in os.listdir(workflows))
        gitlab = os.path.join(ruta, ".gitlab-ci.yml")
        otros = [n for n in _CI_OTROS if os.path.isfile(os.path.join(ruta, n))]
        if not (github or os.path.isfile(gitlab) or otros):
            return ["sin integración continua: no se agrega la revisión del plan"]

        pasos = []
        repo = repo if repo is not None else self.repo_del_estandar()
        if (github or os.path.isfile(gitlab)) and not repo:
            return ["OMITIDO: la integración continua no recibe la revisión del plan: "
                    "el estándar no tiene un remoto de dónde descargarlo"]

        def llenar(plantilla):
            return plantilla.replace("__REPO__", repo).replace("__DESDE__", _CI_DESDE)

        if github:
            destino = os.path.join(ruta, *CI_GITHUB.split("/"))
            if os.path.isfile(destino):
                pasos.append(f"{CI_GITHUB} ya estaba")
            else:
                pasos.append(f"crear {CI_GITHUB}: la integración continua revisa el plan")
                if aplicar:
                    _escribir(destino, llenar(PLANTILLA_CI_GITHUB))
        if os.path.isfile(gitlab):
            destino = os.path.join(ruta, CI_GITLAB)
            if not os.path.isfile(destino):
                pasos.append(f"crear {CI_GITLAB}: la integración continua revisa el plan")
                if aplicar:
                    _escribir(destino, llenar(PLANTILLA_CI_GITLAB))
            texto = _leer(gitlab)
            if CI_GITLAB in texto:
                pasos.append(f".gitlab-ci.yml ya incluye {CI_GITLAB}")
            elif re.search(r"^include:", texto, re.M):
                pasos.append(f"AVISO: .gitlab-ci.yml ya tiene «include:»; agregar ahí "
                             f"«- local: {CI_GITLAB}»")
            else:
                pasos.append(f"incluir {CI_GITLAB} en .gitlab-ci.yml")
                if aplicar:
                    _escribir(gitlab, texto.rstrip("\n") + f"\n\ninclude:\n  - local: {CI_GITLAB}\n")
        for nombre in otros:
            pasos.append(f"AVISO: {nombre} no se sabe ampliar solo; la revisión es "
                         f"`validar.py plan --rango desde..hasta`")
        return pasos

    # ── la instalación completa ──────────────────────────────────────────

    @staticmethod
    def python_de_cimiento(cimiento):
        """El Python del `.venv` de Cimiento, o `None` si no tiene ambiente."""
        return next((p for p in (os.path.join(cimiento, ".venv", "Scripts", "python.exe"),
                                 os.path.join(cimiento, ".venv", "bin", "python"))
                     if os.path.isfile(p)), None)

    TAREA_DE_CONSUMO = "Cimiento leer consumo"

    def programar_lectura(self, aplicar, ejecutar=subprocess.run, sistema=os.name):
        """`EP-025·HU-006` · La lectura del consumo, una vez al día.

        Claude Code borra sus registros a los 30 días: lo que no se lea antes se
        pierde. En Windows queda una tarea programada; en otro sistema se dice
        cómo programarla, porque escribir en el `crontab` de alguien es cambiar
        la configuración de su máquina (`04·S9`).
        """
        cimiento = os.path.join(self.estandar, "proyectos", "cimiento")
        manage = os.path.join(cimiento, "manage.py")
        if not os.path.isfile(manage):
            return []
        python = self.python_de_cimiento(cimiento)
        orden = '"%s" "%s" leer_consumo' % (python or "python", manage)
        if sistema != "nt":
            return ["OMITIDO: programar a mano, una vez al día, con cron: " + orden]
        if not aplicar:
            return ["programar la lectura del consumo una vez al día (schtasks)"]
        if python is None:
            return ["OMITIDO: Cimiento no tiene su ambiente (.venv): la lectura del consumo no se programó"]

        def correr(argumentos):
            return ejecutar(argumentos, capture_output=True, text=True, encoding="utf-8",
                            errors="replace", timeout=60)

        if correr(["schtasks", "/Query", "/TN", self.TAREA_DE_CONSUMO]).returncode == 0:
            return ["la lectura del consumo ya estaba programada"]
        r = correr(["schtasks", "/Create", "/SC", "DAILY", "/ST", "12:00", "/TN", self.TAREA_DE_CONSUMO,
                    "/TR", orden, "/F"])
        if r.returncode == 0:
            return ["lectura del consumo programada una vez al día, a las 12:00"]
        lineas = (r.stderr or r.stdout or "").strip().splitlines()
        return ["OMITIDO: no se pudo programar la lectura del consumo: " + (lineas[-1] if lineas else "schtasks falló")]

    def telemetria(self):
        """`{variable: valor}` que manda los eventos de Claude Code a Cimiento.

        La dirección usa el `PUERTO` del `.env` de Cimiento, el mismo con el que
        `manage.py runserver` levanta sin decirle otro.
        """
        from config import ambiente
        cimiento = os.path.join(self.estandar, "proyectos", "cimiento")
        puerto = ambiente.leer(os.path.join(cimiento, ".env")).get("PUERTO") or "8000"
        return {
            "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
            "OTEL_LOGS_EXPORTER": "otlp",
            "OTEL_METRICS_EXPORTER": "none",
            "OTEL_EXPORTER_OTLP_PROTOCOL": "http/json",
            "OTEL_EXPORTER_OTLP_LOGS_ENDPOINT": f"http://127.0.0.1:{puerto}/v1/logs",
            "OTEL_LOG_TOOL_DETAILS": "1",
        }

    def activar_telemetria(self, aplicar, configuracion=None):
        """`EP-025·HU-007` · Claude Code manda cada llamada a Cimiento, en vivo.

        Va en la configuración del usuario (`~/.claude/settings.json`): Claude
        Code ignora estas variables en la de un repositorio. Solo se agregan las
        que falten: una que el usuario ya tenga no se pisa.
        """
        if not os.path.isfile(os.path.join(self.estandar, "proyectos", "cimiento", "manage.py")):
            return []
        configuracion = configuracion or os.path.join(os.path.expanduser("~"), ".claude", "settings.json")
        datos = {}
        if os.path.isfile(configuracion):
            try:
                datos = json.loads(_leer(configuracion) or "{}")
            except ValueError:
                return ["OMITIDO: ~/.claude/settings.json tiene JSON inválido; la telemetría no se activó"]
        if not isinstance(datos, dict) or not isinstance(datos.get("env", {}), dict):
            return ["OMITIDO: ~/.claude/settings.json no tiene la forma esperada; la telemetría no se activó"]
        entorno = datos.get("env", {})
        faltan = {clave: valor for clave, valor in self.telemetria().items() if clave not in entorno}
        if not faltan:
            return ["la telemetría hacia Cimiento ya estaba activa"]
        if not aplicar:
            return ["activar la telemetría hacia Cimiento en ~/.claude/settings.json"]
        datos["env"] = {**entorno, **faltan}
        os.makedirs(os.path.dirname(configuracion), exist_ok=True)
        with open(configuracion, "w", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(datos, indent=2, ensure_ascii=False) + "\n")
        return [f"telemetría hacia Cimiento activada en ~/.claude/settings.json ({len(faltan)} variable(s)); "
                "vale desde la próxima sesión de Claude Code"]

    def preparar_cimiento(self, aplicar, ejecutar=subprocess.run):
        """`EP-025·HU-001` · Deja lista la aplicación de Cimiento antes de los enganches.

        Instala lo que sus pantallas usan en el navegador (`npm ci`) si falta, y
        crea y migra su base (`manage.py preparar_base`). Va antes de los
        enganches porque el freno va a leer esa base (`EP-025·HU-005`).

        Lo que no se pueda hacer queda dicho y la instalación sigue: no hay nada
        que decidir, solo algo que prender o instalar.
        """
        cimiento = os.path.join(self.estandar, "proyectos", "cimiento")
        if not os.path.isfile(os.path.join(cimiento, "manage.py")):
            return []
        if not aplicar:
            return ["preparar Cimiento: npm ci si falta node_modules/, y manage.py preparar_base"]

        python = self.python_de_cimiento(cimiento)
        if python is None:
            return ["OMITIDO: Cimiento no tiene su ambiente (.venv); crearlo como dice "
                    "proyectos/cimiento/README.md"]

        def correr(orden, limite):
            return ejecutar(orden, cwd=cimiento, capture_output=True, text=True,
                            encoding="utf-8", errors="replace", timeout=limite)

        def ultima_linea(resultado):
            lineas = (resultado.stderr or resultado.stdout or "").strip().splitlines()
            return lineas[-1] if lineas else f"terminó con el código {resultado.returncode}"

        pasos = []
        if not os.path.isdir(os.path.join(cimiento, "node_modules")):
            npm = shutil.which("npm")
            if npm is None:
                pasos.append("OMITIDO: falta npm; sin él las pantallas de Cimiento no tienen estilos")
            else:
                r = correr([npm, "ci", "--no-audit", "--no-fund"], 600)
                pasos.append("npm ci en proyectos/cimiento/" if r.returncode == 0
                             else f"OMITIDO: npm ci falló en proyectos/cimiento/: {ultima_linea(r)}")

        r = correr([python, "manage.py", "preparar_base"], 300)
        if r.returncode == 0:
            pasos.append(r.stdout.strip() or "manage.py preparar_base")
        else:
            pasos.append("OMITIDO: " + ultima_linea(r).removeprefix("CommandError: "))
        return pasos

    @staticmethod
    def asegurar_pymysql(aplicar, ejecutar=subprocess.run, importar=importlib.import_module):
        """`EP-025·HU-005` · PyMySQL en el Python que corre los enganches.

        El freno lee de la base de Cimiento el nivel de cada regla, sin Django,
        y sin ese controlador no la puede leer: no dejaría modificar nada. Se
        instala con el mismo Python que corre la instalación, que es el que
        nombran los enganches.
        """
        try:
            importar("pymysql")
            return ["PyMySQL ya estaba en el Python que corre los enganches"]
        except ImportError:
            pass
        if not aplicar:
            return ["instalar PyMySQL en el Python que corre los enganches"]
        r = ejecutar([sys.executable, "-m", "pip", "install", "PyMySQL>=1.1,<2"], capture_output=True,
                     text=True, encoding="utf-8", errors="replace", timeout=300)
        if r.returncode == 0:
            return ["PyMySQL instalado en el Python que corre los enganches"]
        lineas = (r.stderr or r.stdout or "").strip().splitlines()
        return ["OMITIDO: no se pudo instalar PyMySQL: " + (lineas[-1] if lineas else "pip falló")]

    def instalar(self, nombre, ruta, aplicar):
        # Prepara su propia salida: imprime tildes y flechas, y la consola de
        # Windows tal como arranca no las admite. Quien lo llame como biblioteca
        # no tiene por qué saberlo.
        preparar_salida()

        print(f"\n— {nombre}\n  {ruta}")

        # Se normaliza para que la ruta escrita en el enganche no dependa de cómo
        # llegó (`.` o absoluta, `c:` o `C:`): si no, cada corrida la reescribiría.
        unidad, resto = os.path.splitdrive(os.path.abspath(ruta))
        ruta = unidad.upper() + resto

        if not os.path.isdir(ruta):
            # Único bloqueo: una ruta que no existe suele ser un error de tecleo.
            print("  BLOQUEADO: la carpeta no existe — revisá la ruta")
            return False

        estandar = self.estandar.replace("\\", "/")
        marca = "·" if aplicar else "(simulado)"

        # Huellas y versión ANTES de tocar nada: después los sellos ya dicen la
        # nueva, y una instalación desde cero declararía venir de sí misma.
        antes = self.huellas(ruta)
        anterior = self.version_anterior(ruta)

        propio = self.es_el_estandar(ruta)
        if propio:
            print("  · es la carpeta del propio estándar: se ponen los enganches, "
                  "el histórico y la memoria; nada de configuración de proyecto")
            for paso in (self.preparar_cimiento(aplicar) + self.asegurar_pymysql(aplicar)
                         + self.programar_lectura(aplicar) + self.activar_telemetria(aplicar)):
                print(f"  {marca} {paso}")
        else:
            for paso in self.instalar_estructura(ruta, aplicar):
                print(f"  {marca} {paso}")
            for paso in self.instalar_gitignore(ruta, aplicar):
                print(f"  {marca} {paso}")

        # El de commits va en CADA repositorio; el de edición va UNA vez, en la
        # raíz del espacio de trabajo, donde vive la documentación que revisa.
        repos = self.repositorios_git(ruta)
        if not repos:
            print("  · commit-msg: OMITIDO — no hay repositorios git aquí")
        for repo in repos:
            etiqueta = os.path.relpath(repo, ruta).replace("\\", "/")
            if etiqueta != ".":
                print(f"  repositorio {etiqueta}/")
            for paso in self.instalar_git(repo, estandar, aplicar):
                print(f"  {marca} {paso}")

        for paso in self.instalar_claude(ruta, estandar, aplicar):
            print(f"  {marca} {paso}")

        # El histórico y la memoria valen también para el propio estándar.
        pasos = []
        for instalador in (self.instalar_historico, self.instalar_recuerdos):
            pasos += instalador(ruta, aplicar)
        if not propio:
            for instalador in (self.instalar_stack, self.instalar_agente_config,
                               self.instalar_claude_md, self.instalar_registro, self.instalar_ci):
                pasos += instalador(ruta, aplicar)

        for paso in pasos:
            print(f"  {marca} {paso}")

        for paso in self.registrar_version(ruta, antes, pasos, aplicar, anterior):
            print(f"  {marca} {paso}")

        self.comprobar(ruta, aplicar, propio)
        return True

    def comprobar(self, ruta, aplicar, propio=False):
        """La comprobación final: instalar y decir "listo" sin mirar es prometer.
        Lo que siga faltando después de instalar todo exige una decisión del usuario."""
        from ..validadores.checklist import Checklist

        if propio:
            # El stack describe un proyecto que **usa** el agente: medir con esa
            # vara la carpeta de las reglas daría faltantes que no lo son.
            return
        if not aplicar:
            print("  (simulado) la comprobación final corre al aplicar")
            return

        puntos = Checklist(ruta, self.estandar).revisar()
        print(f"\n  {Checklist.resumen(ruta, puntos)}")

        if not Checklist.pendientes(puntos):
            return
        print("\n  Esto no se pudo resolver solo — necesita una decisión tuya:\n")
        for linea in Checklist.detalle(puntos).splitlines():
            print(f"  {linea}")

    def huellas(self, ruta):
        """`{id: huella sellada}` de cada documento heredado, ahora mismo."""
        return {e.id: e.sellada for e in DocumentosHeredados(ruta, self.estandar).estado()}

    def huellas_previstas(self, ruta):
        """`{id: huella que va a quedar}`: la central de cada uno. Es lo que la
        simulación compara, porque lo que ella ve todavía no ha cambiado."""
        return {e.id: e.actual for e in DocumentosHeredados(ruta, self.estandar).estado()}

    @staticmethod
    def version_anterior(ruta):
        """Con qué versión venía el proyecto: "" si es la primera instalación."""
        registro = RegistroDeVersiones(ruta)
        return registro.version_registrada() or registro.version_sellada()

    def pendientes(self, ruta):
        """Lo que quedó sin resolver después de instalar todo: va al registro."""
        from ..validadores.checklist import Checklist
        if self.es_el_estandar(ruta):
            return []
        return [f"**{p.id}** — {p.detalle or p.componente}"
                for p in Checklist.pendientes(Checklist(ruta, self.estandar).revisar())]

    def registrar_version(self, ruta, antes, pasos, aplicar, anterior=""):
        """Deja constancia en `documentacion/versiones/` de la actualización.

        Se registra si **cambió alguna huella** o si **subió la versión** del
        estándar aunque ninguna plantilla cambiara (si no, el registro se queda
        atrás para siempre). Sin ninguno de los dos no se escribe nada: un
        registro por corrida taparía las actualizaciones de verdad.
        """
        # El estándar no hereda de sí mismo: lleva su `CHANGELOG`.
        if self.es_el_estandar(ruta):
            return []

        actual = self.version_estandar() or "?"

        # `EP-007·HU-002` · Lo que muestra es lo que hace: al simular no se ha
        # copiado nada, así que se compara la huella que **va a quedar**.
        despues = self.huellas(ruta) if aplicar else self.huellas_previstas(ruta)
        cambios = [id for id in despues if antes.get(id, "") != despues.get(id, "")]
        subio = bool(anterior) and anterior != actual

        if not cambios and not subio:
            return ["versiones: ni las plantillas ni la versión cambiaron, "
                    "no hay actualización que registrar"]

        registro = RegistroDeVersiones(ruta, self.estandar)
        if not aplicar:
            detalle = ", ".join(sorted(cambios)) if cambios else f"{anterior} → {actual}"
            # Se nombra el archivo, no la carpeta.
            previsto = os.path.join(CARPETA_VERSIONES, registro.nombre_previsto(actual))
            return [f"registrar {previsto} ({detalle})"]

        archivo = registro.registrar(
            actual, antes, despues, pasos,
            # Se pasa la función, no su resultado: el apartado se calcula cuando
            # el registro ya existe, o se lista a sí mismo.
            pendientes=lambda: self.pendientes(ruta), anterior=anterior)
        return [f"registrar {os.path.relpath(archivo, ruta)}"]


def main(argv=None):
    """La orden de consola: lista el registro, simula o instala. Devuelve 0."""
    preparar_salida()

    p = argparse.ArgumentParser(description="Instala los enganches del estándar en un proyecto.")
    p.add_argument("ruta", nargs="?", help="carpeta del proyecto")
    p.add_argument("--todos", action="store_true",
                   help="todos los proyectos de plantillas/proyectos.md")
    p.add_argument("--aplicar", action="store_true",
                   help="instalar de verdad (sin esto solo simula)")
    a = p.parse_args(argv)

    instalador = Instalador()
    registrados = instalador.proyectos_registrados()

    if a.todos:
        objetivos = registrados
    elif a.ruta:
        ruta = os.path.abspath(a.ruta)
        nombre = next((n for n, r in registrados if os.path.abspath(r) == ruta), "(fuera del registro)")
        objetivos = [(nombre, ruta)]
    else:
        print("Proyectos registrados en plantillas/proyectos.md:\n")
        for nombre, ruta in registrados:
            estado = "" if os.path.isdir(ruta) else "   (no existe)"
            print(f"  {nombre}{estado}\n    {ruta}")
        print("\nIndica una ruta, o --todos. Agrega --aplicar para instalar.")
        return 0

    if not a.aplicar:
        print("MODO SIMULACIÓN — no se modifica nada. Agrega --aplicar.")

    hechos = sum(1 for nombre, ruta in objetivos if instalador.instalar(nombre, ruta, a.aplicar))

    print(f"\n{hechos} de {len(objetivos)} proyecto(s) "
          f"{'procesados' if a.aplicar else 'simulados'}.")
    return 0
