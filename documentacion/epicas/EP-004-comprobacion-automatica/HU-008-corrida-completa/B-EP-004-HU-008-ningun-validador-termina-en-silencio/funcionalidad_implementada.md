# Funcionalidad implementada — Fase B-EP-004-HU-008: ningún validador termina en silencio

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase. El plan decía qué se iba a hacer; esto dice qué hay ahora en el repositorio.

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-004-HU-008-ningun-validador-termina-en-silencio` |
| **HU** | [HU-008 Correr todas las comprobaciones de una sola vez](../HU-008-corrida-completa.md) |
| **Cierra** | El [pendientes/53-enlaces-py-no-tiene-punto-de-entrada.md](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md), sus dos puntos |
| **Fecha de cierre** | 2026-08-17 |
| **Veredicto** | **Cumple** — [resultado_pruebas.md](resultado_pruebas.md) §9 |

---

## Qué hay ahora que antes no había

### 1 · Un módulo que se corre solo dice por dónde se corre

`comun.no_es_punto_de_entrada(subcomando)` imprime a `stderr` y sale con **2**:

```
enlaces.py no se corre solo: es una pieza de `validar.py`, y correrlo así **no comprueba nada**.

Se corre con:
  python validadores/validar.py estandar
```

Los **33** módulos que salían con código 0 y sin salida lo llaman en su bloque de arranque, cada uno nombrando el subcomando que de verdad lo ejecuta.

**El código 2 no es un capricho.** Con 0 el resultado se lee «todo bien»; con 1, «hay fallas». «No comprobé nada» es una tercera cosa y necesitaba su propio número, o un guion que llame al módulo por error no puede distinguirla.

### 2 · `validar.py metareglas`

El único programa que comprueba **once de las veinte filas** del [checklist del estándar](../../../../../base/20-meta-reglas/checklist.md) no estaba en la puerta de entrada. Ahora sí, con `--catalogo` para comprobar además el catálogo de un proyecto (`M16`).

Entre esas once filas están la **5**, que `M3` necesita, y la **15**, que impide que una regla normal mande sobre una `[BLINDADA]`.

Lo que reporta hoy: **7 fallas y 229 avisos**. No son de esta fase — son el capítulo 20 sin cumplirse a sí mismo, o sea el pendiente [19](../../../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md). Lo que esta fase entrega es **con qué medirlo**: esa medición no se podía repetir por línea de comandos desde el 2026-08-14.

### 3 · Una prueba que lee el disco, no una lista

`validadores/tests/test_ninguno_termina_en_silencio.py`, seis casos. Recorre **todos** los `.py` de `validadores/` leyéndolos del disco, así que el programa número 46 entra solo sin que nadie se acuerde de agregarlo.

Uno de los seis casos comprueba que **la lista no esté vacía**. Sin él, un barrido sobre cero archivos pasaría — el mismo defecto de esta fase, cometido por la prueba de esta fase.

### 4 · Una marca de fallo esperado que se retiró

`test_la_regla_sin_clasificar_detiene_la_publicacion` estaba marcada `expectedFailure` por el punto 2 de este pendiente. Ahora pasa. Se le escribió encima **qué no comprueba**, porque su texto denunciaba dos cosas y solo verifica una.

---

## Los números

| Qué | Antes | Ahora |
|---|---|---|
| Módulos que salen con 0 sin imprimir nada | **33** | **0** |
| Módulos que no dicen por dónde se corren | 33 | 0 |
| Subcomandos de `validar.py` | 25 | 26 |
| Pruebas en `validadores/tests/` | 36 | 42 |
| Fallos nuevos en las dos suites | — | **0** |

---

## Lo que quedó abierto, y dónde

| Qué | Dónde va |
|---|---|
| `D-02` — la regla sin clasificar **avisa** y un aviso no detiene | Pendiente [19](../../../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md) |
| `D-03` — `citas.py --aplicar` **escribiría** en `base/` cuatro ejemplos enlazados como si fueran citas | Pendiente [55](../../../../../pendientes/55-el-validador-lee-enlaces-dentro-de-las-comillas-de-codigo.md) |
| El pendiente 55 afirma que `G9` no existe, y sí existe | Corregido en el propio 55 |

Ninguno pertenece a esta fase: el plan los dejó fuera de alcance en su §1 **antes** de ejecutar.

---

## Lo que se supo

**El pendiente preguntaba cuántos módulos tenían el mismo hueco y decía que esa era media gracia.** Son **33 de 45**. La proporción es la noticia: no era un descuido en `enlaces.py`, era el comportamiento por omisión de todo el módulo de comprobación. Cualquier archivo `.py` sin bloque de arranque hace esto, y nadie tiene que equivocarse para que pase.

**Y el reparador es peor que el validador.** `enlaces.py` reportaba de más; `citas.py --aplicar` **escribiría** ese error en `base/`. El pendiente 55 describía el primer daño y no el segundo.
