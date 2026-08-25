# HU-001 — Conectar un proyecto

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-001 |
| **Épica** | [EP-008 Los proyectos se administran desde un solo lugar](../epica.md) |
| **Funcionalidad** | `F-001` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Proyectos |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Solicitante** | El usuario |
| **Estado** | Ready |

---

## 2. Narrativa

- **Como** quien administra varios proyectos a la vez
- **Quiero** registrar un proyecto en la plataforma, con dónde vive su código
- **Para** tener dónde colgar su documentación y poder verlo junto a los demás

---

## 3. Contexto y descripción

Es la primera historia de la plataforma: sin proyectos conectados no hay nada que administrar. Registrar guarda el nombre y la ruta del código, y crea la carpeta donde vivirá la documentación de ese proyecto.

**No toca el código del proyecto.** Registrar es una anotación de la plataforma, no una intervención.

### 3.1 Reglas de negocio

- `RN-1` Registrar un proyecto no modifica nada dentro de su carpeta.
- `RN-2` Dos proyectos no pueden apuntar a la misma ruta.
- `RN-3` La acción queda registrada en la auditoría.

### 3.2 Supuestos

- Basta la ruta del código para ubicar el proyecto.

### 3.3 Fuera de alcance

- Traer su documentación, que es `HU-001` de [EP-010](../../EP-010-lo-escrito-entra-a-la-plataforma/epica.md).
- Configurar qué reglas rigen ahí, que es de la versión 5.

---

## 4. Criterios de aceptación

### CA-01 — Un proyecto queda registrado

```gherkin
Dado un nombre y una ruta que existe en la máquina
Cuando el usuario conecta el proyecto
Entonces queda registrado y aparece en la lista
Y se crea su carpeta de documentación en la plataforma
```

**Cómo validarlo:** conectar una carpeta cualquiera y comprobar que aparece en la lista, y que su carpeta de documentación existe.

### CA-02 — Una ruta que no existe no se registra

```gherkin
Dado una ruta que no existe
Cuando el usuario intenta conectar el proyecto
Entonces no se registra
Y se responde con la ruta que se buscó
```

### CA-03 — Registrar dos veces la misma ruta avisa

```gherkin
Dado una ruta ya registrada por otro proyecto
Cuando el usuario intenta conectarla de nuevo
Entonces no se registra
Y se dice qué proyecto ya la tiene
```

### CA-04 — Registrar no toca el código

```gherkin
Dado un proyecto con archivos propios
Cuando se conecta
Entonces ningún archivo de su carpeta cambia, se mueve ni se crea
```

**Cómo validarlo:** comparar la carpeta antes y después. Es el caso de «que NO pase» de esta historia.

### Criterios transversales

- La acción queda en la auditoría, con quién y cuándo.
- Un proyecto sin control de versiones se registra, con la advertencia de que su código no tiene respaldo.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Recuperación | Lo registrado queda como texto, y el índice se puede reconstruir (`RNF-04`) |
| Disponibilidad | Funciona sin red (`RNF-03`) |

---

## 6. Diseño y referencias

- Especificación: [documentacion/proyectos/spec.md](../../../proyectos/spec.md).
- Pantallas `P-01` y `P-02` del [diseño de interfaz](../../../../cvds/diseno/diseno-de-interfaz.md).
- Decisiones que la gobiernan: [`DA-01`](../../../../cvds/diseno/decisiones-de-arquitectura.md) y [`DA-02`](../../../../cvds/diseno/decisiones-de-arquitectura.md).

---

## 7. Tareas técnicas derivadas

1. Levantar la plataforma con su almacenamiento de texto y su índice.
2. Guardar el registro de un proyecto y crear su carpeta.
3. Comprobar la ruta y el duplicado antes de guardar.
4. Entregar la acción a la auditoría.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| A · La plataforma levanta y guarda | La base sobre la que se registra | Sin abrir |
| B · Se conecta un proyecto | Esta historia | Sin abrir |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | Nada. Es la primera |
| **Riesgo** | Que la ruta cambie seguido y el registro quede viejo. Lo cubre `HU-002` |

---

## 10. Definition of Ready

- ☑ La especificación del módulo está aprobada.
- ☑ El modelo de datos define la entidad Proyecto.
- ☑ Los cuatro criterios son comprobables.

## 11. Definition of Done

- ☐ Los cuatro criterios con veredicto y evidencia.
- ☐ La acción queda registrada en la auditoría.
- ☐ Comprobado que la carpeta del proyecto no cambió.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | Sí | No necesita otra historia |
| Negociable | Sí | Qué datos se piden al registrar se puede ajustar |
| Valiosa | Sí | Sin esto no hay plataforma |
| Estimable | Sí | Es guardar un registro y crear una carpeta |
| Pequeña | Sí | Cabe en una fase, con su base en la anterior |
| Verificable | Sí | Los cuatro criterios se comprueban mirando la lista y la carpeta |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-08-25 | Nace de `F-001`, al aprobarse el inventario de Cimiento |
