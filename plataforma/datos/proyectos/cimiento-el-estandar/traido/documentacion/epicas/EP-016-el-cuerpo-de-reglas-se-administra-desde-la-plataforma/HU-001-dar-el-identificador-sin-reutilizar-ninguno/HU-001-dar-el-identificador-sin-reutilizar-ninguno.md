# HU-001 — Dar el identificador sin reutilizar ninguno

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-001 |
| **Épica** | [EP-016 El cuerpo de reglas se administra desde la plataforma](../epica.md) |
| **Funcionalidad** | `F-006` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Reglas |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | S |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-09-01, con sus tres criterios probados |
---

## 2. Narrativa

- **Como** quien escribe reglas que otros van a citar por su número
- **Quiero** que cada regla nueva reciba un identificador que nadie tuvo antes
- **Para** que una cita escrita hace un año siga apuntando a lo mismo

---

## 3. Contexto y descripción

El cuerpo de reglas tiene **257 reglas en 24 capítulos**, de las cuales **9 están derogadas**. Los identificadores se asignan a mano.

**Por qué esto es lo primero de la épica.** Una especificación escrita hace un año, un commit, una fase cerrada: todos citan reglas por su identificador. Si un número se le da a otra regla, todas esas citas empiezan a apuntar a algo que dice otra cosa, **y no hay forma de notarlo leyendo**: la cita sigue viéndose bien.

**Y por eso el número de una derogada tampoco se libera.** Derogar no borra: la regla se queda escrita, marcada, y su número ocupado para siempre. Lo exige `M11`.

### 3.1 Reglas de negocio

- `RN-1` **El siguiente identificador es el que sigue al mayor**, no el primer hueco.
- `RN-2` **Las derogadas cuentan.** Su identificador sigue ocupado.
- `RN-3` **Se comprueba antes de guardar.** Después ya hay dos reglas con el mismo número.
- `RN-4` El lector de reglas es el del estándar. No se duplica.

### 3.2 Supuestos

- Que el proyecto tiene el estándar instalado. Si no, se dice en vez de devolver una lista vacía.

### 3.3 Fuera de alcance

- Escribir la regla, que es la `HU-002`.
- Cambiar el formato de un identificador.

---

## 4. Criterios de aceptación

### CA-01 — Una regla nueva recibe el siguiente número libre

```gherkin
Dado un capítulo con reglas numeradas hasta la N
Cuando se pide el identificador para una regla nueva
Entonces se entrega el N más uno
```

**Cómo validarlo:** sobre este repositorio, capítulo por capítulo.
- **Aprobado cuando:** el número entregado no lo tiene nadie.

### CA-02 — El número de una derogada no se reasigna

```gherkin
Dado un capítulo con una regla derogada
Cuando se pide el siguiente identificador
Entonces el de la derogada no se entrega
Y tampoco se rellena el hueco que dejó
```

**Cómo validarlo:** con un capítulo cuyo número mayor tenga huecos por debajo.
- **Aprobado cuando:** se entrega el que sigue al mayor. **Es el criterio que decide.**

### CA-03 — No se puede guardar con un identificador ya usado

```gherkin
Dado un identificador que ya tiene otra regla, viva o derogada
Cuando se comprueba antes de guardar
Entonces se rechaza, y se dice por qué
```

**Cómo validarlo:** con uno vigente y con uno derogado.
- **Aprobado cuando:** los dos se rechazan.

### Criterios transversales

- Sin el lector del estándar **se dice**, en vez de devolver una lista vacía que se leería como «no hay reglas».
- Un capítulo sin reglas empieza en uno.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Integridad | **Cero identificadores reutilizados.** Es lo único que esta historia no puede fallar |
| Recuperación | Nada que reconstruir: se lee al pedirlo |

---

## 6. Diseño y referencias

- Funcionalidad `F-006` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- Requisito `RF-06` del [análisis](../../../../cvds/analisis-requisitos/README.md).
- La regla que lo manda: [`20·M11`](../../../../base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md).

---

## 7. Tareas técnicas derivadas

1. El puente hacia el lector de reglas del estándar.
2. Los identificadores usados por prefijo, con las derogadas adentro.
3. El siguiente libre.
4. La comprobación de antes de guardar.
5. Los huecos, para mirar y no para usar.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [G-EP-016-HU-001-ningun-numero-se-reutiliza](G-EP-016-HU-001-ningun-numero-se-reutiliza/estado-fase.md) | Los tres CA | Cerrada el 2026-09-01: **Cumple** |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | El lector de reglas del estándar |
| **Riesgo 1** | Que se rellene un hueco creyendo que está libre. Por eso el siguiente es el que sigue al mayor |
| **Riesgo 2** | Que el lector no esté y se devuelva vacío. Se revienta en vez de callar |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ La épica aprobada el 2026-09-01.
- ☑ Medido el cuerpo de reglas: 257, 9 derogadas, 24 capítulos.

## 11. Definition of Done

- ☑ Los tres criterios con veredicto y evidencia.
- ☑ Comprobado sobre este repositorio, capítulo por capítulo.
- ☑ Comprobado que el de una derogada no se entrega.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | Sí | Solo necesita leer el cuerpo de reglas |
| Negociable | Sí | Cómo se muestra se puede ajustar; el número, no |
| Valiosa | Sí | Es lo que impide que una cita vieja apunte a otra cosa |
| Estimable | Sí | Es leer y contar |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se corre sobre este repositorio |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz, y cerrada el mismo día |
