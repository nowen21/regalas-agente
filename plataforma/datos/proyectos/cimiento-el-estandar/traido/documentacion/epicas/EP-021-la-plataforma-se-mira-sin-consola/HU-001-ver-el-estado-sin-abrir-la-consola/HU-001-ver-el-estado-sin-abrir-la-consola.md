# HU-001 — Ver el estado sin abrir la consola

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-001 |
| **Épica** | [EP-021 La plataforma se mira sin consola](../epica.md) |
| **Funcionalidad** | Ninguna nueva: **la mitad de pantalla** de `F-012`, `F-016`, `F-021`, `F-024`, `F-029` y `F-030` |
| **Módulos** | Avisos, Ciclo de vida, Comprobaciones, Aprobaciones, Memoria |
| **Tipo** | Funcional |
| **Prioridad** | Should |
| **Estimación** | M |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-09-02, con sus tres criterios probados |
---

## 2. Narrativa

- **Como** quien quiere saber cómo va todo sin escribir una orden
- **Quiero** ver el tablero, las fases, lo comprobado, lo aprobado y lo recordado
- **Para** que enterarse no dependa de acordarse de qué orden se escribe

---

## 3. Contexto y descripción

**Trece módulos y solo dos con pantalla.** Y las fichas de cuatro funcionalidades piden pantalla explícitamente.

**La consola no resuelve el problema que esas funcionalidades vinieron a resolver.** `F-029` pide *que enterarse no dependa de ir a mirar*, y una orden sigue pidiendo ir a mirar. `F-012` dice que sirve *para ver todas las fases a la vez*, y doscientas líneas en una terminal no se ven a la vez.

**Son pantallas de solo mirar.** Aprobar, corregir un recuerdo o abrir una fase son cambios de estado, y `00·N1` los quiere con su confirmación: siguen por consola.

### 3.1 Reglas de negocio

- `RN-1` **Una pantalla vacía dice que está vacía, y por qué.**
- `RN-2` **Ninguna convierte un «no se sabe» en un cero.**
- `RN-3` Cada pantalla dice **qué no muestra**.
- `RN-4` Ninguna calcula: piden a su módulo.
- `RN-5` Nada sale a la red.
- `RN-6` Un proyecto que no existe da 404, no una pantalla rota.

### 3.2 Supuestos

- Que el proyecto está conectado y sus documentos se pueden leer.

### 3.3 Fuera de alcance

- **Cambiar algo desde la pantalla.**
- **Seis módulos siguen sin pantalla:** Auditoría, Medición, Expediente, Reglas, Seguridad y Almacén.

---

## 4. Criterios de aceptación

### CA-01 — Las cinco pantallas responden y se llega a ellas

```gherkin
Dado un proyecto conectado
Cuando se abre su ficha
Entonces hay enlace a sus cuatro pantallas
Y al tablero se llega desde cualquier pantalla
```

**Cómo validarlo:** pidiendo las cinco y mirando los enlaces.
- **Aprobado cuando:** las cinco responden y ninguna hay que escribirla a mano.

### CA-02 — Una pantalla vacía dice que está vacía

```gherkin
Dado un proyecto sin fases, sin aprobaciones y sin memoria
Cuando se abren sus pantallas
Entonces cada una dice que no hay nada, y por qué
```

**Cómo validarlo:** con un proyecto recién conectado.
- **Aprobado cuando:** ninguna sale en blanco. **Es el criterio que decide.**

### CA-03 — Ninguna convierte un «no se sabe» en un cero

```gherkin
Dado un proyecto sin datos, y una fase que no dice desde cuándo está quieta
Cuando se leen las pantallas
Entonces dicen «sin datos» y «no lo dice»
```

**Cómo validarlo:** con los dos casos.
- **Aprobado cuando:** en ninguna sale un cero donde no se sabe.

### Criterios transversales

- Cada pantalla dice **qué deja por fuera**.
- Un proyecto que no existe da 404.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Sin conexión | Nada sale a la red |
| Honestidad | Las advertencias van impresas donde se leen los datos |

---

## 6. Diseño y referencias

- Las fichas de `F-012`, `F-024`, `F-029` y `F-030`, que piden pantalla.
- Las especificaciones de [Avisos](../../../avisos/spec.md), [Ciclo de vida](../../../ciclo-de-vida/spec.md), [Comprobaciones](../../../comprobaciones/spec.md), [Aprobaciones](../../../aprobaciones/spec.md) y [Memoria](../../../memoria/spec.md).
- Señal [`S-107`](../../../senales.md), por lo del «no se sabe».

---

## 7. Tareas técnicas derivadas

1. Las cinco vistas, que piden y no calculan.
2. Las cinco plantillas, con su caso vacío.
3. Las rutas, antes de la comodín de proyectos.
4. Los enlaces desde la ficha del proyecto y desde la cabecera.
5. Las §7 de las cinco especificaciones.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [Z-EP-021-HU-001-lo-vacio-se-dice](Z-EP-021-HU-001-lo-vacio-se-dice/estado-fase.md) | Los tres CA | Cerrada el 2026-09-02: **Cumple** |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | `EP-019` y `EP-020`, que calculan lo que se muestra |
| **Riesgo 1** | **Que una pantalla vacía se lea como una falla.** Cada una lo dice |
| **Riesgo 2** | Que una pantalla dé a entender que muestra todo. Cada una dice qué deja por fuera |
| **Riesgo 3** | Que la lógica se duplique en la vista. Las vistas piden, no calculan |

---

## 10. Definition of Ready

- ☑ `EP-019` y `EP-020` cerradas.
- ☑ Medido: trece módulos, dos con pantalla.
- ☑ La épica aprobada el 2026-09-02.

## 11. Definition of Done

- ☑ Los tres criterios con veredicto y evidencia.
- ☑ Comprobado que lo vacío se dice.
- ☑ Las cinco §7 puestas al día.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | No | Muestra lo que otras dos épicas calculan |
| Negociable | Sí | Cuántas pantallas y cuáles se puede ajustar |
| Valiosa | Sí | Cierra la mitad que falta de seis funcionalidades |
| Estimable | Sí | Son cinco vistas que piden y muestran |
| Pequeña | No del todo | Son cinco pantallas; caben en una fase porque ninguna calcula |
| Verificable | Sí | Se piden y se lee lo que sale |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-09-02 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz, y cerrada el mismo día |
