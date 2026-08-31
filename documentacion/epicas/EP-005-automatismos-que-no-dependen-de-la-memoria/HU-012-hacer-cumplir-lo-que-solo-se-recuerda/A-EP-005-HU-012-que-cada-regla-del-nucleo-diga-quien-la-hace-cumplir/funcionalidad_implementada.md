# Funcionalidad implementada — Fase `A-EP-005-HU-012-que-cada-regla-del-nucleo-diga-quien-la-hace-cumplir` (módulo Automatismos — enganches)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué quedó hecho** al cerrar la fase, y por dónde se usa. Lo que se pidió está en la [HU-012](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md); lo que se planeó, en el [plan_trabajo.md](plan_trabajo.md); lo que se ejecutó, en el [resultado_pruebas.md](resultado_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-005-HU-012-que-cada-regla-del-nucleo-diga-quien-la-hace-cumplir` |
| **Épica / HU** | [EP-005](../../epica.md) · [HU-012](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md) |
| **Módulo** | Automatismos — enganches |
| **Fecha de cierre** | 2026-08-31 |
| **Versión del estándar** | La que registra el [CHANGELOG.md](../../../../../CHANGELOG.md) para esta fase |

---

## 1. Qué se implementó — resumen

**Ninguna regla del núcleo puede publicarse sin decir quién la hace cumplir.** Antes, dieciocho no lo decían y catorce no tenían quién las ejecutara; hoy las dieciocho lo dicen, cinco nombran su pieza y trece declaran, con su motivo, que no la tienen.

Y para las tres reglas que hablan de **cómo escribe el agente** —las marcas de `00·ID8`, el largo de `00·ID9` y el trato de `00·ID10`— se construyó lo que faltaba: una pieza que mide el turno **sobre lo que se acaba de escribir**, y un enganche que lo deja a la vista al cerrarlo. Mide y no detiene: cuando corre, el texto ya salió.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| CA | Qué lo cumple | Dónde | Evidencia |
|---|---|---|---|
| [CA-01](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#ca-01--una-regla-de-núcleo-sin-forma-de-cumplirse-se-reporta) | La comprobación que recorre el capítulo `00` | `validadores/ejecutable.py` · `validar.py ejecutable` | 8 pruebas |
| [CA-02](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#ca-02--no-se-puede-hacer-cumplir-vale-pero-con-motivo) | El motivo se exige, con umbral escrito | `ejecutable.MOTIVO_MINIMO` | 4 pruebas |
| [CA-03](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#ca-03--la-pieza-declarada-existe) | La pieza se resuelve contra el disco | `ejecutable.piezas` | 5 pruebas |
| [CA-04](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#ca-04--id9-queda-con-su-decisión-escrita) | La declaración de `ID9`, y la pieza que la mide | `base/00-identidad-y-rol/reglas/ID9-*.md` · `validadores/redaccion.py` · `adaptadores/claude-code/hook_redaccion.py` | 27 pruebas |
| [RNF-01](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#5-requisitos-no-funcionales) | El mensaje dice qué falta y dónde se escribe | `ejecutable.DONDE` | 1 prueba |
| [RNF-02](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#5-requisitos-no-funcionales) | Dos corridas dan la misma lista | — | 1 prueba |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué se hizo de verdad |
|---|---|
| T-01 | Sección 6 de `estructura-regla.md`: dónde va la declaración, las dos aperturas, y qué lleva cada una |
| T-02 · T-03 | `ejecutable.py`, su subcomando, y su entrada en la corrida completa y en el `pre-push` |
| T-05 · T-07 | El motivo con largo mínimo, y la pieza resuelta por su ruta desde la raíz |
| T-09 · T-10 · T-11 | `redaccion.py`, `hook_redaccion.py`, y el enganche declarado en el instalador |
| T-12 | Las dieciocho declaraciones, escritas con un guion para que quedaran iguales |
| T-13 | El catálogo de reglas validables, al día |
| T-04 · T-06 · T-08 · T-14 | 51 pruebas nuevas en dos archivos |
| T-15 · T-16 · T-17 | Claridad, determinismo, versión y registro |
| **Fuera del plan** | `metareglas.py`: la línea nueva le caía dentro del cuerpo de la regla. Declarado en §2.1 del plan al descubrirlo (`02·F8`) |

---

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| Suite | Resultado |
|---|---|
| `validadores/tests/test_la_regla_del_nucleo_dice_quien_la_hace_cumplir.py` | 24 pruebas, en verde |
| `validadores/tests/test_lo_que_se_acaba_de_escribir_se_mide.py` | 27 pruebas, en verde |
| La batería interna completa (`validar.py internas`) | Sin fallas nuevas respecto de la línea base del día |
| `validar.py metareglas` · `estandar` · `marcas` · `amarre` · `ejecutable` | En verde |

**Lo que las pruebas no dicen**, escrito para que la corrida en verde no se lea de más: que la pieza declarada **haga cumplir** su regla. Se ve que existe y que la declaración está; que ejecute lo que la regla exige lo lee una persona.

---

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

```
python validadores/validar.py ejecutable      # qué regla del núcleo lo dice, y cuál no
```

Y sin pedirlo:

- **Al cerrar cada turno**, el enganche mide lo que el agente acaba de escribir y lo dice **solo si hay algo que decir**.
- **Antes de publicar**, el `pre-push` corre la comprobación y **detiene** el envío si una regla del núcleo no lo declara.

**Al escribir una regla nueva del capítulo `00`**, la declaración se escribe después del ejemplo y antes del checklist, con una de las dos aperturas. El molde lo explica en su sección 6.

---

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué |
|---|---|
| La declaración vive **en la regla**, no en un catálogo aparte | Donde se lee la exigencia está la respuesta, y un catálogo en prosa no se lee igual dos veces |
| **Dos aperturas exactas**, y ninguna más | Un campo libre admitiría «pendiente», que es la respuesta que la historia viene a impedir |
| «Nadie» **exige motivo** | Una casilla marcada sin motivo no es una decisión |
| El enganche **mide y no detiene** | Cuando corre, el texto ya salió. Devolverlo le costaría al usuario leer la versión larga primero y la corta después |
| El umbral del largo sale de `brevedad.HOLGADO` | Dos umbrales que empiezan iguales se separan sin que nadie lo note (`S-091`) |
| El trato directo se cuenta; la variedad del idioma **no** | Contar lo que exige leer sería un número que el lector completa con lo que quiere creer |
| Las declaraciones se escribieron **con un guion** | Dieciocho reglas en diez archivos, con la misma línea en el mismo sitio, es donde una edición a mano deja una distinta |

Señales registradas: [`S-093`](../../../../senales.md) y [`S-094`](../../../../senales.md).

---

## 6. Deuda técnica y pendientes generados

- **El aviso a `shopnest-mesa`**, que reportó el caso y tiene su pendiente 22 abierto. Escribir en otro repositorio se pregunta antes (`00·N1`); queda dicho en el `estado-fase.md` §3.
- **Trece reglas del núcleo siguen sin quien las ejecute**, y eso no es deuda escondida: está declarado en cada una, con su motivo. La que se pueda hacer cumplir el día que aparezca la forma, se cambia de declaración.
- **La comprobación no llega fuera del capítulo `00`.** Es el alcance que la historia fijó, y se extiende si el caso aparece afuera.

---

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

| Documento | Qué se le agregó |
|---|---|
| [`anatomia/que-esta-amarrado-a-la-herramienta.md`](../../../../../anatomia/que-esta-amarrado-a-la-herramienta.md) | Las tres piezas nuevas, con su clasificación |
| [`validadores/reglas-validables.md`](../../../../../validadores/reglas-validables.md) | Que `ID8`, `ID9` e `ID10` ya tienen quien las mida |
| [`base/20-meta-reglas/estructura-regla.md`](../../../../../base/20-meta-reglas/estructura-regla.md) | La sección 6 y la fila del cierre |
| [`documentacion/senales.md`](../../../../senales.md) | `S-093` y `S-094` |
| [`CHANGELOG.md`](../../../../../CHANGELOG.md) · [`VERSION`](../../../../../VERSION) | La entrada de esta fase |

---

## 8. Despliegue — si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

No aplica: el estándar no se despliega. **Lo que sí llega a los proyectos** es el enganche nuevo, la próxima vez que corran el instalador. Como mide sin detener, no puede romperle una sesión a nadie.
