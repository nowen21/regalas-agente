# -*- coding: utf-8 -*-
"""Cierra los documentos de la fase de la HU-010 de EP-025, y la épica (2026-10-05).

Se corrió una vez, desde la raíz del estándar, con las pruebas de la fase en
verde y los `.jsonl` vueltos a leer con los niveles nuevos.
"""
import glob
import io
import os

EPICA = "documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens"
HU = glob.glob(os.path.join(EPICA, "HU-010*"))[0]
FASE = os.path.join(HU, "A-EP-025-HU-010-segunda-tanda")
ANALISIS = ("../../../../../historico-chat/resumenes/2026-10-04/pendientes/"
            "119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md")
MODULO = "`proyectos/cimiento/core/consumo/`, `proyectos/cimiento/core/herramientas/recuperar.py`"

ESTADO = f'''# Estado de fase · Fase `A-EP-025-HU-010-segunda-tanda` (módulo `proyectos/cimiento/core/consumo/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-010-segunda-tanda` |
| **Módulo** | {MODULO} |
| **Planteamiento / Épica / HU** | [EP-025](../../epica.md) · [HU-010](../HU-010-el-gasto-se-ve-por-los-demas-niveles.md) |
| **Última actualización** | 2026-10-05 |

## 1. En qué estación va

**Estación actual:** 12, commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ [Análisis 1 del pendiente 119]({ANALISIS}) |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ Acuerdo 7 y punto 10 del análisis |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-025 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ HU-010, aprobada con el análisis |
| 5 | Escritor de especificación | 👤 especificación aprobada | N/A: la especificación son los CA |
| 6 | Diseñador | diseño coherente | ☑ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ Aprobados por el análisis, el 2026-10-04 |
| 8 | Implementador | implementado + pruebas verdes | ☑ Las 6 tareas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ Sin fallas |
| 10 | Crítico | sin hallazgos graves | ☑ Ninguno |
| 11 | Cierre documental + señales | docs y señales al día | ☑ Resultado, funcionalidad, HU y épica |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

## 1.2 Avance de las tareas del plan

**Hechas:** 6 de 6. **Bloqueadas:** ninguna.

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
| El trabajo de un turno sale de las rutas que tocó, no del aviso de acuerdos | En `trabajo.py` |

## 3. Pendiente / preguntas abiertas

Ninguna.

## 4. Si se bloqueó

No aplica.
'''

RESULTADO = '''# Resultado de Pruebas · Fase `A-EP-025-HU-010-segunda-tanda`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-010-segunda-tanda` |
| **HU** | [HU-010](../HU-010-el-gasto-se-ve-por-los-demas-niveles.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-05 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Máquina local, rama `main`, sobre el commit `29a30ad` más los cambios sin guardar; base de pruebas y base real en MariaDB 11.4.9; versión 54.2.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `ElTrabajoSaleDeLasRutas` (2), `LaPalabraClaveEsLaDeLaLista` (1) y `ElGastoQuedaPorMensajePalabraYTrabajo` (4) | «Hágalo» con la fase, «Analicemos» con «análisis 2 del pendiente 119» y un mensaje sin palabra ni trabajo; cada llamada con su mensaje; el texto no queda en la base; un turno leído en dos veces sigue con su mensaje; leer otra vez no duplica | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Media | `ElGastoQuedaPorHerramientaYAgente` (3) | Edit, Bash y Read con el tamaño de su resultado; el auxiliar con «Explore» y sin mensaje, y su tarea no cuenta como mensaje; la telemetría guarda Bash con 300 y une la llamada al mensaje «p-2» | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Media | `ElTableroMuestraLosSieteNiveles` (2) y la base real | Palabra, trabajo, modelo, tipo de token, herramienta, contexto y mensajes con los números de la muestra; la página trae las ocho secciones. Con el gasto real: 0,33 s (hoy), 0,35 s (7 días), 0,58 s (30 días) | Aprobado | EV-01, EV-02 | Ninguno |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá.

**Qué salió distinto de lo esperado:** la prueba de la HU-006 que exigía no leer `subagents/` pasó a exigir que se lean, como pide esta HU.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Los niveles nuevos con el gasto real | Migración `0003`; se borró el avance de lectura y se corrió `leer_consumo` (1 min 38 s) | 2988 mensajes, 13 160 usos de herramientas, 880 llamadas de auxiliares (general-purpose 738, Explore 112, claude-code-guide 30); 1851 mensajes sin palabra clave, casi todos de antes de `01·C28` |
| 2 | Que lo de las HU-006 a HU-009 siga andando | `manage.py test core.consumo core.proyectos` y `core.enganches.tests_limites` | Todas pasan |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| RNF-01 | CP-003 | 0,58 s con 30 días de gasto real | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 3 de 3 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 3 de 3 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios pasan en la base de pruebas, y con el gasto real los niveles se llenan y el tablero responde en menos de un segundo.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/consumo/tests_segunda_tanda.py` (12 pruebas) |
| EV-02 | Base real | Los conteos y tiempos de las secciones 2 y 3 |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-05 | 3 | 0 | Primera ejecución |
'''

FUNCIONALIDAD = f'''# Funcionalidad implementada · Fase `A-EP-025-HU-010-segunda-tanda` (módulo `proyectos/cimiento/core/consumo/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-010-segunda-tanda` |
| **Módulo** | {MODULO} |
| **Especificación del módulo** | Los CA de la [HU-010](../HU-010-el-gasto-se-ve-por-los-demas-niveles.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-010 (CA-01 a CA-03) |
| **Fecha de cierre** | 2026-10-05 |
| **Versión del estándar al cerrar** | 54.2.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

El gasto queda también por mensaje del usuario, con su palabra clave y el trabajo que tocó su turno; por herramienta; por agente auxiliar, cuyos registros ahora se leen; por modelo y por tipo de token. «Gasto» suma esas secciones, lo que llena el contexto y los últimos mensajes.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Programa | `proyectos/cimiento/core/consumo/lector.py`, `proyectos/cimiento/core/consumo/trabajo.py`, `proyectos/cimiento/core/herramientas/recuperar.py`, `proyectos/cimiento/core/consumo/models.py`, `proyectos/cimiento/core/consumo/migrations/0003_segunda_tanda.py`, `proyectos/cimiento/core/consumo/guardar.py` | ✅ | CP-001 |
| CA-02 | Programa | `proyectos/cimiento/core/consumo/lector.py`, `proyectos/cimiento/core/consumo/guardar.py`, `proyectos/cimiento/core/consumo/telemetria.py`, `proyectos/cimiento/core/consumo/views.py` | ✅ | CP-002 |
| CA-03 | Programa | `proyectos/cimiento/core/consumo/tablero.py`, `proyectos/cimiento/core/consumo/templates/consumo/_datos.html` | ✅ | CP-003 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 6 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): `proyectos/cimiento/core/consumo/tests.py` se declaró durante la fase, al ver que su prueba de la HU-006 pedía lo contrario de esta HU; `proyectos/cimiento/core/consumo/views.py` pasa las herramientas de la telemetría al guardado.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

«Gasto» en el menú, con los mismos filtros de la HU-008.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El trabajo sale de las rutas tocadas en el turno | El aviso de acuerdos nombra fases de otras sesiones | No hace falta: está en `trabajo.py` |
| El avance de lectura guarda el mensaje en curso | Un turno puede quedar partido entre dos lecturas | No hace falta: está en `guardar.py` |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

No aplica.

## 8. Despliegue, si aplica  ·  `13·DOC4`

`preparar_base` aplica la migración `0003`. Para llenar lo ya guardado: borrar el avance de lectura y correr `leer_consumo`.
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
     "Las 6 tareas quedaron hechas el 2026-10-05, con la versión 54.2.0. Detalle en "
     "[`funcionalidad_implementada.md`](funcionalidad_implementada.md).\n\n**Hallazgos al ejecutar:** ninguno."),
])
cambiar(glob.glob(os.path.join(HU, "HU-010-*.md"))[0], [
    ("| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |\n"
     "|---|---|---|---|---|---|---|\n",
     "| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |\n"
     "|---|---|---|---|---|---|---|\n"
     "| `A-EP-025-HU-010-segunda-tanda` | CA-01 a CA-03 | (vacío) | "
     "[plan_trabajo.md](A-EP-025-HU-010-segunda-tanda/plan_trabajo.md) | "
     "[plan_pruebas.md](A-EP-025-HU-010-segunda-tanda/plan_pruebas.md) | "
     "[resultado_pruebas.md](A-EP-025-HU-010-segunda-tanda/resultado_pruebas.md) | Terminada |\n"),
    ("| **Estado** | En curso |", "| **Estado** | Terminada |"),
])
cambiar(os.path.join(EPICA, "epica.md"), [
    ("| El gasto se ve por los demás niveles | Could | N/A | N/A | Backlog |",
     "| El gasto se ve por los demás niveles | Could | N/A | N/A | Terminada |"),
    ("| 10 | HU-010 | HU-008 | Amplía lo que ya funciona | Backlog |",
     "| 10 | HU-010 | HU-008 | Amplía lo que ya funciona | Terminada |"),
    ("| **Estado** | En curso |", "| **Estado** | Terminada |"),
    ("- [ ] **CAE-01**", "- [x] **CAE-01**"),
    ("- [ ] **CAE-02**", "- [x] **CAE-02**"),
    ("- [ ] **CAE-03**", "- [x] **CAE-03**"),
])
print("HU-010 y EP-025 cerradas en sus documentos")
