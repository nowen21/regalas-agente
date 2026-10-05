# HU-006 · El gasto de cada llamada queda guardado


---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-006 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens en vivo](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/consumo/`, `adaptadores/claude-code/hook_presupuesto.py`, `proyectos/cimiento/core/herramientas/instalar.py` |
| **Tipo** | Funcional |
| **Prioridad** | Must: sexta de la épica |
| **Estimación** | L |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | En curso |

---

## 2. Narrativa

- **Como** quien mantiene Cimiento
- **Quiero** que el gasto de cada llamada de Claude Code quede guardado en la base, por proyecto, sesión, enganche y archivo leído
- **Para** saber qué conviene pasar a un programa, aunque Claude Code borre sus registros a los 30 días

---

## 3. Contexto y descripción

Claude Code anota cada llamada en `~/.claude/projects/«carpeta»/«sesión».jsonl` y borra esos archivos a los 30 días. Hoy `hook_presupuesto.py` los lee para sumar el consumo de la sesión, sin guardar nada ni separar por proyecto, enganche o archivo ([épica](../epica.md), §3).

### 3.1 Reglas de negocio

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | Se guarda cada llamada con proyecto, sesión, fecha, modelo y tokens de entrada, de caché creada, de caché leída y de salida | Análisis 1 del pendiente 119, acuerdos 7 y 8 |
| RN-02 | Se guarda lo que agrega cada enganche y lo que ocupa cada archivo leído; como Claude Code no los cuenta en tokens, se estiman por caracteres y quedan marcados como estimación | Acuerdo 7; propuesta del agente para la estimación |
| RN-03 | Cada archivo `.jsonl` se lee desde donde se quedó la vez anterior | Acuerdo 9 |
| RN-04 | Leer el formato de Claude Code va aparte de guardar: otra herramienta agrega su lector | «Dónde más puede pasar», otra herramienta de IA |
| RN-05 | Leer dos veces lo mismo no duplica nada | `03·D6` |
| RN-06 | La suma del consumo sigue siendo la de `presupuesto.py`; no se escribe otra | Punto 6, `07·Q4` |
| RN-07 | La lectura la hace una orden de Cimiento, que la instalación programa una vez al día | Punto 6 |

### 3.2 Supuestos

- El formato del `.jsonl` es el verificado el 2026-10-05: las llamadas son líneas `assistant` con `message.usage`; los enganches, líneas `attachment` de tipo `hook_*`; los archivos leídos, un `tool_use` de `Read` y su `tool_result`.

### 3.3 Fuera de alcance

- Los agentes auxiliares (`subagents/`) y los demás niveles: HU-010.
- La llegada en vivo por telemetría: HU-007.

---

## 4. Criterios de aceptación

### CA-01 · Las llamadas de un proyecto quedan guardadas

**Sale de:** análisis 1 del pendiente 119, punto 5.

```gherkin
Dado un proyecto registrado con registros de Claude Code en su carpeta
Cuando se corre la orden de leer el consumo
Entonces cada llamada queda en la base con su proyecto, sesión, fecha, modelo y tokens
Y lo que agregó cada enganche y lo que ocupó cada archivo leído quedan con su estimación
```

**Cómo validarlo:**
1. En `proyectos/cimiento/`, correr `.venv\Scripts\python manage.py leer_consumo` → dice cuántas llamadas, enganches y archivos leyó por proyecto, con los totales de `presupuesto.py`.
2. Correr `python manage.py test core.consumo` → pasan los casos de lectura y guardado con un `.jsonl` de muestra.

**Aprobado cuando:** los números de la muestra coinciden con lo que la prueba espera.

### CA-02 · Leer otra vez no duplica

**Sale de:** análisis 1 del pendiente 119, punto 5.

```gherkin
Dado un .jsonl ya leído
Cuando se corre la orden otra vez, con o sin líneas nuevas
Entonces solo se guardan las líneas nuevas
Y una llamada partida en varias líneas cuenta una vez
```

**Cómo validarlo:**
1. Correr `python manage.py test core.consumo` → pasan los casos de lectura repetida y de llamada partida.

**Aprobado cuando:** las cantidades no cambian al repetir y crecen solo con lo nuevo.

### CA-03 · Una línea rota no tumba la lectura

**Sale de:** análisis 1 del pendiente 119, punto 5.

```gherkin
Dado un .jsonl con una línea ilegible o a medio escribir al final
Cuando se lee
Entonces se salta la ilegible, se guarda lo demás
Y la línea a medio escribir se vuelve a leer la vez siguiente
```

**Cómo validarlo:**
1. Correr `python manage.py test core.consumo` → pasan los casos de línea rota.

**Aprobado cuando:** lo legible queda guardado y la línea final incompleta se lee después.

### CA-04 · La suma es la de siempre y la lectura queda programada

**Sale de:** análisis 1 del pendiente 119, punto 6.

```gherkin
Dado la suma del consumo de la sesión que hace hook_presupuesto.py
Cuando usa el lector nuevo
Entonces suma con presupuesto.py, contando una vez cada llamada aunque ocupe varias líneas
Y la instalación del estándar programa la lectura una vez al día
```

**Cómo validarlo:**
1. Correr `python manage.py test core.consumo` → pasa el caso de la llamada partida en la suma de la sesión.
2. Correr `python validadores/instalar.py "«carpeta del estándar»"` → aparece el paso de programar la lectura.

**Aprobado cuando:** la llamada partida cuenta una vez y el paso aparece.

> Medido el 2026-10-05 en la sesión `c3d82767`: 619 líneas con `usage` son 208 llamadas. Contar por línea, como hacía `hook_presupuesto.py`, daba 3,79 millones de tokens donde hay 1,15 millones.

### Criterios de aceptación transversales

- [ ] Errores: un fallo previsto da mensaje accionable **sin exponer detalles internos**; el sistema queda consistente, sin datos a medias (`05`, [`00·N3`](../../../../base/00-nucleo-blindado.md#n3--no-romper-cosas-para-pasar-un-obstáculo-blindada)).
- [ ] Idempotencia: reintentar o doble-enviar **no duplica** efectos ([`03·D6`](../../../../base/03-datos.md#d6--concurrencia-e-idempotencia)).
- [ ] Privacidad: datos personales/sensibles no se exponen ni se registran en claro; se tratan según `marco-normativo` (`12`, [`00·N4`](../../../../base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)).
- [ ] No regresión: lo existente sigue funcionando; la suite relacionada queda verde (`08`, [`02·F5`](../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)).

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Privacidad** | No se guarda el texto de los mensajes, de los enganches ni de los archivos: solo tamaños, nombres y rutas (capítulo `12`) |
| RNF-02 | **Rendimiento** | La segunda lectura de un archivo sin cambios no lo vuelve a recorrer |

---

## 6. Diseño y referencias

Documento funcional: [análisis 1 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-1.md), acuerdos 7, 8 y 9; puntos 5 y 6.

Modelo de datos afectado: tablas nuevas de llamadas, enganches, archivos leídos y avance de lectura.

---

## 7. Tareas técnicas derivadas

- [ ] Lector del formato de Claude Code, sin Django.
- [ ] Modelos y guardado sin duplicar.
- [ ] Orden `leer_consumo`.
- [ ] `hook_presupuesto.py` usa el lector nuevo.
- [ ] La instalación programa la lectura.
- [ ] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-006-lectura-de-los-jsonl` | CA-01 a CA-04 | (vacío) | [plan_trabajo.md](A-EP-025-HU-006-lectura-de-los-jsonl/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-006-lectura-de-los-jsonl/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-006-lectura-de-los-jsonl/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-003 | Alto |
| Riesgo | Claude Code cambie el formato | El lector va aparte y una línea que no entiende se salta |
| Riesgo | La estimación por caracteres se aleje de los tokens reales | Queda marcada como estimación, con el factor en una sola constante |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-05 | Claude | Creación de la HU desde el análisis 1 del pendiente 119 |
