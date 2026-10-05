# -*- coding: utf-8 -*-
"""Compara los módulos viejos del grupo «sesión» con sus clases nuevas
(sesión del 2026-10-04, análisis 1 del pendiente 116): enmascarar, historico,
externo, presupuesto, rutas_fuera, cargador, checkpoint, veredicto, traza,
respaldo, corredor y temas, sobre este repositorio y los proyectos dados.

    python paridad_sesion.py [proyecto ...]

Cada hallazgo se compara como (ruta normalizada, línea, severidad, mensaje); lo
demás, por lo que devuelven las funciones públicas. Lo que escribe el histórico
se compara en dos copias dentro de una carpeta temporal: nunca en un
`historico-chat/` real.
"""
import glob
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
VALIDADORES = os.path.join(RAIZ, "validadores")
CIMIENTO = os.path.join(RAIZ, "proyectos", "cimiento")
sys.path.insert(0, VALIDADORES)
sys.path.insert(0, CIMIENTO)

import cargador as v_cargador  # noqa: E402
import checkpoint as v_checkpoint  # noqa: E402
import corredor as v_corredor  # noqa: E402
import enmascarar as v_enmascarar  # noqa: E402
import externo as v_externo  # noqa: E402
import historico as v_historico  # noqa: E402
import presupuesto as v_presupuesto  # noqa: E402
import respaldo as v_respaldo  # noqa: E402
import rutas_fuera as v_rutas  # noqa: E402
import secretos as v_secretos  # noqa: E402
import temas as v_temas  # noqa: E402
import traza as v_traza  # noqa: E402
import veredicto as v_veredicto  # noqa: E402
from core.enganches.cargador import Cargador  # noqa: E402
from core.enganches.checkpoint import Checkpoint  # noqa: E402
from core.enganches.enmascarar import Enmascarador  # noqa: E402
from core.enganches.externo import ContenidoExterno  # noqa: E402
from core.enganches.historico import Historico, Transcript  # noqa: E402
from core.enganches.presupuesto import Presupuesto  # noqa: E402
from core.enganches.rutas_fuera import RutasFuera  # noqa: E402
from core.enganches.veredicto import CopiaDelVeredicto  # noqa: E402
from core.herramientas.corredor import PruebasDelEstandar  # noqa: E402
from core.herramientas.respaldo import Respaldo  # noqa: E402
from core.herramientas.temas import IndiceTematico  # noqa: E402
from core.validadores import secretos as n_secretos  # noqa: E402
from core.validadores.traza import Traza  # noqa: E402

_HORA = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")


def clave(h, raiz):
    ruta = h.archivo if os.path.isabs(h.archivo) else os.path.join(raiz, h.archivo)
    return (os.path.normcase(os.path.realpath(ruta)), h.linea, h.severidad, h.mensaje)


def igual(nombre, a, b):
    print("%-40s %s" % (nombre, "IGUAL" if a == b else "DISTINTO"))
    if a != b:
        print("   viejo:", str(a)[:400])
        print("   nuevo:", str(b)[:400])
    return a == b


def leer(ruta):
    with io.open(ruta, encoding="utf-8", errors="replace") as f:
        return f.read()


def transcripts_de(raiz):
    """Los transcripts de Claude Code de ese proyecto, solo para leer."""
    nombre = re.sub(r"[^A-Za-z0-9]", "-", os.path.abspath(raiz))
    carpeta = os.path.join(os.path.expanduser("~"), ".claude", "projects")
    candidatas = [c for c in glob.glob(os.path.join(carpeta, "*")) if os.path.basename(c).lower() == nombre.lower()]
    return sorted(glob.glob(os.path.join(candidatas[0], "*.jsonl")), key=os.path.getsize)[:4] if candidatas else []


def transcripciones(raiz):
    carpeta = os.path.join(raiz, "historico-chat")
    if not os.path.isdir(carpeta):
        return []
    return [os.path.join(carpeta, n) for n in sorted(os.listdir(carpeta))
            if n.endswith(".md") and n != "README.md"]


# ── Por módulo ────────────────────────────────────────────────────────────

def p_enmascarar(raiz):
    ok = igual("secretos: patrones", [p.pattern for p, _ in v_secretos.SEGUROS] + [
        v_secretos._ASIGNA.pattern, v_secretos._ENTORNO.pattern],
        [p.pattern for p, _ in n_secretos.SEGUROS] + [n_secretos.ASIGNA.pattern, n_secretos._ENTORNO.pattern])
    textos = ["", None, "API_KEY=supersecreto123456", 'password: "S3creto"', "clave = h.regla",
              "token: xyz", "AKIA1234567890ABCDEF", "la contraseña: Patito2026", "password: changeme",
              "API_KEY=os.environ['MI_CLAVE_LARGA']", 'secret = "tu-clave-aqui"']
    for ruta in transcripciones(raiz):
        textos += leer(ruta).splitlines(keepends=True)
    distintos = [t for t in textos if v_enmascarar.enmascarar(t) != Enmascarador.enmascarar(t)
                 or (t and v_enmascarar.hay_clave(t) != Enmascarador.hay_clave(t))]
    ok &= igual("enmascarar (%d textos)" % len(textos), distintos, [])
    return ok


def p_historico_lee(raiz):
    ok = True
    distintos = [r for r in transcripciones(raiz) if v_historico.turnos(leer(r)) != Historico.turnos(leer(r))]
    ok &= igual("historico.turnos (%d)" % len(transcripciones(raiz)), distintos, [])
    h = Historico(raiz)
    ok &= igual("historico.sesiones", v_historico.sesiones(raiz), h.sesiones())
    for args in ({}, {"limite": 5}, {"tope": 1000}, {"tope": 10}):
        ok &= igual("historico.contexto %s" % args, v_historico.contexto(raiz, **args), h.contexto(**args))
    marcas = []
    for r in transcripciones(raiz)[-15:]:
        m = re.search(r"<!-- sesion: (.+?) -->", leer(r))
        if m:
            marcas.append(m.group(1))
    marcas.append("no-existe")
    ok &= igual("historico.archivo_de_sesion (%d)" % len(marcas),
                [v_historico.archivo_de_sesion(raiz, s) for s in marcas],
                [h.archivo_de_sesion(s) for s in marcas])
    ok &= igual("historico._archivo", [v_historico._archivo(raiz, s, crear=False) for s in marcas],
                [h.archivo(s) for s in marcas])
    jsonl = transcripts_de(raiz)
    ok &= igual("historico.ultima_respuesta (%d)" % len(jsonl),
                [v_historico.ultima_respuesta(t) for t in jsonl + ["", "no-existe.jsonl"]],
                [Transcript.ultima_respuesta(t) for t in jsonl + ["", "no-existe.jsonl"]])
    carpeta = os.path.join(raiz, "historico-chat")
    nombres = [os.path.basename(r) for r in transcripciones(raiz)]
    ok &= igual("historico._enlace_al_resumen", [v_historico._enlace_al_resumen(carpeta, n) for n in nombres],
                [Historico._enlace_al_resumen(carpeta, n) for n in nombres])
    temas = ["Él tema-con ñ", "", "--", "a_b c", "Sesión"]
    ok &= igual("historico._slug/_legible", [(v_historico._slug(t), v_historico._legible(t)) for t in temas],
                [(Historico._slug(t), Historico._legible(t)) for t in temas])
    return ok


def _arbol(raiz):
    """`{ruta relativa: texto}` con las horas y la raíz de la copia normalizadas."""
    salida = {}
    for carpeta, _subs, archivos in os.walk(raiz):
        for nombre in archivos:
            ruta = os.path.join(carpeta, nombre)
            texto = _HORA.sub("<hora>", leer(ruta)).replace(raiz.replace(os.sep, "/"), "<raiz>")
            salida[os.path.relpath(ruta, raiz).replace("\\", "/")] = texto
    return salida


def _escribir_con(modulo_viejo, raiz, jsonl, hoy):
    """Lo mismo, con el viejo o con el nuevo, sobre una copia."""
    carpeta = os.path.join(raiz, "historico-chat")
    os.makedirs(os.path.join(carpeta, "resumenes", hoy), exist_ok=True)
    rastro = []
    existente = transcripciones(raiz)[-1] if transcripciones(raiz) else ""
    m = re.search(r"<!-- sesion: (.+?) -->", leer(existente)) if existente else None
    if modulo_viejo:
        anotar_u = lambda s, t: v_historico.anotar_usuario(raiz, s, t)  # noqa: E731
        anotar_a = lambda s, t: v_historico.anotar_agente(raiz, s, t)  # noqa: E731
        aviso, renombrar = v_historico.aviso_de_nombre, v_historico.renombrar
    else:
        h = Historico(raiz)
        anotar_u, anotar_a = h.anotar_usuario, h.anotar_agente
        aviso, renombrar = Historico.aviso_de_nombre, Historico.renombrar
    if m:
        rastro.append(anotar_u(m.group(1), "sigue la charla con API_KEY=supersecreto123456\n\ny otra línea"))
    ruta = anotar_u("paridad-nueva", "hola")
    rastro.append(ruta)
    rastro.append(anotar_u("paridad-nueva", "   "))
    for t in jsonl[:1]:
        rastro.append(anotar_a("paridad-nueva", t))
        rastro.append(anotar_a("paridad-nueva", t))         # el enganche repetido no duplica
    rastro.append(aviso(ruta))
    rastro.append(aviso(ruta))                               # se pide una sola vez
    resumen = os.path.join(carpeta, "resumenes", hoy, os.path.basename(ruta)[len(hoy) + 1:])
    with io.open(resumen, "w", encoding="utf-8", newline="\n") as f:
        f.write("# x\n\nDe [historico-chat/%s](../../%s).\n" % (os.path.basename(ruta), os.path.basename(ruta)))
    rastro.append(renombrar(ruta, "La prueba de paridad", "lo que se probó"))
    try:
        renombrar(os.path.join(carpeta, "no-existe.md"), "x")
    except FileNotFoundError as e:
        rastro.append(str(e))
    return [(r or "").replace(raiz, "<raiz>").replace(raiz.replace(os.sep, "/"), "<raiz>") for r in rastro]


def p_historico_escribe(raiz, jsonl):
    from datetime import datetime
    hoy = datetime.now().strftime("%Y-%m-%d")
    origen = os.path.join(raiz, "historico-chat")
    if not os.path.isdir(origen):
        return igual("historico escribe (sin historico-chat)", 0, 0)
    with tempfile.TemporaryDirectory() as tmp:
        a, b = os.path.join(tmp, "viejo"), os.path.join(tmp, "nuevo")
        for destino in (a, b):
            shutil.copytree(origen, os.path.join(destino, "historico-chat"),
                            ignore=shutil.ignore_patterns("scripts", "trazas", ".estado", ".tocado"))
        rastro_a = _escribir_con(True, a, jsonl, hoy)
        rastro_b = _escribir_con(False, b, jsonl, hoy)
        orden_a = os.path.join(VALIDADORES, "historico.py").replace(os.sep, "/")
        orden_b = os.path.join(CIMIENTO, "core", "enganches", "historico.py").replace(os.sep, "/")
        rastro_a = [r.replace(orden_a, "<orden>") for r in rastro_a]
        rastro_b = [r.replace(orden_b, "<orden>") for r in rastro_b]
        ok = igual("historico: lo que devuelve al escribir", rastro_a, rastro_b)
        arbol_a, arbol_b = _arbol(a), _arbol(b)
        distintos = sorted(k for k in set(arbol_a) | set(arbol_b) if arbol_a.get(k) != arbol_b.get(k))
        ok &= igual("historico: lo que queda escrito (%d)" % len(arbol_a), distintos, [])
        # La traza se deja junto al histórico de la sesión, en las mismas copias.
        for t in jsonl[:1]:
            lista_a, lista_b = v_traza.pasos(t), Traza.pasos(t)
            texto_a = v_traza.como_texto(lista_a, v_traza.cierre(lista_a))
            texto_b = Traza.como_texto(lista_b, Traza.cierre(lista_b))
            ra = v_traza.escribir(a, "paridad-nueva", texto_a)
            rb = Traza.escribir(b, "paridad-nueva", texto_b)
            ok &= igual("traza.escribir", (ra or "").replace(a, ""), (rb or "").replace(b, ""))
            ok &= igual("traza.escribir sin sesión", v_traza.escribir(a, "no-hay", texto_a),
                        Traza.escribir(b, "no-hay", texto_b))
            arbol_a, arbol_b = _arbol(a), _arbol(b)
            distintos = sorted(k for k in set(arbol_a) | set(arbol_b) if arbol_a.get(k) != arbol_b.get(k))
            ok &= igual("traza: lo que queda escrito", distintos, [])
    return ok


def p_externo():
    raiz = RAIZ
    casos = [("WebFetch", {"url": "https://a.b"}), ("WebSearch", {"query": "q"}), ("WebFetch", None),
             ("mcp__gmail__leer", {"id": 1}), ("mcp__solo", None), ("Read", {"file_path": os.path.join(raiz, "x")}),
             ("Read", {"file_path": "C:/otro/x"}), ("Read", {"path": "/tmp/x"}), ("Read", {}), ("Read", "cadena"),
             ("Bash", {"command": "curl"}), ("", None), (None, None)]
    ok = True
    for raiz_ in (raiz, None, ""):
        ok &= igual("externo (raíz %r)" % raiz_,
                    [(v_externo.es_externa(n, e, raiz_), v_externo.origen(n, e), v_externo.sobre(n, e, raiz_))
                     for n, e in casos],
                    [(ContenidoExterno.es_externa(n, e, raiz_), ContenidoExterno.origen(n, e),
                      ContenidoExterno.sobre(n, e, raiz_)) for n, e in casos])
    return ok


def p_presupuesto():
    listas = [[], [{"entrada": 999_998}, {"entrada": 1}], [{"entrada": 999_999}, {"entrada": 1}],
              [{"entrada": 500_000}, {"entrada": 450_000}, {"entrada": 100_000, "salida": 3, "cache": 9}],
              [{"entrada": 10, "cache": 5_000_000}], [{"salida": None}]]
    ok = True
    for umbral in (0, 1000, 1_000_000):
        viejo = [(v_presupuesto.resumen(l), v_presupuesto.cruzo_tramo(l, umbral),
                  v_presupuesto.como_texto(v_presupuesto.resumen(l), umbral),
                  v_presupuesto.aviso_de_tramo(v_presupuesto.resumen(l), 2, umbral or 1)) for l in listas]
        nuevo = [(Presupuesto.resumen(l), Presupuesto.cruzo_tramo(l, umbral),
                  Presupuesto.como_texto(Presupuesto.resumen(l), umbral),
                  Presupuesto.aviso_de_tramo(Presupuesto.resumen(l), 2, umbral or 1)) for l in listas]
        ok &= igual("presupuesto (umbral %d)" % umbral, viejo, nuevo)
    ok &= igual("presupuesto.TRAMO", v_presupuesto.TRAMO, Presupuesto.TRAMO)
    return ok


def p_rutas(raiz):
    padre = os.path.dirname(raiz)
    rutas = ["", None, "   ", ".", "README.md", raiz, os.path.join(raiz, "x", "..", "y.md"),
             os.path.join(raiz, "..", os.path.basename(raiz) + "-viejo", "x.py"), os.path.join(padre, "suelto.py"),
             tempfile.gettempdir(), raiz.upper(), raiz.replace("\\", "/") + "/a/b.py", "/c/Users/x.py"]
    for carpeta, _s, archivos in os.walk(raiz):
        if ".git" in carpeta or "node_modules" in carpeta:
            continue
        rutas += [os.path.join(carpeta, a) for a in archivos[:2]]
        if len(rutas) > 400:
            break
    ok = True
    for casa in (raiz, "", padre):
        ok &= igual("rutas_fuera (casa %s, %d)" % (os.path.basename(casa) or "vacía", len(rutas)),
                    [v_rutas.aviso(r, casa) for r in rutas], [RutasFuera.aviso(r, casa) for r in rutas])
    return ok


def p_cargador(raiz):
    base = os.path.join(raiz, "base")
    return (igual("cargador.contexto", v_cargador.contexto(raiz), Cargador.contexto(raiz))
            & igual("cargador.contexto sin gate", v_cargador.contexto(raiz, gate_ok=False),
                    Cargador.contexto(raiz, gate_ok=False))
            & igual("cargador.reglas", v_cargador.reglas(base), Cargador.reglas(base))
            & igual("cargador.paquete", v_cargador.paquete(raiz), Cargador.paquete(raiz)))


def p_fases(raiz):
    """El checkpoint y la copia del veredicto, sobre cada documento de las épicas."""
    archivos = []
    for carpeta, _s, nombres in os.walk(os.path.join(raiz, "documentacion", "epicas")):
        archivos += [os.path.join(carpeta, n) for n in nombres]
    archivos.append(os.path.join(raiz, "documentacion", "epicas", "X-EP-1-HU-1-x", "plan_trabajo.md"))
    distintos = []
    for ruta in archivos:
        viejo, nuevo = v_checkpoint.rezago(ruta), Checkpoint.rezago(ruta)
        if viejo != nuevo or v_checkpoint.fase_de(ruta) != Checkpoint.fase_de(ruta):
            distintos.append(ruta)
        elif viejo and v_checkpoint.como_texto(viejo, raiz) != Checkpoint.como_texto(nuevo, raiz):
            distintos.append(ruta)
    ok = igual("checkpoint (%d archivos)" % len(archivos), distintos, [])
    resultados = [r for r in archivos if os.path.basename(r) == "resultado_pruebas.md"]
    distintos = [r for r in resultados
                 if v_veredicto.leer_veredicto(r) != CopiaDelVeredicto.leer_veredicto(r)
                 or v_veredicto.propagar(r, "2026-10-04", escribir=False)
                 != CopiaDelVeredicto.propagar(r, "2026-10-04", escribir=False)]
    ok &= igual("veredicto (%d resultados)" % len(resultados), distintos, [])
    textos = [("cumple", ("2", "3")), ("no cumple", None)]
    ok &= igual("veredicto.texto_del_estado", [v_veredicto.texto_del_estado(c, n, "x") for c, n in textos],
                [CopiaDelVeredicto.texto_del_estado(c, n, "x") for c, n in textos])
    return ok


def p_traza(raiz):
    ok = True
    for t in transcripts_de(raiz) + ["no-existe.jsonl"]:
        a, b = v_traza.pasos(t), Traza.pasos(t)
        ok &= igual("traza %s" % os.path.basename(t)[:20], (a, v_traza.cierre(a), v_traza.como_texto(a, v_traza.cierre(a)),
                                                           v_traza.sesion_de(t)),
                    (b, Traza.cierre(b), Traza.como_texto(b, Traza.cierre(b)), Traza.sesion_de(t)))
    return ok


def p_respaldo(raiz):
    ok = igual("respaldo.comandos", v_respaldo.comandos(raiz), Respaldo(raiz).comandos())
    ok &= igual("respaldo.respaldar simulado", v_respaldo.respaldar(raiz, "x"), Respaldo(raiz).respaldar("x"))
    return ok


def p_respaldo_main():
    nuevo_guion = os.path.join(CIMIENTO, "core", "herramientas", "respaldo.py")
    ok = True
    with tempfile.TemporaryDirectory() as tmp:
        for declarado in ("«…»", "echo respaldando", "exit 1"):
            os.makedirs(os.path.join(tmp, ".agente"), exist_ok=True)
            with io.open(os.path.join(tmp, ".agente", "stack.md"), "w", encoding="utf-8") as f:
                f.write("| Acción | Comando |\n|---|---|\n| **Respaldo de datos** | `%s` |\n" % declarado)
            ok &= igual("respaldo comandos (%s)" % declarado, v_respaldo.comandos(tmp), Respaldo(tmp).comandos())
            ok &= igual("respaldo respaldar (%s)" % declarado, v_respaldo.respaldar(tmp, "x", True),
                        Respaldo(tmp).respaldar("x", True))
            for args in ([], ["--raiz", tmp, "--", "echo", "x"], ["--raiz", tmp, "--aplicar", "--", "echo", "listo"]):
                salidas = []
                for guion in (os.path.join(VALIDADORES, "respaldo.py"), nuevo_guion):
                    r = subprocess.run([sys.executable, guion] + args, capture_output=True, text=True,
                                       encoding="utf-8", errors="replace", timeout=60)
                    # Con `--aplicar` el nuevo vacía su salida antes de la operación:
                    # el orden cambia a propósito, las líneas no.
                    salidas.append((r.returncode, sorted(r.stdout.splitlines()) if "--aplicar" in args else r.stdout))
                ok &= igual("respaldo main %s (%s)" % (args[-2:], declarado), salidas[0], salidas[1])
    return ok


def p_corredor(raiz):
    pruebas = PruebasDelEstandar(raiz)
    ok = igual("corredor.archivos_de", v_corredor.archivos_de(v_corredor.carpeta_de(raiz)),
               PruebasDelEstandar.archivos_de(pruebas.carpeta()))
    ok &= igual("corredor.reclamo", sorted(clave(h, raiz) for h in v_corredor.reclamo(raiz)),
                sorted(clave(h, raiz) for h in pruebas.reclamo()))
    if os.path.isdir(v_corredor.carpeta_de(raiz)):
        solo = ["test_la_clave_sin_comillas_se_enmascara", "test_no_hay"]
        viejo = v_corredor.correr(raiz, solo)
        nuevo = PruebasDelEstandar(raiz).correr(solo)
        ok &= igual("corredor.correr solo", (viejo[0].testsRun, sorted(clave(h, raiz) for h in viejo[1]), viejo[2]),
                    (nuevo[0].testsRun, sorted(clave(h, raiz) for h in nuevo[1]), nuevo[2]))
    return ok


def p_corredor_temporal():
    pasa = "import unittest\nclass C(unittest.TestCase):\n    def test_a(self): pass\n"
    falla = "import unittest\nclass D(unittest.TestCase):\n    def test_c(self): self.assertEqual(1, 2)\n"
    ok = True
    for archivos in ((), (("test_uno.py", pasa),), (("test_uno.py", pasa), ("test_dos.py", falla),
                                                    ("test_roto.py", "import no_existe\n"))):
        for solo in (None, ["test_uno"], ["test_no"]):
            claves = []
            for es_viejo in (True, False):
                with tempfile.TemporaryDirectory() as tmp:
                    carpeta = os.path.join(tmp, "validadores", "tests")
                    os.makedirs(carpeta)
                    for nombre, cuerpo in archivos:
                        with io.open(os.path.join(carpeta, nombre), "w", encoding="utf-8") as f:
                            f.write(cuerpo)
                    if es_viejo:
                        hallazgos, reclamo = v_corredor.validar(tmp, solo), v_corredor.reclamo(tmp)
                    else:
                        p = PruebasDelEstandar(tmp, solo=solo)
                        hallazgos, reclamo = p.validar(), p.reclamo()
                    sello = os.path.join(tmp, v_corredor.SELLO)
                    claves.append((sorted(clave(h, tmp)[1:] for h in hallazgos),
                                   sorted(os.path.relpath(clave(h, tmp)[0], os.path.normcase(os.path.realpath(tmp)))
                                          for h in hallazgos),
                                   [h.mensaje for h in reclamo],
                                   leer(sello).split("\n")[1:] if os.path.isfile(sello) else None))
            ok &= igual("corredor temporal %d archivo(s) %s" % (len(archivos), solo), claves[0], claves[1])
    with tempfile.TemporaryDirectory() as tmp:
        ok &= igual("corredor sin plataforma",
                    [h.mensaje for h in v_corredor.correr_la_plataforma(tmp)[0]],
                    [h.mensaje for h in PruebasDelEstandar(tmp).correr_la_plataforma()[0]])
    return ok


def p_temas(raiz):
    viejo, nuevo = v_temas, IndiceTematico(raiz)
    ok = igual("temas.generar", viejo.generar(raiz), nuevo.generar())
    ok &= igual("temas.validar", sorted(clave(h, raiz) for h in viejo.validar(raiz)),
                sorted(clave(h, raiz) for h in nuevo.validar()))
    ok &= igual("temas.linea_resumen", viejo.linea_resumen(raiz), nuevo.linea_resumen())
    return ok


def en_un_proyecto(raiz):
    print("== %s" % raiz)
    ok = p_enmascarar(raiz)
    ok &= p_historico_lee(raiz)
    ok &= p_historico_escribe(raiz, transcripts_de(raiz) or transcripts_de(RAIZ))
    ok &= p_rutas(raiz)
    ok &= p_cargador(raiz)
    ok &= p_fases(raiz)
    ok &= p_traza(raiz)
    ok &= p_respaldo(raiz)
    ok &= p_corredor(raiz)
    ok &= p_temas(raiz)
    return ok


if __name__ == "__main__":
    todo_bien = p_externo() & p_presupuesto() & p_respaldo_main() & p_corredor_temporal()
    proyectos = sys.argv[1:] or ["c:/wamp64/www/proyectos/personales/agro-system"]
    for proyecto in [RAIZ] + proyectos:
        if os.path.isdir(proyecto):
            todo_bien &= en_un_proyecto(os.path.abspath(proyecto))
    print("\nPARIDAD COMPLETA" if todo_bien else "\nHAY DIFERENCIAS")
