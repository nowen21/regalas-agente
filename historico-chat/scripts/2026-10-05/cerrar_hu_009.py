# -*- coding: utf-8 -*-
"""Cierra los documentos de la fase de la HU-009 de EP-025 (2026-10-05).

Se corrió una vez, desde la raíz del estándar, con las pruebas de la fase en
verde y el aviso probado con un límite bajo en la base real.
"""
import glob
import io
import os

EPICA = "documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens"
HU = glob.glob(os.path.join(EPICA, "HU-009*"))[0]
FASE = os.path.join(HU, "A-EP-025-HU-009-avisos-por-limite")
ANALISIS = ("../../../../../historico-chat/resumenes/2026-10-04/pendientes/"
            "119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md")
MODULO = ("`proyectos/cimiento/core/enganches/`, `proyectos/cimiento/core/consumo/lector.py`, "
          "`proyectos/cimiento/core/proyectos/`, `adaptadores/claude-code/hook_presupuesto.py`")

ESTADO = f'''# Estado de fase · Fase `A-EP-025-HU-009-avisos-por-limite` (módulo `proyectos/cimiento/core/enganches/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-009-avisos-por-limite` |
| **Módulo** | {MODULO} |
| **Planteamiento / Épica / HU** | [EP-025](../../epica.md) · [HU-009](../HU-009-se-avisa-cuando-un-enganche-o-un-archivo-pesa-demasiado.md) |
| **Última actualización** | 2026-10-05 |

## 1. En qué estación va

**Estación actual:** 12, commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ [Análisis 1 del pendiente 119]({ANALISIS}) |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ Acuerdo 10 y punto 9 del análisis |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-025 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ HU-009, aprobada con el análisis |
| 5 | Escritor de especificación | 👤 especificación aprobada | N/A: la especificación son los CA |
| 6 | Diseñador | diseño coherente | ☑ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ Aprobados por el análisis, el 2026-10-04 |
| 8 | Implementador | implementado + pruebas verdes | ☑ Las 5 tareas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ Sin fallas |
| 10 | Crítico | sin hallazgos graves | ☑ D-01 corregido dentro de la fase |
| 11 | Cierre documental + señales | docs y señales al día | ☑ Resultado, funcionalidad, HU y épica |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

## 1.2 Avance de las tareas del plan

**Hechas:** 5 de 5. **Bloqueadas:** ninguna.

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | Cumple |
| **CA cumplidos** | 3 de 3 |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | `resultado_pruebas.md` |

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| En `UserPromptSubmit` y `SessionStart`, el texto plano de un enganche también llega al modelo; el lector no lo contaba | En `lector.py` y en sus pruebas |

## 3. Pendiente / preguntas abiertas

Ninguna.

## 4. Si se bloqueó

No aplica.
'''

RESULTADO = '''# Resultado de Pruebas · Fase `A-EP-025-HU-009-avisos-por-limite`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-009-avisos-por-limite` |
| **HU** | [HU-009](../HU-009-se-avisa-cuando-un-enganche-o-un-archivo-pesa-demasiado.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-05 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Máquina local, rama `main`, sobre el commit `29a30ad` más los cambios sin guardar; base real en MariaDB 11.4.9; versión 54.2.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `LoQuePasaElLimiteSeAvisa` (6 pruebas) | El turno anterior, con el mensaje siguiente escrito o sin escribir; solo lo que pasó el límite, y lo que está justo en él no; un mismo enganche dos veces sale una, con «(2 veces)»; el enganche entero avisa y sale con 0; sin transcripción, sale con 0 y callado | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `CadaExcesoSeAvisaUnaVez` | El turno siguiente sin excesos no avisa | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Media | `LosLimitesSonLosDelProyecto` (3 pruebas) y el límite por enganche de este proyecto en 100, en la base real | Los del registro; sin registro o sin base, 2000 y 10 000. Con 100 en la base real, el enganche avisó con «el límite del proyecto es 100» y salió con 0; el límite volvió a 2000 | Aprobado | EV-01, EV-02 | D-01 |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá.

**Qué salió distinto de lo esperado:** el paso manual mostró D-01.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que lo de la HU-006 y el freno sigan andando | `manage.py test core.consumo core.proyectos` y `ElNivelDeLaRegla`, `SinBaseNoSeModifica` | Todas pasan |
| 2 | Los enganches guardados, leídos otra vez con el lector corregido | Se borraron los enganches y el avance de lectura, que salen de los `.jsonl`, y se corrió `leer_consumo` | Llamadas de 12 890 a 13 111 (las nuevas de la sesión, sin duplicar); enganches de 3850 a 5823 |

## 4. Defectos encontrados

| ID | Caso | Qué pasó | Esperado | Obtenido | Estado |
|---|---|---|---|---|---|
| D-01 | CP-003 | El aviso nombraba «UserPromptSubmit» y no contaba el enganche de las señales | El nombre de cada enganche, y todo lo que llega al modelo | Los contextos de `UserPromptSubmit` no tienen `hook_success` hermano, y el texto plano de un enganche en `UserPromptSubmit` o `SessionStart` no se contaba | Corregido en `lector.py`: el nombre sale del título entre corchetes, y el texto plano de esos dos momentos cuenta. Dos pruebas en `ElLectorVeTodosLosEnganches` |

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| RNF-01 | CP-003 | `LimitesDelProyecto` con PyMySQL, sin Django | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 3 de 3 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 3 de 3 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios pasan, y el aviso llegó con el límite de la base real.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/enganches/tests_limites.py` (12 pruebas) |
| EV-02 | Base real | El aviso con el límite 100, devuelto a 2000 |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-05 | 3 | 0 | Primera ejecución |
'''

FUNCIONALIDAD = f'''# Funcionalidad implementada · Fase `A-EP-025-HU-009-avisos-por-limite` (módulo `proyectos/cimiento/core/enganches/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-009-avisos-por-limite` |
| **Módulo** | {MODULO} |
| **Especificación del módulo** | Los CA de la [HU-009](../HU-009-se-avisa-cuando-un-enganche-o-un-archivo-pesa-demasiado.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-009 (CA-01 a CA-03) |
| **Fecha de cierre** | 2026-10-05 |
| **Versión del estándar al cerrar** | 54.2.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Con cada mensaje, el agente recibe un aviso si en el turno anterior un enganche agregó, o un archivo leído ocupó, más tokens que el límite de su proyecto. Cada exceso se avisa una vez y no detiene nada. De paso, el lector cuenta también lo que un enganche escribe como texto plano y nombra cada enganche por su título.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Programa | `proyectos/cimiento/core/consumo/lector.py`, `proyectos/cimiento/core/enganches/presupuesto.py`, `adaptadores/claude-code/hook_presupuesto.py` | ✅ | CP-001 |
| CA-02 | Programa | `proyectos/cimiento/core/consumo/lector.py` | ✅ | CP-002 |
| CA-03 | Programa | `proyectos/cimiento/core/proyectos/limites.py`, `proyectos/cimiento/core/proyectos/models.py`, `proyectos/cimiento/core/enganches/niveles.py` | ✅ | CP-003 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 5 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Llega solo, con cada mensaje, por `hook_presupuesto.py --modo aviso`. Los límites se cambian en Cimiento, en «Proyectos», «Editar».

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El mensaje que se está mandando es el último si después de él no hay respuesta del agente | El texto del mensaje no sirve para reconocerlo: Claude Code le suma el contexto del editor | No hace falta: está en `turno_anterior` |
| El texto plano de un enganche cuenta solo en `UserPromptSubmit` y `SessionStart` | En `Stop` y `PostToolUse` ese texto no llega al modelo | No hace falta: está en `lector.py` |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

No aplica.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Ninguno: el enganche ya estaba conectado en `UserPromptSubmit`.
'''


def escribir(ruta, texto):
    with io.open(ruta, "w", encoding="utf-8", newline="") as f:
        f.write(texto)


def cambiar(ruta, pares):
    texto = io.open(ruta, encoding="utf-8").read()
    for viejo, nuevo in pares:
        assert viejo in texto, (ruta, viejo[:70])
        texto = texto.replace(viejo, nuevo, 1)
    escribir(ruta, texto)


escribir(os.path.join(FASE, "estado-fase.md"), ESTADO)
escribir(os.path.join(FASE, "resultado_pruebas.md"), RESULTADO)
escribir(os.path.join(FASE, "funcionalidad_implementada.md"), FUNCIONALIDAD)
cambiar(os.path.join(FASE, "plan_trabajo.md"), [
    ("«Se llena al cerrar la fase.»",
     "Las 5 tareas quedaron hechas el 2026-10-05, con la versión 54.2.0. Detalle en "
     "[`funcionalidad_implementada.md`](funcionalidad_implementada.md).\n\n**Hallazgos al ejecutar:** D-01, "
     "corregido dentro de `lector.py`, que el plan declara."),
])
cambiar(glob.glob(os.path.join(HU, "HU-009-*.md"))[0], [
    ("| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |\n"
     "|---|---|---|---|---|---|---|\n",
     "| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |\n"
     "|---|---|---|---|---|---|---|\n"
     "| `A-EP-025-HU-009-avisos-por-limite` | CA-01 a CA-03 | (vacío) | "
     "[plan_trabajo.md](A-EP-025-HU-009-avisos-por-limite/plan_trabajo.md) | "
     "[plan_pruebas.md](A-EP-025-HU-009-avisos-por-limite/plan_pruebas.md) | "
     "[resultado_pruebas.md](A-EP-025-HU-009-avisos-por-limite/resultado_pruebas.md) | Terminada |\n"),
    ("| **Estado** | En curso |", "| **Estado** | Terminada |"),
])
cambiar(os.path.join(EPICA, "epica.md"), [
    ("| Se avisa cuando un enganche o un archivo pesa demasiado | Should | N/A | N/A | Backlog |",
     "| Se avisa cuando un enganche o un archivo pesa demasiado | Should | N/A | N/A | Terminada |"),
    ("| 9 | HU-009 | HU-003, HU-006 | Usa los límites del registro y los datos guardados | Backlog |",
     "| 9 | HU-009 | HU-003, HU-006 | Usa los límites del registro y los datos guardados | Terminada |"),
])
print("HU-009 cerrada en sus documentos")
