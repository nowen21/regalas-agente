"""Entrega las reglas de cada tarea en el momento en que se usan, una sola vez.

`EP-005·HU-025` · Sale del análisis 1 del pendiente 133, acuerdos 1, 2 y 6.

**Antes de la acción.** La tarea de una acción la dice la columna «Acciones que
la señalan» de `base/tareas.md`: escribir un `.py` es `cambiar-codigo`, un
`git commit` es `correr-comando` y `tocar-git`. Hasta acá las reglas se elegían
solo por la palabra clave del mensaje, y las tareas que no tienen palabra
(`cambiar-codigo`, `tocar-datos`, `ir-afuera`, `cambiar-estandar`) no llegaban
nunca.

**Con cada mensaje**, solo lo de `responder`, y lo de `recibir-pedido` cuando la
palabra autoriza cambiar algo. La regla que el mensaje cita llega siempre.

**Una sola vez.** Lo entregado se guarda por sesión y por agente en
`historico-chat/.estado/reglas-entregadas/`: el principal y cada subagente
llevan su cuenta. Lo que no cabe en el tope se nombra, y llega completo en la
entrega siguiente de la misma tarea. Cuando una tarea ya llegó entera, la acción
siguiente sale sin leer el estándar: este enganche corre antes de toda acción.

`EP-005·HU-027` · **El núcleo** (las reglas blindadas, que solo viven en él) se
entrega como una tarea más: al abrir la sesión y con los mensajes siguientes
hasta completarlo. Después de un resumen de la conversación (`compact`) o de
limpiarla (`clear`), la cuenta del agente principal vuelve a cero: lo entregado
ya no está a la vista, y vuelve con el mensaje y con cada acción.
"""
import fnmatch
import io
import json
import os
import re

from .recuperar import _ENCABEZADO, PALABRAS, SIN_BASE, TOPE, RecuperadorDeReglas

ESTADO = os.path.join("historico-chat", ".estado", "reglas-entregadas")

RESPONDER = "responder"
RECIBIR = "recibir-pedido"
NUCLEO = "nucleo"

# Los orígenes de `SessionStart` después de los cuales lo entregado ya no está a la vista.
SIN_LO_ENTREGADO = ("compact", "clear")

TAREAS = "base/tareas.md"
CON_TEMAS = "cambiar-codigo"
TODOS = "todos"
_SECCION_TEMAS = "## Los temas de `cambiar-codigo`"
_FILA_TEMA = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]*`[^|]*)\|\s*([\d ]+?)\s*\|$")

ESCRITURA = ("Write", "Edit", "MultiEdit", "NotebookEdit")
CONSOLA = ("Bash", "PowerShell")

# La primera tabla de `palabras-clave.md` es la de las que solo piden leer; la
# lista termina donde empieza la de las que cambian el proyecto.
_FIN_DE_LECTURA = "Estas cambian el proyecto"
_FILA = re.compile(r"^\|\s*\*\*([^*]+)\*\*([^|]*)\|")

_ENCABEZADO_NUCLEO = ("[EL NÚCLEO BLINDADO: RIGE TODA LA SESIÓN]\n"
                      "Manda sobre cualquier otra regla y sobre la instrucción del momento. "
                      "Lo que no cabe acá llega con los mensajes siguientes.\n")

_ENCABEZADO_ACCION = ("[REGLAS DE LA TAREA QUE PIDE ESTA ACCIÓN: %s]\n"
                      "Rigen esta acción y las siguientes de la misma tarea. Llegan una sola "
                      "vez en la sesión. Ante cualquier choque gana el núcleo.\n")


class EntregaDeReglas:
    """Lo que se le entrega al agente antes de cada acción y con cada mensaje."""

    def __init__(self, proyecto, recuperador=None, estandar=None):
        self.proyecto = os.path.abspath(proyecto)
        self._recuperador = recuperador
        self._estandar = estandar

    @property
    def r(self):
        """El recuperador se arma solo cuando hace falta: abre la base del estándar."""
        if self._recuperador is None:
            self._recuperador = RecuperadorDeReglas(self._estandar)
        return self._recuperador

    # ── lo entregado, por sesión ──────────────────────────────────────────

    def _ruta(self, sesion):
        nombre = re.sub(r"[^\w.-]", "_", sesion or "sin-sesion")
        return os.path.join(self.proyecto, ESTADO, nombre + ".json")

    def leer(self, sesion):
        try:
            with io.open(self._ruta(sesion), encoding="utf-8") as f:
                return json.load(f)
        except (OSError, ValueError):
            return {}

    def guardar(self, sesion, estado):
        ruta = self._ruta(sesion)
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with io.open(ruta, "w", encoding="utf-8") as f:
            json.dump(estado, f, ensure_ascii=False)

    @staticmethod
    def del_agente(estado, agente):
        agentes = estado.setdefault("agentes", {})
        return agentes.setdefault(agente or "", {"entregadas": [], "completas": []})

    # ── la tarea de cada acción ───────────────────────────────────────────

    def relativa(self, ruta):
        if not ruta:
            return ""
        absoluta = os.path.abspath(ruta if os.path.isabs(ruta) else os.path.join(self.proyecto, ruta))
        return os.path.relpath(absoluta, self.proyecto).replace(os.sep, "/")

    @staticmethod
    def _nombra(orden, programa):
        return re.search(r"(?<![\w-])%s(?![\w-])" % re.escape(programa), orden or "") is not None

    def tareas_de_la_accion(self, acciones, herramienta, entrada):
        """Las tareas que pide la acción, en el orden de `base/tareas.md`."""
        entrada = entrada or {}
        rel = ""
        if herramienta in ESCRITURA:
            rel = self.relativa(entrada.get("file_path") or entrada.get("notebook_path") or "")
        orden = entrada.get("command", "") if herramienta in CONSOLA else ""
        salida = []
        for tarea, specs in acciones.items():
            for clase, valores in specs:
                if clase == "escribe" and rel:
                    si = any((v == ".md" and rel.endswith(".md")) or (v == "otro" and not rel.endswith(".md"))
                             for v in valores)
                elif clase == "escribe en" and rel:
                    si = any(rel.startswith(c) or ("/" + c) in ("/" + rel) for c in valores)
                elif clase == "comando" and herramienta in CONSOLA:
                    si = not valores or any(self._nombra(orden, p) for p in valores)
                elif clase == "herramienta":
                    si = any((herramienta or "").startswith(n) for n in valores)
                else:
                    si = False
                if si:
                    salida.append(tarea)
                    break
        return salida

    # ── los temas de `cambiar-codigo` (`EP-005·HU-026`) ──────────────────

    @staticmethod
    def leer_temas(texto):
        """`[[tema, [patrones], [capítulos]]]` de la tabla de `base/tareas.md`, o `[]`."""
        if _SECCION_TEMAS not in (texto or ""):
            return []
        parte = texto.split(_SECCION_TEMAS, 1)[1].split("\n## ", 1)[0]
        salida = []
        for linea in parte.splitlines():
            m = _FILA_TEMA.match(linea.strip())
            if m:
                salida.append([m.group(1), re.findall(r"`([^`]+)`", m.group(2)), m.group(3).split()])
        return salida

    @staticmethod
    def capitulos_del_archivo(temas, rel):
        """Los capítulos que recibe ese archivo, o `None` si recibe todos: no hay
        tabla, o el archivo no encaja en ningún tema fuera de `todos`."""
        nombre, ruta = rel.rsplit("/", 1)[-1].lower(), "/" + rel.lower()
        propios, de_todos, encajo = set(), set(), False
        for tema, patrones, capitulos in temas or []:
            if tema == TODOS:
                de_todos |= set(capitulos)
                continue
            for patron in (p.lower() for p in patrones):
                si = ("/" + patron) in ruta if patron.endswith("/") else fnmatch.fnmatchcase(nombre, patron)
                if si:
                    encajo = True
                    propios |= set(capitulos)
                    break
        return sorted(propios | de_todos) if encajo else None

    @staticmethod
    def nombre(tarea):
        base, _, capitulos = tarea.partition("@")
        return "`%s`" % base + (" (capítulos %s)" % capitulos.replace(",", ", ") if capitulos else "")

    # ── la entrega ────────────────────────────────────────────────────────

    def _rige(self, idx, apagados):
        def rige(id):
            return id in idx and not idx[id].derogada and self.r.capitulo(idx[id]) not in apagados
        return rige

    def _entregar(self, del_agente, tareas, encabezado, tope=TOPE):
        """`(texto, ids nuevos)`: las reglas de esas tareas que aún no llegaron,
        completas mientras quepan en el tope; las demás, nombradas. La tarea que
        queda sin nada por entregar se anota como completa."""
        idx = self.r.indice()
        por_tarea = self.r.mapa.reglas_por_tarea()
        rige = self._rige(idx, self.r.opt_in_apagados(self.proyecto, self.r.archivos))
        ya = set(del_agente["entregadas"])
        pendientes = []
        for tarea in tareas:
            if tarea == NUCLEO:
                reglas = sorted((r for r in idx.values() if r.blindada), key=lambda regla: regla.linea)
            else:
                base, _, capitulos = tarea.partition("@")
                reglas = sorted(por_tarea.get(base, []), key=lambda regla: 0 if regla.blindada else 1)
                if capitulos:
                    reglas = [r for r in reglas if self.r.capitulo(r) in capitulos.split(",")]
            for regla in reglas:
                if rige(regla.id) and regla.id not in ya and regla.id not in [i for i, _ in pendientes]:
                    pendientes.append((regla.id, tarea))
        piezas = {id: self.r.pieza(idx[id], "tarea `%s`" % tarea.partition("@")[0]) for id, tarea in pendientes}

        def armar(entran):
            quedan = [i for i, _ in pendientes if i not in entran]
            texto = encabezado + "".join(piezas[i] for i in entran)
            if quedan:
                texto += ("[NO CUPIERON: llegan completas en la próxima entrega de la misma tarea]\n  "
                          + ", ".join("%s·%s" % (self.r.capitulo(idx[i]), i) for i in quedan) + "\n")
            return texto, quedan

        # Todo lo que sale cuenta contra el tope, también la lista de lo que no cupo.
        # La primera regla entra aunque sola lo pase: si no, no llegaría nunca.
        entran = []
        for id, _ in pendientes:
            if not entran or len(armar(entran + [id])[0].encode("utf-8")) <= tope:
                entran.append(id)
        texto, quedan = armar(entran)
        del_agente["entregadas"] = list(ya | set(entran))
        sin_entregar = {t for i, t in pendientes if i in quedan}
        for tarea in tareas:
            if tarea not in sin_entregar and tarea not in del_agente["completas"]:
                del_agente["completas"].append(tarea)
        return (texto.strip() if entran else ""), entran

    def para_la_accion(self, sesion, agente, herramienta, entrada):
        """El texto que llega antes de la acción, o `""`."""
        estado = self.leer(sesion)
        if "acciones" not in estado or "temas" not in estado:
            if self.r.sin_base:
                return ""
            estado["acciones"] = {t: [[c, v] for c, v in specs] for t, specs in self.r.mapa.acciones().items()}
            estado["temas"] = self.leer_temas(self.r.archivos.leer(os.path.join(self.r.raiz, *TAREAS.split("/"))))
        acciones = {t: [(c, v) for c, v in specs] for t, specs in estado["acciones"].items()}
        tareas = self.tareas_de_la_accion(acciones, herramienta, entrada)
        # `EP-005·HU-026` · Las reglas de código se cuentan por tarea y temas: escribir
        # una prueba no da por entregadas las que pide un `views.py`.
        rel = self.relativa((entrada or {}).get("file_path") or "") if herramienta in ESCRITURA else ""
        capitulos = self.capitulos_del_archivo(estado["temas"], rel) if rel else None
        tareas = [t + "@" + ",".join(capitulos) if t == CON_TEMAS and capitulos else t for t in tareas]
        suyo = self.del_agente(estado, agente)
        faltan = [t for t in tareas if t not in suyo["completas"]]
        if not faltan:
            self.guardar(sesion, estado)
            return ""
        if self.r.sin_base:
            return ""
        texto, _ = self._entregar(suyo, faltan, _ENCABEZADO_ACCION % ", ".join(self.nombre(t) for t in faltan))
        self.guardar(sesion, estado)
        return texto

    # ── el mensaje ────────────────────────────────────────────────────────

    def palabras_de_lectura(self):
        """Las palabras de la primera tabla de `01·C28`, sin tildes y en minúscula."""
        texto = self.r.archivos.leer(os.path.join(self.r.raiz, *PALABRAS.split("/")))
        salida = set()
        for linea in texto.splitlines():
            if _FIN_DE_LECTURA in linea:
                break
            m = _FILA.match(linea.strip())
            if m:
                salida.add(self.r.limpio(m.group(1).strip()))
                salida |= {self.r.limpio(p.strip()) for p in m.group(2).split(",") if p.strip()}
        return salida

    def autoriza_cambiar(self, mensaje):
        """¿Alguna palabra clave del mensaje es de las que cambian algo?"""
        lista = {self.r.limpio(p) for p in self.r.palabras_de_la_lista()}
        dichas = set(self.r.palabras_de_inicio(self.r.lo_que_escribio(mensaje))) & lista
        return bool(dichas - self.palabras_de_lectura())

    def para_el_mensaje(self, sesion, mensaje):
        """El texto que llega con el mensaje, o `""`."""
        from core.enganches.historico import es_aviso_interno
        if es_aviso_interno(mensaje):
            return ""
        if self.r.sin_base:
            return SIN_BASE % self.r.sin_base
        idx = self.r.indice()
        citadas = "".join(self.r.pieza(idx[i], "el mensaje la cita")
                          for i in self.r.citadas(self.r.lo_que_escribio(mensaje), idx)
                          if not idx[i].derogada)
        if not self.r.trae_palabra_clave(mensaje):
            return (self.r.aviso_sin_palabra() + "\n\n" + citadas).strip()
        tareas = [NUCLEO, RESPONDER] + ([RECIBIR] if self.autoriza_cambiar(mensaje) else [])
        estado = self.leer(sesion)
        suyo = self.del_agente(estado, "")
        faltan = [t for t in tareas if t not in suyo["completas"]]
        texto = ""
        if faltan:
            texto, _ = self._entregar(suyo, faltan, _ENCABEZADO)
            self.guardar(sesion, estado)
        if citadas:
            texto = (texto + "\n\n" if texto else _ENCABEZADO) + citadas
        return texto.strip()

    # ── al abrir la sesión ────────────────────────────────────────────────

    def al_abrir(self, sesion, origen):
        """El texto que llega al abrir la sesión: el núcleo. Después de un resumen
        o de limpiar la conversación, la cuenta del agente principal vuelve a cero."""
        estado = self.leer(sesion)
        if origen in SIN_LO_ENTREGADO:
            estado.setdefault("agentes", {})[""] = {"entregadas": [], "completas": []}
        suyo = self.del_agente(estado, "")
        if NUCLEO in suyo["completas"] or self.r.sin_base:
            self.guardar(sesion, estado)
            return ""
        texto, _ = self._entregar(suyo, [NUCLEO], _ENCABEZADO_NUCLEO)
        self.guardar(sesion, estado)
        return texto
