# -*- coding: utf-8 -*-
import sys, os
SP = r"C:/Users/user/AppData/Local/Temp/claude/c--Ing--Jose-ia-agente/563dc2f9-c782-46f9-af82-c9bc948b3566/scratchpad"
sys.path.insert(0, SP)
import fase_docs
os.chdir(r"c:\Ing. Jose\ia\agente")

C = "documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-005-no-pisar-lo-escrito/B-EP-007-HU-005-el-readme-heredado-recibe-lo-que-la-plantilla-suma"
A = "../../../../../"
fase_docs.fase(C, dict(
 hu_id="HU-005 No pisar lo escrito", hu_rel="../HU-005-no-pisar-lo-escrito.md",
 ep_id="EP-007 Instalación y actualización",
 modulo="Instalador del estándar, los documentos heredados",
 origen="📝 **Modifica la fase `A`**, que retrodocumentó el «no pisar lo escrito»: esta agrega la otra mitad, que es completar sin pisar.",
 de_donde=f"el punto 8 del [pendiente 33]({A}pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md), donde estaba dicho así: «el mecanismo replica y el texto que lo explica no»",
 ca="el `CA-01` de la historia, que pide que instalar sobre algo escrito no borre nada.",
 objetivo="que el `README` heredado del histórico reciba lo que la plantilla del estándar haya sumado, sin pisar una línea de lo que el proyecto escribió.",
 contexto="""**El defecto era asimétrico y por eso costaba verlo.** El `CLAUDE.md` de cada proyecto sí recibía las secciones nuevas del estándar, con un mecanismo aditivo que ya existía desde `01·C18`; el `README.md` del histórico, no: si ya existía, el instalador solo le refrescaba el sello.

**La consecuencia:** un proyecto instalado en julio se quedaba con el texto de julio para siempre. Y no se notaba, porque el archivo existe, se lee bien y dice cosas ciertas; solo que dice **menos** de lo que el estándar ya sabe.

**No hubo que inventar el mecanismo:** `_completar_secciones` ya estaba escrito y probado para el `CLAUDE.md`. Lo que faltaba era usarlo en el otro archivo.""",
 fuera="""- **Los demás documentos heredados** (`.agente/`, el índice de la memoria). Se completan si aparece la misma necesidad; hoy no hay evidencia de que se haya perdido nada por ahí.
- **Reordenar o corregir** lo que el proyecto escribió. Aditivo significa que se agrega al final y nada más.""",
 linea_base="""| Qué se verificó | Resultado |
|---|---|
| ¿Existía el mecanismo? | **Sí**, `_completar_secciones`, usado por `instalar_claude_md` desde `01·C18` |
| ¿Qué hacía el instalador con el README del histórico? | Si existía, **solo refrescaba el sello**; el texto se quedaba como estaba |
| ¿Cómo reconoce una sección? | Por su encabezado `##` o menor; el `#` del título no cuenta, porque lleva el nombre del proyecto y nunca coincide |""",
 trece="""| # | Respuesta |
|---|---|
| 1-3 | Que el instalador complete el README heredado; lo usa cualquier proyecto instalado |
| 4-5 | §1; fuera quedan los demás heredados y cualquier reescritura |
| 6-8 | No hay datos ni interfaz: es un archivo de texto del proyecto |
| 9 | §2.1 |
| 10 | Corre solo al instalar o reinstalar; no hay que pedirlo |
| 11 | No aplica porque escribe en el proyecto donde se corre, con la autorización de correr el instalador |
| 12 | No aplica porque nada obliga: el proyecto recibe lo nuevo la próxima vez que instale |
| 13 | [plan_pruebas.md](plan_pruebas.md) |""",
 archivos=f"""| Archivo | Qué se hace |
|---|---|
| [`validadores/instalar.py`]({A}validadores/instalar.py) | `instalar_historico` completa el README con lo que la plantilla sumó, y lo reporta |
| [`validadores/tests/test_instalar_agrega_al_readme_heredado.py`]({A}validadores/tests/test_instalar_agrega_al_readme_heredado.py) | Nuevo: seis casos |
| [`plantillas/historico-chat.md`]({A}plantillas/historico-chat.md) | Gana la sección que contesta qué manda cuando el histórico y lo acordado se contradicen |
| `CHANGELOG.md`, `VERSION` | La entrada y la subida de versión |""",
 dudas="**Ninguna abierta.** La decisión de hacerlo igual que con el `CLAUDE.md` salió del propio pendiente 33.",
 tareas="""| # | Tarea | Estado |
|---|---|---|
| T-01 | Usar el mecanismo aditivo en `instalar_historico` y reportar qué agregó | ☑ |
| T-02 | Escribir los seis casos de prueba, con el que protege lo escrito por el proyecto | ☑ |
| T-03 | Escribir en la plantilla qué manda cuando el histórico y lo acordado se contradicen | ☑ |
| T-04 | Correr todo y versionar | ☑ |""",
 riesgos="""| # | Riesgo | Cómo se ataca |
|---|---|---|
| B-01 | Que al completar se pise lo del proyecto | `CP-02` es el caso que decide: lo escrito por el proyecto sigue ahí, palabra por palabra |
| B-02 | Que reescriba en cada corrida y ensucie el control de versiones | `CP-03`: sin novedad, el archivo queda byte por byte igual |
| B-03 | Que agregue el título sin su texto | `CP-04`: la sección llega con su cuerpo |""",
 que_se_prueba="""**Se prueba** que la sección nueva llega, que lo del proyecto sobrevive, que sin novedad no se toca nada, y que el sello queda al día.

**No se prueba** contra un proyecto real en esta corrida: las pruebas arman un estándar de mentira en carpeta temporal, porque editar la plantilla de verdad para probar sería tocar el estándar ([`00·N4`](""" + A + """base/00-nucleo-blindado.md)).""",
 alcance="La fase toca `validadores/instalar.py` y `plantillas/`. Se corre la prueba nueva, la suite entera y la comprobación del estándar.",
 trazabilidad="""| CA | Caso | Tipo |
|---|---|---|
| CA-01 · instalar no borra lo escrito | CP-02 | automática |
| CA-01 · lo que el estándar suma llega | CP-01, CP-04, CP-06 | automática |
| transversal · sin novedad no se toca nada | CP-03 | automática |
| transversal · el sello queda al día | CP-05 | automática |
| transversal · no regresión | CP-07 | automática |""",
 casos="""### CP-01 a CP-06 · Los seis casos del instalador

```
python validadores/tests/test_instalar_agrega_al_readme_heredado.py
```

**Esperado:** los seis pasan. **`CP-02` es el que decide**: se instala, el proyecto escribe su propia sección, la plantilla del estándar gana otra, se reinstala, y lo del proyecto sigue palabra por palabra.

### CP-07 · Nada de lo que ya estaba se rompe

```
python validadores/validar.py suite
python validadores/validar.py estandar
```

**Esperado:** las dos sin incumplimientos. Importa porque `instalar.py` lo tocan seis fases distintas.""",
 veredicto="Cumple**, ciclo 1. Siete casos de siete.", veredicto_corto="Cumple", version="31.3.0",
 resultados="""| Caso | Resultado | Veredicto |
|---|---|---|
| CP-01 · la sección nueva llega al proyecto ya instalado | reportada y escrita, con su texto | ✅ |
| CP-02 · lo que el proyecto escribió sigue ahí | palabra por palabra | ✅ |
| CP-03 · sin novedad no reescribe | el archivo queda idéntico | ✅ |
| CP-04 · la sección llega con su cuerpo | más de una línea bajo el título | ✅ |
| CP-05 · el sello queda al día | la huella se reescribe contra la plantilla | ✅ |
| CP-06 · si no existe, se crea entero | `crear historico-chat/README.md` | ✅ |
| CP-07 · no regresión | `suite` y `estandar` sin incumplimientos | ✅ |""",
 costo="""**Un caso falló en la primera corrida, y el fallo era de la prueba, no del código.** `CP-05` buscaba en el archivo la palabra del identificador del componente; el sello real se escribe como `<!-- huella: … · estandar X.Y.Z -->`. Se corrigió la prueba para mirar el sello que de verdad se escribe. Es la diferencia entre probar lo que uno cree que hace el programa y probar lo que hace.""",
 no_probado="""**Que corra sobre los proyectos ya instalados.** Eso pasa cuando cada uno vuelva a instalar; lo que esta fase garantiza es que, cuando pase, reciban lo nuevo sin perder lo suyo.""",
 quedo="**El `README` heredado del histórico ya recibe lo que el estándar suma**, sin pisar una línea de lo que el proyecto escribió, y diciendo qué agregó.",
 trazabilidad_final=f"""| Ítem de la especificación | Categoría | Ubicación esperada | Estado | Evidencia |
|---|---|---|---|---|
| El README heredado se completa | código | `validadores/instalar.py` | ✅ | `instalar_historico` usa el mecanismo aditivo y lo reporta |
| Nada de lo escrito se pisa | prueba | el test nuevo | ✅ | `CP-02` |
| Sin novedad no se toca nada | prueba | el mismo | ✅ | `CP-03` |
| Queda escrito qué manda entre el histórico y lo acordado | doc | `plantillas/historico-chat.md` | ✅ | sección nueva, que además viaja por el mecanismo recién construido |
| El cambio queda versionado | doc | `CHANGELOG.md`, `VERSION` | ✅ | v31.3.0 |""",
 cambia="""**Nada que hacer, y algo que se recibe:** la próxima vez que un proyecto corra el instalador, su `historico-chat/README.md` gana las secciones que el estándar haya sumado desde que se instaló, empezando por la que dice qué manda cuando el histórico y lo acordado se contradicen.""",
 abierto="""**Los demás documentos heredados siguen sin completarse.** El índice de la memoria y los archivos de `.agente/` se copian una vez y no reciben secciones nuevas. Se dejó fuera porque no hay evidencia de que se haya perdido nada por ahí; si aparece, es otra fase de esta historia.""",
 n_tareas=4,
 saber="""**El mecanismo aditivo ya está en dos sitios y es el mismo:** `_completar_secciones` de `instalar.py`. Si mañana hay que completar un tercer documento heredado, se reusa; escribir otro sería tener dos formas de hacer lo mismo.""",
 resumen="""**El README heredado ya no se queda viejo.** El `CLAUDE.md` de cada proyecto recibía las secciones nuevas del estándar y el `README.md` del histórico no: quien instaló en julio se quedaba con el texto de julio, y no se notaba porque el archivo existe y dice cosas ciertas, solo que menos. Ahora el instalador lo completa con el mismo mecanismo, sin pisar lo que el proyecto escribió, y lo dice. De paso, la plantilla gana la sección que contesta **qué manda cuando el histórico y lo acordado se contradicen**: manda lo acordado, y el histórico dice de dónde salió.""",
))
print("ok")
