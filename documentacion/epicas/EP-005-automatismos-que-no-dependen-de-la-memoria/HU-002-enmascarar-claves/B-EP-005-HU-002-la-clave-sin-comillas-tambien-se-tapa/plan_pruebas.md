# Plan de Pruebas — Fase `B-EP-005-HU-002-la-clave-sin-comillas-tambien-se-tapa`   ·   `[CAPA 3]`

> **Retrodocumentado el 2026-08-27.** La fase se construyó y se cerró el 2026-08-22 y **este documento se quedó siendo la plantilla en blanco**: 363 líneas de molde con 36 marcadores sin reemplazar. Lo destapó la [HU-022](../../../EP-004-comprobacion-automatica/HU-022-un-documento-que-sigue-siendo-el-molde-no-cuenta/HU-022-un-documento-que-sigue-siendo-el-molde-no-cuenta.md).
>
> **No se inventa nada.** Los casos salen del [resultado_pruebas.md](resultado_pruebas.md), que sí se escribió y documenta qué entró y qué salió en cada uno. **Lo que no se puede reconstruir —qué se pensó antes de ejecutar— no se escribe.**

---

## 1. Propósito y alcance

Comprobar que **una clave pegada en el chat sin comillas también se tapa** antes de escribirse en la transcripción.

**Es núcleo blindado.** `00·N6` dice que una credencial no se escribe, no se registra y no se guarda — y **la transcripción se versiona**: de ahí no se borra, queda en el historial para siempre.

El enmascarador reusaba el patrón con que se buscan secretos **en código fuente**, donde el valor va entre comillas. **En un chat nadie las escribe**, así que `API_KEY=secreto`, `password: secreto` y una clave dicha en prosa pasaban en claro.

**Entra:** un patrón propio de la conversación —valor sin comillas y sin espacios—, las palabras `token`, `clave` y `contraseña`, y **la exigencia de que el valor traiga un número o mida doce o más**.

**No entra:** la clave dicha enteramente en prosa —*«el token de producción es X»*— cuando no hay dos puntos ni igual. Se dejó **por el riesgo de tapar de más**, que es lo que vuelve inútil un enmascarador.

---

## 2. Estrategia

**Los casos de lo que NO debe taparse pesan más que los de lo que sí**, y no es simetría: **un enmascarador que tapa de más se apaga a la semana**, y entonces no queda nada tapado.

**Y se mide contra el corpus real antes de dejarlo** (`20·M19`): un patrón nuevo se comprueba sobre el texto que de verdad existe, no sobre ejemplos escritos para que pase.

**Ninguna prueba usa una credencial real ni inventada que parezca real** (`00·N6`): los valores son cadenas evidentemente falsas.

---

## 3. Casos de prueba

### Lo que sí se tapa

| Caso | Qué entra | Qué debe salir |
|---|---|---|
| **CP-001** · asignación sin comillas | `API_KEY=supersecreto123456` | Se tapa **el valor, no la variable** |
| **CP-002** · con dos puntos | `password: MiClave123456` | Se tapa |
| **CP-003** · la palabra en español | `la contraseña: Patito2026` | Se tapa |
| **CP-004** · valor largo sin números | `secret=abcdefghijklmnop` | Se tapa |

### Lo que **no** se tapa, que es la mitad que sostiene esto

| Caso | Qué entra | Qué debe salir |
|---|---|---|
| **CP-005** · código pegado en el chat | `clave = h.regla or algo` | **No** se tapa |
| **CP-006** · valor corto y sin números | `token: xyz` | **No** se tapa |
| **CP-007** · lee del entorno | `API_KEY=os.environ[...]` | **No** se tapa — es la forma correcta |
| **CP-008** · un molde | `password: changeme` | **No** se tapa — taparlo vuelve ilegible un ejemplo |
| **CP-009** · una frase normal | «La clave del asunto es que el proceso sirva» | **No** se toca |

**El `CP-005` es el que fijó el diseño.** Al medir sobre el repositorio apareció `clave = h.regla`, que es **código pegado, no una credencial** — y fue esa medición la que obligó a exigir un número o una longitud mínima. Sin ese caso, el enmascarador habría tapado código.

**El `CP-007` es el peor de tapar:** es exactamente lo que se quiere que la gente haga. Taparlo enseñaría lo contrario.

---

## 4. Criterio de aprobación

- Los nueve casos, ejecutados.
- **Cero falsos positivos sobre el histórico completo del repositorio**, medido antes de dejarlo.
- La marca es `«enmascarado»`, **la misma que el estándar ya usa**, no una inventada.
- La suite en verde.

---

## 5. Qué se ejecutó, y con qué resultado

Está en el [resultado_pruebas.md](resultado_pruebas.md). En corto: sobre el histórico completo de este repositorio el patrón nuevo tocaría **cero líneas** — ningún falso positivo en el corpus real. Y sobre el resto del repositorio apareció el único que importaba, `clave = h.regla`, que **no se tapa**.

---

## 6. Herramientas y datos

`unittest`, y el histórico completo del repositorio como corpus real. **Ninguna prueba usa credenciales** (`00·N6`): los valores de los casos son cadenas evidentemente falsas.

---

## 7. Control de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1 | 2026-08-27 | **Retrodocumentado.** La fase cerró el 2026-08-22 sin este documento |
