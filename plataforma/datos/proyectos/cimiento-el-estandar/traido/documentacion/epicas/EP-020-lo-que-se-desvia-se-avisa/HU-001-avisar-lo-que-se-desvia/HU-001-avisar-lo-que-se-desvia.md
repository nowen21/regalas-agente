# HU-001 — Avisar lo que se desvía

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-001 |
| **Épica** | [EP-020 Lo que se desvía se avisa](../epica.md) |
| **Funcionalidad** | `F-029` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Avisos |
| **Tipo** | Funcional |
| **Prioridad** | Should |
| **Estimación** | S |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-09-01, con sus tres criterios probados |
---

## 2. Narrativa

- **Como** quien no puede leer doscientos archivos para saber qué se quedó atrás
- **Quiero** que lo que se desvió salga solo
- **Para** que enterarse no dependa de ir a mirar

---

## 3. Contexto y descripción

**Todo lo que hace falta saber ya está escrito**, y nadie lo lee. Medido acá el 2026-09-01: **3 historias sin ninguna fase** y **28 funcionalidades construidas sin verificar**.

**Demasiados avisos se vuelven ruido, y el ruido se ignora completo.** Está en la ficha, y no lo arregla el código: lo arregla no inventar avisos. Por eso son **tres clases** y no quince.

**Y hubo que definir «vencida»**, porque el estándar nunca le puso fecha a una deuda. Acá quiere decir *sin moverse hace más de 30 días*, que es lo único que el texto sabe.

### 3.1 Reglas de negocio

- `RN-1` **Todo aviso dice qué lo disparó y dónde mirar.** El que no puede, no se emite.
- `RN-2` Salen de lo que más duele a lo que menos.
- `RN-3` **Un aviso atendido no vuelve.**
- `RN-4` Cuando la lista se recorta, se dice.
- `RN-5` Una fase que no dice desde cuándo lleva quieta **no se da por vencida**.

### 3.2 Supuestos

- Que las fases traen su última actualización y el inventario su columna de verificado.

### 3.3 Fuera de alcance

- **Arreglar lo que se avisa.**
- Mandarlo por correo, y la pantalla.

---

## 4. Criterios de aceptación

### CA-01 — Una deuda vencida se avisa

```gherkin
Dada una fase sin cerrar que lleva más de 30 días sin tocarse
Cuando se piden los avisos
Entonces sale, con los días que lleva
```

**Cómo validarlo:** con una fase vieja y otra reciente.
- **Aprobado cuando:** sale la vieja y no la reciente.

### CA-02 — Cada aviso dice qué lo disparó y dónde mirar

```gherkin
Dado cualquier aviso
Cuando se lee
Entonces trae qué lo disparó y la ruta donde mirar
```

**Cómo validarlo:** recorriendo los tres tipos.
- **Aprobado cuando:** los dos datos están en todos.

### CA-03 — Un aviso atendido no vuelve a aparecer

```gherkin
Dado un aviso atendido
Cuando se piden los avisos otra vez
Entonces no sale
Y se dice cuántos están callados a propósito
```

**Cómo validarlo:** arreglando la causa de uno y callando otro.
- **Aprobado cuando:** ninguno de los dos vuelve. **Es el criterio que decide.**

### Criterios transversales

- Sin avisos **se dice con palabras**; no se devuelve una lista vacía.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Claridad | Ningún aviso sin causa ni sin destino |
| Honestidad | «Vencida» sale con su definición |

---

## 6. Diseño y referencias

- Funcionalidad `F-029` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- [Especificación del módulo Avisos](../../../avisos/spec.md).
- Señales [`S-110`](../../../senales.md) y [`S-113`](../../../senales.md).

---

## 7. Tareas técnicas derivadas

1. Las tres clases de aviso.
2. Ordenar por lo que más duele.
3. Leer lo callado a propósito.
4. Decir cuando recorta, y cuando no hay nada.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [W-EP-020-HU-001-todo-aviso-dice-que-lo-disparo](W-EP-020-HU-001-todo-aviso-dice-que-lo-disparo/estado-fase.md) | Los tres CA | Cerrada el 2026-09-01: **Cumple** |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | `EP-019`, que dice en qué estación va cada fase |
| **Riesgo 1** | Que el ruido haga ignorar la lista entera. Tres clases, y ninguna sin causa |
| **Riesgo 2** | Que «vencida» se lea como un vencimiento acordado. Sale con su definición |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ La épica aprobada el 2026-09-01.
- ☑ `EP-019` cerrada.

## 11. Definition of Done

- ☑ Los tres criterios con veredicto y evidencia.
- ☑ Comprobado que todo aviso dice qué lo disparó.
- ☑ Comprobado que lo atendido no vuelve.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | No | Lee lo que `EP-019` ordena |
| Negociable | Sí | Cuáles clases de aviso hay se puede ampliar, con cuidado |
| Valiosa | Sí | En su primera corrida encontró cinco carpetas que nadie veía |
| Estimable | Sí | Son tres recorridos sobre texto |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se corre y se mira la lista |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz, y cerrada el mismo día |
