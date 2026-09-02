# HU-005 — Configurar qué rige en cada proyecto

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-005 |
| **Épica** | [EP-008 Los proyectos se administran desde un solo lugar](../epica.md) |
| **Funcionalidad** | `F-004` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Proyectos |
| **Tipo** | Funcional |
| **Prioridad** | Should |
| **Estimación** | S |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-09-01, con sus tres criterios probados |
---

## 2. Narrativa

- **Como** quien tiene proyectos de tamaños muy distintos
- **Quiero** elegir por proyecto qué reglas opcionales rigen
- **Para** que uno pequeño no cargue con lo que solo necesita uno grande

---

## 3. Contexto y descripción

**Lo obligatorio no se puede apagar.** Es la única exigencia dura de esta historia, y la razón de que exista: sin ella, «configurable» quiere decir «el estándar rige cuando conviene», que es no tener estándar.

**Qué es opcional lo dice el estándar, no la plataforma.** Una regla es opt-in cuando ella lo dice (`*opt-in*`) o cuando lo dice la cabecera de su capítulo, y entonces rige a todas las suyas. Guardar acá una lista propia sería una segunda verdad que envejece. Medido: **49 de 257** reglas son opcionales.

**Y cada opción es una forma más de que dos proyectos no se parezcan.** Está en la ficha, y no se resuelve con código: por eso lo que se enciende y se apaga queda escrito, con fecha y con quién.

### 3.1 Reglas de negocio

- `RN-1` Una regla opcional se enciende y se apaga por proyecto.
- `RN-2` **Una obligatoria no se puede apagar, y se dice por qué.**
- `RN-3` De fábrica, lo opcional viene apagado.
- `RN-4` La configuración vive en el proyecto, no en la base.
- `RN-5` **Ante la duda, una regla es obligatoria.**

### 3.2 Supuestos

- Que el estándar marca lo opcional como el capítulo 20 manda.

### 3.3 Fuera de alcance

- **Elegir moldes por proyecto.** Se deja para cuando haya más de un molde por documento.
- La pantalla.

---

## 4. Criterios de aceptación

### CA-01 — Una regla opcional se activa y desactiva por proyecto

```gherkin
Dada una regla marcada opt-in
Cuando se enciende en un proyecto
Entonces rige allí, con la fecha y quién lo hizo
```

**Cómo validarlo:** encendiendo y apagando.
- **Aprobado cuando:** el estado cambia y queda escrito con fecha y autor.

### CA-02 — Una obligatoria no se puede desactivar, y se dice por qué

```gherkin
Dada una regla que no está marcada opt-in
Cuando se intenta apagar
Entonces no se hace, y se dice que apagarla volvería el estándar una sugerencia
```

**Cómo validarlo:** intentándolo con una obligatoria.
- **Aprobado cuando:** no se hace. **Es el criterio que decide.**

### CA-03 — El agente recibe lo configurado allá, no lo de otro proyecto

```gherkin
Dados dos proyectos con configuraciones distintas
Cuando se pide lo que rige en uno
Entonces sale lo suyo y nada del otro
```

**Cómo validarlo:** con dos proyectos a la vez.
- **Aprobado cuando:** ninguno se cruza.

### Criterios transversales

- Un proyecto que no configuró nada **se dice así**, no como uno con cero reglas.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Integridad | Lo obligatorio nunca se apaga |
| Portabilidad | La configuración viaja con el repositorio |

---

## 6. Diseño y referencias

- Funcionalidad `F-004` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- [Especificación del módulo Proyectos](../../../proyectos/spec.md).
- Capítulo `20`, que fija cómo se marca una regla opcional.

---

## 7. Tareas técnicas derivadas

1. Hallar qué reglas son opcionales, leyendo `base/`.
2. Escribir el estado en el proyecto, con fecha y quién.
3. Rechazar apagar una obligatoria.
4. Entregar lo de ese proyecto y de ninguno más.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [V-EP-008-HU-005-lo-obligatorio-no-se-apaga](V-EP-008-HU-005-lo-obligatorio-no-se-apaga/estado-fase.md) | Los tres CA | Cerrada el 2026-09-01: **Cumple** |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | `F-001`, que conecta el proyecto, y `F-005`, que escribe las reglas |
| **Riesgo 1** | **Que se marque como opcional algo que no lo es.** Pasó: buscar la marca en todo el archivo daba 52 reglas, entre ellas `02·F0` |
| **Riesgo 2** | Que cada opción aleje dos proyectos. Está declarado en la ficha y no se resuelve acá |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ La épica aprobada.
- ☑ El cuerpo de reglas marca lo opcional.

## 11. Definition of Done

- ☑ Los tres criterios con veredicto y evidencia.
- ☑ Comprobado que una obligatoria no se apaga.
- ☑ La lista de opcionales leída nombre por nombre.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | Sí | Lee `base/` y escribe en el proyecto |
| Negociable | Sí | Dónde vive el archivo se puede ajustar |
| Valiosa | Sí | Un proyecto pequeño no debería cargar con todo |
| Estimable | Sí | Es leer marcas y escribir una tabla |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se enciende, se apaga y se vuelve a leer |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz, y cerrada el mismo día |
