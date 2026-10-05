# HU-010 · El gasto se ve por los demás niveles


---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-010 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens en vivo](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/consumo/`, `proyectos/cimiento/core/herramientas/recuperar.py` |
| **Tipo** | Funcional |
| **Prioridad** | Could: décima de la épica |
| **Estimación** | L |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien mantiene Cimiento
- **Quiero** ver el gasto también por mensaje y palabra clave, por lo que llena el contexto, por herramienta, por agente auxiliar, por modelo, por tipo de token y por trabajo
- **Para** saber cuánto cuesta cada clase de pedido y cada análisis, HU o fase, y qué conviene automatizar

---

## 3. Contexto y descripción

La HU-008 muestra la primera tanda de niveles. Esta suma la segunda ([épica](../epica.md); análisis 1 del pendiente 119, acuerdo 7 y punto 10).

Verificado el 2026-10-05 en los `.jsonl`:

- Las líneas del agente no dicen a qué mensaje responden; las del usuario traen `promptId`. Cada llamada es del último mensaje anterior a ella.
- Cada `tool_use` trae el nombre de la herramienta, y su `tool_result` el resultado.
- Los agentes auxiliares escriben en `«sesión»/subagents/agent-«id».jsonl`, con su tipo en `agent-«id».meta.json`.
- Ningún dato dice qué trabajo estaba activo. El aviso de acuerdos nombra fases de otras sesiones, así que no sirve; las rutas que se tocan en el turno sí lo dicen.

### 3.1 Reglas de negocio

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | Por mensaje: cada llamada queda unida al mensaje del usuario que la originó, y el mensaje guarda su palabra clave de `01·C28`, no su texto | Acuerdo 7; RNF-01 de la HU-006 |
| RN-02 | Por trabajo: un mensaje es del análisis o de la fase cuyos archivos se tocaron en su turno (`analisis-N.md` de un pendiente, o una carpeta `A-EP-…-HU-…`); si no tocó ninguno, queda sin trabajo | Acuerdo 7; propuesta del agente para cómo se cruza |
| RN-03 | Por herramienta: cada uso de una herramienta queda con su nombre y el tamaño de su resultado | Acuerdo 7 |
| RN-04 | Por agente auxiliar: se leen también sus `.jsonl`, y sus llamadas quedan con el tipo de agente | Acuerdo 7 |
| RN-05 | Por modelo y por tipo de token: con lo que ya guarda cada llamada | Acuerdo 7 |
| RN-06 | Lo que llena el contexto: lo que entró por enganches, por archivos leídos y por otras herramientas, frente al contexto más grande que alcanzó una llamada | Acuerdo 7; propuesta del agente para cómo se mide |
| RN-07 | Todo se ve en el tablero de la HU-008, con sus mismos filtros | Acuerdo 2 |

### 3.2 Supuestos

- Los `.jsonl` siguen la forma verificada el 2026-10-05.

### 3.3 Fuera de alcance

- El mensaje de un agente auxiliar: sus llamadas no se unen a un mensaje del usuario.
- La palabra clave de un mensaje que solo llegó por telemetría, que no trae el texto.

---

## 4. Criterios de aceptación

### CA-01 · El gasto queda por mensaje, palabra clave y trabajo

**Sale de:** análisis 1 del pendiente 119, punto 10.

```gherkin
Dado un .jsonl con dos mensajes, uno que empieza con «Hágalo» y edita un plan de fase, y otro con «Analicemos» que edita un análisis
Cuando se lee
Entonces cada llamada queda unida a su mensaje
Y cada mensaje queda con su palabra clave y su trabajo, sin su texto
```

**Cómo validarlo:**
1. Correr `python manage.py test core.consumo` → pasan los casos de mensajes y trabajo.

**Aprobado cuando:** las llamadas de cada mensaje y su palabra y trabajo coinciden con la muestra.

### CA-02 · El gasto queda por herramienta y por agente auxiliar

**Sale de:** análisis 1 del pendiente 119, punto 10.

```gherkin
Dado un .jsonl con Bash y Edit, y un agente auxiliar con su meta
Cuando se lee
Entonces cada herramienta queda con el tamaño de su resultado
Y las llamadas del auxiliar quedan con su tipo de agente
```

**Cómo validarlo:**
1. Correr `python manage.py test core.consumo` → pasan los casos de herramientas y auxiliares.

**Aprobado cuando:** los tamaños y el tipo coinciden con la muestra.

### CA-03 · El tablero muestra los siete niveles

**Sale de:** análisis 1 del pendiente 119, punto 10.

```gherkin
Dado gasto guardado de los siete niveles
Cuando se abre «Gasto»
Entonces se ve por palabra clave, por trabajo, por herramienta, por agente auxiliar, por modelo, por tipo de token y lo que llena el contexto
Y los últimos mensajes con su gasto
```

**Cómo validarlo:**
1. Correr `python manage.py test core.consumo` → pasan los casos del tablero.
2. Abrir «Gasto» con el gasto real → se ven las secciones nuevas.

**Aprobado cuando:** cada sección trae los números de la muestra.

### Criterios de aceptación transversales

- [ ] Privacidad: del mensaje solo se guarda su palabra clave (`12`, [`00·N4`](../../../../base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)).
- [ ] Idempotencia: leer otra vez no duplica ([`03·D6`](../../../../base/03-datos.md#d6--concurrencia-e-idempotencia)).
- [ ] No regresión: lo existente sigue funcionando; la suite relacionada queda verde (`08`, [`02·F5`](../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)).

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | La parte del tablero que se recarga sigue por debajo de un segundo con el gasto real |

---

## 6. Diseño y referencias

Documento funcional: [análisis 1 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md), acuerdo 7 y punto 10.

Modelo de datos afectado: tablas nuevas de mensajes y de herramientas; `Llamada` suma su mensaje y su agente.

---

## 7. Tareas técnicas derivadas

- [ ] El lector une llamadas y mensajes, ve herramientas y lee auxiliares.
- [ ] Palabra clave y trabajo de cada mensaje.
- [ ] Modelos, migración y guardado.
- [ ] Las secciones del tablero.
- [ ] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-010-segunda-tanda` | CA-01 a CA-03 | (vacío) | [plan_trabajo.md](A-EP-025-HU-010-segunda-tanda/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-010-segunda-tanda/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-010-segunda-tanda/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-006, HU-008 | Alto |
| Riesgo | Un turno que no toca archivos de una fase queda sin trabajo | Se muestra como «sin trabajo», sin adivinar |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-05 | Claude | Creación de la HU desde el análisis 1 del pendiente 119 |
