# Diseño: ¿cómo lo va a hacer?   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito cómo el estándar de trabajo heredable va a cumplir lo que exigió el análisis, antes de escribir nada.

> **Escrito como si no hubiera nada construido.** Sale de los requisitos de [cvds/analisis-requisitos/README.md](../analisis-requisitos/README.md), no del repositorio.

**Estado: BORRADOR** (2026-08-22, sin aprobar).

---

## 1. Qué entra a esta etapa

| Qué se recibe | De dónde viene | ¿Aprobado? |
|---|---|---|
| Catorce requisitos funcionales y nueve no funcionales | Análisis | No: el análisis está en borrador |
| Siete reglas del negocio y tres actores | Análisis | No |
| Restricciones: sin infraestructura propia, `.md` como fuente | Planificación | No |

## 2. Los módulos y sus límites

| Módulo | Qué hace | Qué deja explícitamente fuera | Requisitos que cubre |
|---|---|---|---|
| Cuerpo de reglas | Guarda las exigencias, cada una con su identificador y su texto | Ejecutarlas: solo las declara | 1, 2 |
| Cargador de sesión | Entrega el cuerpo de reglas al agente cuando la sesión abre | Decidir cuáles aplican: entrega todas | 1 |
| Comprobaciones | Lee lo escrito y dice si cumple o no, sin opinar | Corregir lo que encuentra | 3, 4 |
| Enganches | Disparan lo que debe pasar solo: al abrir, al guardar y al cerrar | Sustituir al usuario en una aprobación | 2, 7, 8 |
| Instalador | Copia el estándar a un proyecto ajeno y anota qué versión adoptó | Actualizar sin que el usuario lo apruebe | 5, 6 |
| Moldes del ciclo | Los documentos modelo que se copian y se llenan | El contenido de cada proyecto | 9 |
| Generador de entregables | Convierte los `.md` del ciclo en `.docx` | Recibir cambios hechos en el `.docx` | RF-10 |
| Interfaz local | Muestra en pantalla los documentos del ciclo y lo guardado en la memoria | Editar: solo lee, porque lo que cambia el estado pasa por aprobación | RF-12 |
| Memoria | Guarda lo aprendido y lo devuelve en la sesión siguiente | Decidir qué es importante: guarda lo que la sesión declaró | RF-13 |

## 3. Las decisiones de arquitectura

| # | Qué se decidió | Alternativas descartadas | Por qué | Documento |
|---|---|---|---|---|
| 1 | Las reglas son texto plano en el repositorio | Base de datos, servicio remoto, configuración de la herramienta | El texto se lee, se versiona y viaja con el proyecto sin instalar nada | Pendiente |
| 2 | Una regla, un archivo, con identificador que no se reutiliza | Un archivo por capítulo | Se cita por identificador desde documentos que sobreviven a la regla | Pendiente |
| 3 | Lo que se exige se comprueba con programas que solo leen | Confiar en que el agente lo recuerde | Lo que depende de su memoria se incumple sin que nadie se entere | Pendiente |
| 4 | El `.md` es la fuente y el `.docx` una salida | Editar el `.docx` y sincronizar de vuelta | Dos fuentes divergen; una salida se regenera | Pendiente |
| 5 | La instalación copia y anota la versión adoptada | Enlazar el estándar desde una ruta común | Un proyecto debe poder quedarse en su versión y saber que quedó atrás | Pendiente |
| 6 | La interfaz corre en la máquina de quien trabaja, y solo lee | Servicio en línea, o pantalla que también edita | Un servicio obliga a sostener infraestructura; una pantalla que edita se salta la aprobación | Pendiente |
| 7 | La memoria vive en el repositorio del proyecto | El almacén de recuerdos de la herramienta | Ahí no viaja con el proyecto, no se versiona y nadie más la ve | Pendiente |
| 8 | Cada pieza entra sin obligar a tocar las anteriores | Un núcleo que conozca a todas | Si agregar una obliga a reescribir las otras, el sistema deja de poder crecer | Pendiente |

## 4. Los datos

| Qué se define | Dónde queda |
|---|---|
| Entidades: regla, versión, proyecto adoptante, señal, sesión | Pendiente, en el modelo de datos |
| Qué se guarda y por cuánto tiempo | Todo en archivos del repositorio, sin caducidad: el historial es el valor |
| Qué pasa con los datos que ya existen | Nada que migrar: el proyecto arranca sin datos previos |

## 5. La interfaz y la navegación

| Qué se define | Dónde queda |
|---|---|
| Inventario de pantallas | Una sola: el visor local que lista los documentos del ciclo y ofrece el `.docx` |
| Qué ve cada actor | El usuario ve todo; el agente no usa pantalla, usa archivos |

## 6. El contrato con quien integra

| Qué se define | Dónde queda |
|---|---|
| Operaciones, entradas, salidas y errores | N/A porque no se expone servicio: el contrato son los archivos y la línea de comandos |
| Qué se promete que no cambia | El nombre y la ubicación de lo que un proyecto hereda, y los identificadores de regla |

## 7. Cómo se cumple lo no funcional

| Exigencia del análisis | Cómo la cumple el diseño |
|---|---|
| Abrir la sesión no demora más de dos segundos | El cargador lee archivos de texto, sin red ni base de datos |
| Funciona sin red | Todo vive en el repositorio; ninguna comprobación consulta afuera |
| Ninguna credencial escrita | El enganche tapa antes de guardar, y una comprobación rechaza el guardado si encuentra una |
| Sin datos de personas | El modelo no tiene entidad de persona; los nombres que aparecen son de autoría |
| Lo entiende quien no conoce el proyecto | Cada documento se lee entero sin abrir otro, y la sigla se explica la primera vez |
| Python de la biblioteca estándar | Ninguna comprobación importa paquetes de terceros |
| Se instala sin tocar el código del proyecto | El instalador solo agrega archivos y un enganche |
| Una versión nueva no rompe lo que servía | Antes de publicar se corre lo que ya servía, y lo que obligue a rehacer algo se declara |
| Una pieza nueva entra sin reescribir las otras | Cada pieza es un archivo propio, y el cargador las toma todas sin conocerlas de antemano |

## 8. Qué puede salir mal, y qué se hace

| Qué falla | Qué ve quien lo usa | Cómo se recupera |
|---|---|---|
| El cargador no encuentra las reglas | Aviso al abrir la sesión, con la ruta que buscó | Se corrige la ruta; la sesión sigue sin reglas y lo dice |
| Una comprobación reprueba de más | Rechazos que nadie entiende | Se apaga esa comprobación y se corrige; nunca se apagan todas |
| El agente ignora lo que se le cargó | Trabajo que incumple sin aviso | Lo detecta la comprobación, no la memoria del usuario |
| El generador produce un `.docx` incompleto | Falta una sección en el entregable | Se regenera desde el `.md`, que no se perdió |

## 9. Los entregables de esta etapa, y a quién van

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Especificación por módulo, nueve módulos | [plantillas/ciclo-vida-proyectos/06-especificacion-modulo.md](../../plantillas/ciclo-vida-proyectos/06-especificacion-modulo.md) | Usuario, se acuerda | Pendiente |
| Modelo de datos | [plantillas/ciclo-vida-proyectos/14-modelo-de-datos.md](../../plantillas/ciclo-vida-proyectos/14-modelo-de-datos.md) | Equipo | Pendiente |
| Diseño de la interfaz local | [plantillas/ciclo-vida-proyectos/15-diseno-de-interfaz.md](../../plantillas/ciclo-vida-proyectos/15-diseno-de-interfaz.md) | Usuario | Pendiente: pantallas de documentos y de memoria |
| Documentación de la API | [plantillas/ciclo-vida-proyectos/16-documentacion-de-api.md](../../plantillas/ciclo-vida-proyectos/16-documentacion-de-api.md) | Quien integre con la interfaz local | Pendiente: la interfaz expone rutas locales, y eso ya es un contrato |
| Ocho decisiones de arquitectura | [plantillas/ADR.md](../../plantillas/ADR.md) | Equipo | Pendiente |

## 10. Las puertas de esta etapa

| Qué no se puede hacer | Hasta que | Regla |
|---|---|---|
| Escribir código | la especificación del módulo esté acordada | [`02·F2`](../../base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md) |
| Dar por diseñado | los siete requisitos no funcionales tengan su fila en la sección 7 | Cumplido: los siete están |

## 11. La decisión de cierre

**No se pasa a implementación todavía**, decidido por el autor el 2026-08-22.

Las nueve especificaciones de módulo están pendientes, y esa es la puerta. **Lo que cambió el 2026-08-24:** el sistema dejó de ser solo reglas y pasó a ser un sistema que crece, así que entraron dos módulos, la interfaz local y la memoria, tres decisiones de arquitectura y el contrato de las rutas locales, que antes se había dado por no aplicable.

## 12. Qué de esta etapa cumple hoy el proyecto

> Del análisis del 2026-08-24 sobre la versión 33.4.0. El resumen de las siete etapas, y lo que este análisis no puede decir, están en [cvds/README.md](../README.md).

| Qué exige el ciclo | Qué lo cumple hoy | Dónde está |
|---|---|---|
| Los módulos y sus límites | Qué archivo hace qué, y qué está amarrado a la herramienta | [anatomia/](../../anatomia/mapa-del-sitio.md) |
| La seguridad | Capítulo propio, con el enmascarado de credenciales corriendo solo | [base/04-seguridad.md](../../base/04-seguridad.md) y [validadores/secretos.py](../../validadores/secretos.py) |
| Entorno técnico y estándares | Calidad de código, dependencias, entornos y estructura, cada uno con su capítulo | Capítulos 07, 10, 11 y 14 de [base/](../../base/README.md) |

**A medias**

| # | Qué |
|---|---|
| 1 | la arquitectura está en las tres capas del [README.md](../../README.md) pero sin dibujo ni contrato entre piezas |
| 2 | el porqué de las decisiones vive en [notas/](../../notas/README.md), que no es el molde de decisión y no lista alternativas descartadas |
| 3 | el modelo de datos existe como [memoria/esquema.sql](../../memoria/esquema.sql) sin diccionario de campos |
| 4 | la interfaz tiene su [README](../../interfaz/README.md) pero no documento de diseño |
| 5 | la trazabilidad requisito a módulo no está escrita |

**No existe**

| # | Qué |
|---|---|
| 1 | ninguna decisión de arquitectura escrita con el molde de [plantillas/ADR.md](../../plantillas/ADR.md) |
| 2 | documentación de la interfaz de programación de la app local |
| 3 | la tabla que dice cómo se cumple cada requisito no funcional |
