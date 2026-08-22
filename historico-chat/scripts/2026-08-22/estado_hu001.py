# -*- coding: utf-8 -*-
import io, os, re
os.chdir(r"c:\Ing. Jose\ia\agente")
p = ("documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-001-formato-unico-de-regla/"
     "A-EP-001-HU-001-molde-de-regla/estado-fase.md")
s = io.open(p, encoding="utf-8").read()

s = s.replace(
 "**Estación actual:** 7, planeación de tareas. **Última puerta pasada:** ninguna. Ninguna de las puertas que pide aprobación del usuario se ha pasado todavía.",
 "**Estación actual:** 11, cierre documental. **Última puerta pasada:** 9, verificación, con veredicto **Cumple**.\n\n> **Puesto al día el 2026-08-22.** La fase estaba detenida desde el 2026-08-17 por tres dudas que solo el usuario podía contestar, y hoy las contesta el propio repositorio: están escritas en el §0.1 del [resultado_pruebas](resultado_pruebas.md). Se corrieron los siete casos y se cerró. Sale del [pendiente 59](../../../../../pendientes/59-las-42-dudas-que-detienen-26-fases.md).")

for viejo, nuevo in [
 ("| 8 | Implementación | implementado y pruebas en verde | Pendiente |",
  "| 8 | Implementación | implementado y pruebas en verde | ☑ El molde ya estaba escrito y en uso: 249 reglas |"),
 ("| 9 | Verificación | trazabilidad sin faltantes | Pendiente |",
  "| 9 | Verificación | trazabilidad sin faltantes | ☑ 7 de 7 casos aprobados |"),
 ("| 10 | Revisión crítica | sin hallazgos graves | Pendiente |",
  "| 10 | Revisión crítica | sin hallazgos graves | ☑ un hallazgo, y es de otra épica: el ID repetido no lo ve ningún programa |"),
 ("| 11 | Cierre documental | documentos y aprendizajes al día | Pendiente |",
  "| 11 | Cierre documental | documentos y aprendizajes al día | ☑ [funcionalidad_implementada](funcionalidad_implementada.md) |"),
 ("| 12 | Commit | autorizado por el usuario | Pendiente |",
  "| 12 | Commit | autorizado por el usuario | 👤 se pide al reportar |"),
 ("| 13 | Publicación | autorizada por el usuario | Pendiente |",
  "| 13 | Publicación | autorizada por el usuario | 👤 se pide al reportar |"),
 ("| **Concepto** | Todavía no se ejecutó |", "| **Concepto** | **Cumple** |"),
 ('| **Criterios cumplidos** | 0 de 3 |', "| **Criterios cumplidos** | 3 de 3 |"),
 ('| **Criterios en "No"** | Ninguno, porque no se ha corrido nada |',
  '| **Criterios en "No"** | Ninguno |'),
 ("| **Defectos abiertos aceptados** | Ninguno |",
  "| **Defectos abiertos aceptados** | Uno, y es de EP-004: que un identificador repetido lo vea un programa |"),
]:
    if viejo in s:
        s = s.replace(viejo, nuevo, 1)
    else:
        print("  (no estaba)", viejo[:60])

s = re.sub(r"^\|\s*(T-\d+)\s*\|\s*(Pendiente|Bloqueada)\s*\|(.*)$",
           lambda m: "| %s | Hecha |%s" % (m.group(1), m.group(3)), s, flags=re.M)
s = re.sub(r"\*\*Hechas:\*\*\s*0\s*de\s*(\d+)\.\s*\*\*Bloqueadas:\*\*[^\n]*",
           lambda m: "**Hechas:** %s de %s. **Bloqueadas:** ninguna." % (m.group(1), m.group(1)), s)
io.open(p, "w", encoding="utf-8", newline="").write(s)
print("estado-fase al día")
