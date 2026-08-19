# Pendiente · Las señales no tienen dónde escribirse

**Estado:** **cerrado** el 2026-08-18. Anotado el 2026-08-14.

| | |
|---|---|
| **Historia de usuario** | [EP-006 · HU-002 — Guardar en el repositorio](../../documentacion/epicas/EP-006-memoria-de-lo-aprendido/HU-002-guardar-en-el-repositorio/HU-002-guardar-en-el-repositorio.md) — la señal es memoria de lo aprendido, y lo que falta es dónde se guarda |

## El problema

`13·DOC5` manda registrar como señal lo que no se recupera del código. La plantilla existe. El archivo donde escribirlas, en este repositorio, no existía: se creó el 2026-08-14 con las primeras cinco, después de una sesión entera de la que casi todo lo aprendido se quedó en la transcripción.

Eso es lo mismo que ya pasó con el histórico de sesiones. Se resolvió cuando dejó de depender de que alguien se acordara.

## Qué falta

**1. El enganche.** Que al aparecer una decisión o un aprendizaje se recuerde escribir la señal, en el momento. Al cerrar la sesión no sirve: un chat no tiene final.

**2. El molde corto.** Cuatro campos: qué pasó, por qué importa, qué se decidió y dónde queda. La plantilla actual tiene siete, y siete campos se llenan las dos primeras veces.

**3. La separación.** Lo que se aprendió va a señales; lo que falta hacer, a `pendientes/`. Hoy se confunden porque los dos salen del mismo momento.

## El límite

Decidir qué merece ser señal es criterio. Lo que se automatiza es el recordatorio y el formato, no el juicio.

---

# Cómo cerró — 2026-08-18

**Los tres puntos.**

## 1 · El enganche

[validadores/hook_senales.py](../../validadores/hook_senales.py), conectado a `UserPromptSubmit`. Recuerda escribir la señal **en el turno**, no al cerrar — porque al cerrar no sirve: un chat no tiene final y nadie sabe cuál fue el último mensaje hasta mucho después.

**Lo difícil no era que avisara: era que no se volviera ruido.** Un aviso que sale en cada turno se deja de leer, y entonces vale lo mismo que no tenerlo — es exactamente lo que el [58](nada-hace-cumplir-id9.md) describe con `ID9`, donde anotar el incumplimiento se volvió el sustituto de corregirlo.

Tres condiciones lo evitan, y las tres tienen su prueba:

- **Una vez por sesión.** La marca vive dentro del propio archivo de señales, en un comentario que no se ve al leerlo. Un temporal se borraría al reiniciar y el aviso volvería a salir.
- **Solo si el proyecto lleva señales.** Sin el archivo no avisa ni lo crea.
- **Nunca escribe una señal.** Reconocer qué merece serlo es criterio, y es del agente. La prueba cuenta las señales antes y después.

## 2 · El molde corto

De siete campos a **cuatro**: qué pasó · por qué importa · qué se decidió · dónde queda.

El pendiente lo decía con precisión: *«siete campos se llenan las dos primeras veces»*. A la tercera la señal no se escribe, y una señal no escrita es peor que una incompleta.

Lo que se quitó no se perdió: **la fecha y quién la escribió ya los guarda el control de versiones**, y el alcance y las relaciones se dicen en el texto cuando hacen falta.

## 3 · La separación

La plantilla abre ahora con la pregunta que separa señal de pendiente:

| Si la frase dice... | Es | Va a |
|---|---|---|
| qué pasó y qué se decidió | Señal | `documentacion/senales.md` |
| qué falta hacer | Pendiente | `pendientes/`, con su historia |

**Una misma conversación suele dejar las dos**, y por eso se confunden. El enganche lo repite en su aviso.

## El límite, respetado

Decidir qué merece ser señal sigue siendo criterio. **Lo que se automatizó es el recordatorio y el formato, no el juicio** — que era la línea que este pendiente trazaba.

## Cómo quedó comprobado

[validadores/tests/test_enganche_de_senales.py](../../validadores/tests/test_enganche_de_senales.py), 10 casos. Siete al aviso y tres a que **no detenga el trabajo**: sale con código 0 sobre una carpeta vacía, sobre una ruta que no existe y sobre este repositorio. Un enganche que rompe el turno es peor que el problema que resuelve.
