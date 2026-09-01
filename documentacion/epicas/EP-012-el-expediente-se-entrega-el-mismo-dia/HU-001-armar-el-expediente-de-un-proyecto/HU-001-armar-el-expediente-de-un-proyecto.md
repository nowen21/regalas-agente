# HU-001 — Armar el expediente de un proyecto

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-001 |
| **Épica** | [EP-012 El expediente se entrega el mismo día](../epica.md) |
| **Funcionalidad** | `F-025` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Expediente |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Solicitante** | El usuario |
| **Estado** | Aprobada el 2026-08-31 |
---

## 2. Narrativa

- **Como** quien tiene que entregar la documentación de un proyecto
- **Quiero** que se junte sola, en el orden del ciclo, y me diga qué le falta
- **Para** entregar el mismo día, y saber antes de entregar qué está incompleto

---

## 3. Contexto y descripción

Los documentos ya están en la plataforma: el módulo Importación los trajo y reconoció **1 054** en este repositorio, repartidos en 19 tipos. Lo que no hay es forma de juntarlos.

Armarlo a mano cuesta un día, y **se arma distinto cada vez**: dos entregas del mismo proyecto no se parecen. Peor, un expediente armado a mano no distingue entre «este documento no existe» y «se me pasó».

**Lo que este trabajo entrega no es un archivo**, sino el conjunto ordenado y **la lista de lo que falta**. Convertirlo al formato del cliente es la [HU-002](../HU-002-generar-el-entregable-de-ofimatica/HU-002-generar-el-entregable-de-ofimatica.md).

### 3.1 Reglas de negocio

- `RN-1` El expediente se arma **en el orden del ciclo**, no en el orden en que los documentos llegaron.
- `RN-2` Lo que falta se lista con su nombre. **Nunca se inventa** un documento ausente.
- `RN-3` Lo que está a medio llenar se marca antes de entregar (`RN-5` del inventario: lo sin verificar se entrega diciendo que lo está).
- `RN-4` **La auditoría y la memoria no entran.** Decidido el 2026-08-31, cerrando la duda 5 del análisis.
- `RN-5` Armar no modifica ningún documento: solo los junta.

### 3.2 Supuestos

- Que lo que Importación reconoció alcanza. Un documento que ese módulo no reconoce **no entra al expediente y se dice**, en vez de desaparecer.

### 3.3 Fuera de alcance

- Generar el archivo de ofimática, que es la `HU-002`.
- Llenar los documentos desde la plataforma (`F-014`).
- Decidir si el proyecto se entrega: el expediente informa, la decisión es del usuario.

---

## 4. Criterios de aceptación

### CA-01 — El expediente se arma en el orden del ciclo

```gherkin
Dado un proyecto con documentos traídos a la plataforma
Cuando se pide su expediente
Entonces salen todos sus documentos, agrupados por etapa del ciclo
Y en el orden en que el ciclo los produce, no en el que llegaron
```

**Cómo validarlo:** pedir el expediente de este repositorio y comparar el orden con las siete etapas de `cvds/`.
- **Aprobado cuando:** el orden es el del ciclo y no el del disco.

### CA-02 — Lo que falta se lista, y no se inventa

```gherkin
Dado un proyecto al que le falta un documento del ciclo
Cuando se pide su expediente
Entonces ese documento aparece en la lista de lo que falta, con su nombre
Y no aparece en el expediente como si existiera
```

**Cómo validarlo:** quitar un documento de un proyecto de prueba y pedir el expediente.
- **Aprobado cuando:** se nombra lo que falta, y el expediente no lo trae vacío.

### CA-03 — Lo que está a medio llenar se marca

```gherkin
Dado un documento con espacios sin llenar
Cuando entra al expediente
Entonces queda marcado como incompleto, con cuántos espacios le faltan
```

**Cómo validarlo:** con un documento real que conserve marcas de espacio por llenar.
- **Aprobado cuando:** el expediente lo señala **antes** de que alguien lo entregue.

### CA-04 — La auditoría y la memoria no entran

```gherkin
Dado un proyecto con auditoría y con memoria escritas
Cuando se arma su expediente
Entonces ninguna de las dos aparece
```

**Cómo validarlo:** armar el expediente de este repositorio, que tiene las dos.
- **Aprobado cuando:** no aparecen. Es el caso de «que NO pase» de esta historia.

### CA-05 — Se puede pedir hasta cierto alcance

```gherkin
Dado un proyecto con varias fases
Cuando se pide el expediente hasta una fase
Entonces salen los documentos hasta ahí, y se dice cuáles quedaron fuera
```

**Cómo validarlo:** pedirlo completo y acotado, y comparar.
- **Aprobado cuando:** lo acotado **dice qué dejó fuera**; recortar en silencio es lo mismo que perder.

### Criterios transversales

- Armar el expediente **no modifica** ningún documento.
- Un proyecto sin documentos lo dice, en vez de devolver un expediente vacío.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Recuperación | El expediente se rehace desde el texto cuantas veces se pida (`DA-01`) |
| Rendimiento | Un proyecto de mil documentos se arma sin que el usuario se pregunte si se colgó |
| Claridad | La lista de lo que falta se lee sin abrir nada más |

---

## 6. Diseño y referencias

- Funcionalidad `F-025` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- Requisito `RF-25` del [análisis](../../../../cvds/analisis-requisitos/README.md).
- Decisión que la gobierna: [`DA-09`](../../../../cvds/diseno/decisiones-de-arquitectura.md), para lo que sigue en la `HU-002`.
- De dónde salen los documentos: [plataforma/nucleo/importacion/moldes.py](../../../../plataforma/nucleo/importacion/moldes.py), que es quien reconoce qué es cada archivo.

---

## 7. Tareas técnicas derivadas

1. Declarar el orden del ciclo, tipo por tipo.
2. Juntar los documentos de un proyecto en ese orden.
3. Calcular qué falta contra lo que el ciclo espera.
4. Marcar los que traen espacios sin llenar.
5. Acotar por alcance, diciendo qué queda fuera.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| Por abrir | Esta historia | Sin abrir |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | `EP-010`: sin los documentos traídos no hay qué juntar |
| **Riesgo 1** | Que el orden del ciclo no esté definido para todos los tipos. Se declara en la especificación, y lo que no encaje se dice en vez de acomodarse |
| **Riesgo 2** | Que «lo que falta» se calcule contra una lista escrita a mano que envejece. Sale de las etapas del ciclo, que ya están escritas |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ La duda 5 resuelta: la auditoría y la memoria quedan fuera.
- ☑ El módulo Expediente tiene especificación aprobada: [documentacion/expediente/spec.md](../../../expediente/spec.md), el 2026-08-31.
- ☑ Está declarado el orden del ciclo, tipo por tipo: la §5.1 de la especificación.

## 11. Definition of Done

- ☐ Los cinco criterios con veredicto y evidencia.
- ☐ Un expediente real armado, sobre este repositorio.
- ☐ Comprobado que la auditoría y la memoria no entraron.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | Casi | Necesita lo que Importación ya trajo |
| Negociable | Sí | El orden del ciclo y el alcance se pueden ajustar |
| Valiosa | Sí | Es lo que hoy cuesta un día |
| Estimable | Sí | Es leer, ordenar y comparar contra una lista |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se arma el expediente de este repositorio y se mira |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-08-31 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz |
| 2026-08-31 | Nace de `F-025`, con la épica `EP-012` aprobada ese día |
