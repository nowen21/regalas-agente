# HU-007 · Cimiento usa AdminLTE 4

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-007 |
| **Épica / Feature** | [EP-028 · Las pantallas orientan al usuario sin que conozca cómo está armado el sistema](../epica.md) |
| **Módulo / Componente** | Las pantallas de Cimiento: `templates/`, las plantillas de cada app, `static/` y la configuración de estáticos |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | L |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | El agente |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** quien usa Cimiento
- **Quiero** que sus pantallas usen la plantilla AdminLTE 4
- **Para** tener sus recursos, entre ellos un menú lateral con íconos en cada entrada

---

## 3. Contexto y descripción

El 2026-10-07 el usuario pidió los íconos del menú dos veces, después instaló AdminLTE 4 con npm y decidió que reemplaza a Tabler («Hágalo si la reemplaza»). La decisión cambia, para Cimiento, el acuerdo 3 del [análisis 1 del pendiente 137](../../../../historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/analisis-1.md), que decía que Cimiento usa Tabler. Lo demás de ese acuerdo sigue: cada proyecto usa a fondo la plantilla que tiene instalada, y la guía de diseño de pantallas no se ata a ninguna.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Todas las pantallas de Cimiento usan AdminLTE 4: su estructura (`app-wrapper`, `app-header`, `app-sidebar`, `app-main`), sus componentes y los de Bootstrap 5, que es su base |
| RN-02 | Los íconos son Bootstrap Icons, los que usa AdminLTE; cada entrada del menú y de sus submenús lleva el suyo |
| RN-03 | Tabler sale de Cimiento: ni su CSS, ni su JS, ni sus clases propias |
| RN-04 | Lo que Tabler traía y AdminLTE no (List.js para las tablas) se instala aparte, con npm |
| RN-05 | Lo que la pantalla mostraba no cambia: solo cambia la plantilla |
| RN-06 | La guía de diseño de pantallas dice que la plantilla de Cimiento es AdminLTE 4, por propuesta |

### 3.2 Supuestos

- AdminLTE 4.10.0 está instalado en `node_modules/admin-lte/`.

### 3.3 Fuera de alcance

- Cambiar lo que hace cada pantalla.

---

## 4. Criterios de aceptación

### CA-01 · Las pantallas usan AdminLTE

**Sale de:** decisión del usuario del 2026-10-07

```gherkin
Dado una cuenta que entra a Cimiento
Cuando abre cualquier pantalla
Entonces la página carga AdminLTE y Bootstrap, y no carga Tabler
Y su estructura es la de AdminLTE: encabezado, menú lateral y contenido
```

**Cómo validarlo:** correr `manage.py test core.inicio.tests_adminlte` → resultado esperado: los casos pasan.

### CA-02 · El menú y sus submenús llevan íconos

**Sale de:** corrección del usuario del 2026-10-07 («los items de los menús no tiene íconos»)

```gherkin
Dado una cuenta que entra a Cimiento
Cuando mira el menú lateral
Entonces cada entrada y cada ítem de sus submenús lleva su ícono de Bootstrap Icons
```

**Cómo validarlo:** correr `manage.py test core.inicio.tests_adminlte` → resultado esperado: el caso pasa.

### CA-03 · Ninguna clase de Tabler queda

**Sale de:** RN-03

```gherkin
Dado las plantillas y el código que arma HTML en Cimiento
Cuando se buscan las clases propias de Tabler
Entonces no queda ninguna
```

**Cómo validarlo:** correr `manage.py test core.inicio.tests_adminlte` → resultado esperado: el caso pasa.

### Criterios de aceptación transversales

- [ ] No regresión: las suites de todas las apps con pantallas quedan verdes.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Dependencias** | AdminLTE 4.10.0, Bootstrap 5.3, Bootstrap Icons y List.js, con versión fija en `package.json` |

---

## 6. Diseño y referencias

| Qué | Dónde |
|---|---|
| Plantilla | AdminLTE 4 (adminlte.io/themes/v4) |
| Guía | `base/17-guia-de-pantallas.md` |
| Modelo de datos afectado | Ninguno |

---

## 7. Tareas técnicas derivadas

- [ ] Dependencias y estáticos.
- [ ] La plantilla base, la de entrada y la de Cimiento apagado.
- [ ] Las clases de Tabler en las plantillas y en el código.
- [ ] Pruebas y la propuesta de la guía.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-028-HU-007-adminlte` | CA-01, CA-02, CA-03 | (vacío) | [plan_trabajo.md](A-EP-028-HU-007-adminlte/plan_trabajo.md) | [plan_pruebas.md](A-EP-028-HU-007-adminlte/plan_pruebas.md) | [resultado_pruebas.md](A-EP-028-HU-007-adminlte/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Una pantalla queda con una clase de Tabler y se ve rota | CA-03 lo busca en todas |

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
| **V**aliosa | Sí | La plantilla que eligió el usuario |
| **E**stimable | Sí | |
| **S**mall (pequeña) | Sí | Una fase |
| **T**esteable | Sí | Pruebas de Django |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-07 | El agente | Creación de la HU, desde la decisión del usuario del 2026-10-07 |
