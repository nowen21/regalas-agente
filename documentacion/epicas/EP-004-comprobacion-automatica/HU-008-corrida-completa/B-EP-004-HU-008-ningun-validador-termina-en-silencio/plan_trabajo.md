# Plan de Trabajo — Fase B-EP-004-HU-008-ningun-validador-termina-en-silencio (módulo Comprobación automática)

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en [HU-008](../HU-008-corrida-completa.md); las pruebas, en el [plan_pruebas.md](plan_pruebas.md); lo que dieron, en el [resultado_pruebas.md](resultado_pruebas.md); lo que quedó, en el [funcionalidad_implementada.md](funcionalidad_implementada.md).

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `B-EP-004-HU-008-ningun-validador-termina-en-silencio` |
| **Épica** | [EP-004 Comprobación automática](../../epica.md) |
| **HU** | [HU-008 Correr todas las comprobaciones de una sola vez](../HU-008-corrida-completa.md) — una sola (`F12.1`) |
| **Módulo** | Comprobación automática (`validadores/`) |
| **Especificación del módulo** | [HU-008](../HU-008-corrida-completa.md). Su `RN-01` —una sola puerta de entrada— es la especificación de esta fase |
| **Fecha apertura** | 2026-08-17 |
| **Rama** | `main` (árbol compartido con otra sesión; ver §10, B-04) |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): 🔀 **Híbrido.**

- 📝 **Complementa** a la [fase A](../A-EP-004-HU-008-la-corrida-completa-en-una-linea/), que construye la puerta de entrada única. Esta se ocupa de lo que pasa cuando alguien **no** la usa.
- ✨ **Funcionalidad nueva:** el guardián de arranque y el subcomando `metareglas`.

**De dónde sale:** el [pendientes/hecho/ningun-validador-termina-en-silencio.md](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md).

**CA de la HU que cubre esta fase**

| CA de HU-008 | Qué exige | Estado al abrir |
|---|---|---|
| [CA-02](../HU-008-corrida-completa.md) — se puede correr una sola | Que correr una comprobación suelta dé un resultado creíble | **Roto.** 33 de 45 módulos salían con código 0 sin imprimir nada |

**Y su `RN-01`,** que pide una sola puerta de entrada: `metareglas.py` no estaba en ella, así que once de las veinte filas del [checklist del estándar](../../../../../base/20-meta-reglas/checklist.md) no se podían comprobar por línea de comandos.

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que ningún programa de `validadores/` pueda afirmar con su silencio. O dice lo que encontró, o dice por dónde se corre.

**Por qué es grave y no cosmético.** Un validador que no existe se nota. Uno que calla **afirma**: sale con código 0 y sin salida, que es exactamente lo que imprime cuando ha mirado todo y está en orden. La fase `B-EP-005-HU-008` se lo creyó el 2026-08-16 y escribió «cero enlaces rotos» en su resultado de pruebas; el entrypoint real reportaba veinte.

**Fuera de alcance:**

- **Convertir en `FALLA` el `AVISO` de la regla sin clasificar** (defecto `D-02`). Se descubrió al quitar el `expectedFailure` y **no se arregla acá**: es del pendiente [19](../../../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md) ([`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)).
- **Los 7 fallos y 229 avisos que destapó `validar.py metareglas`.** Son el pendiente 19. Acá se construye el que mide, no se arregla lo medido.
- **Los enganches** (`hook_*.py`), que se corren solos a propósito.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

**Medido el 2026-08-17 contra el repositorio:**

| Qué | Cuánto |
|---|---|
| Archivos `.py` en `validadores/` | 45 |
| Con bloque de arranque | 11 |
| **Sin arranque — salían con 0 en silencio** | **33** |
| Enganches, que se corren solos a propósito | 6 |
| Subcomandos de `validar.py` | 25, y `metareglas` no era uno |

> El pendiente decía «unos treinta programas; no se sabe cuántos tienen el mismo hueco». **Son 33**, y esa cuenta era media gracia del pendiente.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo | Tipo | Nota |
|---|---|---|
| `validadores/comun.py` | Modificar | `no_es_punto_de_entrada()`, el ayudante que muere diciendo por dónde se corre |
| 33 módulos de `validadores/` | Modificar | Su bloque de arranque, con el subcomando que les corresponde |
| `validadores/validar.py` | Modificar | El subcomando `metareglas`, con su `--catalogo` |
| `validadores/tests/test_ninguno_termina_en_silencio.py` | Nuevo | Los casos de §3 |
| `validadores/pruebas.py` | Modificar | Quitarle el `expectedFailure` a la prueba que el propio pendiente dejó marcada |

### 2.2 Matriz de dependencias del refactor  ·  `F17`

| Archivo | Cambio | Quién depende | Dónde podría romper |
|---|---|---|---|
| Los 33 módulos | Bloque `__main__` nuevo; **ninguna función cambia** | `validar.py`, los enganches, las pruebas | Solo si algo los ejecutaba como guion esperando código 0. Se comprueba corriendo las dos suites |
| `comun.py` | Función nueva | Todos | Nada: no toca lo que ya había |
| `validar.py` | Import y subcomando nuevos | Los enganches | Los subcomandos existentes no se tocan |

**Comprobación previa obligatoria (T-01):** correr las dos suites **antes** y guardar el resultado. Sin eso, «los fallos que quedan ya estaban» es una afirmación sin respaldo — y en este repositorio hay otra sesión trabajando en el mismo árbol, así que la afirmación importa más que de costumbre.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Sale con código **2** | Salir con 1 | Con 1 se confunde «no comprobé nada» con «comprobé y hay fallas». Son cosas opuestas y un guion tiene que poder distinguirlas |
| El mensaje va a `stderr` | A `stdout` | Quien tenga la salida en una tubería no debe recibir esto como si fueran hallazgos |
| El mensaje nombra el subcomando exacto | Un «ver `--help`» genérico | Quien corrió el módulo suelto ya demostró que no sabe cuál es. Decírselo cuesta una línea |
| El ayudante vive en `comun.py` | Repetir el bloque en cada módulo | 33 copias envejecen distinto |
| La prueba lee los módulos **del disco** | Una lista escrita a mano | Una lista a mano no cubre al módulo 46. Así entra solo |

### 2.7 Dudas por resolver antes de escribir

Ninguna. El pendiente traía las dos salidas —tener punto de entrada, o morirse diciendo por dónde se corre— y son compatibles: los que tienen subcomando lo nombran, los que no, mandan al `--help`.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Correr las dos suites **antes** y guardar el resultado | Test | 0,25 h | — | EV-01 |
| T-02 | Medir cuántos módulos tienen el hueco | Test | 0,25 h | — | EV-02 |
| T-03 | `comun.no_es_punto_de_entrada()` | Comprobación | 0,5 h | T-01 | EV-03 |
| T-04 | El bloque de arranque en los 33, con su subcomando | Comprobación | 1 h | T-03 | EV-03 |
| T-05 | El subcomando `metareglas` en `validar.py` | Comprobación | 0,5 h | T-03 | EV-04 |
| T-06 | La prueba que recorre el disco y no una lista | Test | 1 h | T-04 | EV-03 |
| T-07 | Quitarle el `expectedFailure` a la prueba del punto 2 | Test | 0,25 h | T-05 | EV-04 |
| T-08 | Comparar las dos suites contra T-01 | Test | 0,25 h | T-06, T-07 | EV-01 |

**Total estimado:** 4 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-03 → T-04 → T-06 → T-08.
**Paralelizables:** T-02 desde el principio; T-05 y T-07 después de T-03.

**T-01 va primero y no se salta**, y esta vez por dos razones: la de siempre, y que hay otra sesión escribiendo en el mismo árbol.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación

| CA | Método | Evidencia | Estado |
|---|---|---|---|
| CA-02 / RN-01 | Ejecutar cada módulo suelto y mirar código y salida | EV-02, EV-03 | ☑ |
| RN-01 · `metareglas` | Correr el subcomando nuevo | EV-04 | ☑ |
| No regresión | Comparar las dos suites contra la línea base | EV-01 | ☑ |

| ID | Evidencia | Dónde |
|---|---|---|
| EV-01 | Las dos suites, antes y después | [resultado_pruebas.md](resultado_pruebas.md) |
| EV-02 | El conteo de módulos mudos | [resultado_pruebas.md](resultado_pruebas.md) |
| EV-03 | Salida de los módulos corridos sueltos | [resultado_pruebas.md](resultado_pruebas.md) |
| EV-04 | Salida de `validar.py metareglas` | [resultado_pruebas.md](resultado_pruebas.md) |

---

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | El repositorio, de lectura. Los módulos se ejecutan en subproceso y no escriben nada |
| Datos precargados | Ninguno: el material de prueba son los propios `.py` |

**`citas.py` no se ejecuta con `--aplicar`** en ninguna prueba: sin esa bandera simula, y con ella escribiría en `base/` ([`00·N4`](../../../../../base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada)).

---

## 7. Reversión / rollback

Se revierte volviendo el commit atrás. Ninguna función cambió: quitar los bloques de arranque devuelve el comportamiento anterior exacto.

---

## 8. Producción y migración incremental

**No toca datos.** Cambia lo que ve quien ejecute un módulo suelto: antes nada y código 0, ahora un mensaje y código 2. **Un guion externo que dependiera del código 0 se rompería** — y es lo correcto: ese guion creía estar comprobando algo.

---

## 9. Reglas del estándar aplicadas

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F11`](../../../../../base/02-flujo-de-trabajo/reglas/F11-una-fase-solo-modifica-codigo-de-su-propio-modulo.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md), [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar).

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que algún módulo se ejecutara como guion en algún sitio | Se rompería | Las dos suites y los enganches comprobados | **Cerrado:** ninguna suite cambió |
| B-02 | Que el mensaje se lea como un hallazgo | Ruido | Va a `stderr` y con código 2 | **Cerrado** |
| B-03 | `D-02`: la regla sin clasificar avisa y no detiene | Un aviso no impide publicar | **Fuera de alcance.** Reportado al pendiente 19 | Abierto |
| B-04 | Otra sesión escribe en el mismo árbol | Confundir sus fallos con los propios | T-01: línea base comparada con `git stash`. Los 8 fallos y 1 error son suyos | **Cerrado por medición** |
| B-05 | `citas.py --aplicar` enlazaría cuatro ejemplos como si fueran citas | Ensuciaría `base/` | **Descubierto acá, fuera de alcance.** Reportado al pendiente 55 | Abierto |

---

## 11. Definition of Done

- [x] Ningún módulo sale con 0 sin imprimir nada
- [x] Cada uno dice por dónde se corre, con su subcomando exacto
- [x] El código de salida distingue «no comprobé» de «hay fallas»
- [x] `validar.py metareglas` existe y comprueba
- [x] La prueba recorre el disco, no una lista
- [x] `expectedFailure` retirado de la prueba del punto 2
- [x] Las dos suites comparadas contra la línea base
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el [funcionalidad_implementada.md](funcionalidad_implementada.md) de esta fase.
