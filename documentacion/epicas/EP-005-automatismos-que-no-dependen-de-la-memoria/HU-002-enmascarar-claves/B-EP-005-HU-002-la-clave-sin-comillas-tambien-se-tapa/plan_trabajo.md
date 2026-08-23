# Plan de Trabajo — Fase B-EP-005-HU-002-la-clave-sin-comillas-tambien-se-tapa (módulo Enganches de sesión)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. Se escribe **antes** de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-005-HU-002-la-clave-sin-comillas-tambien-se-tapa` |
| **Épica** | `EP-005` |
| **HU** | `HU-002` |
| **Módulo** | Enganches de sesión |
| **Fecha apertura** | 2026-08-22 |
| **Rama** | `main` |

**ORIGEN:** 📝 **Modifica fase.** Cierra en rojo lo que la fase A de esta misma historia dejó al ejecutarse el 2026-08-22, anotado entonces en el [pendiente 84](../../../../../pendientes/hecho/una-clave-pegada-sin-comillas-queda-en-claro.md).

---

## 1. Objetivo y alcance

**El problema.** El enmascarador reusaba el patrón con que se buscan secretos **en código fuente**, donde el valor va entre comillas. En un chat nadie las escribe, así que `API_KEY=secreto`, `password: secreto` y una clave dicha en prosa pasaban en claro a la transcripción, **que se versiona**. Es núcleo blindado: `00·N6` dice que una credencial no se escribe, no se registra y no se guarda.

**Lo que entra:**

- Un patrón propio de la conversación: el valor sin comillas y sin espacios.
- Se sumaron `token`, `clave` y `contraseña`, que son las que se dicen hablando.
- Se exige que el valor traiga un número o mida doce o más, para no tapar código.

**Fuera de alcance:** la clave dicha enteramente en prosa —«el token de producción es X»— sigue sin taparse cuando no hay dos puntos ni igual. Es el punto 2 del pendiente, y se dejó por el riesgo de tapar de más, que es el que vuelve inútil un enmascarador.

---

## 2. Análisis previo — línea base verificada

**Medido antes de dejarlo, que es lo que [`20·M19`](../../../../../base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md) pide.** Sobre el histórico completo de este repositorio el patrón nuevo tocaría **cero líneas**: ningún falso positivo en el corpus real. Y sobre el resto del repositorio apareció el único que importaba, `clave = h.regla`, que es código pegado y no una credencial. Esa medición fue la que obligó a pedir un número o una longitud.

### 2.1 Archivos que se crean o modifican

- `validadores/enmascarar.py`
- `validadores/tests/test_la_clave_sin_comillas_se_enmascara.py`

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Un patrón aparte para la conversación | Ensanchar el de código | Buscar secretos en código y taparlos en un chat son dos problemas distintos con la misma cara. Ensanchar el de código habría empeorado la búsqueda en código |
| El valor pide un número o doce caracteres | Cualquier valor de seis o más | Sin eso, `clave = h.regla` se tapaba. Un secreto casi siempre trae un número, y si no lo trae es largo |
| Se conserva el nombre de la variable | Tapar la línea entera | Quien lea la transcripción tiene que poder seguir entendiendo de qué se hablaba |

---

## 3. Verificación

Los casos del `resultado_pruebas` §2, y las suites que la fase toca. **La batería entera no**, que es lo que `02·F5` pone como INCORRECTO y que en esta misma jornada ya costó catorce minutos y once rojos que ya existían.

---

## 4. Reversión

Revertir el commit de la fase. Todo es aditivo sobre funciones que ya existían.

---

## 5. Reglas aplicadas

- [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), porque el pendiente baja a fase.
- [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md), por el alcance de la corrida.
- [`20·M19`](../../../../../base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md), porque se midió antes de dejar el criterio.
- `20·M10`, por la versión y el registro.

---

## 6. Cierre

**No se escribe acá.** Va en el `funcionalidad_implementada.md` de esta carpeta.
