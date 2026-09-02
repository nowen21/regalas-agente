# Resultado de Pruebas — Fase `A-EP-013-HU-001-los-huecos-de-un-documento-se-ven`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué resultado y si cada criterio quedó cumplido**. Los casos están en el [plan_pruebas.md](plan_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-013-HU-001-los-huecos-de-un-documento-se-ven` |
| **HU** | [HU-001 Ver qué le falta a un documento](../HU-001-ver-que-le-falta-a-un-documento.md) |
| **Fecha de ejecución** | 2026-09-01 |
| **Ejecutó** | El agente, sobre los documentos traídos de este repositorio |
| **Ciclo** | 1 |

---

## 1. Resumen de la ejecución

| | Cuántos |
|---|---|
| Casos del plan | 6 |
| Ejecutados | 6 |
| Pasaron | 6 |
| Fallaron | 0 |
| Pruebas automáticas nuevas | **26** |

**Los documentos de este repositorio, medidos:**

| | Cuánto |
|---|---|
| Documentos traídos | 1 002 |
| **Con espacios por llenar** | **54** |
| Espacios por llenar en total | **77** |
| Marcas con nombre que entraron en la cuenta | **0** |
| Tipos sin molde, dichos como tales | 2 |
| Dependencias nuevas | **0** |

---

## 2. Ejecución caso por caso

### CP-001 — Se dice qué molde sigue el documento

Los tipos del ciclo dan su molde numerado. **Los tres que viven fuera de la carpeta del ciclo** dan el suyo: señales, decisiones de arquitectura y la etapa, que además depende de dónde está el archivo y no de su nombre, porque las siete se llaman `README.md`.

Los dos que no tienen molde, el índice y el registro de versión, salen como reconocidos y sin molde, con el porqué escrito.

**Resultado: pasa.**

### CP-002 — Se listan los huecos, con cuántos son y dónde

| Entrada | Salió |
|---|---|
| Tres huecos en líneas distintas | Tres, con su línea |
| Dos en la misma línea | Dos, en columnas distintas |
| Uno dentro de un bloque cercado | **No se cuenta** |
| Un documento sin huecos | Lo dice |

Cada hueco trae **el texto que lo rodea**, no solo su posición. La `HU-002` va a escribir ahí, y un número de línea solo no dice si el documento se movió.

**Resultado: pasa.**

### CP-003 — Solo el hueco cierto entra en la cuenta

**El caso que la medición cambió antes de construir.**

Un documento con un `«…»` y una marca del molde da **uno**: el de nombre sale en la lista de posibles. Y una cita del autor que no está en el molde **ni se cuenta ni se lista**: no es un hueco de ninguna clase.

**Sobre los documentos reales: ninguna marca con nombre entró en la cuenta.** De las 341 marcas de las 130 historias, 75 están en el molde y ninguna sigue en la línea del molde: son etiquetas del autor.

**Resultado: pasa.**

### CP-004 — Lo que llena la instalación no se cuenta como pendiente

`«RUTA-ESTANDAR»` no entra en la cuenta del usuario **y aparece en la suya**, con su número. Un documento cuyas únicas marcas son de instalación sale **completo**, y con sus dos marcas dichas aparte.

**Resultado: pasa.**

### CP-005 — Un documento de tipo desconocido lo dice

Un documento sin tipo se responde diciéndolo, y no recibe molde. Un tipo inventado tampoco recibe el del más parecido.

**Y se distinguen tres cosas que se confundían en una:** que no se le conoce el tipo, que el tipo no tiene molde escrito, y que el molde existe y no se pudo leer. La primera se arregla enseñándole el tipo a Importación; la segunda, escribiendo el molde. Confundirlas esconde la que sí tiene arreglo.

**Resultado: pasa.**

### CP-006 — Mirar no modifica nada

Contenido y fecha de modificación, comparados antes y después. **Ninguno cambia.**

**Resultado: pasa.**

---

## 3. La comparación con el expediente  ·  el bloqueo `B-03` del plan

El plan exigía correr las dos cuentas y explicar la diferencia con números. Se corrieron:

| Cuenta | Documentos con huecos |
|---|---|
| Módulo Expediente | 31 |
| Módulo Ciclo de vida | **54** |
| En común | 30 |

**La diferencia son 24 más y 1 menos, y las dos se explican:**

| Diferencia | Cuántos | Por qué |
|---|---|---|
| Los ve solo el Ciclo de vida | **24** | **Todos son índices**, y un índice no entra al expediente. Sus huecos existen y el expediente nunca los mostró |
| Los ve solo el Expediente | **1** | Su `«…»` está dentro de un bloque cercado. Ahí es un ejemplo, no un hueco. El expediente no distingue |

Sobre los mismos 1 002 documentos traídos, contando igual, las dos dan **55 y 54**. La única diferencia es el bloque cercado. **Las dos cuentas dicen lo mismo, y la de esta fase corrige un caso.**

**El `B-03` queda cerrado.**

---

## 4. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| Qué se miró | Resultado |
|---|---|
| Los 24 que solo ve el Ciclo de vida | Los 24 son de tipo índice. Ninguno es un falso positivo |
| El que solo ve el Expediente | Su marca está dentro de un bloque cercado, donde se escribe para mostrarla |
| Que ningún documento cambiara | Contenido y fecha iguales |

---

## 5. Veredicto por criterio de aceptación

| CA | Evidencia | Veredicto |
|---|---|---|
| [CA-01](../HU-001-ver-que-le-falta-a-un-documento.md#ca-01--se-dice-qué-molde-sigue-el-documento) | CP-001 | **Cumple** |
| [CA-02](../HU-001-ver-que-le-falta-a-un-documento.md#ca-02--se-listan-los-huecos-con-cuántos-son-y-dónde) | CP-002, §3 | **Cumple** |
| [CA-03](../HU-001-ver-que-le-falta-a-un-documento.md#ca-03--solo-el-hueco-cierto-entra-en-la-cuenta) | CP-003 | **Cumple** |
| [CA-04](../HU-001-ver-que-le-falta-a-un-documento.md#ca-04--lo-que-llena-la-instalación-no-se-cuenta-como-pendiente) | CP-004 | **Cumple** |
| [CA-05](../HU-001-ver-que-le-falta-a-un-documento.md#ca-05--un-documento-de-tipo-desconocido-lo-dice) | CP-005 | **Cumple** |

## 5.1 Lo que el plan exigía

| Lo que el plan pedía | Qué pasó |
|---|---|
| La tabla de moldes declarada | Hecha: 17 con molde, 2 sin, y los tres de fuera |
| La cuenta sobre lo real, escrita | Hecha: **54 documentos, 77 huecos** |
| Comparar con la cuenta del expediente | Hecha, en la §3, y explicada entera |
| Que ningún documento cambie | Comprobado |
| Sin dependencias nuevas | **Cero** |

---

## 6. Veredicto de la fase

**Concepto: Cumple.**

De cualquier documento del ciclo se sabe qué molde sigue y qué huecos le faltan, con la cuenta y con dónde está cada uno. El criterio que decidía, que un hueco con nombre no infle la cuenta, **se midió antes de construir**, y esa medición cambió el diseño: la idea original habría dado por incompleto todo documento bien escrito.

**Lo que aparece de nuevo, y no estaba pedido:** 24 documentos con espacios por llenar que el expediente nunca mostró, porque los índices no entran al expediente.

**Y lo que esta fase no puede decir:** si la lista sirve para llenar. Eso lo dirá la `HU-002`, llenando un documento real de punta a punta.

---

## 7. Evidencias

| ID | Qué es | Dónde |
|---|---|---|
| EV-01 | Las 26 pruebas del módulo | `plataforma/nucleo/ciclo_de_vida/tests.py` |
| EV-02 | Lo contado sobre este repositorio | §1 y §3 |

**Las dos baterías:** 733 pruebas del estándar y 278 de la plataforma, **cero rojas**.

---

## 8. Ciclos anteriores

No hay: es el primer ciclo de la fase.
