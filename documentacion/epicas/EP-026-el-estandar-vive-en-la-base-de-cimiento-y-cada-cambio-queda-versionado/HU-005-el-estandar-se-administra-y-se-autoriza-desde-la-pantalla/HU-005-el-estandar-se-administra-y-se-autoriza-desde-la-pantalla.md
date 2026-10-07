# HU-005 · El estándar se administra y se autoriza desde la pantalla

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-005 |
| **Épica / Feature** | [EP-026 — El estándar vive en la base de Cimiento y cada cambio queda versionado](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/estandar/` |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | L |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien administra Cimiento
- **Quiero** cambiar el estándar y la memoria de cada proyecto desde la pantalla, y aprobar ahí lo que proponga el agente
- **Para** que todo cambio pase por mi aprobación y quede con su historia y su versión

---

## 3. Contexto y descripción

Hoy el estándar se edita a mano en archivos. Sale del [análisis 1 del pendiente 132](../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md), acuerdos 2, 3, 10 y 17, puntos 10 y 11 de «Lo que se tiene que hacer».

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | El administrador crea, cambia y quita documentos del estándar desde la pantalla; cada envío hace las dos preguntas y sube la versión del estándar (acuerdos 2, 7) |
| RN-02 | Al guardar un documento, el mapa de tareas y las reglas por tarea se vuelven a armar en la base, en la misma versión |
| RN-03 | La memoria de cada proyecto se ve y se cambia en la pantalla, y el arranque de sesión la lee de la base (acuerdo 17) |
| RN-04 | Lo que propone el agente o un programa queda como propuesta; se aplica solo cuando el administrador la aprueba en la pantalla (acuerdo 3) |
| RN-05 | El grupo consulta ve, no cambia ni aprueba |
| RN-06 | El agente lee un documento o un recuerdo de la base con una orden, sin tocar la pantalla |

### 3.2 Supuestos

- El texto se edita como markdown, igual que en los archivos.

### 3.3 Fuera de alcance

- Congelar `base/` (HU-006).

---

## 4. Criterios de aceptación

### CA-01 · El administrador cambia un documento y queda versionado

**Sale de:** análisis 1 del pendiente 132, punto 10 de «Lo que se tiene que hacer»

```gherkin
Dado un documento del estándar
Cuando el administrador lo cambia en la pantalla respondiendo las dos preguntas
Entonces el documento cambia, la historia tiene el cambio y el estándar sube la versión que dicen las respuestas
Y el mapa de tareas y las reglas por tarea quedan armados de nuevo en esa misma versión
```

**Cómo validarlo:** correr `manage.py test core.estandar` → resultado esperado: el caso pasa.

### CA-02 · Crear y quitar un documento

**Sale de:** análisis 1 del pendiente 132, acuerdo 10

```gherkin
Dado el administrador en la pantalla
Cuando crea un documento bajo base/ o quita uno
Entonces queda creado o quitado, con su cambio en la historia
Y una ruta fuera de base/ se rechaza
```

**Cómo validarlo:** correr `manage.py test core.estandar` → resultado esperado: el caso pasa.

### CA-03 · La memoria de cada proyecto en la pantalla y en el arranque

**Sale de:** análisis 1 del pendiente 132, acuerdo 17

```gherkin
Dado un proyecto con recuerdos en la base
Cuando el administrador cambia o crea un recuerdo
Entonces queda con su historia y sube la versión del proyecto
Y el arranque de sesión del proyecto muestra el índice que está en la base
```

**Cómo validarlo:** correr `manage.py test core.estandar` → resultado esperado: el caso pasa.

### CA-04 · Lo que propone el agente se aprueba en la pantalla

**Sale de:** análisis 1 del pendiente 132, punto 11 de «Lo que se tiene que hacer»

```gherkin
Dado que el agente propone un texto nuevo para un documento con manage.py proponer
Cuando el administrador lo aprueba en la pantalla con las dos preguntas
Entonces el documento cambia con su versión y la propuesta queda aprobada
Y si la rechaza, nada cambia y la propuesta queda rechazada
```

**Cómo validarlo:** correr `manage.py test core.estandar` → resultado esperado: el caso pasa.

### CA-05 · Consulta solo mira, y el agente lee con una orden

**Sale de:** RN-05 y RN-06

```gherkin
Dada una cuenta del grupo consulta
Cuando intenta guardar, quitar o aprobar
Entonces recibe 403 y nada cambia
Y manage.py ver_estandar y manage.py ver_recuerdo imprimen el texto de la base
```

**Cómo validarlo:** correr `manage.py test core.estandar` → resultado esperado: el caso pasa.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Seguridad** | Solo el grupo administrador cambia o aprueba |
| RNF-02 | **Trazabilidad** | Toda propuesta guarda quién la hizo, quién la resolvió y cuándo |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 132](../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md) |
| Modelo de datos afectado | Tabla nueva `estandar_propuesta` |

---

## 7. Tareas técnicas derivadas

- [ ] Pantallas del estándar, la memoria y las propuestas.
- [ ] Armar el mapa en la base al guardar.
- [ ] Órdenes `proponer`, `ver_estandar` y `ver_recuerdo`.
- [ ] El arranque lee la memoria de la base.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-026-HU-005-la-pantalla-del-estandar` |  | (vacío) | [plan_trabajo.md](A-EP-026-HU-005-la-pantalla-del-estandar/plan_trabajo.md) | [plan_pruebas.md](A-EP-026-HU-005-la-pantalla-del-estandar/plan_pruebas.md) | [resultado_pruebas.md](A-EP-026-HU-005-la-pantalla-del-estandar/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-003 y HU-004 | Terminadas |

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
| **V**aliosa | Sí | El estándar se administra donde vive |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | Pantallas de un módulo |
| **T**esteable | Sí | Pruebas de Django |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | El agente | Creación de la HU, desde el análisis 1 del pendiente 132 |
