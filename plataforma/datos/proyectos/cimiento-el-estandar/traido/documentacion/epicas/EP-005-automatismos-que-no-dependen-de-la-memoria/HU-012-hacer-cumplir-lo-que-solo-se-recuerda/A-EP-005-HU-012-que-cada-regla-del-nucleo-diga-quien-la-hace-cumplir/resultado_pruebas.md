# Resultado de Pruebas — Fase `A-EP-005-HU-012-que-cada-regla-del-nucleo-diga-quien-la-hace-cumplir`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué resultado y si cada criterio quedó cumplido**. Los casos están en el [plan_pruebas.md](plan_pruebas.md); lo que se pedía, en la [HU-012](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-005-HU-012-que-cada-regla-del-nucleo-diga-quien-la-hace-cumplir` |
| **HU** | [HU-012](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md) |
| **Fecha de ejecución** | 2026-08-31 |
| **Ejecutó** | El agente, sobre el repositorio del estándar |
| **Ciclo** | 1 |

---

## 1. Resumen de la ejecución

| | Cuántos |
|---|---|
| Casos del plan | 9 |
| Ejecutados | 9 |
| Pasaron | 9 |
| Fallaron | 0 |
| Pruebas automáticas nuevas | **51** (24 del validador, 27 de la pieza de redacción) |

**La cifra que abre y cierra la fase:**

| | Antes | Después |
|---|---|---|
| Reglas vigentes del capítulo `00` | 18 | 18 |
| Sin decir quién las hace cumplir | **18** | **0** |
| Con una pieza que las ejecuta, declarada | 0 | **5** — `N6`, `N7`, `ID8`, `ID9`, `ID10` |
| Declaradas sin quien las ejecute, con motivo | 0 | **13** |

---

## 2. Ejecución caso por caso

### CP-001 — La regla que no lo dice se reporta, y la que sí, no

**Sobre el estándar de verdad, antes de escribir nada:**

```
$ python validadores/validar.py ejecutable
`N1` no dice quién la hace cumplir. Se escribe después del ejemplo y antes del
checklist, con una de las dos aperturas: `**Quién la hace cumplir:**` o
`**Nadie la hace cumplir:**`
... 18 hallazgos
```

**Sobre cuerpos de reglas armados:** un hallazgo cuando falta, ninguno cuando está, y con dos reglas solo se reporta la que falta. El hallazgo es de severidad **falla**, así que la corrida termina con error.

**Resultado: pasa.**

### CP-002 — «Nadie la hace cumplir», con motivo y sin él

| Entrada | Salida |
|---|---|
| `**Nadie la hace cumplir:** ningún programa ve si el usuario aprobó, porque la aprobación ocurre en el chat.` | no se reporta |
| `**Nadie la hace cumplir:** no.` | se reporta: *«declara que nadie la hace cumplir y no dice por qué»* |
| `**Nadie la hace cumplir:** es criterio.` | se reporta |

**Resultado: pasa.** El umbral del motivo está escrito con su porqué en el propio módulo: «no se puede», «es criterio» y «lo lee una persona» caben las tres por debajo, y ninguna de las tres dice nada.

### CP-003 — La pieza declarada existe

| Entrada | Salida |
|---|---|
| `` `validadores/inventado.py` `` | se reporta, **nombrando la pieza** |
| `` `validadores/marcas.py` `` (existe) | no se reporta |
| «un enganche del estándar», sin ruta | se reporta: *«no nombra la pieza»* |

**Resultado: pasa.**

### CP-004 — Los dos límites que la historia pide

- **Regla derogada:** queda fuera de la comprobación.
- **Dos piezas declaradas:** se revisan las dos; basta que una no exista para que se reporte, y el mensaje nombra la que falló.

**Resultado: pasa.**

### CP-005 — Qué se cuenta de un turno, y qué no

Los siete textos del plan dieron lo esperado. Los cuatro que **no** se cuentan —la cita, el bloque de código, la tercera persona y la palabra que contiene las letras— salieron limpios.

**Resultado: pasa.**

### CP-006 — El enganche calla cuando todo está bien

```
entrada: {"transcript_path": <una respuesta sucia>}
salida : [redacción] trato directo de `00·ID10`: usted
código : 0

entrada: {"transcript_path": <una respuesta limpia>}
salida : (nada)
código : 0

entrada: esto no es json
código : 0
```

**Resultado: pasa.** Las tres terminan en 0: medir no puede costarle el turno a nadie.

### CP-007 — Claridad y determinismo

- **`RNF-01`:** el mensaje nombra la regla, dice qué falta y dónde se escribe. Comprobado sobre el texto del hallazgo.
- **`RNF-02`:** dos corridas seguidas dan la misma lista de mensajes.
- **El umbral del largo** se compara contra `brevedad.HOLGADO`, no contra un número escrito a mano.

**Resultado: pasa.**

### CP-008 — El canal es el instalador

`hook_redaccion.py` figura en la tabla de enganches de `instalar.py`, en el evento de cierre de turno, y el archivo existe. El instalador se corrió sobre este repositorio y lo dejó puesto:

```
$ python validadores/instalar.py "c:/Ing. Jose/ia/agente" --aplicar
  · agregar enganche Stop a .claude\settings.json
```

**Resultado: pasa.**

### CP-009 — No regresión

`python validadores/validar.py internas` sobre las 650 pruebas del estándar. **Ninguna falla nueva** respecto de la línea base del día, que traía cinco rojas de archivos de otra sesión.

**Resultado: pasa.**

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| Qué se miró | Resultado |
|---|---|
| Las dieciocho declaraciones, una por una | Cada una dice lo que de verdad pasa hoy, no lo que se querría |
| El sello del checklist de las dieciocho | **No se venció ninguno.** La declaración no cambia lo que la regla exige |
| El largo del cuerpo de las dieciocho | **Ninguna reprobó la fila 10 por la línea nueva** |
| Las marcas de `00·ID8` en el capítulo `00` | **Cero marcas nuevas**, contadas contra lo guardado |
| El enganche corriendo en la sesión de verdad | Se ve al cerrar cada turno |

**Ninguna prueba tocó datos reales:** todo corrió sobre carpetas temporales y sobre el propio repositorio.

---

## 4. Defectos encontrados

| # | Qué pasó | Severidad | Dónde quedó |
|---|---|---|---|
| D-01 | La línea nueva caía **dentro del cuerpo de la regla**: ocho reglas del capítulo `00` pasaron a reprobar la fila 10 del checklist sin haber cambiado lo que exigen | Alta | Arreglado en la fase: `metareglas.py` la trata como lo que es, algo que va **después** del cuerpo |
| D-02 | La declaración **vencía el sello** del checklist, porque el comparador ve el texto hasta el checklist y ahí la línea es nueva | Alta | Arreglado en la fase, con el mismo argumento con el que ya estaba exenta la tipografía: el sello responde por lo que la regla *exige* |
| D-03 | Tres declaraciones traían raya larga como inciso, y el trinquete del `pre-commit` habría rechazado el commit | Media | Reescritas sin raya. **Contadas antes de commitear**, no después del rechazo |

**Los tres son de la misma familia:** una línea nueva dentro de un archivo de reglas la miran cuatro comprobaciones distintas, y ninguna sabía que existía.

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| CA / RNF | Evidencia | Veredicto |
|---|---|---|
| [CA-01](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#ca-01--una-regla-de-núcleo-sin-forma-de-cumplirse-se-reporta) | CP-001 · 18 reportadas antes, 0 después | **Cumple** |
| [CA-02](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#ca-02--no-se-puede-hacer-cumplir-vale-pero-con-motivo) | CP-002 | **Cumple** |
| [CA-03](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#ca-03--la-pieza-declarada-existe) | CP-003 · CP-004 | **Cumple** |
| [CA-04](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#ca-04--id9-queda-con-su-decisión-escrita) | CP-005 · CP-006 · CP-008 · la declaración escrita en `ID9` | **Cumple**, con una salvedad: el aviso a `shopnest-mesa` no se ha dado. Escribir en otro repositorio se pregunta antes (`00·N1`) |
| [RNF-01](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#5-requisitos-no-funcionales) | CP-007 | **Cumple** |
| [RNF-02](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#5-requisitos-no-funcionales) | CP-007 | **Cumple** |

## 5.1 Lo que el plan exigía

| Lo que el plan pedía | Qué pasó |
|---|---|
| Fijar el sitio de la declaración en el molde | Hecho: sección 6 de `estructura-regla.md`, con las dos aperturas y su tabla |
| La comprobación que recorre el núcleo | `validadores/ejecutable.py`, y `validar.py ejecutable` |
| Que la pieza declarada exista | Comprobado contra el disco, con la ruta desde la raíz |
| La declaración de `ID9` escrita | Hecha, y la de las otras diecisiete |
| Avisarle a `shopnest-mesa` | **No hecho**, y declarado: se pregunta antes de escribir en otro repositorio |
| Versionar | Hecho, en la entrada del registro de cambios |

---

## 6. Veredicto de la fase

**Concepto: Cumple.**

Los cuatro criterios de aceptación quedaron cumplidos con evidencia, y los dos requisitos no funcionales también. Lo que no se hizo está dicho con su nombre: el aviso al proyecto que reportó el caso, que exige escribir en un repositorio ajeno y por eso se pregunta antes.

**Lo que la fase no puede decir**, y queda escrito para que la cuenta no se lea de más: que las cinco piezas declaradas **hagan cumplir** su regla. Se comprobó que existen y que la declaración está; que ejecuten lo que la regla exige lo lee una persona.

---

## 7. Evidencias

| ID | Qué es | Dónde |
|---|---|---|
| EV-01 | 24 pruebas del validador | `validadores/tests/test_la_regla_del_nucleo_dice_quien_la_hace_cumplir.py` |
| EV-02 | 27 pruebas de la pieza de redacción y su enganche | `validadores/tests/test_lo_que_se_acaba_de_escribir_se_mide.py` |
| EV-03 | El enganche puesto por el instalador | `.claude/settings.json`, evento de cierre de turno |
| EV-04 | Las dieciocho declaraciones | [`base/00-nucleo-blindado.md`](../../../../../base/00-nucleo-blindado.md) y [`base/00-identidad-y-rol/reglas/`](../../../../../base/00-identidad-y-rol/reglas/) |
| EV-05 | La medición que abrió la fase | [`historico-chat/scripts/2026-08-31/medir-quien-hace-cumplir-el-nucleo.py`](../../../../../historico-chat/scripts/2026-08-31/medir-quien-hace-cumplir-el-nucleo.py) |
| EV-06 | El guion que escribió las dieciocho declaraciones | [`historico-chat/scripts/2026-08-31/declarar-quien-hace-cumplir-el-nucleo.py`](../../../../../historico-chat/scripts/2026-08-31/declarar-quien-hace-cumplir-el-nucleo.py) |

---

## 8. Ciclos anteriores

No hay: es el primer ciclo de la fase.
