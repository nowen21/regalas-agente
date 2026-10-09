# HU-030 · El Resumen del gasto responde en la mitad del tiempo y no se recalcula con cada aviso

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-030 |
| **Épica / Feature** | [EP-025 · Cimiento se administra y muestra el gasto de tokens](../epica.md) |
| **Módulo / Componente** | El gasto: `core/consumo/` |
| **Tipo** | Rendimiento |
| **Prioridad** | Should |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien mira el gasto mientras el agente trabaja
- **Quiero** que el Resumen responda rápido y que la pantalla no se recalcule con cada mensaje
- **Para** usar la pantalla justo cuando más se necesita, sin que la base haga el mismo cálculo muchas veces por minuto

---

## 3. Contexto y descripción

El Resumen tarda entre 1,1 y 1,3 s, y más de la mitad es la gráfica por día, que trae cada llamada a Python y la suma una por una. Además, cada aviso del vigilante vuelve a pedir la pestaña abierta y la franja, y mientras el agente trabaja eso pasa con cada mensaje. Sale del [análisis 1 del pendiente 146](../../../../historico-chat/resumenes/2026-10-08/pendientes/146-el-resumen-del-gasto-tarda-y-se-pide-con-cada-mensaje/analisis-1.md), acuerdos 1 a 3, puntos 1 y 2 de «Lo que se tiene que hacer».

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Las gráficas por día se suman en la base agrupadas por hora en UTC; Python pasa cada hora a su día local (acuerdo 1) |
| RN-02 | Dan los mismos números que hoy, también para las llamadas cerca de la medianoche local (acuerdo 1) |
| RN-03 | Los avisos del vigilante refrescan la pantalla como máximo una vez cada 30 segundos (acuerdo 2) |
| RN-04 | Con la pantalla escondida en el navegador no se refresca; al volver a verla se refresca una vez si llegó algún aviso (acuerdo 2) |
| RN-05 | El botón «Actualizar» refresca en el momento (acuerdo 2) |

### 3.2 Supuestos

- La zona horaria de Cimiento tiene diferencia de horas enteras con UTC, como Colombia.

### 3.3 Fuera de alcance

- Cargar las zonas horarias en MySQL.
- Guardar el Resumen ya calculado.

---

## 4. Criterios de aceptación

### CA-01 · La gráfica por día suma en la base y da lo mismo

**Sale de:** análisis 1 del pendiente 146, punto 1 de «Lo que se tiene que hacer»

```gherkin
Dadas llamadas de hoy, de ayer a las 23:30 hora local y de hoy a las 00:30 hora local
Cuando se arman las gráficas por día
Entonces cada llamada cae en su día local
Y la base devuelve una fila por hora, no una por llamada
```

**Cómo validarlo:** correr `manage.py test core.consumo.tests_rapido` → resultado esperado: los casos pasan; y medir el Resumen sobre la base real.

### CA-02 · La pantalla junta los avisos

**Sale de:** punto 2

```gherkin
Dada la pantalla del gasto abierta
Cuando llegan varios avisos seguidos
Entonces se refresca como máximo una vez cada 30 segundos
Y escondida no se refresca, y al volver se refresca una vez si llegó algo
Y el botón «Actualizar» refresca en el momento
```

**Cómo validarlo:** correr `manage.py test core.consumo.tests_rapido` → resultado esperado: los casos pasan.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | El Resumen, sobre la base real, tarda menos de la mitad de lo medido el 2026-10-09 (1,1 a 1,3 s) |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 146](../../../../historico-chat/resumenes/2026-10-08/pendientes/146-el-resumen-del-gasto-tarda-y-se-pide-con-cada-mensaje/analisis-1.md) |
| Modelo de datos afectado | Ninguno |

---

## 7. Tareas técnicas derivadas

- [x] Las gráficas por día suman en la base.
- [x] La pantalla junta los avisos.
- [x] Pruebas y medición.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-025-HU-030-resumen-rapido` | CA-01 a CA-02 | (vacío) | [plan_trabajo.md](A-EP-025-HU-030-resumen-rapido/plan_trabajo.md) | [plan_pruebas.md](A-EP-025-HU-030-resumen-rapido/plan_pruebas.md) | [resultado_pruebas.md](A-EP-025-HU-030-resumen-rapido/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Una zona horaria con media hora correría una llamada al día vecino | Bajo: Cimiento corre en Colombia |

---

## 10. Precondiciones  (Definition of Ready - DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas y desbloqueadas
- [x] Cumple criterios INVEST

## 11. Poscondiciones (Definition of Done - DoD)

- [x] Todos los criterios de aceptación verificados
- [x] Documentación actualizada

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | |
| **N**egociable | Sí | |
| **V**aliosa | Sí | La pantalla responde mientras se trabaja |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Pruebas de Django y medición sobre la base real |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-09 | El agente | Creación de la HU, desde el análisis 1 del pendiente 146 |
