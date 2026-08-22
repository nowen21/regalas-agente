# -*- coding: utf-8 -*-
import sys, os, io
SP = r"C:/Users/user/AppData/Local/Temp/claude/c--Ing--Jose-ia-agente/563dc2f9-c782-46f9-af82-c9bc948b3566/scratchpad"
sys.path.insert(0, SP)
import cerrar_estado
os.chdir(r"c:\Ing. Jose\ia\agente")

# El contrato del módulo nuevo, y su fila en el índice de docs.
io.open("validadores/docs/conteo.md", "w", encoding="utf-8", newline="\n").write("""# `conteo.py` — por cuál regla se incumple más

**Qué hace.** Al terminar la corrida completa, agrupa los hallazgos por la regla a la que pertenecen, imprime el recuento y anota una línea en un registro para poder comparar dos corridas.

**Para qué sirve el número.** Una regla que produce cien hallazgos por semana casi nunca significa un equipo descuidado: significa una regla **mal escrita**, o una que hace falta automatizar. Sin el número, esa conversación es opinión contra opinión, y [`20·M19`](../../base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md) pide justamente ese dato antes de construir un validador.

## De dónde sale la regla de cada hallazgo

**Del mensaje que el validador ya escribe.** Los veinticuatro citan su regla al explicar el incumplimiento: «(20·M5 · fila 10)», «S4/N6», «02·F24». Agruparlos no exigió tocarlos uno por uno.

| Caso | Qué se toma |
|---|---|
| El hallazgo la declara | esa, sin mirar el mensaje |
| El mensaje cita `20·M5` y `M5` | **`20·M5`**: el capítulo hace único al identificador |
| El mensaje no cita ninguna | `(sin regla)`, contado aparte |

**Lo que no se sabe no se reparte.** Sumar los hallazgos sin regla a cualquier otra falsearía el número que se usa para decidir qué regla cambiar, y ese número es todo el punto.

## Qué se guarda, y qué no

| Se guarda | No se guarda |
|---|---|
| el identificador de la regla | el texto del hallazgo |
| cuántas veces | la ruta ni la línea del archivo revisado |
| la fecha y la versión del estándar | nada del contenido revisado |

**Por qué importa tanto.** En un mensaje de incumplimiento viaja el contenido revisado, y ahí puede ir una clave o un dato personal ([`00·N6`](../../base/00-nucleo-blindado.md), [`12·PR4`](../../base/12-privacidad-datos.md)). Un archivo de métricas que copie lo revisado es una fuga con nombre de estadística.

## Dónde vive

`metricas/conteo-por-regla.jsonl`, **fuera del control de versiones**: es generado, y [`09·G3`](../../base/09-git.md) deja fuera lo generado. Su contenido cambia en cada corrida, así que versionarlo llenaría el historial de ruido. El precedente es `plantillas/proyectos.md`.

Una línea por corrida. Con dos líneas ya se puede decir qué bajó y qué subió, que es lo que se imprime al final.

## Cómo se corre

```
python validadores/validar.py todo
```

No hay subcomando propio: el conteo es lo último de la corrida completa, porque contar exige haber corrido todo.

## Casos que lo protegen

[`validadores/tests/test_el_conteo_por_regla.py`](../tests/test_el_conteo_por_regla.py), once. El que decide es `CP-002`: el registro no puede contener el texto del hallazgo.
""")

p = "validadores/docs/README.md"
s = io.open(p, encoding="utf-8").read()
if "conteo.md" not in s:
    a = "| `guardian_version.py` |"
    i = s.find(a); fin = s.find("\n", i)
    s = s[:fin] + "\n| `conteo.py` | [conteo.md](conteo.md) | Al terminar la corrida completa, dice por cuál regla se incumple más, y guarda solo el número. |" + s[fin:]
    io.open(p, "w", encoding="utf-8", newline="").write(s)

C = "documentacion/epicas/EP-004-comprobacion-automatica/HU-009-conteo-por-regla/A-EP-004-HU-009-el-conteo-de-hallazgos-por-regla/"
A = "../../../../../"
io.open(C + "resultado_pruebas.md", "w", encoding="utf-8", newline="").write("""# Resultado de Pruebas — Fase A-EP-004-HU-009-el-conteo-de-hallazgos-por-regla

**Para qué sirve este documento.** Registra qué se ejecutó y con qué resultado. Los casos viven en el [plan_pruebas.md](plan_pruebas.md), que no se toca al ejecutar.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-004-HU-009-el-conteo-de-hallazgos-por-regla` |
| **HU** | [HU-009 Conteo por regla](../HU-009-conteo-por-regla.md) |
| **Ciclo** | 1 · **Fecha** 2026-08-22 |
| **Ejecutado por** | El agente, por la orden del usuario de resolver el [pendiente 59](""" + A + """pendientes/59-las-42-dudas-que-detienen-26-fases.md) |

### 0.1 Las dos dudas que la detenían

| Duda | Decisión |
|---|---|
| ¿dónde vive el registro: versionado, no versionado o solo en la salida? | **No versionado**, decisión 25 del pendiente 59: [`09·G3`](""" + A + """base/09-git.md) deja fuera lo generado, y su contenido cambia en cada corrida |
| ¿espera a la corrida completa de HU-008? | **No esperaba: hoy ya existe.** Se construyó en esta misma jornada, y el conteo se enganchó a ella, que es donde tiene sentido: contar exige haber corrido todo |

## 1. Resumen

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos |
|---|---:|---:|---:|---:|
| 1 | 4 del plan, 11 escritos | 11 | 11 | 0 |

## 2. Caso por caso

| Caso | Qué comprueba | Resultado |
|---|---|---|
| CP-001 · la corrida deja el conteo agrupado por regla | y la regla sale del mensaje que el validador ya escribe | ✅ Aprobado, con cuatro casos: deducción, prioridad del capítulo, regla declarada y lo que no nombra ninguna |
| CP-002 · el registro no contiene la clave del archivo revisado | **el caso que decide** | ✅ Aprobado: se guarda `04·S4` y el número; no la clave, no la ruta, no el mensaje |
| CP-003 · dos corridas con un arreglo en medio muestran la baja | para eso se guarda | ✅ Aprobado: lo que no cambió no se reporta |
| CP-004 · el campo nuevo no rompe nada | `Hallazgo` lo usan los 24 validadores | ✅ Aprobado: se imprime igual, y una línea rota del registro no se lleva el resto |

## 3. La primera corrida real, que es el dato que faltaba

```
$ python validadores/validar.py todo
…
Hallazgos por regla (3552 en total):
  00·ID8       2391
  (sin regla)  603
  F18          296
  S3            85
  F2            36
```

**Y ese primer número ya dice algo.** `00·ID8` —las marcas de generación automática— produce **dos de cada tres hallazgos del repositorio**. No es que se incumpla más: es que se mide sobre todo el árbol, incluidos el histórico y los documentos de trabajo, mientras la regla exige limpieza en lo que se **entrega**. Es exactamente la clase de conversación que este conteo vino a hacer posible, y queda anotada para quien mire la regla.

## 4. Defectos encontrados

**Ninguno del conteo.** Y una decisión de diseño que vale escribir: los hallazgos se acumulan en `comun.reportar`, por donde pasan todos, en vez de pedirle a cada validador que además los devuelva. Tocar veinticuatro archivos para saber algo que ya pasa por un solo punto habría sido el camino largo y frágil.

## 5. Veredicto

**Cumple.** Once casos de once.
""")

io.open(C + "funcionalidad_implementada.md", "w", encoding="utf-8", newline="").write("""# Funcionalidad implementada — Fase A-EP-004-HU-009-el-conteo-de-hallazgos-por-regla

**Para qué sirve este documento.** Dice qué quedó hecho al cerrar la fase, con su trazabilidad.

> **Cerrada el 2026-08-22, con el estándar en la versión 31.10.0.** Es el sello que dice **bajo qué reglas** cerró este trabajo: una regla escrita después no lo reabre ([`20·M10`](""" + A + """base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).

## 0. Qué quedó, en una frase

**Al terminar la corrida completa se sabe por cuál regla se incumple más, y dos corridas se pueden comparar.**

## 1. Trazabilidad ([`13·DOC11`](""" + A + """base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| Cada hallazgo dice a qué regla pertenece | código | [`validadores/comun.py`](""" + A + """validadores/comun.py) | ✅ | `Hallazgo.regla`, deducida del mensaje que ya se escribe |
| La corrida deja el conteo | código | [`validadores/conteo.py`](""" + A + """validadores/conteo.py) y `validar.py todo` | ✅ | el recuento se imprime y se anota |
| El registro guarda solo el identificador y el número | código | el mismo | ✅ | `CP-002`: ni la clave, ni la ruta, ni el mensaje |
| Vive fuera del control de versiones | doc | `.gitignore` | ✅ | `metricas/conteo-por-regla.jsonl`, con el motivo escrito |
| Dos corridas se comparan | código | `conteo.comparar` | ✅ | `CP-003` |
| El contrato dice qué se guarda y qué no | doc | [`validadores/docs/conteo.md`](""" + A + """validadores/docs/conteo.md) | ✅ | con las dos tablas |
| Los casos | prueba | [`test_el_conteo_por_regla.py`](""" + A + """validadores/tests/test_el_conteo_por_regla.py) | ✅ | once |

## 2. Lo que cambia para un proyecto que hereda

**Corre solo con la corrida completa**, y no pide nada. Un proyecto que use `validar.py todo` empieza a acumular su propio recuento, en su carpeta y fuera de su control de versiones.

## 3. Lo que queda abierto

**El primer dato ya pide una conversación:** `00·ID8` produce dos de cada tres hallazgos del repositorio, porque se mide sobre todo el árbol mientras la regla exige limpieza en lo que se **entrega**. O la medición se acota a lo entregable, o la regla dice que aplica a todo. Está anotado en el resultado de esta fase; decidirlo no es de acá.
""")

cerrar_estado.cerrar(C.rstrip("/"), cumplidos="3 de 3",
                     nota_extra="Construida entera; el conteo se enganchó a la corrida completa, que nació esta misma jornada.")
print("ok")
