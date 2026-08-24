# Implementación: ¿qué se toca, y en qué orden?   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito cómo se parte el trabajo en unidades que caben en una jornada y se pueden revertir, en qué orden se hacen y cómo se deshace lo que salga mal. El detalle de cada unidad vive en su propia fase; acá queda el gobierno de todas.

> Plantilla. Se llena al abrir la etapa y se actualiza con cada fase cerrada. La envergadura ajusta la profundidad, nunca la existencia: la sección sin materia se llena con `N/A porque «…»`, nunca se borra. Reemplaza los `«…»` y borra esta caja.

> **Cómo se redacta lo que va dentro de cada `«…»`.** En el idioma del proyecto ([`01·C8`](«RUTA-ESTANDAR»/base/01-conducta.md#c8--habla-el-idioma-del-proyecto)) y en la menor cantidad de palabras con la que se entienda ([`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md)): el dato primero, sin repaso, sin justificación que nadie pidió y sin paso a paso. Lo que no cabe se escribe en su documento y se enlaza.

**Estado: «BORRADOR / EN CURSO / CERRADA»** («AAAA-MM-DD»).

---

## 1. Qué entra a esta etapa

| Qué se recibe | De dónde viene | ¿Aprobado? |
|---|---|---|
| Especificación de cada módulo | Diseño | «Sí / No, y cuáles faltan» |
| Historias con criterios de aceptación | Análisis | «…» |
| Decisiones de arquitectura | Diseño | «…» |

## 2. Cómo se parte el trabajo

> **Una fase es la unidad de ejecución de una historia:** cabe en una jornada, se entrega completa y se revierte sola. Lo que no cabe en una jornada no es una fase, son dos.

| Fase | Historia que ejecuta | Módulos que toca | Depende de | Estado |
|---|---|---|---|---|
| «A-EP01-HU01-descripción» | «HU-001» | «…» | — | «Sin abrir / En curso / Cerrada» |
| «…» | «…» | «…» | «…» | «…» |

## 3. El orden, y por qué ese

> El orden no es el del documento: es el de las dependencias y el del riesgo. Lo que más incertidumbre tiene va primero, mientras queda tiempo de cambiar de camino.

| Qué va primero | Por qué |
|---|---|
| «…» | «…» |

## 4. Cómo se deshace lo que salga mal

| Si falla | Cómo se vuelve atrás | Qué se pierde |
|---|---|---|
| «Una fase a medias» | «…» | «…» |
| «Un cambio ya integrado» | «…» | «…» |
| «Algo que tocó datos» | «…» | «…» |

## 5. Qué se escribe mientras se construye

> **La documentación de esta etapa no se escribe al final.** El documento de la fase se llena en el momento, porque después nadie recuerda por qué se hizo así.

| Qué se escribe | Cuándo | Molde |
|---|---|---|
| Plan de trabajo de la fase | Antes de tocar nada | [plantillas/ciclo-vida-proyectos/07-plan-trabajo.md](../../ciclo-vida-proyectos/07-plan-trabajo.md) |
| Estado de la fase | Al cambiar de estación | [plantillas/ciclo-vida-proyectos/10-estado-fase.md](../../ciclo-vida-proyectos/10-estado-fase.md) |
| Lo que la sesión dejó | En el momento en que aparece | «…» |

## 6. La deuda que se declara

> Deuda es lo que se decidió no hacer ahora, con conocimiento. Lo que se olvidó no es deuda: es un defecto. La deuda sin fecha ni dueño no se paga nunca.

| # | Qué quedó sin hacer | Por qué se aceptó | Quién la paga | Para cuándo |
|---|---|---|---|---|
| 1 | «…» | «…» | «…» | «…» |

## 7. Los entregables de esta etapa, y a quién van

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Fase, una por historia | [plantillas/ciclo-vida-proyectos/05-fase.md](../../ciclo-vida-proyectos/05-fase.md) | Equipo | «…» |
| Plan de trabajo | [plantillas/ciclo-vida-proyectos/07-plan-trabajo.md](../../ciclo-vida-proyectos/07-plan-trabajo.md) | Cliente, se aprueba con su plan de pruebas | «…» |
| Estado de cada fase | [plantillas/ciclo-vida-proyectos/10-estado-fase.md](../../ciclo-vida-proyectos/10-estado-fase.md) | Equipo | «…» |
| El producto construido | No aplica | Cliente, al desplegar | «…» |

## 8. Las puertas de esta etapa

| Qué no se puede hacer | Hasta que | Regla |
|---|---|---|
| Tocar código | haya especificación acordada | [`02·F2`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md) |
| Ejecutar un plan | esté aprobado junto con su plan de pruebas | [`02·F4`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md) |
| Dar una fase por cerrada | su resultado de pruebas tenga veredicto | «…» |

## 9. La decisión de cierre

**«Se pasa a pruebas / No se pasa»**, decidido por «quién» el «AAAA-MM-DD».

«Qué fases quedaron abiertas, qué deuda se declaró, y qué de eso bloquea la entrega.»
