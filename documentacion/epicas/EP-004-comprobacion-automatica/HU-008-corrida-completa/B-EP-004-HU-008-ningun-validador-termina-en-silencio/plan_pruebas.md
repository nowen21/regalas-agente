# Plan de Pruebas — Fase B-EP-004-HU-008: ningún validador termina en silencio

**Para qué sirve este documento.** Dice **con qué casos se comprueba** que lo construido hace lo que la HU pidió. Su exigencia central es que ningún criterio quede sin caso. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el [resultado_pruebas.md](resultado_pruebas.md).

| Campo | Valor |
|---|---|
| **Código** | PP-B-EP-004-HU-008 |
| **Versión** | 1.0 |
| **Alcance** | Fase `B-EP-004-HU-008-ningun-validador-termina-en-silencio` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Pendiente — el usuario |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12**.

---

## 3. Estrategia de pruebas

### 3.1 Niveles

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Sistema | Cada módulo ejecutado **como lo haría una persona en su terminal** | Subproceso | Sí |
| Regresión | Que las dos suites den lo mismo que antes | El repositorio | Sí |

**No hay unitarias, y es a propósito.** El defecto no vive dentro de una función: vive en **lo que pasa al ejecutar el archivo**. Probarlo importando el módulo no reproduciría nada — el bloque `__main__` no corre al importar. Hay que lanzarlo.

### 3.2 Tipos

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | El silencio, el mensaje y el código de salida |
| Límites | ☑ | El módulo sin subcomando, el enganche, el reparador |
| No regresión | ☑ | Las dos suites |

### 3.3 Técnicas

- **Barrido exhaustivo, leído del disco.** No se prueba una muestra: se prueban **todos** los `.py` de `validadores/`. Una lista escrita a mano dejaría fuera al módulo que nazca mañana, que es justo el que va a tener el hueco.
- **Caso histórico.** `enlaces.py` y `metareglas.py`, los dos que el pendiente nombra, tienen su caso propio además del barrido.
- **Triangulación.** El resultado esperado no sale del programa: sale de mirar si el archivo tiene bloque de arranque y qué subcomando le corresponde.
- **Prueba de la prueba.** Un caso comprueba que la lista de módulos **no esté vacía**. Sin él, un barrido sobre cero archivos pasaría — que es el mismo defecto que esta fase persigue, cometido por la prueba.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)):

1. La suite nueva (`test_ninguno_termina_en_silencio.py`).
2. `validadores/tests/` entera.
3. `validadores/pruebas.py` entera — se toca un archivo que **todas** usan.
4. Los subcomandos de `validar.py` que corren en cada sesión.

---

## 5. Matriz de trazabilidad

| CA / exigencia | Caso(s) | Tipo | Prioridad | Estado |
|---|---|---|---|---|
| CA-02 · una comprobación suelta da un resultado creíble | [CP-001](#cp-001--ninguno-sale-con-0-sin-decir-nada), [CP-002](#cp-002--cada-uno-dice-por-dónde-se-corre) | Funcional | Crítica | ☐ |
| RN-01 · una sola puerta de entrada | [CP-003](#cp-003--el-código-de-salida-distingue-los-dos-casos), [CP-005](#cp-005--metareglas-se-corre-desde-la-puerta) | Funcional | Crítica | ☐ |
| Los dos casos del pendiente | [CP-004](#cp-004--los-dos-casos-que-destaparon-el-pendiente) | Funcional | Crítica | ☐ |
| Transversal · Límites | [CP-006](#cp-006--los-que-no-entran-al-barrido-y-por-qué) | Límites | Alta | ☐ |
| Transversal · No regresión | [CP-007](#cp-007--las-dos-suites-dan-lo-mismo-que-antes) | Regresión | Crítica | ☐ |

**Cobertura:** 5 de 5 exigencias con caso = 100%, **transversales incluidas y contadas**.

---

## 6. Casos de prueba

### CP-001 — Ninguno sale con 0 sin decir nada

| Campo | Valor |
|---|---|
| **Tipo** | Funcional — el defecto que se corrige |
| **Precondiciones** | Ninguna |
| **Datos** | Todos los `.py` de `validadores/`, leídos del disco |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Listar los `.py`, quitando entradas y enganches | Al menos 20 |
| 2 | Ejecutar cada uno en subproceso, sin argumentos | Terminan |
| 3 | Juntar los que salen con 0 **y** sin salida | La lista queda vacía |

**Resultado esperado final:** ninguno afirma con su silencio.

> **Este caso falla hoy** en 33 módulos, que es la medida del pendiente.

---

### CP-002 — Cada uno dice por dónde se corre

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Ejecutar cada módulo suelto | Termina |
| 2 | Buscar `validar.py` en su salida | Está en todos |

**Resultado esperado final:** el mensaje no dice solo «no se corre así»; dice **cómo sí**. Quien corrió el módulo suelto ya demostró que no sabe cuál es su subcomando.

---

### CP-003 — El código de salida distingue los dos casos

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Ejecutar cada módulo suelto y leer su código | **2** en todos |

**Resultado esperado final:** ni 0 ni 1. Con 0 se lee «todo bien»; con 1, «hay fallas». **«No comprobé nada» es una tercera cosa** y necesita su propio código, o un guion que llame por error al módulo no puede distinguirla.

---

### CP-004 — Los dos casos que destaparon el pendiente

| Campo | Valor |
|---|---|
| **Datos** | `enlaces.py` → `estandar` · `metareglas.py` → `metareglas` |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Ejecutar cada uno suelto | Código 2 |
| 2 | Leer la salida | Dice «no comprueba nada» |
| 3 | Buscar el subcomando exacto en el mensaje | Está, y es el suyo |

**Resultado esperado final:** los dos casos nombrados en el pendiente quedan cubiertos con su nombre, no por barrido. **Un defecto que ya se cobró una métrica falsa merece su caso propio.**

---

### CP-005 — `metareglas` se corre desde la puerta

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validar.py metareglas` | Imprime algo |
| 2 | Buscar «meta-reglas» en la salida | Está |
| 3 | Contar los hallazgos | Hay hallazgos: el capítulo 20 no se cumple a sí mismo |

**Resultado esperado final:** las once filas del checklist que solo este programa comprueba vuelven a ser medibles por línea de comandos.

> **Lo que este caso NO comprueba:** que los hallazgos estén bien, ni que sean pocos. Eso es el pendiente 19. Acá se comprueba que **haya con qué medir**.

---

### CP-006 — Los que no entran al barrido, y por qué

| # | Caso | Resultado esperado |
|---|---|---|
| 1 | `validar.py`, `pruebas.py`, `instalar.py`, `historico.py`, `comun.py` | Fuera: tienen arranque propio |
| 2 | Los seis `hook_*.py` | Fuera: se corren solos a propósito, los llama la herramienta |
| 3 | `citas.py` | Fuera: **no es validador, es el reparador**. Corriéndolo sin argumentos simula y dice qué haría |
| 4 | La lista de módulos a barrer | **No vacía** — al menos 20 |

**Resultado esperado final:** las exclusiones están escritas con su motivo, y ninguna es «porque falla».

> El paso 4 es la prueba de la prueba. Un barrido sobre una lista vacía pasa siempre, y pasaría diciendo lo mismo que si hubiera comprobado 40 archivos — **el defecto de esta fase, cometido por la prueba de esta fase**.

---

### CP-007 — Las dos suites dan lo mismo que antes

| Campo | Valor |
|---|---|
| **Precondiciones** | El resultado de las dos suites guardado **antes** del cambio (T-01) |

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validadores/tests/` | Pasa, más los casos nuevos |
| 2 | Correr `validadores/pruebas.py` | Mismos fallos que antes, ni uno más |
| 3 | Comparar contra T-01 | Idéntico |
| 4 | Correr `validar.py` en sus subcomandos de siempre | Igual que antes |

**Resultado esperado final:** los 33 bloques de arranque no cambiaron el comportamiento de ninguna función.

> **Cuidado especial con el paso 2.** Hay **otra sesión trabajando en el mismo árbol**, y sus archivos a medias hacen fallar pruebas que no tienen nada que ver con esta fase. La comparación se hace con los cambios de esta fase guardados aparte (`git stash`), o los fallos ajenos se leen como propios.

---

## 9. Gestión de defectos

| Severidad | Qué sería acá | Atención |
|---|---|---|
| **Crítica** | Que algún módulo siga saliendo con 0 en silencio, o que una suite deje de pasar | Inmediato |
| **Alta** | Que el mensaje no nombre el subcomando correcto | Antes de cerrar |
| **Media** | Redacción del mensaje | Se reporta |

Lo que aparezca fuera de estos criterios **se propone, no se arregla de paso** ([`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)).

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Módulos que salen con 0 en silencio | **0** (eran 33) |
| Módulos que no dicen por dónde se corren | **0** |
| Pruebas del repositorio que dejan de pasar | **0** |
| Fallos nuevos respecto de la línea base | **0** |
| Cobertura de exigencias | 100% — 5 de 5, transversales incluidas |

Un solo concepto, sin estado intermedio: **Cumple** o **No cumple**.
