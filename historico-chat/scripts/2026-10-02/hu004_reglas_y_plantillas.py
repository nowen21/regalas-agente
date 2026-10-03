# -*- coding: utf-8 -*-
"""Fase A de la HU-004: T-01, T-02, T-04 a T-08. Reglas y plantillas, según el análisis 1 del pendiente 103
(conclusiones 9, 10, 18, 19, 24, 31, 33 y 41) y el análisis 2 (conclusión 7). Los sellos de checklist de
las reglas que cambian se vuelven a aplicar contra 47.0.0."""
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SELLO = "contra **v47.0.0**, el **2026-10-02**."


def cambiar(relativa, pares):
    ruta = os.path.join(RAIZ, *relativa.split("/"))
    with open(ruta, encoding="utf-8") as f:
        t = f.read()
    for viejo, nuevo in pares:
        assert t.count(viejo) == 1, (relativa, viejo[:70])
        t = t.replace(viejo, nuevo)
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)


def main():
    cambiar("base/02-flujo-de-trabajo/reglas/F28-el-cambio-se-aplica-donde-nace-y-baja-en-orden.md", [
        ("y baja en orden por la épica, la HU, la especificación y el plan. Ningún documento de abajo cambia antes que el de arriba",
         "y baja en orden por la épica, la HU, la especificación y el plan. Cada uno cambia en su mismo archivo, que pasa a su versión siguiente; el análisis no se reescribe, se numera el siguiente"),
        ("CORRECTO:   se corrige la HU, después la especificación y al final el plan\n",
         "CORRECTO:   se corrige la HU en su mismo archivo, después la especificación\n            y al final el plan, cada uno en su versión siguiente\n"),
        ("contra **v42.0.0**, el **2026-10-02**.", SELLO),
    ])
    cambiar("base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md", [
        ("Descubrir a mitad que hace falta otro **detiene la ejecución**: se pausa, se reporta, se propone ampliar el plan y se espera el OK.",
         "Descubrir a mitad que hace falta otro **detiene la ejecución** y vuelve al análisis: el plan pasa a su versión siguiente con aprobación nueva."),
        ("CORRECTO:   descubre Y → PAUSA + reporta + propone ampliar el plan → usuario\n            aprueba (o difiere Y a otra fase) → sigue con el plan actualizado\n",
         "CORRECTO:   descubre Y → se detiene → vuelve al análisis → el plan pasa a\n            su versión siguiente y el usuario la aprueba → sigue\n"),
        ("contra **v30.8.0**, el **2026-08-22**.", SELLO),
    ])
    cambiar("base/02-flujo-de-trabajo/reglas/F9-no-subdividas-ni-renegocies-un-plan-ya-aprobado.md", [
        ("Se reportan como hallazgo derivado, no como opción a elegir, y no habilitan a repartir el trabajo restante (límite). Retomar lo decide el usuario (autoriza).",
         "Detienen la ejecución y vuelven al análisis, no se ofrecen como opción a elegir, y no habilitan a repartir el trabajo restante (límite). Retomar lo decide el usuario al aprobar el análisis (autoriza)."),
        ("contra **v30.8.0**, el **2026-08-22**.", SELLO),
    ])
    cambiar("base/13-documentacion/reglas/DOC24-cierra-el-analisis-en-su-mismo-archivo.md", [
        ("lo que aparezca después abre el análisis siguiente (deroga",
         "lo que aparezca después abre el análisis siguiente, que trata solo lo que falló y sus implicaciones, y decide primero si es parte del plan en curso: si lo es, se resuelve antes de seguir; si no, nace su pendiente y el plan sigue (deroga"),
        ("contra **v40.0.0**, el **2026-10-01**.", SELLO),
    ])
    cambiar("base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md", [
        ("Si hay duda de si una fase está cerrada, decide el usuario ([`01·C7`](../../01-conducta.md#c7--ante-dos-lecturas-pregunta)) (autoriza).",
         "Si hay duda de si una fase está cerrada, decide el usuario ([`01·C7`](../../01-conducta.md#c7--ante-dos-lecturas-pregunta)) (autoriza). Un hallazgo sobre lo que una fase cerrada construyó sí la reabre, y su plan pasa a la versión siguiente ([`02·F28`](../../02-flujo-de-trabajo/reglas/F28-el-cambio-se-aplica-donde-nace-y-baja-en-orden.md))."),
        ("contra **v30.8.0**, el **2026-08-22**.", SELLO),
    ])
    cambiar("base/02-flujo-de-trabajo/base.md", [
        ("**el plan aprobado no se modifica para anotarle resultados**, porque entonces se pierde contra qué comparar.",
         "**el plan aprobado no se modifica para anotarle resultados**, porque entonces se pierde contra qué comparar. Si al ejecutarlo aparece un hallazgo, la ejecución se detiene, vuelve al análisis y el plan pasa a su versión siguiente, con aprobación nueva ([`F28`](reglas/F28-el-cambio-se-aplica-donde-nace-y-baja-en-orden.md))."),
    ])
    cambiar("base/02-flujo-de-trabajo/nomenclatura-de-fases.md", [
        ("Ej.: `D-B-EP-001-HU-003-Ajuste de la validación de permisos` (la fase `D` complementa a la `B`).\n",
         "Ej.: `D-B-EP-001-HU-003-Ajuste de la validación de permisos` (la fase `D` complementa a la `B`).\n\n"
         "**Ajuste aprobado por el usuario en el análisis 1 del pendiente 103 (punto 18), 2026-10-02:** el complemento es para trabajo nuevo. "
         "Si aparece un hallazgo sobre lo que una fase ya construyó, esa fase se reabre y su plan pasa a la versión siguiente; no se crea otra que la complemente.\n"),
    ])
    cambiar("plantillas/ciclo-vida-proyectos/07-plan-trabajo.md", [
        ("Este plan se queda como se aprobó, para comparar lo que se dijo contra lo que pasó.",
         "Este plan se queda como se aprobó, para comparar lo que se dijo contra lo que pasó. Lo único que se le anota al cerrar es cuántos hallazgos salieron al ejecutarlo, para saber si el análisis funcionó."),
    ])
    with open(os.path.join(RAIZ, "plantillas", "ciclo-vida-proyectos", "07-plan-trabajo.md"), encoding="utf-8") as f:
        t = f.read()
    if "Hallazgos al ejecutar" not in t:
        t = t.rstrip("\n") + "\n\n**Hallazgos al ejecutar:** «número», con el enlace al análisis que abrió cada uno, o «ninguno».\n"
        with open(os.path.join(RAIZ, "plantillas", "ciclo-vida-proyectos", "07-plan-trabajo.md"), "w", encoding="utf-8", newline="\n") as f:
            f.write(t)
    cambiar("plantillas/ciclo-vida-proyectos/10-estado-fase.md", [
        ("**Motivo:** «pruebas rojas / hallazgo grave del Crítico / alcance rechazado / dependencia faltante».",
         "**Motivo:** «hallazgo al ejecutar, con el enlace al análisis que abrió / pruebas rojas / hallazgo grave del Crítico / alcance rechazado / dependencia faltante»."),
    ])
    cambiar("plantillas/analisis.md", [
        ("se abre `analisis-«N+1»`.md, que trata solo lo que falló y sus implicaciones sobre lo ya hecho.",
         "se abre `analisis-«N+1»`.md, que trata solo lo que falló y sus implicaciones sobre lo ya hecho. Primero decide si el hallazgo es parte del plan en curso: si lo es, el pendiente se mejora y se resuelve antes de seguir; si no, se crea su pendiente y el plan continúa."),
    ])


if __name__ == "__main__":
    main()
