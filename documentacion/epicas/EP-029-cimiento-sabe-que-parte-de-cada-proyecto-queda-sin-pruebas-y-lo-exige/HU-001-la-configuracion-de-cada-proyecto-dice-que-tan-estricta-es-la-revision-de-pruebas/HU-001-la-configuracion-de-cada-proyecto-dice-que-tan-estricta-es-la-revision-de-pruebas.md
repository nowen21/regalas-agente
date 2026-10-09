# HU-001 · La configuración de cada proyecto dice qué tan estricta es la revisión de pruebas y cada cuántos días toca

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-001 |
| **Épica / Feature** | [EP-029 · Cimiento sabe qué parte de cada proyecto queda sin pruebas y lo exige desde su configuración](../epica.md) |
| **Módulo / Componente** | `core/proyectos/ajustes.py`, su ayuda, y la app nueva `core/pruebas/` |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | En curso |

---

## 2. Narrativa

- **Como** quien administra los proyectos desde Cimiento
- **Quiero** elegir en la página de cada proyecto qué tan estricto ser con la revisión de pruebas y cada cuántos días hacerla
- **Para** que Cimiento sepa qué exigirle a cada uno y guarde cómo le fue en cada revisión

---

## 3. Contexto y descripción

La configuración de cada proyecto no exige revisar las pruebas ni guarda el estado de esa revisión. Sale del [análisis 1 del pendiente 141](../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-1.md), puntos 2, 3 y 11 de «Lo que se tiene que hacer».

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Los dos ajustes van en las tres capas que ya existen: fábrica, valor común y valor del proyecto (acuerdo 9) |
| RN-02 | Qué tan estricto ser tiene tres opciones: solo avisar, no dejar guardar los cambios, o nada. De fábrica, solo avisar (acuerdo 11) |
| RN-03 | Cada cuántos días revisar va desde 1. De fábrica, 7 (acuerdo 11) |
| RN-04 | La base guarda, por proyecto, si tiene la parte que revisa, y de cada revisión: la fecha, la herramienta, el resultado archivo por archivo y el de las pruebas de navegador (punto 3) |
| RN-05 | Las opciones y su ayuda se entienden sin saber del tema (acuerdo 8, `00·ID7`) |

### 3.2 Supuestos

- La página del proyecto y la de «Configuración» muestran todo ajuste del catálogo sin cambiar sus plantillas.

### 3.3 Fuera de alcance

- Correr la revisión (HU-002) y avisar (HU-003).

---

## 4. Criterios de aceptación

### CA-01 · Los dos ajustes existen en las tres capas

**Sale de:** análisis 1 del pendiente 141, puntos 2 y 11

```gherkin
Dado un proyecto sin valores propios
Cuando se leen sus ajustes
Entonces «qué tan estricta es la revisión» vale «solo avisar» y «cada cuántos días» vale 7
Y si el proyecto guarda «no dejar guardar» y 3, valen esos solo para él
Y un valor que no está entre las opciones o menor que 1 se rechaza
```

**Cómo validarlo:** correr `manage.py test core.pruebas` → resultado esperado: los casos pasan.

### CA-02 · Los dos ajustes salen en la página del proyecto con su ayuda

**Sale de:** puntos 2 y 11

```gherkin
Dado el formulario de un proyecto y el de «Configuración»
Cuando se abren
Entonces cada uno trae los dos ajustes
Y cada ajuste tiene su «?» con un texto que no usa términos técnicos
```

**Cómo validarlo:** correr `manage.py test core.pruebas core.ayuda` → resultado esperado: los casos pasan.

### CA-03 · La base guarda el estado de la revisión de cada proyecto

**Sale de:** punto 3

```gherkin
Dado un proyecto registrado
Cuando se guarda una revisión con su fecha, su herramienta, sus archivos y el resultado del navegador
Entonces la última revisión del proyecto es esa
Y el proyecto dice si tiene la parte que revisa
Y si nunca se revisó, la última revisión es ninguna
```

**Cómo validarlo:** correr `manage.py test core.pruebas` → resultado esperado: los casos pasan.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Usabilidad** | Ayuda sin términos técnicos (`00·ID7`) |
| RNF-02 | **Compatibilidad** | Tablas nuevas, aditivas: nada de lo que existe cambia |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 141](../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-1.md) |
| Modelo de datos afectado | Dos claves nuevas de ajustes; tablas nuevas de `core/pruebas/` |

---

## 7. Tareas técnicas derivadas

- [x] Los dos ajustes y su ayuda.
- [x] La app `core/pruebas/` con el estado y las revisiones.
- [x] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-029-HU-001-ajustes-y-estado-de-la-revision` | CA-01, CA-02, CA-03 | (vacío) | [plan_trabajo.md](A-EP-029-HU-001-ajustes-y-estado-de-la-revision/plan_trabajo.md) | [plan_pruebas.md](A-EP-029-HU-001-ajustes-y-estado-de-la-revision/plan_pruebas.md) | [resultado_pruebas.md](A-EP-029-HU-001-ajustes-y-estado-de-la-revision/resultado_pruebas.md) | Cumple; falta el commit |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Ninguna | | |

---

## 10. Precondiciones  (Definition of Ready - DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas y desbloqueadas
- [x] Cumple criterios INVEST

## 11. Poscondiciones (Definition of Done - DoD)

- [x] Todos los criterios de aceptación verificados
- [x] Documentación actualizada

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | |
| **N**egociable | Sí | |
| **V**aliosa | Sí | Cimiento sabe qué exigirle a cada proyecto |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Pruebas de Django |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-08 | El agente | Creación de la HU, desde el análisis 1 del pendiente 141 |
