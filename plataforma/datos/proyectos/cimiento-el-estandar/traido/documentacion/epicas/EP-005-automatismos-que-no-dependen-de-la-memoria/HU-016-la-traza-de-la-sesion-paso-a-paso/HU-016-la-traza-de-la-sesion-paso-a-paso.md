# HU-016 — La traza de la sesión, paso a paso

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-016 |
| **Épica / Feature** | [EP-005 Automatismos que no dependen de la memoria](../epica.md) |
| **Módulo / Componente** | Automatismos — lectores de la sesión |
| **Tipo** | Técnica |
| **Prioridad** | Should |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Hecha |

---

## 2. Narrativa

- **Como** quien revisa qué hizo el agente en una sesión, propia o de un proyecto heredero
- **Quiero** una línea de tiempo paso a paso: hora, herramienta, qué se le pidió, cuánto tardó y si falló
- **Para** reconstruir cómo pasó algo sin leer la transcripción entera, y medir cuántos pasos cuesta una fase

---

## 3. Contexto y descripción

De una sesión queda **qué se dijo** (`historico-chat/`, por [HU-001](../HU-001-transcripcion-de-la-sesion/HU-001-transcripcion-de-la-sesion.md)) y **cuánto costó** (por [HU-014](../HU-014-el-consumo-se-ve-a-tiempo/HU-014-el-consumo-se-ve-a-tiempo.md)). No queda **qué se ejecutó**. La transcripción interna de la herramienta lo tiene: en las líneas del agente hay bloques `tool_use` (nombre, argumentos, hora) y en las del usuario bloques `tool_result` (el `tool_use_id` al que responden, `is_error`, hora). Nadie los lee.

Es un lector sobre un archivo que ya existe, como `presupuesto`: no agrega enganches ni toca los proyectos.

Sale del [pendientes/hecho/la-sesion-tiene-su-traza.md](../../../../pendientes/hecho/la-sesion-tiene-su-traza.md).

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | La fuente es la transcripción de la sesión, un archivo de líneas JSON. Un paso es un bloque `tool_use`; su respuesta, el bloque `tool_result` con el mismo `tool_use_id`. La duración es la diferencia entre las dos marcas de tiempo |
| RN-02 | Cada paso se escribe en una fila: número, hora de inicio, herramienta, resumen de la entrada en una línea (la ruta, el comando, la URL o el patrón, recortado a 80 caracteres), duración, y estado (`ok`, `error`, o `sin respuesta` si ningún `tool_result` lo contestó) |
| RN-03 | Al final va el cierre: cuántos pasos, cuántos por herramienta, cuántos errores, el paso más lento y la duración entre el primer paso y la última respuesta |
| RN-04 | No copia el contenido de ningún resultado ni de ninguna respuesta del agente: ahí pueden ir claves y datos. Solo la entrada recortada y el estado |
| RN-05 | Es un lector a demanda: `validar.py traza <transcripción>` imprime la traza. Con `--escribir` y `--raiz`, la deja en `historico-chat/trazas/<nombre>.md`, donde `<nombre>` es el del archivo de `historico-chat/` que lleva la marca `<!-- sesion: <id> -->` de esa sesión, y agrega su línea al `README.md` de `trazas/` |
| RN-06 | Una línea ilegible se salta; un archivo que no existe o no tiene ningún paso se dice en una frase, sin traza de error |
| RN-07 | Vive en `validadores/` sin nombrar la herramienta: lee un formato de transcripción (líneas JSON con bloques `tool_use`/`tool_result`), como ya hacen `brevedad` y `presupuesto`. `validar.py amarre` lo comprueba |

### 3.2 Supuestos

- Las marcas de tiempo de la transcripción están en ISO 8601 con zona (`2026-08-20T14:02:13.634Z`), como se leyó hoy en una transcripción real.
- El `id` de sesión está en el nombre del archivo de la transcripción y en el campo `sessionId` de sus líneas.

### 3.3 Fuera de alcance

- Escribir la traza sola al cerrar la sesión: sería un enganche y es otra historia.
- Medir lo que la herramienta no registra: el razonamiento, lo que el agente leyó sin herramienta.
- Tapar claves dentro de la entrada de un comando: la entrada se recorta y los resultados no se copian; lo demás es de `enmascarar`.

---

## 4. Criterios de aceptación

### CA-01 — La línea de tiempo de una sesión

```gherkin
Dado que una transcripción tiene tres pasos, uno de ellos con error
Cuando se corre el lector sobre ella
Entonces salen tres filas en orden, cada una con hora, herramienta, entrada recortada, duración y estado
Y la del error dice error
```

**Cómo validarlo:**

1. Armar una transcripción sintética con tres `tool_use` (`Read`, `Bash`, `WebFetch`) y sus tres `tool_result`, el del `Bash` con `is_error: true`, separados por segundos conocidos.
2. Correr `validar.py traza <archivo>`. Resultado esperado: tres filas numeradas 1, 2 y 3; la fila 2 dice `Bash`, su comando y `error`; las duraciones coinciden con los segundos puestos.
3. Comprobar que el contenido de los `tool_result` no aparece en la salida. Resultado esperado: no aparece.
- **Aprobado cuando:** las tres filas salen en orden con los cinco datos y el contenido no se copió.

### CA-02 — El cierre dice los totales

```gherkin
Dado la misma transcripción
Cuando termina la traza
Entonces el cierre dice 3 pasos, 1 error, el conteo por herramienta, el más lento y la duración total
```

**Cómo validarlo:**

1. Leer las últimas líneas de la salida de CA-01. Resultado esperado: «3 pasos», «1 error», una línea por herramienta con su cuenta, el nombre del paso más lento y la duración entre el primer `tool_use` y el último `tool_result`.
- **Aprobado cuando:** los cinco totales coinciden con los datos sintéticos.

### CA-03 — Con `--escribir` queda junto al histórico, indexada

```gherkin
Dado un proyecto con historico-chat/ y un histórico cuya marca es la sesión de la transcripción
Cuando se corre el lector con --escribir --raiz <proyecto>
Entonces aparece historico-chat/trazas/<mismo nombre>.md con la traza
Y historico-chat/trazas/README.md tiene su línea
```

**Cómo validarlo:**

1. En una carpeta temporal crear `historico-chat/2026-08-20-sesion.md` con `<!-- sesion: abc -->` y una transcripción `abc.jsonl`.
2. Correr `validar.py traza abc.jsonl --escribir --raiz <carpeta>`. Resultado esperado: existe `historico-chat/trazas/2026-08-20-sesion.md` con las filas, y `historico-chat/trazas/README.md` con una línea que lo enlaza.
3. Correr de nuevo. Resultado esperado: el archivo se reescribe y el índice no duplica la línea.
4. Correr con `--escribir` sobre una carpeta sin `historico-chat/`. Resultado esperado: una frase que lo dice, código 1, nada escrito.
- **Aprobado cuando:** escribe, indexa una sola vez, y sin histórico no inventa nada.

### CA-04 — Lo raro no revienta

```gherkin
Dado una transcripción con una línea ilegible, un tool_use sin tool_result, y otra vacía
Cuando se corre el lector
Entonces la línea ilegible se salta, el paso sin respuesta dice «sin respuesta», y la vacía da una frase y nada más
```

**Cómo validarlo:**

1. Transcripción con una línea «esto no es JSON» entre pasos válidos. Resultado esperado: la traza sale igual.
2. Transcripción con un `tool_use` sin su `tool_result`. Resultado esperado: fila con estado «sin respuesta» y duración vacía.
3. Archivo vacío, y ruta inexistente. Resultado esperado: una frase cada uno, código 1, sin traza de error de Python.
- **Aprobado cuando:** los cuatro casos se comportan así.

### Criterios de aceptación transversales

- [x] **Límites** — vacío, ilegible, sin respuesta, sin marcas de tiempo (duración vacía).
- [x] **Privacidad** — ningún contenido de resultado se copia (RN-04).
- [x] **No regresión** — las suites que ya corrían siguen en verde.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | Una transcripción de 1 MB se traza en menos de 2 segundos |
| RNF-02 | **Privacidad** | La salida no contiene ningún fragmento del contenido de un `tool_result` |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** N/A.
- **Documento funcional:** la especificación del módulo, [documentacion/automatismos/spec.md](../../../automatismos/spec.md).
- **Contrato de API:** N/A.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Lector que empareja `tool_use` con `tool_result`, calcula duraciones y arma filas y cierre.
- [ ] Subcomando `traza` en `validar.py`, con `--escribir` y `--raiz`.
- [ ] Escritura en `historico-chat/trazas/` con su índice.
- [ ] Casos de prueba.
- [ ] Especificación, mapa del sitio, README del histórico.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase (`02·F12.6`) | CA que cubre | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|
| [A-EP-005-HU-016-el-lector-de-la-traza](A-EP-005-HU-016-el-lector-de-la-traza/README.md) | CA-01 a CA-04 | [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-016-la-traza-de-la-sesion-paso-a-paso/A-EP-005-HU-016-el-lector-de-la-traza/plan_trabajo.md](A-EP-005-HU-016-el-lector-de-la-traza/plan_trabajo.md) | [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-016-la-traza-de-la-sesion-paso-a-paso/A-EP-005-HU-016-el-lector-de-la-traza/plan_pruebas.md](A-EP-005-HU-016-el-lector-de-la-traza/plan_pruebas.md) | [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-016-la-traza-de-la-sesion-paso-a-paso/A-EP-005-HU-016-el-lector-de-la-traza/resultado_pruebas.md](A-EP-005-HU-016-el-lector-de-la-traza/resultado_pruebas.md) | Cerrada el 2026-08-20: Cumple |

**Qué documento responde qué**, para no buscar en el que no es:

| Pregunta | Documento |
|---|---|
| Qué se pide y cuándo se da por aceptado | Esta HU |
| Qué se va a hacer, en qué orden y sobre qué archivos | `plan_trabajo.md` de la fase |
| Con qué casos se comprueba cada CA | `plan_pruebas.md` de la fase |
| Qué se ejecutó, con qué resultado, y si el CA quedó cumplido | `resultado_pruebas.md` de la fase |
| En qué estación va y qué la tiene detenida | `estado-fase.md` de la fase |
| Qué quedó hecho al final | `funcionalidad_implementada.md` de la fase |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-001 de esta épica: la marca `<!-- sesion: id -->` del histórico es lo que une la transcripción con su archivo | Medio |
| Dependencia | HU-014: el mismo archivo de transcripción, ya leído por `hook_presupuesto.py` | Bajo |
| Riesgo | Que la herramienta cambie el formato de la transcripción | El lector salta lo que no entiende y lo dice en el cierre; no revienta |
| Riesgo | Que la entrada recortada traiga una clave escrita en un comando | Se recorta a 80 caracteres y se documenta el límite; el histórico ya pasa por `enmascarar` |

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas y desbloqueadas

## 11. Definition of Done (DoD)

- [ ] Los cuatro criterios de aceptación verificados
- [ ] Trazada una sesión real de este repositorio
- [ ] Especificación, mapa del sitio y README del histórico al día
- [ ] Versionada (`20·M10`)
- [ ] El pendiente 73 cerrado nombrando la fase

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | No espera a nadie; puede ir antes o después de HU-015 |
| **N**egociable | Sí | Qué columnas lleva la fila y dónde se guarda se pueden discutir |
| **V**aliosa | Sí | Es la medida que falta junto al consumo |
| **E**stimable | Sí | Un lector, un subcomando, sus casos |
| **S**mall (pequeña) | Sí | Cuatro comportamientos |
| **T**esteable | Sí | Transcripciones sintéticas en carpetas temporales |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-20 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde el pendiente 73, que sale del H-6 de la sesión 5 del día |
| 2026-08-20 | Ing. José Dúmar Jiménez Ruíz | Fase A ejecutada y cerrada: nace `validadores/traza.py` con su subcomando; la primera traza real (191 pasos) queda en `historico-chat/trazas/`. 28.0.0 |
