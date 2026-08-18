# Funcionalidad implementada — Fase «A-EP-007-HU-001-rellenar-los-marcadores-al-copiar»   ·   `[CAPA 3]`

Consolida qué se implementó, la trazabilidad, qué se probó y qué quedó. Se escribe en la estación de cierre, **antes del commit** de la fase.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-007-HU-001-rellenar-los-marcadores-al-copiar` |
| **Módulo** | Instalación (`validadores/instalar.py`) |
| **Especificación del módulo** | No existe. Queda como deuda en §6 — la fase no la escribió, y está declarado desde el plan |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md) |
| **HU / CA cubiertas** | HU-001 ([CA-01](../HU-001-instalar-con-una-linea.md#ca-01--una-línea-deja-el-proyecto-listo), [CA-02](../HU-001-instalar-con-una-linea.md#ca-02--correrla-dos-veces-no-rompe-nada)) |
| **Fecha de cierre** | 2026-08-16 |
| **Commit** | pendiente — lo autoriza el usuario aparte |

---

## 1. Qué se implementó — resumen

Un proyecto recién instalado ya no recibe documentos con huecos donde debía ir la ruta del estándar. Antes, tres de los cuatro sitios donde el instalador copia escribían la plantilla tal cual, así que la cita a una regla llegaba muerta y quien hacía clic no llegaba a ninguna parte.

Además queda la primera prueba automática del repositorio: instala en una carpeta desechable y comprueba que ningún archivo copiado conserve un marcador que el instalador sabía llenar. Corre sola y no necesita instalar nada.

---

## 2. Trazabilidad

### 2.1 Especificación → implementación

El módulo de instalación **no tiene especificación**, así que no hay afirmaciones contra las cuales trazar. En su lugar se traza contra los criterios de aceptación de la HU, que es lo que hay escrito:

| Exigencia | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «el proyecto queda con todo lo que debe tener» — y lo que quedó, sirve | instalación | [`validadores/instalar.py`](../../../../../validadores/instalar.py) · `instalar_stack`, `instalar_recuerdos`, `instalar_agente_config` | ✅ | CP-001 y CP-002 del [`resultado_pruebas.md`](resultado_pruebas.md) |
| «correrla dos veces no rompe nada» | instalación | las mismas tres funciones | ✅ | CP-003 |
| «funciona en rutas con espacios y tildes» | instalación | ídem | ✅ | CP-004 |
| Que exista una prueba que lo compruebe sola | prueba | [`validadores/tests/test_instalar_marcadores.py`](../../../../../validadores/tests/test_instalar_marcadores.py) | ✅ | `Ran 6 tests · OK`, y se comprobó que se pone roja con el defecto puesto |

**Faltantes / diferimientos:** que el módulo no tenga especificación es el faltante, y es anterior a esta fase. Va a §6.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | `instalar_stack` pasa por `_rellenar` | ✅ hecha | `validadores/instalar.py` | CP-001 |
| T-02 | Ídem `instalar_recuerdos` | ✅ hecha | `validadores/instalar.py` | CP-001 |
| T-03 | Ídem `instalar_agente_config` | ✅ hecha | `validadores/instalar.py` | CP-001 |
| T-04 | La prueba que faltó | ✅ hecha | `validadores/tests/test_instalar_marcadores.py` | `Ran 6 tests · OK` |
| T-05 | Documentar qué rellena cada función | ✅ hecha | `validadores/docs/instalar.md` | El documento |
| T-06 | Segunda corrida en la prueba | ✅ hecha | Dentro del CP-003 | CP-003 |
| T-07 | `CHANGELOG` y `VERSION` | ✅ hecha | [`CHANGELOG.md`](../../../../../CHANGELOG.md) 21.1.0 | La entrada |

**Correspondencia con el plan:** 7 tareas en el plan, 7 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba:**

| Archivo | Por qué hubo que tocarlo | Quién autorizó |
|---|---|---|
| Ninguno | — | — |

Los cinco archivos del plan §2.1 son exactamente los cinco que se tocaron.

**Esfuerzo real contra estimado:** el plan estimó 5,5 h. El trabajo se hizo en una sesión, con una pausa de por medio para corregir el criterio. Lo que se subestimó no fue el código —tres líneas— sino **acordar qué había que comprobar**: escribir el criterio de la prueba costó más que el arreglo.

---

## 3. Qué se probó

- **Fuente:** [`resultado_pruebas.md`](resultado_pruebas.md) · **Veredicto:** **Cumple**.
- **Suites corridas + resultado:** `validadores/tests/` — 6 de 6 verdes. Alcance quirúrgico: no se corrió nada más.
- **Verificaciones manuales:**
  - El enlace del `.agente/stack-instalacion.md` instalado abre la regla `F13`. **Es el enlace que un proyecto reportó roto.**
  - Los 19 enlaces `.md` del proyecto instalado resuelven: 0 rotos.
  - Con el defecto reintroducido a propósito, la prueba se pone roja y nombra cada marcador. Sin esto, «aprobado» no distinguiría entre que el arreglo funciona y que la prueba no mira nada.
- **Defectos abiertos que se aceptaron:** ninguno.

---

## 4. Cómo se usa / puntos de entrada

- **Punto de entrada:** la misma línea de instalación de siempre. No cambia cómo se corre, cambia lo que deja escrito.
- **La prueba:** `python -m unittest discover -s validadores/tests`.
- **Permisos o datos base sembrados:** ninguno.

---

## 5. Decisiones no obvias

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Rellenar en cada una de las tres funciones | Se descartó un envoltorio único de escritura: es mejor diseño, pero es un refactor más grande y esta fase arreglaba un `P0` | Va a §6 como deuda |
| La prueba comprueba los marcadores de `_rellenos()`, no la marca `«` | Un `.md` copiado trae dos clases de hueco: el que llena el instalador y el que llena el proyecto. Comprobar los dos da rojo en 65 líneas que están bien | En `validadores/docs/instalar.md` y en el `resultado_pruebas` §2 |
| `unittest` de la biblioteca estándar | No hay pytest instalado ni pruebas en el repositorio. La épica pide correr sin internet y sin instalar nada antes | En el `resultado_pruebas` §0 |
| Probar la instalación entera y no función por función | El defecto no estaba en ninguna función suelta, sino en que **una de cuatro** rellenaba. Probar cada una por separado no lo habría atrapado | En el `plan_pruebas` §3.1 |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| El módulo de instalación no tiene especificación | Diferido por el plan | Pendiente por abrir |
| Un proyecto instalado antes de este cambio no se arregla reinstalando. Son dos motivos: los 4 archivos de `.agente/` no se pisan, y el `stack-instalacion.md` sí se pisaría pero la huella sale del stack central, así que el instalador lo da por al día y no reescribe | Atajo decidido el primero (riesgo `B-01` del plan, aprobado por el usuario) · **No previsto** el segundo | El segundo lo comprobó `shopnest-mesa` el mismo día y quedó como [pendiente 42](../../../../../pendientes/hecho/el-arreglo-del-40-no-llegaba-a-lo-ya-instalado.md) |
| Los cuatro puntos de copia repiten el mismo paso en vez de pasar por un envoltorio único | Atajo decidido — lo decidió el usuario al aprobar el plan §2.6 | Pendiente por abrir |
| `enlaces.py` no tiene bloque `__main__`: correrlo directo no imprime nada y sale con código 0 | No previsto — se descubrió en esta sesión, fuera de esta fase | Anotado en el [pendiente 41](../../../../../pendientes/hecho/el-marcador-se-resuelve-contra-el-estandar.md) |
| Falta avisarle a `shopnest-mesa` que su reporte cerró | Diferido por el plan | Depende del [pendiente 36](../../../../../pendientes/36-falta-la-regla-que-obliga-a-reportar-lo-que-es-del-estandar.md) |

---

## 7. Lo que esta fase deja como lección

**La fase existe porque otra no existió.** El mismo arreglo se había hecho el día anterior sin fase, sin plan de pruebas y sin caso que ejecutar; el defecto salió del proyecto que lo sufrió. Con fase, el caso que lo destapaba estaba escrito antes de tocar el código.

**Y el plan aprobado también se equivocó.** El criterio de la prueba mezclaba dos cosas y salió rojo en 65 líneas correctas. Lo que evitó el daño no fue acertar, sino que la ejecución se detuviera a reportarlo en vez de ajustar el criterio en silencio para que pasara.
