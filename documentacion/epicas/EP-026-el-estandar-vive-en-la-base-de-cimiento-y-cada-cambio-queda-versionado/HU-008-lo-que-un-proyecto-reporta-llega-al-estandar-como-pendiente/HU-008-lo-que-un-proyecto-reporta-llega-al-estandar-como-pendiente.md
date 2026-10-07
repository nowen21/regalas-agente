# HU-008 · Lo que un proyecto reporta llega al estándar como pendiente

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-008 |
| **Épica / Feature** | [EP-026 — El estándar vive en la base de Cimiento y cada cambio queda versionado](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/estandar/` y el aviso de versión |
| **Tipo** | Funcional |
| **Prioridad** | Should |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien trabaja en un proyecto que hereda el estándar
- **Quiero** reportar al estándar lo que encuentro mal en él, y enterarme cuando se corrige
- **Para** que la corrección llegue a todos los proyectos con su versión

---

## 3. Contexto y descripción

El reporte es hoy un archivo suelto hecho con una plantilla. Sale del [análisis 1 del pendiente 132](../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md), acuerdos 13 y 14, punto 14 de «Lo que se tiene que hacer».

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Un proyecto reporta desde la pantalla o con `manage.py reportar`; el reporte queda abierto, con su historia y sin subir versión (acuerdo 13) |
| RN-02 | Se marca corregido con la versión del estándar que lo corrigió: la versión sube cuando Cimiento corrige, no cuando llega el reporte (acuerdo 13) |
| RN-03 | El proyecto que reportó recibe el aviso al abrir su sesión siguiente, una sola vez |
| RN-04 | Con el estándar en la base, el aviso de versión atrasada compara con la versión de la base, no con `VERSION` (acuerdo 14) |

### 3.2 Supuestos

- El proyecto que reporta está registrado en Cimiento.

### 3.3 Fuera de alcance

- Corregir el estándar: se hace en la pantalla (HU-005).

---

## 4. Criterios de aceptación

### CA-01 · Reportar

**Sale de:** análisis 1 del pendiente 132, punto 14 de «Lo que se tiene que hacer»

```gherkin
Dado un proyecto registrado
Cuando reporta con manage.py reportar o desde la pantalla
Entonces el reporte queda abierto en «Estándar» → «Reportes», con su historia
Y la versión del estándar no cambia
```

**Cómo validarlo:** correr `manage.py test core.estandar` → resultado esperado: el caso pasa.

### CA-02 · Corregir con su versión

**Sale de:** análisis 1 del pendiente 132, acuerdo 13

```gherkin
Dado un reporte abierto y una versión del estándar posterior a él
Cuando el administrador lo marca corregido con esa versión
Entonces el reporte queda corregido y apunta a esa versión
```

**Cómo validarlo:** correr `manage.py test core.estandar` → resultado esperado: el caso pasa.

### CA-03 · El proyecto se entera

**Sale de:** RN-03

```gherkin
Dado un reporte corregido y sin avisar
Cuando el proyecto que lo hizo abre una sesión
Entonces el arranque dice que su reporte quedó corregido y en qué versión
Y en la sesión siguiente ya no lo dice
```

**Cómo validarlo:** correr `manage.py test core.estandar` → resultado esperado: el caso pasa.

### CA-04 · El aviso de versión mira la base

**Sale de:** acuerdo 14

```gherkin
Dado el estándar congelado en la versión X de la base
Cuando un proyecto declara una versión anterior
Entonces el aviso de versión atrasada dice X, y acepta como existentes las versiones de la base
```

**Cómo validarlo:** correr `manage.py test core.estandar` → resultado esperado: el caso pasa.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Trazabilidad** | El reporte guarda quién lo hizo, quién lo resolvió y con qué versión |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 132](../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md) |
| Modelo de datos afectado | Tabla nueva `estandar_reporte` |

---

## 7. Tareas técnicas derivadas

- [ ] Modelo, pantalla y orden `reportar`.
- [ ] Aviso al proyecto al corregir.
- [ ] El aviso de versión mira la base.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-026-HU-008-los-reportes` |  | (vacío) | [plan_trabajo.md](A-EP-026-HU-008-los-reportes/plan_trabajo.md) | [plan_pruebas.md](A-EP-026-HU-008-los-reportes/plan_pruebas.md) | [resultado_pruebas.md](A-EP-026-HU-008-los-reportes/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-002, HU-005 y HU-006 | Terminadas |

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
| **V**aliosa | Sí | Lo que un proyecto encuentra se corrige para todos |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Pruebas de Django |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | El agente | Creación de la HU, desde el análisis 1 del pendiente 132 |
