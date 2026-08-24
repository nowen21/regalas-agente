# Acta de constitución y plan de proyecto   ·   `[CAPA 3]`

**Para qué sirve este documento.** Es la autorización formal del proyecto y su plan de conjunto: quién lo encarga, qué autoriza exactamente, con qué hitos y qué riesgos se asumen. El planteamiento dice **qué problema** se resuelve; esta dice **que se autoriza resolverlo**, con nombre, fecha y límites.

> **Escrito como si no hubiera nada construido**, igual que el resto de [cvds/](../README.md). Acompaña a [cvds/planificacion/README.md](README.md). Quien encarga y quien autoriza son la misma persona, y eso se escribe igual: la firma de uno mismo también fija el compromiso.

**Estado: APROBADO** (2026-08-24, por Ing. José Dúmar Jiménez Ruíz).

## 1. Acta de constitución

| Campo | Valor |
|---|---|
| **Proyecto** | Estándar de trabajo heredable para un agente de IA |
| **Quién lo encarga** | Ing. José Dúmar Jiménez Ruíz, que además lo usa y lo aprueba |
| **Qué autoriza** | Construir los siete paquetes del desglose de [README.md](README.md#10-desglose-del-trabajo-wbsedt): reglas cargadas al abrir, herencia e instalación, comprobación automática, registro de lo que la sesión deja, enmascarado de credenciales, moldes del ciclo y generador del entregable |
| **Qué NO autoriza** | Servidor, panel de administración ni servicio en línea. Tampoco actualizar un proyecto que hereda sin su aprobación, ni editar el `.docx` y devolverlo al `.md` |
| **Presupuesto aceptado** | Sin dinero. Tiempo del autor, estimado en 88 jornadas con un tercio de margen |
| **Fecha de autorización** | 2026-08-24 |

## 2. Hitos del plan

| # | Hito | Qué queda entregado | Fecha objetivo |
|---|---|---|---|
| 1 | Las reglas se cargan solas y mandan | El cuerpo de reglas y el cargador de sesión, con el núcleo que nada contradice | Sin fecha |
| 2 | Lo que se exige se comprueba solo | Una comprobación corriendo por cada regla que la admita | Sin fecha |
| 3 | El ciclo se documenta mientras se construye | Los moldes del ciclo, en uso desde la primera fase | Sin fecha |
| 4 | Instalado en un proyecto que no es del autor | Alguien ajeno lo instala siguiendo solo el manual, y lo usa una semana | Sin fecha |
| 5 | El entregable sale de lo escrito | El `.docx` generado desde los `.md`, sin redigitar nada | Sin fecha |

> **Ninguna fecha, y se dice.** El proyecto no tiene plazo comprometido con nadie: se sostiene mientras se use. Poner fechas de deseo sería inventar un compromiso que no existe.

## 3. Recursos y responsables

| Rol | Quién | Qué decide |
|---|---|---|
| Quien encarga y usa | Ing. José Dúmar Jiménez Ruíz | El alcance, cada aprobación de puerta y la aceptación final |
| Quien construye | El agente, por sesión | Lo técnico dentro del plan aprobado |
| Quien hereda | Los proyectos que adopten el estándar | Qué versión adoptan, y cuándo se ponen al día |

## 4. Riesgos del proyecto

| # | Riesgo | Impacto | Qué se hace si ocurre |
|---|---|---|---|
| 1 | El agente no obedece lo que se le carga al abrir | El proyecto entero pierde sentido | Se comprueba con programa lo que no se puede confiar a su memoria |
| 2 | Nadie ajeno lo adopta | Queda como preferencia personal, no como estándar | Se instala en un proyecto ajeno y se mide si lo usan |
| 3 | El estándar crece hasta que nadie lo lee entero | Deja de cumplirse por volumen | Se recorta al molde, y el porqué se va a su nota |
| 4 | Dos reglas se contradicen | Se incumple una obedeciendo la otra | Gana el núcleo, y la más nueva se deroga sin borrarla |
| 5 | Todo depende de una sola persona | Sin ella, el estándar se congela | Queda escrito y legible sin su autor, que es lo único que lo hace sobrevivir |

## 5. Cómo se comunica el avance

El estado real se lee en el repositorio, no se reporta aparte: el estado de cada fase, el registro de versiones y lo que cada sesión dejó escrito. Se revisa al cerrar cada versión, y ahí se decide qué entra en la siguiente.

Los proyectos que heredan se enteran solos: al abrir sesión se les avisa si la versión que adoptaron quedó atrás, y qué cambió desde entonces.
