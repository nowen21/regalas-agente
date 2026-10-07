# HU-004 · Los enganches leen el estándar de la base

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-004 |
| **Épica / Feature** | [EP-026 — El estándar vive en la base de Cimiento y cada cambio queda versionado](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/estandar/` y los lectores del estándar |
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
- **Quiero** que las reglas que recibe el agente, lo que el freno deja escribir y el arranque de sesión salgan de la base
- **Para** que el estándar que rige sea el de la base y no el de los archivos

---

## 3. Contexto y descripción

`recuperar.py`, el mapa de tareas, el freno y el arranque leen `base/` del disco. Sale del [análisis 1 del pendiente 132](../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md), acuerdos 5 y 9, puntos 8 y 9 de «Lo que se tiene que hacer».

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Las reglas de cada mensaje, las autorizaciones del freno y el arranque se leen de la base (acuerdo 5) |
| RN-02 | Si la base no responde, el enganche de reglas lo dice y el freno no deja modificar nada (acuerdo 9) |
| RN-03 | Una carpeta que no es la del estándar se sigue leyendo del disco |
| RN-04 | Antes de encender la lectura, la base se pone al día con lo guardado en git desde la importación, con su versión |

### 3.2 Supuestos

- La base es local: leer todos los documentos en cada enganche cuesta poco.

### 3.3 Fuera de alcance

- Editar el estándar en la base (HU-005) y congelar `base/` (HU-006).

---

## 4. Criterios de aceptación

### CA-01 · Las reglas salen de la base

**Sale de:** análisis 1 del pendiente 132, punto 8 de «Lo que se tiene que hacer»

```gherkin
Dado un documento del estándar que en la base dice algo distinto que en el archivo
Cuando el enganche de reglas, el freno o el arranque lo leen
Entonces leen lo de la base
```

**Cómo validarlo:** correr `manage.py test core.estandar` → resultado esperado: el caso pasa.

### CA-02 · Sin base, se dice y el freno no deja modificar

**Sale de:** análisis 1 del pendiente 132, punto 9 de «Lo que se tiene que hacer»

```gherkin
Dado que la base no responde
Cuando llega un mensaje
Entonces el enganche de reglas dice que no hay base y que no se trabaja
Y el freno no deja modificar nada
```

**Cómo validarlo:** correr `manage.py test core.estandar` → resultado esperado: el caso pasa.

### CA-03 · Mismas reglas que antes

**Sale de:** `02·F7`, no romper lo existente

```gherkin
Dada la base al día con los archivos
Cuando se elige qué reglas llegan con un mensaje
Entonces llegan las mismas que leyendo los archivos
```

**Cómo validarlo:** correr `manage.py test core.estandar` → resultado esperado: el caso pasa.

### CA-04 · La base se pone al día con git

**Sale de:** RN-04

```gherkin
Dados documentos de base/ que cambiaron en git desde la importación
Cuando se corre manage.py sincronizar_estandar
Entonces la base toma lo guardado en git, cada cambio en la historia, y el estándar sube una versión
```

**Cómo validarlo:** correr `manage.py test core.estandar` → resultado esperado: el caso pasa.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | Una sola consulta por proceso para todo el estándar |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 132](../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md) |
| Modelo de datos afectado | Ninguno |

---

## 7. Tareas técnicas derivadas

- [ ] Lector del estándar desde la base, con la cara de `Archivos`.
- [ ] Los lectores lo usan.
- [ ] `sincronizar_estandar`.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-026-HU-004-leer-de-la-base` |  | (vacío) | [plan_trabajo.md](A-EP-026-HU-004-leer-de-la-base/plan_trabajo.md) | [plan_pruebas.md](A-EP-026-HU-004-leer-de-la-base/plan_pruebas.md) | [resultado_pruebas.md](A-EP-026-HU-004-leer-de-la-base/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Otra sesión edita `base/` después de encender la lectura y su cambio no rige | Se enciende cuando `base/` no tiene cambios sin guardar, y la HU-006 lo congela en seguida |

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
| **I**ndependiente | Sí | Usa la HU-003 ya terminada |
| **N**egociable | Sí | |
| **V**aliosa | Sí | Rige el estándar de la base |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Pruebas de Django |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-06 | El agente | Creación de la HU, desde el análisis 1 del pendiente 132 |
