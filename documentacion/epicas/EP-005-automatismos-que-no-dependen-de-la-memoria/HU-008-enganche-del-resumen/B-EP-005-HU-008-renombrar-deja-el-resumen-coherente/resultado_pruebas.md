# Resultado de Pruebas — Fase «B-EP-005-HU-008-renombrar-deja-el-resumen-coherente»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [`plan_pruebas.md`](plan_pruebas.md), que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-005-HU-008-renombrar-deja-el-resumen-coherente` |
| **HU** | [HU-008 — Enganche del resumen](../HU-008-enganche-del-resumen.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-16 |
| **Ejecutado por** | El agente |
| **Ambiente y versión** | Windows 11 · Python 3.11 · estándar 21.2.1 → 21.3.0 |

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

Un solo ciclo: ningún caso falló por defecto del código ni del propio caso.

---

## 2. Ejecución caso por caso

### CA-04 · CP-001 — el resumen arrastrado apunta al nombre nuevo

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Comprobar el estado inicial del resumen | Dice `(../../2026-01-02-sesion.md)` | Lo dice |
| 2 | Correr `renombrar(...)` con el tema `el-tema-real` | Sin error | Sin error |
| 3 | Mirar la carpeta del día | Está `el-tema-real.md` y no está el viejo | Así quedó |
| 4 | Leer el enlace de adentro | Texto y destino con el nombre nuevo, `2026-01-02-el-tema-real.md` | Exacto |
| 5 | Comprobar contra el disco que el destino existe | El archivo está | Está |
| 6 | Buscar menciones al nombre viejo | Cero | Cero |

**Veredicto:** ✅ Cumple.

---

### CA-04 · CP-002 — el enlace a otra sesión no se toca

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr `renombrar(...)` sobre un resumen que además nombra `2026-01-01-otra.md` | Sin error | Sin error |
| 2 | Leer el enlace propio | Quedó con el nombre nuevo | Quedó |
| 3 | Leer el enlace a la otra sesión | Queda **igual** | Igual |

**Veredicto:** ✅ Cumple. Es el riesgo `B-01` del plan, y no se materializó.

---

### CA-04 · CP-003 — renombrar una sesión sin resumen no revienta

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Borrar la carpeta de resúmenes y correr `renombrar(...)` | Termina sin error | Terminó |
| 2 | Mirar la transcripción y el índice | Renombrada y reindexado | Así quedó |

**Veredicto:** ✅ Cumple.

---

### CA-04 · CP-004 — el caso se pone rojo si se revierte el arreglo

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Comentar la llamada a `_reenlazar()` en `_mover_resumen()` | El arreglo queda revertido | Revertido |
| 2 | Correr la suite de la fase | El CP-001 y el CP-002 se ponen rojos | Los dos rojos, en el paso que lee el enlace: *«el enlace de vuelta no quedó con el nombre nuevo»* |
| 3 | Comprobar que el CP-003 sigue verde | Verde — no depende del arreglo | Verde |
| 4 | Volver a poner la llamada y correr todo | 22 de 22 en verde | 22 de 22 |

**Veredicto:** ✅ Cumple. Los casos miden lo que dicen medir.

---

## 3. Defectos encontrados

Ninguno.

---

## 4. Lo que se descubrió fuera del criterio

**`validadores/enlaces.py` no se puede correr solo.** No tiene punto de entrada: `python validadores/enlaces.py --raiz .` termina en silencio y con código 0 **sin haber comprobado nada**, que es lo peor que puede hacer un validador — se lee como «cero enlaces rotos». El entrypoint real es `python validadores/validar.py estandar --raiz .`. Esta fase lo dio por bueno una vez antes de darse cuenta, y la métrica del §7 quedó corregida contra la corrida de verdad.

**Cerrar el pendiente rompe los enlaces que lo citaban.** Mover el archivo del 35 a `pendientes/hecho/` dejó 12 enlaces rotos: dos en el índice del backlog, uno en el pendiente 36, seis en tres resúmenes del 2026-08-16 y uno en el `plan_trabajo` de esta misma fase. **Ya había pasado y nadie lo vio:** el `plan_trabajo` de la fase `B-EP-007-HU-001` sigue apuntando al archivo del pendiente 45, que se movió al cerrarlo. Es el [pendiente 33 · punto 4](«RUTA-ESTANDAR»/pendientes/33-defectos-que-destaparon-los-resumenes-viejos.md) —renombrar deja rotos los enlaces de fuera— aplicado a los pendientes en vez de a las sesiones.

**`validadores/docs/historico.md` estaba atrasado respecto del código.** El documento no nombraba `renombrar()` ni ninguna de sus siete funciones de apoyo: se escribió antes de que el renombrado existiera. Esta fase documentó lo que su tarea `T-05` exigía —`renombrar()`, `_mover_resumen()`, `_reenlazar()` y las dos constantes— y **no** lo demás: `_titular`, `_reindexar`, `_reindexar_dia`, `_libre`, `_slug`, `_legible`, `_marcar` y `_pedir_nombre` siguen sin documentar.

Queda propuesto y no ejecutado ([`02·F20`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)): no viene de ningún CA de esta fase, así que no se toca por iniciativa propia.

---

## 5. Cobertura contra el plan de pruebas

| Exigencia | Caso | Estado |
|---|---|---|
| CA-04 — el resumen arrastrado apunta al nombre nuevo | CP-001 | ✅ |
| CA-04 · no tocar el enlace de otra sesión | CP-002 | ✅ |
| CA-04 · límite, sesión sin resumen | CP-003 | ✅ |
| CA-04 · prueba de la prueba | CP-004 | ✅ |

**Cobertura:** 1 de 1 CA = 100%. **4 de 4 casos ejecutados.**

---

## 6. Veredicto de la fase

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 1 de 1 |
| **CA en "No"** | ninguno |
| **Defectos abiertos aceptados** | ninguno |

---

## 7. Métricas contra la meta del plan

| Métrica | Meta | Dio |
|---|---|---|
| Cobertura de CA | 100% | 100% |
| Casos ejecutados | 4 de 4 | 4 de 4 |
| Pruebas del repositorio en verde | 19 + 3 nuevas | 22 de 22 |
| Enlaces rotos después de renombrar | 0 | 0 — ninguno de los que reporta `validar.py estandar` viene de renombrar una sesión |

**La primera corrida de esta métrica no valía.** Se corrió `python validadores/enlaces.py --raiz .`, que termina en silencio porque no tiene punto de entrada, y se leyó ese silencio como «cero». La cifra de arriba sale de `python validadores/validar.py estandar --raiz .`, que sí comprueba.
