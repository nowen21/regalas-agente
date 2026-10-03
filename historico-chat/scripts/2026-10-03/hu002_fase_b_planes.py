# -*- coding: utf-8 -*-
"""Fase B de la HU-002: plan de trabajo, plan de pruebas, estado de la fase y su fila en la HU."""
import glob
import io
import os
import re

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
HU_DIR = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "HU-002-*"))[0]
HU_DOC = "HU-002-cada-documento-sale-del-anterior.md"
FASE = "B-EP-023-HU-002-el-agente-recibe-los-acuerdos-y-el-plan-marca-lo-suyo"
D = os.path.join(HU_DIR, FASE)
A10 = "[análisis 10](../../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-10.md)"
HU_REL = "documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/HU-002-cada-documento-sale-del-anterior/" + HU_DOC

PLAN = """# Plan de Trabajo · Fase `{f}` (módulo `validadores/`, `adaptadores/claude-code/` y `plantillas/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `{f}` |
| **Épica** | [EP-023](../../epica.md) |
| **HU** | [HU-002](../{hu}), una sola (`F12.1`) |
| **Módulo** | `validadores/`, `adaptadores/claude-code/`, `plantillas/` |
| **Especificación del módulo** | Los CA-04 y CA-05 de la HU-002 |
| **Fecha apertura** | 2026-10-03 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): segunda fase de la HU-002. Sale de los puntos 1 y 2 de «Lo que se tiene que hacer» del {a10} (acuerdos 3 y 4).

**Carencias que cierra** (`02·F14` Q3): el agente no recibe los acuerdos de los que sale lo que trabaja y los pierde cuando la conversación se resume; el plan no distingue lo que sale del análisis de lo que propone el agente.

**Aprobación** (`02·F4`): pendiente.

**Disparo** (`02·F15`, etapa 2): el usuario pidió escribir esta fase el 2026-10-03 con «Escriba».

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-002 | Estado |
|---|---|
| CA-04 · El agente recibe los acuerdos de los que sale lo que trabaja | ☐ |
| CA-05 · Lo que el plan decide por su cuenta queda marcado como propuesta del agente | ☐ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que con cada mensaje le lleguen al agente los acuerdos de los que sale lo que trabaja, y que toda decisión del plan diga de qué acuerdo sale o que es propuesta del agente.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-04 | Un enganche entrega, con cada mensaje, los acuerdos de la fase en curso y los del análisis prendido | Programa y enganche | Media |
| CA-05 | La tabla de decisiones del plan cita el acuerdo o marca la propuesta, y el validador de origen detiene la que no tiene ninguna | Plantilla y validador | Baja |

**Fuera de alcance:** el freno que compara con el plan de la fase en curso (HU-007, fase `B`).

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-10-03, sobre la versión 49.0.0:

- `adaptadores/claude-code/hook_reglas.py` entrega con cada mensaje las reglas que pide el mensaje. La herramienta acepta 10.000 caracteres por enganche, y el de las reglas ya usa casi todo su tope (`recuperar.TOPE`). No entrega acuerdos.
- `validadores/origen.py` ya sigue la cadena del criterio al punto y del punto al acuerdo (`leer_analisis`, `_revisar_hu`), pero solo para avisar orígenes rotos; no lee el plan.
- `validadores/analisis_en_curso.py` guarda en `historico-chat/.estado/analisis-en-curso.txt` qué análisis está prendido.
- Ningún programa dice qué fase está en curso. `validadores/estacion_commit.py` anota el commit en la estación 12 del estado de la fase. De 240 fases, 105 no lo tienen anotado porque cerraron antes de que existiera esa anotación; las 105 tienen `funcionalidad_implementada.md` y ninguna trae la aprobación con versión que pide el plan desde 48.0.0.
- La tabla 2.6 de `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` tiene «Decisión», «Alternativa descartada» y «Justificación»; no pide de dónde sale la decisión.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

> Cada fila lleva una o más rutas exactas entre comillas invertidas, separadas por coma.

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/acuerdos.py` | Nuevo | Programa | La fase en curso y los acuerdos que le tocan; los del análisis prendido; el texto con su tope |
| `adaptadores/claude-code/hook_acuerdos.py` | Nuevo | Enganche | Entrega el texto con cada mensaje |
| `validadores/instalar.py` | Modificar | Instalador | Registra el enganche |
| `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` | Modificar | Plantilla | La columna «Sale de» en la tabla 2.6 |
| `validadores/origen.py` | Modificar | Validador | La decisión del plan sin acuerdo ni marca |
| `validadores/tests/test_los_acuerdos_llegan.py` | Nuevo | Pruebas | Los casos del plan de pruebas |
| `anatomia/mapa-del-sitio.md` | Modificar | Documentación | El programa y el enganche nuevos |
| `{hurel}` | Modificar | Documentación | La fila de esta fase |
| `CHANGELOG.md`, `VERSION` | Modificar | Versión | 50.0.0 |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| La tabla 2.6 del plan suma una columna | Los planes nuevos | Se exige solo a los planes aprobados desde 50.0.0 |
| La fase en curso | El freno de la HU-007, fase `B` | Queda en `acuerdos.py` para que el freno la use |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Los acuerdos llegan con cada mensaje y, como las reglas, completos los que caben y los demás nombrados con su tema y su número | Cortar el texto donde se acabe el tope | El tema es lo que va antes de los dos puntos del acuerdo | Análisis 10, acuerdo 4 |
| La fase está en curso desde que se crea su carpeta hasta que su estado tiene el commit anotado | Desde que se aprueba su plan | El plan se escribe con la fase ya en curso | Análisis 10, acuerdo 4 |
| La fase cuyo plan no trae la aprobación con versión y ya tiene `funcionalidad_implementada.md` se da por cerrada | Contar en curso toda fase sin commit anotado | 105 fases que cerraron antes de que existiera la anotación quedarían en curso para siempre | Propuesta del agente |
| Los acuerdos de la fase salen de los CA de la tabla de su plan; si el plan todavía no los nombra, de todos los CA de su HU | Esperar a que el plan exista | El acuerdo 4 pide que lleguen desde que se crea la carpeta | Análisis 10, acuerdo 4 |
| Los acuerdos llegan por un enganche propio | Sumarlos al enganche de las reglas | El tope es por enganche y el de las reglas ya va casi lleno | Propuesta del agente |
| La tabla 2.6 suma la columna «Sale de», con «análisis N, acuerdo M» o «Propuesta del agente» | Una tabla aparte | Cada decisión dice de dónde sale en su misma fila | Análisis 10, acuerdo 3 |
| `origen.py` exige la columna solo a los planes aprobados desde 50.0.0 | Exigirla a todos | Los planes aprobados antes no se reabren (`20·M10`) | Propuesta del agente |
| La versión sube a 50.0.0, MAYOR | MENOR | Un plan nuevo no pasa `origen` sin la columna | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| Lo que recibe el agente con cada mensaje | Las reglas | Las reglas y los acuerdos de lo que trabaja | `02·F1` |
| Tabla 2.6 del plan | Sin origen | Cada decisión con su acuerdo o la marca de propuesta | `02·F27` |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-04 · El agente recibe los acuerdos de los que sale lo que trabaja

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | `acuerdos.py`: las fases en curso; los acuerdos de cada una, siguiendo el «Sale de» de sus CA; los de los análisis aprobados del pendiente del análisis prendido; y el texto con su tope, completos los que caben y los demás nombrados | `validadores/acuerdos.py` | CA-04 | Lo usa también el freno de la HU-007 | 2 h | Ninguna | CP-001, CP-002 |
| T-02 | El enganche que entrega ese texto con cada mensaje; nunca detiene el trabajo | `adaptadores/claude-code/hook_acuerdos.py` | CA-04 | Todo mensaje | 0,5 h | T-01 | CP-002 |
| T-03 | El instalador registra el enganche | `validadores/instalar.py` | CA-04 | Todo proyecto, al reinstalar | 0,3 h | T-02 | CP-002 |

### CA-05 · Lo que el plan decide por su cuenta queda marcado como propuesta del agente

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-04 | La tabla 2.6 suma la columna «Sale de», con su nota | `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` | CA-05 | Los planes nuevos | 0,3 h | Ninguna | CP-003 |
| T-05 | `origen.py` detiene, en el plan aprobado desde 50.0.0, la decisión que no cita un acuerdo existente de un análisis de su épica ni dice «Propuesta del agente» | `validadores/origen.py` | CA-05 | Ninguno en los planes aprobados antes | 1 h | T-04 | CP-003 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-06 | Escribir los casos del plan de pruebas; poner el programa y el enganche en el mapa del sitio; la fila de la fase en la HU; subir a 50.0.0 con «⚠ obliga a migrar» | `validadores/tests/test_los_acuerdos_llegan.py`, `anatomia/mapa-del-sitio.md`, `{hurel}`, `CHANGELOG.md`, `VERSION` | CA-04, CA-05 | Todo proyecto adopta la versión | 1 h | T-01 a T-05 | CP-001 a CP-004 |

## 4. Secuencia de ejecución

T-01, T-02 y T-03; después T-04 y T-05; al final T-06, con los validadores, las pruebas de la fase y la medición de marcas (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-04 | Con una fase en curso y con un análisis prendido, leer lo que el enganche entrega | CP-001, CP-002 |
| CA-05 | Leer la plantilla; el validador sobre un plan con una decisión sin acuerdo ni marca | CP-003 |

## 6. Datos y ambiente de prueba

Un proyecto de prueba en una carpeta temporal, con una épica, una HU, un pendiente con análisis aprobados y fases en distintos estados.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Cada proyecto adopta la 50.0.0 con el instalador, que registra el enganche nuevo. Los planes aprobados antes no se revisan; desde esa versión, cada decisión del plan dice de dónde sale.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`02·F1`, `02·F4`, `02·F8`, `02·F27`, `20·M2`, `20·M10`, `00·ID8`, `00·ID9`, `02·F5`, `02·F18`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Que los acuerdos llenen el mensaje | Tienen su propio tope: los que no caben llegan nombrados |
| Que una fase vieja aparezca en curso | Se reconoce por su cierre y por no traer la aprobación con versión |

## 11. Definition of Done

- [ ] CA-04 y CA-05 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Los validadores y las pruebas de la fase sin fallas, y cero marcas nuevas.
- [ ] `VERSION` y `CHANGELOG.md` en 50.0.0.
- [ ] Aprobación del usuario.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Se llena al cerrar la fase.

**Hallazgos al ejecutar:** se anota al cerrar.
"""

CPS = [
    ("CP-001", "CA-04", "Alta", "Sí", "Los acuerdos de la fase en curso", "T-01 terminada",
     "Una HU con CA que salen de un análisis aprobado y fases en distintos estados",
     [("Fase recién creada, sin plan", "Llegan los acuerdos de todos los CA de la HU"),
      ("Fase con plan que nombra un solo CA", "Llegan solo los acuerdos de ese CA"),
      ("Fase con el commit anotado en su estado", "No llega nada de esa fase"),
      ("Fase cuyo plan no trae la aprobación con versión y tiene `funcionalidad_implementada.md`", "No llega nada de esa fase")]),
    ("CP-002", "CA-04", "Alta", "Sí", "Los acuerdos del análisis prendido, con su tope", "T-01 a T-03 terminadas",
     "Un pendiente con los análisis 1 y 2 aprobados y el 3 prendido",
     [("Pedir el texto con el análisis 3 prendido", "Trae los acuerdos de los análisis 1 y 2"),
      ("Pedir el texto con un tope pequeño", "Los que no caben llegan nombrados con su tema y su número"),
      ("Correr el enganche con una entrada dañada", "Sale con 0 y no detiene"),
      ("Leer los enganches que registra el instalador", "Está el de los acuerdos")]),
    ("CP-003", "CA-05", "Alta", "Sí", "La decisión del plan dice de dónde sale", "T-04 y T-05 terminadas",
     "Planes de prueba aprobados con 49.0.0 y con 50.0.0",
     [("Leer la tabla 2.6 de la plantilla", "Tiene la columna «Sale de»"),
      ("Validar un plan de 50.0.0 con una decisión sin acuerdo ni marca", "Una falla"),
      ("Validar uno que cita un acuerdo que no existe", "Una falla"),
      ("Validar uno con una cita válida y una «Propuesta del agente»", "Ninguna falla"),
      ("Validar un plan aprobado con 49.0.0 sin la columna", "Ninguna falla")]),
    ("CP-004", "RNF-06", "Media", "Parcial", "Cada tarea cita su criterio", "Fase terminada", "Ninguno",
     [("Correr `validar.py flujo` y leer el plan", "Ninguna tarea sin su criterio")]),
]

PRUEBAS = """# Plan de Pruebas · Fase `{f}`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice con qué casos se comprueban los criterios de esta fase y qué resultado se espera. Se aprueba antes de correr la primera prueba; lo que pase al correrlas va en el `resultado_pruebas.md` de la fase.

| Campo | Valor |
|---|---|
| **Código** | PP-EP023-HU002-B |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-002: CA-04 y CA-05 |
| **Fecha** | 2026-10-03 |
| **Elaborado por** | Claude |
| **Revisado por** | Ing. José Dúmar Jiménez Ruíz |
| **Aprobado por** | Pendiente |
| **Estado** | Borrador |

Para una fase, la plantilla pide las secciones 3, 5, 6, 9 y 12; las demás son opcionales y no se usan.

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Unitario | La fase en curso, los acuerdos, el tope, el enganche y el validador de origen | Claude | Proyecto de prueba en una carpeta temporal | Sí |
| Aceptación | Que la plantilla diga lo que pide el criterio | Ing. José Dúmar Jiménez Ruíz | Lectura | No |

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | CA-04 y CA-05 |
| Compatibilidad | ☑ | Las fases y los planes de antes no cambian de estado |

### 3.3 Técnicas de diseño de casos

- Partición: fase recién creada, con plan, con commit y vieja; plan aprobado antes y desde 50.0.0; acuerdos que caben y que no.

### 3.4 Priorización

| Prioridad | Criterio | Cobertura exigida |
|---|---|---|
| Alta | CA-04 y CA-05 | 100% |

### 3.5 Alcance de la ejecución automatizada  ·  `02·F5`

Las pruebas de la fase: `validadores/tests/test_los_acuerdos_llegan.py`; las de los programas que cambia: `test_origen.py` y las del instalador; `validar.py estandar`, `flujo` y `origen`, y las marcas de lo que se va a guardar.

## 5. Matriz de trazabilidad

| HU | CA | Caso de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
{mat}

**Cobertura:** 2 de 2 criterios de esta fase y el RNF-06.

## 6. Casos de prueba

{casos}

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición | Tiempo de atención |
|---|---|---|
| **Alta** | Un acuerdo que debía llegar no llega, o una decisión sin origen pasa | Antes de cerrar la fase |
| **Baja** | Una marca de redacción | Antes de cerrar la fase |

### 9.2 Flujo del defecto

Un defecto se anota en el resultado de las pruebas. Si es un error dentro de lo que el plan aprobó, se corrige y se vuelve a correr el caso. Si está fuera del plan, es un hallazgo: se detiene la fase y vuelve al análisis.

### 9.3 Contenido mínimo de un reporte

- Caso y paso donde apareció.
- Resultado esperado frente al obtenido.

### 9.4 Registro

Los defectos van en el `resultado_pruebas.md` de la fase.

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de exigencias | Criterios y RNF con caso / criterios y RNF de la fase | 100% |
| Casos ejecutados | Ejecutados / diseñados | 100% |

### 12.2 Dónde se miden

En el `resultado_pruebas.md` de la fase.
"""


def escribir(nombre, texto):
    os.makedirs(D, exist_ok=True)
    with io.open(os.path.join(D, nombre), "w", encoding="utf-8", newline="\n") as s:
        s.write(texto)


def plan():
    escribir("plan_trabajo.md", PLAN.format(f=FASE, hu=HU_DOC, a10=A10, hurel=HU_REL))


def plan_pruebas():
    filas, casos = [], []
    for c in CPS:
        tipo = "Trazabilidad" if c[1] == "RNF-06" else "Funcional"
        filas.append("| HU-002 | %s | %s | %s | %s | %s | ☐ |" % (c[1], c[0], tipo, c[2], c[3]))
        pasos = "\n".join("| %d | %s | %s |" % (i, a, b) for i, (a, b) in enumerate(c[7], 1))
        casos.append("### %s · %s\n\n| Campo | Valor |\n|---|---|\n| **HU / CA** | HU-002 / %s |\n"
                     "| **Precondiciones** | %s |\n| **Datos de entrada** | %s |\n\n"
                     "| # | Acción | Resultado esperado |\n|---|---|---|\n%s" % (c[0], c[4], c[1], c[5], c[6], pasos))
    escribir("plan_pruebas.md", PRUEBAS.format(f=FASE, mat="\n".join(filas), casos="\n\n".join(casos)))


def estado():
    origen = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "HU-007-*", "A-EP-023-*", "estado-fase.md"))[0]
    t = io.open(origen, encoding="utf-8").read()
    t = t.replace(os.path.basename(os.path.dirname(origen)), FASE)
    pares = [
        ("(módulo `base/`, `plantillas/` y `validadores/`)", "(módulo `validadores/`, `adaptadores/claude-code/` y `plantillas/`)"),
        ("| **Módulo** | `base/`, `plantillas/` y `validadores/` |", "| **Módulo** | `validadores/`, `adaptadores/claude-code/` y `plantillas/` |"),
        ("[HU-007](../HU-007-nada-se-escribe-fuera-del-plan-aprobado.md)", "[HU-002](../%s)" % HU_DOC),
        ("| **Última actualización** | 2026-10-02 |", "| **Última actualización** | 2026-10-03 |"),
        ("**Estación actual:** 12, commit. **Última puerta pasada:** 11.", "**Estación actual:** 7, planificador de tareas. **Última puerta pasada:** 6."),
        ("☑ Análisis 1 y 8 del pendiente 103", "☑ Análisis 10 del pendiente 103"),
        ("☑ Los análisis 1 y 8, aprobados", "☑ El análisis 10, aprobado"),
        ("| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ El 2026-10-02 |", "| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ El 2026-10-03 |"),
        ("N/A: la especificación son los CA-01, CA-03 y CA-04", "N/A: la especificación son los CA-04 y CA-05"),
        ("☑ Aprobados el 2026-10-02", "☐ Escritos; esperan la aprobación"),
        ("| 8 | Implementador | implementado + pruebas verdes | ☑ Las 8 tareas; las pruebas de la fase pasan |", "| 8 | Implementador | implementado + pruebas verdes | ☐ |"),
        ("| 9 | Verificador | trazabilidad sin faltantes | ☑ `flujo` sin fallas |", "| 9 | Verificador | trazabilidad sin faltantes | ☐ |"),
        ("| 10 | Crítico | sin hallazgos graves | ☑ Ninguno |", "| 10 | Crítico | sin hallazgos graves | ☐ |"),
        ("| 11 | Cierre documental + señales | docs y señales al día | ☑ Resultado de pruebas, HU y registro de cambios |", "| 11 | Cierre documental + señales | docs y señales al día | ☐ |"),
        ("| 12 | Commit | 👤 autorizado | ✅ `34be029` |", "| 12 | Commit | 👤 autorizado | ☐ |"),
        ("**Hechas:** 8 de 8. **Bloqueadas:** ninguna.", "**Hechas:** 0 de 6. **Bloqueadas:** todas, hasta que se aprueben los planes."),
        ("| **Concepto** | Cumple |", "| **Concepto** | Sin ejecutar |"),
        ("| **CA cumplidos** | 3 de 3 |", "| **CA cumplidos** | 0 de 2 |"),
        ("## 3. Pendiente / preguntas abiertas\n\nNinguna.\n", "## 3. Pendiente / preguntas abiertas\n\n- Que el usuario apruebe el plan de trabajo y el de pruebas.\n"),
    ]
    for a, b in pares:
        assert t.count(a) == 1, a
        t = t.replace(a, b)
    escribir("estado-fase.md", t)


def fila_en_la_hu():
    p = os.path.join(HU_DIR, HU_DOC)
    s = io.open(p, encoding="utf-8").read()
    m = re.search(r"^\| `A-EP-023-HU-002-[^\n]*\|$", s, re.M)
    assert m
    fila = ("| [`%s`](%s/estado-fase.md) | CA-04, CA-05 | Fase `A` | [plan](%s/plan_trabajo.md) | "
            "[pruebas](%s/plan_pruebas.md) | Pendiente | Planes escritos, sin aprobar |" % (FASE, FASE, FASE, FASE))
    s = s[:m.end()] + "\n" + fila + s[m.end():]
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)


if __name__ == "__main__":
    plan()
    plan_pruebas()
    estado()
    fila_en_la_hu()
