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

## 2. La arquitectura, en una frase y un dibujo

**Cómo está armado:** archivos de texto que el agente lee al abrir, programas que los revisan sin cambiarlos, y enganches que disparan lo uno y lo otro en el momento que toca. Todo corre en la máquina de quien trabaja, sin servicio ni red ([`DA-01`](decisiones-de-arquitectura.md), [`DA-06`](decisiones-de-arquitectura.md)).

```
        [ Sesión de trabajo con el agente ]
                      |
   al abrir ──> Cargador ──> Cuerpo de reglas (texto)
                      |
   al guardar ─> Enganches ──> Enmascarado de credenciales
                      |            └─> Memoria (lo aprendido)
   al cerrar ──> Enganches ──> Registro de la sesión
                      |
                Comprobaciones ──> leen: reglas, documentos y código
                      |
                 Moldes del ciclo ──> Generador ──> entregable
                      |
                 Interfaz local ──> muestra, no cambia
                      |
                 Instalador ──> lleva todo a otro proyecto
```

**Quién llama a quién:** los enganches llaman a todo lo demás; nada llama a los enganches. Las comprobaciones solo leen, y por eso ningun componente depende de que otra haya corrido antes ([`DA-08`](decisiones-de-arquitectura.md)).

## 3. Los módulos y sus límites

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

## 4. Las decisiones de arquitectura

> **`DA` es de decisión de arquitectura.** Es el número con que se cita cada una desde cualquier otro documento.

| # | Qué se decidió | Alternativas descartadas | Por qué | Documento |
|---|---|---|---|---|
| DA-01 | Las reglas son archivos de texto en el repositorio | Base de datos, servidor, o la configuración de la herramienta | El texto se lee sin instalar nada y viaja con el proyecto cuando alguien se lo lleva | [decisiones-de-arquitectura.md](decisiones-de-arquitectura.md) |
| DA-02 | Una regla, un archivo, y un número que no se reutiliza | Juntar las de un tema en un archivo, o renumerarlas al reordenar | Un documento de hace un año cita ese número, y tiene que seguir apuntando a lo mismo | [decisiones-de-arquitectura.md](decisiones-de-arquitectura.md) |
| DA-03 | Las comprobaciones leen y avisan, pero no corrigen | Confiar en que el agente se acuerde, o que el programa arregle solo | Lo que depende de su memoria se incumple sin que nadie se entere, y lo que se arregla solo se salta a quien debía decidir | [decisiones-de-arquitectura.md](decisiones-de-arquitectura.md) |
| DA-04 | El texto es la fuente, y el entregable se genera desde él | Escribir directo en ofimática, o mantener los dos y sincronizarlos | Lo que se genera se rehace cuando haga falta; un segundo original hay que mantenerlo para siempre | [decisiones-de-arquitectura.md](decisiones-de-arquitectura.md) |
| DA-05 | Instalar deja una copia, y anota qué versión se adoptó | Apuntar a una carpeta común, o traer la última versión al abrir | Un proyecto tiene derecho a quedarse en la versión que conoce, y a enterarse cuando quedó atrás | [decisiones-de-arquitectura.md](decisiones-de-arquitectura.md) |
| DA-06 | La pantalla corre en la máquina, y solo deja mirar | Ponerla en línea, o dejar editar desde ahí | Mirar no arriesga nada; cambiar pide aprobación, y esa conversación es con el agente | [decisiones-de-arquitectura.md](decisiones-de-arquitectura.md) |
| DA-07 | La memoria del agente vive dentro del proyecto | El almacén de la herramienta, o una memoria común a todos los proyectos | Lo aprendido en un proyecto es parte de ese proyecto, y debe leerse aunque cambie la herramienta | [decisiones-de-arquitectura.md](decisiones-de-arquitectura.md) |
| DA-08 | Un componente nuevo no obliga a tocar los que ya estaban | Un componente central que llame a las demás, o que se registren entre sí | Es la forma de que agregar algo deje de llevarse por delante lo anterior | [decisiones-de-arquitectura.md](decisiones-de-arquitectura.md) |

**Las ocho, con lo que se pierde y qué las haría cambiar, están en [decisiones-de-arquitectura.md](decisiones-de-arquitectura.md).**

## 5. Los datos

Qué guarda el sistema y dónde queda escrito el detalle.

| Qué se define | Dónde queda |
|---|---|
| Entidades, relaciones y el diccionario de cada campo | [modelo-de-datos.md](modelo-de-datos.md): siete entidades, con qué significa cada campo |
| Dónde vive cada cosa | Texto para lo que una persona lee; base local solo para lo que hay que buscar |
| Qué se indexa, y por qué consulta | Buscar anotaciones por tema, reglas por capítulo, y qué cambió entre dos versiones |
| Qué se guarda y por cuánto tiempo | Todo en archivos del repositorio, sin caducidad: el historial es el valor |
| Qué pasa con los datos que ya existen | Nada que migrar: el proyecto arranca sin datos previos |

## 6. La interfaz y la navegación

Qué se ve en pantalla y dónde queda escrito el detalle.

| Qué se define | Dónde queda |
|---|---|
| Inventario de pantallas y navegación | [diseno-de-interfaz.md](diseno-de-interfaz.md): seis pantallas, y qué se ve cuando falta algo |
| Qué ve cada actor | El usuario ve todo; quien recibe el proyecto no ve la memoria; el agente no usa pantalla |
| Qué mensajes ve quien se equivoca | Nunca una pantalla vacía: se dice qué falta y dónde debería estar |

## 7. El contrato con quien integra

| Qué se define | Dónde queda |
|---|---|
| Las peticiones, lo que devuelven y qué pasa si falta algo | [contrato-de-la-interfaz.md](contrato-de-la-interfaz.md): siete peticiones, todas de solo lectura |
| Qué se promete que no va a cambiar | Los nombres de esas siete, y que ninguna cambie el estado del proyecto |
| Qué pasa cuando el otro lado no responde | Se leen los archivos directamente: son la fuente, y la interfaz solo los muestra |

## 8. Cómo se cumple lo no funcional

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
| Un componente nuevo entra sin reescribir los otros | Cada componente es un archivo propio, y el cargador los toma todos sin conocerlos de antemano |

## 9. Qué puede salir mal, y qué se hace

| Qué falla | Qué ve quien lo usa | Cómo se recupera |
|---|---|---|
| El cargador no encuentra las reglas | Aviso al abrir la sesión, con la ruta que buscó | Se corrige la ruta; la sesión sigue sin reglas y lo dice |
| Una comprobación reprueba de más | Rechazos que nadie entiende | Se apaga esa comprobación y se corrige; nunca se apagan todas |
| El agente ignora lo que se le cargó | Trabajo que incumple sin aviso | Lo detecta la comprobación, no la memoria del usuario |
| El generador produce un `.docx` incompleto | Falta una sección en el entregable | Se regenera desde el `.md`, que no se perdió |

## 10. La trazabilidad

Cada requisito con el módulo que lo va a implementar y la decisión de la que depende.

| Requisito | Módulo que lo implementa | Decisión de la que depende |
|---|---|---|
| RF-01 | Cargador de sesión | `DA-01` |
| RF-02 | Enganches | `DA-03` |
| RF-03 | Comprobaciones | `DA-03` |
| RF-04 | Comprobaciones | `DA-03` |
| RF-05 | Instalador | `DA-05` |
| RF-06 | Instalador | `DA-05` |
| RF-07 | Enganches | `DA-01` |
| RF-08 | Enganches | `DA-03` |
| RF-09 | Moldes del ciclo | `DA-02` |
| RF-10 | Generador de entregables | `DA-04` |
| RF-11 | Comprobaciones | `DA-03` |
| RF-12 | Interfaz local | `DA-06` |
| RF-13 | Memoria | `DA-07` |
| RF-14 | Comprobaciones | `DA-08` |

**Requisitos sin módulo: ninguno. Módulos sin requisito: ninguno.**

## 11. Los entregables de esta etapa, y a quién van

Qué documentos produce la etapa, con qué molde se escriben y quién los recibe.

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Especificación por módulo, nueve módulos | [plantillas/ciclo-vida-proyectos/06-especificacion-modulo.md](../../plantillas/ciclo-vida-proyectos/06-especificacion-modulo.md) | Usuario, se acuerda | Pendiente |
| Modelo de datos | [plantillas/ciclo-vida-proyectos/14-modelo-de-datos.md](../../plantillas/ciclo-vida-proyectos/14-modelo-de-datos.md) | Equipo | Escrito en [modelo-de-datos.md](modelo-de-datos.md), con siete entidades y su diccionario |
| Diseño de la interfaz local | [plantillas/ciclo-vida-proyectos/15-diseno-de-interfaz.md](../../plantillas/ciclo-vida-proyectos/15-diseno-de-interfaz.md) | Usuario | Escrito en [diseno-de-interfaz.md](diseno-de-interfaz.md), seis pantallas |
| Contrato de la interfaz local | [plantillas/ciclo-vida-proyectos/16-documentacion-de-api.md](../../plantillas/ciclo-vida-proyectos/16-documentacion-de-api.md) | Quien integre con la interfaz local | Escrito en [contrato-de-la-interfaz.md](contrato-de-la-interfaz.md), siete peticiones |
| Ocho decisiones de arquitectura | [plantillas/ADR.md](../../plantillas/ADR.md) | Equipo | Escritas en [decisiones-de-arquitectura.md](decisiones-de-arquitectura.md), con sus alternativas descartadas |

## 12. Las puertas de esta etapa

| Qué no se puede hacer | Hasta que | Regla |
|---|---|---|
| Escribir código | la especificación del módulo esté acordada | [`02·F2`](../../base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md) |
| Dar por diseñado | los siete requisitos no funcionales tengan su fila en la sección 7 | Cumplido: los siete están |

## 13. La decisión de cierre

**No se pasa a implementación todavía**, decidido por el autor el 2026-08-22.

Las nueve especificaciones de módulo están pendientes, y esa es la puerta. **Lo que cambió el 2026-08-24:** el sistema dejó de ser solo reglas y pasó a ser un sistema que crece, así que entraron dos módulos, la interfaz local y la memoria, tres decisiones de arquitectura y el contrato de las rutas locales, que antes se había dado por no aplicable.

## 14. Qué de esta etapa cumple hoy el proyecto

> Del análisis del 2026-08-24 sobre la versión 33.4.0. El resumen de las siete etapas, y lo que ese análisis no puede decir, están en [cvds/README.md](../README.md).

| Qué exige el ciclo | Qué lo cumple hoy | Dónde está |
|---|---|---|
| Los módulos y sus límites | Qué archivo hace qué, y qué está amarrado a la herramienta | [anatomia/](../../anatomia/mapa-del-sitio.md) |
| La seguridad | Capítulo propio, con el enmascarado de credenciales corriendo solo | [base/04-seguridad.md](../../base/04-seguridad.md) y [validadores/secretos.py](../../validadores/secretos.py) |
| Entorno técnico y estándares | Calidad de código, dependencias, entornos y estructura, cada uno con su capítulo | Capítulos 07, 10, 11 y 14 de [base/](../../base/README.md) |

**Los ocho hallazgos de esta etapa, y qué se escribió para cada uno**

| # | Hallazgo del análisis | Qué se escribió | Dónde quedó |
|---|---|---|---|
| 1 | La arquitectura estaba en las tres capas del README, sin dibujo ni contrato entre componentes | Cómo está armado en una frase, el dibujo de quién llama a quién, y por qué ningun componente depende de que otra haya corrido | Sección 2 |
| 2 | El porqué de las decisiones vivía en notas, sin alternativas descartadas | Ocho decisiones con lo que se descartó, por qué, qué se pierde y qué las haría cambiar | [decisiones-de-arquitectura.md](decisiones-de-arquitectura.md) |
| 3 | El modelo de datos existía como un esquema, sin diccionario de campos | Siete entidades, con qué significa cada campo, cuáles son obligatorios y qué se indexa | [modelo-de-datos.md](modelo-de-datos.md) |
| 4 | La interfaz tenía README, no documento de diseño | Seis pantallas, la navegación, qué ve cada quien, y **qué se ve cuando falta algo** | [diseno-de-interfaz.md](diseno-de-interfaz.md) |
| 5 | La trazabilidad requisito a módulo no estaba escrita | Los catorce requisitos, cada uno con su módulo y la decisión de la que depende | Sección 10 |
| 6 | Ninguna decisión escrita con el molde que las exige | Las ocho, con identificador propio para poder citarlas | [decisiones-de-arquitectura.md](decisiones-de-arquitectura.md) |
| 7 | Sin documentación del contrato de la interfaz | Siete peticiones, todas de solo lectura, con qué se promete y qué no | [contrato-de-la-interfaz.md](contrato-de-la-interfaz.md) |
| 8 | Sin la tabla de cómo se cumple cada requisito no funcional | Los nueve, cada uno con la decisión de diseño que lo cumple | Sección 8 |

**Lo único que sigue abierto**

| Qué | Por qué no lo puede cerrar quien escribe |
|---|---|
| Ninguno de estos documentos está aprobado | La aprobación es del usuario, y sin ella no hay diseño acordado: la puerta de la implementación es la especificación acordada (`02·F2`) |

**Aprobado por: «quién», el «AAAA-MM-DD».**
