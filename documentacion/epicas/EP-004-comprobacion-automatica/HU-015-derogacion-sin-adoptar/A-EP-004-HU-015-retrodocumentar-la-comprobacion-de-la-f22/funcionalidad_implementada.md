# Funcionalidad implementada — Fase «A-EP-004-HU-015-retrodocumentar-la-comprobacion-de-la-f22»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito **qué quedó hecho**, para que quien llegue después no tenga que deducirlo del código ni del historial.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-004-HU-015-retrodocumentar-la-comprobacion-de-la-f22` |
| **Épica / HU** | [EP-004](../../epica.md) · [HU-015](../HU-015-derogacion-sin-adoptar.md) |
| **Versión del estándar** | 21.3.0 → **21.3.1** (PARCHE) |
| **Fecha de cierre** | 2026-08-16 |

---

## 1. Qué quedó funcionando

**No cambió ninguna línea de producción.** Lo que faltaba era la cadena: el programa que comprueba [`02·F22`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md) se escribió el 2026-08-16 en la misma sesión que la regla, sin épica, sin historia y sin fase. Ahora tiene su fase, su plan y —lo que de verdad le faltaba— **evidencia que corre**.

Lo que quedó comprobado, contra las derogaciones reales del estándar:

- Un proyecto que declara una versión anterior a una derogación **y tiene fases** produce una falla que nombra la regla jubilada, en qué versión se jubiló y qué la reemplazó.
- Una derogación ya adoptada no se vuelve a cobrar.
- Sin fases no se cobra: el trabajo que `02·F0` exceptúa no queda bloqueado.
- Sin `CLAUDE.md` o sin versión declarada, calla en vez de romper, y comprobar no modifica nada del proyecto.

---

## 2. Qué se tocó

| Archivo | Qué |
|---|---|
| [`validadores/tests/test_version_derogaciones.py`](../../../../../validadores/tests/test_version_derogaciones.py) | **Nuevo.** Cuatro casos, uno por criterio más los transversales |
| [`validadores/docs/version.md`](../../../../../validadores/docs/version.md) | Dice que las tres funciones están bajo prueba, y por qué unos casos usan datos reales y otro inventados |
| [`HU-015-derogacion-sin-adoptar.md`](../HU-015-derogacion-sin-adoptar.md) | §8 con la fase, tareas, `DoD`, estado y bitácora |
| [`pendientes/hecho/el-validador-de-la-f22-tiene-su-fase.md`](../../../../../pendientes/hecho/el-validador-de-la-f22-tiene-su-fase.md) | El pendiente 38, cerrado |
| [`CHANGELOG.md`](../../../../../CHANGELOG.md) · `VERSION` | 21.3.1 |

---

## 3. Cómo se comprueba

```
python -m unittest discover -s validadores/tests
```

26 pruebas, 26 en verde. Las cuatro nuevas están en `ProyectoDeMentira`.

**Los casos corren contra las derogaciones reales del estándar**, no contra una inventada: si mañana cambia la marca del encabezado que `20·M11` exige, la prueba lo dice en vez de pasar contra un dato de mentira. El único que usa datos inventados es el del filtro de versiones, porque es aritmética y con datos reales cambiaría de significado en cada derogación nueva.

---

## 4. Qué quedó fuera

- **Reconocer la fase que adopta la derogación** para dejarla pasar. Ya estaba declarado fuera de alcance en la historia.
- **El filtro de las reglas opcionales** que el proyecto nunca encendió.
- **La especificación del módulo de comprobación.** Deuda heredada, declarada en el §10 del plan.

---

## 5. Lo que esta fase dejó dicho

**El diagnóstico del pendiente 38 estaba a medias.** Decía que el código había quedado sin el registro que dice por qué es como es, y resultó que `validadores/docs/version.md` ya lo explicaba con ejemplos. Lo que faltaba no era documentación: era **prueba**. Un trabajo sin fase se queda sin plan de pruebas, y eso es lo que no se recupera solo.
