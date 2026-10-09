# -*- coding: utf-8 -*-
"""Validadores del estándar: el punto de entrada único.

Uso:
  python validadores/validar.py estandar
  python validadores/validar.py plantilla <documento.md> [--contra <plantilla.md>]
  python validadores/validar.py commit [--archivo <ruta> | --revision HEAD]

Código de salida: 0 si no hay FALLA, 1 si hay al menos una.
Los AVISO no rompen la ejecución: señalan lo que un humano debe mirar.

Es el mismo programa que vivía en `validadores/validar.py` (sesión del
2026-10-04, análisis 1 del pendiente 116), pero llama a las clases de
`core/`. `validadores/validar.py` quedó como puerta: los `.githooks` de cada
proyecto instalado lo llaman por esa ruta. La salida impresa es la de antes,
letra por letra; lo comprueba `historico-chat/scripts/2026-10-04/paridad_validar.py`.
"""
import argparse
import datetime
import os
import sys

from ..comun import Archivos, Proyecto
from ..comun.consola import Reporte, preparar_salida
from ..enganches.origen import OrigenDeCadaPunto
from ..enganches.plan_vs_hecho import PlanContraLoHecho
from ..herramientas.corredor import PruebasDelEstandar
from ..herramientas.mapa_tareas import MapaDeTareasAlDia
from ..herramientas.temas import IndiceTematico
from ..validadores import (ArchivosVersionados, Auditoria, CapturasYLogs, CatalogoDelProyecto,
                           Checklist, CitasEnlazadas, ConsultasCostosas, ConvencionDeNombres,
                           CrucesEntreModulos, DocumentoContraPlantilla, EnlacesRotos,
                           EstructuraDeFases, Expediente, FuncionesLargas, HistoricoInmutable,
                           IndicesDeCarpetas, IndicesPorAfinar, IntegracionContinua,
                           IntegridadDeEsquema, InventarioDeAcciones, InyeccionYSesion, Linter,
                           LockfileVersionado, MapaDelAmarre, MapaDelSitio, MarcasDeGeneracion,
                           MensajeDeCommit, Metareglas, MigracionesReversibles, Numeracion,
                           NumeracionDePendientes, PruebasAisladas, QuienLaHaceCumplir, RamaDedicada,
                           Reaperturas, SecretosEnElCodigo, SesionesMezcladas, Suite, TablasDeDominio,
                           TrazabilidadDeFases, VersionDelCambio, VersionDelEstandar, Vigencia)
from ..validadores.analisis import AnalisisAprobados
from ..validadores.brevedad import Brevedad
from ..validadores.conteo import ConteoPorRegla
from ..validadores.flujo import PlanDeLaFase
from ..validadores.indices import CompletadorDeIndices
from ..validadores.pendientes import Pendientes
from ..validadores.parecidas import ReglasParecidas
from ..validadores.repetidas import FuncionesRepetidas
from ..validadores.traza import Traza
from ..validadores.versiones import DocumentosHeredados, RegistroDeVersiones

# La carpeta del estándar: el `--raiz` por defecto de lo que revisa el estándar,
# y desde donde se nombran las rutas en los reportes.
RAIZ = Proyecto.estandar()


def raiz_del_proyecto():
    """Dónde está parado quien corre el comando, no dónde vive el estándar.

    `61` · **`RAIZ` es la carpeta del propio estándar**, y usarla por defecto en
    los subcomandos que revisan *un proyecto* hacía que revisaran el estándar
    creyendo que revisaban el proyecto. Lo reportó `rni-dp`: `validar.py
    secretos` le devolvió **10 fallas y 8 avisos** sobre archivos de
    `validadores/`, una carpeta que ese proyecto no tiene; eran las claves
    falsas que el propio detector usa para comprobar que detecta.

    **Lo grave no es el ruido: es que la comprobación decía que sí había
    corrido.** Un validador de secretos que siempre falla deja de servir para
    ver lo nuevo, y lo nuevo aquí son credenciales.

    Los subcomandos que revisan **el estándar** siguen apuntando a `RAIZ`: ahí
    sí es lo correcto.
    """
    return os.getcwd()


# `EP-004·HU-008` · Las comprobaciones que **no** entran en la corrida completa,
# cada una con su motivo. Se nombran una por una, no por patrón: una lista ancha
# dejaría fuera, sin que nadie lo note, el subcomando que se registre mañana.
FUERA_DE_LA_CORRIDA = {
    "todo": "es esta misma",
    "linter": "corre la herramienta del proyecto y tarda; va aparte",
    "suite": "corre la suite del proyecto y tarda; va aparte",
    "internas": "corre las pruebas del propio estándar y tarda; va aparte",
    "audit": "sale a la red a preguntar por vulnerabilidades; va aparte",
    "plantilla": "necesita que le digan qué documento revisar",
    "commit": "necesita el mensaje del commit",
    "traza": "necesita la transcripción de una sesión",
    "temas": "escribe un archivo cuando se le pide `--aplicar`",
    "plan": "necesita el commit del que salió la fase para comparar archivos",
    "sesiones": "mira lo que está preparado para un commit; fuera de esa hora no hay nada que mirar",
    "parecidas": "se pide para una regla o para lo que entra en el commit; sobre todas, lista casi 150",
}


class _Reporte(Reporte):
    """El `Reporte` de siempre, con dos diferencias que dejan la salida como era.

    Una ruta relativa se lee desde donde está parado quien corre el comando,
    como hacía `relativo`: el mensaje de un commit llega como
    `.git/COMMIT_EDITMSG` desde la carpeta del proyecto, y leída desde el
    estándar nombraría un archivo que no es.

    Y una ruta de fuera del estándar se escribe como se pidió: `Proyecto`
    resuelve la raíz con `realpath`, que en Windows cambia `c:` por `C:`, y
    el reporte de un proyecto diría su carpeta distinto de como la dio el enganche.
    """

    def __init__(self, raiz=None):
        super().__init__(raiz)
        self.pedidas = []

    def como_se_pidio(self, archivo):
        for pedida in self.pedidas:
            real = os.path.realpath(pedida)
            if real == pedida:
                continue
            resto = archivo[len(real):]
            if os.path.normcase(archivo[:len(real)]) == os.path.normcase(real) and resto[:1] in ("", "\\", "/"):
                return pedida + resto
        return archivo

    def donde(self, hallazgo):
        archivo = self.como_se_pidio(os.path.abspath(hallazgo.archivo)) if hallazgo.archivo else hallazgo.archivo
        ruta = self.proyecto.mostrar(archivo)
        return "%s:%s" % (ruta, hallazgo.linea) if hallazgo.linea else ruta


class Consola:
    """Los subcomandos de `validar.py`. Un solo `Reporte` y un solo `Archivos`
    por corrida: la corrida completa cuenta por regla todo lo que se reportó, y
    lo que no se pudo leer se dice en cada reporte que venga después."""

    def __init__(self):
        self.reporte = _Reporte(RAIZ)
        self.archivos = Archivos()
        self.analizador = None
        self.nombres = ()

    # ── lo común ──────────────────────────────────────────────────────────

    def reportar(self, hallazgos, titulo=None):
        return self.reporte.reportar(hallazgos, titulo, self.archivos)

    def relativo(self, ruta):
        """Ruta relativa al estándar; completa si vive fuera de él."""
        return self.reporte.proyecto.mostrar(ruta)

    # ── la corrida completa ───────────────────────────────────────────────

    def cmd_todo(self, a):
        """`EP-004·HU-008` · Una línea dice cómo está el proyecto.

        **Por qué no llama a los validadores uno por uno**: cada subcomando sabe
        cosas que su clase no (qué raíz usar, qué imprimir, qué recorrer), y
        copiarlas acá sería tener dos versiones de lo mismo. Se corre **el mismo
        subcomando** que correría una persona, con sus valores por defecto.

        **Lo lento y lo que pide argumentos quedan fuera, con su motivo escrito.**
        Es la decisión 23 del pendiente 59: `linter`, `suite` y `audit` van aparte
        porque tardan, y una corrida que tarda no se corre.
        """
        resumen = []
        peor = 0
        fuera = dict(FUERA_DE_LA_CORRIDA)
        nombres = self.nombres

        # **El estándar no es un proyecto instalado**, y las comprobaciones de
        # instalación miden justamente eso. Corridas sobre la carpeta donde vive
        # el estándar dan falla siempre, y una falla que siempre está apaga la
        # corrida entera.
        if os.path.isdir(os.path.join(a.raiz, "base")) and os.path.isfile(os.path.join(a.raiz, "VERSION")):
            for nombre, motivo in (("checklist", "mide si un proyecto tiene el estándar instalado"),
                                   ("versiones", "compara los documentos heredados con los del estándar"),
                                   ("version", "compara la versión que declara un proyecto")):
                fuera[nombre] = motivo + "; acá estamos **en** el estándar"

        for nombre in nombres:
            if nombre in fuera:
                continue
            try:
                sub_args = self.analizador.parse_args([nombre])
            except SystemExit:
                resumen.append((nombre, None, "pide argumentos: se corre aparte"))
                continue
            if getattr(sub_args, "raiz", "") is None:
                sub_args.raiz = a.raiz
            elif getattr(a, "raiz", None):
                sub_args.raiz = a.raiz
            try:
                codigo = sub_args.func(sub_args)
            except SystemExit as e:
                codigo = int(getattr(e, "code", 1) or 0)
            except Exception as e:              # noqa: BLE001
                # `EP-004·HU-003` · Que una comprobación reviente no puede
                # llevarse a las otras cuarenta: se anota y la corrida sigue.
                resumen.append((nombre, 1, "reventó: %s" % e))
                peor = 1
                continue
            resumen.append((nombre, codigo, ""))
            peor = max(peor, codigo or 0)
            print()

        # `EP-004·HU-009` · El conteo por regla, que es lo que dice **qué regla
        # cambiar**. Se anota una línea por corrida, fuera del control de
        # versiones, con el identificador y el número: nunca el texto del hallazgo.
        todos = list(self.reporte.corrida)
        if todos:
            conteo = ConteoPorRegla(a.raiz, self.archivos)
            conteo.anotar(todos, cuando=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            print()
            for linea in conteo.lineas(todos):
                print(linea)
        print("== Corrida completa · %s ==" % self.relativo(os.path.abspath(a.raiz)))
        con_falla = [n for n, c, _ in resumen if c == 1]
        rotos = [(n, m) for n, c, m in resumen if m and "reventó" in m]
        for nombre, motivo in fuera.items():
            if nombre in nombres and nombre != "todo":
                print("  (fuera: %s — %s)" % (nombre, motivo))
        print("%d comprobación(es) corridas · %d con fallas%s"
              % (len(resumen), len(con_falla), (": " + ", ".join(con_falla)) if con_falla else ""))
        for nombre, motivo in rotos:
            print("  %s %s" % (nombre, motivo))
        if not con_falla:
            print("Sin fallas. Los avisos de cada comprobación salen arriba.")

        return 1 if peor else 0

    # ── el estándar y sus documentos ──────────────────────────────────────

    def cmd_estandar(self, a):
        indices = IndicesDeCarpetas(a.raiz, self.archivos)
        hallazgos = (EnlacesRotos(a.raiz, self.archivos).validar()
                     + indices.archivos_de_carpetas()
                     + indices.dias_de_resumenes()
                     + CitasEnlazadas(a.raiz, self.archivos).validar())
        return self.reportar(hallazgos, "Coherencia del estándar")

    def cmd_plantilla(self, a):
        if not os.path.isfile(a.documento):
            sys.exit(f"no existe el documento: {a.documento}")

        texto = self.archivos.leer(a.documento)
        ruta_plantilla = a.contra or DocumentoContraPlantilla.deducir(a.documento, texto)

        if not ruta_plantilla:
            sys.exit(
                f"no se pudo deducir la plantilla de {self.relativo(a.documento)}.\n"
                f"Indícala con --contra plantillas/<archivo>.md")
        if not os.path.isfile(ruta_plantilla):
            sys.exit(f"no existe la plantilla: {ruta_plantilla}")

        hallazgos = DocumentoContraPlantilla(RAIZ, a.documento, ruta_plantilla, self.archivos).validar()
        return self.reportar(hallazgos, f"{self.relativo(a.documento)} contra {self.relativo(ruta_plantilla)}")

    def cmd_fases(self, a):
        raiz = os.path.abspath(a.raiz)
        fases = EstructuraDeFases(raiz, self.archivos)
        codigo = self.reportar(fases.validar(), f"Épica → HU → Fase · {self.relativo(raiz)}")
        # HU-017 · el inventario va al final, después de los hallazgos: es el
        # resumen de cuánto falta, no un incumplimiento más.
        linea = fases.linea_inventario()
        if linea:
            print(linea)
        return codigo

    def cmd_pendientes(self, a):
        raiz = os.path.abspath(a.raiz)
        codigo = self.reportar(NumeracionDePendientes(raiz, self.archivos).validar(),
                               f"Numeración de pendientes · {self.relativo(raiz)}")
        # HU-018 · el próximo número libre va siempre, haya hallazgos o no.
        pendientes = Pendientes(raiz, self.archivos)
        linea = pendientes.linea_proximo()
        if linea:
            print(linea)
        # `EP-023·HU-003·CA-08` · el índice lo arma el programa, no se edita a mano.
        if getattr(a, "indice", False):
            print(f"Índice escrito en {self.relativo(pendientes.escribir_indice())}")
        return codigo

    def cmd_trazabilidad(self, a):
        raiz = os.path.abspath(a.raiz)
        return self.reportar(TrazabilidadDeFases(raiz, self.archivos).validar(),
                             f"Trazabilidad épica↔HU · plan · cierre · {self.relativo(raiz)}")

    def cmd_versionado(self, a):
        raiz = os.path.abspath(a.raiz)
        proyecto = Proyecto(raiz)
        repos = proyecto.repositorios()
        if not repos:
            sys.exit(f"no hay repositorios git en {self.relativo(raiz)}")

        versionado = ArchivosVersionados(raiz, self.archivos, solo_preparados=a.preparados)
        hallazgos = []
        for repo in repos:
            hallazgos += versionado.revisar_repositorio(repo, proyecto.prefijo_de(repo) or repo)

        # `EP-005·HU-005` · Y lo que **no** se puede guardar: un cambio de la norma
        # sin su versión y su entrada. Solo cuando se mira el commit.
        if a.preparados:
            for repo in repos:
                hallazgos += VersionDelCambio(repo, self.archivos,
                                              ruta_mostrada=proyecto.prefijo_de(repo) or repo).validar()

        # `22` · Y la numeración en sí: es la misma pregunta (¿este cambio está
        # versionado?) vista por el número.
        hallazgos += Numeracion(raiz, self.archivos).validar()

        alcance = "lo que entra en el commit" if a.preparados else "todo el repositorio"
        return self.reportar(hallazgos, f"Qué está versionado ({alcance}) · {self.relativo(raiz)}")

    def cmd_metareglas(self, a):
        """`53` · El único programa que comprueba once de las veinte filas del
        checklist del estándar no tenía por dónde correrse."""
        raiz = os.path.abspath(a.raiz)
        hallazgos = Metareglas(raiz, self.archivos).validar()
        if a.catalogo:
            hallazgos += CatalogoDelProyecto(a.catalogo, self.archivos, estandar=raiz).validar()
        return self.reportar(hallazgos, f"El estándar contra sus meta-reglas · {self.relativo(raiz)}")

    def cmd_ejecutable(self, a):
        """`EP-005·HU-012` · Qué regla del núcleo tiene quien la ejecute, y cuál no."""
        raiz = os.path.abspath(a.raiz)
        ejecutable = QuienLaHaceCumplir(raiz, self.archivos)
        codigo = self.reportar(ejecutable.validar(), f"Quién hace cumplir el núcleo · {self.relativo(raiz)}")
        linea = ejecutable.como_texto()
        if linea:
            print(linea)
        return codigo

    def cmd_acciones(self, a):
        """`13` · El inventario de lo que el agente puede hacer, y qué cuesta deshacerlo."""
        raiz = os.path.abspath(a.raiz)
        acciones = InventarioDeAcciones(raiz, self.archivos)
        codigo = self.reportar(acciones.validar(), f"Acciones del agente y su riesgo · {self.relativo(raiz)}")
        linea = acciones.linea_resumen()
        if linea:
            print(linea)
        return codigo

    def cmd_tareas(self, a):
        """`EP-005·HU-023` · Toda regla dice a qué tareas aplica, y el mapa las junta."""
        raiz = os.path.abspath(a.raiz)
        return self.reportar(MapaDeTareasAlDia(raiz, self.archivos).validar(),
                             f"El mapa de tareas · {self.relativo(raiz)}")

    def cmd_amarre(self, a):
        """`15` · Qué se queda y qué hay que rehacer si mañana el agente es otro."""
        raiz = os.path.abspath(a.raiz)
        amarre = MapaDelAmarre(raiz, self.archivos)
        codigo = self.reportar(amarre.validar(), f"El mapa del amarre a la herramienta · {self.relativo(raiz)}")
        linea = amarre.linea_resumen()
        if linea:
            print(linea)
        return codigo

    def cmd_analisis(self, a):
        """`13·DOC24` · `EP-023·HU-001·CA-06` · Un análisis aprobado trae sus cuatro partes."""
        raiz = os.path.abspath(a.raiz)
        return self.reportar(AnalisisAprobados(raiz, self.archivos).validar(),
                             f"Las cuatro partes de cada análisis aprobado · {self.relativo(raiz)}")

    def cmd_origen(self, a):
        """`02·F27` · `EP-023·HU-002·CA-01` · Cada punto dice de qué punto del anterior sale."""
        raiz = os.path.abspath(a.raiz)
        return self.reportar(OrigenDeCadaPunto(raiz, self.archivos).validar(),
                             f"Cada punto dice de dónde sale · {self.relativo(raiz)}")

    def cmd_sitio(self, a):
        """`33` · El mapa del sitio no envejece: una carpeta nueva se ve enseguida."""
        raiz = os.path.abspath(a.raiz)
        sitio = MapaDelSitio(raiz, self.archivos)
        codigo = self.reportar(sitio.validar(), f"El mapa del sitio · {self.relativo(raiz)}")
        linea = sitio.linea_resumen()
        if linea:
            print(linea)
        return codigo

    def cmd_temas(self, a):
        """`33` · Los temas del histórico, en un archivo en vez de en cuarenta."""
        raiz = os.path.abspath(a.raiz)
        temas = IndiceTematico(raiz, self.archivos)
        if a.aplicar:
            print(f"escrito {self.relativo(temas.escribir())}")
        codigo = self.reportar(temas.validar(), f"El índice temático del histórico · {self.relativo(raiz)}")
        linea = temas.linea_resumen()
        if linea:
            print(linea)
        return codigo

    def cmd_plan(self, a):
        """`EP-004·HU-013` · Lo hecho contra el plan aprobado."""
        raiz = os.path.abspath(a.raiz)
        plan = PlanContraLoHecho(raiz, self.archivos, fase=a.fase, desde=a.desde)
        if a.preparados:
            # `EP-023·HU-007` · lo que entra en el commit, contra el plan aprobado.
            return self.reportar(plan.comparar_preparados(),
                                 f"Lo que entra en el commit contra el plan · {self.relativo(raiz)}")
        if a.rango:
            # `EP-023·HU-007·CA-02` · lo que trae un rango de commits, en la
            # integración continua.
            return self.reportar(plan.comparar_rango(a.rango),
                                 f"Lo que trae {a.rango} contra el plan · {self.relativo(raiz)}")
        codigo = self.reportar(plan.validar(), f"El plan aprobado contra lo hecho · {self.relativo(raiz)}")
        print(plan.linea_resumen())
        return codigo

    def cmd_brevedad(self, a):
        """`58` · Cuánto ocupa lo que el agente contesta. **Mide, no detiene.**

        `ID9` no se puede comprobar con un programa (decidir qué palabra sobra
        exige entender qué cambia la decisión del que lee) y esto no lo intenta.
        Cuenta lo que sí se cuenta.
        """
        raiz = os.path.abspath(a.raiz)
        brevedad = Brevedad(raiz, self.archivos)
        codigo = self.reportar(brevedad.validar(), f"Brevedad de las respuestas · {self.relativo(raiz)}")
        linea = brevedad.como_texto()
        if linea:
            print(linea)
        return codigo

    def cmd_inmutable(self, a):
        """La transcripción del histórico solo crece: se agrega, no se reescribe."""
        raiz = os.path.abspath(a.raiz)
        return self.reportar(HistoricoInmutable(raiz, self.archivos).validar(),
                             f"Histórico que solo crece · {self.relativo(raiz)}")

    def cmd_traza(self, a):
        """`EP-005 · HU-016` · Qué ejecutó la sesión, paso a paso. **Lee, no valida.**"""
        ruta = os.path.abspath(a.transcripcion)
        lista = Traza.pasos(ruta)
        if not lista:
            print("sin pasos que trazar: el archivo no existe, está vacío o no "
                  f"tiene llamadas a herramientas — {ruta}")
            return 1
        texto = Traza.como_texto(lista, Traza.cierre(lista))
        if not a.escribir:
            print(texto)
            return 0
        raiz = os.path.abspath(a.raiz)
        destino = Traza.escribir(raiz, Traza.sesion_de(ruta), texto)
        if not destino:
            print("no hay dónde dejarla: falta historico-chat/, o ningún histórico "
                  f"lleva la marca de la sesión {Traza.sesion_de(ruta)}")
            return 1
        print(f"traza escrita: {os.path.relpath(destino, raiz)}")
        return 0

    def cmd_indices(self, a):
        """`09·14` · Escribe la línea del índice que falta, en vez de solo reportarla.

        **Sin `--aplicar` solo dice qué escribiría.** Es el mismo trato que el resto
        de los reparadores: ver antes de tocar.
        """
        raiz = os.path.abspath(a.raiz)
        tocados = CompletadorDeIndices(raiz, self.archivos).completar(escribir=a.aplicar)
        print(f"== Índices · {self.relativo(raiz)} ==")
        if not tocados:
            print("OK: ningún índice tiene líneas que agregar.")
        else:
            marca = "escrito" if a.aplicar else "simulado; agrega --aplicar"
            for archivo, cuantas in tocados:
                print(f"  {self.relativo(archivo)}: {cuantas} línea(s) ({marca})")
        return self.reportar(IndicesPorAfinar(raiz, self.archivos).validar(), None)

    def cmd_reaperturas(self, a):
        """`09·10` · Qué fases se reabrieron. **Mide retrabajo, no culpa.**"""
        raiz = os.path.abspath(a.raiz)
        reaperturas = Reaperturas(raiz, self.archivos)
        codigo = self.reportar(reaperturas.validar(), f"Fases reabiertas · {self.relativo(raiz)}")
        linea = reaperturas.linea_resumen()
        if linea:
            print(linea)
        return codigo

    def cmd_marcas(self, a):
        """`11` · Las marcas de `00·ID8` en lo que se hereda.

        Solo `base/` y `plantillas/`: es lo que viaja a los proyectos. Con
        `--preparados` mira **lo que entra en el commit** y aplica el trinquete:
        que la cuenta no suba. Es lo que corre el enganche.
        """
        raiz = os.path.abspath(a.raiz)
        if a.preparados:
            return self.reportar(MarcasDeGeneracion(raiz, self.archivos, solo_preparados=True).validar(),
                                 f"Marcas nuevas en lo que se va a guardar · {self.relativo(raiz)}")
        # `EP-004·HU-024` · El resultado no se entrega solo: va con el alcance.
        # Un cero decía dos cosas distintas y no las separaba: «no hay marcas» y
        # «acá no se miró». Las dos frases salen de lo que la corrida recorrió.
        marcas = MarcasDeGeneracion(raiz, self.archivos)
        salida = self.reportar(marcas.validar(), f"Marcas de generación automática · {self.relativo(raiz)}")
        donde, sin_contar = marcas.alcance()
        print(f"Alcance: {donde}.")
        print(f"Y {sin_contar}.")
        return salida

    def cmd_sesiones(self, a):
        """`80` · Que un commit no se lleve el trabajo de otra sesión. **Avisa y no detiene.**"""
        raiz = os.path.abspath(a.raiz)
        return self.reportar(SesionesMezcladas(raiz, self.archivos).validar(),
                             f"Sesiones mezcladas en el commit · {self.relativo(raiz)}")

    def cmd_pruebas(self, a):
        """`EP-029·HU-003` · Si la revisión de pruebas falta o está vencida. Con
        «no dejar guardar» es falla y el `pre-commit` rechaza; si no, avisa."""
        from ..comun import AVISO, FALLA, Hallazgo
        from ..pruebas.aviso import RevisionDelProyecto
        raiz = os.path.abspath(a.raiz)
        textos, detiene = RevisionDelProyecto(raiz).avisos()
        nivel = FALLA if detiene else AVISO
        return self.reportar([Hallazgo(nivel, raiz, 0, texto) for texto in textos],
                             f"Revisión de pruebas · {self.relativo(raiz)}")

    def cmd_expediente(self, a):
        """El mapa de completitud del expediente de un proyecto. **Nunca falla.**"""
        raiz = os.path.abspath(a.raiz)
        lineas, hallazgos = Expediente(raiz, self.archivos).reporte()
        print(f"== Expediente del ciclo · {self.relativo(raiz)} ==")
        for linea in lineas:
            print(linea)
        if hallazgos:
            print()
            for h in hallazgos:
                print(self.reporte.linea(h))
        return 0

    def cmd_vigencia(self, a):
        """`14` · Qué reglas llevan más tiempo sin que nadie se pregunte si sirven. **Nunca falla.**"""
        raiz = os.path.abspath(a.raiz)
        return self.reportar(Vigencia(raiz, self.archivos).validar(), f"Vigencia de las reglas · {self.relativo(raiz)}")

    # ── el código de un proyecto ──────────────────────────────────────────

    def _uno(self, clase, titulo, a):
        """Los subcomandos que son un validador y un título, nada más."""
        raiz = os.path.abspath(a.raiz)
        return self.reportar(clase(raiz, self.archivos).validar(), f"{titulo} · {self.relativo(raiz)}")

    def cmd_secretos(self, a):
        return self._uno(SecretosEnElCodigo, "Secretos en el código", a)

    def cmd_dependencias(self, a):
        return self._uno(LockfileVersionado, "Lockfile versionado", a)

    def cmd_rama(self, a):
        return self._uno(RamaDedicada, "Rama de trabajo", a)

    def cmd_migraciones(self, a):
        return self._uno(MigracionesReversibles, "Migraciones reversibles", a)

    def cmd_errores(self, a):
        return self._uno(CapturasYLogs, "Errores tragados", a)

    def cmd_rendimiento(self, a):
        return self._uno(ConsultasCostosas, "Cargas sin límite", a)

    def cmd_esquema(self, a):
        return self._uno(IntegridadDeEsquema, "Integridad de esquema", a)

    def cmd_estructura(self, a):
        """`01` · Dónde vive el código y cómo se llama, contra la convención que el proyecto declara."""
        return self._uno(ConvencionDeNombres, "Ubicación y nombres del código", a)

    def cmd_entidades(self, a):
        """`01` · Lo que se le exige a una tabla de dominio: `03·D1`, `15·IM2`, `15·IM5`."""
        return self._uno(TablasDeDominio, "Tablas de dominio y entidades inmutables", a)

    def cmd_cruces(self, a):
        """`01` · El cruce entre dos módulos se registra en los dos: `13·DOC7`."""
        return self._uno(CrucesEntreModulos, "Cruces entre módulos", a)

    def cmd_flujo(self, a):
        return self._uno(PlanDeLaFase, "Plan de trabajo", a)

    def cmd_ci(self, a):
        return self._uno(IntegracionContinua, "Integración continua", a)

    def cmd_seguridad(self, a):
        return self._uno(InyeccionYSesion, "Concatenación e inyección", a)

    def cmd_calidad(self, a):
        return self._uno(FuncionesLargas, "Funciones largas", a)

    def cmd_repetidas(self, a):
        """`07·Q4` · `EP-004·HU-026` · La función que hace lo mismo que otra. Avisa, no
        frena. Con `--preparados`, solo las nuevas del commit."""
        raiz = os.path.abspath(a.raiz)
        alcance = "lo que entra en el commit" if a.preparados else "todo el código"
        return self.reportar(FuncionesRepetidas(raiz, self.archivos, solo_preparados=a.preparados).validar(),
                             f"Funciones repetidas ({alcance}) · {self.relativo(raiz)}")

    def cmd_parecidas(self, a):
        """`20·M12` · `EP-004·HU-027` · Las reglas que se parecen por significado.
        Avisa, no frena. Con `--regla`, las de esa; con `--preparados`, las de lo
        que entra en el commit."""
        raiz = os.path.abspath(a.raiz or Proyecto.estandar())
        alcance = ", ".join(a.regla) if a.regla else ("lo que entra en el commit" if a.preparados else "todas")
        validador = ReglasParecidas(raiz, self.archivos, ids=a.regla, solo_preparados=a.preparados)
        return self.reportar(validador.validar(), f"Reglas parecidas ({alcance}) · {self.relativo(raiz)}")

    def cmd_aislamiento(self, a):
        return self._uno(PruebasAisladas, "Pruebas aisladas", a)

    def cmd_linter(self, a):
        return self._uno(Linter, "Linter/formateador", a)

    def cmd_suite(self, a):
        return self._uno(Suite, "Suite de pruebas", a)

    def cmd_auditoria(self, a):
        return self._uno(Auditoria, "Audit de vulnerabilidades", a)

    def cmd_internas(self, a):
        """Las pruebas del estándar. Apunta a `RAIZ` y no a donde esté parado
        quien lo corre: son las pruebas **del estándar**. `suite` es la otra."""
        if a.reclamo:
            # Mirar una fecha, no correr las pruebas: es lo que puede colgarse de
            # algo que pasa seguido sin volverse un peaje de 9,6 minutos.
            return self.reportar(PruebasDelEstandar(RAIZ, self.archivos).reclamo(),
                                 "¿Hace falta correr las pruebas del estándar?")
        return self.reportar(PruebasDelEstandar(RAIZ, self.archivos, solo=a.solo).validar(),
                             "Pruebas del estándar")

    # ── la instalación en un proyecto ─────────────────────────────────────

    def cmd_version(self, a):
        return self._uno(VersionDelEstandar, "Versión del estándar", a)

    def cmd_checklist(self, a):
        raiz = os.path.abspath(a.raiz)
        puntos = Checklist(raiz).revisar()
        if not puntos:
            sys.exit("no se pudo leer plantillas/stack-instalacion.md")

        print(f"== Instalación del agente · {self.relativo(raiz)} ==")
        for p in puntos:
            print(f"  {p}")

        faltan = Checklist.pendientes(puntos)
        print(f"\n{Checklist.resumen(raiz, puntos)}")
        if faltan:
            print(f"\n{Checklist.detalle(puntos)}")

        # El desfase de número se informa, no reprueba: lo que el proyecto tiene
        # que aplicar ya lo dicen los componentes de arriba.
        for h in VersionDelEstandar(raiz, self.archivos).validar():
            print(f"\nAl margen: {h.mensaje}")
        return 1 if faltan else 0

    def cmd_versiones(self, a):
        raiz = os.path.abspath(a.raiz)
        heredados, registro = DocumentosHeredados(raiz), RegistroDeVersiones(raiz)
        print(f"== Documentos heredados del estándar · {self.relativo(raiz)} ==")
        for e in heredados.estado():
            marca = "ok" if e.al_dia else "VIEJO"
            print(f"  [{marca}] {e.id} — {e.mensaje() or e.componente.destino}")

        ultima = registro.version_registrada()
        print(f"\nÚltima actualización registrada: {ultima or '(ninguna)'}")
        for nombre, fecha, ver in registro.registros()[-5:]:
            print(f"  {fecha}  {ver:<10} {nombre}")

        atrasados = heredados.viejos()
        cumple, detalle = registro.revisar()
        if not cumple:
            print(f"\n{detalle}")
        if atrasados:
            print("\nSe pone al día con:")
            print(f'  python "{RAIZ.replace(os.sep, "/")}/validadores/instalar.py" '
                  f'"{raiz.replace(os.sep, "/")}" --aplicar')
        return 1 if (atrasados or not cumple) else 0

    def cmd_commit(self, a):
        if a.archivo:
            mensaje, origen = self.archivos.leer(a.archivo), a.archivo
            commit = MensajeDeCommit(os.getcwd(), self.archivos, mensaje=mensaje, origen=origen)
        else:
            origen = f"commit {a.revision}"
            commit = MensajeDeCommit(os.getcwd(), self.archivos, revision=a.revision)
        return self.reportar(commit.validar(), f"Mensaje de {origen}")

    # ── el analizador ─────────────────────────────────────────────────────

    def armar(self):
        """El analizador con todos los subcomandos. `todo` lo usa para correr a los demás."""
        p = argparse.ArgumentParser(
            prog="validar.py",
            description="Comprueba lo que del estándar se puede comprobar sin criterio.")
        sub = p.add_subparsers(dest="comando", required=True)
        proyecto = "carpeta del proyecto (por defecto, donde estás parado)"

        def agregar(nombre, ayuda, func, raiz=False, **raiz_kw):
            s = sub.add_parser(nombre, help=ayuda)
            if raiz is not False:
                s.add_argument("--raiz", default=raiz, **raiz_kw)
            s.set_defaults(func=func)
            return s

        agregar("todo", "la corrida completa en una línea · todo lo que aplica, menos lo lento",
                self.cmd_todo, None, help=proyecto)
        agregar("estandar", "enlaces rotos e índices desactualizados", self.cmd_estandar, RAIZ)

        pl = agregar("plantilla", "un documento contra su plantilla", self.cmd_plantilla)
        pl.add_argument("documento")
        pl.add_argument("--contra", help="ruta de la plantilla (si no se deduce sola)")

        agregar("fases", "jerarquía y nombres de épica/HU/fase · 02·F12", self.cmd_fases, None, help=proyecto)

        pd = agregar("pendientes", "numeración de `pendientes/` y cruce con su índice · HU-018",
                     self.cmd_pendientes, None, help=proyecto)
        pd.add_argument("--indice", action="store_true",
                        help="escribe `documentacion/pendientes.md` con todos los pendientes · EP-023·HU-003")

        agregar("trazabilidad", "enlace épica↔HU, ORIGEN y tabla de cierre · F4/DOC",
                self.cmd_trazabilidad, None, help=proyecto)

        v = agregar("versionado", "secretos y artefactos versionados · 09-git.md · G3",
                    self.cmd_versionado, None, help=proyecto)
        v.add_argument("--preparados", action="store_true",
                       help="solo lo que entra en el commit actual (para el enganche)")

        mr = agregar("metareglas", "el cuerpo de reglas contra el checklist del capítulo 20",
                     self.cmd_metareglas, RAIZ, help="carpeta del estándar")
        mr.add_argument("--catalogo", help="carpeta de un proyecto, para comprobar además su catálogo · M16")

        agregar("ejecutable", "qué regla del núcleo declara quien la hace cumplir",
                self.cmd_ejecutable, RAIZ, help="carpeta del estándar")
        agregar("reaperturas", "qué fases volvieron atrás desde su cierre · retrabajo",
                self.cmd_reaperturas, RAIZ, help="carpeta del estándar")

        ix = agregar("indices", "escribe la línea del índice que falta · 13·DOC13",
                     self.cmd_indices, RAIZ, help="carpeta del estándar")
        ix.add_argument("--aplicar", action="store_true", help="escribe de verdad; sin esto solo simula")

        agregar("sesiones", "que el commit no mezcle el trabajo de dos sesiones · avisa",
                self.cmd_sesiones, RAIZ, help="carpeta del estándar")

        agregar("pruebas", "que la revisión de pruebas esté al día · EP-029·HU-003",
                self.cmd_pruebas, RAIZ, help="carpeta del proyecto")

        ma = agregar("marcas", "marcas de generación automática en lo que se hereda · 00·ID8",
                     self.cmd_marcas, RAIZ, help="carpeta del estándar")
        ma.add_argument("--preparados", action="store_true",
                        help="solo lo que entra en el commit, y con trinquete: falla si la cuenta sube")

        agregar("expediente", "qué entregables del ciclo tiene el proyecto · informa, no detiene",
                self.cmd_expediente, RAIZ, help="carpeta del proyecto")
        agregar("vigencia", "reglas que nadie ha revisado de fondo · EP-001·HU-007·CA-04",
                self.cmd_vigencia, RAIZ, help="carpeta del estándar")
        agregar("acciones", "el inventario de acciones del agente y su riesgo · 00·N1",
                self.cmd_acciones, RAIZ, help="carpeta del estándar")
        agregar("amarre", "qué piezas están atadas a la herramienta · el mapa no envejece",
                self.cmd_amarre, RAIZ, help="carpeta del estándar")
        agregar("tareas", "toda regla dice a qué tareas aplica y el mapa está al día",
                self.cmd_tareas, RAIZ, help="carpeta del estándar")

        pv = agregar("plan", "lo hecho contra el plan aprobado · 02·F8 y sus casos",
                     self.cmd_plan, RAIZ, help="carpeta del proyecto")
        pv.add_argument("--fase", help="carpeta de una fase concreta")
        pv.add_argument("--desde", help="commit del que salió la fase")
        pv.add_argument("--preparados", action="store_true",
                        help="lo que entra en el commit: falla por lo que el plan no declara ni una regla autoriza")
        pv.add_argument("--rango",
                        help="lo que trae un rango de commits, desde..hasta: lo usa la integración continua")

        te = agregar("temas", "índice temático del histórico · buscar por tema, no por fecha",
                     self.cmd_temas, RAIZ, help="carpeta del proyecto")
        te.add_argument("--aplicar", action="store_true",
                        help="escribe el índice; sin esto solo dice si quedó atrás")

        agregar("analisis", "cada análisis aprobado trae sus cuatro partes · EP-023·HU-001",
                self.cmd_analisis, RAIZ, help="carpeta del repositorio")
        agregar("origen", "cada punto dice de qué punto del anterior sale · 02·F27",
                self.cmd_origen, RAIZ, help="carpeta del repositorio")
        agregar("sitio", "el mapa del sitio nombra toda carpeta que existe · no envejece",
                self.cmd_sitio, RAIZ, help="carpeta del estándar")
        agregar("inmutable", "la transcripción del histórico solo crece · detecta, no impide",
                self.cmd_inmutable, RAIZ, help="carpeta del proyecto")
        agregar("brevedad", "cuánto ocupa lo que el agente contesta · 00·ID9 · mide, no detiene",
                self.cmd_brevedad, RAIZ, help="carpeta del estándar")

        tr = sub.add_parser("traza", help="qué ejecutó la sesión, paso a paso · EP-005 · HU-016 · lee, no valida")
        tr.add_argument("transcripcion", help="el archivo de líneas JSON de la sesión")
        tr.add_argument("--escribir", action="store_true",
                        help="deja la traza en historico-chat/trazas/ junto al histórico de la sesión")
        tr.add_argument("--raiz", default=RAIZ, help="carpeta del proyecto")
        tr.set_defaults(func=self.cmd_traza)

        for nombre, ayuda, func in (
                ("estructura", "dónde vive el código y cómo se llama · 14·EST1 · 14·EST2", self.cmd_estructura),
                ("entidades", "tablas de dominio y entidades inmutables · 03·D1 · 15·IM2 · 15·IM5",
                 self.cmd_entidades),
                ("cruces", "el cruce entre dos módulos se registra en los dos · 13·DOC7", self.cmd_cruces),
                ("secretos", "secretos incrustados en el código · 04·S4", self.cmd_secretos),
                ("dependencias", "lockfile presente y versionado · 10·DEP2", self.cmd_dependencias),
                ("rama", "trabajo en rama dedicada y al día · 09·G4", self.cmd_rama),
                ("migraciones", "cada migración declara su reversión · 03·D2", self.cmd_migraciones),
                ("errores", "capturas de error vacías · 05·E1", self.cmd_errores),
                ("rendimiento", "`SELECT *` y cargas sin límite · 06·R2", self.cmd_rendimiento),
                ("esquema", "FK con política de borrado · 03·D1", self.cmd_esquema),
                ("flujo", "el plan de trabajo: 13 preguntas e incertidumbre · 02·F14/F17", self.cmd_flujo),
                ("seguridad", "concatenación SQL/shell y asignación masiva · 04·S3", self.cmd_seguridad),
                ("calidad", "funciones demasiado largas · 07·Q3", self.cmd_calidad),
                ("ci", "pipeline de CI con pruebas y linter · 09·G6", self.cmd_ci),
                ("aislamiento", "pruebas contra BD efímera, no real · 08·T4", self.cmd_aislamiento),
                ("linter", "corre el linter/formateador del stack · 07·Q6", self.cmd_linter),
                ("suite", "corre la suite de pruebas del stack · 08·T5", self.cmd_suite)):
            agregar(nombre, ayuda, func, None, help=proyecto)

        rp = agregar("repetidas", "funciones que repiten lo que hace otra · 07·Q4", self.cmd_repetidas, None,
                     help=proyecto)
        rp.add_argument("--preparados", action="store_true",
                        help="solo las funciones nuevas de lo que entra en el commit")

        pa = agregar("parecidas", "reglas que se parecen por significado · 20·M12", self.cmd_parecidas, None,
                     help=proyecto)
        pa.add_argument("--regla", action="append", help="el ID de la regla (F25); se puede repetir")
        pa.add_argument("--preparados", action="store_true", help="solo las reglas de lo que entra en el commit")

        inte = agregar("internas", "corre las pruebas del propio estándar · 08·T5", self.cmd_internas)
        inte.add_argument("solo", nargs="*", help="archivos a correr; sin esto, todos (02·F5)")
        inte.add_argument("--reclamo", action="store_true", help="no corre nada: solo dice si hace falta correrlas")

        for nombre, ayuda, func in (
                ("audit", "audit de vulnerabilidades del stack · 10·DEP3", self.cmd_auditoria),
                ("version", "desfase de versión del estándar vs la que declara el proyecto", self.cmd_version),
                ("checklist", "stack de instalación del agente: qué le falta al proyecto", self.cmd_checklist),
                ("versiones", "documentos heredados del estándar: cuáles quedaron viejos", self.cmd_versiones)):
            agregar(nombre, ayuda, func, None, help=proyecto)

        c = agregar("commit", "mensaje de commit contra 09-git.md · G2", self.cmd_commit)
        c.add_argument("--archivo", help="archivo con el mensaje (p. ej. COMMIT_EDITMSG)")
        c.add_argument("--revision", default="HEAD", help="commit ya hecho (por defecto HEAD)")

        self.analizador = p
        self.nombres = tuple(sub.choices)
        return p

    def correr(self, argv=None):
        a = self.armar().parse_args(argv)
        # `61` · El que revisa **un proyecto** arranca donde está parado el usuario.
        # Antes caía en la carpeta del estándar y revisaba el estándar creyendo que
        # revisaba el proyecto: silencioso, y el resultado decía que sí había corrido.
        if getattr(a, "raiz", "") is None:
            a.raiz = raiz_del_proyecto()
        for pedida in (getattr(a, "raiz", None), getattr(a, "catalogo", None)):
            if pedida:
                self.reporte.pedidas.append(os.path.abspath(pedida))
        return a.func(a)


def main(argv=None):
    """Corre la orden y devuelve el código de salida.

    Lo que antes terminaba con `sys.exit("mensaje")` (sin repositorio, sin
    plantilla) sigue diciendo el mensaje por la salida de errores y vuelve con 1;
    la ayuda y los argumentos mal puestos vuelven con el código de `argparse`.
    """
    preparar_salida()
    try:
        return Consola().correr(argv)
    except SystemExit as e:
        if isinstance(e.code, str):
            print(e.code, file=sys.stderr)
            return 1
        return e.code or 0


if __name__ == "__main__":
    sys.exit(main())
