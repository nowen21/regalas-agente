# HU-025 · Cada línea del `.jsonl` queda en la base en el momento, con las claves tapadas

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-025 |
| **Épica / Feature** | [EP-025 — Cimiento se administra y muestra el gasto de tokens](../epica.md) |
| **Módulo / Componente** | Cimiento, `core/consumo/` |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | En prueba |

---

## 2. Narrativa

- **Como** dueño de Cimiento
- **Quiero** que cada línea que Claude Code escribe en un `.jsonl` quede en la base en el momento, sin claves
- **Para** no perder el gasto ni lo que pasó cuando Claude Code borre el archivo a los 30 días

---

## 3. Contexto y descripción

El gasto se lee de afuera, se pierde a los 30 días y el vigilante guarda con relojes. Sale del [análisis 1 del pendiente 124](../../../../historico-chat/resumenes/2026-10-05/pendientes/124-la-pantalla-gasto-no-dice-por-donde-empezar/analisis-1.md), acuerdos 4, 5 y 6. Hoy la base guarda solo conteos; el [vigilante](../../../../proyectos/cimiento/core/consumo/vigilante.py) espera 2 segundos después de cada aviso de Windows y relee la lista de proyectos cada 60.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Cada línea completa de un `.jsonl` de un proyecto activo se guarda en la base con las claves tapadas, una sola vez |
| RN-02 | Los conteos salen de las mismas líneas, en la misma transacción |
| RN-03 | El vigilante guarda con cada aviso de Windows, sin esperar |
| RN-04 | Un `.jsonl` de una carpeta desconocida hace releer la lista de proyectos en ese momento |
| RN-05 | Ningún intervalo de tiempo decide cuándo se guarda |

### 3.2 Supuestos

- Claude Code escribe líneas completas terminadas en salto; la última sin salto se lee en el aviso siguiente.

### 3.3 Fuera de alcance

- Avisarle a la pantalla: EP-025·HU-027.
- Mostrar las líneas en una pantalla.

---

## 4. Criterios de aceptación

### CA-01 · La línea queda en la base, sin claves y una sola vez

**Sale de:** análisis 1 del pendiente 124, punto 6 de «Lo que se tiene que hacer»

```gherkin
Dado un proyecto activo con un .jsonl que trae una línea con una clave
Cuando el vigilante guarda el archivo
Entonces cada línea completa queda en la base con la clave tapada
Y guardarlo otra vez no la duplica
Y los conteos de llamadas quedan igual que antes
```

**Cómo validarlo:**
1. En `proyectos/cimiento/`, correr `python manage.py test core.consumo.tests_lineas`.
2. Leer el resultado de `LasLineasQuedanEnLaBase` → resultado esperado: sus pruebas en verde.
- Aprobado cuando las pruebas de líneas, de clave tapada y de no duplicar pasan.

### CA-02 · El vigilante guarda en el momento del aviso

**Sale de:** análisis 1 del pendiente 124, punto 7 de «Lo que se tiene que hacer»

```gherkin
Dado el vigilante corriendo
Cuando Windows avisa que un .jsonl cambió
Entonces lo nuevo queda en la base en ese mismo aviso
Y el código del vigilante no tiene ningún intervalo de espera
```

**Cómo validarlo:**
1. Correr `python manage.py test core.consumo.tests_vigilante`.
2. Buscar `sleep` y `CADA` en `core/consumo/vigilante.py` → resultado esperado: no aparecen.
- Aprobado cuando las pruebas pasan y la búsqueda no encuentra nada.

### CA-03 · Un proyecto nuevo entra con su primer aviso

**Sale de:** análisis 1 del pendiente 124, punto 8 de «Lo que se tiene que hacer»

```gherkin
Dado el vigilante corriendo y un proyecto que se registra después de arrancar
Cuando llega el aviso de un .jsonl de ese proyecto
Entonces el vigilante relee la lista y guarda el gasto
```

**Cómo validarlo:**
1. Correr `python manage.py test core.consumo.tests_vigilante`.
2. Leer el resultado de la prueba del proyecto nuevo → resultado esperado: en verde.
- Aprobado cuando la prueba pasa.

### CA-04 · El README dice cómo llega el gasto

**Sale de:** análisis 1 del pendiente 124, punto 9 de «Lo que se tiene que hacer»

```gherkin
Dado el README de Cimiento
Cuando se lee cómo llega el gasto
Entonces dice que lo guarda el vigilante en la base, sin telemetría
```

**Cómo validarlo:**
1. Abrir `proyectos/cimiento/README.md` y buscar `/v1/logs` → resultado esperado: no aparece.
- Aprobado cuando el párrafo nombra al vigilante y la base.

### Criterios de aceptación transversales

- [x] Privacidad: ninguna clave queda en la base (`00·N6`).
- [x] Idempotencia: leer dos veces lo mismo no duplica líneas ni conteos.
- [x] No regresión: las pruebas de `core.consumo` siguen en verde.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Seguridad** | Lo que entra a la base pasa por el `Enmascarador` de Cimiento |
| RNF-02 | **Rendimiento** | Releer desde cero los `.jsonl` que hay (438 MB medidos el 2026-10-06) termina sin agotar la memoria: se procesa archivo por archivo |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Mockup o prototipo | No aplica |
| Documento funcional | [Análisis 1 del pendiente 124](../../../../historico-chat/resumenes/2026-10-05/pendientes/124-la-pantalla-gasto-no-dice-por-donde-empezar/analisis-1.md) |
| Contrato de API | No aplica |
| Modelo de datos afectado | Tabla nueva `LineaDeSesion` en `core/consumo/models.py` |

---

## 7. Tareas técnicas derivadas

- [x] Modelo y migración de `LineaDeSesion`.
- [x] Guardar las líneas en `GuardadoDeConsumo.leer_archivo`.
- [x] Vigilante sin relojes y con relectura por carpeta desconocida.
- [x] `leer_consumo --desde-cero` para traer lo que ya está en los `.jsonl`.
- [x] README de Cimiento.
- [x] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| [`A-EP-025-HU-025-lineas-a-la-base-sin-relojes`](A-EP-025-HU-025-lineas-a-la-base-sin-relojes/) | CA-01 a CA-04 | | [plan_trabajo](A-EP-025-HU-025-lineas-a-la-base-sin-relojes/plan_trabajo.md) | [plan_pruebas](A-EP-025-HU-025-lineas-a-la-base-sin-relojes/plan_pruebas.md) | [resultado](A-EP-025-HU-025-lineas-a-la-base-sin-relojes/resultado_pruebas.md) · **Cumple** | Cumple, falta el commit |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | [EP-001·HU-040](../../EP-001-cuerpo-de-reglas-heredable/HU-040-c29-reconoce-la-base-de-cimiento/HU-040-c29-reconoce-la-base-de-cimiento.md): `01·C29` reconoce la base | Alto, ya cumplida |
| Riesgo | El tapado reemplaza un valor dentro de una línea JSON y la deja ilegible | Se guarda la línea como texto; los conteos salen de la línea original antes de tapar |
| Riesgo | Sin espera, Claude Code escribe varias líneas seguidas y llegan varios avisos | El lector solo toma líneas completas y recuerda hasta dónde leyó: cada aviso guarda lo que haya, sin duplicar |

---

## 10. Precondiciones  (Definition of Ready - DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas y desbloqueadas
- [x] Cumple criterios INVEST

## 11. Poscondiciones (Definition of Done - DoD)

- [x] Pruebas de la fase pasando
- [x] Todos los criterios de aceptación verificados
- [x] README y CHANGELOG actualizados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | Solo depende de la HU-040, ya cumplida |
| **N**egociable | Sí | |
| **V**aliosa | Sí | El gasto deja de perderse a los 30 días |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | Un modelo, el guardado y el vigilante |
| **T**esteable | Sí | Pruebas automáticas |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | El agente | Creación de la HU, desde el análisis 1 del pendiente 124 |
| 2026-10-06 | El agente | Fase `A` con veredicto Cumple, versión 55.2.0 |
