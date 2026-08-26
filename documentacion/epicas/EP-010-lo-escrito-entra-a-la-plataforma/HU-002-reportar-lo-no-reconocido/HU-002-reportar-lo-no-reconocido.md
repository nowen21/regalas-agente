# HU-002 — Reportar lo que no sigue ningún molde

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-002 |
| **Épica** | [EP-010 Lo que ya está escrito entra a la plataforma](../epica.md) |
| **Funcionalidad** | `F-028` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Importación |
| **Tipo** | Funcional |
| **Prioridad** | Should |
| **Estimación** | S |
| **Solicitante** | El usuario |
| **Estado** | Cerrada el 2026-08-25, con sus criterios probados |

---

## 2. Narrativa

- **Como** quien trae un proyecto con años de documentación
- **Quiero** saber qué quedó por fuera y dónde está
- **Para** decidir yo qué hacer con eso, en vez de perderlo sin enterarme

---

## 3. Contexto y descripción

Traer reconoce lo que sigue un molde. El resto no entra, y **eso no es una falla: es un dato**. Lo que no se reconoce suele ser lo más valioso, porque son las notas que nadie escribió con molde.

Adivinar su forma sería peor que no traerlo: ensuciaría lo que sí sirve.

### 3.1 Reglas de negocio

- `RN-1` Lo que no se reconoce no se transforma ni se acomoda.
- `RN-2` Nada se pierde en silencio: se dice qué es y dónde está.
- `RN-3` Si todo se reconoció, se dice, en vez de mostrar una lista vacía.

### 3.2 Supuestos

- Que lo no reconocido es minoría y cabe en una lista legible.

### 3.3 Fuera de alcance

- Convertir lo no reconocido a un molde, ahora o después.

---

## 4. Criterios de aceptación

### CA-01 — Lo no reconocido queda listado con su ruta

```gherkin
Dado un proyecto con documentos que no siguen ningún molde
Cuando termina la traída
Entonces se lista cada uno con la ruta del archivo
Y se dice cuántos son
```

### CA-02 — Nada se transforma sin que el usuario lo diga

```gherkin
Dado un documento que no se reconoce
Cuando termina la traída
Entonces no entró a la plataforma
Y su archivo de origen no cambió
```

### CA-03 — Si todo se reconoció, se dice

```gherkin
Dado un proyecto donde todo siguió un molde conocido
Cuando termina la traída
Entonces se dice que no quedó nada por fuera
Y no se muestra una lista vacía
```

### Criterios transversales

- El reporte queda guardado con la acción de traer, para poder volver a mirarlo.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Usabilidad | `RNF-07`: el reporte se entiende sin conocer el proyecto |

---

## 6. Diseño y referencias

- Especificación: [documentacion/importacion/spec.md](../../../importacion/spec.md), sección 6.
- Pantalla `P-11` del [diseño de interfaz](../../../../cvds/diseno/diseno-de-interfaz.md).

---

## 7. Tareas técnicas derivadas

1. Acumular lo no reconocido durante la traída, con su ruta.
2. Mostrar el reporte al terminar, y guardarlo con la acción.
3. Decir explícitamente cuando no quedó nada por fuera.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [F · Lo que no se reconoce se reporta](F-EP-010-HU-002-lo-que-no-se-reconoce-se-reporta/README.md) | Esta historia | Cerrada el 2026-08-25. Los cuatro criterios con veredicto |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | `HU-001` de esta épica: primero hay que traer |
| **Riesgo** | Que la lista sea tan larga que nadie la lea. Si pasa, se agrupa por carpeta y se dice cuántos hay de cada clase |

---

## 10. Definition of Ready

- ☑ La especificación del módulo está aprobada.
- ☑ `HU-001` está definida.
- ☑ Los tres criterios son comprobables.

## 11. Definition of Done

- ☐ Los tres criterios con veredicto y evidencia.
- ☐ Probado sobre este repositorio, con cuántos quedaron por fuera.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | No del todo | Va pegada a la traída |
| Negociable | Sí | Cómo se agrupa el reporte se puede ajustar |
| Valiosa | Sí | Evita perder en silencio lo que no encaja |
| Estimable | Sí | Es acumular y mostrar |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se prueba con documentos que no siguen molde |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-08-25 | Nace de `F-028`, al aprobarse el inventario de Cimiento |
