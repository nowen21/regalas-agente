# 2026-10-05 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-10-05-sesion-2.md](../../2026-10-05-sesion-2.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

| Campo | Valor |
|---|---|
| Viene de | «...» |

---

## Hallazgos de esta sesión

### H-1 · La pantalla «Gasto» no dice por dónde empezar, y el gasto no llega en vivo ni queda dentro del proyecto

| Campo | Valor |
|---|---|
| Qué pasó | La pantalla «Gasto» pone 20 bloques seguidos con el mismo peso, sin el total del período, con datos repetidos y con lo que dice dónde ahorrar de último. Al revisarla se encontró que lo «en vivo» acordado se construyó con relojes que nadie acordó (la pantalla pregunta cada 10 segundos y el vigilante guarda cada 2), que el gasto se lee del almacén de Claude Code, fuera del proyecto y borrado a los 30 días, y que el histórico firma como del usuario los avisos internos de Claude Code |
| Por qué importa | La pantalla sirve para decidir qué pasar a un programa y así no se ve; lo que se construye sin acuerdo se aparta de lo pedido; lo que vive afuera incumple `01·C29` y se pierde; y la trazabilidad atribuye al usuario mensajes que no escribió |
| Versión | 2, según el [análisis 1 del pendiente 124](pendientes/124-la-pantalla-gasto-no-dice-por-donde-empezar/analisis-1.md) |
| Pendiente | [Pendiente 124: la pantalla «Gasto» no dice por dónde empezar, y el gasto no llega en vivo ni queda dentro del proyecto](pendientes/124-la-pantalla-gasto-no-dice-por-donde-empezar/pendiente.md) |

### H-2 · El enganche del análisis espera al histórico con un reloj

| Campo | Valor |
|---|---|
| Qué pasó | Al revisar dónde más había relojes, en el análisis 1 del pendiente 124, se encontró que `AnalisisEnCurso.esperar` revisa cada 0,25 segundos si el histórico ya anotó el turno |
| Por qué importa | Es una espera por reloj donde lo acordado es actuar por evento, y si el histórico tarda más de 5 segundos el análisis queda sin el turno |
| Pendiente | [Pendiente 128: el enganche del análisis espera al histórico con un reloj](pendientes/128-el-analisis-espera-al-historico-con-un-reloj/pendiente.md) |

### H-3 · El tapado de claves no reconoce las de Anthropic ni las variables con prefijo

| Campo | Valor |
|---|---|
| Qué pasó | Al probar EP-025·HU-025, una clave `sk-ant-api03-...` y una asignación `ANTHROPIC_API_KEY=...` quedaron en claro: el tapado no conoce la forma de Anthropic, y su patrón de asignación pide que la variable empiece en `api_key`, así que no ve las que traen un prefijo |
| Por qué importa | Las líneas de los `.jsonl` entran a la base pasando por ese tapado, el histórico también lo usa y el control de commits usa la misma lista; una clave sin tapar queda guardada, contra `00·N6` |
| Versión | 2, según el [análisis 1 del pendiente 129](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-002-enmascarar-claves/pendientes/129-el-enmascarador-no-reconoce-las-claves-de-anthropic/analisis-1.md) |
| Pendiente | [Pendiente 129: el tapado de claves no reconoce las de Anthropic ni las variables con prefijo](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-002-enmascarar-claves/pendientes/129-el-enmascarador-no-reconoce-las-claves-de-anthropic/pendiente.md) |

### H-4 · La plantilla del plan de pruebas y `cerrar_fase` piden la matriz de dos formas distintas

| Campo | Valor |
|---|---|
| Qué pasó | Al cerrar la fase B de EP-025·HU-025 con `manage.py cerrar_fase`, la orden no leyó la matriz escrita como pide la plantilla (enlaces y varios casos por fila) y tomó como plantilla un plan con comillas «» en el título |
| Por qué importa | Para cerrar hay que desobedecer la plantilla, y el cierre falla sin decir que el problema es el formato |
| Pendiente | [Pendiente 130](../../../documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/HU-016-cerrar-y-reabrir-una-fase-y-separar-los-cambios-por-sesion-son-funcionalidades-de-cimiento/pendientes/130-la-matriz-de-la-plantilla-no-la-lee-cerrar-fase/pendiente.md) |

### H-5 · Responder una pregunta del agente no tiene palabra clave

| Campo | Valor |
|---|---|
| Qué pasó | El usuario respondió «autorizo» a una pregunta del agente y el enganche de reglas lo tomó como mensaje sin palabra clave de `01·C28`: hubo que repetirlo con «Hágalo». El usuario aprobó sumar «Respondo» a la lista |
| Por qué importa | Cada respuesta que no encaja cuesta un mensaje más, y obliga a usar palabras que autorizan más de lo que la respuesta quería |
| Pendiente | [Pendiente 131: responder una pregunta del agente no tiene palabra clave](../2026-10-06/pendientes/131-responder-una-pregunta-no-tiene-palabra-clave/pendiente.md) |

---|---|
| Qué pasó | El 2026-10-06 12:37, el freno detuvo una orden de consola sobre `$F/plan_trabajo.md`: el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | Por crear: lo decide el análisis siguiente del pendiente de la fase |

---|---|
| Qué pasó | El 2026-10-06 13:00, el freno detuvo una orden de consola sobre `$TEMP/msg131.txt`: queda fuera del proyecto (04·S9). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | Por crear: lo decide el análisis siguiente del pendiente de la fase |

---|---|
| Qué pasó | El 2026-10-06 13:01, el freno detuvo una orden de consola sobre `prompts/disenio-tablero-consumo-tokens.md`: el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | Por crear: lo decide el análisis siguiente del pendiente de la fase |

---

## ¿Se puede cerrar la sesión?

Se cierra cuando ningún hallazgo queda sin anotar: cada uno enlaza su pendiente, y su pendiente existe. Anotar es dejar el archivo, no decir «quedó pendiente».

| Para cerrar | Estado |
|---|---|
| Todo hallazgo enlaza su pendiente | ☐ |
| Todo pendiente enlazado existe | ☐ |
| Lo que se hizo está aprobado y guardado | ☐ |

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

_(Si la sesión no dejó nada, se escribe «nada»: es un dato, no un olvido.)_

<!-- aviso: falta decir si la sesión se puede cerrar -->
