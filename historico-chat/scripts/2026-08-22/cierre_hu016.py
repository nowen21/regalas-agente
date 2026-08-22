# -*- coding: utf-8 -*-
import sys, os, io
SP = r"C:/Users/user/AppData/Local/Temp/claude/c--Ing--Jose-ia-agente/563dc2f9-c782-46f9-af82-c9bc948b3566/scratchpad"
sys.path.insert(0, SP)
import cerrar_estado
os.chdir(r"c:\Ing. Jose\ia\agente")

H = "documentacion/epicas/EP-004-comprobacion-automatica/HU-016-el-pendiente-cerrado-nombra-su-fase/"
A = "../../../../../"


def escribir(ruta, texto):
    io.open(ruta, "w", encoding="utf-8", newline="").write(texto)


escribir(H + "A-EP-004-HU-016-el-pendiente-cerrado-declara-su-fase/resultado_pruebas.md", """# Resultado de Pruebas — Fase A-EP-004-HU-016-el-pendiente-cerrado-declara-su-fase

**Para qué sirve este documento.** Registra qué se ejecutó y con qué resultado. Los casos viven en el [plan_pruebas.md](plan_pruebas.md), que no se toca al ejecutar.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-004-HU-016-el-pendiente-cerrado-declara-su-fase` |
| **HU** | [HU-016 El pendiente cerrado nombra su fase](../HU-016-el-pendiente-cerrado-nombra-su-fase.md) |
| **Ciclo** | 1 · **Fecha** 2026-08-22 |
| **Ejecutado por** | El agente, por la orden del usuario de resolver el [pendiente 59](""" + A + """pendientes/59-las-42-dudas-que-detienen-26-fases.md) |

### 0.1 Las dos dudas que la detenían

| Duda | Decisión, del pendiente 59 |
|---|---|
| ¿desde cuándo se exige? | **Desde el 2026-08-16**, que es cuando nació la exigencia. Lo cerrado antes no se reabre, igual que `20·M10` con cualquier norma nueva (decisión 26) |
| ¿dónde se declara? | **Una fila fija en la ficha de cabecera**, no una sección: una sección se olvida sin dejar rastro, una fila se ve vacía (decisión 27) |

## 1. Resumen

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos |
|---|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 |

## 2. Caso por caso

| Caso | Qué comprueba | Resultado |
|---|---|---|
| CP-001 · el cerrado sin fase se reporta, el que la nombra no | el corazón del CA | ✅ Aprobado, como **aviso**: ya no rompe nada, solo cortó su rastro |
| CP-002 · la fase inventada se reporta | nombrar una fase que no existe es peor que no nombrar ninguna | ✅ Aprobado: se busca la carpeta en `documentacion/epicas/` |
| CP-003 · el cerrado por decisión no se reporta | no hubo desarrollo, no hay fase que nombrar | ✅ Aprobado |
| CP-004 · lo cerrado antes del corte queda de su lado | la norma no se aplica hacia atrás | ✅ Aprobado, y también lo que no declara fecha |

## 3. Lo que la primera corrida midió

**24 pendientes cerrados desde el 2026-08-16 no dicen en qué fase se hicieron.** Esa es la deuda real, y ahora se puede ver corriendo `validar.py pendientes` en vez de abriendo 35 archivos.

**No se rellenaron acá, y es a propósito.** Averiguar la fase de cada uno exige leer su historia y su commit; hacerlo a las corridas es el camino directo a escribir una fase que no fue. Cada uno lo gana cuando alguien lo toque, y mientras tanto el aviso lo recuerda.

**Y por qué los que no declaran fecha quedan fuera:** los pendientes viejos no la traen, así que exigirles la fase sería aplicar hacia atrás una norma nueva. Treinta avisos que nunca se van apagan la comprobación entera, que es el patrón que este repositorio ya vio cuatro veces.

## 4. Veredicto

**Cumple.** Cuatro casos de cuatro, más ocho automatizados en [`test_pendientes_historia.py`](""" + A + """validadores/tests/test_pendientes_historia.py).
""")

escribir(H + "A-EP-004-HU-016-el-pendiente-cerrado-declara-su-fase/funcionalidad_implementada.md", """# Funcionalidad implementada — Fase A-EP-004-HU-016-el-pendiente-cerrado-declara-su-fase

**Para qué sirve este documento.** Dice qué quedó hecho al cerrar la fase, con su trazabilidad.

## 0. Qué quedó, en una frase

**Un pendiente cerrado que no dice en qué fase se hizo ya no pasa inadvertido:** la corrida lo nombra.

## 1. Trazabilidad ([`13·DOC11`](""" + A + """base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| El cerrado sin fase se reporta | código | [`validadores/pendientes.py`](""" + A + """validadores/pendientes.py) | ✅ | `cerrado_declara_su_fase`, como aviso |
| La fase nombrada tiene que existir | código | el mismo | ✅ | se busca su carpeta en `documentacion/epicas/` |
| Lo cerrado por decisión queda fuera | código | el mismo | ✅ | no hubo desarrollo |
| Lo anterior al 2026-08-16 queda fuera | código | el mismo | ✅ | la norma no se aplica hacia atrás |
| Los casos | prueba | [`test_pendientes_historia.py`](""" + A + """validadores/tests/test_pendientes_historia.py) | ✅ | ocho, con los dos sentidos |

## 2. Lo que cambia para un proyecto que hereda

**Gana la comprobación en su propia carpeta de pendientes**, con el mismo corte: solo se le exige a lo que cierre de ahora en adelante.

## 3. Lo que queda abierto

**24 pendientes cerrados desde el corte siguen sin declarar su fase.** Está medido y a la vista en cada corrida; se llena cuando cada uno se toque, porque reconstruir la fase de veinticuatro de memoria es el camino directo a escribir una que no fue.
""")

escribir(H + "B-EP-004-HU-016-todo-pendiente-abierto-nombra-su-historia/resultado_pruebas.md", """# Resultado de Pruebas — Fase B-EP-004-HU-016-todo-pendiente-abierto-nombra-su-historia

**Para qué sirve este documento.** Registra qué se ejecutó y con qué resultado. Los casos viven en el [plan_pruebas.md](plan_pruebas.md).

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-004-HU-016-todo-pendiente-abierto-nombra-su-historia` |
| **HU** | [HU-016](../HU-016-el-pendiente-cerrado-nombra-su-fase.md) |
| **Ciclo** | 1 · **Fecha** 2026-08-22 |
| **Ejecutado por** | El agente, por la orden del usuario de resolver el [pendiente 59](""" + A + """pendientes/59-las-42-dudas-que-detienen-26-fases.md) |

## 1. Resumen

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos |
|---|---:|---:|---:|---:|
| 1 | 6 | 6 | 6 | 0 |

## 2. Caso por caso

| Caso | Qué comprueba | Resultado |
|---|---|---|
| CP-001 · el abierto sin la fila se reporta | y **detiene**: un pendiente sin historia no se puede ejecutar | ✅ Aprobado |
| CP-002 · la historia inventada se reporta | queda cubierto por el mismo camino que la fase inventada | ✅ Aprobado |
| CP-003 · el tema declarado pasa, la fila vacía no | no toda idea tiene historia todavía, y decirlo es una respuesta | ✅ Aprobado |
| CP-004 · los enrutados siguen en verde | los tres pendientes abiertos de hoy pasan sin tocar nada | ✅ Aprobado |
| CP-005 · la fila fuera de la ficha no cuenta | la fila vive en la ficha de cabecera, no en cualquier tabla | ✅ Aprobado |
| CP-006 · los casos borde del archivo | el índice de la carpeta no es un pendiente | ✅ Aprobado |

## 3. Por qué esta falla y la otra avisa

**Un abierto sin historia es un impedimento**: [`02·F23`](""" + A + """base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md) manda construirlo como fase de una historia, y sin ella no hay dónde. **Un cerrado sin fase ya no rompe nada**: cortó su rastro, que es grave para leer el pasado y no impide nada hoy.

Es la misma regla que quedó escrita en el pendiente 59: **detiene lo que impide trabajar, avisa lo que solo informa mal.**

## 4. Veredicto

**Cumple.** Seis casos de seis. Los tres pendientes abiertos del repositorio pasan hoy sin cambios: el enrutamiento del 2026-08-17 dejó a cada uno con su historia, y esto es lo que impide que el próximo nazca sin ella.
""")

escribir(H + "B-EP-004-HU-016-todo-pendiente-abierto-nombra-su-historia/funcionalidad_implementada.md", """# Funcionalidad implementada — Fase B-EP-004-HU-016-todo-pendiente-abierto-nombra-su-historia

**Para qué sirve este documento.** Dice qué quedó hecho al cerrar la fase, con su trazabilidad.

## 0. Qué quedó, en una frase

**Un pendiente abierto que no nombra su historia rompe la corrida**, así que el enrutamiento deja de depender de que alguien se acuerde.

## 1. Trazabilidad ([`13·DOC11`](""" + A + """base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| El abierto sin la fila detiene | código | [`validadores/pendientes.py`](""" + A + """validadores/pendientes.py) | ✅ | `abierto_nombra_su_historia`, con FALLA |
| La fila vacía también | código | el mismo | ✅ | o nombra la historia, o dice por qué no la tiene |
| Lo que no es un pendiente numerado no cuenta | código | el mismo | ✅ | el índice de la carpeta queda fuera |
| Los casos | prueba | [`test_pendientes_historia.py`](""" + A + """validadores/tests/test_pendientes_historia.py) | ✅ | ocho, los dos sentidos juntos |

## 2. Lo que cambia para un proyecto que hereda

**Un pendiente nuevo tiene que decir a qué historia baja.** Si todavía no lo sabe, la fila lo dice con esas palabras: eso pasa, y es lo que distingue una idea de un pendiente listo para ejecutar.

## 3. Lo que queda abierto

**Nada de esta fase.** Lo que sigue abierto es del otro sentido: los 24 cerrados que no declaran su fase, medidos en la fase `A`.
""")

for c, cum, nota in (
    (H + "A-EP-004-HU-016-el-pendiente-cerrado-declara-su-fase", "1 de 1",
     "Construida: `pendientes.py` gana la comprobación hacia abajo, y midió 24 cerrados sin fase."),
    (H + "B-EP-004-HU-016-todo-pendiente-abierto-nombra-su-historia", "1 de 1",
     "Construida: la comprobación hacia arriba, que **detiene**."),
):
    cerrar_estado.cerrar(c, cumplidos=cum, nota_extra=nota)
print("ok")
