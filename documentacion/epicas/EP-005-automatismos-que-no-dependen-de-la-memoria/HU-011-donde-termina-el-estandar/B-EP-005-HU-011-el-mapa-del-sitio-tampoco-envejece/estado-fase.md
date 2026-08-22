# Estado de fase — Fase B-EP-005-HU-011-el-mapa-del-sitio-tampoco-envejece

**Para qué sirve este documento.** Dice en qué estación va la fase y qué la tiene detenida, para que una sesión nueva siga desde ahí sin releer la conversación.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-005-HU-011-el-mapa-del-sitio-tampoco-envejece` |
| **Módulo** | Comprobaciones del repositorio, los mapas de `anatomia/` |
| **Épica / HU / origen** | [EP-005 Automatismos que no dependen de la memoria](../../epica.md), [HU-011 Dónde termina el estándar](../HU-011-donde-termina-el-estandar.md), el punto 8 del [pendiente 33](../../../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md), donde quedó preguntado si el mapa del sitio se comprueba o se actualiza a mano |
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

**El mapa ya se comprueba, así que no hace falta releerlo entero.** Si `validar.py sitio` está en verde, el mapa nombra todo lo que existe. Lo que sigue sin comprobarse es si la descripción de cada carpeta es la acertada, y eso se lee.
