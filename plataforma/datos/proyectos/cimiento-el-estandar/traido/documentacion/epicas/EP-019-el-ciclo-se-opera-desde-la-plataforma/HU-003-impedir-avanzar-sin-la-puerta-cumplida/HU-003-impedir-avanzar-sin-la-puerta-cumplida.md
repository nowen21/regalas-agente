# HU-003 — Impedir avanzar sin la puerta cumplida

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-003 |
| **Épica** | [EP-019 El ciclo se opera desde la plataforma](../epica.md) |
| **Funcionalidad** | `F-013` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Ciclo de vida |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | S |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-09-01, con sus tres criterios probados |
---

## 2. Narrativa

- **Como** quien no quiere depender de acordarse de cada puerta
- **Quiero** que no se pase a la estación siguiente sin lo que esa puerta exige
- **Para** que las puertas se cumplan solas

---

## 3. Contexto y descripción

**Una puerta que estorba se termina saltando**, y está escrito en la ficha de `F-013`: *«cada una tiene que justificarse»*. Por eso se comprueban **tres** y no trece: las que dejan daño cuando se saltan.

**El rechazo dice cuál puerta falta.** «No se puede avanzar» obliga a ir a buscar; «falta la estación 7, el plan aprobado» se arregla de una.

**Y no es un candado.** Cualquiera puede escribir el archivo a mano. Lo que se logra es que saltarse la puerta sea **un acto deliberado en vez de un olvido**, y eso es la promesa entera, no una más grande.

### 3.1 Reglas de negocio

- `RN-1` Sin el plan aprobado no se pasa a ejecución.
- `RN-2` **Sin veredicto no se cierra.**
- `RN-3` Sin el commit autorizado no se publica.
- `RN-4` **El rechazo nombra la puerta que falta.**
- `RN-5` Una estación sin puerta comprobable lo dice, en vez de dejar pasar en silencio.

### 3.2 Supuestos

- Que la fase tiene su tabla de estaciones y su veredicto escritos.

### 3.3 Fuera de alcance

- **Impedirlo de verdad.** Esto avisa; el archivo se puede escribir a mano.
- Las otras diez estaciones.

---

## 4. Criterios de aceptación

### CA-01 — Una fase sin plan aprobado no pasa a ejecución

```gherkin
Dada una fase con la estación 7 sin cumplir
Cuando se pregunta si puede pasar a la 8
Entonces no pasa
```

**Cómo validarlo:** con la 7 marcada y sin marcar.
- **Aprobado cuando:** solo pasa con la 7 cumplida.

### CA-02 — Una fase sin veredicto no se cierra

```gherkin
Dada una fase sin veredicto, o con veredicto «No cumple»
Cuando se pregunta si puede cerrarse
Entonces no puede
```

**Cómo validarlo:** con los tres veredictos posibles.
- **Aprobado cuando:** solo pasa con «Cumple». **Es el criterio que decide.**

### CA-03 — El rechazo dice cuál puerta falta

```gherkin
Dada una fase que no puede pasar
Cuando se lee el motivo
Entonces nombra la puerta y dice qué daño evita
```

**Cómo validarlo:** leyendo los motivos de los tres rechazos.
- **Aprobado cuando:** los tres nombran la puerta.

### Criterios transversales

- Una estación sin puerta comprobable **lo dice**, y no se hace la que aprueba.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Claridad | Todo veredicto trae motivo, también cuando deja pasar |
| Honestidad | Se declara que no es un candado |

---

## 6. Diseño y referencias

- Funcionalidad `F-013` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- [Especificación del módulo Ciclo de vida](../../../ciclo-de-vida/spec.md).
- Señal [`S-109`](../../../senales.md): una ayuda que se presenta como garantía hace que la gente deje de mirar.

---

## 7. Tareas técnicas derivadas

1. Las tres puertas comprobables.
2. El veredicto de las pruebas.
3. El motivo, siempre, también en el sí.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [U-EP-019-HU-003-el-rechazo-dice-cual-puerta-falta](U-EP-019-HU-003-el-rechazo-dice-cual-puerta-falta/estado-fase.md) | Los tres CA | Cerrada el 2026-09-01: **Cumple** |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | La `HU-002`, que lee la tabla |
| **Riesgo 1** | Que se presente como candado y la gente deje de mirar. **Se declara que no lo es** |
| **Riesgo 2** | Que trece puertas estorben y se salten todas. Se comprueban tres |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ La épica aprobada el 2026-09-01.
- ☑ La `HU-002` cerrada.

## 11. Definition of Done

- ☑ Los tres criterios con veredicto y evidencia.
- ☑ Comprobado que el rechazo nombra la puerta.
- ☑ Escrito que no es un candado.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | No | Necesita la tabla que lee la `HU-002` |
| Negociable | Sí | Cuáles puertas se comprueban se puede ajustar |
| Valiosa | Sí | Las puertas hoy dependen de acordarse |
| Estimable | Sí | Son tres comprobaciones |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se pregunta y se lee el motivo |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz, y cerrada el mismo día |
