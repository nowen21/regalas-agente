# -*- coding: utf-8 -*-
"""Las fases que ya se ejecutaron y cuyo `estado-fase` quedó diciendo que no.

No inventa nada: solo se aplica a las fases cuyo `resultado_pruebas` y
`funcionalidad_implementada` están escritos, con veredicto. Lo que corrige es el
documento que se quedó atrás.
"""
import io, os, re, glob
os.chdir(r"c:\Ing. Jose\ia\agente")

NOTA = ("\n> **Puesto al día el 2026-08-22.** Este documento decía que no se había "
        "ejecutado ninguna tarea, y la fase estaba **hecha y probada**: su "
        "[resultado_pruebas](resultado_pruebas.md) trae el veredicto y su "
        "[funcionalidad_implementada](funcionalidad_implementada.md) el cierre. "
        "Lo que faltaba era este archivo, que es justo el que una sesión nueva "
        "lee para saber por dónde va. Sale del [pendiente 59]"
        "(../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md).\n")

FASES = [
 "documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/A-EP-001-HU-010-cuando-la-historia-hace-de-especificacion",
 "documentacion/epicas/EP-004-comprobacion-automatica/HU-012-marcas-de-generacion-automatica/A-EP-004-HU-012-contar-las-marcas-de-generacion-automatica",
 "documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-002-enmascarar-claves/A-EP-005-HU-002-enmascarar-la-clave-antes-de-escribirla",
 "documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-004-control-del-mensaje-de-cambio/A-EP-005-HU-004-retrodocumentar-el-control-del-mensaje-de-cambio",
 "documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-010-la-regla-llega-al-escribir-el-archivo/A-EP-005-HU-010-el-capitulo-llega-al-escribir-el-archivo",
]

for carpeta in FASES:
    p = os.path.join(carpeta, "estado-fase.md")
    s = io.open(p, encoding="utf-8").read()
    original = s

    # 1 · Las filas de tareas pasan a hechas.
    def fila(m):
        return "| %s | Hecha |%s" % (m.group(1), m.group(3))
    s = re.sub(r"^\|\s*(T-\d+)\s*\|\s*(Pendiente|Bloqueada)\s*\|(.*)$", fila, s, flags=re.M)

    # 2 · El recuento.
    def recuento(m):
        n = m.group(1)
        return "**Hechas:** %s de %s. **Bloqueadas:** ninguna." % (n, n)
    s = re.sub(r"\*\*Hechas:\*\*\s*0\s*de\s*(\d+)\.\s*\*\*Bloqueadas:\*\*[^\n]*",
               recuento, s)

    # 3 · Los avisos de que no arrancó.
    s = re.sub(r"\n\*\*Nada se ejecutó todavía\.\*\*[^\n]*\n", "\n", s)
    s = re.sub(r"\n>\s*\*\*El plan quedó aprobado[^\n]*\n(?:>[^\n]*\n)*", "\n", s)
    s = re.sub(r"\n>\s*\*\*(?:La fase|Esta fase)[^\n]*(?:sigue|no arrancó|detenid)[^\n]*\n(?:>[^\n]*\n)*", "\n", s)

    # 4 · La nota de por qué se tocó este archivo hoy.
    if "Puesto al día el 2026-08-22" not in s:
        i = s.find("## 1.2")
        if i < 0:
            i = s.find("## 2.")
        s = s[:i] + NOTA.lstrip("\n") + "\n" + s[i:]

    io.open(p, "w", encoding="utf-8", newline="").write(s)
    print(("cambiado " if s != original else "SIN CAMBIO ") + os.path.basename(carpeta))
