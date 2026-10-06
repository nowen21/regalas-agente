# HU-026 · La pantalla «Gasto» dice primero lo importante

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-026 |
| **Épica / Feature** | [EP-025 — Cimiento se administra y muestra el gasto de tokens](../epica.md) |
| **Módulo / Componente** | Cimiento, `core/consumo/` (pantalla «Gasto») |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien revisa el gasto de tokens
- **Quiero** ver primero cuánto se gasta y si sube o baja, y el resto ordenado por propósito
- **Para** decidir rápido qué pasar a un programa sin recorrer 13 tablas

---

## 3. Contexto y descripción

La pantalla no ordena lo que muestra: 20 bloques con el mismo peso, sin el total del período ni su comparación, con datos repetidos y con lo del ahorro de último. Sale del [análisis 1 del pendiente 124](../../../../historico-chat/resumenes/2026-10-05/pendientes/124-la-pantalla-gasto-no-dice-por-donde-empezar/analisis-1.md), acuerdos 1, 2 y 3.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Arriba, siempre visibles: filtros, hora de la última actualización con su botón, y la franja con el total y su variación, las llamadas, el % de caché releída y el contexto máximo |
| RN-02 | Debajo, cinco pestañas: Resumen, Dónde se gasta, Contexto, Ahorro y Actividad |
| RN-03 | La variación compara con el tramo anterior cortado a la misma hora |
| RN-04 | En Contexto no se marca ninguna fila: se muestran el promedio y el máximo por vez junto al límite actual |
| RN-05 | Salen la gráfica «Por proyecto» y la tabla por tipo de token; «estimado» se dice una sola vez por pestaña |
| RN-06 | Ningún intervalo de tiempo pide datos: hasta la HU-027, se actualiza con el botón |

### 3.2 Supuestos

- Los datos salen de la base que llena el vigilante (HU-025).

### 3.3 Fuera de alcance

- Que la pantalla se entere sola de lo nuevo: HU-027.

---

## 4. Criterios de aceptación

### CA-01 · La franja dice el total y si sube o baja

**Sale de:** análisis 1 del pendiente 124, puntos 2 y 3 de «Lo que se tiene que hacer»

```gherkin
Dado gasto en el período y en el tramo anterior
Cuando se abre «Gasto»
Entonces la franja muestra el total, su variación contra el tramo anterior cortado a la misma hora, las llamadas, el % de caché releída y el contexto máximo
```

**Cómo validarlo:**
1. En `proyectos/cimiento/`, correr `.venv/Scripts/python manage.py test core.consumo.tests_tablero`.
- Aprobado cuando las pruebas de la franja pasan.

### CA-02 · Cinco pestañas, cada una con lo suyo

**Sale de:** análisis 1 del pendiente 124, punto 2 de «Lo que se tiene que hacer»

```gherkin
Dado la pantalla «Gasto» abierta
Cuando se elige una pestaña
Entonces se carga solo esa pestaña con su contenido
Y «Dónde se gasta» agrupa por proyecto, palabra, trabajo, modelo o agente, con porcentaje y barra
Y no está la gráfica «Por proyecto» ni la tabla por tipo de token
```

**Cómo validarlo:**
1. Correr `manage.py test core.consumo.tests_tablero`.
2. Abrir `http://127.0.0.1:8015/gasto/` con una cuenta y recorrer las cinco pestañas.
- Aprobado cuando las pruebas pasan y cada pestaña muestra lo que dice RN-02.

### CA-03 · Contexto muestra promedio, máximo y límite

**Sale de:** análisis 1 del pendiente 124, punto 4 de «Lo que se tiene que hacer»

```gherkin
Dado enganches y archivos con gasto
Cuando se abre la pestaña Contexto
Entonces cada uno muestra veces, promedio y máximo por vez, y el límite actual
Y ninguna fila queda marcada
```

**Cómo validarlo:**
1. Correr `manage.py test core.consumo.tests_tablero`.
- Aprobado cuando la prueba de Contexto pasa.

### CA-04 · La ayuda describe la pantalla nueva

**Sale de:** análisis 1 del pendiente 124, punto 5 de «Lo que se tiene que hacer»

```gherkin
Dado la ayuda de «Gasto»
Cuando se lee
Entonces describe la franja, las pestañas y el botón de actualizar
Y no dice «cada 10 segundos»
```

**Cómo validarlo:**
1. Abrir `core/ayuda/templates/ayuda/secciones/gasto.html` y buscar «10 segundos» → no aparece.
- Aprobado cuando la ayuda nombra las cinco pestañas.

### Criterios de aceptación transversales

- [x] Autorización: sin cuenta, la pantalla y sus partes mandan a entrar.
- [x] No regresión: las pruebas de `core.consumo` siguen en verde.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | Cada pestaña corre solo sus consultas, no las de las otras |
| RNF-02 | **Compatibilidad** | Usa solo lo que ya carga la pantalla: Tabler, htmx y ApexCharts |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Mockup o prototipo | El dibujo del turno 7 del [análisis 1 del pendiente 124](../../../../historico-chat/resumenes/2026-10-05/pendientes/124-la-pantalla-gasto-no-dice-por-donde-empezar/analisis-1.md) |
| Documento funcional | El mismo análisis, acuerdos 1 a 3 |
| Contrato de API | Rutas `gasto/`, `gasto/franja/` y `gasto/pestana/<nombre>/` |
| Modelo de datos afectado | Ninguno |

---

## 7. Tareas técnicas derivadas

- [ ] Sumas nuevas en `tablero.py`: tramo anterior, por día y tipo, agrupar por, contexto por vez, ahorro en tres grupos.
- [ ] Vistas y rutas de la franja y de cada pestaña.
- [ ] Plantillas de la franja y las cinco pestañas.
- [ ] Ayuda y pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| [`A-EP-025-HU-026-franja-y-pestanas`](A-EP-025-HU-026-franja-y-pestanas/) | CA-01 a CA-04 | | [plan_trabajo](A-EP-025-HU-026-franja-y-pestanas/plan_trabajo.md) | [plan_pruebas](A-EP-025-HU-026-franja-y-pestanas/plan_pruebas.md) | | En curso |
| `B-EP-025-HU-026-la-ayuda-de-gasto` |  | (vacío) | [plan_trabajo.md](B-EP-025-HU-026-la-ayuda-de-gasto/plan_trabajo.md) | [plan_pruebas.md](B-EP-025-HU-026-la-ayuda-de-gasto/plan_pruebas.md) | [resultado_pruebas.md](B-EP-025-HU-026-la-ayuda-de-gasto/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-025: los datos de la base | Medio, ya cumplida |
| Riesgo | Sin el refresco de 10 segundos, la pantalla queda quieta hasta la HU-027 | El botón ↻ actualiza; la HU-027 sigue en este mismo trabajo |

---

## 10. Precondiciones  (Definition of Ready - DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Diseño acordado en el análisis
- [x] Cumple criterios INVEST

## 11. Poscondiciones (Definition of Done - DoD)

- [ ] Pruebas de la fase pasando
- [ ] Todos los criterios de aceptación verificados
- [ ] Ayuda actualizada

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | |
| **N**egociable | Sí | |
| **V**aliosa | Sí | Se ve qué automatizar sin recorrer tablas |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | Una pantalla |
| **T**esteable | Sí | |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | El agente | Creación de la HU, desde el análisis 1 del pendiente 124 |
