# HU-004 — Publicar una versión del cuerpo de reglas

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-004 |
| **Épica** | [EP-016 El cuerpo de reglas se administra desde la plataforma](../epica.md) |
| **Funcionalidad** | `F-008` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Reglas |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-09-01, con sus tres criterios probados |
---

## 2. Narrativa

- **Como** quien mantiene el estándar que otros proyectos heredan
- **Quiero** publicar una versión solo cuando esté dicho qué cambió y nada se haya roto
- **Para** no mandarle a nadie una versión que le rompe lo que le servía

---

## 3. Contexto y descripción

**Publicar es lo que vuelve real un cambio.** Antes de eso, una regla escrita no rige en ninguna parte: los proyectos siguen con la versión que adoptaron. Y después, lo publicado se lo lleva quien lo adopte, con lo bueno y con lo roto.

**La puerta ya existe.** La construyó `F-022`, y corre las comprobaciones del estándar y la suite del proyecto. Esta historia la usa; no la vuelve a escribir.

**Lo que la plataforma no escribe es la entrada del registro.** Es prosa: dice qué pasó y por qué importa, y eso lo escribe una persona. Lo que sí hace es **negarse a publicar sin ella**.

### 3.1 Reglas de negocio

- `RN-1` **Un número no se publica dos veces.** Dos proyectos declarando la misma versión con reglas distintas es un desorden que no se deshace.
- `RN-2` **Sin entrada en el registro no se publica**, y la entrada dice si es MAYOR, MENOR o PARCHE.
- `RN-3` **Si la puerta no pasa, no se publica.**
- `RN-4` **Lo que falta se dice todo junto.** De a uno obliga a intentar tres veces.

### 3.2 Supuestos

- Que la entrada del registro la escribe una persona antes de pedir publicar.

### 3.3 Fuera de alcance

- **Escribir la entrada del registro.**
- Decidir qué entra en la versión.

---

## 4. Criterios de aceptación

### CA-01 — Se publica con su número, su fecha y qué cambió

```gherkin
Dado un número libre, con entrada en el registro y la puerta en verde
Cuando se pide publicar
Entonces la versión queda escrita
```

**Cómo validarlo:** con un registro de prueba.
- **Aprobado cuando:** el archivo de versión queda con el número nuevo.

### CA-02 — Sin registro de qué cambió no se publica

```gherkin
Dado un número sin entrada en el registro
Cuando se pide publicar
Entonces no se publica, y se dice por qué
```

**Cómo validarlo:** pidiendo una versión que el registro no menciona.
- **Aprobado cuando:** se rechaza. **Es el criterio que decide.**

### CA-03 — Si rompe algo que servía, no se publica

```gherkin
Dado que la puerta de publicación no pasa
Cuando se pide publicar
Entonces no se publica
```

**Cómo validarlo:** con la puerta en rojo.
- **Aprobado cuando:** se rechaza, y el archivo de versión no cambia.

### Criterios transversales

- Un número ya publicado se rechaza.
- Una entrada sin tipo se rechaza: es lo que le dice al que adopta si le toca rehacer algo.
- Lo que falta sale **todo junto**.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Integridad | El archivo de versión no cambia si algo falta |
| Claridad | Todo lo que falta, en una sola respuesta |

---

## 6. Diseño y referencias

- Funcionalidad `F-008` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- Requisito `RF-08` del [análisis](../../../../cvds/analisis-requisitos/README.md).
- La puerta: `F-022`, del módulo Comprobaciones.

---

## 7. Tareas técnicas derivadas

1. Encontrar la entrada del registro de esa versión.
2. Leer su tipo.
3. Pedir la puerta.
4. Juntar todo lo que falte.
5. Escribir la versión, solo si no falta nada.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [J-EP-016-HU-004-sin-decir-que-cambio-no-se-publica](J-EP-016-HU-004-sin-decir-que-cambio-no-se-publica/estado-fase.md) | Los tres CA | Cerrada el 2026-09-01: **Cumple** |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | `F-022`, la puerta, y `F-005`, que escribe las reglas |
| **Riesgo 1** | Publicar dos veces el mismo número. Se comprueba contra el registro |
| **Riesgo 2** | Que la entrada exista y no diga el tipo. Se rechaza |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ La épica aprobada el 2026-09-01.
- ☑ `F-022` cerrada.

## 11. Definition of Done

- ☑ Los tres criterios con veredicto y evidencia.
- ☑ Comprobado que sin entrada no se publica.
- ☑ Comprobado que con la puerta en rojo no se publica.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | No | Necesita la puerta de `F-022` |
| Negociable | Sí | Cómo se muestra lo que falta se puede ajustar |
| Valiosa | Sí | Es lo que impide mandarle a otro una versión rota |
| Estimable | Sí | Es juntar tres comprobaciones que ya existen |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se pide con un registro de prueba |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz, y cerrada el mismo día |
