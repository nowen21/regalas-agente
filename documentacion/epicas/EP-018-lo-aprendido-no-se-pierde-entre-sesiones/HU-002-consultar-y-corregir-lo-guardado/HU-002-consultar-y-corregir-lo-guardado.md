# HU-002 — Consultar y corregir lo guardado

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-002 |
| **Épica** | [EP-018 Lo aprendido no se pierde entre sesiones](../epica.md) |
| **Funcionalidad** | `F-024` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Memoria |
| **Tipo** | Funcional |
| **Prioridad** | Should |
| **Estimación** | S |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-09-01, con sus tres criterios probados |
---

## 2. Narrativa

- **Como** el usuario, que no ve lo que el agente recuerda
- **Quiero** poder consultarlo, corregirlo y darlo de baja
- **Para** que un recuerdo equivocado deje de regir sin tener que adivinar cuál era

---

## 3. Contexto y descripción

**Es un problema de confianza antes que de comodidad**, y así está escrito en la ficha de `F-024`: *«hoy solo el agente ve lo que recuerda»*.

**Corregir conserva lo que decía antes.** Un recuerdo corregido cuenta dos cosas, y las dos sirven: lo que vale hoy, y lo que se creía ayer. Borrar la segunda deja la corrección sin explicación.

**Dar de baja marca, no borra.** Es la misma razón por la que las reglas del estándar se derogan en vez de desaparecer (`20·M11`): lo que ya no vale sigue siendo la respuesta a por qué algo se hizo como se hizo.

### 3.1 Reglas de negocio

- `RN-1` Se busca por palabra, en el título y en el cuerpo.
- `RN-2` **Corregir conserva lo que decía antes**, debajo y marcado.
- `RN-3` **Dar de baja no borra**: marca el recuerdo y lo deja fuera de lo que se le entrega al agente.
- `RN-4` Una búsqueda sin coincidencias **lo dice**.

### 3.2 Supuestos

- Que los recuerdos están guardados como los deja la `HU-001`.

### 3.3 Fuera de alcance

- **La pantalla.** Van órdenes de consola, como el resto de esta etapa.
- Revisar solo si un recuerdo sigue siendo cierto.

---

## 4. Criterios de aceptación

### CA-01 — Se busca por palabra

```gherkin
Dado un conjunto de recuerdos
Cuando se busca una palabra
Entonces salen los que la traen, en el título o en el cuerpo
```

**Cómo validarlo:** buscando algo que está y algo que no.
- **Aprobado cuando:** salen los que corresponden, y el vacío se dice con palabras.

### CA-02 — Corregir deja constancia de qué decía antes

```gherkin
Dado un recuerdo guardado
Cuando se corrige su texto
Entonces queda el texto nuevo
Y debajo, marcado, lo que decía antes
```

**Cómo validarlo:** corrigiendo y leyendo el archivo.
- **Aprobado cuando:** están los dos textos. **Es el criterio que decide.**

### CA-03 — Dar de baja no lo borra

```gherkin
Dado un recuerdo vigente
Cuando se da de baja
Entonces el archivo sigue estando
Y deja de salir entre los vigentes
```

**Cómo validarlo:** dando de baja y pidiendo las dos listas.
- **Aprobado cuando:** sale en todos y no sale en los vigentes.

### Criterios transversales

- El resumen dice cuántos hay, cuántos vigentes y cuántos de baja.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Integridad | Ningún recuerdo se borra |
| Trazabilidad | Toda corrección deja qué decía antes |

---

## 6. Diseño y referencias

- Funcionalidad `F-024` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md).
- [Especificación del módulo Memoria](../../../memoria/spec.md).
- Señal [`S-110`](../../../senales.md), por lo del resultado vacío.

---

## 7. Tareas técnicas derivadas

1. Buscar por palabra.
2. Corregir conservando lo anterior.
3. Dar de baja con su marca.
4. El resumen.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [Q-EP-018-HU-002-corregir-conserva-lo-que-decia-antes](Q-EP-018-HU-002-corregir-conserva-lo-que-decia-antes/estado-fase.md) | Los tres CA | Cerrada el 2026-09-01: **Cumple** |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | La `HU-001`, que guarda |
| **Riesgo 1** | Que corregir borre lo anterior. Queda debajo |
| **Riesgo 2** | Que dar de baja borre el archivo. Solo le pone la marca |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ La épica aprobada el 2026-09-01.
- ☑ La `HU-001` cerrada.

## 11. Definition of Done

- ☑ Los tres criterios con veredicto y evidencia.
- ☑ Comprobado que corregir conserva lo anterior.
- ☑ Comprobado que dar de baja no borra.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | No | Necesita lo que guarda la `HU-001` |
| Negociable | Sí | Cómo se marca la baja se puede ajustar |
| Valiosa | Sí | Hoy el usuario no ve lo que el agente recuerda |
| Estimable | Sí | Es leer, marcar y escribir texto |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se corrige y se lee el archivo |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz, y cerrada el mismo día |
