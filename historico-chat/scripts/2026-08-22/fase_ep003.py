# -*- coding: utf-8 -*-
import sys, os
SP = r"C:/Users/user/AppData/Local/Temp/claude/c--Ing--Jose-ia-agente/563dc2f9-c782-46f9-af82-c9bc948b3566/scratchpad"
sys.path.insert(0, SP)
import fase_docs, p19lib as L
os.chdir(r"c:\Ing. Jose\ia\agente")

C = "documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-002-modelos-del-encargo/B-EP-003-HU-002-la-historia-declara-que-criterio-depende-de-cual"
A = "../../../../../"
fase_docs.fase(C, dict(
 hu_id="HU-002 Modelos del encargo", hu_rel="../HU-002-modelos-del-encargo.md",
 ep_id="EP-003 Documentos modelo y procedimientos",
 modulo="Moldes del ciclo de vida, el de la historia de usuario",
 origen="📝 **Modifica la fase `A`**, que retrodocumentó los moldes del encargo: este agrega al de la historia una columna que no tenía.",
 de_donde=f"el punto 8 del [pendiente 33]({A}pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md), abierto desde el 2026-08-07",
 ca="el `CA-01` de la historia, que pide que los moldes del encargo digan lo que hay que llenar.",
 objetivo="que una historia pueda decir **qué criterio no se puede comprobar mientras otro no esté cumplido**, sin inventar una sección nueva.",
 contexto="""**El hueco, medido el 2026-08-07:** la tabla de fases de la plantilla dice qué CA cubre cada fase, pero no si un CA depende de otro. Sin eso, dos fases se ordenan al revés y el error aparece al probar, cuando ya se construyó.

**Por qué columna y no sección.** Una sección nueva la paga toda historia, incluidas las que no tienen ninguna dependencia. Una columna vacía no cuesta nada de llenar y se ve de un vistazo junto a la fase que le importa.""",
 fuera="""- **Comprobar la dependencia con un programa.** Que el orden declarado sea el correcto exige leer los dos criterios; por [`20·M19`]({A}base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md), primero tiene que cumplirse a mano.
- **Rellenar la columna en las 101 historias ya escritas.** La columna se llena cuando la historia se toca; ninguna queda mal por tenerla vacía.""".replace("{A}", A),
 linea_base="""| Qué se verificó | Resultado |
|---|---|
| ¿La plantilla ya tenía dónde decirlo? | **No.** Su §8 tiene fase, CA que cubre, los tres enlaces y el estado |
| ¿Alguna regla lo exige? | **No**, y no se agrega ninguna: la columna es del molde, no una exigencia nueva |
| ¿Rompe las historias ya escritas? | **No.** Una tabla con una columna menos sigue siendo válida; se completa al tocarla |""",
 trece="""| # | Respuesta |
|---|---|
| 1-3 | Una columna en el molde de la historia, para declarar dependencia entre criterios; la usa cualquier proyecto que herede las plantillas |
| 4-5 | §1; fuera quedan el validador y el relleno hacia atrás |
| 6-8 | No hay datos ni interfaz: el entregable es un molde |
| 9 | §2.1 |
| 10 | En `plantillas/ciclo-vida-proyectos/`, que el instalador copia |
| 11 | No aplica porque no hay ejecución ni permisos |
| 12 | No aplica porque nada obliga a migrar: la columna vacía es válida |
| 13 | [plan_pruebas.md](plan_pruebas.md) |""",
 archivos=f"""| Archivo | Qué se hace |
|---|---|
| [`plantillas/ciclo-vida-proyectos/04-HU.md`]({A}plantillas/ciclo-vida-proyectos/04-HU.md) | La tabla de §8 gana la columna «Depende de», con una fila de ejemplo que la usa y la frase que dice cómo se llena |
| `CHANGELOG.md`, `VERSION` | La entrada y la subida de versión |""",
 dudas="**Ninguna abierta.** La única que había, si entraba a la plantilla, la decidió el usuario al ordenar resolver el pendiente 33.",
 tareas="""| # | Tarea | Estado |
|---|---|---|
| T-01 | Agregar la columna a la tabla de §8, con su fila de ejemplo | ☑ |
| T-02 | Escribir cómo se llena: con criterios, no con fases, y vacía si no hay dependencia | ☑ |
| T-03 | Correr las pruebas y versionar | ☑ |""",
 riesgos="""| # | Riesgo | Cómo se ataca |
|---|---|---|
| B-01 | Que se llene con fases en vez de criterios, que es lo que ya dice la primera columna | La frase de abajo lo dice con esas palabras, y la fila de ejemplo muestra un CA, no una fase |
| B-02 | Que se vuelva obligatoria de hecho y llene de ruido las historias simples | Queda escrito que vacía es correcto |""",
 que_se_prueba="""**Se prueba** que el molde sigue siendo válido y que la columna se entiende sin explicación aparte.

**No se prueba** que las dependencias declaradas sean las correctas: eso exige leer los dos criterios y es de quien escribe la historia.""",
 alcance="La fase toca un archivo de `plantillas/`. Se corre la comprobación del estándar y la del texto heredable; no se corren las suites de la interfaz ni las de los validadores, que esta fase no toca.",
 trazabilidad="""| CA | Caso | Tipo |
|---|---|---|
| CA-01 · el molde dice lo que hay que llenar | CP-01, CP-02 | manual documentada |
| transversal · no regresión | CP-03, CP-04 | automática |""",
 casos=f"""### CP-01 · La columna se entiende sin ir a otro documento

**Cómo se ejecuta:** leer §8 del molde y responder, sin abrir nada más, qué se escribe en «Depende de» y qué se hace si no hay dependencia.

**Esperado:** las dos respuestas están en la frase que sigue a la tabla: se escriben criterios, no fases, y si no hay dependencia queda vacía.

### CP-02 · Una historia sin dependencias no paga nada

**Cómo se ejecuta:** tomar una historia real con criterios independientes (por ejemplo [HU-002 de esta épica]({A}documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-002-modelos-del-encargo/HU-002-modelos-del-encargo.md)) y comprobar que la columna vacía no la deja incompleta.

**Esperado:** la tabla se lee igual; ningún validador la reporta.

### CP-03 · El estándar sigue coherente

```
python validadores/validar.py estandar
```

**Esperado:** sin incumplimientos.

### CP-04 · El molde no gana marcas de generación automática

```
python validadores/validar.py marcas --preparados
```

**Esperado:** sin fallas: `plantillas/` es texto que viaja a los proyectos.""",
 veredicto="Cumple**, ciclo 1. Cuatro casos de cuatro.", veredicto_corto="Cumple", version="31.1.0",
 resultados="""| Caso | Resultado | Veredicto |
|---|---|---|
| CP-01 · se entiende sin ir a otro lado | la frase contesta las dos preguntas | ✅ |
| CP-02 · la historia sin dependencias no paga | columna vacía, tabla válida, ningún validador la reporta | ✅ |
| CP-03 · el estándar sigue coherente | `validar.py estandar`: sin incumplimientos | ✅ |
| CP-04 · sin marcas | `validar.py marcas --preparados`: cero fallas | ✅ |""",
 costo="**Nada.** Es el cambio más barato de los cuatro que dejó abierto el pendiente 33, y salió a la primera.",
 no_probado="**Que la dependencia declarada sea la correcta.** Ningún programa puede decidir si un criterio depende de otro; lo decide quien escribe la historia, y por eso la columna no tiene validador.",
 quedo="**Una historia puede decir qué criterio depende de cuál**, en la misma tabla donde ya dice qué fase cubre cada uno.",
 trazabilidad_final=f"""| Ítem de la especificación | Categoría | Ubicación esperada | Estado | Evidencia |
|---|---|---|---|---|
| La tabla de fases admite declarar dependencia entre criterios | doc | `plantillas/ciclo-vida-proyectos/04-HU.md` | ✅ | columna «Depende de» y su fila de ejemplo |
| Queda escrito cómo se llena | doc | el mismo archivo | ✅ | la frase que sigue a la tabla: criterios, no fases; vacía si no hay |
| El cambio queda versionado | doc | `CHANGELOG.md`, `VERSION` | ✅ | v31.1.0 |""",
 cambia="**Nada que hacer.** La columna es aditiva y vacía es correcta. Una historia nueva la trae; una vieja la gana cuando alguien la toque.",
 abierto="**Sin validador, a propósito.** Si con el uso aparece que la columna se llena mal (con fases en vez de criterios), eso sí se puede contar y entonces valdría automatizarlo, según [`20·M19`](" + A + "base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md).",
 n_tareas=3,
 saber="**La columna es opcional y vacía es correcta.** No hay que rellenarla en las historias ya escritas; se llena cuando la historia se toque y tenga una dependencia real.",
 resumen="**Una historia ya puede decir qué criterio depende de cuál.** La tabla de fases decía qué CA cubre cada fase, pero no si un CA no se puede comprobar mientras otro no esté cumplido; sin eso, dos fases se ordenan al revés y se descubre al probar. Se resolvió con una columna, no con una sección: la historia sin dependencias la deja vacía y no paga nada.",
))
print("ok")
