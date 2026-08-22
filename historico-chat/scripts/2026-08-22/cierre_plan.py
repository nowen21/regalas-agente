# -*- coding: utf-8 -*-
import sys, os, io
SP = r"C:/Users/user/AppData/Local/Temp/claude/c--Ing--Jose-ia-agente/563dc2f9-c782-46f9-af82-c9bc948b3566/scratchpad"
sys.path.insert(0, SP)
import cerrar_estado
os.chdir(r"c:\Ing. Jose\ia\agente")

C = "documentacion/epicas/EP-004-comprobacion-automatica/HU-013-comparar-el-plan-con-lo-hecho/A-EP-004-HU-013-comparar-lo-hecho-con-el-plan-aprobado/"
A = "../../../../../"

io.open(C + "resultado_pruebas.md", "w", encoding="utf-8", newline="").write("""# Resultado de Pruebas — Fase A-EP-004-HU-013-comparar-lo-hecho-con-el-plan-aprobado

**Para qué sirve este documento.** Registra qué se ejecutó y con qué resultado. Los casos viven en el [plan_pruebas.md](plan_pruebas.md), que no se toca al ejecutar.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-004-HU-013-comparar-lo-hecho-con-el-plan-aprobado` |
| **HU** | [HU-013 Comparar el plan con lo hecho](../HU-013-comparar-el-plan-con-lo-hecho.md) |
| **Ciclo** | 1 · **Fecha** 2026-08-22 |
| **Ejecutado por** | El agente, por la orden del usuario de resolver el [pendiente 59](""" + A + """pendientes/59-las-42-dudas-que-detienen-26-fases.md) |

### 0.1 Las dos dudas que la detenían

| Duda | Decisión, del pendiente 59 |
|---|---|
| ¿contra qué se comparan los archivos tocados? | **Contra el commit del que salió la fase** (decisión 22): la rama arrastra trabajo ajeno y lo sin guardar cambia mientras se mira |
| ¿el `CA-03` se intenta comprobar o se declara criterio humano? | **Criterio humano** (decisión 10): comparar los pasos ejecutados con los escritos exige leer los dos textos y decidir si dicen lo mismo con otras palabras. Queda declarado en [`reglas-validables.md`](""" + A + """validadores/reglas-validables.md) |

## 1. Resumen

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos |
|---|---:|---:|---:|---:|
| 1 | 4 del plan, 11 escritos | 11 | 11 | 0 |

## 2. Caso por caso

| Caso | Qué comprueba | Resultado |
|---|---|---|
| CP-001 · el archivo tocado y no declarado se avisa; el declarado, no | el corazón del `CA-01` | ✅ Aprobado |
| CP-002 · el formato que no se entiende se avisa, no se supone | tres casos: sin sección, sin plan, sin commit de origen | ✅ Aprobado |
| CP-003 · el criterio sin caso y el plan de pruebas sin casos se avisan | el `CA-02` | ✅ Aprobado, y con el criterio cubierto **se calla** |
| CP-004 · los documentos de la propia fase no cuentan | **el caso que decide** | ✅ Aprobado |
| CP-005 · nunca detiene | un archivo de más puede ser un descubrimiento aprobado | ✅ Aprobado |

## 3. La primera corrida encontró un incumplimiento del propio trabajo de hoy

**Y es el mejor argumento a favor de la herramienta.** Corrida sobre la fase del conteo por regla, cerrada media hora antes:

```
$ python validadores/validar.py plan --fase …/A-EP-004-HU-009-… --desde HEAD~1
[AVISO] validadores/conteo.py — lo tocó la fase y su plan no lo declara
[AVISO] validadores/docs/conteo.md — lo tocó la fase y su plan no lo declara
[AVISO] validadores/tests/test_el_conteo_por_regla.py — lo tocó la fase y su plan no lo declara
```

**Los tres son ciertos.** Ese plan, escrito el 2026-08-17, declaraba tocar `validadores/comun.py`, `validar.py`, `pruebas.py` y dos documentos: daba por hecho que el conteo viviría dentro de `validar.py`. Al construirlo se vio que era mejor un módulo propio, con su contrato y su archivo de pruebas, **y eso amplió el plan sin escribirlo**, que es exactamente lo que [`02·F8`](""" + A + """base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md) prohíbe hacer en silencio.

**Queda dicho acá y no se disimula.** La decisión de separar el módulo fue buena; lo que faltó fue anotarla en el plan antes de ejecutar. Es el primer hallazgo real de este validador y es sobre quien lo escribió.

## 4. Sobre los otros trece avisos del repositorio

La corrida completa sobre las 113 fases con plan deja **13 avisos de criterios sin caso**, casi todos en fases viejas cuyo plan de pruebas nombra los criterios de otra forma. No se corrigieron acá: son de sus propias fases, y arreglarlos de paso sería repetir el defecto que esta misma fase acaba de encontrar.

## 5. Veredicto

**Cumple.** Once casos de once, y el `CA-03` declarado como criterio humano con su motivo escrito.
""")

io.open(C + "funcionalidad_implementada.md", "w", encoding="utf-8", newline="").write("""# Funcionalidad implementada — Fase A-EP-004-HU-013-comparar-lo-hecho-con-el-plan-aprobado

**Para qué sirve este documento.** Dice qué quedó hecho al cerrar la fase, con su trazabilidad.

> **Cerrada el 2026-08-22, con el estándar en la versión 31.11.0.** Es el sello que dice **bajo qué reglas** cerró este trabajo: una regla escrita después no lo reabre ([`20·M10`](""" + A + """base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).

## 0. Qué quedó, en una frase

**Se puede comprobar, con una orden, si una fase tocó los archivos que su plan declaró.**

## 1. Trazabilidad ([`13·DOC11`](""" + A + """base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| Los archivos declarados se leen del plan | código | [`validadores/plan_vs_hecho.py`](""" + A + """validadores/plan_vs_hecho.py) | ✅ | `declarados`, sobre la §2.1 del molde |
| Se comparan contra el commit de origen | código | el mismo | ✅ | `--desde`; sin él, lo dice y no inventa |
| El archivo de más se avisa | código | el mismo | ✅ | y encontró tres del trabajo de hoy |
| Los documentos de la fase no cuentan | código | el mismo | ✅ | `CP-004` |
| El criterio sin caso se avisa | código | `comparar_casos` | ✅ | `CP-003` |
| Nunca detiene | código | el mismo | ✅ | `CP-005` |
| `02·F8` pasa a validador escrito | doc | [`reglas-validables.md`](""" + A + """validadores/reglas-validables.md) | ✅ | con lo que sigue siendo criterio, escrito |
| El `CA-03` queda como criterio humano | doc | el mismo | ✅ | con su motivo |
| El contrato | doc | [`docs/plan_vs_hecho.md`](""" + A + """validadores/docs/plan_vs_hecho.md) | ✅ | qué compara y qué no |
| Los casos | prueba | [`test_el_plan_contra_lo_hecho.py`](""" + A + """validadores/tests/test_el_plan_contra_lo_hecho.py) | ✅ | once |

## 2. Lo que cambia para un proyecto que hereda

**Gana una orden.** Al cerrar una fase, `validar.py plan --fase … --desde …` dice si se tocó algo que el plan no decía. No corre sola en la corrida completa porque necesita el commit de origen, que solo sabe quien abrió la fase.

## 3. Lo que queda abierto

**Trece avisos de criterios sin caso** en fases viejas, cuyos planes de prueba nombran los criterios de otra forma. Son de sus propias fases y no se tocaron: arreglarlos de paso sería repetir el defecto que este mismo validador acaba de encontrar.

**Y el que encontró sobre el trabajo de hoy:** la fase del conteo por regla amplió su plan sin escribirlo. Queda anotado en su [resultado](../../HU-009-conteo-por-regla/A-EP-004-HU-009-el-conteo-de-hallazgos-por-regla/resultado_pruebas.md) y en el de esta.
""")

cerrar_estado.cerrar(C.rstrip("/"), cumplidos="3 de 3",
                     nota_extra="Construida entera, y su primera corrida encontró un incumplimiento del trabajo de la misma jornada.")

# el hallazgo, anotado también en la fase del conteo
p = C.replace("HU-013-comparar-el-plan-con-lo-hecho/A-EP-004-HU-013-comparar-lo-hecho-con-el-plan-aprobado/",
              "HU-009-conteo-por-regla/A-EP-004-HU-009-el-conteo-de-hallazgos-por-regla/") + "resultado_pruebas.md"
s = io.open(p, encoding="utf-8").read()
a = "## 5. Veredicto"
extra = """## 4.1 Lo que otro validador encontró sobre esta misma fase

**El comparador de plan contra lo hecho, construido media hora después, dijo que esta fase tocó tres archivos que su plan no declaraba:** `validadores/conteo.py`, su contrato y su archivo de pruebas. Es cierto: el plan, escrito el 2026-08-17, daba por hecho que el conteo viviría dentro de `validar.py`, y al construirlo se vio que convenía un módulo propio.

**La decisión fue buena y el procedimiento no:** ampliar el plan exige escribirlo antes de ejecutar ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)). Queda dicho acá, que es donde alguien lo va a buscar.

## 5. Veredicto"""
assert a in s
io.open(p, "w", encoding="utf-8", newline="").write(s.replace(a, extra, 1))

assert io.open("VERSION", encoding="utf-8").read().strip() == "31.10.0"
io.open("VERSION", "w", encoding="utf-8", newline="").write("31.11.0\n")
c = io.open("CHANGELOG.md", encoding="utf-8").read()
e = """## 31.11.0 — 2026-08-22

**MENOR** (una comprobación nueva para el cierre de una fase; nadie tiene que hacer nada).

**Ya se puede comprobar si una fase tocó los archivos que su plan decía.** El estándar exige desde siempre que una unidad de trabajo edite lo que su plan declaró, y que descubrir otro archivo detenga la ejecución hasta ampliarlo por escrito; comprobarlo era leer el plan y los cambios a la vez, o sea casi nunca. Ahora una orden los compara contra el punto del que salió la fase, y avisa lo que no cuadra. También dice qué criterio de aceptación se quedó sin ningún caso que lo compruebe.

**Avisa y no detiene**, porque un archivo de más puede ser un descubrimiento que se reportó y se aprobó, y eso no se ve desde los archivos. Lo que el programa afirma es que la lista no cuadra; si la explicación cuadra, lo lee una persona.

**Y su primera corrida encontró un incumplimiento del trabajo de esta misma jornada:** la mejora anterior tocó tres archivos que su plan no declaraba. La decisión de separarlos fue buena; lo que faltó fue anotarla antes de ejecutar. Queda escrito en las dos fases.

**El detalle.** Fase [`A-EP-004-HU-013`](documentacion/epicas/EP-004-comprobacion-automatica/HU-013-comparar-el-plan-con-lo-hecho/A-EP-004-HU-013-comparar-lo-hecho-con-el-plan-aprobado/README.md), del [pendiente 59](pendientes/59-las-42-dudas-que-detienen-26-fases.md), con sus decisiones 10 y 22. Nace [`validadores/plan_vs_hecho.py`](validadores/plan_vs_hecho.py) y el subcomando `validar.py plan`, con once casos. Lo que **no** se automatiza queda declarado: comparar los pasos ejecutados con los escritos exige leer los dos textos, y eso sigue siendo de una persona.

"""
c = c.replace("## 31.10.0 — 2026-08-22", e + "## 31.10.0 — 2026-08-22", 1)
io.open("CHANGELOG.md", "w", encoding="utf-8", newline="").write(c)
print("ok")
