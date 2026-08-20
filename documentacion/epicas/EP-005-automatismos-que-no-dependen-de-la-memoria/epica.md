# EP-005 — Automatismos que no dependen de que alguien se acuerde

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-005 |
| **Brief de origen** | [planteamiento.md](../../../planteamiento.md) |
| **Iniciativa** | Que una IA que programa trabaje siempre igual |
| **Producto** | Estándar de agente para desarrollo de software |
| **Tipo** | Técnica (habilitadora) |
| **Prioridad** | Must |
| **Estimación** | M |
| **Horizonte** | Primera entrega |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Propuesta |

## 2. Resumen ejecutivo

Una comprobación que hay que acordarse de correr no protege nada. Lo mismo pasa con escribir lo que se decidió en una sesión: si se deja para el final, no se escribe, porque un chat casi nunca tiene final claro. Se cierra la ventana y se perdió.

Esta épica hace que esas cosas se disparen solas en el momento en que ocurren. Al abrir la sesión, al escribir un archivo, al preparar una publicación. Nadie decide correrlas: pasan.

Lo más importante que se dispara solo es la transcripción de cada sesión. El chat se borra, el repositorio no, así que cada intercambio queda escrito tal como pasó, con la hora leída del reloj de la máquina.

## 3. Problema y oportunidad

### 3.1 Situación actual

Lo que se decidió en un chat vive solamente en ese chat. Cuando se cierra, se pierde el porqué de las decisiones y la sesión siguiente vuelve a discutir lo mismo. Y las comprobaciones que existen se corren cuando alguien se acuerda, que es casi nunca.

### 3.2 Impacto de no hacerlo

Se repite trabajo ya hecho, se contradicen decisiones ya tomadas, y una clave pegada por descuido puede terminar publicada sin que nada se queje.

### 3.3 Evidencia

| Fuente | Hallazgo |
|---|---|
| Sesiones anteriores sin transcripción | El porqué de varias decisiones se perdió y hubo que reconstruirlo discutiéndolo otra vez |
| Comprobaciones que dependen de correrse a mano | Se corren solo cuando algo ya salió mal |

## 4. Objetivo y propuesta de valor

**Objetivo.** Que lo que hoy depende de que alguien se acuerde ocurra solo, en el momento del trabajo, sin que nadie lo decida.

**Hipótesis de valor.** Si el automatismo se dispara en el momento del trabajo, el cumplimiento deja de depender de la disciplina. Se sabrá cuando una sesión quede escrita completa sin que nadie la haya pedido.

### 4.1 Beneficios esperados

| Beneficiario | Beneficio | Tipo |
|---|---|---|
| La persona | No tiene que acordarse de nada | Cualitativo |
| La sesión siguiente | Encuentra escrito qué se decidió antes y por qué | Cualitativo |
| El repositorio | No recibe una clave pegada por descuido | Cualitativo |

## 5. Alcance

### 5.1 Dentro del alcance

- La transcripción de cada sesión, escrita a medida que pasa y no al cerrar.
- La hora de cada intercambio leída del reloj de la máquina, nunca estimada.
- El disparo automático de las comprobaciones en el momento del trabajo: al abrir sesión, al escribir un archivo, antes de guardar un cambio y antes de publicarlo.
- El control del mensaje con que se guarda un cambio.
- La revisión de que no salga una clave hacia el repositorio, incluida la que se pegó en el chat.
- El control de que un cambio de reglas venga con su versión y su registro.

### 5.2 Fuera del alcance

- Escribir las comprobaciones. Eso es EP-004; aquí solo se disparan.
- Decidir qué se escribe en la transcripción más allá de lo que pasó. Se transcribe, no se resume.
- Aprobar en nombre de la persona. Ningún automatismo aprueba.

### 5.3 Diferido

- Automatismos que necesiten que el proyecto declare sus convenciones propias. Se retoman cuando esa declaración exista.

## 5.4 Alcance funcional completo

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Finalidad | Que lo obligatorio ocurra solo, en el momento del trabajo |
| 2 | Actores | La persona que trabaja, la IA que responde, el programa que se dispara |
| 3 | Información | Cada intercambio se guarda con quién habló, qué dijo y a qué hora, según el reloj de la máquina |
| 4 | Campos | La transcripción tiene campos definidos: fecha, hora, quién, contenido. La hora que no se registró se escribe como no registrada. El detalle baja a la historia de usuario |
| 5 | Validaciones | La hora no se estima ni se reconstruye de memoria; el contenido no se resume ni se parafrasea |
| 6 | Reglas de negocio | El archivo de la sesión se crea con la primera decisión o el primer cambio, no al cerrar; se actualiza después de cada intercambio |
| 7 | Estados y transiciones | Una sesión está abierta o cerrada. Un automatismo pasa, avisa o detiene |
| 8 | Operaciones | Escribir el intercambio, disparar la comprobación, detener la publicación, avisar y dejar seguir |
| 9 | Restricciones | Un automatismo no aprueba nada; lo que detiene tiene que decir cómo saltarse el control cuando haya que hacerlo |
| 10 | Relaciones | Los automatismos disparan las comprobaciones de EP-004 y alimentan la memoria de EP-006 |
| 11 | Consultas | Se necesita poder leer la transcripción de una sesión pasada y encontrarla por su tema |
| 12 | Mensajes | Cuando un automatismo detiene, dice qué falló, cómo se arregla y cómo se salta |
| 13 | Errores | El reloj no responde, el archivo está bloqueado, la sesión se corta a la mitad |
| 14 | Permisos | No aplica porque corre en la máquina de quien trabaja |
| 15 | Auditoría | La transcripción de la sesión es la auditoría |
| 16 | Resultado final | La épica está completa cuando una sesión queda escrita completa sin que nadie la haya pedido, y ninguna comprobación obligatoria depende de que alguien la corra |

**Detalle adicional**

| # | Pregunta | Respuesta |
|---|---|---|
| 17 | Ciclo de vida | La transcripción no se borra ni se edita después. Es registro de lo que pasó |
| 24 | Datos sensibles | Una clave pegada en el chat se guarda enmascarada, dejando la marca de que se enmascaró |
| 25 | Convivencia | Si una sesión se corta sin cierre, lo escrito hasta ahí queda igual de válido |

## 6. Usuarios y actores

| Actor | Rol en el proceso | Necesidad principal |
|---|---|---|
| La persona | Trabaja, sin acordarse de nada | Que las cosas pasen solas |
| La sesión siguiente | Lee lo que quedó escrito | Encontrar el porqué de lo decidido |

**Volumetría estimada.** Varias sesiones por día, cada una con decenas de intercambios.

## 7. Criterios de aceptación de la épica

- [ ] **CAE-01** Cada sesión queda escrita a medida que pasa, sin que nadie lo pida.
- [ ] **CAE-02** Cada intercambio lleva la hora leída del reloj de la máquina, y la que no se registró se marca como tal.
- [ ] **CAE-03** Las comprobaciones obligatorias se disparan en el momento del trabajo.
- [ ] **CAE-04** Una clave pegada en el chat no llega literal al repositorio.
- [ ] **CAE-05** Un cambio de reglas sin versión ni registro no se puede guardar.
- [ ] **CAE-06** Ningún automatismo aprueba en nombre de la persona.

## 8. Métricas de éxito

| Métrica | Línea base | Meta | Cuándo se mide | Dónde |
|---|---|---|---|---|
| Sesiones sin transcripción | Todas, hoy | Ninguna | Cada semana | Carpeta de sesiones |
| Comprobaciones obligatorias que dependen de correrse a mano | Todas, hoy | Ninguna | Al terminar la épica | Lista de automatismos |

## 9. Historias de usuario

| ID | Título | Prioridad | Estimación |
|---|---|---|---|
| [HU-001](HU-001-transcripcion-de-la-sesion/HU-001-transcripcion-de-la-sesion.md) | Escribir la sesión a medida que pasa, con hora del reloj | Must | M |
| [HU-002](HU-002-enmascarar-claves/HU-002-enmascarar-claves.md) | Enmascarar una clave antes de que quede escrita | Must | M |
| [HU-003](HU-003-disparo-al-escribir-un-archivo/HU-003-disparo-al-escribir-un-archivo.md) | Disparar las comprobaciones al escribir un archivo | Must | M |
| [HU-004](HU-004-control-del-mensaje-de-cambio/HU-004-control-del-mensaje-de-cambio.md) | Controlar el mensaje con que se guarda un cambio | Must | S |
| [HU-005](HU-005-cambio-de-reglas-con-version/HU-005-cambio-de-reglas-con-version.md) | Impedir guardar un cambio de reglas sin versión ni registro | Must | M |
| [HU-006](HU-006-bateria-antes-de-publicar/HU-006-bateria-antes-de-publicar.md) | Correr la batería completa antes de publicar | Should | M |
| [HU-007](HU-007-recoger-lo-guardado-por-fuera/HU-007-recoger-lo-guardado-por-fuera.md) | Recoger al abrir sesión lo que quedó guardado por fuera del repositorio | Should | S |
| [HU-008](HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md) | El enganche que sostiene el resumen de la sesión | Must | M |
| [HU-009](HU-009-lo-que-rige-cada-frase-llega-puesto/HU-009-lo-que-rige-cada-frase-llega-puesto.md) | Lo que gobierna cada frase llega puesto al abrir la sesión | Must | M |
| [HU-010](HU-010-la-regla-llega-al-escribir-el-archivo/HU-010-la-regla-llega-al-escribir-el-archivo.md) | El capítulo que rige lo que se escribe llega al escribirlo | Must | M |
| [HU-011](HU-011-donde-termina-el-estandar/HU-011-donde-termina-el-estandar.md) | Dónde termina el estándar y dónde empieza el adaptador | Should | M |
| [HU-012](HU-012-hacer-cumplir-lo-que-solo-se-recuerda/HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md) | Hacer cumplir lo que hoy solo se recuerda | Must | M |
| [HU-013](HU-013-el-checkpoint-se-reclama-solo/HU-013-el-checkpoint-se-reclama-solo.md) | El checkpoint de la fase se reclama solo | Should | S |
| [HU-014](HU-014-el-consumo-se-ve-a-tiempo/HU-014-el-consumo-se-ve-a-tiempo.md) | El consumo de la sesión se ve mientras se puede actuar | Should | S |

## 10. Consideraciones técnicas

### 10.1 Componentes afectados

| Componente | Impacto | Observaciones |
|---|---|---|
| Automatismos | Nuevo | |
| Programas de comprobación | Sin cambio | Se invocan tal como están |
| Transcripción de sesiones | Nuevo | |

### 10.2 Decisiones de arquitectura

- El automatismo se genera durante la instalación, no se escribe a mano en cada proyecto, para que llegue igual a todos.
- Lo que detiene el trabajo se limita a lo rápido. Un control lento se termina saltando, y eso es peor que no tenerlo.

### 10.4 Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| Rapidez | Lo que se dispara en medio del trabajo no puede hacer esperar |
| Tolerancia a fallas | Si el automatismo falla, lo dice; no deja el trabajo a medias en silencio |
| Fidelidad | La transcripción es literal, no un resumen |

## 11. Dependencias

| ID | Dependencia | Tipo | Estado |
|---|---|---|---|
| DEP-01 | EP-004, porque son las comprobaciones que se disparan | Interna | Bloqueante |
| DEP-02 | EP-007, porque los automatismos llegan al proyecto con la instalación | Interna | Bloqueante |

## 12. Riesgos

| ID | Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|---|
| R-01 | Que un control lento haga que la gente lo desactive | Media | Alto | Solo lo rápido detiene; lo lento se corre aparte |
| R-02 | Que enmascarar de más corrompa la transcripción | Media | Alto | Se enmascara solo lo que tiene forma inequívoca de clave |
| R-03 | Que la sesión se corte antes de escribir el último intercambio | Alta | Bajo | Se escribe después de cada intercambio, no al final |

## 13. Supuestos y restricciones

**Supuestos**

- La herramienta con que se trabaja permite disparar un programa en momentos definidos.

**Restricciones**

- El reloj es el de la máquina. No hay servicio de hora externo, porque todo funciona sin internet.

## 14. Hoja de ruta

| Fase | Contenido | HU |
|---|---|---|
| Fase 1 | Transcripción y enmascarado | HU-001, HU-002 |
| Fase 2 | Disparo de comprobaciones y control del mensaje | HU-003, HU-004 |
| Fase 3 | Control de versión y batería previa a publicar | HU-005, HU-006 |
| Fase 4 | Recogida de lo que quedó por fuera | HU-007 |

## 15. Definition of Ready

- [ ] Momentos de disparo identificados
- [ ] Formato de la transcripción definido

## 16. Definition of Done

- [ ] Todas las historias obligatorias aceptadas
- [ ] Una sesión de prueba queda escrita completa sin pedirlo
- [ ] Ningún automatismo aprueba en nombre de la persona
- [ ] Lo que detiene dice cómo saltarse el control

## 17. Bitácora de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-13 | Ing. José Dúmar Jiménez Ruíz | Creación de la épica desde el brief |
| 2026-08-20 | Ing. José Dúmar Jiménez Ruíz | Nacen HU-013 y HU-014 desde los pendientes 64 y 65; el 66 baja como fase B de HU-009 |
