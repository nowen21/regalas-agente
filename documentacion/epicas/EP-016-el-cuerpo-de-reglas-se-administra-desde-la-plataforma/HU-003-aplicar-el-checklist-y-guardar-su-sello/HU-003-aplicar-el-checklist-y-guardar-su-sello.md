# HU-003 — Aplicar el checklist y guardar su sello

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-003 |
| **Épica** | [EP-016 El cuerpo de reglas se administra desde la plataforma](../epica.md) |
| **Funcionalidad** | `F-007` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Reglas |
| **Tipo** | Funcional |
| **Prioridad** | Should |
| **Estimación** | M |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-09-01, con sus tres criterios probados |
---

## 2. Narrativa

- **Como** quien escribe reglas que otros van a heredar
- **Quiero** aplicarle a cada una la lista de comprobación y que el resultado quede escrito
- **Para** que se sepa contra qué se comprobó, y que ese resultado no sobreviva a un cambio del texto

---

## 3. Contexto y descripción

**El checklist ya existe**, con sus **20 filas**, y cada una nombra la meta-regla que la respalda. La plataforma no inventa ninguna: las trae y guarda lo que se responda.

**Buena parte de las filas pide criterio, y eso no se automatiza.** Lo dice la ficha: *«la plataforma acompaña, no decide»*. Si el capítulo es el dueño del tema, o si la regla ya existe con otras palabras, lo responde una persona.

**Lo que sí protege de verdad es la caducidad.** Un sello pegado a una regla que después se editó dice que algo se comprobó, y lo que se comprobó era otro texto. **Es peor que no tener sello: da confianza sin respaldo.**

### 3.1 Reglas de negocio

- `RN-1` **El checklist se lee del estándar**, no se copia.
- `RN-2` **Una fila que no aplica lleva su motivo.** Sin motivo no se distingue de una que se saltó.
- `RN-3` **Si la regla se edita, el sello queda anulado**, y se dice.
- `RN-4` **La comparación por fechas no es el veredicto.** El estándar es el que decide.
- `RN-5` El sello dice **contra qué versión** se aplicó.

### 3.2 Supuestos

- Que el proyecto tiene el checklist del estándar en su sitio.

### 3.3 Fuera de alcance

- **Responder las filas.** El criterio es de una persona.
- Cambiar el checklist.

---

## 4. Criterios de aceptación

### CA-01 — Una regla queda con su sello y su fecha

```gherkin
Dado una regla y las respuestas del checklist
Cuando se arma su sello
Entonces queda el bloque con el veredicto, la versión y la fecha
```

**Cómo validarlo:** armando el sello con respuestas de prueba.
- **Aprobado cuando:** trae veredicto, versión, fecha y su aviso de caducidad.

### CA-02 — Editar la regla anula el sello y lo dice

```gherkin
Dado una regla sellada en una fecha
Y que su archivo cambió después
Cuando se pregunta por su sello
Entonces se dice que parece anulado
Y se dice que el veredicto lo da el estándar
```

**Cómo validarlo:** con `M11`, sellada el 2026-08-07 y tocada el 2026-08-19.
- **Aprobado cuando:** lo dice, **y no lo presenta como veredicto**.

### CA-03 — Una fila que no aplica queda escrita con su motivo

```gherkin
Dado una fila respondida como que no aplica
Cuando se arma el sello
Entonces su motivo queda escrito
Y si no se dio motivo, queda marcado como espacio por llenar
```

**Cómo validarlo:** armando el sello con y sin motivo.
- **Aprobado cuando:** el motivo sale, o el hueco se ve.

### Criterios transversales

- Sin el checklist del estándar **se dice**, en vez de armar un sello contra nada.
- La cabecera de la tabla del checklist no se cuenta como fila.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Honestidad | **La comparación por fechas se llama como lo que es.** No es el veredicto |
| Trazabilidad | El sello dice contra qué versión y en qué fecha |

---

## 6. Diseño y referencias

- Funcionalidad `F-007` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- Requisito `RF-07` del [análisis](../../../../cvds/analisis-requisitos/README.md).
- El instrumento: [base/20-meta-reglas/checklist.md](../../../../base/20-meta-reglas/checklist.md).

---

## 7. Tareas técnicas derivadas

1. Leer las filas del checklist.
2. Leer el sello de una regla: contra qué versión y cuándo.
3. La comparación por fechas, **llamada como lo que es**.
4. Preguntarle al estándar el veredicto de verdad.
5. El molde del sello, con los motivos de lo que no aplica.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [I-EP-016-HU-003-un-sello-no-sobrevive-a-un-cambio](I-EP-016-HU-003-un-sello-no-sobrevive-a-un-cambio/estado-fase.md) | Los tres CA | Cerrada el 2026-09-01: **Cumple** |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | La `HU-002`, que escribe la regla que se va a sellar |
| **Riesgo 1** | **Que la comparación por fechas se tome por veredicto.** Midiéndola así, 185 de 248 reglas salían anuladas y el estándar dice que ninguna lo está |
| **Riesgo 2** | Que alguien crea que la plataforma responde las filas. La orden lo dice |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ La épica aprobada el 2026-09-01.
- ☑ Medido el checklist: 20 filas.

## 11. Definition of Done

- ☑ Los tres criterios con veredicto y evidencia.
- ☑ Comprobado sobre una regla real que el sello se lee.
- ☑ Comprobado que la comparación por fechas no se presenta como veredicto.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | No | Necesita la regla que la `HU-002` escribe |
| Negociable | Sí | Cómo se muestran las filas se puede ajustar |
| Valiosa | Sí | Un sello que sobrevive a un cambio da confianza sin respaldo |
| Estimable | Sí | Es leer una tabla y armar un bloque |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se lee el sello de una regla real |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz, y cerrada el mismo día |
