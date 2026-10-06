# HU-012 · La telemetría se retira


---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-012 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens en vivo](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/consumo/`, `proyectos/cimiento/core/herramientas/instalar.py` |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien mantiene Cimiento
- **Quiero** quitar la telemetría
- **Para** que el gasto llegue por un solo camino, el `.jsonl` que lee el vigilante

---

## 3. Contexto y descripción

Con el vigilante de la HU-011 la telemetría no aporta: no trae enganches y solo la mandan las sesiones abiertas después de activarla ([análisis 2 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md), acuerdo 2, punto 4). Deja sin efecto la [HU-007](../HU-007-el-gasto-llega-a-cimiento-en-vivo/HU-007-el-gasto-llega-a-cimiento-en-vivo.md).

### 3.1 Reglas de negocio

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | Se retiran la ruta `/v1/logs`, su vista, el lector de la telemetría y su guardado | Punto 4 |
| RN-02 | La instalación deja de activar la telemetría y quita de `~/.claude/settings.json` las seis variables que puso, solo si tienen el valor que puso; las demás del usuario se quedan | Punto 4 |
| RN-03 | Lo que la telemetría ya guardó en la base se queda: es gasto real | Propuesta del agente |

### 3.2 Supuestos

- El vigilante de la HU-011 ya corre.

### 3.3 Fuera de alcance

- Quitar de la tabla de llamadas el campo `solicitud`: lo sigue llenando el `.jsonl`.

---

## 4. Criterios de aceptación

### CA-01 · No queda la telemetría en Cimiento

**Sale de:** análisis 2 del pendiente 119, punto 4.

```gherkin
Dado Cimiento corriendo
Cuando algo manda un envío a /v1/logs
Entonces la ruta no existe
Y no queda código de la telemetría
```

**Cómo validarlo:**
1. Correr `python manage.py test core.consumo` desde `proyectos/cimiento/` → pasa el caso de la ruta.

**Aprobado cuando:** `/v1/logs` responde que no existe.

### CA-02 · La instalación la quita y no la vuelve a poner

**Sale de:** análisis 2 del pendiente 119, punto 4.

```gherkin
Dado un ~/.claude/settings.json con las seis variables y otras del usuario
Cuando corre la instalación del estándar
Entonces las seis variables ya no están
Y las del usuario siguen
Y una variable con otro valor no se toca
```

**Cómo validarlo:**
1. Correr `python -m unittest core.herramientas.tests_instalacion` → pasan los casos de retirar.

**Aprobado cuando:** solo salen las seis con el valor que puso la instalación.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Integridad** | Lo guardado no se pierde |

---

## 6. Diseño y referencias

Documento funcional: [análisis 2 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md), acuerdo 2.

---

## 7. Tareas técnicas derivadas

- [x] Quitar la ruta, la vista, el lector y el guardado.
- [x] La instalación retira las variables.
- [x] Pruebas, y la nota en la HU-007.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-012-retirar-la-telemetria` | CA-01 a CA-02 | (vacío) | [plan_trabajo.md](A-EP-025-HU-012-retirar-la-telemetria/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-012-retirar-la-telemetria/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-012-retirar-la-telemetria/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-011 | Alto |
| Riesgo | Quitar una variable que el usuario puso | Solo sale la que tiene el valor exacto de la instalación |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-05 | Claude | Creación de la HU desde el análisis 2 del pendiente 119 |
