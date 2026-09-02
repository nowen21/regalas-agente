# HU-003 — Medir el tiempo que se gasta revisando

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-003 |
| **Épica** | [EP-011 Lo que se repite sale a la luz](../epica.md) |
| **Funcionalidad** | `F-032` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Medición |
| **Tipo** | Funcional |
| **Prioridad** | Could |
| **Estimación** | S |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-09-01, con sus dos criterios probados |
---

## 2. Narrativa

- **Como** quien quiere saber si todo esto sirvió
- **Quiero** ver cuánto tiempo se gasta revisando lo entregado, y cómo cambia
- **Para** saberlo en vez de suponerlo

---

## 3. Contexto y descripción

**La medición inicial debió tomarse antes de empezar y no se tomó.** Lo dice la propia ficha de `F-032`, y al construirlo se confirmó: lo más viejo que quedó grabado ya es el proyecto en marcha.

Lo que hay es la **reconstruida**: el tramo más viejo del histórico. **No es un antes, es el comienzo de lo que quedó grabado**, y sale escrito en cada comparación. Una línea base que se presenta como un antes de verdad hace que cualquier mejora parezca mayor de lo que es.

**Medir no le cuesta nada al usuario.** El tiempo sale de las horas que el enganche del estándar ya escribe en cada mensaje: entre la respuesta del agente y el mensaje siguiente hay un hueco, y ese hueco es lo que se tardó en leer. Pedirle al usuario que cronometre sería cobrarle la medición, y la ficha lo prohíbe.

**Medido acá el 2026-09-01:** 1615 revisiones, 144 horas, mediana de 99 segundos — y todo dentro de un solo mes.

### 3.1 Reglas de negocio

- `RN-1` **Medir no obliga al usuario a anotar nada.**
- `RN-2` La línea base sale **siempre marcada como reconstruida**.
- `RN-3` Un hueco mayor a dos horas no es revisión: se descarta y se cuenta.
- `RN-4` Un mensaje sin hora se dice aparte; no se le inventa una.
- `RN-5` **Con un solo mes no se compara**, y se explica por qué.

### 3.2 Supuestos

- Que el histórico está indexado y sus mensajes traen hora.

### 3.3 Fuera de alcance

- **Reconstruir la medición inicial de verdad.** No se puede, y decirlo es parte del entregable.
- Medir el tiempo del agente.

---

## 4. Criterios de aceptación

### CA-01 — Hay una medición inicial contra la cual comparar

```gherkin
Dado un histórico con varios meses
Cuando se pide la línea base
Entonces sale el tramo más viejo con datos suficientes
Y viene marcada como reconstruida
```

**Cómo validarlo:** con dos meses de sesiones.
- **Aprobado cuando:** sale la más vieja y dice que es reconstruida. **Es el criterio que decide.**

### CA-02 — Medir no obliga al usuario a anotar nada a mano

```gherkin
Dado el histórico tal como el enganche lo escribe
Cuando se mide
Entonces el tiempo sale de las horas que ya están
```

**Cómo validarlo:** midiendo sin agregar ningún dato.
- **Aprobado cuando:** el número sale sin que nadie anote nada.

### Criterios transversales

- **Con un solo mes no se compara**, y se dice por qué en vez de devolver un cero.
- Los huecos larguísimos se descartan, y se dice cuántos.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Honestidad | La línea base nunca se presenta como un antes de verdad |
| Costo | Medir no puede costar más que lo que ahorra |

---

## 6. Diseño y referencias

- Funcionalidad `F-032` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- [Especificación del módulo Medición](../../../medicion/spec.md).
- Señal [`S-113`](../../../senales.md): un tiempo supuesto y uno medido se escriben igual.

---

## 7. Tareas técnicas derivadas

1. Los huecos entre la respuesta y el mensaje siguiente.
2. Descartar los larguísimos y los de un segundo.
3. Juntar por mes, con mediana.
4. La línea base, marcada.
5. Negarse a comparar cuando no hay con qué.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [Y-EP-011-HU-003-la-linea-base-dice-que-es-reconstruida](Y-EP-011-HU-003-la-linea-base-dice-que-es-reconstruida/estado-fase.md) | Los dos CA | Cerrada el 2026-09-01: **Cumple** |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | `F-018` y `F-030`, y de que el histórico esté indexado |
| **Riesgo 1** | **Que la línea base se lea como un antes de verdad.** Sale marcada, cada vez |
| **Riesgo 2** | Que un almuerzo se cuente como cuatro horas de lectura. Se descarta y se cuenta aparte |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ La épica aprobada.
- ☑ El histórico indexado, con 3665 de 3720 mensajes con hora.

## 11. Definition of Done

- ☑ Los dos criterios con veredicto y evidencia.
- ☑ Comprobado que la línea base dice que es reconstruida.
- ☑ Comprobado que con un mes no se compara.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | No | Necesita el histórico indexado |
| Negociable | Sí | Los topes de descarte se pueden ajustar |
| Valiosa | Sí | Es lo que responde si el proyecto sirvió |
| Estimable | Sí | Es restar horas |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se mide y se compara |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz, y cerrada el mismo día. Se confirmó al construirla que la medición inicial no existe |
