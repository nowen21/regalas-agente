# Pendiente · Cada tarea sabe qué reglas le aplican

**Estado:** **hecho** el 2026-09-28, en la misma sesión que lo anotó. Lo construyó HU-023 de EP-005 en dos fases: la `A` dejó la lista, la línea en el núcleo y el programa del mapa (39.2.0); la `B`, las 252 reglas con sus tareas, el validador, la corrección del amarre y el recuperador por tareas conectado en el estándar (39.3.0).

| | |
|---|---|
| **Historia de usuario** | [EP-005 · HU-023](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-023-cada-tarea-sabe-que-reglas-le-aplican/HU-023-cada-tarea-sabe-que-reglas-le-aplican.md). Va en EP-005 y no por la historia dueña de cada capítulo porque anota las reglas de todos a la vez, como `EP-005·HU-012` |
| **De dónde sale** | [H-7 de la sesión del 2026-09-28](../historico-chat/resumenes/2026-09-28/sesion.md), sobre por qué el agente olvida las reglas |
| **Proyecto de origen** | El estándar mismo |

## El problema

No hay un mapa que lleve de una tarea a las reglas que le aplican.

El 2026-09-28 el usuario decidió que el agente no cargue las reglas al arrancar, sino que antes de cada tarea identifique y lea las que le corresponden: *«Lo importante es que tenga claro que existen reglas que debe cumplir y que, antes de realizar una tarea, debe identificar y consultar las que correspondan a lo que está haciendo»*. Para eso el agente tiene que poder ir de «voy a escribir un documento» o «llegó un pedido» a las reglas que tocan. Hoy los índices de `base/` están ordenados por capítulo, y para encontrar una regla hay que saber de antemano en qué capítulo está.

El antecedente más cercano es [validadores/reglas-antes-de-la-accion.md](../validadores/reglas-antes-de-la-accion.md), del 2026-09-16. Clasifica las reglas por **cuándo** se pueden comprobar (antes de la acción, sobre el texto, al guardar, o por criterio), no por **a qué tarea** aplican. Lo generó un guion de una sola vez y cuenta 248 reglas; `metareglas.py` cuenta hoy 261.

## Por qué importa

Sin el mapa, la instrucción de arranque que decidió el usuario dice «busca las reglas que aplican» y no dice dónde. Y el enganche que le muestre al agente la regla en el momento de actuar no sabe cuál mostrar. Es la pieza que une las dos.

Un mapa escrito a mano envejece: hoy fallan 4 pruebas porque al mapa del amarre nadie le agregó `validadores/recuperar.py`, que entró el 2026-09-16.

## Qué falta

1. **Una lista cerrada de tareas**, como la de las palabras clave: recibir un pedido, escribir un documento, cambiar código, hacer un commit, y las que salgan de revisar las reglas. Sin lista cerrada, cada regla nombra la tarea a su manera y el mapa no agrupa nada.
2. **Que cada regla declare a qué tareas aplica**, con una línea en su propio texto.
3. **Un programa que arme el mapa** leyendo esas líneas, y lo deje en `base/mapa-de-tareas.md`, con el enlace a cada regla.
4. **Un validador** que falle si una regla vigente no declara sus tareas, si nombra una tarea fuera de la lista o si el mapa quedó viejo.

Hay dos salidas para el punto 3:

- **Generar el mapa desde las reglas.** Cada regla dice lo suyo y el mapa sale solo. Cuesta tocar las 252 reglas vigentes una vez, pero no envejece.
- **Escribir el mapa a mano.** Es más rápido de arrancar y envejece como el del amarre.

Conviene generarlo.

## El límite

No cubre la instrucción que el agente recibe al arrancar la sesión (H-1) ni el enganche que le muestra la regla en el momento de actuar (H-4 y H-5). Esos dos usan el mapa; este pendiente solo lo construye.

## Cómo se sabrá que cerró

- La lista de tareas existe, cerrada, en `base/`.
- Toda regla vigente declara sus tareas, y `base/mapa-de-tareas.md` sale del programa.
- El validador falla con una regla sin tareas, con una tarea fuera de la lista y con el mapa viejo, y pasa con el repositorio como queda.
- `python validadores/validar.py estandar` y `python validadores/validar.py metareglas` terminan sin fallas.
