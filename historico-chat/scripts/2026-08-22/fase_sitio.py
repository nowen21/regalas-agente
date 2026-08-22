# -*- coding: utf-8 -*-
import sys, os
SP = r"C:/Users/user/AppData/Local/Temp/claude/c--Ing--Jose-ia-agente/563dc2f9-c782-46f9-af82-c9bc948b3566/scratchpad"
sys.path.insert(0, SP)
import fase_docs
os.chdir(r"c:\Ing. Jose\ia\agente")

C = "documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-011-donde-termina-el-estandar/B-EP-005-HU-011-el-mapa-del-sitio-tampoco-envejece"
A = "../../../../../"
fase_docs.fase(C, dict(
 hu_id="HU-011 Dónde termina el estándar", hu_rel="../HU-011-donde-termina-el-estandar.md",
 ep_id="EP-005 Automatismos que no dependen de la memoria",
 modulo="Comprobaciones del repositorio, los mapas de `anatomia/`",
 origen="📝 **Modifica la fase `A`**, que hizo lo mismo con el otro mapa de `anatomia/`: el del amarre a la herramienta. Este cubre el que faltaba.",
 de_donde=f"el punto 8 del [pendiente 33]({A}pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md), donde quedó preguntado si el mapa del sitio se comprueba o se actualiza a mano",
 ca="el `CA-03` de la historia, que pide que lo escrito sobre la anatomía del repositorio no envejezca en silencio.",
 objetivo="que una carpeta nueva del repositorio no pueda quedarse fuera del mapa del sitio sin que nadie se entere.",
 contexto="""**La decisión era mano o programa, y se eligió programa** por lo que ya había pasado con el otro mapa: `anatomia/` estuvo fuera de la tabla del `CLAUDE.md` hasta el 2026-08-18, y nadie lo notó porque un mapa desactualizado **se lee igual de bien**; simplemente miente por omisión.

**Y la primera corrida lo confirmó:** cuatro carpetas existían sin estar en el mapa (`adaptadores/`, `analisis/`, `documentacion/`, `evals/`) y una que el mapa nombraba ya no existe (`diplomado-ia/`). El mapa decía que el repositorio tenía doce carpetas y tiene dieciséis.""",
 fuera="""- **Comprobar que la descripción sea la acertada**, o que la carpeta esté en la zona correcta. Eso es un juicio y se lee; acá se comprueba que **esté nombrada**.
- **El segundo nivel del árbol.** Una carpeta nueva dentro de `base/` la reportan los índices de capítulo, que ya existen.
- **Los archivos sueltos de la raíz.** Un archivo nuevo en la raíz es raro y se ve; una carpeta nueva se pierde.""",
 linea_base="""| Qué se verificó | Resultado |
|---|---|
| ¿Había un precedente construido? | **Sí:** [`amarre.py`](" + A + "validadores/amarre.py) hace exactamente esto con el mapa del amarre, y se reusa su forma: dos lados, falla y aviso |
| ¿Cuántas carpetas tiene el repositorio? | **16** de primer nivel, sin contar lo local y lo generado |
| ¿Cuántas nombraba el mapa? | **12.** Faltaban cuatro y sobraba una |
| ¿Qué queda fuera por diseño? | `.git`, `.venv`, `__pycache__`, `terceros`, `node_modules` y demás: no viajan ni se versionan |""".replace('" + A + "', A),
 trece="""| # | Respuesta |
|---|---|
| 1-3 | Una comprobación que mantiene honesto el mapa del sitio; la usa quien mantiene el estándar |
| 4-5 | §1; fuera quedan la calidad de la descripción y el segundo nivel |
| 6-8 | No hay datos ni interfaz: lee carpetas y un `.md` |
| 9 | §2.1 |
| 10 | `python validadores/validar.py sitio`, y en la ayuda del programa |
| 11 | No aplica porque solo lee |
| 12 | No aplica porque no cambia ninguna norma |
| 13 | [plan_pruebas.md](plan_pruebas.md) |""",
 archivos=f"""| Archivo | Qué se hace |
|---|---|
| [`validadores/sitio.py`]({A}validadores/sitio.py) | Nuevo: las dos formas de envejecer del mapa, más el recuento |
| [`validadores/validar.py`]({A}validadores/validar.py) | Gana el subcomando `sitio` |
| [`validadores/tests/test_el_mapa_del_sitio_no_envejece.py`]({A}validadores/tests/test_el_mapa_del_sitio_no_envejece.py) | Nuevo: siete casos |
| [`anatomia/mapa-del-sitio.md`]({A}anatomia/mapa-del-sitio.md) | Se pone al día con lo que la primera corrida encontró |
| `CHANGELOG.md`, `VERSION` | La entrada y la subida de versión |""",
 dudas="**Ninguna abierta.** La única que había, mano o programa, la resolvió el pendiente 33 con su evidencia.",
 tareas="""| # | Tarea | Estado |
|---|---|---|
| T-01 | Escribir `sitio.py` con los dos lados y el recuento | ☑ |
| T-02 | Enchufarlo como subcomando de `validar.py` | ☑ |
| T-03 | Escribir los siete casos de prueba | ☑ |
| T-04 | Poner al día el mapa con lo que la primera corrida encontró | ☑ |
| T-05 | Correr todo y versionar | ☑ |""",
 riesgos="""| # | Riesgo | Cómo se ataca |
|---|---|---|
| B-01 | Que reporte siempre y termine apagado | El caso `CP-04` exige que, nombrada la carpeta, se calle. Es el caso que decide |
| B-02 | Que confunda una carpeta local con una del estándar | La lista de lo que queda fuera se escribe una por una, no por patrón ancho |
| B-03 | Que un nombre parecido cuente por la carpeta real | `CP-07`: `mis-plantillas/` no cuenta como `plantillas/` |""",
 que_se_prueba="""**Se prueba** que reporta la carpeta que falta, que avisa de la que sobra, que se calla cuando el mapa está bien, y que no confunde lo local con lo del estándar.

**No se prueba** que la descripción del mapa sea buena: eso lo lee una persona.""",
 alcance="La fase toca `validadores/` y `anatomia/`. Se corre la prueba nueva, la suite completa y la comprobación del estándar; no se corren las de la interfaz.",
 trazabilidad="""| CA | Caso | Tipo |
|---|---|---|
| CA-03 · lo escrito sobre la anatomía no envejece | CP-01, CP-02, CP-03 | automática |
| CA-03 · la comprobación sirve, o sea que se calla | CP-04, CP-05, CP-07 | automática |
| transversal · se puede mirar sin abrir el mapa | CP-06 | automática |
| transversal · no regresión | CP-08 | automática |""",
 casos="""### CP-01 a CP-07 · Los siete casos del programa

```
python validadores/tests/test_el_mapa_del_sitio_no_envejece.py
```

**Esperado:** los siete pasan. `CP-01` la carpeta que falta es falla; `CP-02` sin mapa es falla; `CP-03` la carpeta que ya no existe es aviso, no falla; **`CP-04` nombrada la carpeta, se calla**; `CP-05` lo local y lo generado no cuentan; `CP-06` el recuento se lee sin abrir el mapa; `CP-07` un nombre parecido no cuenta por la carpeta real.

### CP-08 · Nada de lo que ya estaba se rompe

```
python validadores/validar.py suite
python validadores/validar.py estandar
```

**Esperado:** las dos sin incumplimientos.""",
 veredicto="Cumple**, ciclo 1. Ocho casos de ocho, y el programa encontró cinco defectos reales en su primera corrida.",
 veredicto_corto="Cumple", version="31.2.0",
 resultados="""| Caso | Resultado | Veredicto |
|---|---|---|
| CP-01 a CP-07 | `Ran 7 tests ... OK` | ✅ |
| CP-08 · no regresión | `suite` y `estandar` sin incumplimientos | ✅ |

**Y la corrida contra el repositorio real, que es la prueba de que sirve:**

```
$ python validadores/validar.py sitio      (antes de poner al día el mapa)
4 falla(s), 1 aviso(s).
Carpetas de primer nivel: 16 · nombradas en el mapa: 12 · sin nombrar: 4

$ python validadores/validar.py sitio      (después)
OK: sin incumplimientos.
Carpetas de primer nivel: 16 · nombradas en el mapa: 16 · sin nombrar: 0
```""",
 costo="""**Nada que corregir, pero sí una decisión al escribirlo:** cómo reconocer que una carpeta está nombrada. Buscar el nombre suelto daba falsos aciertos (la palabra «base» sale en cada párrafo), así que se busca `nombre/`, con la barra, que es como el mapa las escribe. `CP-07` protege esa decisión.""",
 no_probado="""**Que la descripción sea la acertada ni que la zona esté bien elegida.** Que `evals/` sea herramienta y no bitácora es un juicio; el programa comprueba que esté, no dónde.""",
 quedo="**El mapa del sitio ya no puede envejecer en silencio:** `validar.py sitio` reporta la carpeta que existe y no está, y avisa de la que está y ya no existe.",
 trazabilidad_final=f"""| Ítem de la especificación | Categoría | Ubicación esperada | Estado | Evidencia |
|---|---|---|---|---|
| La carpeta que existe y el mapa no nombra se reporta | prueba | `validadores/sitio.py` | ✅ | `CP-01`, y cuatro casos reales encontrados |
| La carpeta que el mapa nombra y ya no existe se avisa | prueba | el mismo | ✅ | `CP-03`, y `diplomado-ia/` encontrada |
| La comprobación se calla cuando está bien | prueba | el mismo | ✅ | `CP-04` |
| Se puede correr en una línea | doc | `validar.py sitio` | ✅ | subcomando con su ayuda |
| El mapa quedó al día | doc | `anatomia/mapa-del-sitio.md` | ✅ | 16 de 16 carpetas nombradas |
| El cambio queda versionado | doc | `CHANGELOG.md`, `VERSION` | ✅ | v31.2.0 |""",
 cambia="**Nada.** El mapa del sitio es de este repositorio, no de los proyectos que heredan: `anatomia/` no viaja. Lo que un proyecto sí gana es el precedente, por si quiere comprobar sus propios mapas.",
 abierto="""**El segundo nivel sigue sin comprobarse.** Una carpeta nueva dentro de `plantillas/` o de `documentacion/` no la ve nadie. Se dejó fuera a propósito, porque el ruido de reportar cada subcarpeta apagaría la comprobación; si con el uso aparece que ahí también se pierde algo, es una fase más de esta historia.""",
 n_tareas=5,
 saber="""**El mapa ya se comprueba, así que no hace falta releerlo entero.** Si `validar.py sitio` está en verde, el mapa nombra todo lo que existe. Lo que sigue sin comprobarse es si la descripción de cada carpeta es la acertada, y eso se lee.""",
 resumen="""**El mapa del sitio ya no envejece en silencio.** Se decidió comprobarlo con un programa en vez de actualizarlo a mano, y la primera corrida encontró cuatro carpetas que existían sin estar en el mapa y una que el mapa nombraba y ya no existe: decía doce y son dieciséis. Nace [`validadores/sitio.py`](""" + A + """validadores/sitio.py), el subcomando `validar.py sitio` y siete casos de prueba.""",
))
print("ok")
