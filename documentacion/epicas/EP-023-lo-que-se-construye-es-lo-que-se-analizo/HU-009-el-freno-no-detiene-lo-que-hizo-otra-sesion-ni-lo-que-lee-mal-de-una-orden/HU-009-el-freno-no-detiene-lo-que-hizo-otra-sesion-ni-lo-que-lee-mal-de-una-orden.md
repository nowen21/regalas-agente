# HU-009 · El freno no detiene lo que hizo otra sesión ni lo que lee mal de una orden

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-009 |
| **Épica / Feature** | [EP-023 — Lo que se construye es lo que se analizó](../epica.md) |
| **Módulo / Componente** | Cimiento, `core/enganches/freno.py` y `adaptadores/claude-code/hook_despues.py` |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** dueño del estándar
- **Quiero** que el freno detenga solo lo que de verdad hizo la sesión y no estaba aprobado
- **Para** que el trabajo permitido no se frene sin motivo

---

## 3. Contexto y descripción

Sale del [análisis 4 del pendiente 133](../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-4.md), acuerdos 1 y 2. El 2026-10-09 el freno detuvo dos veces trabajo permitido: una orden que solo leía, porque otra sesión cambió `.gitignore` al mismo tiempo; y un `sed` que escribía una fila de tabla, porque partió la orden por las barras verticales que iban dentro de las comillas.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Un archivo que cambió durante una orden no se le carga a la sesión si otra sesión del proyecto, activa en los últimos 10 minutos, lo nombra en lo que hizo |
| RN-02 | La orden de consola se parte solo por los separadores que están fuera de comillas |

### 3.2 Supuestos

- Claude Code guarda la transcripción de cada sesión del proyecto en la misma carpeta, y le pasa al enganche la ruta de la propia.

### 3.3 Fuera de alcance

- Resolver variables de la consola, como `$R`.

---

## 4. Criterios de aceptación

### CA-01 · Lo que hizo otra sesión no detiene a esta

**Sale de:** análisis 4 del pendiente 133, punto 2 de «Lo que se tiene que hacer»

```gherkin
Dado que otra sesión del proyecto, activa hace menos de 10 minutos, escribió un archivo
Cuando ese archivo aparece cambiado después de una orden de esta sesión
Entonces el freno no lo cuenta como fuera del plan
Y si ninguna otra sesión lo nombra, lo sigue contando
```

**Cómo validarlo:**
1. En `proyectos/cimiento/`, correr `manage.py test core.enganches.tests_freno_otras_sesiones`.
- Aprobado cuando las pruebas pasan.

### CA-02 · La orden se parte solo fuera de las comillas

**Sale de:** análisis 4 del pendiente 133, punto 3 de «Lo que se tiene que hacer»

```gherkin
Dado un sed -i que escribe una fila de tabla con barras verticales entre comillas
Cuando el freno busca los archivos que escribe
Entonces encuentra solo el archivo del final
Y una orden con tubería o punto y coma fuera de comillas se sigue partiendo
```

**Cómo validarlo:**
1. Correr `manage.py test core.enganches.tests_freno_otras_sesiones`.
- Aprobado cuando las pruebas pasan.

### Criterios de aceptación transversales

- [ ] No regresión: las pruebas del freno siguen en verde.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | De cada otra sesión se lee solo el final de su transcripción |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Mockup o prototipo | No aplica |
| Documento funcional | [Análisis 4 del pendiente 133](../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-4.md), acuerdos 1 y 2 |
| Contrato de API | No aplica |
| Modelo de datos afectado | Ninguno |

---

## 7. Tareas técnicas derivadas

- [ ] Que el freno descarte lo que hizo otra sesión.
- [ ] Que parta la orden respetando las comillas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| [`A-EP-023-HU-009-otras-sesiones-y-comillas`](A-EP-023-HU-009-otras-sesiones-y-comillas/) | CA-01, CA-02 | | [plan_trabajo](A-EP-023-HU-009-otras-sesiones-y-comillas/plan_trabajo.md) | [plan_pruebas](A-EP-023-HU-009-otras-sesiones-y-comillas/plan_pruebas.md) | [resultado](A-EP-023-HU-009-otras-sesiones-y-comillas/resultado_pruebas.md) | Cerrada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Otra sesión solo nombró el archivo, sin escribirlo | Ese cambio no se detiene; el plazo de 10 minutos lo limita |

---

## 10. Precondiciones  (Definition of Ready - DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas

## 11. Poscondiciones (Definition of Done - DoD)

- [ ] Pruebas de la fase pasando
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | |
| **N**egociable | Sí | |
| **V**aliosa | Sí | El freno deja de detener trabajo permitido |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-09 | El agente | Creación de la HU, desde el análisis 4 del pendiente 133 |
