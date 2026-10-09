# HU-029 · El vigilante se reinicia solo cuando cambia su código

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-029 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens](../epica.md) |
| **Módulo / Componente** | El gasto: `core/consumo/` |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien usa Cimiento
- **Quiero** que el vigilante del consumo se reinicie solo cuando cambia el código de Cimiento
- **Para** que no siga días con código viejo ni haya que reiniciarlo a mano

---

## 3. Contexto y descripción

El 2026-10-08 se encontró que el vigilante corría desde el 2026-10-05 con el código de antes de la HU-025: no guardó las líneas de sesión durante dos días y nada lo avisó (H-37). Reiniciarlo era manual, porque el freno no deja que el agente lance un proceso que queda corriendo. El usuario preguntó por qué tenía que ser manual y aprobó la opción 1: que se reinicie solo cuando cambia su código.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | El vigilante se entera de que cambió un `.py` de Cimiento porque Windows le avisa, igual que con los `.jsonl`: sin revisar cada cierto tiempo (análisis 1 del pendiente 124, acuerdos 4 y 6) |
| RN-02 | No cuentan las pruebas, ni lo que está en `.venv`, `__pycache__`, `node_modules`, `.agente` o `.git` |
| RN-03 | Espera a que el código deje de cambiar unos segundos antes de reiniciar: un cambio de varios archivos produce un solo reinicio |
| RN-04 | Arranca el nuevo y solo se detiene cuando el nuevo ya escribió su número de proceso. Si el nuevo no arranca, el viejo sigue y lo deja anotado |
| RN-05 | Nunca quedan dos vigilantes trabajando al tiempo más que los segundos del relevo |

### 3.2 Supuestos

- `watchdog` ya está instalado: es el que avisa de los `.jsonl`.

### 3.3 Fuera de alcance

- Arrancar el vigilante cuando no está corriendo (lo hace el inicio de sesión de Windows).

---

## 4. Criterios de aceptación

### CA-01 · Un cambio de código reinicia el vigilante

**Sale de:** RN-01, RN-02, RN-03

```gherkin
Dado un vigilante corriendo
Cuando cambian uno o varios .py de Cimiento que no son pruebas
Entonces, cuando dejan de cambiar, arranca un vigilante nuevo una sola vez
Y un cambio en una prueba, en .venv o en __pycache__ no reinicia nada
```

**Cómo validarlo:** correr `manage.py test core.consumo.tests_reinicio` → resultado esperado: los casos pasan.

### CA-02 · El relevo no deja al consumo sin vigilante

**Sale de:** RN-04, RN-05

```gherkin
Dado un reinicio en marcha
Cuando el nuevo escribe su número de proceso
Entonces el viejo se detiene
Y si el nuevo no lo escribe a tiempo, el viejo sigue, vuelve a escribir el suyo y anota por qué
```

**Cómo validarlo:** correr `manage.py test core.consumo.tests_reinicio` y reiniciar el de verdad cambiando un archivo → resultado esperado: los casos pasan y el número de proceso cambia.

### Criterios de aceptación transversales

- [ ] No regresión: `core.consumo` queda verde.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Sin relojes** | Nada revisa cada cierto tiempo; las únicas esperas son la de calma después de un cambio y la del relevo |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| El vigilante | `core/consumo/vigilante.py` |
| El reinicio | `core/consumo/reinicio.py` |
| Modelo de datos afectado | Ninguno |

---

## 7. Tareas técnicas derivadas

- [ ] Vigilar el código de Cimiento y reiniciar con relevo.
- [ ] Pruebas y el reinicio de verdad.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-029-reinicio-solo` | CA-01, CA-02 | (vacío) | [plan_trabajo.md](A-EP-025-HU-029-reinicio-solo/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-029-reinicio-solo/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-029-reinicio-solo/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | El nuevo arranca con un archivo a medio escribir y falla | RN-03 espera la calma, y RN-04 deja corriendo el viejo |

---

## 10. Precondiciones  (Definition of Ready - DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas y desbloqueadas
- [x] Cumple criterios INVEST

## 11. Poscondiciones (Definition of Done - DoD)

- [ ] Todos los criterios de aceptación verificados
- [ ] Documentación actualizada

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | |
| **N**egociable | Sí | |
| **V**aliosa | Sí | Evita perder lo que Claude Code borra a los 30 días |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | Una fase |
| **T**esteable | Sí | Pruebas de Django y el reinicio de verdad |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-08 | El agente | Creación de la HU, desde la aprobación del usuario del 2026-10-08 |
