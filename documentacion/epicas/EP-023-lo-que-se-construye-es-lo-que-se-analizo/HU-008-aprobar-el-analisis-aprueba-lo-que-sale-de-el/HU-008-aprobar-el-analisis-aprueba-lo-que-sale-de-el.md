# HU-008 · Aprobar el análisis aprueba lo que sale de él

> Sus criterios salen de «Lo que se tiene que hacer» del [análisis 1 del pendiente 116](../../../../historico-chat/resumenes/2026-10-04/pendientes/116-el-codigo-de-cimiento-se-repite-en-vez-de-reusarse/analisis-1.md), punto 8, que sale de su acuerdo 6. Los campos que no son alcance (módulo, tipo, estimación y responsable) son propuesta del agente y esperan la aprobación del usuario.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-008 |
| **Épica / Feature** | [EP-023 Lo que se construye es lo que se analizó](../epica.md) |
| **Módulo / Componente** | `base/02-flujo-de-trabajo/`, `plantillas/ciclo-vida-proyectos/`, `proyectos/cimiento/core/enganches/` |
| **Tipo** | Técnica |
| **Prioridad** | Primera del análisis 1 del pendiente 116 (acuerdo 6: «va de primero en el orden») |
| **Estimación** | S |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Terminada el 2026-10-04, con sus tres criterios probados |

---

## 2. Narrativa

- **Como** el usuario, que aprueba el análisis completo con sus acuerdos y lo que se tiene que hacer
- **Quiero** que aprobar el análisis apruebe también los planes que salen de él y cumplen sus filas
- **Para** no tener que aprobar otra vez, fase por fase, lo que ya aprobé al cerrar el análisis

---

## 3. Contexto y descripción

Hoy `02·F4` pide un OK explícito para cada plan y `02·F25` aclara que el permiso de arrancar no lo es. Con un análisis aprobado, ese segundo OK repite lo ya decidido: el usuario lo dijo en la sesión del 2026-10-04 («si aprueba el análisis no me tiene que estar preguntando cada rato si apruebo»). El acuerdo 6 lo resuelve cambiando las dos reglas, sin crear una nueva (`20·M12`).

### 3.1 Reglas de negocio

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | El plan que sale de un análisis aprobado y cumple sus filas queda aprobado | Análisis 1 del pendiente 116, acuerdo 6 |
| RN-02 | Lo que el análisis no contempló pide aprobación otra vez | Acuerdo 6 |
| RN-03 | La marca de aprobación del plan cita el análisis que la da | Punto 8 |
| RN-04 | Se cambian `02·F4` y `02·F25`; no se crea una regla nueva | Acuerdo 6 |
| RN-05 | Un plan «cumple las filas» del análisis cuando su HU está nombrada en una fila de «Lo que se tiene que hacer» | Punto 8 |

### 3.2 Supuestos

- Que el análisis aprobado lleva la marca `> **Aprobado**` que ya lee `core/enganches/analisis_en_curso.py`.

### 3.3 Fuera de alcance

- Aprobar planes de HU que el análisis no nombra.
- Las otras filas del análisis 1 del pendiente 116.

---

## 4. Criterios de aceptación

### CA-01 · Las reglas dicen que el análisis aprobado aprueba sus planes

**Sale de:** análisis 1, punto 8 (del pendiente 116).

```gherkin
Dado que se leen 02·F4 y 02·F25
Cuando un plan sale de un análisis aprobado y cumple sus filas
Entonces las dos reglas lo dan por aprobado, citando el análisis
Y lo que el análisis no contempló sigue pidiendo el OK explícito
```

**Cómo validarlo:**
1. Abrir `base/02-flujo-de-trabajo/reglas/` y leer `F4` y `F25`.
2. Abrir `CHANGELOG.md` y `VERSION`.

**Aprobado cuando:** las dos reglas lo dicen, `CHANGELOG.md` trae la entrada y `VERSION` sube de versión mayor.

### CA-02 · El plan aprobado por un análisis lo cita, y el programa lo acepta

**Sale de:** análisis 1, punto 8 (del pendiente 116).

```gherkin
Dado un plan cuya línea de aprobación cita un análisis aprobado que nombra su HU
Cuando el freno o la comparación del commit leen el plan
Entonces lo tratan como aprobado
Y si el análisis no está aprobado, o no nombra la HU, no lo tratan como aprobado
```

**Cómo validarlo:**
1. Correr `python manage.py test core.enganches.tests_freno` desde `proyectos/cimiento/`.
2. Revisar los casos del plan que cita un análisis aprobado, uno sin aprobar y uno que no nombra la HU.

**Aprobado cuando:** el primero cuenta como aprobado y los otros dos no.

### CA-03 · La plantilla del plan permite citar el análisis

**Sale de:** análisis 1, punto 8 (del pendiente 116).

```gherkin
Dado la plantilla del plan de trabajo
Cuando se llena la línea de aprobación
Entonces dice cómo escribirla cuando la aprobación viene de un análisis
```

**Cómo validarlo:**
1. Abrir `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md`, fila **Aprobación**.

**Aprobado cuando:** la fila muestra las dos formas: la persona con fecha y versión, o el análisis aprobado con su enlace.

### Criterios de aceptación transversales

- [x] No regresión: lo existente sigue funcionando; la suite relacionada queda verde (`08`, [`02·F5`](../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)).

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Compatibilidad** | Los planes aprobados por una persona siguen valiendo igual |

---

## 6. Diseño y referencias

- Documento funcional: [análisis 1 del pendiente 116](../../../../historico-chat/resumenes/2026-10-04/pendientes/116-el-codigo-de-cimiento-se-repite-en-vez-de-reusarse/analisis-1.md), acuerdo 6 y punto 8.

---

## 7. Tareas técnicas derivadas

- [ ] Cambiar `02·F4` y `02·F25`, con su entrada en `CHANGELOG.md` y la versión mayor.
- [ ] Ajustar la fila **Aprobación** de la plantilla del plan.
- [ ] Hacer que `PlanDeTrabajo` acepte la aprobación que cita un análisis aprobado que nombra la HU.
- [ ] Pruebas en `tests_freno.py`.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-023-HU-008-el-plan-cita-el-analisis-que-lo-aprueba` | CA-01, CA-02, CA-03 | (vacío) | [plan_trabajo.md](A-EP-023-HU-008-el-plan-cita-el-analisis-que-lo-aprueba/plan_trabajo.md) | [plan_pruebas.md](A-EP-023-HU-008-el-plan-cita-el-analisis-que-lo-aprueba/plan_pruebas.md) | [resultado_pruebas.md](A-EP-023-HU-008-el-plan-cita-el-analisis-que-lo-aprueba/resultado_pruebas.md) | Cerrada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Que un plan se dé por aprobado con un análisis que no lo contempló | Se exige que el análisis nombre la HU del plan (RN-05) |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-04 | Claude | Creación de la HU desde el análisis 1 del pendiente 116 |
