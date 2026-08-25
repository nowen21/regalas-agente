# HU-001 — Registrar cada acción que se hace

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-001 |
| **Épica** | [EP-009 Todo lo que se hace queda registrado](../epica.md) |
| **Funcionalidad** | `F-018` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Auditoría |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Solicitante** | El usuario |
| **Estado** | Aprobada el 2026-08-25 por Ing. José Dúmar Jiménez Ruíz |

---

## 2. Narrativa

- **Como** quien responde por lo que se hace en sus proyectos
- **Quiero** que quede constancia de cada cambio, con quién, cuándo y sobre qué
- **Para** poder demostrar meses después qué pasó, sin depender de mi memoria

---

## 3. Contexto y descripción

Cada vez que un módulo cambia algo, entrega la acción a la auditoría. Se guarda antes de que el cambio surta efecto, y no se puede editar después.

La acción responde **qué se hizo**; el enlace a la sesión permite leer después **por qué**.

### 3.1 Reglas de negocio

- `RN-1` Lo registrado no se edita ni se borra.
- `RN-2` Si el registro no se puede escribir, la acción no se ejecuta.
- `RN-3` Ninguna credencial entra al registro.
- `RN-4` Se registra la acción, no la conversación de la sesión.

### 3.2 Supuestos

- Que registrar la acción alcanza, y que el porqué queda cubierto por lo que la sesión escribe.

### 3.3 Fuera de alcance

- Consultar lo registrado con filtros, que es `F-019` de la versión 4.
- Guardar la transcripción de las sesiones, que se sigue guardando aparte.

---

## 4. Criterios de aceptación

### CA-01 — Toda acción que cambia algo queda registrada

```gherkin
Dado cualquier módulo que cambia algo
Cuando ejecuta la acción
Entonces queda un registro con qué se hizo, sobre qué, quién y cuándo
```

### CA-02 — Lo registrado no se puede editar ni borrar

```gherkin
Dado un registro ya escrito
Cuando alguien intenta modificarlo o borrarlo
Entonces no se puede
Y el intento queda registrado
```

### CA-03 — Sin constancia no hay efecto

```gherkin
Dado que el registro no se puede escribir
Cuando un módulo intenta ejecutar una acción
Entonces la acción se detiene
Y se avisa por qué
```

**Cómo validarlo:** dejar el registro sin poder escribirse y pedir una acción cualquiera. Nada debe cambiar.

### CA-04 — La acción de una sesión queda enlazada

```gherkin
Dado que la acción ocurre dentro de una sesión de trabajo
Cuando queda registrada
Entonces trae el enlace a esa sesión
Y desde ahí se puede leer lo que la sesión dejó escrito
```

### CA-05 — Ninguna credencial entra al registro

```gherkin
Dado un texto que contiene algo parecido a una clave
Cuando se registra la acción
Entonces la clave queda tapada
Y el nombre de la variable queda legible
```

### Criterios transversales

- Una sesión que no dejó nada escrito deja el enlace vacío, y eso se muestra como dato.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Trazabilidad | `RNF-12`: toda acción dice quién, cuándo y sobre qué |
| Seguridad | `RNF-05`: ninguna credencial escrita |
| Recuperación | El registro es texto: se lee sin la plataforma |

---

## 6. Diseño y referencias

- Especificación: [documentacion/auditoria/spec.md](../../../auditoria/spec.md).
- Decisión que la gobierna: [`DA-08`](../../../../cvds/diseno/decisiones-de-arquitectura.md).
- Modelo de datos: el registro y su campo de sesión, sección 3 del [modelo](../../../../cvds/diseno/modelo-de-datos.md).

---

## 7. Tareas técnicas derivadas

1. Escribir el registro como texto que solo se agrega.
2. Tapar credenciales antes de escribir.
3. Detener la acción si el registro no se puede escribir.
4. Enlazar la acción con la sesión que la produjo.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| D · Todo lo que se hace queda registrado | Esta historia | Sin abrir |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | `EP-008 HU-001`, para saber en qué proyecto ocurrió la acción |
| **Riesgo 1** | Que registrar antes de ejecutar haga lento el trabajo. Se mide en el uso |
| **Riesgo 2** | Que el registro crezca y no se pueda consultar. Se indexa desde el principio |

---

## 10. Definition of Ready

- ☑ La especificación del módulo está aprobada.
- ☑ Está resuelto qué se audita de una sesión.
- ☑ Los cinco criterios son comprobables.

## 11. Definition of Done

- ☐ Los cinco criterios con veredicto y evidencia.
- ☐ Comprobado que ninguna acción cambia algo sin quedar registrada.
- ☐ Comprobado que el registro no se puede editar.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | Casi | Necesita que exista el registro de proyectos |
| Negociable | Sí | Qué acciones se registran se puede ajustar |
| Valiosa | Sí | Es lo que permite demostrar qué pasó |
| Estimable | Sí | Es escribir, tapar y enlazar |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se prueba haciendo acciones y mirando el registro |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-08-25 | Nace de `F-018`. Ese mismo día se decide que se registran las acciones más lo que la sesión dejó escrito |
