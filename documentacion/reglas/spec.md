# Especificación del módulo Reglas  ·  `[CAPA 3]`

- **Slug del módulo:** `reglas`
- **Estado:** aprobada, el 2026-09-01 por Ing. José Dúmar Jiménez Ruíz
- **Versión del producto:** 3, según [cvds/implementacion/README.md](../../cvds/implementacion/README.md)

---

## 1. Propósito y alcance

Administrar el cuerpo de reglas desde la plataforma: numerarlas sin reutilizar ninguna, escribirlas, derogarlas, sellarlas, publicarlas y entregárselas al agente.

- **Dentro de alcance:** las seis funcionalidades de `F-005` a `F-010`.
- **Fuera de alcance:** decidir si una regla es buena, detectar contradicciones, y hacerlas cumplir, que es del módulo Comprobaciones.

## 2. Contexto — qué hay hoy

**Medido el 2026-09-01 sobre este repositorio:**

| Qué se midió | Resultado |
|---|---|
| Reglas en total | **257** |
| Vigentes | 248 |
| Derogadas | 9 |
| Capítulos con prefijo propio | 24 |
| Blindadas | 9 |

Todas se escriben editando archivos a mano, y el estándar ya sabe leerlas: las parte por capítulo, les saca el identificador, y distingue la derogada de la vigente y la blindada de la común.

## 3. Supuestos, dependencias y preguntas abiertas

- **Supuestos:** que el proyecto tiene el estándar instalado, con su lector de reglas. Si no, se dice en vez de devolver una lista vacía.
- **Dependencias:** el estándar, por el puente; Proyectos, que dice dónde vive cada uno; Auditoría, que registra lo que se escribe; Comprobaciones, cuya puerta se pide antes de publicar.
- **Preguntas abiertas:** ninguna que detenga.

## 4. Reglas de negocio

1. **Ningún identificador se reutiliza**, ni el de una regla derogada. Baja de `M11`.
2. **El siguiente identificador es el que sigue al mayor**, no el primer hueco.
3. **Nada se borra: se deroga.** La regla se queda escrita, marcada, con su texto debajo.
4. **La fuente es el texto.** Las reglas viven en archivos; la base no guarda su contenido.
5. **Antes de guardar se muestran las que se parecen**, y se dice que eso no detecta contradicciones.
6. **Una regla blindada no se deroga desde acá.** Sostienen a las demás.
7. **Escribir queda registrado en la auditoría.**

## 5. Modelo de datos

- **Entidades:** ninguna. El cuerpo de reglas **es** el conjunto de archivos, y se lee al pedirlo.
- **Valores configurables:** dónde vive `validadores/`, que ya lo declara la configuración.
- **Migración:** no aplica.

### 5.1 Por qué el siguiente es el que sigue al mayor

**Un hueco no se puede interpretar desde acá.** Puede ser una regla que se derogó y se movió de archivo, o una que nunca existió, o una numeración que empezó en otro sitio. Rellenar huecos es **la única forma de reutilizar un número sin darse cuenta**, así que no se rellenan.

Los huecos se pueden mirar, para revisar el cuerpo de reglas. Lo que se mira ahí es justamente lo que la asignación no va a entregar nunca.

### 5.2 Qué hace y qué no hace la lista de reglas parecidas

**Hace:** poner al lado las reglas vigentes que comparten palabras significativas con el título que se va a escribir, dando más peso a las del mismo capítulo.

**No hace:** decir si se contradicen. Dos reglas se contradicen por lo que significan, y eso no se saca contando palabras.

**Y por qué importa la diferencia.** Llamarlo detector de contradicciones sería peor que no tenerlo: **quien confía en un detector deja de mirar**, y las que se le escapan pasan sin que nadie las revise. Por eso el aviso lo dice cada vez, incluso cuando no encuentra nada.

## 6. Comportamiento y flujos

**Pedir el siguiente identificador.** Se recibe el prefijo del capítulo. Se leen los que ya existen, **contando las derogadas**, y se devuelve el que sigue al mayor.

**Escribir una regla.** Se recibe el capítulo, el prefijo y el título.

- Primero se muestran las reglas vigentes que hablan de lo mismo, **y no se escribe nada**.
- Solo si se pide expresamente, se asigna el identificador, se comprueba que esté libre y se escribe el archivo con el formato canónico.
- **La regla nace con sus huecos puestos:** el cuerpo y el ejemplo salen con la marca de espacio por llenar. Se ve que falta algo, y el módulo Ciclo de vida puede llenarlo.

**Derogar una regla.** Se recibe cuál, en qué versión deja de regir, a qué mirar en su lugar y por qué.

- Se le pone la marca en el encabezado y el aviso debajo. **El texto original se conserva.**
- Su identificador queda ocupado para siempre.
- Una regla que no existe, una ya derogada y **una blindada** se responden diciendo por qué no.

## 7. Interfaz

Sin pantalla en esta versión. Se pide por orden de consola, como el resto de los módulos de esta etapa.

## 8. Permisos y autorización

Un solo usuario, sin credenciales propias.

## 9. Marco normativo

**Escribe en el repositorio del usuario**, como el módulo Ciclo de vida. Lo que lo hace seguro es lo mismo: queda registrado, y nada se borra.

## 10. Plan de pruebas

| Qué se prueba | Casos |
|---|---|
| Leer el cuerpo | Con vigentes y derogadas · sin lector del estándar |
| El siguiente identificador | Con reglas · sin ninguna · con huecos |
| Que NO pase | Reutilizar un identificador · rellenar un hueco · borrar al derogar |
| Escribir | El formato canónico, y los huecos puestos |
| Derogar | Legible, marcada, y con su porqué |
| Las parecidas | Que encuentre, que no invente, y **que diga lo que no puede decir** |

## 11. Criterios de aceptación

- `CA-1` Una regla nueva recibe el siguiente identificador libre.
- `CA-2` El identificador de una derogada no se reasigna.
- `CA-3` No se puede guardar con un identificador ya usado.
- `CA-4` Una regla nueva queda guardada con su identificador y su molde.
- `CA-5` Derogar deja la regla legible y marcada.
- `CA-6` Antes de guardar se muestran las que hablan de lo mismo.

Los tres primeros son de `F-006`; los tres siguientes, de `F-005`. Los de `F-007` a `F-010` se agregan cuando lleguen sus historias.

## 12. Decisiones tomadas

| Decisión | Alternativa descartada | Por qué |
|---|---|---|
| **El lector de reglas se usa por un puente** | Escribir uno propio | Dos lectores se separan, y el día que el formato cambie uno va a leer mal sin avisar |
| **El siguiente es el que sigue al mayor** | El primer hueco libre | Rellenar huecos es la única forma de reutilizar un número sin darse cuenta |
| **Las derogadas cuentan para la numeración** | Contar solo las vigentes | Su identificador sigue citado en documentos escritos hace años |
| **Se muestran las parecidas, y se dice que no detecta contradicciones** | Llamarlo detector | Quien confía en un detector deja de mirar |
| **La regla nace con sus huecos puestos** | Nacer vacía | Una regla incompleta que no se nota se publica incompleta |
| **Una blindada no se deroga desde acá** | Dejarlo pasar | Sostienen a las demás, y derogarlas por una orden de consola es demasiado fácil |
| **La fuente es el archivo** | Guardar la regla en la base | El texto pasaría a ser una copia, y se queda vieja al primer cambio a mano |

## 13. Trazabilidad

| Funcionalidad | Requisito | Historia | Fase que lo construye |
|---|---|---|---|
| F-006 | RF-06 | [HU-001 Dar el identificador sin reutilizar ninguno](../epicas/EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/HU-001-dar-el-identificador-sin-reutilizar-ninguno/HU-001-dar-el-identificador-sin-reutilizar-ninguno.md) | [G-EP-016-HU-001-ningun-numero-se-reutiliza](../epicas/EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/HU-001-dar-el-identificador-sin-reutilizar-ninguno/G-EP-016-HU-001-ningun-numero-se-reutiliza/estado-fase.md), cerrada el 2026-09-01 |
| F-005 | RF-05 | [HU-002 Escribir, corregir y derogar una regla](../epicas/EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/HU-002-escribir-corregir-y-derogar-una-regla/HU-002-escribir-corregir-y-derogar-una-regla.md) | [H-EP-016-HU-002-derogar-marca-y-no-borra](../epicas/EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/HU-002-escribir-corregir-y-derogar-una-regla/H-EP-016-HU-002-derogar-marca-y-no-borra/estado-fase.md), cerrada el 2026-09-01 |
| F-007 | RF-07 | Por escribir | — |
| F-008 | RF-08 | Por escribir | — |
| F-009 | RF-09 | Por escribir | — |
| F-010 | RF-10 | Por escribir | — |

## 14. Cruces con otros módulos

- **El estándar:** aporta el lector de reglas. Este módulo **no sabe** cómo está escrita una regla por dentro.
- **Proyectos:** dice dónde vive cada proyecto.
- **Auditoría:** registra lo que se escribe y lo que se deroga.
- **Ciclo de vida:** puede llenar los huecos con que nace una regla.
- **Comprobaciones:** su puerta se pide antes de publicar una versión.

---

## 15. Cambios después de aprobada

| Fecha | Qué cambió | Por qué | Aprobado por |
|---|---|---|---|
| — | — | — | — |
