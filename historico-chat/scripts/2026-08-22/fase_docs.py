# -*- coding: utf-8 -*-
"""Escribe los seis documentos de una fase corta, sin marcadores sin llenar."""
import io, os


def escribir(p, s):
    io.open(p, "w", encoding="utf-8", newline="").write(s)


def fase(carpeta, datos):
    """datos: dict con las piezas de texto de la fase."""
    d = datos
    n = os.path.basename(carpeta)
    arriba = "../" * (carpeta.count("/") + 1)

    escribir(os.path.join(carpeta, "plan_trabajo.md"), f"""# Plan de Trabajo — Fase {n}

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden y sobre qué archivos. El requisito vive en [{d['hu_id']}]({d['hu_rel']}); las pruebas, en el [plan_pruebas.md](plan_pruebas.md).

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `{n}` |
| **Épica** | [{d['ep_id']}](../../epica.md) |
| **HU** | [{d['hu_id']}]({d['hu_rel']}), una sola |
| **Módulo** | {d['modulo']} |
| **Fecha apertura** | 2026-08-22 |

**ORIGEN** ([`13·DOC12`]({arriba}base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): {d['origen']}

**De dónde sale:** {d['de_donde']}

**CA que cubre:** {d['ca']}

## 1. Objetivo y alcance

**Objetivo:** {d['objetivo']}

{d['contexto']}

**Fuera de alcance:**

{d['fuera']}

## 2. Análisis previo, línea base verificada

{d['linea_base']}

### 2.1 Archivos que se crean o modifican

{d['archivos']}

### 2.2 Las trece preguntas, en corto

{d['trece']}

### 2.3 Dudas por resolver

{d['dudas']}

## 3. Tareas

{d['tareas']}

## 4. Riesgos

{d['riesgos']}
""")

    escribir(os.path.join(carpeta, "plan_pruebas.md"), f"""# Plan de Pruebas — Fase {n}

**Para qué sirve este documento.** Dice con qué se comprueba que la fase quedó bien antes de cerrarla. Lo ejecutado está en [resultado_pruebas.md](resultado_pruebas.md).

## 0. Qué se prueba, y qué no

{d['que_se_prueba']}

## 1. Alcance de ejecución ([`02·F5`]({arriba}base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md))

{d['alcance']}

## 2. Trazabilidad criterio a caso

{d['trazabilidad']}

## 3. Los casos

{d['casos']}

## 4. Criterio de cierre

La fase cierra con todos los casos en verde. Un caso rojo se corrige antes de publicar, no se anota como pendiente.
""")

    escribir(os.path.join(carpeta, "resultado_pruebas.md"), f"""# Resultado de Pruebas — Fase {n}

**Para qué sirve este documento.** Dice qué se ejecutó, con qué y qué dio. El plan está en [plan_pruebas.md](plan_pruebas.md).

## 0. Veredicto

**{d['veredicto']}** Ejecutado el 2026-08-22 contra la versión {d['version']}, en Windows con Python 3.

## 1. Caso por caso

{d['resultados']}

## 2. Lo que costó llegar al verde

{d['costo']}

## 3. Lo que no se probó

{d['no_probado']}
""")

    escribir(os.path.join(carpeta, "funcionalidad_implementada.md"), f"""# Funcionalidad implementada — Fase {n}

**Para qué sirve este documento.** Dice qué quedó hecho al cerrar la fase, con la trazabilidad de cada ítem hasta el archivo donde vive.

## 0. Qué quedó, en una frase

{d['quedo']}

## 1. Trazabilidad ([`13·DOC11`]({arriba}base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))

{d['trazabilidad_final']}

## 2. Lo que cambia para un proyecto que hereda

{d['cambia']}

## 3. Lo que queda abierto

{d['abierto']}
""")

    escribir(os.path.join(carpeta, "estado-fase.md"), f"""# Estado de fase — Fase {n}

**Para qué sirve este documento.** Dice en qué estación va la fase y qué la tiene detenida, para que una sesión nueva siga desde ahí sin releer la conversación.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `{n}` |
| **Módulo** | {d['modulo']} |
| **Épica / HU / origen** | [{d['ep_id']}](../../epica.md), [{d['hu_id']}]({d['hu_rel']}), {d['de_donde']} |
| **Última actualización** | 2026-08-22 |

## 1. En qué estación va

**Estación actual:** 8, cierre documental. **Última puerta pasada:** 7, veredicto **{d['veredicto_corto']}**.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 «haga los dos para que salga de una de eso», 2026-08-22 | ☑ |
| 3 | Diseño del plan detallado | [plan_trabajo](plan_trabajo.md) y [plan_pruebas](plan_pruebas.md) | ☑ |
| 4 | Pausa y presentación | 👤 se reporta con el resultado | ☑ |
| 5 | Aprobación del plan detallado | 👤 en la orden que disparó el trabajo | ☑ |
| 6 | Ejecución continua | {d['n_tareas']} tareas | ☑ |
| 7 | Pruebas | [resultado_pruebas](resultado_pruebas.md) | ☑ |
| 8 | Cierre documental | [funcionalidad_implementada](funcionalidad_implementada.md) | ☑ |

**Hechas:** {d['n_tareas']} de {d['n_tareas']}. **Bloqueadas:** ninguna.

## 2. Qué la tiene detenida

**Nada.** La fase está cerrada.

## 3. Lo que una sesión nueva tiene que saber

{d['saber']}
""")

    escribir(os.path.join(carpeta, "README.md"), f"""# {n}

Contenido inmediato de esta carpeta.

| Qué | De qué se trata |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Qué se hizo, en qué orden y sobre qué archivos |
| [plan_pruebas.md](plan_pruebas.md) | Con qué casos se comprueba |
| [resultado_pruebas.md](resultado_pruebas.md) | Qué se ejecutó, qué salió y el veredicto |
| [estado-fase.md](estado-fase.md) | En qué estación va y qué la tiene detenida |
| [funcionalidad_implementada.md](funcionalidad_implementada.md) | Qué quedó hecho al final |

De dónde sale: {d['de_donde']}

{d['resumen']}

**Estado:** cerrada el 2026-08-22 (v{d['version']}). Veredicto **{d['veredicto_corto']}**.
""")
    print("escrita", n)
