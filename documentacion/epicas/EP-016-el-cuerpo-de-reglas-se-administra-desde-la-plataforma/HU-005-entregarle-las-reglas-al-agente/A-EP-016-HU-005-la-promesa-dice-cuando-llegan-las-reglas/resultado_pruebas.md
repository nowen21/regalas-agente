# Resultado de Pruebas · Fase `A-EP-016-HU-005-la-promesa-dice-cuando-llegan-las-reglas`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra qué se ejecutó de verdad y con qué resultado, y de ahí sale el **veredicto** de la fase: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección *Qué se probó* del `funcionalidad_implementada.md`. El diseño de los casos vive en el `plan_pruebas.md` de esta misma fase, que no se modifica al ejecutar: se aprobó antes y así se queda.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-016-HU-005-la-promesa-dice-cuando-llegan-las-reglas` |
| **HU** | [HU-005](../HU-005-entregarle-las-reglas-al-agente.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-09-28 |
| **Ejecutado por** | El agente |
| **Ambiente y versión** | El repositorio del estándar, rama `main`, versión 39.4.0 sin commit |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 0 | 0 | 0 |

## 2. Ejecución caso por caso

**CA-01 · CP-001, que la promesa diga cuándo llegan las reglas**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Buscar «al abrir» y «reglas» en el mismo renglón, en `cvds/` y EP-016, sin las fases cerradas | Ninguno que prometa las reglas al abrir | Dos renglones, y los dos dicen lo correcto: los enganches al abrir sesión, con cada mensaje y al cerrar, y «Al abrir la sesión no se entregan» |
| 2 | Leer la ficha de `F-009` y la fila de `RF-09` | Con cada mensaje las de la tarea, y enteras cuando se piden | Lo dicen, con el tope de 10.000 caracteres como razón |
| 3 | Leer HU-005 | Narrativa, título del CA-01 y contexto de acuerdo | De acuerdo; el CA-01 se llama «Cuando se piden, salen las reglas con su texto» |
| 4 | Correr `python validadores/validar.py estandar` | Sin incumplimientos | `OK: sin incumplimientos` |

**Encontrado al ejecutar:** la búsqueda del paso 1 dio cinco promesas más que la lista del plan. Tres estaban en archivos que el plan no nombraba, `cvds/planificacion/acta-de-constitucion.md` y `cvds/diseno/README.md`. Son del mismo módulo, los cubre la T-05 y el riesgo B-01 del plan los anticipaba. Se corrigieron en esta fase.

## 3. Veredicto

| CA | Veredicto |
|---|---|
| CA-01 | Cumple |

**Concepto de la fase:** Cumple, 1 de 1. **Defectos abiertos:** ninguno.
