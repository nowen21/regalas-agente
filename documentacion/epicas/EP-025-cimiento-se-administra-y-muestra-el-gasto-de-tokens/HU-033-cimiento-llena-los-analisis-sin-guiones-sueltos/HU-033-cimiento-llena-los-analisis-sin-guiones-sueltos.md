# HU-033 · Cimiento llena los análisis sin guiones sueltos

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-033 |
| **Épica / Feature** | [EP-025 — Cimiento se administra y muestra el gasto de tokens](../epica.md) |
| **Módulo / Componente** | Cimiento, `core/enganches/analisis_en_curso.py` y un comando de `core/proyectos/` |
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
- **Quiero** que Cimiento llene los análisis: lo que siempre es igual, solo, y lo que redacta el agente, con un comando fijo
- **Para** que no se vuelva a escribir un guion suelto por cada análisis

---

## 3. Contexto y descripción

Sale del [análisis 3 del pendiente 133](../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-3.md), acuerdo 1. Cada análisis se llena con un guion escrito para él, y ya hay 49 en `historico-chat/scripts/`. Casi todos hacen una de dos cosas: llenar el encabezado (las rutas y las copias del pendiente y del hallazgo) o poner el texto de una sección.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Al prender un análisis nuevo, Cimiento pone las rutas del estándar y la copia del pendiente |
| RN-02 | En el análisis 1, también la copia del hallazgo que nombra el «De dónde sale» del pendiente; en los siguientes, el hallazgo que lo abre es nuevo y lo pone el agente |
| RN-03 | Lo que Cimiento no encuentra queda con su marca, para el agente |
| RN-04 | El comando reemplaza el texto de una sección por el que se le da; si la sección no existe, falla diciendo cuáles hay |

### 3.2 Supuestos

- Los análisis siguen siendo archivos `.md` hasta la EP-030·HU-003.

### 3.3 Fuera de alcance

- Pasar los análisis a la base: es la EP-030·HU-003.
- Llenar los documentos de cierre de una fase: es el pendiente 147.

---

## 4. Criterios de aceptación

### CA-01 · Al prender, el encabezado queda lleno

**Sale de:** análisis 3 del pendiente 133, punto 2 de «Lo que se tiene que hacer»

```gherkin
Dado un pendiente con su hallazgo enlazado en «De dónde sale»
Cuando se prende su primer análisis
Entonces el análisis trae las rutas del estándar, la copia del pendiente y la copia del hallazgo
Y en el segundo análisis trae las rutas y el pendiente, y deja el hallazgo para el agente
```

**Cómo validarlo:**
1. En `proyectos/cimiento/`, correr `manage.py test core.enganches.tests_llenar_analisis`.
- Aprobado cuando las pruebas pasan.

### CA-02 · Un comando fijo guarda el texto de una sección

**Sale de:** análisis 3 del pendiente 133, punto 3 de «Lo que se tiene que hacer»

```gherkin
Dado un análisis con la sección «Lo acordado»
Cuando se corre manage.py analisis seccion «análisis» "Lo acordado" --archivo texto.md
Entonces el texto de esa sección queda reemplazado y el resto del análisis igual
Y con una sección que no existe, falla diciendo cuáles hay
```

**Cómo validarlo:**
1. Correr `manage.py test core.enganches.tests_llenar_analisis`.
- Aprobado cuando las pruebas pasan.

### Criterios de aceptación transversales

- [ ] No regresión: prender un análisis sigue igual en todo lo demás.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Robustez** | Si llenar el encabezado falla, el análisis se crea igual, con la plantilla tal cual |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Mockup o prototipo | No aplica |
| Documento funcional | [Análisis 3 del pendiente 133](../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-3.md), acuerdo 1 |
| Contrato de API | No aplica |
| Modelo de datos afectado | Ninguno |

---

## 7. Tareas técnicas derivadas

- [ ] Llenar el encabezado al prender.
- [ ] El comando para guardar una sección.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| [`A-EP-025-HU-033-encabezado-y-secciones`](A-EP-025-HU-033-encabezado-y-secciones/) | CA-01, CA-02 | | [plan_trabajo](A-EP-025-HU-033-encabezado-y-secciones/plan_trabajo.md) | [plan_pruebas](A-EP-025-HU-033-encabezado-y-secciones/plan_pruebas.md) | [resultado](A-EP-025-HU-033-encabezado-y-secciones/resultado_pruebas.md) | Cerrada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | La plantilla del análisis cambia sus marcas | El encabezado deja de llenarse; las marcas se leen de una sola lista |

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
| **V**aliosa | Sí | Se acaban los guiones sueltos para llenar análisis |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-09 | El agente | Creación de la HU, desde el análisis 3 del pendiente 133 |
