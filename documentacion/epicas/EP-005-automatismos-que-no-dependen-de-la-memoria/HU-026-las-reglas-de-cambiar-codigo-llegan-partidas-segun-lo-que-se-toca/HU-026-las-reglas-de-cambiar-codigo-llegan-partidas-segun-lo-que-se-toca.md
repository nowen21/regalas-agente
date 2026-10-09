# HU-026 · Las reglas de cambiar código llegan partidas según lo que se toca

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-026 |
| **Épica / Feature** | [EP-005 — Automatismos que no dependen de la memoria](../epica.md) |
| **Módulo / Componente** | Cimiento, `core/herramientas/` y `base/tareas.md` |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** dueño del estándar
- **Quiero** que el agente sepa que si está haciendo una cosa le aplican unas reglas, y si está haciendo otra, otras
- **Para** que cada acción sobre código traiga solo las reglas de su tema, y no las 128 de una vez

---

## 3. Contexto y descripción

Sale del [análisis 1 del pendiente 133](../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-1.md), acuerdo 3, y del [análisis 2](../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-2.md), acuerdo 1, que lo reemplaza: las reglas de código se reparten por temas, no en tres grupos. Las reglas de `cambiar-codigo` son 128, 67 KB, en 21 capítulos. Con la [HU-025](../HU-025-las-reglas-de-cada-tarea-llegan-antes-de-la-accion/HU-025-las-reglas-de-cada-tarea-llegan-antes-de-la-accion.md) llegan antes de la acción, por partes, pero todas: escribir una prueba trae también las de despliegue.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Cada capítulo del estándar es un tema |
| RN-02 | Una tabla de `base/tareas.md` dice qué temas recibe cada tipo de archivo, por su ruta |
| RN-03 | Todo archivo de código recibe además los temas que la tabla marca para todos |
| RN-04 | El archivo que no encaja en ningún tipo recibe todos los temas de código |
| RN-05 | Cada regla sigue llegando una sola vez en la sesión |

### 3.2 Supuestos

- La HU-025 ya entrega las reglas por acción.

### 3.3 Fuera de alcance

- Cambiar la línea `**Aplica a:**` de cada regla.
- Partir otras tareas.

---

## 4. Criterios de aceptación

### CA-01 · Cada archivo recibe solo los temas que toca

**Sale de:** análisis 2 del pendiente 133, punto 4 de «Lo que se tiene que hacer»

```gherkin
Dado que el agente va a escribir un archivo de pruebas
Cuando el enganche de antes de la acción elige las reglas de cambiar código
Entonces le llegan las del tema de pruebas y las de los temas para todos
Y no las de despliegue ni las de interfaz
```

**Cómo validarlo:**
1. En `proyectos/cimiento/`, correr `manage.py test core.herramientas.tests_entrega_de_reglas`.
- Aprobado cuando las pruebas pasan.

### CA-02 · El archivo que no encaja recibe todos los temas

**Sale de:** análisis 2 del pendiente 133, punto 4 de «Lo que se tiene que hacer»

```gherkin
Dado un archivo de código que no encaja en ningún tipo de la tabla
Cuando el enganche elige las reglas
Entonces le llegan todas las de cambiar código
```

**Cómo validarlo:**
1. Correr `manage.py test core.herramientas.tests_entrega_de_reglas`.
- Aprobado cuando las pruebas pasan.

### CA-03 · La tabla de temas está en el estándar

**Sale de:** análisis 2 del pendiente 133, punto 3 de «Lo que se tiene que hacer»

```gherkin
Dado base/tareas.md
Cuando se lee
Entonces trae la tabla de temas: cada tipo de archivo con sus patrones y sus capítulos
Y el cambio queda con su versión y su registro
```

**Cómo validarlo:**
1. Leer `base/tareas.md` con `manage.py documento ver estandar base/tareas.md`.
- Aprobado cuando trae la tabla y la versión subió.

### Criterios de aceptación transversales

- [ ] No regresión: sin la tabla en el estándar, la entrega sigue como en la HU-025.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Tamaño** | Al escribir una prueba, lo de cambiar código no pasa de 25 KB |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Mockup o prototipo | No aplica |
| Documento funcional | [Análisis 2 del pendiente 133](../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-2.md), acuerdo 1 |
| Contrato de API | No aplica |
| Modelo de datos afectado | Ninguno |

---

## 7. Tareas técnicas derivadas

- [ ] Escribir la tabla de temas en `base/tareas.md`.
- [ ] Elegir los temas por la ruta del archivo y entregar solo esos.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| [`A-EP-005-HU-026-temas-por-archivo`](A-EP-005-HU-026-temas-por-archivo/) | CA-01 a CA-03 | HU-025 | [plan_trabajo](A-EP-005-HU-026-temas-por-archivo/plan_trabajo.md) | [plan_pruebas](A-EP-005-HU-026-temas-por-archivo/plan_pruebas.md) | [resultado](A-EP-005-HU-026-temas-por-archivo/resultado_pruebas.md) | Cerrada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | [HU-025](../HU-025-las-reglas-de-cada-tarea-llegan-antes-de-la-accion/HU-025-las-reglas-de-cada-tarea-llegan-antes-de-la-accion.md) | Sin ella, nadie entrega estas reglas |

---

## 10. Precondiciones  (Definition of Ready - DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas

## 11. Poscondiciones (Definition of Done - DoD)

- [ ] Pruebas de las fases pasando
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | No | Depende de la HU-025 |
| **N**egociable | Sí | |
| **V**aliosa | Sí | La primera acción sobre código deja de cargar 80 KB |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-09 | El agente | Creación de la HU, desde el análisis 1 del pendiente 133 |
| 2026-10-09 | El agente | Versión 2: por temas en vez de tres grupos, según el análisis 2 del pendiente 133 |
