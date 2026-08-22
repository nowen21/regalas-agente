# -*- coding: utf-8 -*-
import sys, os, io
SP = r"C:/Users/user/AppData/Local/Temp/claude/c--Ing--Jose-ia-agente/563dc2f9-c782-46f9-af82-c9bc948b3566/scratchpad"
sys.path.insert(0, SP)
import cerrar_estado
os.chdir(r"c:\Ing. Jose\ia\agente")

C = "documentacion/epicas/EP-002-versionado-y-adopcion/HU-005-sellar-el-trabajo-cerrado/A-EP-002-HU-005-el-sello-de-version-en-el-cierre/"
A = "../../../../../"

io.open(C + "resultado_pruebas.md", "w", encoding="utf-8", newline="").write("""# Resultado de Pruebas — Fase A-EP-002-HU-005-el-sello-de-version-en-el-cierre

**Para qué sirve este documento.** Registra qué se ejecutó y con qué resultado. Los casos viven en el [plan_pruebas.md](plan_pruebas.md), que no se toca al ejecutar.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-002-HU-005-el-sello-de-version-en-el-cierre` |
| **HU** | [HU-005 Sellar el trabajo cerrado](../HU-005-sellar-el-trabajo-cerrado.md) |
| **Ciclo** | 1 · **Fecha** 2026-08-22 |
| **Ejecutado por** | El agente, por la orden del usuario de resolver el [pendiente 59](""" + A + """pendientes/59-las-42-dudas-que-detienen-26-fases.md) |

### 0.1 Las dos dudas que la detenían

| Duda | Decisión |
|---|---|
| ¿el validador lo exige o solo lo avisa? | **Avisa**, y no por comodidad: un cierre sin sello **no rompe nada hoy**, solo deja sin respuesta la pregunta de bajo qué reglas cerró. La regla del día, escrita en el pendiente 59, es detener lo que impide trabajar y avisar lo que solo informa mal |
| ¿el campo entra en los dos modelos o solo en el del cierre? | **Solo en el del cierre** (decisión 28). Al abrir la fase todavía no hay nada que sellar, y un campo que se llena con «pendiente» es un campo que nadie llena |

## 1. Resumen

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos |
|---|---:|---:|---:|---:|
| 1 | 5 | 5 | 5 | 0 |

## 2. Caso por caso

| Caso | Qué comprueba | Resultado |
|---|---|---|
| CP-001 · el cierre sin sello se detecta, y el que lo tiene pasa | el corazón del CA | ✅ Aprobado: `validar.py fases` lo reporta como aviso |
| CP-002 · el campo pide de dónde salió el número | «del archivo `VERSION` en el momento de cerrar» | ✅ Aprobado, escrito en el propio molde |
| CP-003 · la fase cerrada bajo una versión anterior no se reporta por reglas posteriores | es el motivo de existir del sello | ✅ Aprobado: lo cerrado antes del 2026-08-22 queda fuera |
| CP-004 · la derogación sin adoptar detiene la fase en curso, no la cerrada | ya lo hacía [`02·F22`](""" + A + """base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md) | ✅ Aprobado |
| CP-005 · el sello está desde el estado de la fase | se lee sin abrir el cierre | ✅ Aprobado: el estado enlaza al cierre, que lo trae en su cabecera |

## 3. Lo que se construyó, y lo que se selló

**El molde del cierre gana el campo** «Versión del estándar al cerrar», con la caja que dice para qué sirve: sin él, una regla nueva de mañana parece incumplida hoy.

**Y `validar.py fases` lo comprueba**, reconociendo las dos formas: la fila del molde y la frase suelta. El molde es lo que se pide, pero un cierre escrito a mano que diga «cerrada el … con el estándar en la 31.8.0» dice exactamente lo mismo, y reportarlo sería reportar la forma en vez del contenido.

**Los quince cierres escritos hoy quedaron sellados**, cada uno con la versión bajo la que de verdad cerró, de la 30.9.1 a la 31.8.0.

## 4. Defectos encontrados

**Uno, y del propio trabajo de hoy:** los cierres que se escribieron durante la jornada no traían el campo, porque el campo no existía cuando se escribieron. Se sellaron los quince. **Lo anterior no se toca:** `20·M10` dice que un cambio de norma no reabre lo cerrado, y este campo es justamente el que lo hace comprobable.

## 5. Veredicto

**Cumple.** Cinco casos de cinco.
""")

io.open(C + "funcionalidad_implementada.md", "w", encoding="utf-8", newline="").write("""# Funcionalidad implementada — Fase A-EP-002-HU-005-el-sello-de-version-en-el-cierre

**Para qué sirve este documento.** Dice qué quedó hecho al cerrar la fase, con su trazabilidad.

> **Cerrada el 2026-08-22, con el estándar en la versión 31.9.0.** Es el sello que dice **bajo qué reglas** cerró este trabajo: una regla escrita después no lo reabre ([`20·M10`](""" + A + """base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).

## 0. Qué quedó, en una frase

**Todo cierre dice bajo qué versión del estándar cerró**, así que una regla nueva ya no puede hacer parecer incumplido un trabajo viejo.

## 1. Trazabilidad ([`13·DOC11`](""" + A + """base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| El molde del cierre pide el sello | doc | [`plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md`](""" + A + """plantillas/ciclo-vida-proyectos/11-funcionalidad-implementada.md) | ✅ | campo y caja del porqué |
| El cierre sin sello se detecta | código | [`validadores/fases.py`](""" + A + """validadores/fases.py) | ✅ | `cierre_sin_sello`, como aviso |
| Se reconocen las dos formas de escribirlo | código | el mismo | ✅ | la fila del molde y la frase suelta |
| Nada se exige hacia atrás | código | el mismo | ✅ | corte en el 2026-08-22 |
| Los cierres de hoy quedaron sellados | doc | quince fases | ✅ | de la 30.9.1 a la 31.8.0 |

## 2. Lo que cambia para un proyecto que hereda

**Un cierre nuevo lleva una línea más.** La escribe quien cierra, con el número que tenga `VERSION` en ese momento. Los cierres anteriores no se tocan.

## 3. Lo que queda abierto

**El sello no se pone solo.** Podría: el número está en `VERSION` y el momento es el cierre. No se automatizó porque, según [`20·M19`](""" + A + """base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md), primero tiene que cumplirse a mano y verse cuántas veces se olvida; hoy lleva un día de vida.
""")

cerrar_estado.cerrar(C.rstrip("/"), cumplidos="2 de 2",
                     nota_extra="Se construyó el campo del molde y su comprobación, y se sellaron los quince cierres de la jornada.")

assert io.open("VERSION", encoding="utf-8").read().strip() == "31.8.0"
io.open("VERSION", "w", encoding="utf-8", newline="").write("31.9.0\n")
c = io.open("CHANGELOG.md", encoding="utf-8").read()
e = """## 31.9.0 — 2026-08-22

**MENOR** (el documento de cierre de una fase gana un campo; lo ya cerrado no se toca).

**Un trabajo cerrado ya dice bajo qué reglas se cerró.** Sin eso, cada regla nueva hace parecer incumplido lo viejo, y hay que reabrirlo para averiguar si lo estaba, que es exactamente lo que el estándar dice que **no** pasa: una norma nueva no reabre lo cerrado. Ahora el documento de cierre trae el número de versión del estándar en el momento de cerrar, y la comprobación de fases avisa cuando falta.

**Avisa, no detiene:** un cierre sin ese dato no rompe nada hoy, solo deja una pregunta sin respuesta. Y no se exige hacia atrás: lo cerrado antes de hoy queda de su lado.

**El detalle.** Fase [`A-EP-002-HU-005`](documentacion/epicas/EP-002-versionado-y-adopcion/HU-005-sellar-el-trabajo-cerrado/A-EP-002-HU-005-el-sello-de-version-en-el-cierre/README.md), del [pendiente 59](pendientes/59-las-42-dudas-que-detienen-26-fases.md), con sus decisiones 7 y 28. El campo entra al molde del cierre y no al de apertura, porque al abrir todavía no hay nada que sellar. La comprobación reconoce la fila del molde y también la frase escrita a mano, para no reportar la forma en vez del contenido. Los quince cierres escritos hoy quedaron sellados con la versión bajo la que de verdad cerraron.

"""
c = c.replace("## 31.8.0 — 2026-08-22", e + "## 31.8.0 — 2026-08-22", 1)
io.open("CHANGELOG.md", "w", encoding="utf-8", newline="").write(c)
print("ok")
