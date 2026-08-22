# Estado de fase — Fase C-EP-005-HU-001-el-historico-se-busca-por-tema

**Para qué sirve este documento.** Dice en qué estación va la fase y qué la tiene detenida, para que una sesión nueva siga desde ahí sin releer la conversación.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `C-EP-005-HU-001-el-historico-se-busca-por-tema` |
| **Módulo** | Histórico de sesiones, sus índices |
| **Épica / HU / origen** | [EP-005 Automatismos que no dependen de la memoria](../../epica.md), [HU-001 Transcripción de la sesión](../HU-001-transcripcion-de-la-sesion.md), el punto 8 del [pendiente 33](../../../../../pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md), anotado el 2026-08-14: «una sesión trata varios temas y por el título no se encuentran» |
| **Última actualización** | 2026-08-22 |

## 1. En qué estación va

**Estación actual:** 8, cierre documental. **Última puerta pasada:** 7, veredicto **Cumple**.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 «haga los dos para que salga de una de eso», 2026-08-22 | ☑ |
| 3 | Diseño del plan detallado | [plan_trabajo](plan_trabajo.md) y [plan_pruebas](plan_pruebas.md) | ☑ |
| 4 | Pausa y presentación | 👤 se reporta con el resultado | ☑ |
| 5 | Aprobación del plan detallado | 👤 en la orden que disparó el trabajo | ☑ |
| 6 | Ejecución continua | 5 tareas | ☑ |
| 7 | Pruebas | [resultado_pruebas](resultado_pruebas.md) | ☑ |
| 8 | Cierre documental | [funcionalidad_implementada](funcionalidad_implementada.md) | ☑ |

**Hechas:** 5 de 5. **Bloqueadas:** ninguna.

## 2. Qué la tiene detenida

**Nada.** La fase está cerrada.

## 3. Lo que una sesión nueva tiene que saber

**El índice se genera, no se escribe.** Si aparece desactualizado, `validar.py temas --aplicar` y listo; editarlo a mano es trabajo perdido, y su propia cabecera lo advierte.
