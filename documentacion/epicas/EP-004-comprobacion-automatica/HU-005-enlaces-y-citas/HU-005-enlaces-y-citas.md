# HU-005 — Comprobar los enlaces y las citas a reglas

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-005 |
| **Épica / Feature** | [EP-004 Comprobación automática de lo que no admite discusión](../epica.md) |
| **Módulo / Componente** | Programas de comprobación |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Backlog |

---

## 2. Narrativa

- **Como** quien lee la documentación del trabajo
- **Quiero** que un programa avise cuando un enlace no lleva a ninguna parte o una cita nombra una regla que no existe
- **Para** que la documentación siga sirviendo después de mover, renombrar o dividir un archivo

---

## 3. Contexto y descripción

La documentación se sostiene con enlaces: la fase apunta a su historia, la historia a su épica, la regla a la regla que extiende. En cuanto un archivo se mueve, los enlaces que lo nombraban dejan de funcionar y nadie se entera hasta que alguien hace clic.

Pasa lo mismo con las citas a reglas. El estándar se cita por identificador, y una cita a una regla que no existe manda a quien lee a buscar algo que no está.

Hay tres cosas distintas aquí, y las tres se responden con un sí o un no: que el enlace resuelva, que el índice de una carpeta liste lo que hay dentro, y que el texto del enlace diga dónde vive el archivo. También entra el cruce entre documentos que se referencian: si uno declara que consume a otro, el otro tiene que registrarlo.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Todo enlace a un archivo del proyecto apunta a algo que existe |
| RN-02 | El índice de una carpeta nombra todo lo que cuelga de ella, y no nombra lo que ya no está |
| RN-03 | El texto del enlace es la ruta completa desde la raíz; el destino es la ruta relativa |
| RN-04 | Toda cita a una regla usa el identificador acordado y esa regla existe |
| RN-05 | El cruce entre dos documentos se registra en los dos, o no se registra en ninguno |
| RN-06 | No se comprueban los enlaces a código de un proyecto, porque ese código no vive en el estándar |
| RN-07 | No se comprueban los enlaces de una transcripción de sesión, porque se copia literal y sus rutas son las del chat |

### 3.2 Supuestos

- La estructura de carpetas cambia seguido. La comprobación tiene que resistir eso sin mantenimiento.

### 3.3 Fuera de alcance

- Comprobar que el enlace lleve al lugar correcto dentro del archivo. Se comprueba el archivo, no la sección.
- Corregir los enlaces rotos. Reparar es una decisión y se corre aparte.

---

## 4. Criterios de aceptación

### CA-01 — Un enlace roto se reporta

```gherkin
Dado que un documento enlaza a otro archivo del proyecto
Cuando ese archivo no existe
Entonces la comprobación reporta el enlace con su archivo y su línea
Y la corrida termina con error
```

**Cómo validarlo:**

1. Agregar en un documento de prueba un enlace a un archivo que no existe.
2. Correr la comprobación de coherencia. Resultado esperado: reporta el enlace con la línea exacta y el destino que no resolvió.
3. Borrar el enlace y volver a correr. Resultado esperado: no reporta nada.
- **Aprobado cuando:** el enlace roto se reporta y la corrida termina con error.

### CA-02 — Un índice desactualizado se reporta

```gherkin
Dado que una carpeta tiene su índice
Cuando se agrega un archivo y no se agrega su línea al índice
Entonces la comprobación reporta el archivo que falta
```

**Cómo validarlo:**

1. Crear un archivo dentro de una carpeta que tenga índice, sin tocar el índice.
2. Correr la comprobación. Resultado esperado: reporta que el índice no menciona ese archivo.
3. Agregar la línea al índice y volver a correr. Resultado esperado: no reporta nada.
4. Borrar el archivo dejando su línea en el índice y correr otra vez. Resultado esperado: reporta que el índice nombra algo que ya no existe.
- **Aprobado cuando:** los dos sentidos se reportan.

### CA-03 — Una cita a una regla que no existe se reporta

```gherkin
Dado que un documento cita una regla del estándar por su identificador
Cuando esa regla no existe
Entonces la comprobación lo reporta y nombra el identificador citado
```

**Cómo validarlo:**

1. Escribir en un documento del estándar una cita a un identificador inventado.
2. Correr la comprobación. Resultado esperado: reporta la cita con su línea.
3. Cambiarla por una regla que sí existe y volver a correr. Resultado esperado: no reporta nada.
- **Aprobado cuando:** la cita inventada se reporta y la buena no.

### CA-04 — El cruce escrito en un solo lado se reporta

```gherkin
Dado que la documentación de un módulo declara que consume otro módulo
Cuando el módulo consumido no lo registra en su historial cruzado
Entonces la comprobación lo reporta y nombra los dos documentos
```

**Cómo validarlo:**

1. En la documentación de un módulo de prueba, declarar que consume a otro.
2. Correr la comprobación sin tocar el segundo documento. Resultado esperado: reporta que falta el registro del otro lado.
3. Registrar el cruce en el segundo documento y volver a correr. Resultado esperado: no reporta nada.
- **Aprobado cuando:** el cruce a medias se reporta y el completo no.

### Criterios de aceptación transversales

- [ ] **Límites** — un enlace a una carpeta, uno con ancla y uno que es un ejemplo de formato tienen comportamiento definido.
- [ ] **No regresión** — los enlaces que ya resolvían siguen resolviendo.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Rendimiento** | Recorrer cientos de archivos sin que la espera desanime a correrlo |
| **Compatibilidad** | Funciona con rutas de Windows, con espacios y con tildes |
| **Determinismo** | El mismo árbol de archivos da el mismo resultado |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, la salida es texto en la terminal.
- **Documento funcional:** [documentacion/epicas/EP-004-comprobacion-automatica/epica.md](../epica.md), §5.1.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Recorrer los documentos y resolver cada enlace contra el disco.
- [ ] Comparar el índice de cada carpeta con lo que hay dentro, en los dos sentidos.
- [ ] Indexar dónde vive cada regla y comprobar las citas contra ese índice.
- [ ] Comprobar el formato de dos partes del enlace.
- [ ] Comprobar el cruce entre documentos que se referencian.
- [ ] Escribir pruebas de lo que NO se debe reportar: ejemplos de formato, código de proyecto y transcripciones.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

Todavía no se descompuso en fases.

**Qué documento responde qué**, para no buscar en el que no es:

| Pregunta | Documento |
|---|---|
| Qué se pide y cuándo se da por aceptado | Esta HU |
| Qué se va a hacer, en qué orden y sobre qué archivos | `plan_trabajo.md` de la fase |
| Con qué casos se comprueba cada CA | `plan_pruebas.md` de la fase |
| Qué se ejecutó, con qué resultado, y si el CA quedó cumplido | `resultado_pruebas.md` de la fase |
| En qué estación va y qué la tiene detenida | `estado-fase.md` de la fase |
| Qué quedó hecho al final | `funcionalidad_implementada.md` de la fase |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | HU-003, porque los hallazgos salen con la forma ya definida | Alto |
| Riesgo | Que se reporten como rotos los enlaces que son ejemplos de formato | Se excluyen por su forma y queda escrito por qué |
| Riesgo | Que el formato de dos partes marque tanto que nadie lo mire | Se corre aparte de la comprobación de todos los días |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Los enlaces rotos se reportan
- [ ] Los índices se comprueban en los dos sentidos
- [ ] Las citas a reglas se comprueban contra el índice de reglas
- [ ] El cruce entre documentos se comprueba en los dos lados
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Necesita la forma del hallazgo de HU-003 |
| **N**egociable | Sí | El alcance del formato de dos partes se puede discutir |
| **V**aliosa | Sí | La documentación deja de romperse en silencio |
| **E**stimable | Sí | El alcance lo fija el árbol de archivos |
| **S**mall (pequeña) | Parcial | Son cuatro comprobaciones distintas |
| **T**esteable | Sí | Se prueba rompiendo enlaces a propósito |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
