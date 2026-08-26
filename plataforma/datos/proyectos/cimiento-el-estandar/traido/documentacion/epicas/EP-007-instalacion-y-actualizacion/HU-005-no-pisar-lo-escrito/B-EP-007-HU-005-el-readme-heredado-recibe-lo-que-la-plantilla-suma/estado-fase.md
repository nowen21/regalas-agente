# Estado de fase — Fase B-EP-007-HU-005-el-readme-heredado-recibe-lo-que-la-plantilla-suma

**Para qué sirve este documento.** Dice en qué estación va la fase y qué la tiene detenida, para que una sesión nueva siga desde ahí sin releer la conversación.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-007-HU-005-el-readme-heredado-recibe-lo-que-la-plantilla-suma` |
| **Módulo** | Instalador del estándar, los documentos heredados |
| **Épica / HU / origen** | [EP-007 Instalación y actualización](../../epica.md), [HU-005 No pisar lo escrito](../HU-005-no-pisar-lo-escrito.md), el punto 8 del [pendiente 33](../../../../../pendientes/hecho/lo-que-quedo-abierto-en-las-sesiones-viejas.md), donde estaba dicho así: «el mecanismo replica y el texto que lo explica no» |
| **Última actualización** | 2026-08-22 |

## 1. En qué estación va

**Estación actual:** cerrada. **Última puerta pasada:** 9, el commit `a07a964`.

> **La estación se corrigió el 2026-08-25**, leyendo el historial: el trabajo de esta fase estaba guardado desde hacía tiempo, y lo que faltaba era la marca. El hash sale de `git log` sobre su documento de cierre, no de una suposición.

| # | Etapa | Puerta | Estado |
|---|---|---|---|
| 1 | Declaración macro de la fase | bloque de fase con su identificador | ☑ |
| 2 | Disparo / autorización de inicio | 👤 «haga los dos para que salga de una de eso», 2026-08-22 | ☑ |
| 3 | Diseño del plan detallado | [plan_trabajo](plan_trabajo.md) y [plan_pruebas](plan_pruebas.md) | ☑ |
| 4 | Pausa y presentación | 👤 se reporta con el resultado | ☑ |
| 5 | Aprobación del plan detallado | 👤 en la orden que disparó el trabajo | ☑ |
| 6 | Ejecución continua | 4 tareas | ☑ |
| 7 | Pruebas | [resultado_pruebas](resultado_pruebas.md) | ☑ |
| 8 | Cierre documental | [funcionalidad_implementada](funcionalidad_implementada.md) | ☑ |

**Hechas:** 4 de 4. **Bloqueadas:** ninguna.

## 2. Qué la tiene detenida

**Nada.** La fase está cerrada.

## 3. Lo que una sesión nueva tiene que saber

**El mecanismo aditivo ya está en dos sitios y es el mismo:** `_completar_secciones` de `instalar.py`. Si mañana hay que completar un tercer documento heredado, se reusa; escribir otro sería tener dos formas de hacer lo mismo.
