# Pendiente · El estándar depende de una sola herramienta

**Estado:** cerrado el 2026-08-19 · anotado 2026-08-13.

| | |
|---|---|
| **Historia de usuario** | [EP-005 · HU-011 — Dónde termina el estándar y dónde empieza el adaptador](../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-011-donde-termina-el-estandar/HU-011-donde-termina-el-estandar.md) — lo que está amarrado a la herramienta son los automatismos, que es de lo que trata la épica |

Marcar dónde termina el estándar y dónde empieza el adaptador de Claude Code, y dejar el adaptador en un solo lugar, para que el día que la herramienta cambie no se caiga todo lo demás.

## El problema

Las reglas de [`base/`](../../base) son texto y sirven en cualquier parte. Lo que las hace cumplir no.

- Cinco de los validadores son enganches de Claude Code: `hook_md.py`, `hook_checklist.py`, `hook_sesion.py`, `hook_recuerdos.py` y `hook_historico.py`.
- [`instalar.py`](../../validadores/instalar.py) escribe esos enganches en `.claude/settings.json`.
- [`cargador.py`](../../validadores/cargador.py) arma el texto que se le entrega al agente en el formato que espera esa herramienta, y el archivo de entrada se llama `CLAUDE.md`.
- La carpeta [`skills/`](../../skills) es un formato de esa herramienta.
- El histórico de sesiones y la memoria del agente se llenan porque un enganche de esa herramienta los dispara.

Si mañana el usuario trabaja con otro agente, lo que sobrevive son las reglas escritas. Se pierde todo lo que las hace cumplir solas, que es justo lo que el repo lleva meses construyendo. Y el estándar no se daría cuenta: no hay ningún archivo que diga cuáles piezas están amarradas y cuáles no.

Hay una ironía que vale nombrar. El estándar le exige esto mismo a los proyectos que lo heredan: el capítulo [`10 · Dependencias de terceros`](../../base/10-dependencias.md) manda cuidar de qué se depende, y el [`11 · Configuración y entornos`](../../base/11-configuracion-entornos.md) manda separar lo de cada máquina de lo que va en el repositorio. El estándar no se lo aplica a sí mismo.

## De dónde sale

De los apuntes del diplomado, módulo 2:

- La nota de los cuatro componentes de la IA pone la **dependencia del proveedor** como el riesgo propio del componente de cómputo, al lado del costo y de dónde queda alojado el dato.
- La diapositiva del ecosistema de la IA muestra cientos de proveedores por casilla y casi todos son empresas jóvenes. La lectura de esa lámina fue: el riesgo ahí es de proveedor, no de tecnología.

## Qué habría que construir

**1. ~~El mapa.~~ · HECHO el 2026-08-18** → [`anatomia/que-esta-amarrado-a-la-herramienta.md`](../../anatomia/que-esta-amarrado-a-la-herramienta.md). **18 de 53 validadores amarrados, 35 libres**, y el amarre de verdad son los ocho `hook_*` más `instalar.py`, que los enchufa. Lo que no se buscaba: **`base/` nombra la herramienta 26 veces**, catorce solo en `01-conducta.md`. Casi todas son `CLAUDE.md` —un nombre de archivo, no la máquina de atrás—, así que el amarre de lo que se hereda es superficial; pero `20·M3` se incumple diez veces y nadie lo reporta, porque el validador de tecnología busca lenguajes y frameworks, no herramientas de agente.

~~**1. El mapa.**~~ Una tabla en [`anatomia/`](../../anatomia) con las piezas del repo en tres columnas: la que sirve con cualquier agente, la que es adaptador de Claude Code, y la que es de la máquina. Se hace leyendo, una vez.

**2. El adaptador en un solo sitio.** Hoy la dependencia está repartida entre los cinco `hook_*.py` y `instalar.py`. Recogerla en una capa con un nombre propio (`adaptadores/claude-code/`, por decir algo) hace visible el tamaño real del amarre, que hoy nadie sabe cuál es.

**3. El contrato.** Escribir qué necesita el estándar de cualquier agente para funcionar: que se pueda inyectar texto al arranque, que se pueda correr un guion después de escribir un archivo, y que se pueda cortar un commit. Con eso escrito, soportar otro agente es llenar un formulario en vez de empezar de cero.

## Qué no propone

Soportar hoy un segundo agente. Eso es trabajo grande y sin nadie que lo pida, y construirlo antes de necesitarlo produce una capa de abstracción diseñada contra un solo caso, que es la peor clase de capa. Lo que sí conviene ahora es **saber cuánto costaría**, y hoy ni eso se sabe.

## Prioridad

Baja mientras la herramienta no cambie, y ese es el punto: cuando cambie, ya será tarde para averiguarlo. El mapa del punto 1 es de una tarde y deja el resto decidible.


---

# Estado — 2026-08-18: el punto 1 hecho, con su comprobación

**Sigue abierto**, y lo que falta son los puntos 2 y 3.

| Punto | Estado |
|---|---|
| **1 · El mapa** | ✅ **Hecho** — [`anatomia/que-esta-amarrado-a-la-herramienta.md`](../../anatomia/que-esta-amarrado-a-la-herramienta.md), y **no envejece en silencio**: `validar.py amarre` lo comprueba |
| **2 · El adaptador en un solo sitio** | ☐ abierto |
| **3 · El contrato** | ☐ abierto |

**54 piezas: 18 amarradas, 36 libres.** El adaptador de verdad son los ocho `hook_*` más `instalar.py`, que los enchufa.

## Por qué los puntos 2 y 3 no se hicieron

**No los cubre ningún criterio de [EP-005 · HU-011](../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-011-donde-termina-el-estandar/HU-011-donde-termina-el-estandar.md)**, que son: toda pieza tiene su columna, cada amarrada dice qué se pierde, y el mapa se queda viejo y se nota. Los tres hablan **del mapa**, no de mover código ni de escribir un contrato.

Por [`02·F19`](../../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md) el criterio **es** la especificación, así que hacen falta criterios nuevos o una historia propia — **la misma situación del [16](../16-primero-que-el-proceso-sirva-despues-se-automatiza.md) y del punto 2 del [33](../33-defectos-que-destaparon-los-resumenes-viejos.md)**, y es decisión del usuario.

## Lo que el mapa destapó y no estaba en el pendiente

**`base/` nombra la herramienta 26 veces**, catorce solo en `01-conducta.md`, y `base/` es lo que se hereda y lo que `20·M3` declara agnóstico. Casi todas son `CLAUDE.md` —un nombre de archivo—, así que el amarre es superficial; pero **`M3` se incumple diez veces y nadie lo reporta**, porque el validador de tecnología busca lenguajes y frameworks, no herramientas de agente.

---

# Cerrado — 2026-08-19: los puntos 2 y 3

| Punto | Estado |
|---|---|
| **1 · El mapa** | ✅ 2026-08-18 — [`anatomia/que-esta-amarrado-a-la-herramienta.md`](../../anatomia/que-esta-amarrado-a-la-herramienta.md), comprobado por `validar.py amarre` |
| **2 · El adaptador en un solo sitio** | ✅ [`adaptadores/claude-code/`](../../adaptadores/claude-code) |
| **3 · El contrato** | ✅ [`adaptadores/contrato.md`](../../adaptadores/contrato.md) |

## Primero los dos criterios que faltaban

**Ninguno de los tres de [EP-005 · HU-011](../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-011-donde-termina-el-estandar/HU-011-donde-termina-el-estandar.md) cubría esto**, y estaba escrito arriba desde ayer: los tres hablan **del mapa**, no de mover código ni de escribir un contrato. Se escribieron el `CA-04` y el `CA-05`, y de ahí salió el trabajo.

Es el mismo eslabón que faltaba en el [14](las-reglas-no-tienen-fecha-de-revision.md), y por el mismo motivo: **un pendiente puede estar bien enrutado a su historia y aun así no tener de dónde colgarse.**

## La frontera

> **`validadores/` es lo que sirve con cualquier agente. `adaptadores/` es lo que existe porque una herramienta concreta lo llama.**

Los ocho `hook_*` se mudaron. `instalar.py` los enchufa desde la ruta nueva, y una prueba fija que **no vuelva a aparecer uno en `validadores/`** — porque ahí no rompe nada hoy, y ese es exactamente el problema: el amarre volvería a crecer sin que nadie lo note.

## El recuento no bajó, y era el riesgo

**Mirando solo `validadores/`, el mapa habría dicho «10 amarrados de 51» y habría sonado a mejora.** Lo único que hubo fue una mudanza. `amarre.py` ahora mira las dos carpetas y sigue diciendo **18 de 59**.

> Un mapa que mejora solo porque el código se movió es un mapa que miente. Hay una prueba para eso.

## Qué se rompió al mover, y cómo se supo

**Nada quedó en silencio, y eso se comprobó antes de mover.** `checklist.py` compara el comando exacto del enganche instalado: un proyecto con la ruta vieja lo reporta en el primer mensaje de la siguiente sesión.

Lo que sí apareció al correr las pruebas:

- **Los enganches importaban por vecindad.** Siete resolvían sus módulos con «la carpeta donde estoy»; `hook_relacionadas.py` ni siquiera lo decía —funcionaba porque estaba al lado—. Ahora los ocho dicen dónde está lo agnóstico, que es lo que siempre debieron decir.
- **`hook_resumen.py` contaba dos niveles para llegar a la raíz y ahora son tres.** Contar mal no revienta: apunta a una carpeta que existe y el enganche **deja de escribir sin avisar**. Lo cazó la prueba que lo corre por el camino real.
- **Once referencias en las dos baterías** apuntaban a la ubicación vieja.

## Lo que sigue sin hacerse, a propósito

**Soportar hoy un segundo agente.** Construir la abstracción antes de tener el segundo caso produce una capa diseñada contra uno solo, que es la peor clase de capa. Lo que hacía falta era **saber cuánto costaría**, y ahora está escrito: ocho programas a reescribir, cincuenta y uno que se quedan, ninguna regla que tocar.

## Lo que este pendiente destapó y sigue abierto

**`base/` nombra la herramienta 26 veces** y `20·M3` la declara agnóstica. Casi todas son un nombre de archivo, así que el amarre es superficial — pero **`M3` se incumple diez veces y nadie lo reporta**, porque el detector de tecnología busca lenguajes y frameworks, no herramientas de agente.

Va anotado en el [pendiente 19](../19-el-capitulo-20-no-se-cumple-a-si-mismo.md), que es el que lleva la cuenta de lo que el capítulo 20 no se cumple a sí mismo.
