# Implementación: ¿qué se toca, y en qué orden?   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito cómo se parte la construcción del estándar de trabajo heredable en unidades que caben en una jornada, en qué orden se hacen y cómo se deshace lo que salga mal.

> **Escrito como si no hubiera nada construido.** Las fases salen de los siete módulos del [diseño](../diseno/README.md) y de los objetivos de [planificación](../planificacion/README.md), no del repositorio.

**Estado: BORRADOR** (2026-08-22, sin abrir).

---

## 1. Qué entra a esta etapa

| Qué se recibe | De dónde viene | ¿Aprobado? |
|---|---|---|
| Especificación de los siete módulos | Diseño | No: están pendientes, y son la puerta |
| Historias con criterios de aceptación | Análisis | No: el inventario no está aprobado |
| Cinco decisiones de arquitectura | Diseño | No |

## 2. Cómo se parte el trabajo

| Fase | Historia que ejecuta | Módulos que toca | Depende de | Estado |
|---|---|---|---|---|
| A. El cuerpo de reglas se escribe y se cita | Guardar las exigencias con identificador | Cuerpo de reglas | — | Sin abrir |
| B. Las reglas se cargan al abrir la sesión | Cargar sin que nadie lo pida | Cargador, Enganches | A | Sin abrir |
| C. Nada cambia de estado sin aprobación | Impedir el cambio no autorizado | Enganches | B | Sin abrir |
| D. Lo escrito se comprueba solo | Comprobar lo que la regla exige | Comprobaciones | A | Sin abrir |
| E. Lo no probado se declara sin verificar | Declarar el estado real | Comprobaciones | D | Sin abrir |
| F. La sesión deja su rastro fuera del chat | Escribir lo que la sesión dejó | Enganches | B | Sin abrir |
| G. Ninguna credencial queda escrita | Tapar antes de guardar | Enganches | B | Sin abrir |
| H. El estándar se instala en otro proyecto | Instalar y anotar la versión | Instalador | A, D | Sin abrir |
| I. El proyecto sabe cuándo quedó atrás | Avisar el desfase y qué cambió | Instalador | H | Sin abrir |
| J. Los moldes del ciclo existen y se exigen | Documentar mientras se construye | Moldes, Comprobaciones | D | Sin abrir |
| K. El entregable sale del `.md` | Generar el `.docx` | Generador | J | Sin abrir |
| L. Se mide el tiempo de revisión | Medir antes y después | Comprobaciones | D, F | Sin abrir |

## 3. El orden, y por qué ese

| Qué va primero | Por qué |
|---|---|
| A, el cuerpo de reglas | Sin reglas escritas no hay qué cargar, qué comprobar ni qué heredar |
| D, la comprobación | Es el paquete con más incertidumbre: no se sabe cuántas reglas se comprueban solas, y eso puede cambiar el diseño |
| H, la instalación fuera | Es el supuesto que sostiene el proyecto entero, y sigue sin confirmar |
| K, el generador, al final | Necesita documentos ya escritos; hacerlo antes es convertir plantillas vacías |

## 4. Cómo se deshace lo que salga mal

| Si falla | Cómo se vuelve atrás | Qué se pierde |
|---|---|---|
| Una fase a medias | Se descarta la rama de trabajo | Solo lo de esa jornada |
| Un cambio ya integrado | Se revierte el cambio y se sube una versión de corrección | Nada, si la versión anterior sigue publicada |
| Una regla que resultó equivocada | Se deroga con su motivo, nunca se borra | Nada: las citas viejas siguen resolviendo |
| Una instalación en un proyecto ajeno | El proyecto se queda en la versión que tenía | Nada: la instalación no toca su código |

## 5. Qué se escribe mientras se construye

| Qué se escribe | Cuándo | Molde |
|---|---|---|
| Plan de trabajo de la fase | Antes de tocar nada | [plantillas/ciclo-vida-proyectos/07-plan-trabajo.md](../../plantillas/ciclo-vida-proyectos/07-plan-trabajo.md) |
| Estado de la fase | Al cambiar de estación | [plantillas/ciclo-vida-proyectos/10-estado-fase.md](../../plantillas/ciclo-vida-proyectos/10-estado-fase.md) |
| Lo que la sesión dejó | En el momento en que aparece, no al cerrar | El documento de señales del proyecto |
| La entrada del registro de versiones | Al cerrar cada versión | El registro de cambios |

## 6. La deuda que se declara

| # | Qué quedó sin hacer | Por qué se aceptó | Quién la paga | Para cuándo |
|---|---|---|---|---|
| 1 | Sin medición del tiempo de revisión antes de empezar | No hay línea base y el proyecto ya arrancó | El autor | Antes de afirmar que se redujo |
| 2 | El generador de `.docx` queda para el final | Necesita documentos escritos que todavía no existen | El autor | Antes de la primera entrega a un tercero |

## 7. Los entregables de esta etapa, y a quién van

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Doce fases, una por historia | [plantillas/ciclo-vida-proyectos/05-fase.md](../../plantillas/ciclo-vida-proyectos/05-fase.md) | Equipo | Pendiente |
| Plan de trabajo de cada fase | [plantillas/ciclo-vida-proyectos/07-plan-trabajo.md](../../plantillas/ciclo-vida-proyectos/07-plan-trabajo.md) | Usuario, con su plan de pruebas | Pendiente |
| Estado de cada fase | [plantillas/ciclo-vida-proyectos/10-estado-fase.md](../../plantillas/ciclo-vida-proyectos/10-estado-fase.md) | Equipo | Pendiente |
| El estándar construido | No aplica | Usuario y proyectos que heredan | Pendiente |

## 8. Las puertas de esta etapa

| Qué no se puede hacer | Hasta que | Regla |
|---|---|---|
| Tocar código | haya especificación acordada | [`02·F2`](../../base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md) |
| Ejecutar un plan | esté aprobado junto con su plan de pruebas | [`02·F4`](../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md) |
| Dar una fase por cerrada | su resultado de pruebas tenga veredicto por criterio | El estado lo fija la prueba, no la lectura |

## 9. La decisión de cierre

**No se abre la etapa todavía**, decidido por el autor el 2026-08-22.

Falta la especificación de los siete módulos. Las doce fases están definidas y ordenadas: la D y la H son las que hay que hacer temprano, porque una decide si el diseño de comprobación se sostiene y la otra confirma el supuesto del que depende todo el proyecto.
