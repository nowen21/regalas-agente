# Funcionalidad implementada — Fase «A-EP-004-HU-005-el-marcador-se-resuelve-contra-el-estandar»   ·   `[CAPA 3]`

Consolida qué se implementó, la trazabilidad, qué se probó y qué quedó. Se escribe en la estación de cierre, **antes del commit** de la fase.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-005-el-marcador-se-resuelve-contra-el-estandar` |
| **Módulo** | Comprobación (`validadores/enlaces.py`) |
| **Especificación del módulo** | No existe. Queda como deuda en §6 — declarado desde el plan |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md) |
| **HU / CA cubiertas** | HU-005 ([CA-01](../HU-005-enlaces-y-citas.md#ca-01--un-enlace-roto-se-reporta)) |
| **Fecha de cierre** | 2026-08-16 |
| **Commit** | pendiente — lo autoriza el usuario aparte |

---

## 1. Qué se implementó — resumen

El revisor de enlaces ya da el mismo veredicto se lo corra desde donde se lo corra. Antes, dentro de un proyecto, una cita a una regla escrita con el marcador salía siempre rota —aunque estuviera bien puesta—, porque el programa la buscaba dentro del proyecto en vez de dentro del estándar.

Es la red de seguridad de la [21.1.0](../../../../../CHANGELOG.md): aquella hizo que los marcadores dejaran de salir sin llenar; esta hace que, si mañana se escapa uno, el veredicto siga siendo el correcto.

---

## 2. Trazabilidad

### 2.1 Especificación → implementación

El módulo de comprobación **no tiene especificación**, así que se traza contra el criterio de aceptación de la HU, que es lo que hay escrito:

| Exigencia | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| «un enlace roto se reporta» — y uno bueno no, mire quien mire | comprobación | [`validadores/enlaces.py`](../../../../../validadores/enlaces.py) · `ESTANDAR` y la rama del marcador en `validar_enlaces` | ✅ | CP-001, CP-002 y CP-003 del [`resultado_pruebas.md`](resultado_pruebas.md) |
| Que el veredicto no cambie sobre el propio estándar | no regresión | la misma | ✅ | Salida de `validar.py estandar` idéntica antes y después |
| Que exista una prueba que lo fije | prueba | [`validadores/tests/test_enlaces_marcador.py`](../../../../../validadores/tests/test_enlaces_marcador.py) | ✅ | `Ran 12 tests · OK`, y se comprobó que se pone roja con el defecto puesto |

**Faltantes / diferimientos:** que el módulo no tenga especificación es anterior a esta fase. Va a §6.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | Guardar la salida de `validar.py estandar` antes del cambio | ✅ hecha | Archivo de trabajo temporal | `0 falla(s), 5 aviso(s)` · 8 líneas |
| T-02 | Resolver el marcador contra la carpeta del estándar | ✅ hecha | `validadores/enlaces.py` | CP-003 |
| T-03 | Prueba de las dos raíces | ✅ hecha | `validadores/tests/test_enlaces_marcador.py` | CP-003 |
| T-04 | Prueba del marcador que no resuelve | ✅ hecha | El mismo archivo | CP-002 |
| T-05 | Comparar la salida contra la de T-01 | ✅ hecha | — | **Idénticas** |
| T-06 | Actualizar `validadores/docs/enlaces.md` | ✅ hecha | `validadores/docs/enlaces.md` | El documento |
| T-07 | `CHANGELOG` y `VERSION` | ✅ hecha | [`CHANGELOG.md`](../../../../../CHANGELOG.md) 21.1.1 | La entrada |

**Correspondencia con el plan:** 7 tareas en el plan, 7 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba:**

| Archivo | Por qué hubo que tocarlo | Quién autorizó |
|---|---|---|
| Ninguno | — | — |

**Esfuerzo real contra estimado:** el plan estimó 3,75 h. El cambio de código fue una línea; lo que costó fue montar la prueba de las dos raíces sin que se apoyara en el programa que estaba probando.

---

## 3. Qué se probó

- **Fuente:** [`resultado_pruebas.md`](resultado_pruebas.md) · **Veredicto:** **Cumple**.
- **Suites corridas + resultado:** `validadores/tests/` — 12 de 12 verdes (6 de esta fase, 6 de la hermana). Alcance quirúrgico.
- **Verificaciones manuales:**
  - La salida de `validar.py estandar` es **idéntica** antes y después del cambio. Es lo que respalda el «acá no cambió nada».
  - Con la versión vieja cargada en memoria, el CP-003 se pone rojo.
- **Defectos abiertos que se aceptaron:** ninguno.

---

## 4. Cómo se usa / puntos de entrada

- **Punto de entrada:** `python validadores/validar.py estandar`, y los enganches que ya lo llamaban. No cambia cómo se corre.
- **La prueba:** `python -m unittest discover -s validadores/tests`.
- **Permisos o datos base sembrados:** ninguno.

---

## 5. Decisiones no obvias

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La carpeta del estándar se deduce del propio archivo | Se descartó pedirla por parámetro: el módulo ya sabe dónde vive, y pedir el dato por fuera agrega una forma más de equivocarse | En el comentario de `ESTANDAR`, en el código |
| Se conserva la rama del marcador aunque ya no lleguen marcadores | Es la red para el que se escape mañana. Quitarla dejaría el arreglo dependiendo de que la fase hermana nunca falle | Plan §2.6 |
| El CP-003 compara dos carpetas que **ninguna** es el estándar | Si una lo fuera, coincidirían por casualidad y el caso pasaría sin probar nada | `resultado_pruebas` §2 |
| El resultado esperado se toma del disco, no del programa | Preguntarle al programa que se está probando si acertó no prueba nada | `plan_pruebas` §3.3 |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| El módulo de comprobación no tiene especificación | Diferido por el plan | Pendiente por abrir |
| `enlaces.py` no tiene bloque `__main__`: correrlo directo no imprime nada y sale con código 0, que se lee como «sin hallazgos» | No previsto — apareció en esta sesión y **ya causó daño**: se dio por buena una comprobación que nadie había calculado | Anotado en el [pendiente 41](../../../../../pendientes/hecho/el-marcador-se-resuelve-contra-el-estandar.md); es de la [HU-008](../../HU-008-corrida-completa/), no de esta |
| El [punto 1 del pendiente 33](../../../../../pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md) —enlaces con espacios dados por rotos— no se reprodujo en el CP-004 | Cambio del entorno | Sigue abierto en el 33; acá solo consta que no apareció |

---

## 7. Lo que esta fase deja como lección

**Un revisor que se equivoca en los dos sentidos es peor que no tenerlo.** Marcaba como roto lo bueno, y donde eso pasa el aviso se deja de leer — ya había costado media sesión de fallas invisibles en un proyecto. Por eso el CP-002 existe: comprobar que el arreglo no se logró callando.

**Y el orden importó.** Esta fase iba después de la que quitó la causa, no antes. Al revés, se habría tapado el síntoma y la causa habría seguido mandando marcadores crudos a cada proyecto que se instalara.
