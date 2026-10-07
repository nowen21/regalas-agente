# HU-006 · Las tablas de Cimiento usan los recursos de tablas de la plantilla

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-006 |
| **Épica / Feature** | [EP-028 · Las pantallas orientan al usuario sin que conozca cómo está armado el sistema](../epica.md) |
| **Módulo / Componente** | Las plantillas con tablas de Cimiento, `static/tablas.js` y `templates/includes/tabla_pie.html` |
| **Tipo** | Funcional |
| **Prioridad** | Should |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien busca algo en una lista de Cimiento
- **Quiero** ordenar por cualquier columna, filtrar y escoger cuántas filas ver
- **Para** encontrar lo que necesito sin recorrer la lista entera

---

## 3. Contexto y descripción

Ninguna tabla de Cimiento se ordena, se filtra ni se pagina; Tabler, ya instalado, trae el patrón de tabla con List.js. Sale del [análisis 1 del pendiente 137](../../../../historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/analisis-1.md), punto 9, y se hace con la guía de diseño de pantallas (`base/17-guia-de-pantallas.md`, §6 y §12).

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Las listas de registros se ordenan pulsando el título de la columna, se filtran debajo y se paginan escogiendo cuántas filas ver (guía §6) |
| RN-02 | Se usa el patrón de tabla de Tabler con List.js, que ya está instalado; el código va una sola vez, en `static/tablas.js`, y el pie en una plantilla parcial (guía §12, `17·I5`) |
| RN-03 | Las tablas que la base ya pagina (historia y versiones) conservan su paginación y ganan orden y filtro en la página |
| RN-04 | Quedan fuera las tablas que no son listas de registros: el manual, los recuadros del gasto (se recargan solos) y las reglas de un proyecto (son un formulario) |

### 3.2 Supuestos

- Tabler 1.6.1 trae `libs/list.js`.

### 3.3 Fuera de alcance

- Quitar columnas: lo decide la EP-027·HU-005 para las rutas.

---

## 4. Criterios de aceptación

### CA-01 · Las listas se ordenan, se filtran y se paginan

**Sale de:** análisis 1 del pendiente 137, punto 9

```gherkin
Dado una lista de registros de Cimiento
Cuando se abre
Entonces cada columna tiene su botón para ordenar y su filtro debajo
Y el pie deja escoger 10, 20, 50 o 100 filas por página
```

**Cómo validarlo:** correr `manage.py test core.inicio.tests_tablas` → resultado esperado: el caso pasa.

### CA-02 · Un solo código y un solo pie

**Sale de:** guía §12

```gherkin
Dado las tablas avanzadas
Cuando se revisa su código
Entonces todas usan data-tabla-avanzada, el pie común y static/tablas.js
Y la página carga List.js de Tabler
```

**Cómo validarlo:** correr `manage.py test core.inicio.tests_tablas` → resultado esperado: el caso pasa.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Dependencias** | Ninguna nueva: List.js viene con Tabler |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 137](../../../../historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/analisis-1.md) |
| Guía | `base/17-guia-de-pantallas.md`, §6 y §12 |
| Modelo de datos afectado | Ninguno |

---

## 7. Tareas técnicas derivadas

- [ ] `static/tablas.js` y el pie común.
- [ ] Las listas de registros.
- [ ] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-028-HU-006-tablas-avanzadas` |  | (vacío) | [plan_trabajo.md](A-EP-028-HU-006-tablas-avanzadas/plan_trabajo.md) | [plan_pruebas.md](A-EP-028-HU-006-tablas-avanzadas/plan_pruebas.md) | [resultado_pruebas.md](A-EP-028-HU-006-tablas-avanzadas/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-002 | Terminada |

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
| **V**aliosa | Sí | Se encuentra lo que se busca |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Pruebas de Django |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-07 | El agente | Creación de la HU, desde el análisis 1 del pendiente 137 |
