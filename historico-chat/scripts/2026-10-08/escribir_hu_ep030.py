"""Escribe las nueve HU de la EP-030 y su tabla en la épica, desde el análisis 1 del pendiente 142."""
import glob
import os
import re

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
BASE = os.path.join(RAIZ, "documentacion", "epicas", "EP-030-los-documentos-de-cimiento-viven-en-su-base")
A = ("../../../../historico-chat/resumenes/2026-10-08/pendientes/"
     "142-los-documentos-de-cimiento-viven-en-la-base/analisis-1.md")

H = [
    ("Un solo camino para leer y escribir documentos, con un comando fijo por tipo", "Técnica", "L",
     "Cada operación sobre un documento termina en un guion nuevo, y los programas leen los .md por caminos distintos",
     "Claude, al crear o cambiar un documento", "usar un comando fijo (crear, ver, editar, listar) en vez de escribir un guion",
     "no repetir código de un solo uso", 1, "1, 2 y 3", [
         ("Un comando fijo crea, muestra, edita y lista un documento",
          "Dado un tipo de documento registrado\nCuando se corre su comando crear, ver, editar o listar\n"
          "Entonces la operación se hace en la base\nY no hace falta escribir ningún guion"),
         ("Todo programa lee y escribe documentos por el mismo camino",
          "Dado un programa que necesita un documento\nCuando lo lee o lo escribe\n"
          "Entonces usa el camino único de Cimiento\nY no abre el archivo por su cuenta"),
         ("Cada cambio queda en la historia",
          "Dado un documento\nCuando se cambia por el camino único\n"
          "Entonces queda una fila en Cambio con el antes y el después")]),
    ("Los cambios de los documentos se revisan y se aprueban en la pantalla", "Funcional", "M",
     "Git deja de mostrar los cambios de los documentos que pasan a la base",
     "quien administra Cimiento", "ver qué cambió en cada documento, con el antes y el después, y aprobarlo con un botón",
     "revisar el trabajo sin depender de git", 2, "5", [
         ("La pantalla muestra lo que cambió",
          "Dados cambios en documentos sin aprobar\nCuando se abre la pantalla de revisión\n"
          "Entonces se ve cada documento con su antes y su después"),
         ("Se aprueba con un botón",
          "Dado un cambio sin aprobar\nCuando se oprime Aprobar\nEntonces queda aprobado con la cuenta y la hora\n"
          "Y se une al botón que guarda en git de la EP-026·HU-007")]),
    ("Los pendientes y los análisis viven en la base, partidos en campos", "Técnica", "L",
     "Los documentos que más se escriben en cada conversación siguen siendo archivos",
     "Claude y el freno", "guardar y leer pendientes y análisis en tablas con campos",
     "no depender de archivos ni de marcas de texto", 3, "2 y 3", [
         ("Pendientes y análisis tienen su tabla",
          "Dado un pendiente o un análisis\nCuando se crea o se cambia\nEntonces queda en su tabla, partido en campos"),
         ("Los existentes pasan a la base",
          "Dados los pendiente.md y analisis-N.md que existen\nCuando se corre el comando de importación\n"
          "Entonces quedan en la base\nY sus archivos se borran después de comprobar que todo funciona"),
         ("Los programas que los usan leen la base",
          "Dados el freno, analisis_en_curso, andamio, cerrar y los validadores que leen pendientes y análisis\n"
          "Cuando trabajan\nEntonces leen y escriben la base")]),
    ("Las épicas, las HU y los documentos de cada fase viven en la base, partidos en campos", "Técnica", "XL",
     "La cadena (épica, HU y fase) son unos 2.000 archivos",
     "Claude y el freno", "guardar y leer la cadena en tablas con campos",
     "que el plan aprobado, los criterios y los resultados se consulten sin leer texto", 4, "2 y 3", [
         ("La cadena tiene sus tablas",
          "Dada una épica, una HU o un documento de fase\nCuando se crea o se cambia\n"
          "Entonces queda en su tabla, partido en campos"),
         ("Las existentes pasan a la base",
          "Dados los .md de la cadena\nCuando se corre el comando de importación\nEntonces quedan en la base\n"
          "Y sus archivos se borran después de comprobar que todo funciona"),
         ("Los programas que la usan leen la base",
          "Dados andamio, fase, veredicto, plan_vs_hecho, acuerdos, origen y los validadores\nCuando trabajan\n"
          "Entonces leen y escriben la base")]),
    ("Las transcripciones y los resúmenes de sesión viven en la base", "Técnica", "M",
     "Los enganches escriben archivos en cada turno",
     "los enganches", "guardar cada turno y cada hallazgo en la base",
     "que la conversación no dependa de archivos", 5, "2 y 3", [
         ("Cada turno queda en la base",
          "Dado un mensaje del usuario o una respuesta\nCuando el enganche lo anota\nEntonces queda en la base con su hora"),
         ("Los existentes pasan a la base",
          "Dadas las transcripciones y los resúmenes que existen\nCuando se corre el comando de importación\n"
          "Entonces quedan en la base\nY sus archivos se borran después de comprobar que todo funciona")]),
    ("Las plantillas, notas, prompts, anatomía, CHANGELOG y señales viven en la base", "Técnica", "M",
     "Quedan archivos sueltos fuera de la base",
     "Claude y quien administra Cimiento",
     "consultar plantillas, notas, prompts, anatomía, `CHANGELOG.md` y señales en la base",
     "que no quede ningún .md suelto", 6, "1 y 3", [
         ("Cada uno tiene su tabla",
          "Dada una plantilla, nota, prompt, página de anatomía, entrada del CHANGELOG o señal\n"
          "Cuando se crea o se cambia\nEntonces queda en su tabla"),
         ("Los existentes pasan a la base",
          "Dados los .md de esos tipos\nCuando se corre el comando de importación\nEntonces quedan en la base\n"
          "Y sus archivos se borran después de comprobar que todo funciona")]),
    ("Los índices README y CLAUDE.md desaparecen", "Técnica", "S",
     "404 índices solo sirven para navegar carpetas, y CLAUDE.md se lee del disco",
     "Claude", "recibir por los enganches lo que hoy dice CLAUDE.md, y consultar listas en vez de índices",
     "que no queden archivos que nadie necesita", 7, "1 y 3", [
         ("Los README de índice se quitan",
          "Dados los README de índice\nCuando ya no queda nada que los necesite\nEntonces se borran\n"
          "Y las listas salen de consultas a la base"),
         ("CLAUDE.md llega por los enganches",
          "Dado lo que dice CLAUDE.md\nCuando abre una sesión\nEntonces el enganche se lo pasa a Claude desde la base\n"
          "Y el archivo ya no existe")]),
    ("Las reglas hablan de registros de la base, no de archivos", "Técnica", "M",
     "Las reglas y plantillas piden carpetas y archivos que ya no existen",
     "quien sigue el estándar", "leer reglas que describen cómo se trabaja de verdad",
     "no incumplir reglas imposibles", 8, "1", [
         ("Ninguna regla pide un archivo de documento",
          "Dadas las reglas de los capítulos 02 y 13 y las plantillas\nCuando se revisan\n"
          "Entonces hablan de registros de la base\nY suben la versión del estándar")]),
    ("Los proyectos que heredan guardan sus documentos en la base de Cimiento", "Técnica", "L",
     "Los proyectos que heredan siguen recibiendo .md del instalador",
     "cada proyecto que Cimiento administra", "guardar sus documentos en la base de Cimiento, con su nombre",
     "que todos trabajen igual", 9, "4", [
         ("El instalador no escribe .md",
          "Dado un proyecto\nCuando se instala Cimiento\nEntonces no recibe CLAUDE.md, .agente/*.md ni historico-chat/\n"
          "Y sus documentos quedan en la base de Cimiento con el nombre del proyecto"),
         ("Los existentes pasan a la base",
          "Dados los .md de un proyecto ya instalado\nCuando vuelve a instalar\nEntonces pasan a la base\n"
          "Y es un cambio MAYOR del estándar")]),
]

PLANTILLA = """# HU-{i:03d} · {tit}

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-{i:03d} |
| **Épica / Feature** | [EP-030 · Los documentos de Cimiento viven en su base, con un comando fijo por cada tipo](../epica.md) |
| **Módulo / Componente** | Cimiento |
| **Tipo** | {tipo} |
| **Prioridad** | Must |
| **Estimación** | {est} |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Pendiente |

---

## 2. Narrativa

- **Como** {rol}
- **Quiero** {quiero}
- **Para** {para}

---

## 3. Contexto y descripción

{prob}. Sale del [análisis 1 del pendiente 142]({a}), acuerdos {acu}, punto {punto} de «Lo que se tiene que hacer».

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Cada documento se guarda partido en campos (acuerdo 2) |
| RN-02 | Los archivos se borran solo después de comprobar que todo funciona con la base (acuerdo 3) |

### 3.2 Supuestos

- La base de Cimiento está disponible donde se trabaja.

### 3.3 Fuera de alcance

- Los `.py`, que siguen como archivos (acuerdo 1).

---

## 4. Criterios de aceptación

{ca}---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | {dep} | Alto |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-08 | El agente | Creación de la HU, desde el análisis 1 del pendiente 142 |
"""


def main():
    epica = os.path.join(BASE, "epica.md")
    texto_epica = open(epica, encoding="utf-8").read()
    for i, (tit, tipo, est, prob, rol, quiero, para, punto, acu, casos) in enumerate(H, 1):
        carpeta = glob.glob(os.path.join(BASE, "HU-%03d-*" % i))[0]
        ca = ""
        for j, (nombre, gherkin) in enumerate(casos, 1):
            ca += ("### CA-%02d · %s\n\n**Sale de:** análisis 1 del pendiente 142, punto %d de «Lo que se tiene que hacer»\n\n"
                   "```gherkin\n%s\n```\n\n**Cómo validarlo:** se define en el plan de pruebas de la fase.\n\n"
                   % (j, nombre, punto, gherkin))
        dep = "Ninguna" if i == 1 else "Las HU anteriores de la EP-030, según la hoja de ruta de la épica"
        hu = glob.glob(os.path.join(carpeta, "HU-*.md"))[0]
        with open(hu, "w", encoding="utf-8") as f:
            f.write(PLANTILLA.format(i=i, tit=tit, tipo=tipo, est=est, rol=rol, quiero=quiero, para=para,
                                     prob=prob, a=A, acu=acu, punto=punto, ca=ca, dep=dep))
        readme = os.path.join(carpeta, "README.md")
        r = open(readme, encoding="utf-8").read().replace("La historia de usuario: «…»", "La historia de usuario: " + tit)
        open(readme, "w", encoding="utf-8").write(r)
        texto_epica = re.sub(r"(\| \[HU-%03d\]\([^)]*\) \| )«Título» \| «Prioridad» \| «Estimación» \| «…» \| «…» \|" % i,
                             lambda m: m.group(1) + "%s | Must | %s | No aplica | Pendiente |" % (tit, est), texto_epica)
    open(epica, "w", encoding="utf-8").write(texto_epica)
    print("marcadores que quedan en la épica:", texto_epica.count("«Título»"))


if __name__ == "__main__":
    main()
