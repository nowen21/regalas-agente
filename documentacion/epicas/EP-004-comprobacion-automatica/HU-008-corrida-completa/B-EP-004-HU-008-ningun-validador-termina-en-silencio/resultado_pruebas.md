# Resultado de Pruebas — Fase B-EP-004-HU-008: ningún validador termina en silencio

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué resultado y si cada criterio quedó cumplido**. No se edita el [plan_pruebas.md](plan_pruebas.md) al correr: lo que pasó va acá, para no perder la línea base aprobada.

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-004-HU-008-ningun-validador-termina-en-silencio` |
| **Plan de pruebas** | [PP-B-EP-004-HU-008](plan_pruebas.md) v1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-17 |
| **Ejecutado por** | El agente |
| **Máquina** | Windows 11, Python del sistema |

---

## 1. Línea base, tomada antes de tocar nada (T-01)

| Qué se corrió | Resultado **antes** |
|---|---|
| `validadores/tests/` | `Ran 36 tests · OK` |
| `validadores/pruebas.py` | `Ran 357 tests · FAILED (failures=8, errors=1, expected failures=7)` |
| `validar.py estandar` | `1 falla(s), 5 aviso(s)` |
| Módulos que salen con 0 sin imprimir nada | **33** |

**Los 8 fallos y el 1 error de la línea base no son de esta fase.** Se comprobó guardando los cambios aparte con `git stash` y volviendo a correr: la lista de fallos es **idéntica**, nombre por nombre. Son el estado en vuelo de **otra sesión que trabaja en el mismo árbol** — sus carpetas de fase a medias hacen fallar las pruebas que leen `documentacion/`.

Sin esta comparación, los 8 fallos se habrían leído como daño propio, y arreglar lo que no está roto habría pisado el trabajo de la otra sesión.

---

## 2. Medición del hueco (T-02)

| Qué | Cuánto |
|---|---|
| Archivos `.py` en `validadores/` | 45 |
| Con bloque de arranque | 11 |
| **Sin arranque — salían con código 0 y sin salida** | **33** |

El pendiente decía *«son unos treinta programas; no se sabe cuántos tienen el mismo hueco, y esa es media gracia de este pendiente»*. **La respuesta es 33.**

---

## 3. Casos ejecutados

| Caso | Veredicto | Qué dio |
|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--ninguno-sale-con-0-sin-decir-nada) — ninguno sale con 0 sin decir nada | ✅ **Pasa** | Barrido sobre los 34 módulos que entran: **0 mudos**. Eran 33 |
| [CP-002](plan_pruebas.md#cp-002--cada-uno-dice-por-dónde-se-corre) — cada uno dice por dónde se corre | ✅ **Pasa** | Los 34 nombran `validar.py` en su salida |
| [CP-003](plan_pruebas.md#cp-003--el-código-de-salida-distingue-los-dos-casos) — el código distingue los dos casos | ✅ **Pasa** | Los 34 salen con **2** |
| [CP-004](plan_pruebas.md#cp-004--los-dos-casos-que-destaparon-el-pendiente) — los dos casos del pendiente | ✅ **Pasa** | Ver §4 |
| [CP-005](plan_pruebas.md#cp-005--metareglas-se-corre-desde-la-puerta) — `metareglas` desde la puerta | ✅ **Pasa** | Ver §5 |
| [CP-006](plan_pruebas.md#cp-006--los-que-no-entran-al-barrido-y-por-qué) — los que no entran, y por qué | ✅ **Pasa** | Ver §6 |
| [CP-007](plan_pruebas.md#cp-007--las-dos-suites-dan-lo-mismo-que-antes) — las dos suites | ✅ **Pasa** | Ver §7 |

**7 de 7 casos ejecutados. 7 pasan.**

---

## 4. CP-004 · Los dos casos que destaparon el pendiente

Antes, el caso literal del pendiente:

```
python validadores/enlaces.py --raiz .
→ (nada)
código de salida: 0
```

Después:

```
$ python validadores/enlaces.py --raiz .
enlaces.py no se corre solo: es una pieza de `validar.py`, y correrlo así **no comprueba nada**.

Se corre con:
  python validadores/validar.py estandar
código de salida: 2

$ python validadores/metareglas.py
metareglas.py no se corre solo: es una pieza de `validar.py`, y correrlo así **no comprueba nada**.

Se corre con:
  python validadores/validar.py metareglas
código de salida: 2
```

---

## 5. CP-005 · Lo que destapó poder correr `metareglas`

```
$ python validadores/validar.py metareglas
== El estándar contra sus meta-reglas · . ==
…
7 falla(s), 229 aviso(s).
```

**Esa medición no se podía repetir por línea de comandos desde el 2026-08-14**, y el pendiente [19](../../../../../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md) cita una hecha ese día. Ahora sí.

**Los 7 fallos y 229 avisos no son de esta fase y no se arreglan acá.** Son el capítulo 20 sin cumplirse a sí mismo, que es exactamente lo que el pendiente 19 describe. Lo que esta fase entrega es **con qué medirlo**.

---

## 6. CP-006 · Las exclusiones, con su motivo

| Excluido | Por qué |
|---|---|
| `validar.py`, `pruebas.py`, `instalar.py`, `historico.py`, `comun.py` | Tienen arranque propio y hacen algo al correrse |
| Los seis `hook_*.py` | Son enganches: los llama la herramienta, se corren solos a propósito |
| `citas.py` | **No es validador, es el reparador.** Sin argumentos simula y dice qué haría — lo contrario de callar |

Ninguna exclusión es «porque falla». Y la lista de módulos a barrer se comprueba **no vacía**: sin eso, un barrido sobre cero archivos pasaría diciendo lo mismo que uno sobre cuarenta.

---

## 7. CP-007 · No regresión

| Qué se corrió | Antes | Después |
|---|---|---|
| `validadores/tests/` | `36 tests · OK` | **`42 tests · OK`** (6 nuevos) |
| `validadores/pruebas.py` | `357 · FAILED (8 failures, 1 error, 7 expected failures)` | `357 · FAILED (8 failures, 1 error, **6** expected failures)` |
| `validar.py estandar` | `1 falla, 5 avisos` | `1 falla, 5 avisos` |
| `validar.py fases` | `0 fallas, 44 avisos` | `0 fallas, 44 avisos` |
| `validar.py pendientes` | `OK` | `OK` |
| `validar.py trazabilidad` | `0 fallas, 16 avisos` | `0 fallas, 16 avisos` |

**Los mismos 8 fallos y el mismo error, nombre por nombre.** Ninguno nuevo.

**La diferencia de los `expected failures` es a favor.** Uno de los siete pasó a aprobar: `test_la_regla_sin_clasificar_detiene_la_publicacion`, que el propio pendiente 53 había dejado marcada como fallo esperado por su punto 2. Se le quitó la marca, como el pendiente pedía.

---

## 8. Lo que apareció y no se arregló  ·  [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)

### D-02 · La regla sin clasificar avisa, y un aviso no detiene

Al quitarle el `expectedFailure` a la prueba se leyó su texto completo. Denunciaba **dos** cosas y la prueba solo comprobaba una:

1. `metareglas.py` no tiene subcomando → **cerrado acá**.
2. Lo que sale es un `AVISO`, que no detiene nada → **sigue abierto**.

La prueba pasa con la mitad hecha, así que se le escribió encima qué **no** comprueba. Va al pendiente [19](../../../../../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md).

### D-03 · `citas.py --aplicar` ensuciaría `base/`

Corriendo el reparador en simulación:

```
4 enlazadas · 1 reparadas · 4 archivos (simulado; agrega --aplicar)
```

**Las cinco están mal.** Son los mismos cinco avisos que `validar.py estandar` reporta y que el pendiente [55](../../../../../pendientes/hecho/los-enlaces-de-ejemplo-no-son-enlaces.md) ya identificó como falsos positivos: cuatro son identificadores nombrados **como ejemplo** y el quinto es un enlace a un ancla del mismo archivo, que es lo correcto.

Es peor de lo que el 55 decía. Aquel dice que el validador **reporta de más**; esto es que el reparador **escribiría** ese error en `base/`. Va al pendiente 55.

### Un dato del 55 que resultó falso

El pendiente 55 afirma, sobre `base/20-meta-reglas/estructura-regla.md`, que **«`G9` no existe»**. Sí existe: [base/09-git.md](../../../../../base/09-git.md), *La historia de usuario es la unidad del commit*. Sigue siendo un falso positivo —es un ejemplo, no una cita— pero por otro motivo del que el pendiente da. Corregido allá.

---

## 9. Veredicto

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 5 de 5 — CA-02, `RN-01`, los dos casos del pendiente, Límites y No regresión |
| **CA en «No»** | ninguno |
| **Defectos abiertos aceptados** | `D-02` y `D-03`, los dos **fuera del alcance declarado** y reportados a su pendiente |
| **Ciclos** | 1 |

**Un solo concepto, sin estado intermedio.** Los dos defectos abiertos no bajan el veredicto porque ninguno pertenece a esta fase: el plan los declaró fuera de alcance en §1 antes de ejecutar, no después de encontrarlos.
