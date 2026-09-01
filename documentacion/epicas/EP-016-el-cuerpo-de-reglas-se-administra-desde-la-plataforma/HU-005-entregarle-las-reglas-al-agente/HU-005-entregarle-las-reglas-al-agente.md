# HU-005 — Entregarle las reglas al agente

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-005 |
| **Épica** | [EP-016 El cuerpo de reglas se administra desde la plataforma](../epica.md) |
| **Funcionalidad** | `F-009` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Reglas |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-09-01, con sus tres criterios probados |
---

## 2. Narrativa

- **Como** el agente que abre sesión en un proyecto
- **Quiero** recibir las reglas que rigen ahí, sin pedirlas
- **Para** trabajar bajo las reglas de ese proyecto desde el primer mensaje

---

## 3. Contexto y descripción

**Lo que se entrega es el texto, no un resumen.** Un resumen de una regla es otra regla, y la que el agente obedecería sería la del resumen.

**Y si esto no responde, la fuente sigue ahí.** El cuerpo de reglas son archivos en el proyecto: quien no pueda usar la plataforma los lee y trabaja igual. Esta pieza **acelera y ordena; no es un intermediario sin el cual no se puede**.

Por eso, cuando algo falla, se dice dónde está la fuente. **Devolver una lista vacía se leería como «este proyecto no tiene reglas»**, que es la peor respuesta posible.

### 3.1 Reglas de negocio

- `RN-1` **Se entrega el texto**, no un resumen.
- `RN-2` **Se dice bajo qué versión rige.**
- `RN-3` **Si no se puede, se dice dónde está la fuente.**
- `RN-4` La fuente se nombra **siempre**, se haya podido o no.

### 3.2 Supuestos

- Que el proyecto tiene su cuerpo de reglas instalado.

### 3.3 Fuera de alcance

- **Que el agente las obedezca.** Eso lo cubre `F-020`, y ya está construido.
- Filtrar qué reglas le tocan a cada quién.

---

## 4. Criterios de aceptación

### CA-01 — Al abrir, el agente tiene las reglas sin pedirlas

```gherkin
Dado un proyecto con su cuerpo de reglas
Cuando se piden sus reglas
Entonces salen los capítulos con su texto
Y se dice cuántas rigen y bajo qué versión
```

**Cómo validarlo:** sobre este repositorio.
- **Aprobado cuando:** sale el texto, no un resumen.

### CA-02 — Entregarlas no demora más de dos segundos

```gherkin
Dado un cuerpo de reglas completo
Cuando se entrega
Entonces tarda menos de dos segundos
Y el tiempo se reporta
```

**Cómo validarlo:** midiendo sobre este repositorio, que tiene 248 vigentes.
- **Aprobado cuando:** el número queda escrito y está por debajo.

### CA-03 — Si la plataforma no está, se avisa y se trabaja leyendo la fuente

```gherkin
Dado un proyecto del que no se pueden entregar las reglas
Cuando se piden
Entonces se dice por qué
Y se dice dónde está la fuente
```

**Cómo validarlo:** con un proyecto sin cuerpo de reglas.
- **Aprobado cuando:** se dice, y **no se devuelve una lista vacía**. Es el criterio que decide.

### Criterios transversales

- La fuente se nombra también cuando todo salió bien.
- Las rutas salen relativas al proyecto.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Rendimiento | **Menos de dos segundos**, y el número escrito |
| Disponibilidad | Sin esto, la fuente sigue siendo legible |

---

## 6. Diseño y referencias

- Funcionalidad `F-009` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- Requisito `RF-09` del [análisis](../../../../cvds/analisis-requisitos/README.md).

---

## 7. Tareas técnicas derivadas

1. Recorrer los capítulos en su orden.
2. Leer su texto.
3. Contar las vigentes.
4. Medir cuánto tardó.
5. Decir dónde está la fuente, pase lo que pase.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [K-EP-016-HU-005-las-reglas-llegan-y-la-fuente-sigue-ahi](K-EP-016-HU-005-las-reglas-llegan-y-la-fuente-sigue-ahi/estado-fase.md) | Los tres CA | Cerrada el 2026-09-01: **Cumple** |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | `F-006`, que aporta el lector del cuerpo de reglas |
| **Riesgo 1** | Que tarde demasiado y se vuelva un estorbo al abrir. Se mide |
| **Riesgo 2** | Que un fallo se lea como «no hay reglas». Se dice dónde está la fuente |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ La épica aprobada el 2026-09-01.
- ☑ `F-006` cerrada.

## 11. Definition of Done

- ☑ Los tres criterios con veredicto y evidencia.
- ☑ Medido sobre este repositorio, con el tiempo escrito.
- ☑ Comprobado que un fallo dice dónde está la fuente.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | Casi | Necesita el lector de `F-006` |
| Negociable | Sí | Cómo se entrega el texto se puede ajustar |
| Valiosa | Sí | Es lo que hace que el agente trabaje bajo las reglas del proyecto |
| Estimable | Sí | Es leer archivos y contar |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se mide sobre este repositorio |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz, y cerrada el mismo día |
