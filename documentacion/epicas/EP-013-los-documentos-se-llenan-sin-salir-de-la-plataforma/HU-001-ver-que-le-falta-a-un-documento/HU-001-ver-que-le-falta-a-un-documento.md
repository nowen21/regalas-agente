# HU-001 — Ver qué le falta a un documento

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-001 |
| **Épica** | [EP-013 Los documentos se llenan sin salir de la plataforma](../epica.md) |
| **Funcionalidad** | `F-014` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md) |
| **Módulo** | Ciclo de vida |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Solicitante** | El usuario |
| **Estado** | Terminada el 2026-09-01, con sus cinco criterios probados |
---

## 2. Narrativa

- **Como** quien tiene que dejar un documento del ciclo listo para entregar
- **Quiero** ver qué molde sigue y qué huecos le faltan por llenar
- **Para** saber cuánto falta sin releer el archivo entero

---

## 3. Contexto y descripción

Cada documento del ciclo sigue un molde de `plantillas/`, y el molde marca sus huecos con `«…»`, que es lo que exige [`13·DOC19`](../../../../base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md). Hoy nadie sabe cuántos le faltan a un documento sin abrirlo y recorrerlo con los ojos, y eso no se hace: **el expediente del 2026-08-31 encontró 31 documentos con huecos sin llenar** que se venían entregando así.

**Los huecos no son todos iguales, y solo uno es cierto.** Se midió antes de construir:

| Clase | Cómo se escribe | Qué se hace |
|---|---|---|
| **Cierto** | `«…»` | Se cuenta y se pregunta |
| **Posible** | `«NOMBRE»` que también está en el molde | Se lista aparte, fuera de la cuenta |

**El de nombre no se distingue de una cita** en un documento escrito, porque acá se cita con esas mismas comillas. De 341 marcas en las 130 historias reales, 75 están en el molde y **ninguna** sigue en la línea del molde: son etiquetas del autor, no huecos.

Se listan igual porque cuando `F-011` cree documentos desde el molde, en la versión 5, el documento **será** el molde y entonces sí serán ciertos.

**Y hay una tercera clase que no es un hueco para una persona.** `«RUTA-ESTANDAR»`, con 134 apariciones, la reemplaza la instalación ([validadores/instalar.py](../../../../validadores/instalar.py)). Contarla como pendiente le pone al usuario 134 preguntas que él no responde.

Esta historia **solo mira**. Escribir es la [HU-002](../HU-002-llenar-un-hueco-desde-la-plataforma/HU-002-llenar-un-hueco-desde-la-plataforma.md).

### 3.1 Reglas de negocio

- `RN-1` El molde de un documento se decide por **su tipo**, que el módulo Importación ya reconoce por nombre y ubicación.
- `RN-2` **Solo el hueco cierto entra en la cuenta.** El posible se lista aparte, porque en un documento escrito no se distingue de una cita.
- `RN-3` **Lo que llena la instalación no se cuenta como pendiente del usuario**, y se dice aparte para que nadie crea que se perdió.
- `RN-4` Un documento cuyo tipo no se reconoce **lo dice**. No se le atribuye un molde parecido.
- `RN-5` Mirar no modifica nada.

### 3.2 Supuestos

- Que los moldes de `plantillas/` marcan sus huecos con la convención de `13·DOC19`. Si un molde no la usa, esta historia lo revela en vez de taparlo.

### 3.3 Fuera de alcance

- Llenar el hueco, que es la `HU-002`.
- Juzgar si lo que ya está escrito es bueno: se cuenta lo que falta, no la calidad de lo que hay.
- Los documentos que no son del ciclo.

---

## 4. Criterios de aceptación

### CA-01 — Se dice qué molde sigue el documento

```gherkin
Dado un documento del ciclo traído a la plataforma
Cuando se pide qué le falta
Entonces se dice qué tipo de documento es y qué molde le corresponde
```

**Cómo validarlo:** con un `plan_trabajo.md` y un `epica.md` de este repositorio.
- **Aprobado cuando:** el molde nombrado es el del tipo, no uno parecido.

### CA-02 — Se listan los huecos, con cuántos son y dónde

```gherkin
Dado un documento con huecos sin llenar
Cuando se pide qué le falta
Entonces sale cuántos son
Y cada uno con su línea y con el texto que lo rodea
```

**Cómo validarlo:** sobre los 31 documentos que el expediente marcó incompletos.
- **Aprobado cuando:** la cuenta coincide con contar la marca a mano, y cada hueco se puede ubicar sin abrir el archivo.

### CA-03 — Solo el hueco cierto entra en la cuenta

```gherkin
Dado un documento con un hueco «…» y con una marca «NOMBRE» que tambien esta en su molde
Cuando se pide que le falta
Entonces la cuenta dice uno, que es el cierto
Y el de nombre sale en una lista aparte, de posibles
```

**Por qué así.** Medido el 2026-09-01 sobre las 130 historias reales: de 341 marcas, 75 están en el molde y **ninguna sigue en la línea del molde**. Son el autor citando con las mismas comillas, no huecos. Contarlas daría por incompleto un documento bien escrito.

**Cómo validarlo:** correr sobre las 130 historias y comprobar que la cuenta de ciertos no las incluye.
- **Aprobado cuando:** las dos listas salen separadas, y la de ciertos coincide con lo que ya cuenta el expediente.

### CA-04 — Lo que llena la instalación no se cuenta como pendiente

```gherkin
Dado un documento con «RUTA-ESTANDAR»
Cuando se pide qué le falta
Entonces esa marca no entra en la cuenta de lo que el usuario debe llenar
Y se dice aparte que la reemplaza la instalación
```

**Cómo validarlo:** contar con y sin ella sobre `plantillas/`, donde aparece 134 veces.
- **Aprobado cuando:** no está en la cuenta del usuario **y** tampoco desaparece en silencio.

### CA-05 — Un documento de tipo desconocido lo dice

```gherkin
Dado un archivo que el módulo Importación no reconoce
Cuando se pide qué le falta
Entonces se dice que no se le conoce molde
Y no se le aplica el molde de otro tipo
```

**Cómo validarlo:** con un archivo de nombre inventado dentro de `documentacion/`.
- **Aprobado cuando:** lo dice. Es el caso de «que NO pase» de esta historia.

### Criterios transversales

- Pedir qué falta **no modifica** el documento: se compara el archivo antes y después.
- Un documento sin huecos lo dice, en vez de devolver una lista vacía sin explicación.

---

## 5. Requisitos no funcionales

| Frente | Exigencia |
|---|---|
| Rendimiento | Los 762 documentos de este repositorio se recorren sin que el usuario se pregunte si se colgó |
| Claridad | La lista se lee sin abrir el documento |
| Recuperación | Todo se calcula del texto cuando se pide. Nada que reconstruir (`DA-01`) |

---

## 6. Diseño y referencias

- Funcionalidad `F-014` del [inventario](../../../../cvds/analisis-requisitos/inventario-funcionalidades.md), criterio `CA-2`.
- Requisito `RF-14` del [análisis](../../../../cvds/analisis-requisitos/README.md).
- Decisión que la gobierna: [`DA-12`](../../../../cvds/diseno/decisiones-de-arquitectura.md), que nombra a `RF-14`.
- Quién reconoce el tipo: [plataforma/nucleo/importacion/moldes.py](../../../../plataforma/nucleo/importacion/moldes.py).
- Quién ya cuenta huecos, y de dónde se parte: [plataforma/nucleo/expediente/core.py](../../../../plataforma/nucleo/expediente/core.py).

---

## 7. Tareas técnicas derivadas

1. Mapear cada tipo de documento con su molde de `plantillas/`.
2. Encontrar los huecos de un texto, distinguiendo los que tienen nombre de los que no.
3. Apartar los que llena la instalación, y decirlos aparte.
4. Dar la cuenta y la ubicación de cada uno.
5. Decir cuando un tipo no se reconoce.

---

## 8. Fases que la implementan

| Fase | Qué hace | Estado |
|---|---|---|
| [A-EP-013-HU-001-los-huecos-de-un-documento-se-ven](A-EP-013-HU-001-los-huecos-de-un-documento-se-ven/estado-fase.md) | Los cinco CA | Cerrada el 2026-09-01: **Cumple** |

---

## 9. Dependencias y riesgos

| Qué | Cuál |
|---|---|
| **Depende de** | `EP-010`: sin documentos traídos no hay qué mirar |
| **Riesgo 1** | Que un tipo de documento no tenga molde en `plantillas/`. Se dice, en vez de asignarle el más parecido |
| **Riesgo 2** | Que la cuenta infle con marcas que no son huecos. Ya pasó una vez: contar `«texto»` daba 559 documentos incompletos en vez de 31. Por eso se midió antes de construir, y por eso el de nombre no entra en la cuenta |

---

## 10. Definition of Ready

- ☑ La funcionalidad está en el inventario, con su ficha.
- ☑ La épica aprobada el 2026-09-01.
- ☑ Las clases de hueco, medidas sobre las 130 historias reales: solo `«…»` es cierto.
- ☑ El módulo Ciclo de vida, con [especificación aprobada](../../../ciclo-de-vida/spec.md) el 2026-09-01.

## 11. Definition of Done

- ☑ Los cinco criterios con veredicto y evidencia.
- ☑ Los documentos incompletos de este repositorio, listados: **54, con 77 huecos**.
- ☑ Comprobado que ningún documento cambia al mirarlo.
- ☑ La diferencia con la cuenta del expediente, explicada con números.

## 12. Validación INVEST

| Letra | Cumple | Por qué |
|---|---|---|
| Independiente | Casi | Necesita lo que Importación ya reconoce |
| Negociable | Sí | Qué se muestra de cada hueco se puede ajustar |
| Valiosa | Sí | Es lo que hoy nadie hace: contar antes de entregar |
| Estimable | Sí | Es leer texto y buscar una marca |
| Pequeña | Sí | Cabe en una fase |
| Verificable | Sí | Se corre sobre los 31 documentos ya identificados |

## 13. Bitácora

| Fecha | Qué pasó |
|---|---|
| 2026-09-01 | **Aprobada** por Ing. José Dúmar Jiménez Ruíz |
| 2026-09-01 | Nace de `F-014`, con la épica `EP-013` aprobada ese día |
