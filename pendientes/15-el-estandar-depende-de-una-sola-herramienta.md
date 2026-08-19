# Pendiente · El estándar depende de una sola herramienta

**Estado:** abierto · anotado 2026-08-13.

| | |
|---|---|
| **Historia de usuario** | [EP-005 · HU-011 — Dónde termina el estándar y dónde empieza el adaptador](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-011-donde-termina-el-estandar/HU-011-donde-termina-el-estandar.md) — lo que está amarrado a la herramienta son los automatismos, que es de lo que trata la épica |

Marcar dónde termina el estándar y dónde empieza el adaptador de Claude Code, y dejar el adaptador en un solo lugar, para que el día que la herramienta cambie no se caiga todo lo demás.

## El problema

Las reglas de [`base/`](../base/) son texto y sirven en cualquier parte. Lo que las hace cumplir no.

- Cinco de los validadores son enganches de Claude Code: `hook_md.py`, `hook_checklist.py`, `hook_sesion.py`, `hook_recuerdos.py` y `hook_historico.py`.
- [`instalar.py`](../validadores/instalar.py) escribe esos enganches en `.claude/settings.json`.
- [`cargador.py`](../validadores/cargador.py) arma el texto que se le entrega al agente en el formato que espera esa herramienta, y el archivo de entrada se llama `CLAUDE.md`.
- La carpeta [`skills/`](../skills/) es un formato de esa herramienta.
- El histórico de sesiones y la memoria del agente se llenan porque un enganche de esa herramienta los dispara.

Si mañana el usuario trabaja con otro agente, lo que sobrevive son las reglas escritas. Se pierde todo lo que las hace cumplir solas, que es justo lo que el repo lleva meses construyendo. Y el estándar no se daría cuenta: no hay ningún archivo que diga cuáles piezas están amarradas y cuáles no.

Hay una ironía que vale nombrar. El estándar le exige esto mismo a los proyectos que lo heredan: el capítulo [`10 · Dependencias de terceros`](../base/10-dependencias.md) manda cuidar de qué se depende, y el [`11 · Configuración y entornos`](../base/11-configuracion-entornos.md) manda separar lo de cada máquina de lo que va en el repositorio. El estándar no se lo aplica a sí mismo.

## De dónde sale

De los apuntes del diplomado, módulo 2:

- La nota de los cuatro componentes de la IA pone la **dependencia del proveedor** como el riesgo propio del componente de cómputo, al lado del costo y de dónde queda alojado el dato.
- La diapositiva del ecosistema de la IA muestra cientos de proveedores por casilla y casi todos son empresas jóvenes. La lectura de esa lámina fue: el riesgo ahí es de proveedor, no de tecnología.

## Qué habría que construir

**1. ~~El mapa.~~ · HECHO el 2026-08-18** → [`anatomia/que-esta-amarrado-a-la-herramienta.md`](../anatomia/que-esta-amarrado-a-la-herramienta.md). **18 de 53 validadores amarrados, 35 libres**, y el amarre de verdad son los ocho `hook_*` más `instalar.py`, que los enchufa. Lo que no se buscaba: **`base/` nombra la herramienta 26 veces**, catorce solo en `01-conducta.md`. Casi todas son `CLAUDE.md` —un nombre de archivo, no la máquina de atrás—, así que el amarre de lo que se hereda es superficial; pero `20·M3` se incumple diez veces y nadie lo reporta, porque el validador de tecnología busca lenguajes y frameworks, no herramientas de agente.

~~**1. El mapa.**~~ Una tabla en [`anatomia/`](../anatomia/) con las piezas del repo en tres columnas: la que sirve con cualquier agente, la que es adaptador de Claude Code, y la que es de la máquina. Se hace leyendo, una vez.

**2. El adaptador en un solo sitio.** Hoy la dependencia está repartida entre los cinco `hook_*.py` y `instalar.py`. Recogerla en una capa con un nombre propio (`adaptadores/claude-code/`, por decir algo) hace visible el tamaño real del amarre, que hoy nadie sabe cuál es.

**3. El contrato.** Escribir qué necesita el estándar de cualquier agente para funcionar: que se pueda inyectar texto al arranque, que se pueda correr un guion después de escribir un archivo, y que se pueda cortar un commit. Con eso escrito, soportar otro agente es llenar un formulario en vez de empezar de cero.

## Qué no propone

Soportar hoy un segundo agente. Eso es trabajo grande y sin nadie que lo pida, y construirlo antes de necesitarlo produce una capa de abstracción diseñada contra un solo caso, que es la peor clase de capa. Lo que sí conviene ahora es **saber cuánto costaría**, y hoy ni eso se sabe.

## Prioridad

Baja mientras la herramienta no cambie, y ese es el punto: cuando cambie, ya será tarde para averiguarlo. El mapa del punto 1 es de una tarde y deja el resto decidible.
