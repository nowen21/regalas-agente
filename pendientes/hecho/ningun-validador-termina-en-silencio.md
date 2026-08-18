# Pendiente · `enlaces.py` termina en silencio sin comprobar nada

**Estado:** **cerrado** el 2026-08-17. Anotado el 2026-08-16.

> **Moverlo a `hecho/` costó 54 enlaces rotos la primera vez.** Se deshizo, se construyó [validadores/cerrar.py](../../validadores/cerrar.py) —que mueve el archivo y arrastra sus citas— y se movió con él. Esa medición de 54 es lo que cerró la discusión del [54](../54-cerrar-un-pendiente-rompe-sus-citas.md).

| | |
|---|---|
| **Historia de usuario** | [EP-004 · HU-008 — Correr todas las comprobaciones de una sola vez](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-008-corrida-completa/HU-008-corrida-completa.md) — su RN-01 pide una sola puerta de entrada; un módulo que corre solo y calla es la puerta que falta |
| **De dónde sale** | El hallazgo H-4 del [resumen de la sesión 7](../../historico-chat/resumenes/2026-08-16/sesion-7.md) |
| **Proyecto de origen** | El estándar mismo |
| **Fase que lo cerró** | [`B-EP-004-HU-008-ningun-validador-termina-en-silencio`](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-008-corrida-completa/B-EP-004-HU-008-ningun-validador-termina-en-silencio) — veredicto **Cumple** |

## El problema

```
python validadores/enlaces.py --raiz .
→ (nada)
código de salida: 0
```

No tiene bloque de arranque. **No comprobó nada**, y lo dice con el mismo silencio con el que un validador dice «está todo bien».

## Por qué es `P1`

Un validador que calla sin haber mirado es peor que ninguno: el que no existe se nota, este **afirma**. La fase `B-EP-005-HU-008` se lo creyó el 2026-08-16 y escribió «cero enlaces rotos» en su resultado de pruebas; el entrypoint real —`validar.py estandar`— reportaba veinte. La métrica se corrigió el mismo día, pero pudo haber cerrado así.

## Qué falta

1. Que `enlaces.py` **tenga punto de entrada**, o que se muera diciendo por dónde se corre.
2. **Revisar los demás.** Son unos treinta programas en `validadores/`; no se sabe cuántos tienen el mismo hueco, y esa es media gracia de este pendiente.

   **Segundo caso encontrado: `metareglas.py`** (2026-08-17, retro-documentando EP-001). Mismo síntoma —`python validadores/metareglas.py` no imprime nada y sale con 0— y sin subcomando en `validar.py`. Pesa más que el de `enlaces.py`: es el único programa que comprueba once de las veinte filas del [checklist del estándar](../../base/20-meta-reglas/checklist.md) —entre ellas la 5, que `M3` necesita, y la 15, que impide que una regla normal mande sobre una `[BLINDADA]`— y además `M16`, el respaldo de toda regla de proyecto. El pendiente [19](../19-el-capitulo-20-no-se-cumple-a-si-mismo.md) cita una medición hecha con él el 2026-08-14: hoy esa medición no se puede repetir por la línea de comandos.

## Con qué se cruza

- El [55](../55-el-validador-lee-enlaces-dentro-de-las-comillas-de-codigo.md) y el punto 1 del [33](../33-defectos-que-destaparon-los-resumenes-viejos.md), que son del mismo archivo: los tres hacen que sus hallazgos no se puedan creer, unos por callar y otros por hablar de más.

## Cómo se sabrá que cerró

Correr cualquier validador suelto o dice lo que encontró, o dice cómo se corre. Ninguno termina en silencio con código 0 sin haber mirado.

---

# Cómo cerró — 2026-08-17

## Qué se arregló

**Los dos puntos del pendiente.**

**1 · El silencio.** Un módulo de `validadores/` ejecutado solo caía hasta el final del archivo y salía con código 0 sin imprimir nada — que es exactamente lo que imprime cuando ha mirado todo y está en orden. Ahora muere diciendo por dónde se corre, con su subcomando exacto, y sale con **código 2**: ni 0 ni 1, para que «no comprobé nada» no se confunda ni con «todo bien» ni con «hay fallas».

**2 · `metareglas.py` no tenía subcomando.** Ya lo tiene, con `--catalogo` para el catálogo de un proyecto. Era el único programa que comprueba once de las veinte filas del [checklist del estándar](../../base/20-meta-reglas/checklist.md) —entre ellas la 5, que `M3` necesita, y la 15, que impide que una regla normal mande sobre una `[BLINDADA]`—.

## La respuesta a lo que el pendiente preguntaba

Decía: *«son unos treinta programas; no se sabe cuántos tienen el mismo hueco, y esa es media gracia de este pendiente»*.

**Son 33 de 45.** La proporción es la noticia: no era un descuido en `enlaces.py`, era el comportamiento por omisión de todo el módulo de comprobación. Cualquier `.py` sin bloque de arranque hace esto, y nadie tiene que equivocarse para que pase.

## Los números

| Qué | Antes | Ahora |
|---|---|---|
| Módulos que salen con 0 sin imprimir nada | **33** | **0** |
| Subcomandos de `validar.py` | 25 | 26 |
| Pruebas en `validadores/tests/` | 36 | 42 |
| Fallos nuevos en las dos suites | — | **0** |

La prueba nueva —[`test_ninguno_termina_en_silencio.py`](../../validadores/tests/test_ninguno_termina_en_silencio.py)— **lee los módulos del disco**, no de una lista, así que el programa número 46 entra solo.

## Lo que destapó y no se arregló acá

| Qué | Adónde fue |
|---|---|
| `D-02` — la regla sin clasificar **avisa**, y un aviso no detiene | El [19](../19-el-capitulo-20-no-se-cumple-a-si-mismo.md) |
| `D-03` — `citas.py --aplicar` **escribiría** en `base/` cuatro ejemplos enlazados como si fueran citas | El [55](../55-el-validador-lee-enlaces-dentro-de-las-comillas-de-codigo.md) |
| El 55 afirmaba que `G9` no existe, y sí existe | Corregido en el propio 55 |

**Y una medición que vuelve a ser posible.** `validar.py metareglas` reporta hoy **7 fallas y 229 avisos**. No son de esta fase: son el capítulo 20 sin cumplirse a sí mismo, o sea el [19](../19-el-capitulo-20-no-se-cumple-a-si-mismo.md). Ese pendiente citaba una medición del 2026-08-14 que desde entonces no se podía repetir por línea de comandos. Ahora sí.
