# HU-003 · El estándar 55.1.0 entra a la base

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-003 |
| **Épica / Feature** | [EP-026 — El estándar vive en la base de Cimiento y cada cambio queda versionado](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/estandar/` (nuevo) |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien administra Cimiento
- **Quiero** que el estándar y la memoria de cada proyecto queden en la base de Cimiento
- **Para** administrarlos y leerlos desde ahí, y no desde archivos

---

## 3. Contexto y descripción

El estándar vive en archivos de `base/`. Sale del [análisis 1 del pendiente 132](../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md), acuerdos 2, 5, 6, 10 y 17, punto 7 de «Lo que se tiene que hacer». El título dice 55.1.0 porque esa era la versión al aprobar el análisis; entra la versión que tenga el estándar el día de la importación.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Todo documento de `base/` entra a la base tal como está, con su ruta: los capítulos, las reglas, los anexos, las tareas, las palabras clave y el mapa (acuerdo 10) |
| RN-02 | Las plantillas siguen en archivos (acuerdo 5) |
| RN-03 | La memoria de cada proyecto registrado entra a la base, un recuerdo por registro (acuerdo 17, `01·C19`) |
| RN-04 | La importación es la primera versión del estándar en la base, con el número del archivo `VERSION`; lo anterior queda en git (acuerdo 6) |
| RN-05 | Se importa una sola vez: si la base ya tiene el estándar, no se vuelve a importar encima |
| RN-06 | Lo que se guarda en el estándar tiene historia y sube la versión del estándar (HU-001, HU-002) |

### 3.2 Supuestos

- Los documentos de `base/` son texto UTF-8.

### 3.3 Fuera de alcance

- Leer el estándar desde la base: es la HU-004.
- Editarlo desde la pantalla: es la HU-005.

---

## 4. Criterios de aceptación

### CA-01 · Todo `base/` entra a la base

**Sale de:** análisis 1 del pendiente 132, punto 7 de «Lo que se tiene que hacer»

```gherkin
Dado el estándar en archivos
Cuando se corre manage.py importar_estandar
Entonces cada archivo de base/ queda en la base con su ruta y su texto exacto
Y las reglas que se leen de la base son las mismas que se leen de los archivos
```

**Cómo validarlo:** correr `manage.py test core.estandar` → resultado esperado: el caso pasa.

### CA-02 · La memoria de cada proyecto entra a la base

**Sale de:** análisis 1 del pendiente 132, acuerdo 17

```gherkin
Dado un proyecto registrado con recuerdos en historico-chat/memory/
Cuando se importa
Entonces cada recuerdo queda en la base, del proyecto, con su nombre y su texto
```

**Cómo validarlo:** correr `manage.py test core.estandar` → resultado esperado: el caso pasa.

### CA-03 · La importación es la versión de partida y no se repite

**Sale de:** análisis 1 del pendiente 132, acuerdo 6

```gherkin
Dado el archivo VERSION con la versión X
Cuando se importa
Entonces el estándar queda en la versión X en la base, y cada documento importado es un cambio de esa versión
Y una segunda importación se niega
```

**Cómo validarlo:** correr `manage.py test core.estandar` → resultado esperado: el caso pasa.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Integridad** | El texto que sale de la base es idéntico, carácter por carácter, al del archivo |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 132](../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md) |
| Modelo de datos afectado | Tablas nuevas `estandar_documento` y `estandar_recuerdo` |

---

## 7. Tareas técnicas derivadas

- [ ] Módulo `core/estandar` con `Documento` y `Recuerdo`.
- [ ] Orden `importar_estandar`.
- [ ] Importar en la base real.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-026-HU-003-la-importacion` |  | (vacío) | [plan_trabajo.md](A-EP-026-HU-003-la-importacion/plan_trabajo.md) | [plan_pruebas.md](A-EP-026-HU-003-la-importacion/plan_pruebas.md) | [resultado_pruebas.md](A-EP-026-HU-003-la-importacion/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | EP-001·HU-041, HU-001 y HU-002 | Terminadas |

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
| **V**aliosa | Sí | El estándar queda donde se administra |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Pruebas de Django |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | El agente | Creación de la HU, desde el análisis 1 del pendiente 132 |
