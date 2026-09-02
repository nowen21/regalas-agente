# HU-001 — Guardar lo aprendido

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-001 |
| **Épica** | [EP-018 Lo aprendido no se pierde entre sesiones](../epica.md) |
| **Funcionalidad** | `F-023` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Memoria |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | S |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-09-01, con sus tres criterios probados |
---

## 2. Narrativa

- **Como** quien ya corrigió lo mismo tres veces
- **Quiero** que lo aprendido quede guardado donde no se borra
- **Para** que la sesión siguiente no arranque en blanco

---

## 3. Contexto y descripción

**Es la mitad del problema original**, y la ficha de `F-023` lo dice así: *«sin esto, cada sesión vuelve a empezar»*.

**El lugar ya está decidido y no lo decide esta historia:** `01·C19` manda que la memoria del agente sea un archivo del repositorio, uno por recuerdo, con su línea en el índice de [`historico-chat/memory/`](../../../../historico-chat/memory/memory.md). El almacén de la herramienta queda vacío. Lo que faltaba es poder escribir y leer ahí sin abrir los archivos a mano.

**Guardar no pisa.** Perder un recuerdo por reusar un nombre es el peor fallo posible en un módulo cuyo único trabajo es no perder nada.

### 3.1 Reglas de negocio

- `RN-1` Un recuerdo vive donde no se borra: un archivo del repositorio.
- `RN-2` **Guardar no pisa** lo que ya está: si el nombre existe, se avisa.
- `RN-3` Cada recuerdo guardado le pone su línea al índice.
- `RN-4` Ningún recuerdo guarda credenciales.
- `RN-5` Si no hay nada del tema, **se dice** en vez de inventar.

### 3.2 Supuestos

- Que la carpeta `historico-chat/memory/` existe.

### 3.3 Fuera de alcance

- **Decidir qué merece recordarse.** Eso lo decide quien escribe.
- La pantalla.

---

## 4. Criterios de aceptación

### CA-01 — Lo guardado en una sesión se recupera en la siguiente

```gherkin
Dado un recuerdo guardado
Cuando se piden los vigentes
Entonces está
```

**Cómo validarlo:** guardando y volviendo a leer desde cero.
- **Aprobado cuando:** sale, con su título y su cuerpo.

### CA-02 — Lo de un proyecto no se mezcla con el de otro

```gherkin
Dado que se pide la memoria de un proyecto
Cuando se lee
Entonces solo salen los recuerdos de ese proyecto
```

**Cómo validarlo:** con dos carpetas de proyecto distintas.
- **Aprobado cuando:** ninguno se cruza.

### CA-03 — Si no hay nada del tema, se dice

```gherkin
Dado que se busca una palabra que no está
Cuando se lee la respuesta
Entonces dice que no hay nada de ese tema
```

**Cómo validarlo:** buscando algo que no existe.
- **Aprobado cuando:** lo dice con palabras, no devuelve un vacío.

### Criterios transversales

- Guardar con un nombre que ya existe **avisa y no pisa**.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Integridad | Ningún recuerdo se pierde al guardar otro |
| Claridad | Un resultado vacío se distingue de una falla |

---

## 6. Diseño y referencias

- Funcionalidad `F-023` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- Regla `01·C19`, que decide dónde vive la memoria.
- [Especificación del módulo Memoria](../../../memoria/spec.md).

---

## 7. Tareas técnicas derivadas

1. Leer la carpeta y el índice.
2. Guardar sin pisar.
3. Poner la línea del índice.
4. Decir cuando no hay nada.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [P-EP-018-HU-001-lo-guardado-vuelve-en-la-sesion-siguiente](P-EP-018-HU-001-lo-guardado-vuelve-en-la-sesion-siguiente/estado-fase.md) | Los tres CA | Cerrada el 2026-09-01: **Cumple** |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | `F-001`, el almacén |
| **Riesgo 1** | Que guardar pise un recuerdo. **No pisa:** avisa |
| **Riesgo 2** | Que un recuerdo equivocado siga rigiendo. **Se acepta y se declara:** nada lo revisa solo |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ La épica aprobada el 2026-09-01.
- ☑ La carpeta de recuerdos existe y tiene contenido.

## 11. Definition of Done

- ☑ Los tres criterios con veredicto y evidencia.
- ☑ Comprobado que guardar no pisa.
- ☑ Comprobado que un tema sin recuerdos se dice.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | Sí | Los archivos ya existen |
| Negociable | Sí | El formato del recuerdo se puede ajustar |
| Valiosa | Sí | Es la mitad del problema que originó el proyecto |
| Estimable | Sí | Es leer y escribir texto |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se guarda y se vuelve a leer |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz, y cerrada el mismo día |
