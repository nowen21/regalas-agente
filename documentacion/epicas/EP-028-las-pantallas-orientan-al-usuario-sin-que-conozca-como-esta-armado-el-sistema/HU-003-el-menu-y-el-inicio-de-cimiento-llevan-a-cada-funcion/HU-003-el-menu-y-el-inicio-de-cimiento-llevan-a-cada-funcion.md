# HU-003 · El menú y el inicio de Cimiento llevan a cada función

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-003 |
| **Épica / Feature** | [EP-028 · Las pantallas orientan al usuario sin que conozca cómo está armado el sistema](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/templates/base.html` y `core/inicio/` |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien usa Cimiento
- **Quiero** llegar a cada función desde el menú, y que el inicio me diga lo que espera una decisión
- **Para** no tener que saber dónde está escondida cada pantalla

---

## 3. Contexto y descripción

«Propuestas», «Reportes», «Vista previa», «Subir a git» y «Versiones» solo se alcanzan por enlaces dentro de un párrafo, y el inicio solo dice a qué base está conectado. Sale del [análisis 1 del pendiente 137](../../../../historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/analisis-1.md), punto 5 de «Lo que se tiene que hacer», y se hace con los recursos de Tabler y la guía de diseño de pantallas (`base/17-guia-de-pantallas.md`, en la base), sección 4.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Toda pantalla que no es el detalle de un registro se alcanza desde el menú (`17·I7`) |
| RN-02 | El menú se organiza por lo que se quiere hacer, con submenús, y marca dónde se está (guía §4) |
| RN-03 | El menú y el inicio muestran cuántas propuestas y cuántos reportes esperan una decisión, y llevan a ellos (guía §4) |
| RN-04 | Todo se hace con los componentes de Tabler: `navbar` con `dropdown`, `badge`, `card`, `empty` (acuerdo 3, `17·I5`) |

### 3.2 Supuestos

- Cimiento usa Tabler 1.6.1.

### 3.3 Fuera de alcance

- La pantalla de propuestas en sí (HU-004).

---

## 4. Criterios de aceptación

### CA-01 · Toda pantalla está en el menú

**Sale de:** análisis 1 del pendiente 137, punto 5

```gherkin
Dado una cuenta que entra a Cimiento
Cuando abre cualquier pantalla
Entonces el menú trae, agrupadas por tarea, todas las pantallas que no son el detalle de un registro
Y marca la entrada de la pantalla en que está
```

**Cómo validarlo:** correr `manage.py test core.inicio.tests_menu` → resultado esperado: el caso pasa.

### CA-02 · El inicio muestra lo que espera una decisión

**Sale de:** punto 5

```gherkin
Dado dos propuestas sin aprobar y un reporte abierto
Cuando se abre el inicio
Entonces dice que hay 2 propuestas y 1 reporte esperando, con el enlace a cada pantalla
Y el menú muestra esos mismos números
Y sin nada pendiente, el inicio lo dice
```

**Cómo validarlo:** correr `manage.py test core.inicio.tests_menu` → resultado esperado: el caso pasa.

### CA-03 · Cada entrada del menú lleva su ícono

**Sale de:** corrección del usuario del 2026-10-07 («los íconos en el menú no están»)

```gherkin
Dado una cuenta que entra a Cimiento
Cuando mira el menú
Entonces cada entrada principal lleva su ícono de Tabler Icons, en el lugar que le da la plantilla (nav-link-icon)
Y el ícono es de adorno: el lector de pantalla no lo lee
```

**Cómo validarlo:** correr `manage.py test core.inicio.tests_menu` → resultado esperado: el caso pasa.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | Los contadores salen de dos consultas por página |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Documento funcional | [Análisis 1 del pendiente 137](../../../../historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/analisis-1.md) |
| Guía | `base/17-guia-de-pantallas.md`, §4 y §7: se lee con `manage.py ver_estandar` |

---

## 7. Tareas técnicas derivadas

- [ ] Menú con submenús y contadores.
- [ ] Inicio con lo pendiente.
- [ ] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-028-HU-003-menu-e-inicio` |  | (vacío) | [plan_trabajo.md](A-EP-028-HU-003-menu-e-inicio/plan_trabajo.md) | [plan_pruebas.md](A-EP-028-HU-003-menu-e-inicio/plan_pruebas.md) | [resultado_pruebas.md](A-EP-028-HU-003-menu-e-inicio/resultado_pruebas.md) | Terminada |
| `B-EP-028-HU-003-iconos-del-menu` | CA-03 | (vacío) | [plan_trabajo.md](B-EP-028-HU-003-iconos-del-menu/plan_trabajo.md) | [plan_pruebas.md](B-EP-028-HU-003-iconos-del-menu/plan_pruebas.md) | [resultado_pruebas.md](B-EP-028-HU-003-iconos-del-menu/resultado_pruebas.md) | Terminada |

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
| **V**aliosa | Sí | Ninguna pantalla queda escondida |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | |
| **T**esteable | Sí | Pruebas de Django |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-07 | El agente | Creación de la HU, desde el análisis 1 del pendiente 137 |
