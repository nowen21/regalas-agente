# -*- coding: utf-8 -*-
"""Cierra los documentos de la fase de la HU-007 de EP-025 (2026-10-05).

Se corrió una vez, desde la raíz del estándar, con las pruebas de la fase en
verde y el envío manual a Cimiento prendido.
"""
import glob
import io
import os

EPICA = "documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens"
HU = glob.glob(os.path.join(EPICA, "HU-007*"))[0]
FASE = os.path.join(HU, "A-EP-025-HU-007-recepcion-de-la-telemetria")
ANALISIS = ("../../../../../historico-chat/resumenes/2026-10-04/pendientes/"
            "119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md")

ESTADO = f'''# Estado de fase · Fase `A-EP-025-HU-007-recepcion-de-la-telemetria` (módulo `proyectos/cimiento/core/consumo/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-007-recepcion-de-la-telemetria` |
| **Módulo** | `proyectos/cimiento/core/consumo/`, `proyectos/cimiento/core/herramientas/` |
| **Planteamiento / Épica / HU** | [EP-025](../../epica.md) · [HU-007](../HU-007-el-gasto-llega-a-cimiento-en-vivo.md) |
| **Última actualización** | 2026-10-05 |

## 1. En qué estación va

**Estación actual:** 12, commit. **Última puerta pasada:** 11.

| # | Estación | Puerta | Estado |
|---|---|---|---|
| 1 | Explorador · análisis | contexto entendido | ☑ [Análisis 1 del pendiente 119]({ANALISIS}) |
| 2 | Proponente · alcance | 👤 alcance aprobado | ☑ Acuerdo 9 y punto 7 del análisis |
| 3 | Escritor de épica | 👤 épica aprobada | ☑ EP-025 |
| 4 | Escritor de historia | 👤 HUs aprobadas | ☑ HU-007, aprobada con el análisis |
| 5 | Escritor de especificación | 👤 especificación aprobada | N/A: la especificación son los CA |
| 6 | Diseñador | diseño coherente | ☑ |
| 7 | Planificador de tareas | 👤 plan + pruebas aprobados | ☑ Aprobados por el análisis, el 2026-10-04 |
| 8 | Implementador | implementado + pruebas verdes | ☑ Las 7 tareas |
| 9 | Verificador | trazabilidad sin faltantes | ☑ Sin fallas |
| 10 | Crítico | sin hallazgos graves | ☑ Ninguno |
| 11 | Cierre documental + señales | docs y señales al día | ☑ Resultado, funcionalidad, HU y épica |
| 12 | Commit | 👤 autorizado | ☐ |
| 13 | Publicación / despliegue | 👤 autorizado | ☐ |

## 1.2 Avance de las tareas del plan

**Hechas:** 7 de 7. **Bloqueadas:** ninguna.

## 1.1 Veredicto de las pruebas

| Campo | Valor |
|---|---|
| **Concepto** | Cumple |
| **CA cumplidos** | 4 de 4 |
| **Defectos abiertos aceptados** | Ninguno |
| **Fuente** | `resultado_pruebas.md` |

## 2. Decisiones y señales generadas  ·  `13·DOC5`

| Decisión / aprendizaje | Señal registrada (id/enlace) |
|---|---|
| La telemetría no dice la carpeta del proyecto: sale de la sesión | En `guardar.py` y en la HU |

## 3. Pendiente / preguntas abiertas

Ninguna.

## 4. Si se bloqueó

No aplica.
'''

RESULTADO = '''# Resultado de Pruebas · Fase `A-EP-025-HU-007-recepcion-de-la-telemetria`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-007-recepcion-de-la-telemetria` |
| **HU** | [HU-007](../HU-007-el-gasto-llega-a-cimiento-en-vivo.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-05 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Máquina local, rama `main`, sobre el commit `29a30ad` más los cambios sin guardar; base de pruebas y base real en MariaDB 11.4.9; versión 54.2.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `ElEnvioSeLee` (3 pruebas), `UnaLlamadaLlegaYQuedaGuardada` (3) y un envío a Cimiento prendido en el puerto 8001 | La llamada con modelo, tokens y solicitud, y el archivo con ruta y 300 bytes, en la base con su proyecto; comprimido con gzip también; el envío manual respondió 200 con `{}` y quedó en «Estándar de Agente», y esa fila de prueba se borró | Aprobado | EV-01, EV-02 | Ninguno |
| CP-002 | CA-02 | Media | `LoQueNoValeNoSeGuarda` (5 pruebas) | Otra máquina: 403; JSON roto: 400; sesión sin proyecto o con `../`: 200 y nada guardado; `GET`: 405 | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Alta | `LaMismaLlamadaCuentaUnaVez` (4 pruebas) | Una llamada en los dos órdenes, con el `message.id` del `.jsonl`; el mismo envío dos veces deja una llamada y un archivo; el `.jsonl` deja el archivo en 70 caracteres | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-04 | Media | `ActivarLaTelemetria` (6 pruebas) y la configuración real | Las seis variables, con `http://127.0.0.1:8015/v1/logs`; lo del usuario sigue; otra vez no cambia nada; en simulación no escribe; sin puerto, el 8000; JSON roto no se toca. En `~/.claude/settings.json` quedaron las seis, y la simulación del instalador dice «ya estaba activa» | Aprobado | EV-01, EV-03 | Ninguno |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** el envío manual fue al 8001, donde se había levantado Cimiento a mano; la configuración apunta al 8015, el `PUERTO` del `.env`.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | La migración en la base real | `manage.py preparar_base` | Sin migraciones pendientes |
| 2 | Que lo de la HU-006 siga andando | `manage.py test core.consumo` | 27 pruebas, todas pasan |
| 3 | Las pruebas del instalador que tocó la fase | `ActivarLaTelemetria`, `LaLecturaDelConsumoQuedaProgramada`, `PrepararCimiento` | 18 pruebas, todas pasan |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| CA-04 | CP-004 | Aprobado | Sí |
| RNF-01 | CP-002 | Solo desde `127.0.0.1` o `::1` | Sí |
| RNF-02 | CP-001 | `test_no_guarda_texto` | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 4 de 4 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 4 de 4 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los cuatro criterios pasan en la base de pruebas, y un envío real llegó a Cimiento prendido.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/consumo/tests_telemetria.py` (15 pruebas) y `proyectos/cimiento/core/herramientas/tests_instalacion.py` |
| EV-02 | Base real | El envío manual, guardado y borrado |
| EV-03 | Configuración | El bloque `env` de `~/.claude/settings.json` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-05 | 4 | 0 | Primera ejecución |
'''

FUNCIONALIDAD = '''# Funcionalidad implementada · Fase `A-EP-025-HU-007-recepcion-de-la-telemetria` (módulo `proyectos/cimiento/core/consumo/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-007-recepcion-de-la-telemetria` |
| **Módulo** | `proyectos/cimiento/core/consumo/`, `proyectos/cimiento/core/herramientas/` |
| **Especificación del módulo** | Los CA de la [HU-007](../HU-007-el-gasto-llega-a-cimiento-en-vivo.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-007 (CA-01 a CA-04) |
| **Fecha de cierre** | 2026-10-05 |
| **Versión del estándar al cerrar** | 54.2.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Claude Code manda cada llamada y cada archivo leído a Cimiento, en `/v1/logs`, a los 5 segundos. Cimiento los guarda en las tablas de la HU-006, con su proyecto, y una llamada que llega también por el `.jsonl` queda una sola vez. La instalación del estándar activa la telemetría en la configuración del usuario.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Programa | `proyectos/cimiento/core/consumo/telemetria.py`, `proyectos/cimiento/core/consumo/views.py`, `proyectos/cimiento/core/consumo/urls.py`, `proyectos/cimiento/core/consumo/guardar.py`, `proyectos/cimiento/config/urls.py` | ✅ | CP-001 |
| CA-02 | Programa | `proyectos/cimiento/core/consumo/views.py`, `proyectos/cimiento/core/consumo/guardar.py` | ✅ | CP-002 |
| CA-03 | Programa | `proyectos/cimiento/core/consumo/guardar.py`, `proyectos/cimiento/core/consumo/models.py`, `proyectos/cimiento/core/consumo/lector.py`, `proyectos/cimiento/core/consumo/migrations/0002_llamada_solicitud.py` | ✅ | CP-003 |
| CA-04 | Programa | `proyectos/cimiento/core/herramientas/instalar.py`, `validadores/instalar.py` | ✅ | CP-004 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 7 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Levantar Cimiento con `python manage.py runserver`, sin número: escucha en el `PUERTO` del `.env`, que es adonde Claude Code manda. Vale desde la siguiente sesión de Claude Code que se abra.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El proyecto sale de la sesión, buscando su `.jsonl` | La telemetría no trae la carpeta, y `OTEL_RESOURCE_ATTRIBUTES` es de toda la máquina | No hace falta: está en `guardar.py` |
| La llamada por telemetría se guarda con la solicitud como mensaje, y el `.jsonl` le pone el suyo | Así se ve en vivo sin duplicar | No hace falta: está en `guardar.py` |
| Responder `{}` aunque se descarte | Un error haría reintentar lo que nunca va a entrar | No hace falta |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

No aplica.

## 8. Despliegue, si aplica  ·  `13·DOC4`

La instalación del estándar activa la telemetría en `~/.claude/settings.json`. Para quitarla, borrar de su `env` las claves `CLAUDE_CODE_ENABLE_TELEMETRY` y `OTEL_*`.
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
     "Las 7 tareas quedaron hechas el 2026-10-05, con la versión 54.2.0. Detalle en "
     "[`funcionalidad_implementada.md`](funcionalidad_implementada.md).\n\n**Hallazgos al ejecutar:** ninguno."),
])
cambiar(glob.glob(os.path.join(HU, "HU-007-*.md"))[0], [
    ("| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |\n"
     "|---|---|---|---|---|---|---|\n",
     "| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |\n"
     "|---|---|---|---|---|---|---|\n"
     "| `A-EP-025-HU-007-recepcion-de-la-telemetria` | CA-01 a CA-04 | (vacío) | "
     "[plan_trabajo.md](A-EP-025-HU-007-recepcion-de-la-telemetria/plan_trabajo.md) | "
     "[plan_pruebas.md](A-EP-025-HU-007-recepcion-de-la-telemetria/plan_pruebas.md) | "
     "[resultado_pruebas.md](A-EP-025-HU-007-recepcion-de-la-telemetria/resultado_pruebas.md) | Terminada |\n"),
    ("| **Estado** | En curso |", "| **Estado** | Terminada |"),
])
cambiar(os.path.join(EPICA, "epica.md"), [
    ("| El gasto llega a Cimiento en vivo | Should | N/A | N/A | Backlog |",
     "| El gasto llega a Cimiento en vivo | Should | N/A | N/A | Terminada |"),
    ("| 7 | HU-007 | HU-006 | Guarda en las mismas tablas | Backlog |",
     "| 7 | HU-007 | HU-006 | Guarda en las mismas tablas | Terminada |"),
])
print("HU-007 cerrada en sus documentos")
