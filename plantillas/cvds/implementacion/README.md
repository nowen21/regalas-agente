# Implementación: ¿qué se toca, y en qué orden?   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito cómo se parte el trabajo en unidades que caben en una jornada y se pueden revertir, en qué orden se hacen, con qué reglas se escribe el código y cómo se deshace lo que salga mal. El detalle de cada unidad vive en su propia fase; acá queda el gobierno de todas.

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |

> Plantilla. Se llena al abrir la etapa y se actualiza con cada fase cerrada. La envergadura ajusta la profundidad, nunca la existencia: la sección sin materia se llena con `N/A porque «…»`, nunca se borra. Reemplaza los `«…»` y borra esta caja.

> **Cómo se redacta lo que va dentro de cada `«…»`.** En el idioma del proyecto ([`01·C8`](«RUTA-ESTANDAR»/base/01-conducta.md#c8--habla-el-idioma-del-proyecto)) y en la menor cantidad de palabras con la que se entienda ([`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md)): el dato primero, sin repaso, sin justificación que nadie pidió y sin paso a paso. Lo que no cabe se escribe en su documento y se enlaza. Si en una celda va más de una cosa, se escribe como lista: una por renglón, con `<br>` entre ellas y viñeta al empezar. Separarlas con puntos medios en un solo párrafo las vuelve ilegibles.

> Se escribe desde la propuesta, no desde lo que ya está construido. Lo que existe sirve para saber qué se conserva y qué se rehace, nunca para fijar el alcance. La prueba: si se borra mentalmente lo construido y el documento sigue siendo cierto, está bien escrito.

**Estado: «BORRADOR / EN CURSO / CERRADA»** («AAAA-MM-DD»).

## 1. Qué entra a esta etapa

> Lista lo que la implementación recibe de las etapas anteriores y si llegó aprobado.

| Qué se recibe | De dónde viene | ¿Aprobado? |
|---|---|---|
| Especificación de cada módulo | Diseño | «Sí / No, y cuáles faltan» |
| Historias con criterios de aceptación | Análisis | «…» |
| Decisiones de arquitectura, entorno y estándares | Diseño | «…» |

## 2. Con qué se trabaja

> Deja escrito el entorno de trabajo antes de la primera línea de código. Lo que no queda acá se reconstruye a mano en cada máquina nueva, y nunca queda igual.

| Qué se define | Cómo queda |
|---|---|
| Versiones exactas de lenguaje y dependencias | «…» |
| Cómo se levanta el proyecto desde cero, en una máquina limpia | «…» |
| Qué datos de prueba se usan, y de dónde salen | «…» |
| Dónde viven las credenciales, que no es el código | «…» |

## 3. Cómo se parte el trabajo

> Lista las fases, cada una la unidad de ejecución de una historia: cabe en una jornada, se entrega completa y se revierte sola. Lo que no cabe en una jornada se parte en dos fases.

| Fase | Historia que ejecuta | Módulos que toca | Depende de | Estado |
|---|---|---|---|---|
| «A-EP01-HU01-descripción» | «HU-001» | «…» | — | «Sin abrir / En curso / Cerrada» |
| «…» | «…» | «…» | «…» | «…» |

## 4. El orden, y por qué ese

> Dice qué se hace primero y por qué. El orden lo ponen las dependencias y el riesgo: lo de más incertidumbre va primero, mientras queda tiempo de cambiar de camino.

| Qué va primero | Por qué |
|---|---|
| «…» | «…» |

## 5. Cómo se escribe el código

> Son las reglas de escritura que se exigen en la revisión, cada una con su forma de comprobarla. Lo que no queda escrito acá es preferencia personal y se discute en cada cambio.

| Qué se exige | Cómo se comprueba |
|---|---|
| Nombres y estilo, según el estándar del diseño | «Revisión, o programa que lo revisa solo» |
| Prueba junto al código que la necesita | «…» |
| Sin credenciales ni rutas de una sola máquina | «…» |
| Errores que dicen qué pasó y qué hacer | «…» |
| Cambios pequeños, que se puedan leer de una sentada | «…» |

## 6. Cómo se integra y quién lo revisa

> Dice cómo entra un cambio al código común: la rama, la revisión, lo que corre solo y lo que bloquea.

| Qué se define | Cómo queda |
|---|---|
| Cómo se ramifica el trabajo | «…» |
| Quién revisa antes de integrar, y qué mira | «…» |
| Qué corre solo en cada integración | «Pruebas, revisión de estilo, comprobaciones del estándar» |
| Qué bloquea la integración | «…» |

## 7. Cómo se deshace lo que salga mal

> Dice cómo se vuelve atrás en cada tipo de falla y qué se pierde al hacerlo.

| Si falla | Cómo se vuelve atrás | Qué se pierde |
|---|---|---|
| «Una fase a medias» | «…» | «…» |
| «Un cambio ya integrado» | «…» | «…» |
| «Algo que tocó datos» | «…» | «…» |

## 8. Qué se escribe mientras se construye

> Lista los documentos que se llenan durante la construcción y cuándo. Ninguno se deja para el final: después nadie recuerda por qué se hizo así.

| Qué se escribe | Cuándo | Molde |
|---|---|---|
| Plan de trabajo de la fase | Antes de tocar nada | [plantillas/ciclo-vida-proyectos/07-plan-trabajo.md](../../ciclo-vida-proyectos/07-plan-trabajo.md) |
| Estado de la fase | Al cambiar de estación | [plantillas/ciclo-vida-proyectos/10-estado-fase.md](../../ciclo-vida-proyectos/10-estado-fase.md) |
| Lo que la sesión dejó | En el momento en que aparece | «…» |
| Qué trae la versión, para quien la usa | Al cerrar cada entrega | [plantillas/ciclo-vida-proyectos/19-notas-de-version.md](../../ciclo-vida-proyectos/19-notas-de-version.md) |

## 9. Cómo se sabe cómo va

> Dice qué se mide del avance, cada cuánto y quién lo mira.

| Qué se mide | Cada cuánto | Quién lo mira |
|---|---|---|
| Fases cerradas contra fases abiertas | «…» | «…» |
| Lo que se atrasó, y qué lo atrasó | «…» | «…» |
| Deuda declarada que sigue sin pagar | «…» | «…» |

## 10. La deuda que se declara

> Registra lo que se decidió no hacer ahora, a sabiendas, con quién lo paga y para cuándo. Lo que se olvidó cuenta como defecto, no como deuda, y la deuda sin fecha ni dueño no se paga nunca. Si no se declaró deuda, se escribe `N/A porque «…»`.

| # | Qué quedó sin hacer | Por qué se aceptó | Quién la paga | Para cuándo |
|---|---|---|---|---|
| 1 | «…» | «…» | «…» | «…» |

## 11. Los entregables de esta etapa, y a quién van

> Lista los documentos que produce la etapa y a quién se entregan.

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Fase, una por historia | [plantillas/ciclo-vida-proyectos/05-fase.md](../../ciclo-vida-proyectos/05-fase.md) | Equipo | «…» |
| Plan de trabajo | [plantillas/ciclo-vida-proyectos/07-plan-trabajo.md](../../ciclo-vida-proyectos/07-plan-trabajo.md) | Cliente, se aprueba con su plan de pruebas | «…» |
| Estado de cada fase | [plantillas/ciclo-vida-proyectos/10-estado-fase.md](../../ciclo-vida-proyectos/10-estado-fase.md) | Equipo | «…» |
| Cómo se levanta el proyecto | Sección 2 de este documento | Quien entra al equipo, y quien instala | «…» |
| El producto construido | No aplica | Cliente, al desplegar | «…» |

## 12. Las puertas de esta etapa

> Son las condiciones que bloquean el avance: lo que no se hace hasta que se cumpla algo, con la regla que lo exige.

| Qué no se puede hacer | Hasta que | Regla |
|---|---|---|
| Tocar código | haya especificación acordada | [`02·F2`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md) |
| Ejecutar un plan | esté aprobado junto con su plan de pruebas | [`02·F4`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md) |
| Integrar un cambio | alguien distinto de quien lo escribió lo haya revisado | Sección 6 de este documento |
| Dar una fase por cerrada | su resultado de pruebas tenga veredicto | «…» |

## 13. La decisión de cierre

> Registra si la implementación pasa a pruebas, quién lo decidió y qué de lo pendiente bloquea la entrega.

**«Se pasa a pruebas / No se pasa»**, decidido por «quién» el «AAAA-MM-DD».

«Qué fases quedaron abiertas, qué deuda se declaró, y qué de eso bloquea la entrega.»
