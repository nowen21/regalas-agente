# HU-002 — Reportar cómo va cada proyecto

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-002 |
| **Épica** | [EP-020 Lo que se desvía se avisa](../epica.md) |
| **Funcionalidad** | `F-030` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Avisos |
| **Tipo** | Funcional |
| **Prioridad** | Should |
| **Estimación** | S |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-09-01, con sus tres criterios probados |
---

## 2. Narrativa

- **Como** quien decide dónde poner el tiempo
- **Quiero** ver el avance y la deuda de cada proyecto con la misma medida
- **Para** decidir con datos y no con impresión

---

## 3. Contexto y descripción

**Comparar proyectos distintos con la misma medida engaña si no se dice qué mide.** Está en la ficha de `F-030`, y la respuesta no es dejar de comparar: es que el reporte lleve encima, siempre, la definición de cada columna.

**Y un proyecto sin datos aparece así, no en cero.** Cero fases terminadas de cero es una división que no existe; escribir «0 %» ahí dice que el proyecto va mal cuando lo que pasa es que **no se sabe**. Es la distinción de `S-107`: un estado que admite «no se sabe» necesita su propio nombre.

### 3.1 Reglas de negocio

- `RN-1` La misma medida para todos, y **la medida escrita al lado**.
- `RN-2` La deuda declarada y la vencida salen separadas.
- `RN-3` **Un proyecto sin datos aparece así, no en cero.**
- `RN-4` Los sin datos van al final: no son los peores, son los que no se sabe.
- `RN-5` Lo que no está verificado se reporta así.

### 3.2 Supuestos

- Que los proyectos están conectados y tienen sus fases escritas.

### 3.3 Fuera de alcance

- **Ordenar los proyectos por bueno o malo.** El reporte muestra; decidir es del usuario.
- La pantalla.

---

## 4. Criterios de aceptación

### CA-01 — Se ve el avance de cada proyecto con la misma medida

```gherkin
Dados varios proyectos conectados
Cuando se pide el reporte
Entonces cada uno trae su avance calculado igual
Y debajo está escrito qué mide esa columna
```

**Cómo validarlo:** con dos proyectos de tamaños distintos.
- **Aprobado cuando:** la definición sale con la tabla.

### CA-02 — Se ve la deuda declarada y la vencida

```gherkin
Dado un proyecto con fases quietas e historias sin fase
Cuando se lee su fila
Entonces la deuda y la vencida salen en columnas distintas
```

**Cómo validarlo:** con las dos clases mezcladas.
- **Aprobado cuando:** los dos números salen y no se confunden.

### CA-03 — Un proyecto sin datos aparece así, no en cero

```gherkin
Dado un proyecto sin ninguna fase escrita
Cuando se lee su fila
Entonces dice «sin datos»
```

**Cómo validarlo:** con un proyecto vacío.
- **Aprobado cuando:** no dice «0 %». **Es el criterio que decide.**

### Criterios transversales

- Sin ningún proyecto conectado **se dice**, y no se deja la tabla en blanco.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Honestidad | Toda columna sale con su definición |
| Claridad | «Sin datos» y «cero» nunca se escriben igual |

---

## 6. Diseño y referencias

- Funcionalidad `F-030` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- [Especificación del módulo Avisos](../../../avisos/spec.md).
- Señal [`S-107`](../../../senales.md).

---

## 7. Tareas técnicas derivadas

1. La fila de un proyecto.
2. El avance, o «sin datos».
3. La deuda y la vencida, separadas.
4. La definición de cada columna, impresa con la tabla.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [X-EP-020-HU-002-sin-datos-no-es-cero](X-EP-020-HU-002-sin-datos-no-es-cero/estado-fase.md) | Los tres CA | Cerrada el 2026-09-01: **Cumple** |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | La `HU-001`, que cuenta la deuda |
| **Riesgo 1** | Que comparar engañe. Cada columna sale con su definición |
| **Riesgo 2** | Que un proyecto sin datos parezca el peor. Sale como «sin datos», y de últimas |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ La épica aprobada el 2026-09-01.
- ☑ La `HU-001` cerrada.

## 11. Definition of Done

- ☑ Los tres criterios con veredicto y evidencia.
- ☑ Comprobado que sin datos no es cero.
- ☑ Comprobado que la definición sale con la tabla.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | No | Necesita la cuenta de deuda de la `HU-001` |
| Negociable | Sí | Qué columnas hay se puede ajustar |
| Valiosa | Sí | Hoy se decide con impresión |
| Estimable | Sí | Es juntar dos cuentas por proyecto |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se corre y se lee la tabla |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz, y cerrada el mismo día |
