# HU-001 · El capítulo 17 rige para todo proyecto con pantallas y exige que la pantalla oriente sola

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-001 |
| **Épica / Feature** | [EP-028 · Las pantallas orientan al usuario sin que conozca cómo está armado el sistema](../epica.md) |
| **Módulo / Componente** | El capítulo `17` del estándar, en la base de Cimiento, y `core/proyectos/ajustes.py` |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien construye las pantallas de un proyecto que hereda el estándar
- **Quiero** que el capítulo 17 rija siempre que haya pantallas y que exija que la pantalla oriente sola
- **Para** que ningún proyecto pueda apagar lo que hace usable su interfaz

---

## 3. Contexto y descripción

El capítulo `17 · Interfaz` es opt-in, no exige que la pantalla oriente sola y su regla `I5` remite a un sistema de diseño que ningún proyecto declara. Sale del [análisis 1 del pendiente 137](../../../../historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/analisis-1.md), puntos 2 y 3 de «Lo que se tiene que hacer».

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Los cambios del estándar se proponen y se aprueban en «Estándar» → «Propuestas» (análisis 1 del pendiente 132, acuerdo 3) |
| RN-02 | El capítulo `17` rige para todo proyecto con pantallas; uno sin pantallas no tiene a qué aplicarlo (acuerdo 2) |
| RN-03 | La regla nueva exige una sola cosa: que la pantalla oriente sola (`20·M5`) |
| RN-04 | `17·I5` pide usar lo que trae la plantilla instalada antes de crear nada (acuerdos 2 y 3) |
| RN-05 | El ajuste `opt_in_17` desaparece: ya no hay nada que prender ni apagar |

### 3.2 Supuestos

- Las reglas cambiadas pasan su checklist en el mismo texto que se propone.

### 3.3 Fuera de alcance

- La guía de diseño (HU-002).

---

## 4. Criterios de aceptación

### CA-01 · El capítulo 17 rige para todo proyecto con pantallas

**Sale de:** análisis 1 del pendiente 137, punto 2

```gherkin
Dado el estándar en la base
Cuando se lee el capítulo 17
Entonces su encabezado no dice opt-in
Y un proyecto con el ajuste opt_in_17 en «no» recibe igual sus reglas
Y el ajuste opt_in_17 ya no existe
```

**Cómo validarlo:** correr `manage.py test core.estandar.tests_capitulo17` → resultado esperado: el caso pasa.

### CA-02 · La pantalla orienta sola, y la plantilla instalada va primero

**Sale de:** punto 3

```gherkin
Dado el estándar en la base
Cuando se lee el capítulo 17
Entonces trae la regla I7, «La pantalla orienta sola», con su checklist
Y I5 pide usar lo que trae la plantilla instalada antes de crear un componente
```

**Cómo validarlo:** correr `manage.py test core.estandar.tests_capitulo17` → resultado esperado: el caso pasa.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Trazabilidad** | Cada cambio queda en la historia con su propuesta y su versión |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 137](../../../../historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/analisis-1.md) |
| Modelo de datos afectado | Sale la clave `opt_in_17` de los ajustes |

---

## 7. Tareas técnicas derivadas

- [ ] Proponer el capítulo 17 cambiado.
- [ ] Quitar el ajuste `opt_in_17`.
- [ ] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-028-HU-001-el-capitulo-17-obligatorio` |  | (vacío) | [plan_trabajo.md](A-EP-028-HU-001-el-capitulo-17-obligatorio/plan_trabajo.md) | [plan_pruebas.md](A-EP-028-HU-001-el-capitulo-17-obligatorio/plan_pruebas.md) | [resultado_pruebas.md](A-EP-028-HU-001-el-capitulo-17-obligatorio/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | La aprobación del usuario en «Propuestas» | Sin ella, la fase no cierra |

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
| **V**aliosa | Sí | Ningún proyecto apaga lo que hace usable su interfaz |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Pruebas de Django |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-07 | El agente | Creación de la HU, desde el análisis 1 del pendiente 137 |
