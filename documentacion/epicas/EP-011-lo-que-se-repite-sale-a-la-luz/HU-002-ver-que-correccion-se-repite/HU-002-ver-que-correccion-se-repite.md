# HU-002 — Ver qué corrección se repite

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-002 |
| **Épica** | [EP-011 Lo que se repite sale a la luz](../epica.md) |
| **Funcionalidad** | `F-034` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Medición |
| **Tipo** | Funcional |
| **Prioridad** | Should |
| **Estimación** | L |
| **Solicitante** | El usuario |
| **Estado** | Pendiente, sin aprobar |
---

## 2. Narrativa

- **Como** quien corrige al agente todos los días
- **Quiero** ver qué correcciones tuve que repetir, y cuántas veces
- **Para** escribir la regla que falta, en vez de volver a corregir lo mismo

---

## 3. Contexto y descripción

Es la historia que le da sentido a la anterior. Con las conversaciones indexadas, la plataforma cuenta qué se repitió y lo muestra ordenado, de lo más repetido a lo menos.

**Muestra el patrón, no decide la regla.** Lo que salga del reporte entra a la cadena de siempre: pendiente, historia, fase. La plataforma no escribe reglas sola.

**Lo difícil es `CA-03`**, agrupar dos formas distintas de decir lo mismo. Contar palabras iguales es fácil y no sirve: *"español colombiano"*, *"recuerde la regla de español"* y *"pero español colombiano cómo sería"* son la misma corrección dicha de tres maneras.

### 3.1 Reglas de negocio

- `RN-1` La plataforma muestra el patrón; la regla la decide el usuario.
- `RN-2` Dos formas distintas de decir lo mismo cuentan como una.
- `RN-3` Si no hay nada repetido, se dice, en vez de rellenar el reporte.

### 3.2 Supuestos

- Que lo que el usuario repite queda escrito en la conversación, y no solo en su cabeza.

### 3.3 Fuera de alcance

- Escribir la regla que resuelve el patrón.
- Medir el tiempo de revisión, que es `F-032` y va en la versión 5.

---

## 4. Criterios de aceptación

### CA-01 — El reporte sale por período

```gherkin
Dado un período que el usuario elige
Cuando pide el reporte
Entonces salen las correcciones más repetidas de ese período
Y salen ordenadas de la más repetida a la menos
```

### CA-02 — Cada corrección dice cuántas veces y dónde

```gherkin
Dado una corrección del reporte
Cuando el usuario la mira
Entonces dice cuántas veces se repitió
Y en qué sesiones, con el enlace a cada una
```

### CA-03 — Lo mismo dicho distinto cuenta como uno

```gherkin
Dado dos mensajes que piden lo mismo con palabras distintas
Cuando se cuentan
Entonces cuentan como una sola corrección repetida dos veces
```

**Cómo validarlo:** con las tres formas en que se pidió *español colombiano* en la sesión del 2026-08-25. Tienen que salir como una, no como tres.

### CA-04 — Sin nada repetido, se dice

```gherkin
Dado un período sin ninguna corrección repetida
Cuando el usuario pide el reporte
Entonces se dice que no hubo ninguna
Y no se rellena con lo que solo se dijo una vez
```

### Criterios transversales

- El reporte no propone la regla: muestra el patrón y dice que la decisión sigue siendo del usuario.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Disponibilidad | Funciona sin red, y sin instalar nada aparte (`RNF-03`) |
| Rendimiento | El reporte de un mes sale en menos de lo que cuesta releer una sesión |

---

## 6. Diseño y referencias

- Funcionalidad `F-034` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- Requisito `RF-34` del [análisis](../../../../cvds/analisis-requisitos/README.md).
- Le da a `F-032` la fuente que le faltaba: hoy declara que recibe cuántas correcciones se repiten, y nada las cuenta.

---

## 7. Tareas técnicas derivadas

1. Reconocer en un mensaje que es una corrección, y no otra cosa.
2. Agrupar las que dicen lo mismo con palabras distintas.
3. Contar y ordenar por período.
4. Mostrarlas con sus sesiones enlazadas.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| Por abrir | Esta historia | Sin abrir. Va en la versión 2, después de `HU-001` |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | `HU-001` de esta épica: sin lo indexado no hay qué contar |
| **Riesgo 1** | Que agrupar frases parecidas no salga sin instalar algo que salga a la red. Si no sale, se entrega el conteo exacto y se declara la deuda |
| **Riesgo 2** | Que el reporte diga lo obvio. Se mide por lo que produce: si no nace una regla nueva, no sirvió |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su cambio anotado.
- ☑ Hay un caso real con el que probar `CA-03`.
- ☐ El módulo Medición tiene especificación aprobada.
- ☐ Está decidido qué cuenta como corrección.

## 11. Definition of Done

- ☐ Los cuatro criterios con veredicto y evidencia.
- ☐ `CA-03` probado con las tres formas del caso real.
- ☐ Si la agrupación no salió, la deuda declarada.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | No | Necesita `HU-001` |
| Negociable | Sí | Qué se cuenta y cómo se agrupa se puede ajustar |
| Valiosa | Sí | Es la razón por la que se pidió todo esto |
| Estimable | A medias | La agrupación es la parte que no se sabe cuánto cuesta |
| Pequeña | No | Probablemente sean dos fases: contar exacto, y agrupar |
| Verificable | Sí | Se prueba con un caso real que ya ocurrió |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-08-25 | Nace de `F-034`, que entró al inventario ese día desde [pendientes/85-las-conversaciones-completas-no-se-pueden-analizar.md](../../../../pendientes/85-las-conversaciones-completas-no-se-pueden-analizar.md) |
