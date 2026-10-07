# HU-007 · Un botón de la pantalla guarda en git lo que cambió en Cimiento

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-007 |
| **Épica / Feature** | [EP-026 — El estándar vive en la base de Cimiento y cada cambio queda versionado](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/estandar/` |
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
- **Quiero** aprobar y hacer desde la pantalla el commit de lo que cambió una sesión, y subirlo si quiero
- **Para** que el commit, como todo lo demás, se autorice en la pantalla

---

## 3. Contexto y descripción

El commit se pide aparte en el chat y se hace a mano. Sale del [análisis 1 del pendiente 132](../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md), acuerdos 3, 8 y 22, punto 13 de «Lo que se tiene que hacer».

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | La pantalla muestra lo que cambió cada sesión, lo que tocaron dos y lo que no tiene sesión (acuerdo 22) |
| RN-02 | El botón prepara solo lo de una sesión, hace el commit con la convención del repositorio (primero la idea del usuario, después lo que hizo el agente, sin `Co-Authored-By`) y, si se pide, lo sube con la cuenta de git del computador |
| RN-03 | Si el commit falla, se suelta lo preparado y el cambio queda «sin subir», con el error a la vista; si falla solo la subida, el commit queda y se dice |
| RN-04 | Solo el grupo administrador lo usa; oprimirlo es la aprobación del commit (acuerdo 3) |

### 3.2 Supuestos

- Git y la cuenta para subir ya están configurados en el computador; Cimiento no guarda claves (`00·N6`).

### 3.3 Fuera de alcance

- Resolver lo que tocaron dos sesiones: se nombra y decide quien hace el commit.

---

## 4. Criterios de aceptación

### CA-01 · Se ve lo que cambió cada sesión

**Sale de:** análisis 1 del pendiente 132, punto 13 de «Lo que se tiene que hacer»

```gherkin
Dado un repositorio con cambios de dos sesiones y uno compartido
Cuando se abre la pantalla «Subir a git»
Entonces lista los archivos de cada sesión, el compartido y los que no tienen sesión
```

**Cómo validarlo:** correr `manage.py test core.estandar` → resultado esperado: el caso pasa.

### CA-02 · El botón hace el commit de una sesión

**Sale de:** análisis 1 del pendiente 132, acuerdo 22

```gherkin
Dado lo que cambió una sesión
Cuando el administrador escribe el asunto, la idea y lo hecho y oprime el botón
Entonces el commit lleva solo los archivos de esa sesión, con la idea primero y sin Co-Authored-By
```

**Cómo validarlo:** correr `manage.py test core.estandar` → resultado esperado: el caso pasa.

### CA-03 · Si falla, nada queda a medias

**Sale de:** RN-03

```gherkin
Dado un commit que git rechaza
Cuando se oprime el botón
Entonces lo preparado se suelta y la pantalla dice el error, y nada queda en git
```

**Cómo validarlo:** correr `manage.py test core.estandar` → resultado esperado: el caso pasa.

### CA-04 · Consulta no hace commits

**Sale de:** RN-04

```gherkin
Dada una cuenta del grupo consulta
Cuando oprime el botón
Entonces recibe 403 y no hay commit
```

**Cómo validarlo:** correr `manage.py test core.estandar` → resultado esperado: el caso pasa.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Seguridad** | Cimiento no guarda claves de git: usa las del computador |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 132](../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md) |
| Modelo de datos afectado | Ninguno |

---

## 7. Tareas técnicas derivadas

- [ ] Hacer el commit y subirlo desde un programa, con su contraria si falla.
- [ ] Pantalla «Subir a git».

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-026-HU-007-subir-a-git` |  | (vacío) | [plan_trabajo.md](A-EP-026-HU-007-subir-a-git/plan_trabajo.md) | [plan_pruebas.md](A-EP-026-HU-007-subir-a-git/plan_pruebas.md) | [resultado_pruebas.md](A-EP-026-HU-007-subir-a-git/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | El control del commit tarda | La pantalla espera; el error del control se muestra entero |

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
| **V**aliosa | Sí | El commit se aprueba donde se aprueba todo |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Pruebas con un repositorio temporal |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | El agente | Creación de la HU, desde el análisis 1 del pendiente 132 |
