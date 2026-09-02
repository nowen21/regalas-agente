# HU-003 — Caducar la aprobación cuando el texto cambia

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-003 |
| **Épica** | [EP-017 Una aprobación dice sobre qué texto](../epica.md) |
| **Funcionalidad** | `F-017` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Aprobaciones |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | S |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-09-01, con sus tres criterios probados |
---

## 2. Narrativa

- **Como** quien confía en que algo aprobado sigue siendo lo que se aprobó
- **Quiero** que editar un documento aprobado le quite la aprobación
- **Para** que nadie construya sobre una autorización que ya no cubre lo que hay

---

## 3. Contexto y descripción

**Esta historia salió de un caso real**, y está escrito en la ficha de `F-017`: *«se aprobaron tres documentos y al día siguiente el cambio de producto los dejó sin valor»*. **Nada avisó.**

**Y lo que la vuelve posible es la huella** que guarda la `HU-001`. Sin ella no hay forma de saber si el texto cambió: solo que alguien firmó alguna vez.

**Nada se borra.** La aprobación caducada se queda: es la historia de qué se autorizó y cuándo.

### 3.1 Reglas de negocio

- `RN-1` **Si la huella no coincide, la aprobación caducó.**
- `RN-2` **Se dice cuánto cambió** respecto de lo aprobado.
- `RN-3` **La aprobación anterior no se borra.**
- `RN-4` Si el documento desaparece, también caduca.

### 3.2 Supuestos

- Que la aprobación se registró con su huella.

### 3.3 Fuera de alcance

- **El diff completo.** Lo da el control de versiones, que ya lo hace bien.
- Volver a aprobar solo. Eso lo decide una persona.

---

## 4. Criterios de aceptación

### CA-01 — Editar un documento aprobado le quita la aprobación

```gherkin
Dado un documento aprobado
Cuando se edita su texto
Entonces su estado pasa a caducada
```

**Cómo validarlo:** aprobando y editando.
- **Aprobado cuando:** caduca. **Es el criterio que decide.**

### CA-02 — Se ve qué cambió respecto de lo aprobado

```gherkin
Dado un documento cuya aprobación caducó
Cuando se pregunta qué cambió
Entonces se dice cuántos caracteres hay de más y de menos
```

**Cómo validarlo:** editando para agregar y para quitar.
- **Aprobado cuando:** los dos números salen.

### CA-03 — La aprobación anterior no se borra

```gherkin
Dado un documento aprobado dos veces
Cuando se consulta su historia
Entonces están las dos
Y la que manda es la última
```

**Cómo validarlo:** aprobando, editando y volviendo a aprobar.
- **Aprobado cuando:** quedan dos, y manda la última.

### Criterios transversales

- Si el documento desaparece, también caduca, y se dice.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Integridad | Ninguna aprobación se borra |
| Claridad | Se dice cuánto cambió, no solo que cambió |

---

## 6. Diseño y referencias

- Funcionalidad `F-017` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- Requisito `RF-17` del [análisis](../../../../cvds/analisis-requisitos/README.md).

---

## 7. Tareas técnicas derivadas

1. Comparar la huella de lo que hay con la de la última aprobación.
2. Medir cuánto cambió.
3. Conservar la historia.
4. Tratar el documento que desapareció.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [O-EP-017-HU-003-editar-quita-la-aprobacion-y-no-borra-la-historia](O-EP-017-HU-003-editar-quita-la-aprobacion-y-no-borra-la-historia/estado-fase.md) | Los tres CA | Cerrada el 2026-09-01: **Cumple** |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | La `HU-001`, que guarda la huella |
| **Riesgo 1** | Que caducar borre la anterior. Nada se borra |
| **Riesgo 2** | Que un cambio de tipografía caduque una aprobación. **Se acepta:** una aprobación responde por el texto exacto, no por lo que significa |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ La épica aprobada el 2026-09-01.
- ☑ La `HU-001` cerrada.

## 11. Definition of Done

- ☑ Los tres criterios con veredicto y evidencia.
- ☑ Comprobado que editar caduca.
- ☑ Comprobado que la anterior no se borra.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | No | Necesita la huella de la `HU-001` |
| Negociable | Sí | Cómo se mide el cambio se puede ajustar |
| Valiosa | Sí | Salió de un caso real que costó tres documentos |
| Estimable | Sí | Es comparar dos huellas |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se aprueba, se edita y se mira |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz, y cerrada el mismo día |
