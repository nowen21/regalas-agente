# -*- coding: utf-8 -*-
import sys, os, glob
SP = r"C:/Users/user/AppData/Local/Temp/claude/c--Ing--Jose-ia-agente/563dc2f9-c782-46f9-af82-c9bc948b3566/scratchpad"
sys.path.insert(0, SP)
import fase_docs
os.chdir(r"c:\Ing. Jose\ia\agente")

C = glob.glob("documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-001-transcripcion-de-la-sesion/*-el-historico-se-busca-por-tema")[0].replace("\\", "/")
A = "../../../../../"
fase_docs.fase(C, dict(
 hu_id="HU-001 Transcripción de la sesión", hu_rel="../HU-001-transcripcion-de-la-sesion.md",
 ep_id="EP-005 Automatismos que no dependen de la memoria",
 modulo="Histórico de sesiones, sus índices",
 origen="✨ **Funcionalidad nueva.** El histórico tenía índice por fecha y nombre; este agrega el que faltaba, por tema.",
 de_donde=f"el punto 8 del [pendiente 33]({A}pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md), anotado el 2026-08-14: «una sesión trata varios temas y por el título no se encuentran»",
 ca="el criterio de la historia sobre que la próxima sesión encuentre lo que la anterior dejó.",
 objetivo="poder buscar en el histórico **por tema** y no solo por fecha o por título de sesión.",
 contexto="""**El problema estaba medido:** la sesión del 2026-08-21 tocó siete asuntos distintos, y su nombre solo dice uno. Con 59 resúmenes, encontrar «dónde se decidió esto» era abrir uno por uno.

**Los temas ya estaban escritos.** Cada resumen abre sus hallazgos con `### H-N · lo que pasó`, y ese título **es** el tema. No hizo falta inventar una clasificación ni pedirle a nadie que etiquete nada: se recogen los 345 que ya existían.

**Generado, no escrito a mano**, porque este índice crece en cada sesión: escrito a mano envejecería más rápido que cualquier otro mapa del repositorio.""",
 fuera="""- **Agrupar temas parecidos.** Decidir que dos hallazgos hablan de lo mismo es leer; el índice junta, no clasifica.
- **Generarlo solo en cada sesión.** Hoy se corre a mano o al cerrar; enganchar el disparo es otra fase, y por [`20·M19`]({A}base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md) primero conviene ver si el índice se usa.
- **Indexar la transcripción.** Es la conversación entera; lo que dice qué dejó cada sesión son los resúmenes.""".replace("{A}", A),
 linea_base="""| Qué se verificó | Resultado |
|---|---|
| ¿Cuántos resúmenes hay? | **59**, del 2026-08-06 al 2026-08-22 |
| ¿Cuántos hallazgos escritos? | **345** |
| ¿Cuántos resúmenes no dejaron ninguno? | **6**, y eso también es un dato |
| ¿Qué forma tienen? | `### H-N · tema`, uniforme en los 59 |""",
 trece="""| # | Respuesta |
|---|---|
| 1-3 | Un índice temático generado del histórico; lo usa quien busca por qué se decidió algo |
| 4-5 | §1; fuera quedan agrupar temas y enganchar el disparo |
| 6-8 | No hay datos ni interfaz: lee `.md` y escribe uno |
| 9 | §2.1 |
| 10 | `python validadores/validar.py temas --aplicar`, y el archivo queda junto a los resúmenes |
| 11 | No aplica porque escribe un solo archivo del propio repositorio |
| 12 | No aplica porque no cambia ninguna norma |
| 13 | [plan_pruebas.md](plan_pruebas.md) |""",
 archivos=f"""| Archivo | Qué se hace |
|---|---|
| [`validadores/temas.py`]({A}validadores/temas.py) | Nuevo: recoge los hallazgos, genera el índice y dice si quedó atrás |
| [`validadores/validar.py`]({A}validadores/validar.py) | Gana el subcomando `temas`, con `--aplicar` |
| [`validadores/tests/test_el_historico_se_busca_por_tema.py`]({A}validadores/tests/test_el_historico_se_busca_por_tema.py) | Nuevo: siete casos |
| [`historico-chat/resumenes/indice-tematico.md`]({A}historico-chat/resumenes/indice-tematico.md) | Nuevo: generado, 345 hallazgos |
| `CHANGELOG.md`, `VERSION` | La entrada y la subida de versión |""",
 dudas="**Ninguna abierta.** Que fuera generado y no a mano lo decidió el pendiente 33 con su evidencia.",
 tareas="""| # | Tarea | Estado |
|---|---|---|
| T-01 | Escribir `temas.py`: recoger, generar, y decir si quedó atrás | ☑ |
| T-02 | Enchufarlo como subcomando con `--aplicar` | ☑ |
| T-03 | Escribir los siete casos, con el de la generación estable | ☑ |
| T-04 | Generar el índice del repositorio | ☑ |
| T-05 | Correr todo y versionar | ☑ |""",
 riesgos="""| # | Riesgo | Cómo se ataca |
|---|---|---|
| B-01 | Que el archivo cambie en cada corrida y ensucie el control de versiones | `CP-05`: generar dos veces sobre lo mismo da un archivo idéntico |
| B-02 | Que detenga una corrida por estar desactualizado | Es **aviso**, nunca falla: un índice atrasado informa mal, no rompe nada |
| B-03 | Que alguien lo edite a mano y pierda su trabajo | La cabecera del propio archivo lo dice: se genera, y el próximo generado pisa lo escrito |""",
 que_se_prueba="""**Se prueba** que recoge todos los hallazgos, que cada uno enlaza a su resumen, que un resumen sin hallazgos no ensucia el índice, que generar dos veces da lo mismo y que avisa sin detener.

**No se prueba** que los temas estén bien redactados: son los títulos que cada sesión escribió, y se copian tal cual.""",
 alcance="La fase toca `validadores/` y `historico-chat/resumenes/`. Se corren la prueba nueva, la suite entera y la comprobación del estándar.",
 trazabilidad="""| CA | Caso | Tipo |
|---|---|---|
| CA · lo que la sesión dejó se encuentra | CP-01, CP-02 | automática |
| CA · el índice no miente sobre lo que hay | CP-03, CP-04, CP-06 | automática |
| transversal · generación estable | CP-05 | automática |
| transversal · sin resúmenes no revienta | CP-07 | automática |
| transversal · no regresión | CP-08 | automática |""",
 casos="""### CP-01 a CP-07 · Los siete casos del programa

```
python validadores/tests/test_el_historico_se_busca_por_tema.py
```

**Esperado:** los siete pasan. **`CP-05` es el que decide:** generado dos veces sobre lo mismo, el archivo sale idéntico.

### CP-08 · Nada de lo que ya estaba se rompe

```
python validadores/validar.py suite
python validadores/validar.py estandar
```

**Esperado:** las dos sin incumplimientos.""",
 veredicto="Cumple**, ciclo 1. Ocho casos de ocho.", veredicto_corto="Cumple", version="31.4.0",
 resultados="""| Caso | Resultado | Veredicto |
|---|---|---|
| CP-01 a CP-07 | `Ran 7 tests ... OK` | ✅ |
| CP-08 · no regresión | `suite` y `estandar` sin incumplimientos | ✅ |

**Y la corrida real, que es la que dice si sirve:**

```
$ python validadores/validar.py temas --aplicar
escrito historico-chat/resumenes/indice-tematico.md
Resúmenes: 59 · hallazgos indexados: 345 · resúmenes sin ningún hallazgo: 6
```""",
 costo="**Nada.** Salió a la primera, porque los resúmenes ya escribían sus hallazgos con la misma forma; si cada sesión los hubiera titulado a su manera, esto habría sido un trabajo de leer.",
 no_probado="""**Que el índice sirva para encontrar lo que uno busca.** Eso se sabe usándolo: 345 líneas se recorren con una búsqueda de texto, pero si aparece que hace falta agrupar por tema, es otra fase.""",
 quedo="**El histórico se puede buscar por tema:** los 345 hallazgos de los 59 resúmenes, en un archivo, cada uno enlazado a donde vive.",
 trazabilidad_final=f"""| Ítem de la especificación | Categoría | Ubicación esperada | Estado | Evidencia |
|---|---|---|---|---|
| Los temas de todas las sesiones en un solo sitio | doc | `historico-chat/resumenes/indice-tematico.md` | ✅ | 345 hallazgos, 59 resúmenes |
| Cada tema enlaza a su resumen | prueba | `temas.py` | ✅ | `CP-02` |
| Se regenera en una línea | doc | `validar.py temas --aplicar` | ✅ | subcomando con su ayuda |
| Avisa cuando queda atrás, sin detener | prueba | `temas.py` | ✅ | `CP-06` |
| El cambio queda versionado | doc | `CHANGELOG.md`, `VERSION` | ✅ | v31.4.0 |""",
 cambia="**Nada obligatorio.** El índice es de este repositorio; un proyecto que herede puede generar el suyo con el mismo subcomando, porque lee la estructura de resúmenes que el estándar ya instala.",
 abierto="""**El disparo sigue siendo a mano.** Nadie lo regenera solo al cerrar la sesión; el aviso dice cuándo quedó atrás, que es el paso previo a automatizarlo según `20·M19`.

**Y seis resúmenes no tienen ningún hallazgo escrito.** El índice lo dice en su recuento; si es que esas sesiones no dejaron nada o que nadie lo escribió, es una pregunta para quien las revise.""",
 n_tareas=5,
 saber="""**El índice se genera, no se escribe.** Si aparece desactualizado, `validar.py temas --aplicar` y listo; editarlo a mano es trabajo perdido, y su propia cabecera lo advierte.""",
 resumen="""**El histórico ya se puede buscar por tema.** Una sesión trata varios asuntos y su nombre solo dice uno; con 59 resúmenes, encontrar dónde se decidió algo era abrirlos uno por uno. Los temas ya estaban escritos en los hallazgos de cada resumen, así que se recogen: **345 hallazgos en un archivo**, cada uno enlazado a donde vive. Nace [`validadores/temas.py`](""" + A + """validadores/temas.py), el subcomando `validar.py temas` y siete casos de prueba.""",
))
print("ok")
