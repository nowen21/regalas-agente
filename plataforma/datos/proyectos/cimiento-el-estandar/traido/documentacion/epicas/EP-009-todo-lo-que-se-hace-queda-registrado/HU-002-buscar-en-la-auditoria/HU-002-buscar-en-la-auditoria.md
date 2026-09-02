# HU-002 — Buscar en la auditoría

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-002 |
| **Épica** | [EP-009 Todo lo que se hace queda registrado](../epica.md) |
| **Funcionalidad** | `F-019` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Auditoría |
| **Tipo** | Funcional |
| **Prioridad** | Should |
| **Estimación** | S |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-09-01, con sus tres criterios probados |
---

## 2. Narrativa

- **Como** quien tiene que responder qué pasó y cuándo
- **Quiero** poder preguntarle a la auditoría por proyecto, por fecha y por tipo de acción
- **Para** que el registro sirva de algo el día que haga falta

---

## 3. Contexto y descripción

**La ficha de `F-019` lo dice sin adornos:** *«sin esta, la auditoría existe pero no sirve»*. Un registro que no se puede consultar es un archivo que nadie abre.

La `HU-001` ya dejó todo registrado, y con una garantía fuerte: **la constancia va antes que el efecto**. Lo que falta es la otra mitad — poder preguntarle.

**Y hay un detalle que no es cosmético:** una búsqueda que no encuentra nada tiene que **decirlo**. Un resultado vacío y una consulta que falló se ven exactamente igual desde afuera, y ya pasó una vez en este proyecto (`S-110`).

### 3.1 Reglas de negocio

- `RN-1` Se filtra por proyecto, por rango de fechas y por tipo de acción.
- `RN-2` Lo hallado sale **de lo más reciente a lo más viejo**.
- `RN-3` **Si no hay coincidencias, se dice.**
- `RN-4` Si el resultado se recorta, **se avisa que se recortó**.

### 3.2 Supuestos

- Que la auditoría tiene registros, y los tiene desde la `HU-001`.

### 3.3 Fuera de alcance

- **La pantalla.** Va orden de consola, como el resto de esta etapa.
- Exportar el resultado.

---

## 4. Criterios de aceptación

### CA-01 — Se filtra por proyecto, fecha y tipo de acción

```gherkin
Dado un conjunto de registros de auditoría
Cuando se filtra por proyecto, por rango de fechas y por tipo de acción
Entonces salen solo los que coinciden con los tres
```

**Cómo validarlo:** con registros de varios proyectos, fechas y acciones.
- **Aprobado cuando:** los tres filtros funcionan, juntos y por separado.

### CA-02 — Sin coincidencias se dice que no hay

```gherkin
Dada una búsqueda que no encuentra nada
Cuando se lee la respuesta
Entonces dice que no hay coincidencias
Y se distingue de una consulta que falló
```

**Cómo validarlo:** buscando algo que no está.
- **Aprobado cuando:** lo dice con palabras. **Es el criterio que decide.**

### CA-03 — Responde en menos de un segundo con un año de registros

```gherkin
Dado un año de registros
Cuando se busca
Entonces la respuesta llega en menos de un segundo
```

**Cómo validarlo:** midiendo con un volumen de un año.
- **Aprobado cuando:** el tiempo sale medido y escrito, no supuesto.

### Criterios transversales

- El día del **hasta** entra completo en el rango.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Rendimiento | Menos de un segundo con un año de registros |
| Claridad | Un resultado vacío se distingue de una falla |

---

## 6. Diseño y referencias

- Funcionalidad `F-019` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- [Especificación del módulo Auditoría](../../../auditoria/spec.md).
- Señal [`S-110`](../../../senales.md), por lo del resultado vacío.

---

## 7. Tareas técnicas derivadas

1. Filtrar por los tres campos.
2. Que el día del hasta entre completo.
3. Decir cuando no hay nada.
4. Medir el tiempo y avisar si se recortó.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [R-EP-009-HU-002-la-auditoria-se-puede-preguntar](R-EP-009-HU-002-la-auditoria-se-puede-preguntar/estado-fase.md) | Los tres CA | Cerrada el 2026-09-01: **Cumple** |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | La `HU-001`, que registra |
| **Riesgo 1** | Que un resultado vacío se vea como una falla. Se dice con palabras |
| **Riesgo 2** | Que el rango deje por fuera el último día. El **hasta** entra completo |
| **Riesgo 3** | Que un resultado enorme se recorte en silencio. **Se avisa** |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ La épica aprobada.
- ☑ La `HU-001` cerrada, con la auditoría registrando.

## 11. Definition of Done

- ☑ Los tres criterios con veredicto y evidencia.
- ☑ Comprobado que un resultado vacío se dice.
- ☑ El tiempo medido, no supuesto.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | No | Necesita lo que registra la `HU-001` |
| Negociable | Sí | Qué filtros hay se puede ampliar |
| Valiosa | Sí | Sin ella la auditoría existe pero no sirve |
| Estimable | Sí | Es una consulta con tres filtros |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se busca y se mira lo que sale |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz, y cerrada el mismo día |
