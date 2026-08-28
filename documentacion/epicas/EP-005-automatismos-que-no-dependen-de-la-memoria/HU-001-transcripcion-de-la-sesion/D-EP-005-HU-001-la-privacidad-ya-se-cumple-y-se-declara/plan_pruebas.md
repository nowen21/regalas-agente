# Plan de Pruebas — Fase `D-EP-005-HU-001-la-privacidad-ya-se-cumple-y-se-declara`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** el criterio de esta fase, con qué datos y cuándo se da por aprobado. Lo que se pide vive en la [HU-001](../HU-001-transcripcion-de-la-sesion.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que **lo que se enmascara no queda escrito en claro en la transcripción** — la exigencia transversal que la fase `A` dejó en rojo el 2026-08-22, con razón, porque entonces nada enmascaraba.

### 1.2 Alcance

**Entra:** que enmascare, que no enmascare de más, y que esté **conectado al enganche que escribe**.

**No entra:** construir enmascarado, ampliar qué se tapa, ni tocar el veredicto de la fase `A`.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| La fase [`A`](../A-EP-005-HU-001-retrodocumentar-la-transcripcion-de-la-sesion/resultado_pruebas.md) | El rojo original, y que ya nombraba a la `HU-002` como su destino |
| `S-061` | Un veredicto en rojo es una foto, y nadie la vuelve a mirar |
| `S-063` | Este rojo **fue cierto**; el otro que se revisó el mismo día, no |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| `enmascarar.enmascarar` | Que tape, y que **no** tape de más |
| `historico.py` | Que llame al enmascarado **antes** de escribir |
| `hook_historico.py` | Que sea el que escribe la transcripción |

---

## 3. Estrategia de pruebas

**Se ejecuta, no se lee.** Que un módulo exista y esté importado no es que tape: hoy mismo se afirmó tres veces sobre lo que no se había corrido.

**Y se sigue la cadena entera hasta quien escribe.** La exigencia habla de **lo que queda escrito en la transcripción**, no de lo que el módulo sabe hacer. Un enmascarado perfecto que nadie llama deja la transcripción igual de expuesta.

**Ninguna prueba usa credenciales** (`00·N6`), ni reales ni inventadas que lo parezcan. Es la regla que esta fase verifica: no se puede comprobar que algo no queda escrito escribiéndolo.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Los dos planes, aprobados.
- La línea base, medida antes de crear la carpeta.

### 4.2 Criterios de salida

- Los tres casos **ejecutados**, con su salida copiada.
- El `Estado` de la historia y su casilla, al día.
- La suite completa en verde, con conteo distinto de cero.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **cualquiera de las tres falla**. No hay veredicto parcial: si el enmascarado no está conectado, la exigencia sigue en rojo y esta fase cierra diciéndolo.

**Y se suspende también si la frase normal se tapa.** Un enmascarador que tapa de más se apaga, y entonces no queda nada tapado — declarar cumplida la privacidad con eso sería peor que dejarla en rojo.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| Transversal · Privacidad | CP-001 | De ejecución |
| Transversal · Privacidad, la otra mitad | CP-002 | Que **no** pase |
| Transversal · Privacidad · conexión | CP-003 | De sistema |

---

## 6. Casos de prueba

### CP-001 — Enmascara

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / transversal Privacidad |
| **Tipo** | De ejecución |
| **Prioridad** | Alta |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pasarle `API_KEY=supersecreto123456` | Sale `API_KEY=«enmascarado»` |
| 2 | Comprobar que **el nombre de la variable no se tapa** | Se conserva |
| 3 | La marca | Es `«enmascarado»`, la que el estándar ya usa, no una inventada |

---

### CP-002 — No enmascara de más

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / transversal Privacidad |
| **Tipo** | Que **no** pase |
| **Prioridad** | **Crítica** |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pasarle `la clave del asunto es que sirva` | **Sale intacto** |
| 2 | Comprobar que no se tocó ni un carácter | Idéntico |

**Por qué es el crítico:** declarar cumplida la privacidad con un enmascarador que tapa prosa normal sería **peor que dejarla en rojo**. Se apaga a la semana, y entonces no queda nada tapado — y encima la casilla dice que sí.

---

### CP-003 — Está conectado a quien escribe

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / transversal Privacidad · conexión |
| **Tipo** | **De sistema** |
| **Prioridad** | **Crítica** |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Seguir la cadena: el enganche que escribe la transcripción | `hook_historico.py` |
| 2 | Qué llama | `historico.anotar_usuario` y `anotar_agente` |
| 3 | Que **las dos** rutas enmascaren | El mensaje del usuario **y** la respuesta del agente |
| 4 | Que el enmascarado ocurra **antes** de escribir | Sí |

**Por qué es crítico:** la exigencia dice **«no queda escrito en claro en la transcripción»**. Un enmascarado que nadie llama la deja igual de expuesta. Es el defecto de `EP-002·HU-004`, donde el aviso estaba construido y probado **y el arranque no lo llamaba**.

**El paso 3 importa aparte:** si solo se enmascara el mensaje del usuario, una clave que el agente repita en su respuesta queda en claro.

---

## 7. Datos y ambientes de prueba

Cadenas evidentemente falsas. **Ninguna prueba usa credenciales** (`00·N6`), y ninguna escribe en la transcripción real.

---

## 8. Herramientas

Ejecución directa del módulo, y lectura de la cadena de llamadas. **No hace falta sabotaje:** esta fase no cambia código, y lo que comprueba ya tiene sus propias pruebas en la `HU-002`.

---

## 9. Gestión de defectos

| Severidad | Qué la define |
|---|---|
| Crítica | Tapa prosa normal, o no está conectado |
| Alta | No tapa lo que debe |
| Baja | Redacción |

Si aparece cualquiera, **la fase cierra con «No cumple»** y lo dice: la exigencia seguiría en rojo, y eso es información, no fracaso.

---

## 10. Cronograma

Un solo tramo. La suite completa al final.

---

## 11. Roles y responsabilidades

Una sola persona cumple los roles. El agente comprueba; el usuario aprueba.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Casos ejecutados | 3 de 3 |
| **Casos comprobados leyendo en vez de corriendo** | **0** |
| Prosa normal que se tapa | **0** |
| Rutas de escritura sin enmascarar | **0 de 2** |

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Dar por cumplido leyendo el código | Los tres casos ejecutan |
| Probar solo que tapa | `CP-002` prueba lo contrario, y es el crítico |
| Probar el módulo y no la cadena | `CP-003` sigue hasta el enganche |

---

## 14. Control de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1 | 2026-08-27 | Redacción inicial, junto con el plan de trabajo |

---

## 15. Aprobación

| Rol | Estado |
|---|---|
| Usuario | Pendiente. **No se toca nada hasta que este plan y el de trabajo estén aprobados** (`02·F4`) |
