# HU-002 · Las 269 reglas pasan a las tablas sin perder nada

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-002 |
| **Épica / Feature** | [EP-027 · Las reglas del estándar viven en tablas con la estructura del molde](../epica.md) |
| **Módulo / Componente** | Estándar en la base: `core/estandar/` |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien administra el estándar
- **Quiero** que todas las reglas que hoy están en el texto pasen a sus tablas
- **Para** tenerlas por casillas sin escribirlas de nuevo y sin perder nada de lo que dicen

---

## 3. Contexto y descripción

Las tablas de la HU-001 están vacías. Las reglas están en el texto de los documentos de la base: 269 en los archivos de `base/` y 270 en la base viva. «Validable» no está en el texto: lo registra `validadores/reglas-validables.md`. Sale del [análisis 1 del pendiente 136](../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md), acuerdo 1.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Cada regla del texto queda en una fila, con sus casillas, su capítulo, su documento y su lugar dentro de él |
| RN-02 | Cada capítulo queda en su fila, con su número, su nombre y sus letras |
| RN-03 | Las tareas de cada «Aplica a» quedan en la tabla de tareas, en el orden en que se escribieron |
| RN-04 | Las dependencias de `20·M7` quedan en su tabla, unidas a la regla de destino |
| RN-05 | «Validable» toma lo que dice `validadores/reglas-validables.md`: «sí» con su programa, «falta el programa» o «no»; la regla que no figura queda «sin declarar» |
| RN-06 | Las notas con fecha del sello («Corregida el...», «Partida el...») pasan a la historia de cambios de su regla, con su fecha, y salen del sello (acuerdo 1) |
| RN-07 | El texto de cada documento se arma de nuevo desde las tablas; el texto anterior queda en la historia |
| RN-08 | Todo el paso es una sola versión del estándar; si una regla no pasa, nada pasa y se dice cuál |
| RN-09 | Pasar de nuevo no duplica nada: actualiza lo que ya está |

### 3.2 Supuestos

- Las notas con fecha están todas en el sello: 156, medidas el 2026-10-07. El agente no recibe el sello (`MapaDeTareas.cuerpo`).

### 3.3 Fuera de alcance

- Que los cambios siguientes pasen por las tablas: HU-003.
- Las reglas de cada proyecto: HU-006.

---

## 4. Criterios de aceptación

### CA-01 · Todas las reglas quedan en las tablas

**Sale de:** acuerdo 1 del análisis 1 del pendiente 136

```gherkin
Dado el estándar en la base
Cuando se pasan las reglas a las tablas
Entonces cada regla del texto tiene su fila con sus casillas, su capítulo, sus tareas y sus dependencias
Y su «validable» es el del registro
```

**Cómo validarlo:** correr `manage.py test core.estandar.tests_pasar_reglas` → resultado esperado: los casos pasan.

### CA-02 · Nada se pierde

**Sale de:** acuerdo 1 del análisis 1 del pendiente 136

```gherkin
Dado las reglas ya en las tablas
Cuando se arma cada documento desde ellas
Entonces da el texto de antes, sin las notas con fecha del sello
Y cada nota está en la historia de su regla, con su fecha
```

**Cómo validarlo:** correr `manage.py test core.estandar.tests_pasar_reglas` → resultado esperado: los casos pasan.

### CA-03 · Pasar dos veces no duplica

**Sale de:** RN-09

```gherkin
Dado las reglas ya en las tablas
Cuando se pasan otra vez
Entonces no aparece ninguna fila nueva ni ninguna nota repetida
```

**Cómo validarlo:** correr `manage.py test core.estandar.tests_pasar_reglas` → resultado esperado: el caso pasa.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Atomicidad** | El paso es todo o nada |
| RNF-02 | **Auditoría** | Queda en la historia, en una sola versión |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 136](../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md) |
| Modelo de datos afectado | Las tablas de la HU-001; `estandar_documento`; `historia_cambio` |

---

## 7. Tareas técnicas derivadas

- [ ] El paso de un documento a las tablas, y su texto desde ellas.
- [ ] El comando que pasa todo el estándar.
- [ ] Pruebas, y el paso en la base viva.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-027-HU-002-el-paso` | CA-01, CA-02, CA-03 | (vacío) | [plan_trabajo.md](A-EP-027-HU-002-el-paso/plan_trabajo.md) | [plan_pruebas.md](A-EP-027-HU-002-el-paso/plan_pruebas.md) | [resultado_pruebas.md](A-EP-027-HU-002-el-paso/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-001 | Terminada |
| Riesgo | Una nota que no es con fecha sale del sello por error | Solo se toman los párrafos del sello que abren con negrita y una fecha; el texto anterior queda en la historia |

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
| **V**aliosa | Sí | Las tablas quedan llenas |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Pruebas de Django |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-07 | El agente | Creación de la HU, desde el análisis 1 del pendiente 136 |
