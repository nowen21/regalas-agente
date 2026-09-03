# Diseño: ¿cómo lo va a hacer?   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito **cómo** Cimiento va a cumplir lo que exigió el análisis, antes de escribir código. Su valor está en las decisiones con su porqué: sin ellas, dentro de seis meses nadie sabe por qué está armado así y todos lo cambian a ciegas.

> **Escrito desde la propuesta**, igual que el resto de [cvds/README.md/](../README.md). Sale de los 32 requisitos de [cvds/analisis-requisitos/README.md](../analisis-requisitos/README.md), aprobados el 2026-08-24.

**Estado: APROBADO** (2026-08-24, por Ing. José Dúmar Jiménez Ruíz).

---

## 1. Qué entra a esta etapa

| Qué se recibe | De dónde viene | ¿Aprobado? |
|---|---|---|
| 32 requisitos funcionales y 12 no funcionales | Análisis | Sí, el 2026-08-24 |
| 9 reglas del negocio, 4 actores y 12 casos de uso | Análisis | Sí, el 2026-08-24 |
| El inventario con 32 fichas y sus criterios | Análisis | Sí, el 2026-08-24 |
| Las restricciones: la fuente en texto, sin servicio ajeno, sin gasto | Planificación | Sí, el 2026-08-24 |

## 2. La arquitectura, en una frase y un dibujo

**Cómo está armado:** una aplicación que corre en la máquina de quien trabaja, con la verdad en archivos de texto y una base local que solo hace de índice. El agente le pide las reglas al abrir sesión, y si no la encuentra lee el texto directamente ([`DA-01`](decisiones-de-arquitectura.md), [`DA-03`](decisiones-de-arquitectura.md), [`DA-04`](decisiones-de-arquitectura.md)).

```
        [ Usuario ]                         [ Agente, en un proyecto ]
             |                                        |
        Interfaz local                        al abrir la sesión
             |                                        |
     +-------+----------------+---------------+-------+
     |       |                |               |
  Proyectos  Reglas    Ciclo de vida    Aprobaciones
     |       |                |               |
     +-------+----------------+---------------+
             |                        |
       Documentos en texto      Auditoría        Memoria
       (la verdad)              (no se edita)
             |
        Índice local  ──> se reconstruye desde el texto
             |
       Comprobaciones ──> leen y avisan, no corrigen
             |
       Expediente ──> genera el entregable
```

**Quién llama a quién:** la interfaz llama a los módulos; ningún módulo llama a la interfaz. Las comprobaciones solo leen, y por eso ningún componente depende de que otro haya corrido antes ([`DA-11`](decisiones-de-arquitectura.md)).

## 3. Los módulos y sus límites

> **Un módulo se define por lo que deja afuera.** Si no se puede decir qué NO hace, todavía no está separado de los demás.

| Módulo | Qué hace | Qué deja explícitamente fuera | Requisitos que cubre |
|---|---|---|---|
| Proyectos | Registra los proyectos, su ruta y su configuración; detecta la ruta perdida | Tocar el código del proyecto | RF-01 a RF-04 |
| Reglas | Guarda, versiona y publica las reglas; se las entrega al agente | Hacerlas cumplir: solo las declara y las entrega | RF-05 a RF-10 |
| Ciclo de vida | Crea épicas, historias y fases; lleva su estado y sus puertas | Decidir qué se construye | RF-11 a RF-14 |
| Aprobaciones | Registra la firma y la ata al texto aprobado | Aprobar por su cuenta | RF-15 a RF-17 |
| Auditoría | Registra qué se hizo y deja consultarlo | Interpretar por qué se hizo | RF-18, RF-19 |
| Comprobaciones | Lee lo escrito y dice si cumple | Corregir lo que encuentra | RF-20 a RF-22 |
| Memoria | Guarda lo aprendido y lo devuelve | Decidir qué es importante | RF-23, RF-24 |
| Expediente | Arma el conjunto y genera el entregable | Recibir cambios hechos en el entregable | RF-25, RF-26 |
| Importación | Trae proyectos que ya existen | Transformar lo que no reconoce | RF-27, RF-28 |
| Avisos y reportes | Dice lo que se desvía y cómo va cada proyecto | Decidir qué hacer al respecto | RF-29, RF-30 |
| Seguridad | Tapa las credenciales antes de que se escriban | Guardar credenciales para usarlas después | RF-31 |
| Medición | Registra el tiempo de revisión y lo compara | Juzgar si el tiempo fue bien usado | RF-32 |

## 4. Las decisiones de arquitectura

> **Una decisión de arquitectura es la que cuesta cara de revertir.** Se escribe con las alternativas que se descartaron: sin ellas no se puede defender ni revisar después.
>
> **`DA` es de decisión de arquitectura.** Es el número con que se cita cada una desde cualquier otro documento, y no se reutiliza.

| # | Qué se decidió | Alternativas descartadas | Por qué |
|---|---|---|---|
| DA-01 | La fuente es texto versionado, y la base es un índice | Todo en la base con volcados, o todo en texto sin índice | El respaldo pasa a ser el repositorio, y lo guardado se lee sin la plataforma |
| DA-02 | La documentación vive en el repositorio de la plataforma | Adentro de cada proyecto, o un repositorio por proyecto | Se clona la plataforma y está todo |
| DA-03 | Corre en la máquina de quien trabaja | Un servicio en línea, o atarla a esta máquina | Arranca sin gasto y sin sacar los datos, y deja abierta la puerta del servidor |
| DA-04 | El agente recibe las reglas, y si no responde lee la fuente | Que se detenga, o que cada proyecto guarde su copia | Gobierna cuando está, y no bloquea cuando no está |
| DA-05 | Una regla, un archivo, un número que no se reutiliza | Varias en un archivo, o renumerar al reordenar | Una cita de hace un año sigue apuntando a lo mismo |
| DA-06 | Las comprobaciones leen y avisan, no corrigen | Confiar en la memoria del agente, o que corrijan solas | Lo que depende de su memoria se incumple en silencio |
| DA-07 | La aprobación se ata al texto, y caduca si cambia | Guardar solo que está aprobado, o duplicar el documento | Se puede demostrar qué se autorizó exactamente |
| DA-08 | La auditoría registra acciones, y no se edita | Registrar cada mensaje, o dejar corregir el registro | Lo que importa demostrar es qué se hizo |
| DA-09 | El entregable se genera desde el texto | Escribir en ofimática, o mantener los dos | Lo que se genera se rehace; un segundo original hay que mantenerlo |
| DA-10 | Traer un proyecto no modifica el de origen | Mover su documentación, o enlazarla en dos sitios | Traer tiene que poder deshacerse sin daño |
| DA-11 | Cada componente entra sin tocar los otros | Un componente central que los llame, o que se registren entre ellos | Es la forma de que agregar algo deje de romper lo anterior |
| DA-12 | La pantalla administra, y todo cambio queda firmado y registrado | Que solo deje mirar, o que administre sin registrar | Lo que la hace segura no es prohibir: es registrar |

**Las doce, con lo que se pierde y qué las haría cambiar, están en [decisiones-de-arquitectura.md](decisiones-de-arquitectura.md).**

## 5. Los datos

| Qué se define | Cómo queda |
|---|---|
| Entidades, relaciones y el diccionario de cada campo | [modelo-de-datos.md](modelo-de-datos.md) |
| Dónde vive cada cosa | Texto para la verdad; base local solo para buscar |
| Qué se indexa, y por qué consulta | Documentos por proyecto, reglas por capítulo, auditoría por fecha, memoria por tema |
| Qué pasa si se pierde la base | Se reconstruye desde el texto: no se pierde información |

## 6. La interfaz y la navegación

| Qué se define | Cómo queda |
|---|---|
| Inventario de pantallas y navegación | [diseno-de-interfaz.md](diseno-de-interfaz.md) |
| Qué ve cada actor | El usuario ve y administra todo; el agente no usa pantalla; quien recibe el proyecto no entra |
| Qué mensajes ve quien se equivoca | Nunca una pantalla vacía: se dice qué falta y dónde debería estar |

## 7. El contrato con quien integra

| Qué se define | Cómo queda |
|---|---|
| Qué se le puede pedir a la plataforma desde la misma máquina | [contrato-de-la-interfaz.md](contrato-de-la-interfaz.md) |
| Qué se promete que no va a cambiar | Los nombres de las peticiones, y que ninguna cambie algo sin quedar registrada |
| Qué pasa cuando la plataforma no responde | El agente lee la fuente en texto y avisa que trabaja sin ella |

## 8. La seguridad

> **Esta sección se rehizo el 2026-09-02.** La anterior decía «un solo usuario en esta versión, sin credenciales propias», y se aplazaba hasta el día que la plataforma corriera en un servidor. Ese aplazamiento se levantó antes de esa fecha, por decisión del usuario: *«el que yo lo use no significa que no pueda tener seguridad»*. Lo que sigue es lo que rige.

| Qué se define | Cómo queda |
|---|---|
| Quién entra | **Quien tenga una cuenta y su contraseña.** Ninguna pantalla responde sin haber entrado |
| Con qué se construye | **El sistema de autenticación de Django**, `django.contrib.auth`. No se escribe uno propio |
| Qué puede hacer cada perfil | Dos grupos: **usuario** y **agente**, con los permisos de la sección 6 del [análisis](../analisis-requisitos/README.md) |
| Qué se cifra | **Las contraseñas**, con el algoritmo que trae Django. Nada más: no se guardan credenciales de terceros ni datos de personas |
| Qué queda registrado para auditar | Toda acción que cambia algo, sin poder editarse, y **con la cuenta que la hizo** |
| Dónde viven las credenciales del usuario | Fuera del repositorio, y el enmascarado las tapa antes de que algo las escriba |

### 8.1 Por qué el de Django y no uno propio

**Porque escribir autenticación es la forma más común de escribirla mal.** Guardar contraseñas, compararlas sin filtrar tiempos, expirar sesiones, invalidarlas al cambiar la clave: cada una tiene una manera correcta y varias que parecen correctas. Django ya las tiene resueltas y probadas por mucha más gente de la que va a mirar este repositorio.

**Y porque el modelo encaja sin forzarlo.** Los perfiles de la sección 6 del análisis son **grupos** de Django, y lo que cada uno puede hacer son **permisos**. No hace falta inventar ninguna tabla.

### 8.2 Cuáles de los cuatro actores son cuentas

**Dos de los cuatro, y decirlo evita construir de más.**

| Actor del análisis | ¿Es una cuenta? | Por qué |
|---|---|---|
| El usuario | **Sí**, grupo `usuario` | Administra, aprueba, corrige y publica |
| El agente | **Sí**, grupo `agente` | Entra a leer reglas y a escribir documentos |
| Un proyecto administrado | **No** | No es una persona ni un programa que entre: es una carpeta que se observa |
| Quien recibe un proyecto | **No, y a propósito** | El análisis dice que **no puede entrar a la plataforma**. Recibe el expediente ya generado, por fuera |

### 8.3 Qué separa a los dos grupos

De la sección 6 del análisis, lo que el agente **no** puede hacer:

| Acción | `usuario` | `agente` | Por qué |
|---|---|---|---|
| Ver cualquier pantalla | Sí | Sí | Leer no cambia nada |
| Escribir documentos y abrir fases | Sí | Sí | Es su trabajo |
| **Aprobar un documento** | **Sí** | **No** | Aprobar es del usuario: `00·N1` |
| **Publicar una versión de las reglas** | **Sí** | **No** | Publicar obliga a otros proyectos |
| **Derogar una regla** | **Sí** | **No** | Lo mismo |
| **Administrar cuentas** | **Sí** | **No** | Quien se da permisos a sí mismo no tiene permisos |

### 8.4 Lo que este diseño NO resuelve

- **La plataforma sigue sin exponerse a la red** (`DA-03`). Tener cuentas no la vuelve un servidor: lo vuelve posible sin rehacerla, que es lo que pide `RNF-09`.
- **Las órdenes de consola no piden contraseña.** Quien alcanza la consola de la máquina ya tiene la máquina. Lo que sí cambia es que **el nombre que se declara tiene que ser una cuenta que exista**: se acabó el campo de texto libre.
- **No hay recuperación de contraseña por correo.** No hay correo. Se restablece desde la consola de la máquina.

## 9. El entorno técnico y los estándares

| Qué se define | Cómo queda |
|---|---|
| Con qué se construye | Lo que ya está en la máquina del usuario, sin instalar servicios |
| Ambientes | El propio repositorio para construir, un proyecto de prueba que se crea y se borra, y el uso diario |
| Cómo se nombran archivos y carpetas | Una carpeta por proyecto; los documentos con el nombre de su etapa |
| Cómo se integra el trabajo | En fases que caben en una jornada, con su plan aprobado |
| Qué se registra del funcionamiento | Lo que falla y lo que se desvía, sin registrar la conversación |

## 10. Cómo se cumple lo no funcional

> Los requisitos no funcionales del análisis no se cumplen solos: cada uno necesita una decisión de diseño. La fila sin decisión es un requisito que nadie va a cumplir.

| Exigencia del análisis | Cómo la cumple el diseño |
|---|---|
| RNF-01 entregar reglas en menos de dos segundos | El cargador lee texto y el índice, sin red ni consultas complejas |
| RNF-02 listar proyectos en menos de un segundo | El estado de cada proyecto vive en el índice, no se recalcula leyendo todo |
| RNF-03 funciona sin red | Nada consulta afuera: `DA-03` |
| RNF-04 perder la base no pierde información | La base es índice y se reconstruye: `DA-01` |
| RNF-05 ninguna credencial escrita | El módulo de seguridad tapa antes de guardar, y una comprobación rechaza el guardado |
| RNF-06 sin datos de personas | El modelo no tiene entidad de persona |
| RNF-07 lo entiende quien no conoce el proyecto | Cada pantalla dice qué se está mirando, y los documentos se leen sin abrir otro |
| RNF-08 corre con lo que ya está instalado | Sin servicios de terceros: `DA-03` |
| RNF-09 puede correr en un servidor | Nada ata la aplicación a esta máquina; lo único local son las rutas de los proyectos |
| RNF-10 una versión nueva no rompe lo anterior | Antes de publicar se corre lo que ya servía: `DA-11` |
| RNF-11 un componente nuevo no obliga a reescribir | Cada uno es un archivo aparte: `DA-11` |
| RNF-12 toda acción dice quién, cuándo y sobre qué | La auditoría no se edita: `DA-08` |

## 11. Qué puede salir mal, y qué se hace

| Qué falla | Qué ve quien lo usa | Cómo se recupera |
|---|---|---|
| La plataforma no levanta | El agente avisa que trabaja sin ella | Se lee la fuente en texto; lo trabajado se reconcilia después |
| La base se corrompe | Un aviso al abrir | Se reconstruye desde el texto |
| Se pierde la ruta de un proyecto | Aviso, y su documentación sigue visible | Se vuelve a apuntar la ruta |
| Una comprobación reprueba de más | Rechazos que nadie entiende | Se ajusta esa comprobación, nunca se apagan todas |
| El generador produce un entregable incompleto | Falta una sección | Se regenera desde el texto, que no se perdió |
| Dos cambios a la vez sobre el mismo documento | Uno pisa al otro | El texto está versionado: se recupera lo pisado |

## 12. La trazabilidad

Cada requisito con el módulo que lo implementa y la decisión de la que depende.

| Requisito | Módulo | Decisión | Requisito | Módulo | Decisión |
|---|---|---|---|---|---|
| RF-01 | Proyectos | `DA-02` | RF-17 | Aprobaciones | `DA-07` |
| RF-02 | Proyectos | `DA-02` | RF-18 | Auditoría | `DA-08` |
| RF-03 | Proyectos | `DA-01` | RF-19 | Auditoría | `DA-08` |
| RF-04 | Proyectos | `DA-04` | RF-20 | Comprobaciones | `DA-06` |
| RF-05 | Reglas | `DA-05` | RF-21 | Comprobaciones | `DA-06` |
| RF-06 | Reglas | `DA-05` | RF-22 | Comprobaciones | `DA-11` |
| RF-07 | Reglas | `DA-06` | RF-23 | Memoria | `DA-01` |
| RF-08 | Reglas | `DA-05` | RF-24 | Memoria | `DA-01` |
| RF-09 | Reglas | `DA-04` | RF-25 | Expediente | `DA-09` |
| RF-10 | Reglas | `DA-04` | RF-26 | Expediente | `DA-09` |
| RF-11 | Ciclo de vida | `DA-12` | RF-27 | Importación | `DA-10` |
| RF-12 | Ciclo de vida | `DA-01` | RF-28 | Importación | `DA-10` |
| RF-13 | Ciclo de vida | `DA-12` | RF-29 | Avisos | `DA-01` |
| RF-14 | Ciclo de vida | `DA-12` | RF-30 | Avisos | `DA-01` |
| RF-15 | Aprobaciones | `DA-07` | RF-31 | Seguridad | `DA-06` |
| RF-16 | Aprobaciones | `DA-07` | RF-32 | Medición | `DA-08` |

**Requisitos sin módulo: ninguno. Módulos sin requisito: ninguno.**

## 13. Los entregables de esta etapa, y a quién van

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Especificación por módulo, doce módulos | [plantillas/ciclo-vida-proyectos/06-especificacion-modulo.md](../../plantillas/ciclo-vida-proyectos/06-especificacion-modulo.md) | Usuario, se acuerda | Pendiente |
| Modelo de datos | [plantillas/ciclo-vida-proyectos/14-modelo-de-datos.md](../../plantillas/ciclo-vida-proyectos/14-modelo-de-datos.md) | Equipo | [modelo-de-datos.md](modelo-de-datos.md) |
| Diseño de la interfaz | [plantillas/ciclo-vida-proyectos/15-diseno-de-interfaz.md](../../plantillas/ciclo-vida-proyectos/15-diseno-de-interfaz.md) | Usuario | [diseno-de-interfaz.md](diseno-de-interfaz.md) |
| Contrato de la interfaz local | [plantillas/ciclo-vida-proyectos/16-documentacion-de-api.md](../../plantillas/ciclo-vida-proyectos/16-documentacion-de-api.md) | Quien integre | [contrato-de-la-interfaz.md](contrato-de-la-interfaz.md) |
| Doce decisiones de arquitectura | [plantillas/cvds/diseno/decisiones-de-arquitectura.md](../../plantillas/cvds/diseno/decisiones-de-arquitectura.md) | Equipo | [decisiones-de-arquitectura.md](decisiones-de-arquitectura.md) |
| Diseño de seguridad | Sección 8 de este documento | Usuario | Listo, con su límite declarado |
| Entorno técnico y estándares | Sección 9 de este documento | Equipo | Listo |

## 14. Las puertas de esta etapa

| Qué no se puede hacer | Hasta que | Regla |
|---|---|---|
| Escribir código | la especificación del módulo esté acordada | [`02·F2`](../../base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md) |
| Dar por diseñado | cada requisito no funcional tenga su fila en la sección 10 | Cumplido: los doce están |
| Dar por diseñado | ningún requisito quede sin módulo en la sección 12 | Cumplido |

## 15. La decisión de cierre

**Se pasa a implementación cuando estén las especificaciones de módulo**, decidido por el autor el 2026-08-24. El diseño queda aprobado ese día; lo que falta para abrir código son las doce especificaciones, que son la puerta (`02·F2`).

**Desde esta fecha lo escrito acá es la línea base del diseño.**

**Lo que se acepta sin diseñar, y con qué riesgo:** la seguridad de la sección 8 vale para un solo usuario en su máquina. El día que la plataforma corra en un servidor o la use alguien más, esa sección se rehace entera, y con ella el modelo de datos, que hoy no tiene entidad de persona.

### 15.1 Cambios después del cierre

Uno por fila, con quién lo aprobó. La línea base no se edita en silencio.

| Fecha | Qué cambió | Por qué | Aprobado por |
|---|---|---|---|
| 2026-08-25 | `versión de reglas adoptada` de la entidad `Proyecto` deja de ser obligatoria | Salió al planear la fase B: si el campo es obligatorio, un proyecto que todavía no instaló el estándar no se puede conectar, y el problema declarado era administrar **todos** los proyectos. `RN-3` no cambia: la versión que se declare tiene que existir | Ing. José Dúmar Jiménez Ruíz |

**Qué NO cambió con esto:** ninguna decisión de arquitectura, ninguna pantalla, y ningún otro campo del modelo.

