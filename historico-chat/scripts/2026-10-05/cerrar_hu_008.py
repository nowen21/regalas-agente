# -*- coding: utf-8 -*-
"""Cierra los documentos de la fase de la HU-008 de EP-025 (2026-10-05).

Se corrió una vez, desde la raíz del estándar, con las pruebas de la fase en
verde y el tablero medido contra el gasto real.
"""
import glob
import io
import os

EPICA = "documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens"
HU = glob.glob(os.path.join(EPICA, "HU-008*"))[0]
FASE = os.path.join(HU, "A-EP-025-HU-008-tablero-en-vivo")
ANALISIS = ("../../../../../historico-chat/resumenes/2026-10-04/pendientes/"
            "119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md")

ESTADO = f'''# Estado de fase · Fase `A-EP-025-HU-008-tablero-en-vivo` (módulo `proyectos/cimiento/core/consumo/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-008-tablero-en-vivo` |
| **Módulo** | `proyectos/cimiento/core/consumo/` |
| **Planteamiento / Épica / HU** | [EP-025](../../epica.md) · [HU-008](../HU-008-el-gasto-se-ve-en-vivo-en-el-tablero.md) |
| **Última actualización** | 2026-10-05 |

## 1. En qué estación va

**Estación actual:** 12, commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ [Análisis 1 del pendiente 119]({ANALISIS}) |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ Acuerdos 2, 5, 7, 9 y 14, y punto 8 del análisis |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-025 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ HU-008, aprobada con el análisis |
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
| Ninguna que necesite señal | |

## 3. Pendiente / preguntas abiertas

Que el usuario mire las gráficas en el navegador (CP-001, paso 4).

## 4. Si se bloqueó

No aplica.
'''

RESULTADO = '''# Resultado de Pruebas · Fase `A-EP-025-HU-008-tablero-en-vivo`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-008-tablero-en-vivo` |
| **HU** | [HU-008](../HU-008-el-gasto-se-ve-en-vivo-en-el-tablero.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-05 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Máquina local, rama `main`, sobre el commit `29a30ad` más los cambios sin guardar; base de pruebas y base real en MariaDB 11.4.9; versión 54.2.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno. Del CP-001 queda un paso para el usuario: mirar las gráficas en el navegador.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `ElTableroSuma` (2 pruebas), `LaPaginaMuestraElGasto` (3) y la página contra la base real | Totales, proyectos, sesiones, enganches y archivos con los números de la muestra; siete días con hoy al final; la cuenta de consulta ve «1.210» y «5.000» y los datos de las gráficas; sin cuenta, manda a entrar. Contra la base real: 200 en 1,24 segundos, con 12 proyectos | Aprobado | EV-01, EV-02 | Ninguno |
| CP-002 | CA-02 | Media | `SeFiltra` (3 pruebas) | Un proyecto: 1 llamada; 7 días: 2, 30 días: 3; `dias=99`, `dias=abc`, `proyecto=x` y `proyecto=9999` se ignoran | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Alta | `SeActualizaSolo` (3 pruebas) y la parte que se recarga contra la base real | Una llamada nueva aparece en la siguiente recarga; la página pide `/gasto/datos/` cada 10 segundos con sus filtros; abrir la página guarda lo del `.jsonl` y recargar no lo repite. Con el gasto real: 0,02 s (hoy), 0,2 s (7 días) y 0,28 s (30 días, 9369 llamadas) | Aprobado | EV-01, EV-02 | Ninguno |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá.

**Qué salió distinto de lo esperado:** el paso 4 del CP-001 pide ver las gráficas. Claude no tiene navegador: se comprobó que la página trae los datos de las gráficas y ApexCharts, no que se dibujen.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | La página y la parte que se recarga con el gasto real | Cliente de Django con una cuenta temporal, dentro de una transacción que se deshace | Los tiempos del CP-003; la cuenta no quedó |
| 2 | Que lo de las HU-001 a HU-007 siga andando | `manage.py test core.consumo core.proyectos core.niveles core.cuentas core.inicio` | Todas pasan |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| RNF-01 | CP-003 | 0,28 s con 30 días de gasto real | Sí |
| RNF-02 | CP-001 | Sin cuenta manda a entrar | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 3 de 3 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 3 de 3 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios pasan en la base de pruebas, y contra la base real la página abre y se recarga rápido.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/consumo/tests_tablero.py` (11 pruebas) |
| EV-02 | Base real | Los tiempos de la sección 2 |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-05 | 3 | 0 | Primera ejecución |
'''

FUNCIONALIDAD = '''# Funcionalidad implementada · Fase `A-EP-025-HU-008-tablero-en-vivo` (módulo `proyectos/cimiento/core/consumo/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-008-tablero-en-vivo` |
| **Módulo** | `proyectos/cimiento/core/consumo/` |
| **Especificación del módulo** | Los CA de la [HU-008](../HU-008-el-gasto-se-ve-en-vivo-en-el-tablero.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-008 (CA-01 a CA-03) |
| **Fecha de cierre** | 2026-10-05 |
| **Versión del estándar al cerrar** | 54.2.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

«Gasto» en el menú muestra el gasto de tokens de todos los proyectos: totales, por proyecto y por día en gráficas, las últimas sesiones, los enganches que más agregan y los archivos que más pesan al leerlos. Se filtra por proyecto y por período y se actualiza cada 10 segundos. Al abrirse lee lo nuevo de los `.jsonl`.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Programa | `proyectos/cimiento/core/consumo/tablero.py`, `proyectos/cimiento/core/consumo/views.py`, `proyectos/cimiento/core/consumo/templates/consumo/tablero.html`, `proyectos/cimiento/core/consumo/templates/consumo/_datos.html`, `proyectos/cimiento/core/consumo/formato.py`, `proyectos/cimiento/core/consumo/templatetags/gasto.py`, `proyectos/cimiento/templates/base.html` | ✅ | CP-001 |
| CA-02 | Programa | `proyectos/cimiento/core/consumo/views.py`, `proyectos/cimiento/core/consumo/tablero.py` | ✅ | CP-002 |
| CA-03 | Programa | `proyectos/cimiento/core/consumo/views.py`, `proyectos/cimiento/core/consumo/guardar.py`, `proyectos/cimiento/core/consumo/templates/consumo/tablero.html` | ✅ | CP-003 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 6 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

`/gasto/`, desde «Gasto» en el menú, con cualquier cuenta. `?proyecto=«id»&dias=1|7|30` filtra.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El gasto por día se agrupa en Python | Agruparlo en MariaDB pide las tablas de zonas horarias, que WAMP no trae | No hace falta: está en `tablero.py` |
| Leer los `.jsonl` solo al abrir la página entera | Leer es lo lento; lo vivo llega por telemetría | No hace falta |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

No aplica.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No hay migración: lee las tablas de la HU-006.
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
cambiar(glob.glob(os.path.join(HU, "HU-008-*.md"))[0], [
    ("| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |\n"
     "|---|---|---|---|---|---|---|\n",
     "| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |\n"
     "|---|---|---|---|---|---|---|\n"
     "| `A-EP-025-HU-008-tablero-en-vivo` | CA-01 a CA-03 | (vacío) | "
     "[plan_trabajo.md](A-EP-025-HU-008-tablero-en-vivo/plan_trabajo.md) | "
     "[plan_pruebas.md](A-EP-025-HU-008-tablero-en-vivo/plan_pruebas.md) | "
     "[resultado_pruebas.md](A-EP-025-HU-008-tablero-en-vivo/resultado_pruebas.md) | Terminada |\n"),
    ("| **Estado** | En curso |", "| **Estado** | Terminada |"),
])
cambiar(os.path.join(EPICA, "epica.md"), [
    ("| El gasto se ve en vivo en el tablero | Must | N/A | N/A | Backlog |",
     "| El gasto se ve en vivo en el tablero | Must | N/A | N/A | Terminada |"),
    ("| 8 | HU-008 | HU-006, HU-007 | Necesita datos y la llegada en vivo | Backlog |",
     "| 8 | HU-008 | HU-006, HU-007 | Necesita datos y la llegada en vivo | Terminada |"),
])
print("HU-008 cerrada en sus documentos")
