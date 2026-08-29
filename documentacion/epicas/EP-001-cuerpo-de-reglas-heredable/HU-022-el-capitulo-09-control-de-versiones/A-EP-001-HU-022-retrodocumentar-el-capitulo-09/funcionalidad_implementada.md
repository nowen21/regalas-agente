# Funcionalidad implementada — Fase `A-EP-001-HU-022-retrodocumentar-el-capitulo-09` (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-001-HU-022-retrodocumentar-el-capitulo-09` |
| **Módulo** | Cuerpo de reglas |
| **Especificación del módulo** | La redacción de los CA de la [HU-022](../HU-022-el-capitulo-09-control-de-versiones.md) es la especificación funcional (`02·F19`) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | HU-022 (CA-01, CA-02) |
| **Fecha de cierre** | 2026-08-28 |
| **Versión del estándar al cerrar** | `35.9.0` |
| **Commit** | Se completa al commitear |

---

## 1. Qué se implementó — resumen

**Nada: se comprobó.** Es retro-documentación (`13·DOC6`). El capítulo `09` ya nombraba su historia dueña en la cabecera; lo que faltaba era **dejarlo verificado y darle a la historia una fase donde bajen sus cambios**.

Con esto, el capítulo `09` y sus **11 reglas** dejan de ser texto sin dueño declarado: tienen historia, y la historia tiene por dónde recibir un cambio.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem del especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 — el capítulo nombra su historia dueña | doc | `base/09-git.md`, su cabecera | ✅ | El enlace **resuelve** |
| CA-02 — un cambio tiene dónde bajarse | doc | `HU-022-el-capitulo-09-control-de-versiones.md` §8 | ✅ | `validar.py fases` deja de reclamar |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-00 | Medir el `CA-01` en las 21 | ✅ hecha | `t00-las-22-historias-de-capitulo.py` | **21 de 21** |
| T-01 | La cabecera nombra y el enlace resuelve | ✅ hecha | `base/09-git.md` | `CP-001` |
| T-02 | La historia recibe la fila | ✅ hecha | `HU-022-el-capitulo-09-control-de-versiones.md` | `CP-002` |
| T-03 | El resultado de pruebas | ✅ hecha | [resultado_pruebas.md](resultado_pruebas.md) | — |
| T-04 | El cierre y la fila | ✅ hecha | este documento | — |

**Correspondencia con el plan:** 5 tareas en el plan, 5 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba:** ninguno. **Cero archivos de `base/`**, que era el límite.

**Esfuerzo real contra estimado:** el plan estimaba 1,5 h. El real fue menor: **las cifras las midió un programa capítulo por capítulo**, y escribirlas a mano era lo que costaba.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple** |

- **Suites ejecutadas + resultado:** `validar.py enlaces` **sin enlaces rotos**, y `validar.py fases`, que deja de contar esta historia como «sin fases». No se corre la suite de código: esta fase no toca código.
- **Verificaciones manuales** (`08·T4`):
  - **Ningún archivo de `base/` cambió.**
  - El capítulo tiene **11 regla(s)** donde el analizador las ve.
- **Defectos abiertos que se aceptaron:** Ninguno

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

- **Punto de entrada:** la cabecera del capítulo `09`. Quien vaya a cambiarlo lee ahí por dónde baja el cambio.
- **Permisos o datos base sembrados:** ninguno.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal |
|---|---|---|
| **Las cifras de este documento las midió un programa** | Se descartó copiarlas de la fase del capítulo `02`: copiar ciento cinco documentos es la forma más segura de que uno diga algo falso sin que nadie lo note | `S-081` |
| **El molde se aprobó una vez, no veintiuna** | Veintiuna aprobaciones de un documento idéntico vuelven la puerta un trámite, y una puerta que es trámite deja de mirar | `S-081` |
| **No se tocó `base/`** | Cambiar el capítulo para acomodar la fase es al revés | — |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| Ninguna | — | — |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] Mapa de dependencias: no aplica; la fase no tocó código.
- [x] Catálogo de módulos: no se creó módulo.
- [x] Índice `README.md` de la carpeta de la historia.
- [x] Especificación del módulo: los CA de la HU, que no cambiaron al comprobar.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**No aplica.** El capítulo ya viaja a los proyectos con `base/`; esta fase no cambió su texto.
