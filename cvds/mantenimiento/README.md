# Mantenimiento: ¿cómo se sostiene vivo?   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito qué hay que hacer para que el estándar de trabajo heredable siga sirviendo después de entregado, y cuándo dejaría de valer la pena sostenerlo.

> **Escrito como si no hubiera nada construido.** Sale de lo que exigen las etapas anteriores, no del repositorio.

**Estado: BORRADOR** (2026-08-22, sin abrir).

---

## 1. Qué entra a esta etapa

| Qué se recibe | De dónde viene | ¿Aprobado? |
|---|---|---|
| Lo entregado, con su acta | Despliegue | No: no hay entrega todavía |
| La deuda declarada: sin línea base de revisión, generador al final, y la pantalla que solo lee | Implementación | No |
| Las exigencias de disponibilidad y de datos | Análisis | No |

## 2. Quién lo sostiene

| Qué actividad | Quién responde | Con qué frecuencia | Qué pasa si esa persona no está |
|---|---|---|---|
| Escribir y derogar reglas | El autor | Cuando aparece el incumplimiento | El estándar se congela en su última versión y sigue sirviendo |
| Publicar versiones y su registro | El autor | Al cerrar cada cambio | Los proyectos se quedan en la suya, y el aviso deja de tener qué informar |
| Atender a un proyecto que hereda | El autor | Cuando pregunte | Queda sin respuesta: **es el riesgo de una sola persona** |

## 3. Los respaldos

| Qué se respalda | Cada cuánto | Dónde queda | Cuánto se conserva | Última restauración probada |
|---|---|---|---|---|
| El estándar entero | En cada cambio guardado | Repositorio remoto | Todo el historial, sin caducidad | Pendiente |
| Lo que cada sesión dejó escrito | En el momento en que se escribe | Dentro del propio repositorio | Sin caducidad | Pendiente |
| La memoria de lo aprendido | En cada cambio guardado | Dentro del propio repositorio | Sin caducidad | Pendiente, y es la que más falta hace: es lo único que no se puede rehacer leyendo |
| Lo que un proyecto adoptó | Al instalar | En el repositorio de ese proyecto | Lo que conserve ese proyecto | Pendiente |

**Nada de esto está probado todavía.** Clonar el repositorio en una máquina limpia y abrir una sesión es la prueba, y no se ha hecho.

## 4. Qué se vigila

| Qué se mira | Cuándo se considera problema | Quién se entera, y cómo |
|---|---|---|
| Cuánto demora abrir la sesión | Más de dos segundos | El usuario, en el momento de abrir |
| Reglas escritas sin comprobación | Cuando una regla validable no tiene la suya | Una comprobación que las cuenta |
| Proyectos que quedaron atrás | Cuando su versión es anterior a la publicada | El aviso al abrir la sesión de ese proyecto |
| Comprobaciones que reprueban de más | Cuando alguien empieza a ignorar sus avisos | El usuario, y queda en la bitácora |
| Que una versión nueva rompa lo que servía | Cuando una prueba de lo ya existente falla al publicar | La publicación se detiene y lo dice |
| Que la memoria crezca sin que nadie la lea | Cuando lo guardado no se consulta en meses | Se revisa al cerrar cada versión |

## 5. Qué hacer cuando falla

| Síntoma | Qué revisar primero | Cómo se arregla | A quién se avisa |
|---|---|---|---|
| La sesión abre sin reglas | Que la ruta del estándar exista en ese proyecto | Se corrige la ruta y se vuelve a abrir | Al usuario, en el aviso de apertura |
| Una comprobación rechaza algo correcto | Qué caso la disparó | Se ajusta esa comprobación, nunca se apagan todas | Al usuario, con lo que se cambió |
| Un proyecto no puede actualizar | Si el desfase trae una derogación sin adoptar | Se adopta primero la derogación | A quien mantiene ese proyecto |
| Una credencial llegó a quedar escrita | Dónde quedó y desde cuándo | Se rota la credencial y se limpia el rastro | Al usuario, de inmediato |

**Qué se hace siempre, pase lo que pase:** anotar en la bitácora qué pasó, qué se hizo y qué lo causó, aunque se haya resuelto solo.

## 6. Las rutinas periódicas

| Rutina | Cada cuánto | Quién | Para qué |
|---|---|---|---|
| Restaurar el respaldo en una máquina limpia | Cada tres meses | El autor | Comprobar que el respaldo sirve, no que existe |
| Revisar las reglas sin comprobación | Al cerrar cada versión | El autor | Que no crezca lo que solo depende de la memoria |
| Barrer lo que el usuario pidió dos veces | Al cerrar cada versión | El autor | Convertir en regla lo que ya es costumbre |
| Releer el estándar entero | Una vez al año | El autor | Detectar lo que quedó sin uso o se contradice |

## 7. Cómo se pide un cambio

| Quién pide | Por dónde entra | Quién decide | Qué se le responde |
|---|---|---|---|
| El usuario | Como pendiente escrito | El autor | Si entra, con qué prioridad, y en qué versión saldría |
| Un proyecto que hereda | Como pendiente, con el caso que lo motivó | El autor | Si sirve a cualquier proyecto o solo al suyo |
| El agente, al toparse con un vacío | Como pendiente, en el momento | El autor | Si es regla nueva o interpretación de una existente |

## 8. El fin de vida

| Qué se define | Cómo queda |
|---|---|
| Cuándo se apaga | Cuando la herramienta deje de permitir enganches, o cuando el agente cumpla sin que haga falta escribirlo |
| Qué pasa con los datos | Quedan en el repositorio: son texto, se leen sin el estándar |
| A quién se avisa | A los proyectos que heredan, con una versión mayor que lo declare |

## 9. Los entregables de esta etapa, y a quién van

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Manual técnico y de operación | [plantillas/ciclo-vida-proyectos/18-manual-tecnico-y-de-operacion.md](../../plantillas/ciclo-vida-proyectos/18-manual-tecnico-y-de-operacion.md) | Quien opera | Pendiente |
| Bitácora de operación | [plantillas/ciclo-vida-proyectos/21-bitacora-de-operacion.md](../../plantillas/ciclo-vida-proyectos/21-bitacora-de-operacion.md) | Quien opera | Pendiente |
| Plan de mantenimiento | [plantillas/ciclo-vida-proyectos/22-plan-de-mantenimiento.md](../../plantillas/ciclo-vida-proyectos/22-plan-de-mantenimiento.md) | Usuario | Pendiente |
| Análisis de lo que falló feo | [plantillas/postmortem.md](../../plantillas/postmortem.md) | Equipo | Cuando ocurra |

## 10. Las puertas de esta etapa

| Qué no se puede hacer | Hasta que | Regla |
|---|---|---|
| Dar el estándar por operable | haya una restauración de respaldo probada | Sección 3 de este documento |
| Cerrar un incidente | quede escrito en la bitácora qué lo causó | Sección 5 de este documento |
| Hacer un cambio pedido | entre como pendiente y se baje a historia | Sección 7 de este documento |

## 11. La revisión de esta etapa

**Se revisa cada tres meses.** Última revisión: ninguna.

Lo que este documento deja a la vista antes de empezar: **el mantenimiento entero depende de una sola persona**. Mientras siga así, el fin de vida real del estándar no es el de la sección 8, es el día en que el autor deje de mantenerlo.

## 12. Qué de esta etapa cumple hoy el proyecto

> Del análisis del 2026-08-24 sobre la versión 33.4.0. El resumen de las siete etapas, y lo que este análisis no puede decir, están en [cvds/README.md](../README.md).

| Qué exige el ciclo | Qué lo cumple hoy | Dónde está |
|---|---|---|
| Por dónde entra una solicitud | Todo pedido se escribe como pendiente; 81 cerrados y 3 abiertos | [pendientes/](../../pendientes/README.md) |
| Un cambio grande vuelve a entrar por el ciclo | El pendiente no se ejecuta desde su archivo: baja a historia y se construye como fase | `02·F23` |
| Rutinas periódicas | Al cerrar cada versión se barre lo que el usuario pidió dos veces | `M20` y [plantillas/candidatas-a-regla.md](../../plantillas/candidatas-a-regla.md) |
| Versiones y su numeración | Mayor, menor y parche, con la regla de qué obliga a migrar | [CHANGELOG.md](../../CHANGELOG.md) y [VERSION](../../VERSION) |
| Quién sostiene | Una sola persona, y está dicho | [CLAUDE.md](../../CLAUDE.md) |

**A medias**

| # | Qué |
|---|---|
| 1 | los cuatro tipos de trabajo no se distinguen, así que no se puede decir cuánto se va en corregir |
| 2 | el impacto de un cambio se evalúa como grado de versión, no como qué se rompe |
| 3 | la vigilancia existe como [metricas/](../../metricas/README.md) y [validadores/rendimiento.py](../../validadores/rendimiento.py), sin umbrales ni aviso |
| 4 | qué hacer cuando falla está en [prompts/](../../prompts/) como casos sueltos |

**No existe**

| # | Qué |
|---|---|
| 1 | gravedad con tiempos de respuesta |
| 2 | bitácora de operación |
| 3 | plan de mantenimiento |
| 4 | fin de vida |

Y **ningún respaldo se ha restaurado nunca**: [validadores/respaldo.py](../../validadores/respaldo.py) comprueba el respaldo de los proyectos que heredan, no el de este.
