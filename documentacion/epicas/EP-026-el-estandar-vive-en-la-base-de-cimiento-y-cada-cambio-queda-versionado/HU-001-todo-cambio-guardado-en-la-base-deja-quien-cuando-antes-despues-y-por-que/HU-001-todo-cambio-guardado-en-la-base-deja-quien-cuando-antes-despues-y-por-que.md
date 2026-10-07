# HU-001 · Todo cambio guardado en la base deja quién, cuándo, antes, después y por qué

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-001 |
| **Épica / Feature** | [EP-026 — El estándar vive en la base de Cimiento y cada cambio queda versionado](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/historia/` (nuevo) |
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
- **Quiero** que todo lo que cambia en la base de Cimiento quede en una sola historia
- **Para** saber quién lo cambió, cuándo, cómo estaba, cómo quedó y por qué, y poder deshacerlo

---

## 3. Contexto y descripción

Cada tabla guarda la historia a su manera, o no la guarda: los ajustes de capa 1 y 2 reemplazan el valor viejo sin rastro. Sale del [análisis 1 del pendiente 132](../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md), acuerdos 1, 3, 19 y 21, punto 4 de «Lo que se tiene que hacer».

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Todo crear, cambiar o borrar de una tabla de Cimiento deja un cambio con quién, cuándo, tabla, fila, antes, después y motivo (acuerdos 1 y 19) |
| RN-02 | Vale para toda tabla, también usuarios, grupos y lo que los enganches escriben sin Django (acuerdo 19) |
| RN-03 | Lo que solo se mira no se guarda (acuerdo 21) |
| RN-04 | Nada se borra de la historia, y un cambio se puede deshacer, lo que deja otro cambio (punto 4) |
| RN-05 | Lo que entra a la historia pasa antes por el tapado de claves; las contraseñas quedan como «cambiada» (`00·N6`) |
| RN-06 | El gasto que se trae de Claude Code no entra: cada fila ya es su propia historia, nunca se edita y lleva su fecha |

### 3.2 Supuestos

- Una sola máquina y una sola persona.

### 3.3 Fuera de alcance

- La versión de cada cambio: es la HU-002.

---

## 4. Criterios de aceptación

### CA-01 · Un cambio en cualquier tabla queda en la historia

**Sale de:** análisis 1 del pendiente 132, punto 4 de «Lo que se tiene que hacer»

```gherkin
Dado un ajuste de un proyecto con valor 2000
Cuando una cuenta lo cambia a 3000 con un motivo
Entonces la historia tiene un cambio con esa cuenta, la hora, la tabla, la fila, antes 2000, después 3000 y el motivo
Y lo mismo pasa al crear y al borrar, en cualquier tabla de Cimiento, también en usuarios y grupos
```

**Cómo validarlo:** correr `manage.py test core.historia` → resultado esperado: los casos de crear, cambiar y borrar pasan.

### CA-02 · Lo que escriben los enganches también queda

**Sale de:** análisis 1 del pendiente 132, acuerdo 19

```gherkin
Dado que el enganche del análisis escribe su estado sin Django
Cuando prende, cambia o apaga el análisis de una sesión
Entonces la historia tiene el cambio, con quién «agente»
```

**Cómo validarlo:** correr `manage.py test core.historia` → resultado esperado: el caso del estado del análisis pasa.

### CA-03 · Un cambio se puede deshacer

**Sale de:** análisis 1 del pendiente 132, punto 4 de «Lo que se tiene que hacer»

```gherkin
Dado un cambio de un ajuste de 2000 a 3000
Cuando el administrador lo deshace desde la pantalla «Historia»
Entonces el ajuste vuelve a 2000
Y la historia suma otro cambio que dice qué deshizo
```

**Cómo validarlo:** correr `manage.py test core.historia` y abrir `/historia/` → resultado esperado: el caso de deshacer pasa y la pantalla lista los cambios con su botón.

### CA-04 · Sin claves en la historia

**Sale de:** `00·N6`

```gherkin
Dado que una cuenta cambia su contraseña
Cuando se guarda el cambio
Entonces la historia dice «cambiada» y no guarda el valor
```

**Cómo validarlo:** correr `manage.py test core.historia` → resultado esperado: el caso de la contraseña pasa.

### Criterios de aceptación transversales

- [ ] No regresión: las pruebas de `core.proyectos`, `core.niveles` y `core.cuentas` siguen en verde.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Seguridad** | El grupo consulta ve la historia pero no deshace |
| RNF-02 | **Rendimiento** | Registrar un cambio no cambia el tiempo de una pantalla de forma visible: una consulta antes y una escritura después |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Mockup o prototipo | No aplica |
| Documento funcional | [Análisis 1 del pendiente 132](../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md) |
| Contrato de API | No aplica |
| Modelo de datos afectado | Tabla nueva `historia_cambio` |

---

## 7. Tareas técnicas derivadas

- [ ] Módulo `core/historia` con el modelo `Cambio` y su registro por señales de Django.
- [ ] El estado del análisis escribe su cambio en la historia.
- [ ] Pantalla «Historia» con filtros y el botón de deshacer.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-026-HU-001-el-registro-de-cambios` |  | (vacío) | [plan_trabajo.md](A-EP-026-HU-001-el-registro-de-cambios/plan_trabajo.md) | [plan_pruebas.md](A-EP-026-HU-001-el-registro-de-cambios/plan_pruebas.md) | [resultado_pruebas.md](A-EP-026-HU-001-el-registro-de-cambios/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Que la historia crezca rápido | El gasto no entra (RN-06); lo demás cambia poco |

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
| **I**ndependiente | Sí | No depende de otra HU |
| **N**egociable | Sí | |
| **V**aliosa | Sí | Ningún cambio se pierde |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | Un módulo |
| **T**esteable | Sí | Pruebas de Django |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | El agente | Creación de la HU, desde el análisis 1 del pendiente 132 |
