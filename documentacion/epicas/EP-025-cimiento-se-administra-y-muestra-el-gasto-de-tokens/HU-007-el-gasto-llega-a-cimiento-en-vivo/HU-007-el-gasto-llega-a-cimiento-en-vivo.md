# HU-007 · El gasto llega a Cimiento en vivo


---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-007 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens en vivo](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/consumo/`, `proyectos/cimiento/core/herramientas/instalar.py` |
| **Tipo** | Funcional |
| **Prioridad** | Must: séptima de la épica |
| **Estimación** | M |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien mantiene Cimiento
- **Quiero** que cada llamada de Claude Code llegue a la base de Cimiento a los pocos segundos de hacerse
- **Para** ver el gasto mientras se trabaja, sin esperar la lectura diaria de los `.jsonl`

---

## 3. Contexto y descripción

La HU-006 guarda el gasto leyendo los `.jsonl` una vez al día. Claude Code puede mandar cada llamada, con el estándar OpenTelemetry, a una dirección que se le configure: la llamada llega a los 5 segundos ([épica](../epica.md), §3; análisis 1 del pendiente 119, acuerdo 9).

Verificado en la documentación de Claude Code el 2026-10-05 (`monitoring-usage`):

- Cada llamada llega como el evento `claude_code.api_request`, en `POST /v1/logs`, con `session.id`, `request_id`, `model` y los tokens de entrada, salida, caché leída y caché creada.
- Cada herramienta que termina llega como `claude_code.tool_result`, con `tool_name`, `tool_use_id`, `tool_result_size_bytes` y, con `OTEL_LOG_TOOL_DETAILS=1`, sus parámetros.
- Ningún atributo dice la carpeta del proyecto. La sesión sí: su `.jsonl` está en la carpeta de Claude Code del proyecto.
- La telemetría se activa en la configuración del usuario (`~/.claude/settings.json`); la de un repositorio no puede activarla.

### 3.1 Reglas de negocio

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | Cimiento recibe los eventos en `/v1/logs` y los guarda en las mismas tablas de la HU-006: la llamada en `Llamada`, el archivo leído en `GastoDeArchivo` | Punto 7 |
| RN-02 | Una llamada que llega por telemetría y por el `.jsonl` queda una sola vez: las dos traen el mismo `request_id` | `03·D6`; verificado: en el `.jsonl`, `requestId` y `message.id` van uno a uno |
| RN-03 | El proyecto sale de la sesión: es el registrado cuya carpeta de Claude Code tiene `«sesión».jsonl`. Un evento de una sesión sin proyecto registrado se descarta | Propuesta del agente |
| RN-04 | Solo se reciben envíos de la misma máquina | Acuerdo 9: todo corre en una sola máquina; `04` |
| RN-05 | La instalación escribe en `~/.claude/settings.json` las variables que activan la telemetría, sin pisar las que ya estén | Punto 7; recuerdo «toda herramienta se autoinstala» |
| RN-06 | No se guarda texto: de un evento quedan tokens, modelo, nombres y rutas | RNF-01 de la HU-006 |
| RN-07 | La dirección que la instalación escribe usa el `PUERTO` del `.env` de Cimiento, el mismo con el que `manage.py runserver` levanta sin decirle otro (8015 en esta máquina; 8000 si no se declaró) | Propuesta del agente: el puerto ya existía |

### 3.2 Supuestos

- Cimiento está prendido mientras se trabaja. Lo que llegue con Cimiento apagado no entra por telemetría y lo recupera la lectura de los `.jsonl` (acuerdo 9).

### 3.3 Fuera de alcance

- Mostrar el gasto: HU-008.
- Las métricas de OpenTelemetry (`/v1/metrics`): repiten lo que traen los eventos.
- Prender Cimiento solo al encender la máquina.

---

## 4. Criterios de aceptación

### CA-01 · Una llamada llega y queda guardada

**Sale de:** análisis 1 del pendiente 119, punto 7.

```gherkin
Dado un proyecto registrado con una sesión de Claude Code en curso
Cuando llega a /v1/logs un evento claude_code.api_request de esa sesión
Entonces la llamada queda en la base con su proyecto, sesión, modelo y tokens
Y un claude_code.tool_result de Read deja el archivo leído con su tamaño
```

**Cómo validarlo:**
1. Correr `python manage.py test core.consumo` → pasan los casos de recepción con un envío de muestra en formato OTLP JSON.

**Aprobado cuando:** la llamada y el archivo de la muestra quedan en la base con sus datos.

### CA-02 · Lo que no vale no se guarda

**Sale de:** análisis 1 del pendiente 119, punto 7.

```gherkin
Dado un envío desde otra máquina, un JSON roto o un evento de una sesión sin proyecto registrado
Cuando llega a /v1/logs
Entonces no se guarda nada
Y el envío de otra máquina recibe 403 y el JSON roto 400
```

**Cómo validarlo:**
1. Correr `python manage.py test core.consumo` → pasan los casos de envío rechazado.

**Aprobado cuando:** la base queda igual en los tres casos.

### CA-03 · La misma llamada por los dos caminos cuenta una vez

**Sale de:** análisis 1 del pendiente 119, acuerdo 9.

```gherkin
Dado una llamada que llegó por telemetría
Cuando la lectura del .jsonl encuentra la misma llamada, o el evento llega otra vez
Entonces sigue habiendo una sola llamada
Y queda con el identificador del mensaje del .jsonl
```

**Cómo validarlo:**
1. Correr `python manage.py test core.consumo` → pasan los casos de los dos caminos, en los dos órdenes.

**Aprobado cuando:** hay una sola fila por llamada.

### CA-04 · La instalación activa la telemetría

**Sale de:** análisis 1 del pendiente 119, punto 7.

```gherkin
Dado la configuración del usuario de Claude Code
Cuando se instala el estándar en su propia carpeta
Entonces ~/.claude/settings.json queda con las variables que mandan los eventos a Cimiento
Y lo que el usuario ya tenía queda igual
```

**Cómo validarlo:**
1. Correr las pruebas `ActivarLaTelemetria` de `core/herramientas/tests_instalacion.py` → pasan.
2. Correr `python validadores/instalar.py "«carpeta del estándar»"` → aparece el paso de activar la telemetría.

**Aprobado cuando:** las variables quedan y las demás claves no cambian.

### Criterios de aceptación transversales

- [ ] Validación: un dato inválido se rechaza y **el estado no cambia** (`04`, `03`).
- [ ] Idempotencia: reintentar o doble-enviar **no duplica** efectos ([`03·D6`](../../../../base/03-datos.md#d6--concurrencia-e-idempotencia)).
- [ ] Privacidad: no se guarda texto de mensajes ni de herramientas (`12`, [`00·N4`](../../../../base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)).
- [ ] No regresión: lo existente sigue funcionando; la suite relacionada queda verde (`08`, [`02·F5`](../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)).

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Seguridad** | La ruta no pide cuenta, porque Claude Code no tiene una; por eso solo acepta envíos de la misma máquina |
| RNF-02 | **Privacidad** | De los parámetros de una herramienta solo se guarda la ruta del archivo leído |

---

## 6. Diseño y referencias

Documento funcional: [análisis 1 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md), acuerdo 9 y punto 7.

Contrato: OTLP/HTTP con JSON, `POST /v1/logs`, respuesta `200` con `{}`.

Modelo de datos afectado: `Llamada` suma el identificador de la solicitud (`request_id`).

---

## 7. Tareas técnicas derivadas

- [ ] Leer un envío OTLP JSON, sin Django.
- [ ] La ruta `/v1/logs` y el guardado sin duplicar.
- [ ] El `.jsonl` reconoce la llamada que ya llegó por telemetría.
- [ ] La instalación activa la telemetría.
- [ ] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-007-recepcion-de-la-telemetria` | CA-01 a CA-04 | (vacío) | [plan_trabajo.md](A-EP-025-HU-007-recepcion-de-la-telemetria/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-007-recepcion-de-la-telemetria/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-007-recepcion-de-la-telemetria/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-006 | Alto |
| Riesgo | Claude Code cambie los nombres de los atributos | El lector del envío va aparte, con los nombres en un solo lugar, y lo que no entiende se salta |
| Riesgo | Cimiento apagado | El `.jsonl` recupera lo perdido |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-05 | Claude | Creación de la HU desde el análisis 1 del pendiente 119 |
