# HU-007 · Las reglas `20·M5` y `20·M9` dicen que la regla vive en casillas

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-007 |
| **Épica / Feature** | [EP-027 · Las reglas del estándar viven en tablas con la estructura del molde](../epica.md) |
| **Módulo / Componente** | El capítulo `20` del estándar, en la base de Cimiento |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien escribe o cambia una regla del estándar
- **Quiero** que `20·M5` y `20·M9` digan que cada parte de la regla va en su casilla
- **Para** que las reglas del molde no manden a escribir textos enteros ni a anotar en un archivo lo que ahora es una casilla

---

## 3. Contexto y descripción

`20·M5` describe la regla como un texto con encabezado, y `20·M9` manda a registrar si es validable en `validadores/reglas-validables.md`. Con la EP-027 las dos cosas pasan a casillas. Sale del [análisis 1 del pendiente 136](../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md), punto 12 de «Lo que se tiene que hacer», y de la decisión del 2026-10-07 sobre los tres valores de «validable» (S-346).

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Los cambios del estándar se proponen y el usuario los aprueba en «Estándar» → «Propuestas» (análisis 1 del pendiente 132, acuerdo 3) |
| RN-02 | La regla que se edita vuelve a pasar su checklist, con la versión y la fecha nuevas (`20·M10`) |
| RN-03 | «Validable» tiene tres valores: no; sí, falta el programa; sí, con su programa |

### 3.2 Supuestos

- Las tablas llegan con la HU-001 y las reglas con la HU-002.

### 3.3 Fuera de alcance

- Las demás reglas que nombran `validadores/reglas-validables.md`: su respuesta pasa a la casilla en la HU-002.

---

## 4. Criterios de aceptación

### CA-01 · `20·M5` habla de casillas

**Sale de:** análisis 1 del pendiente 136, punto 12 de «Lo que se tiene que hacer»

```gherkin
Dado el estándar en la base
Cuando se lee 20·M5 con ver_estandar
Entonces dice que cada parte de la regla va en su casilla y que el texto se arma desde ellas
Y su checklist está aplicado con la versión nueva
```

**Cómo validarlo:** correr `manage.py test core.estandar.tests_molde` → resultado esperado: el caso pasa.

### CA-02 · `20·M9` manda a la casilla «validable»

**Sale de:** punto 12 y S-346

```gherkin
Dado el estándar en la base
Cuando se leen 20·M9, el capítulo 20, su checklist y el molde
Entonces ninguno manda a registrar en validadores/reglas-validables.md
Y M9 nombra los tres valores de la casilla
```

**Cómo validarlo:** correr `manage.py test core.estandar.tests_molde` → resultado esperado: el caso pasa.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Trazabilidad** | Cada cambio queda en la historia con su propuesta y su versión |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 136](../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md) |
| Modelo de datos afectado | Ninguno: cambian cinco documentos del estándar |

---

## 7. Tareas técnicas derivadas

- [ ] Redactar los cinco textos y proponerlos.
- [ ] Prueba que lee los textos aprobados.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-027-HU-007-el-molde-habla-de-casillas` |  | (vacío) | [plan_trabajo.md](A-EP-027-HU-007-el-molde-habla-de-casillas/plan_trabajo.md) | [plan_pruebas.md](A-EP-027-HU-007-el-molde-habla-de-casillas/plan_pruebas.md) | [resultado_pruebas.md](A-EP-027-HU-007-el-molde-habla-de-casillas/resultado_pruebas.md) | Terminada |

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
| **V**aliosa | Sí | El molde dice lo que se construye |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Prueba de Django sobre el estándar en la base |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-07 | El agente | Creación de la HU, desde el análisis 1 del pendiente 136 |
