# HU-017 · El freno no deja escribir un guion para lo que Cimiento ya hace


---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-017 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens en vivo](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/enganches/` |
| **Tipo** | Funcional |
| **Prioridad** | Should |
| **Estimación** | S |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien trabaja con el agente
- **Quiero** que no escriba un guion para lo que Cimiento ya hace, y que avise cuando un guion se parece a uno anterior
- **Para** que lo que se repite se vuelva funcionalidad y no otro guion

---

## 3. Contexto y descripción

El 2026-10-05 el agente escribió cinco guiones casi iguales para cerrar fases y otro para separar los cambios por sesión ([análisis 2 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md), acuerdo 6, punto 13). Desde la HU-016 eso lo hace Cimiento.

### 3.1 Reglas de negocio

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | Si el agente escribe un guion en `historico-chat/scripts/` para algo que Cimiento ya hace (cerrar o reabrir una fase, separar los cambios por sesión, crear o quitar con el andamio, cerrar o reabrir un pendiente, instalar o desinstalar, leer el gasto), el freno lo detiene y dice qué orden usar | Punto 13 |
| RN-02 | Si el guion se parece a uno anterior de esa carpeta, por su nombre o por su texto, el freno avisa que la tarea se repite y va como funcionalidad de Cimiento; no lo detiene | Punto 13 |
| RN-03 | Lo que de verdad se hace una vez sigue yendo a `historico-chat/scripts/` (`04·S18`) | Punto 13 |

### 3.2 Supuestos

- El guion se escribe con la herramienta de escritura, que trae su texto.

### 3.3 Fuera de alcance

- Un guion creado por la consola: el freno no ve su texto.

---

## 4. Criterios de aceptación

### CA-01 · Lo que Cimiento ya hace se detiene

**Sale de:** análisis 2 del pendiente 119, punto 13.

```gherkin
Dado un guion nuevo en historico-chat/scripts/ que escribe el resultado y el estado de una fase
Cuando el agente lo va a escribir
Entonces el freno lo detiene y dice que se usa manage.py cerrar_fase
```

**Cómo validarlo:**
1. Correr `python -m unittest core.enganches.tests_guiones` desde `proyectos/cimiento/` → pasan los casos de detener.

**Aprobado cuando:** el aviso nombra la orden de Cimiento.

### CA-02 · Lo parecido se avisa

**Sale de:** análisis 2 del pendiente 119, punto 13.

```gherkin
Dado un guion anterior medir_algo_1.py
Cuando el agente escribe medir_algo_2.py, o uno con casi el mismo texto
Entonces el freno avisa que la tarea se repite, nombra el anterior, y deja escribir
Y un guion distinto pasa sin aviso
```

**Cómo validarlo:**
1. Correr `python -m unittest core.enganches.tests_guiones` → pasan los casos de avisar.

**Aprobado cuando:** el aviso nombra el guion anterior.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | Solo se compara cuando se escribe un guion en esa carpeta |

---

## 6. Diseño y referencias

Documento funcional: [análisis 2 del pendiente 119](../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md), acuerdo 6.

---

## 7. Tareas técnicas derivadas

- [x] El catálogo de lo que Cimiento hace y la comparación con los guiones anteriores.
- [x] El freno los aplica.
- [x] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-017-guiones-repetidos` | CA-01 a CA-02 | (vacío) | [plan_trabajo.md](A-EP-025-HU-017-guiones-repetidos/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-017-guiones-repetidos/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-017-guiones-repetidos/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-016 | Alto |
| Riesgo | Detener un guion que no repite nada | Las señales son específicas; lo parecido solo avisa |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-05 | Claude | Creación de la HU desde el análisis 2 del pendiente 119 |
