# Plan de Pruebas · Fase A-EP-029-HU-002, revisar y su página   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar.

| Campo | Valor |
|---|---|
| **Código** | PP-EP029-HU002-A |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-002](../HU-002-el-boton-revisar-muestra-que-parte-de-cada-proyecto-queda-sin-pruebas.md) |
| **Fecha** | 2026-10-08 |
| **Elaborado por** | El agente |
| **Aprobado por** | [Análisis 1 del pendiente 141](../../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-1.md) |
| **Estado** | Aprobado |

## 3. Estrategia de pruebas

La herramienta de cada lenguaje se simula (`08·T3`): las pruebas no corren coverage.py, PHPUnit ni Angular de verdad. La simulación devuelve lo que cada herramienta escribe, tomado de su documentación.

### 3.5 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Desde `proyectos/cimiento/`: `manage.py test core.pruebas core.inicio core.ayuda core.proyectos`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-002 | CA-01 | CP-001, CP-002 | Funcional | Alta | Sí | ☑ |
| HU-002 | CA-02 | CP-003, CP-004, CP-005 | Funcional | Alta | Sí | ☑ |
| HU-002 | CA-03 | CP-006, CP-007 | Funcional | Alta | Sí | ☑ |
| HU-002 | CA-04 | CP-008, CP-009 | Funcional | Alta | Sí | ☑ |

**Cobertura:** 4 de 4 exigencias cubiertas = 100%.

## 6. Casos de prueba

### CP-001 · Reconoce cada lenguaje

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Carpetas con `manage.py`; con `artisan` y `composer.json`; con `angular.json`; con `requirements.txt` | Django, Laravel, Angular, Python |
| 2 | `manage.py` dentro de `proyectos/app/` | Django, con esa carpeta |
| 3 | `manage.py` solo dentro de `node_modules/` o `.venv/` | Ninguno |

### CP-002 · El lenguaje que no reconoce queda «sin medición»

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Revisar una carpeta vacía | Resultado «sin medición», con mensaje, sin excepción |

### CP-003 · Django: guarda porcentaje y archivos

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Revisar un proyecto Django con la herramienta simulada que deja un reporte con 75% y dos archivos | Resultado «hecha», 75%, los dos archivos con sus líneas sin pruebas |

### CP-004 · Laravel y Angular leen su resultado

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Laravel con un reporte de PHPUnit de 40 de 50 instrucciones | 80% |
| 2 | Angular con la salida «Lines : 62.5% ( 5/8 )» | 62,5% |

### CP-005 · Falta la herramienta o el Python del proyecto

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Django sin `.venv` | «falló», con un mensaje que dice qué hacer |
| 2 | Django con la herramienta que responde «No module named coverage» | «falló», con un mensaje que dice volver a instalar Cimiento en el proyecto |

### CP-006 · El botón arranca la revisión aparte

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Quien administra da clic en «Revisar» | Se pide la orden `revisar_pruebas` en otro proceso y la página dice «Revisando» |
| 2 | Quien no administra envía lo mismo | 403, y no se arranca nada |

### CP-007 · La orden de consola hace la misma revisión

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | `call_command("revisar_pruebas", proyecto=…)` con la herramienta simulada | Queda una revisión guardada y «Revisando» se apaga |

### CP-008 · La página muestra todos los proyectos

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Dos proyectos, uno revisado hace 2 días y otro nunca | Dos filas: «Al día» y «Nunca se ha revisado» |
| 2 | Abrir el inicio | El menú lleva a «Revisión de pruebas» |

### CP-009 · El detalle y su contraria

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir el detalle de un proyecto con dos archivos, de 90% y 30% | El de 30% sale primero |
| 2 | Borrar la revisión | Ya no existe |

## 9. Gestión de defectos

Un defecto se anota en `resultado_pruebas.md` §4.

## 12. Métricas e informe

Casos ejecutados y aprobados sobre 9, en `resultado_pruebas.md`.
