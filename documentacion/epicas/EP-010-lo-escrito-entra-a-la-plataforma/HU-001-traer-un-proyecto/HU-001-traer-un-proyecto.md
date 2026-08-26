# HU-001 — Traer un proyecto con lo que tenga escrito

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-001 |
| **Épica** | [EP-010 Lo que ya está escrito entra a la plataforma](../epica.md) |
| **Funcionalidad** | `F-027` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Importación |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | L |
| **Solicitante** | El usuario |
| **Estado** | Aprobada el 2026-08-25 por Ing. José Dúmar Jiménez Ruíz |

---

## 2. Narrativa

- **Como** quien ya tiene años de documentación escrita en sus proyectos
- **Quiero** traerla a la plataforma tal como está
- **Para** empezar a gobernar el proyecto sin rehacer su historia

---

## 3. Contexto y descripción

Sin esta historia la plataforma arranca vacía y solo sirve para lo que se empiece de cero. Traer recorre la carpeta del proyecto, reconoce los documentos por su forma, y los crea dentro de la plataforma.

**Es la historia de mayor incertidumbre de la versión 1:** no se sabe cuánto de lo escrito se va a reconocer. Por eso su fase va temprano.

### 3.1 Reglas de negocio

- `RN-1` Traer no modifica el proyecto de origen: se copia, no se mueve.
- `RN-2` Traer dos veces no duplica.
- `RN-3` Se muestra qué se va a traer antes de traerlo, y el usuario confirma.
- `RN-4` Lo que falle a mitad se descarta entero: no quedan traídas a medias.

### 3.2 Supuestos

- Que buena parte de lo escrito sigue un molde conocido.

### 3.3 Fuera de alcance

- Reportar lo que no se reconoció, que es `HU-002`.
- Transformar o corregir lo traído.

---

## 4. Criterios de aceptación

### CA-01 — Lo que sigue un molde conocido queda adentro

```gherkin
Dado un proyecto conectado con documentos que siguen un molde
Cuando el usuario los trae
Entonces quedan dentro de la plataforma, cada uno con su tipo
Y se puede ver cuántos entraron
```

### CA-02 — El proyecto de origen queda intacto

```gherkin
Dado un proyecto con su documentación
Cuando se trae a la plataforma
Entonces ningún archivo de su carpeta cambia, se mueve ni se borra
```

**Cómo validarlo:** comparar la carpeta antes y después. Es el caso de «que NO pase» de esta historia.

### CA-03 — Traer dos veces no duplica

```gherkin
Dado un proyecto ya traído
Cuando el usuario lo trae de nuevo
Entonces no se duplica nada
Y se dice qué ya estaba
```

### CA-04 — Se muestra qué se va a traer

```gherkin
Dado un proyecto por traer
Cuando el usuario lo pide
Entonces se muestra qué se encontró y qué se va a traer
Y no se escribe nada hasta que confirme
```

### CA-05 — Una traída que falla no deja nada a medias

```gherkin
Dado que la traída se interrumpe a mitad
Cuando el usuario vuelve a mirar
Entonces no quedó nada de esa pasada
Y el proyecto de origen sigue intacto
```

### Criterios transversales

- La acción queda registrada en la auditoría, con cuántos documentos entraron.
- Probado sobre este mismo repositorio, con sus más de cien fases.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Recuperación | Lo traído queda como texto, y el índice se reconstruye (`RNF-04`) |
| Disponibilidad | Funciona sin red (`RNF-03`) |

---

## 6. Diseño y referencias

- Especificación: [documentacion/importacion/spec.md](../../../importacion/spec.md).
- Decisión que la gobierna: [`DA-10`](../../../../cvds/diseno/decisiones-de-arquitectura.md).
- Pantalla `P-11` del [diseño de interfaz](../../../../cvds/diseno/diseno-de-interfaz.md).

---

## 7. Tareas técnicas derivadas

1. Recorrer la carpeta del proyecto y reconocer los documentos por su forma.
2. Mostrar qué se va a traer, y esperar confirmación.
3. Crear lo reconocido dentro de la plataforma, sin tocar el origen.
4. Descartar entero lo de una pasada que falle.
5. Entregar la acción a la auditoría.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [E · Se trae un proyecto con lo que tenga escrito](E-EP-010-HU-001-se-trae-un-proyecto-con-lo-que-tenga-escrito/README.md) | Esta historia | Cerrada el 2026-08-25, commit `c998695`. 973 documentos traídos del repositorio real |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | `EP-008 HU-001`: solo se trae a un proyecto conectado |
| **Riesgo 1** | Que se reconozca mucho menos de lo esperado. Se sabrá probando, y por eso va temprano |
| **Riesgo 2** | Que traer un proyecto grande demore mucho. Se mide con este repositorio |

---

## 10. Definition of Ready

- ☑ La especificación del módulo está aprobada.
- ☑ Hay un proyecto real para probar.
- ☑ Los cinco criterios son comprobables.

## 11. Definition of Done

- ☐ Los cinco criterios con veredicto y evidencia.
- ☐ Probado sobre este repositorio, con cuántos documentos entraron y cuántos no.
- ☐ Comprobado que el origen quedó intacto.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | Casi | Necesita un proyecto conectado |
| Negociable | Sí | Qué formas se reconocen se puede ampliar |
| Valiosa | Sí | Sin esto la plataforma arranca vacía |
| Estimable | Sí, con margen | Depende de cuántas formas haya que reconocer |
| Pequeña | Al límite | Si reconocer resulta más grande de lo previsto, se parte en dos fases |
| Verificable | Sí | Se prueba trayendo este repositorio |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-08-25 | Nace de `F-027`, al aprobarse el inventario de Cimiento |
