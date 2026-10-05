"""`02·F12` · La estructura épica → HU → fase, y lo que se dice de cada fase.

Comprueba lo que se puede sin criterio: los nombres de carpeta (F12.6, F12.11),
que la fase esté guardada en la épica y la HU que declara (F12.1, F12.3), el
consecutivo sin repetir ni huecos (F12.5, F12.7), los cinco documentos (F12.13)
y que el resultado y el estado digan el mismo veredicto (`HU-014`). Más los
avisos de siete historias que vigilan el mismo árbol, cada uno con su motivo.

Y cuenta: `inventario()` y `por_veredicto()` dan la línea que cierra la corrida.
"""
import os
import re

from ..comun import AVISO, FALLA, Hallazgo, Proyecto
from .base import Validador
from .epicas import CARPETA, DOCUMENTOS, PENDIENTES, Epicas
from .estacion import EstacionDelCommit
from .moldes import Moldes
from .veredictos import ESTADO, RESULTADO, Veredictos

# `EP-002·HU-005` · El sello de versión del cierre se exige desde que el campo
# entró al molde. Lo cerrado antes no se reabre.
SELLO_DESDE = "2026-08-22"
_SELLO_VERSION = re.compile(
    r"(?i)(?:\|\s*\*\*versión del estándar[^|]*\|\s*[«`]?"
    r"|(?:versión|estándar en la|bajo la versión|v)\s*)(\d+\.\d+\.\d+)")
_FECHA_CIERRE = re.compile(r"(?i)(?:\|\s*\*\*fecha de cierre\*\*\s*\|\s*|cerrad[ao]\s+(?:el\s+)?)(\d{4}-\d{2}-\d{2})")

# `EP-023·HU-004·CA-02` · Mientras el análisis de un hallazgo siga sin aprobar,
# la fase está detenida: ni ella ni su HU cierran.
_ENLACE_ANALISIS = re.compile(r"\]\(([^)#\s]*analisis-(\d+)\.md)")
_APROBADO_ANALISIS = re.compile(r"^> \*\*Aprobado\*\*", re.M)

# `EP-004·HU-019/020` · El inventario no guarda la cuenta: se pregunta. Se busca
# el campo con su rótulo, en el primer nivel de estas carpetas.
CARPETAS_DEL_INVENTARIO = ("pendientes", "documentacion")
CUENTA_A_MANO = re.compile(r"^\|\s*\*\*(Total de HU|Completas|Incompletas)\*\*\s*\|\s*\d+\s*\|", re.MULTILINE)

# `EP-003·HU-012` · El vocabulario de estados sale del glosario del estándar: una
# lista acá sería la quinta, y por eso se llegó a tres palabras para «terminado».
_CONJUNTO = re.compile(r"^\|\s*\*\*(Épica|Historia de usuario|Tarea)\*\*[^|]*\|\s*([^|]+?)\s*\|", re.MULTILINE)
_ESTADO_DECLARADO = re.compile(r"^\|\s*\*\*Estado\*\*\s*\|\s*(.+?)\s*\|", re.MULTILINE)


def _leer(ruta):
    try:
        with open(ruta, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def _lista(nombres, tope=None):
    elegidos = sorted(nombres)[:tope] if tope else sorted(nombres)
    return ", ".join(elegidos) + (" …" if tope and len(nombres) > tope else "")


class EstructuraDeFases(Validador):

    nombre = "fases"
    regla = "02·F12"
    descripcion = "estructura épica → HU → fase y veredicto de cada fase"

    def __init__(self, proyecto, archivos=None):
        super().__init__(proyecto, archivos)
        self.arbol = Epicas(self.proyecto)
        self._moldes = None

    @property
    def moldes(self):
        """Las plantillas se leen una vez para los cientos de documentos (`RNF-01`)."""
        if self._moldes is None:
            self._moldes = Moldes(self.proyecto.raiz)
        return self._moldes

    def _fases_de(self, ruta_hu):
        return [n for n in Epicas.subcarpetas(ruta_hu) if Epicas.fase(n)]

    def _historias(self):
        """`(épica, HU)` de nombre válido."""
        for epica in self.arbol.epicas():
            for hu in self.arbol.historias(epica):
                yield epica, hu

    # ── la estructura ────────────────────────────────────────────────────

    def validar(self):
        if not self.arbol.existe():
            return [Hallazgo(FALLA, self.proyecto.raiz, 0, "no existe `%s` — F12.13 la exige" % CARPETA)]
        hallazgos = []
        for nombre in Epicas.subcarpetas(self.arbol.raiz):
            hallazgos += self._revisar_epica(nombre)
        return (hallazgos + self.cierre_sin_sello() + self.cuenta_escrita_a_mano()
                + self.estado_fuera_del_vocabulario() + self.documentos_que_siguen_siendo_el_molde()
                + self.reemplazos_que_no_resuelven() + self.estacion_del_commit_sin_marcar()
                + self.detenidas_por_un_hallazgo())

    def _revisar_epica(self, nombre):
        ruta, donde = os.path.join(self.arbol.raiz, nombre), "%s/%s" % (CARPETA, nombre)
        numero = Epicas.epica(nombre)
        if numero is None:
            return [Hallazgo(FALLA, donde, 0, "no parece una épica: se espera `EP-<número>-<slug>` (F12.13)")]
        hallazgos = []
        # El nombre del documento varía entre la norma y los proyectos: basta uno.
        if not any(os.path.isfile(os.path.join(ruta, n)) for n in ("epica.md", nombre + ".md")):
            hallazgos.append(Hallazgo(AVISO, donde, 0, "sin documento de épica (`epica.md` o `%s.md`)" % nombre))
        for nombre_hu in Epicas.subcarpetas(ruta):
            if nombre_hu == PENDIENTES:
                continue
            ruta_hu, donde_hu = os.path.join(ruta, nombre_hu), "%s/%s" % (donde, nombre_hu)
            num_hu = Epicas.historia(nombre_hu)
            if num_hu is None:
                hallazgos.append(Hallazgo(FALLA, donde_hu, 0, "dentro de una épica solo van HU — se espera "
                                                              "`HU-<número>-<slug>` (F12.11)"))
                continue
            if not os.path.isfile(os.path.join(ruta_hu, nombre_hu + ".md")):
                hallazgos.append(Hallazgo(AVISO, donde_hu, 0, "sin documento `%s.md`" % nombre_hu))
            hallazgos += self._revisar_fases(ruta_hu, donde_hu, numero, num_hu)
        return hallazgos

    def _revisar_fases(self, ruta_hu, donde_hu, num_epica, num_hu):
        fases = [f for f in Epicas.subcarpetas(ruta_hu) if f != PENDIENTES]
        if not fases:
            # AVISO: una HU recién abierta todavía no tiene ninguna.
            return [Hallazgo(AVISO, donde_hu, 0, "sin fases (F12.2: pide al menos una por historia)")]
        hallazgos, vistos = [], {}
        for nombre in fases:
            donde = "%s/%s" % (donde_hu, nombre)
            partes = Epicas.fase(nombre)
            if not partes:
                hallazgos.append(Hallazgo(FALLA, donde, 0, "el nombre no sigue F12.6 — se espera "
                                                           "`<consecutivo>-EP-<número>-HU-<número>-<descripción>`, "
                                                           "p. ej. `A-EP-001-HU-003-Configuración inicial`"))
                continue
            if int(partes["epica"]) != num_epica:
                hallazgos.append(Hallazgo(FALLA, donde, 0, "declara la épica %s pero está guardada en la %d (F12.1)"
                                          % (partes["epica"], num_epica)))
            if int(partes["hu"]) != num_hu:
                hallazgos.append(Hallazgo(FALLA, donde, 0, "declara la HU %s pero está guardada en la %d "
                                                           "(F12.3 · una fase no se comparte entre HU)"
                                          % (partes["hu"], num_hu)))
            consecutivo = partes["consecutivo"].upper()
            if consecutivo in vistos:
                hallazgos.append(Hallazgo(FALLA, donde, 0, "el consecutivo «%s» ya lo usa «%s» (F12.7)"
                                          % (consecutivo, vistos[consecutivo])))
            else:
                vistos[consecutivo] = nombre
            faltan = [d for d in DOCUMENTOS if not os.path.isfile(os.path.join(ruta_hu, nombre, d))]
            if faltan:
                hallazgos.append(Hallazgo(AVISO, donde, 0, "faltan documentos de la fase (F12.13): %s"
                                          % ", ".join(faltan)))
            hallazgos += self.veredictos_que_no_coinciden(os.path.join(ruta_hu, nombre), donde)
        # F12.5 · AVISO: una fase diferida deja un hueco legítimo que mira una persona.
        if vistos and sorted(Epicas.orden_letras(c) for c in vistos) != list(range(1, len(vistos) + 1)):
            hallazgos.append(Hallazgo(AVISO, donde_hu, 0, "el consecutivo de fases no es A, B, C… sin huecos "
                                                          "(F12.5): " + ", ".join(sorted(vistos))))
        return hallazgos

    @staticmethod
    def veredictos_que_no_coinciden(ruta_fase, donde):
        """`HU-014` · El resultado y el estado dicen lo mismo. No comprueba si el
        veredicto es cierto: comprueba que los dos documentos no se contradigan,
        porque la puerta de verificación mira el estado y la verdad está en el resultado."""
        resultado, estado = _leer(os.path.join(ruta_fase, RESULTADO)), _leer(os.path.join(ruta_fase, ESTADO))
        if not resultado or not estado:
            return []                       # una fase a medio escribir no se cobra acá
        hallazgos = []
        v_resultado, v_estado = Veredictos.concepto(resultado), Veredictos.concepto(estado)
        if v_resultado and v_estado and v_resultado != v_estado:
            hallazgos.append(Hallazgo(FALLA, donde, 0, "los dos veredictos de la fase no coinciden (HU-014): "
                                                       "`resultado_pruebas` dice «%s» y `estado-fase` dice «%s». "
                                                       "La puerta de verificación mira el segundo"
                                      % (v_resultado, v_estado)))
        if v_estado == "cumple":
            hallazgos += [Hallazgo(FALLA, donde, 0, "la fase se da por cumplida y el `resultado_pruebas` tiene "
                                                    "«%s» en No (HU-014)" % exigencia)
                          for exigencia in Veredictos.exigencias_en_no(resultado)]
        c_resultado, c_estado = Veredictos.conteo(resultado), Veredictos.conteo(estado)
        if c_resultado and c_estado and c_resultado != c_estado:
            hallazgos.append(Hallazgo(FALLA, donde, 0, "el conteo de criterios no cuadra (HU-014): "
                                                       "`resultado_pruebas` dice %s de %s y `estado-fase` dice %s de %s"
                                      % (c_resultado + c_estado)))
        return hallazgos

    # ── los avisos sobre el mismo árbol ──────────────────────────────────

    def cierre_sin_sello(self):
        """`EP-002·HU-005` · Un cierre nuevo dice bajo qué versión del estándar cerró."""
        hallazgos = []
        for actual, _, archivos in os.walk(self.arbol.raiz):
            if "funcionalidad_implementada.md" not in archivos:
                continue
            ruta = os.path.join(actual, "funcionalidad_implementada.md")
            texto = self.archivos.leer(ruta)
            fecha = _FECHA_CIERRE.search(texto)
            if fecha and fecha.group(1) >= SELLO_DESDE and not _SELLO_VERSION.search(texto):
                hallazgos.append(Hallazgo(AVISO, ruta, 0, "el cierre no dice bajo qué versión del estándar cerró — "
                                                          "sin el sello, una regla nueva de mañana parece incumplida "
                                                          "hoy (EP-002·HU-005)"))
        return hallazgos

    def _analisis_abierto_despues(self, plan):
        """El análisis sin aprobar que sigue al último que cita el plan, o `""`."""
        citados = {}
        for enlace, numero in _ENLACE_ANALISIS.findall(self.archivos.leer(plan)):
            carpeta = os.path.dirname(os.path.normpath(os.path.join(os.path.dirname(plan), enlace)))
            if os.path.isfile(os.path.join(carpeta, "pendiente.md")):
                citados[carpeta] = max(citados.get(carpeta, 0), int(numero))
        for carpeta, ultimo in citados.items():
            for nombre in sorted(os.listdir(carpeta)):
                m = re.match(r"^analisis-(\d+)\.md$", nombre)
                if (m and int(m.group(1)) > ultimo
                        and not _APROBADO_ANALISIS.search(self.archivos.leer(os.path.join(carpeta, nombre)))):
                    return os.path.join(carpeta, nombre)
        return ""

    def detenidas_por_un_hallazgo(self):
        """La fase o la HU que dicen haber cerrado con el análisis de un hallazgo abierto."""
        salida = []
        for nombre_epica in Epicas.subcarpetas(self.arbol.raiz):
            ruta_epica = os.path.join(self.arbol.raiz, nombre_epica)
            for nombre_hu in Epicas.subcarpetas(ruta_epica):
                if Epicas.historia(nombre_hu) is None:
                    continue
                ruta_hu = os.path.join(ruta_epica, nombre_hu)
                hu_md = os.path.join(ruta_hu, nombre_hu + ".md")
                for fase in Epicas.subcarpetas(ruta_hu):
                    plan = os.path.join(ruta_hu, fase, "plan_trabajo.md")
                    abierto = self._analisis_abierto_despues(plan) if os.path.isfile(plan) else ""
                    if not abierto:
                        continue
                    motivo = ("el análisis del hallazgo, `%s`, sigue sin aprobar: la fase está detenida "
                              "(EP-023·HU-004)" % self.proyecto.mostrar(abierto))
                    estado = os.path.join(ruta_hu, fase, ESTADO)
                    if re.search(r"^\|\s*\*\*Concepto\*\*\s*\|\s*Cumple", _leer(estado), re.M):
                        salida.append(Hallazgo(FALLA, estado, 0, "la fase dice «Cumple» y " + motivo))
                    if re.search(r"^\|\s*\*\*Estado\*\*\s*\|\s*Terminada", _leer(hu_md), re.M):
                        salida.append(Hallazgo(FALLA, hu_md, 0, "la HU dice «Terminada» y " + motivo))
        return salida

    def cuenta_escrita_a_mano(self):
        """Un inventario volvió a guardar la cuenta que el árbol ya sabe. Avisa, no corrige."""
        hallazgos = []
        for carpeta in CARPETAS_DEL_INVENTARIO:
            completa = self.proyecto.ruta(carpeta)
            if not os.path.isdir(completa):
                continue
            for nombre in sorted(os.listdir(completa)):
                ruta = os.path.join(completa, nombre)
                if not nombre.lower().endswith(".md") or not os.path.isfile(ruta):
                    continue
                hallazgos += [Hallazgo(AVISO, carpeta + "/" + nombre, 0,
                                       "guarda la cuenta a mano en el campo **%s**, y el árbol ya la sabe: la da "
                                       "`validar.py fases`. Dos copias del mismo dato se separan (EP-004·HU-019)"
                                       % campo)
                              for campo in CUENTA_A_MANO.findall(_leer(ruta))]
        return hallazgos

    @staticmethod
    def vocabulario_de_estados():
        """`{"Historia de usuario": {"Pendiente", …}}` del glosario del estándar, o `{}`."""
        texto = _leer(os.path.join(Proyecto.estandar() or "", "base", "glosario.md"))
        conjuntos = {}
        for quien, lista in _CONJUNTO.findall(texto):
            conjuntos[quien] = {e for e in (x.strip().strip("*") for x in lista.split("·")) if e}
        return conjuntos

    def estado_fuera_del_vocabulario(self):
        """`EP-003·HU-012` · Se mira con qué palabra empieza: «Terminada el 2026-08-14»
        es correcto. La negrita se tolera; la caja no. Que el campo falte no se reporta acá."""
        validos = self.vocabulario_de_estados().get("Historia de usuario")
        if not validos or not self.arbol.existe():
            return []
        lista = " · ".join(sorted(validos))
        hallazgos = []
        for epica in Epicas.subcarpetas(self.arbol.raiz):
            for nombre_hu in Epicas.subcarpetas(os.path.join(self.arbol.raiz, epica)):
                if Epicas.historia(nombre_hu) is None:
                    continue
                relativa = "%s/%s/%s/%s.md" % (CARPETA, epica, nombre_hu, nombre_hu)
                dice = _ESTADO_DECLARADO.search(_leer(self.proyecto.ruta(relativa)))
                if not dice:
                    continue
                valor = dice.group(1).strip().lstrip("*")
                if not valor:
                    hallazgos.append(Hallazgo(AVISO, relativa, 0, "declara su estado vacío. Los que valen: %s "
                                                                  "(EP-003·HU-012)" % lista))
                elif not any(valor.startswith(v) for v in validos):
                    hallazgos.append(Hallazgo(AVISO, relativa, 0, "declara el estado «%s», que el glosario no "
                                                                  "define. Los que valen para una historia: %s "
                                                                  "(EP-003·HU-012)"
                                              % (valor.split("—")[0].split(".")[0].strip()[:34], lista)))
        return hallazgos

    def documentos_que_siguen_siendo_el_molde(self):
        """`EP-004·HU-022` · Dice cuáles, no cuántos: una cifra sin nombres no deja ir a arreglar nada."""
        if not self.moldes:
            return []
        hallazgos = []
        for _, hu in self._historias():
            for fase in self.arbol.fases(hu):
                for documento, quedan in self.moldes.sin_llenar(fase.ruta):
                    hallazgos.append(Hallazgo(AVISO, "%s/%s" % (fase.donde, documento), 0,
                                              "sigue siendo la plantilla: conserva %d de sus marcadores, por ejemplo "
                                              "`%s` — la fase no cuenta terminada mientras esté así (EP-004·HU-022)"
                                              % (len(quedan), sorted(quedan)[0])))
        return hallazgos

    def reemplazos_que_no_resuelven(self):
        """`EP-004·HU-023` · Cada declaración que no se puede aplicar, con el nombre
        escrito: un campo mal escrito que no dice nada parece que funcionó."""
        hallazgos = []
        for _, hu in self._historias():
            fases = self._fases_de(hu.ruta)
            for nombre in fases:
                ruta_fase = os.path.join(hu.ruta, nombre)
                nombrada = Veredictos.declara_reemplazar(ruta_fase)
                if not nombrada:
                    continue
                if nombrada == nombre:
                    motivo = "se nombra a sí misma"
                elif nombrada not in fases:
                    motivo = "esa fase no está en esta historia"
                elif Veredictos.de_la_fase(ruta_fase) != "Cumple":
                    motivo = "quien declara no cumple, y un rojo no cierra otro rojo"
                else:
                    continue
                hallazgos.append(Hallazgo(AVISO, "%s/%s/funcionalidad_implementada.md" % (hu.donde, nombre), 0,
                                          "declara reemplazar el veredicto de `%s` y no se aplica: %s — el veredicto "
                                          "anterior sigue contando (EP-004·HU-023)" % (nombrada, motivo)))
        return hallazgos

    def estacion_del_commit_sin_marcar(self):
        """`EP-005·HU-019` · Un aviso por grupo, diciendo cuáles. Las sin marcar son
        dos cosas: con el cierre escrito es solo la marca; sin él, es trabajo."""
        solo_marca, sin_commit, sin_fila = [], [], []
        for _, hu in self._historias():
            for fase in self.arbol.fases(hu):
                texto = _leer(fase.documento(ESTADO))
                if not texto:
                    continue
                if not EstacionDelCommit.tiene_fila(texto):
                    sin_fila.append(fase.nombre)
                elif EstacionDelCommit.ya_marcada(texto):
                    continue
                elif _leer(fase.documento("funcionalidad_implementada.md")):
                    solo_marca.append(fase.nombre)
                else:
                    sin_commit.append(fase.nombre)
        hallazgos = []
        if solo_marca:
            hallazgos.append(Hallazgo(AVISO, CARPETA, 0, "%d fase(s) con su cierre escrito y la estación 12 sin "
                                                         "marcar — **es la marca, no el trabajo**: %s (EP-005·HU-019)"
                                      % (len(solo_marca), _lista(solo_marca, 5))))
        if sin_commit:
            hallazgos.append(Hallazgo(AVISO, CARPETA, 0, "%d fase(s) sin cierre escrito y sin marcar — **esto sí es "
                                                         "trabajo**: %s (EP-005·HU-019)"
                                      % (len(sin_commit), _lista(sin_commit))))
        if sin_fila:
            hallazgos.append(Hallazgo(AVISO, CARPETA, 0, "%d fase(s) **sin la fila de la estación 12**: no hay dónde "
                                                         "marcar, y el enganche no las toca. Se cuentan aparte porque "
                                                         "no se puede afirmar sobre un campo que no existe "
                                                         "(04·R4, EP-005·HU-019)" % len(sin_fila)))
        return hallazgos

    # ── la cuenta ────────────────────────────────────────────────────────

    def fase_terminada(self, ruta_fase):
        """Sus cinco documentos están **y ninguno sigue siendo el molde**."""
        return (all(os.path.isfile(os.path.join(ruta_fase, d)) for d in DOCUMENTOS)
                and not self.moldes.sin_llenar(ruta_fase))

    def historia_terminada(self, ruta_hu):
        """Al menos una fase, y **todas** terminadas: cerrar la primera no cierra la historia."""
        fases = self._fases_de(ruta_hu)
        return bool(fases) and all(self.fase_terminada(os.path.join(ruta_hu, f)) for f in fases)

    def inventario(self):
        """`(total, completas, incompletas)` de las HU. Una carpeta `HU-` sin su
        documento cuenta, como incompleta: no contarla la volvería invisible."""
        total = completas = 0
        for _, hu in self._historias():
            total += 1
            completas += self.historia_terminada(hu.ruta)
        return total, completas, total - completas

    def por_veredicto(self):
        """`(cumplen, no_cumplen, sin_veredicto)` de las HU **terminadas**. Basta una
        fase que no cumpla; lo que no se deja leer se cuenta aparte (`04·R4`)."""
        cumplen = no_cumplen = sin_veredicto = 0
        for _, hu in self._historias():
            if not self.historia_terminada(hu.ruta):
                continue
            fases = self._fases_de(hu.ruta)
            dejados = Veredictos.reemplazados(hu.ruta, fases)
            dichos = [Veredictos.de_la_fase(os.path.join(hu.ruta, f)) for f in fases if f not in dejados]
            if any(v is None for v in dichos):
                sin_veredicto += 1
            elif "No cumple" in dichos:
                no_cumplen += 1
            else:
                cumplen += 1
        return cumplen, no_cumplen, sin_veredicto

    def linea_inventario(self):
        """La línea que cierra la corrida, o `""` si no hay árbol. Dice qué es cada
        número: «completas» se leía como «cumplen»."""
        total, completas, incompletas = self.inventario()
        if not total:
            return ""
        cumplen, no_cumplen, sin_veredicto = self.por_veredicto()
        return ("HU: %d en total · %d sin terminar · %d terminadas, de las cuales %d cumplen, %d no cumplen y "
                "%d no dicen si cumplen (F12.2)" % (total, incompletas, completas, cumplen, no_cumplen, sin_veredicto))
