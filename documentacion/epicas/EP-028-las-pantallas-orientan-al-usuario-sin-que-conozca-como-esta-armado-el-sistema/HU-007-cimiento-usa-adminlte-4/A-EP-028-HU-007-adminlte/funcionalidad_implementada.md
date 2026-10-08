# Funcionalidad implementada · Fase `A-EP-028-HU-007-adminlte` (módulo Las pantallas de Cimiento: `templates/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-028-HU-007-adminlte` |
| **Módulo** | Las pantallas de Cimiento |
| **Especificación del módulo** | Los CA de la [HU-007](../HU-007-cimiento-usa-adminlte-4.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-007 (CA-01, CA-02, CA-03) |
| **Fecha de cierre** | 2026-10-07 |
| **Versión del estándar al cerrar** | 58.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Cimiento usa AdminLTE 4.10.0, sobre Bootstrap 5.3.8, con Bootstrap Icons. Tabler salió: ni su CSS, ni su JS, ni sus clases.

- La página base tiene la estructura de AdminLTE: un encabezado con la ayuda, la cuenta y el botón para plegar el menú; un menú lateral oscuro con sus submenús desplegables; y el contenido.
- En el menú, cada entrada y cada ítem de submenú llevan su ícono. El menú marca dónde se está y muestra en rojo lo que espera una decisión.
- La entrada y la página de Cimiento sin base son las páginas sueltas de AdminLTE.
- Las clases propias de Tabler se cambiaron por las de Bootstrap y AdminLTE en 28 plantillas y en el HTML que arma el estándar. List.js, que venía dentro de Tabler, se instaló aparte.
- La guía pasa a decir que Cimiento usa AdminLTE 4 con la propuesta 15, que aprueba el usuario.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 · Las pantallas usan AdminLTE | CA | `templates/base.html`, `core/cuentas/templates/cuentas/entrar.html`, `core/inicio/templates/inicio/base_apagada.html`, `config/settings/base.py`, `package.json` | Hecho | CP-001 |
| CA-02 · El menú y sus submenús llevan íconos | CA | `templates/base.html` | Hecho | CP-002 |
| CA-03 · Ninguna clase de Tabler queda | CA | Las 28 plantillas, `core/estandar/presentar.py`, `static/cimiento.css`, `static/estandar.css`, `core/ayuda/static/ayuda/ayuda.css` | Hecho | CP-003 |
| RNF-01 · Versiones fijas | RNF | `package.json` | Hecho | CP-001 |

**Faltantes / diferimientos:** la propuesta 15 de la guía, hasta que el usuario la apruebe.

### 2.2 Plan de trabajo → ejecución

Las 5 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno. `npm install admin-lte` lo corrió el agente por orden del usuario antes de abrir la fase; `package.json` y `package-lock.json` quedaron declarados en este plan.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Basta con recargar Cimiento. Un ícono nuevo del menú se pone con `<i class="nav-icon bi bi-…" aria-hidden="true"></i>`, con el nombre de Bootstrap Icons.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Cada clase de Tabler se cambió por la de Bootstrap o AdminLTE | La plantilla instalada se usa a fondo (`17·I5`); se descartó una hoja que imitara a Tabler | Ninguna |
| List.js se instaló aparte | Venía dentro de Tabler, que sale entero | Ninguna |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

`npm install` en `proyectos/cimiento/` y recargar.
