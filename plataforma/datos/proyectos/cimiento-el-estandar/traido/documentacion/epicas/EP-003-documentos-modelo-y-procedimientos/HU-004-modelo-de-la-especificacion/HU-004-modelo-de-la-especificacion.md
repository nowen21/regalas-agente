# HU-004 — Crear el modelo de la especificación de un módulo

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-004 |
| **Épica / Feature** | [EP-003 Documentos modelo y procedimientos guiados](../epica.md) |
| **Módulo / Componente** | Documentos modelo |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Pendiente |
---

## 2. Narrativa

- **Como** quien va a construir un módulo
- **Quiero** un modelo para escribir qué debe hacer ese módulo antes de programarlo
- **Para** que el código responda a algo acordado y no a lo que yo entendí ese día

---

## 3. Contexto y descripción

La historia de usuario dice qué pide quien encarga. La especificación dice cómo funciona el módulo por dentro: qué datos guarda, qué reglas del negocio garantiza, qué permisos exige, qué pasa en cada camino.

Sin ese documento, el código termina siendo la única fuente de la verdad, y lo que decidió quien lo escribió se pierde en cuanto esa persona no está.

Es también la que hace cumplible la regla de que sin especificación acordada no hay código: hoy esa regla existe, pero el documento que exige no tiene modelo.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Hay un modelo para la especificación de un módulo, y vive en un solo lugar |
| RN-02 | Cubre alcance, contexto, reglas de negocio, datos, comportamiento, permisos, pruebas y decisiones tomadas |
| RN-03 | Ninguna sección se borra: la que no aplica se deja diciendo por qué no aplica |
| RN-04 | Se aprueba antes de escribir código del módulo |
| RN-05 | Cuando un módulo consume a otro, el cruce se registra en los dos documentos |
| RN-06 | El módulo que ya tiene código y no tiene especificación se documenta antes de tocarlo |

### 3.2 Supuestos

- Un módulo tiene una sola especificación, aunque tenga muchas historias de usuario y muchas fases.

### 3.3 Fuera de alcance

- Los modelos de la fase. Eso es HU-003.
- El procedimiento que guía su redacción. Eso es HU-006.

---

## 4. Criterios de aceptación

### CA-01 — El modelo existe y cubre lo que el código necesita saber

```gherkin
Dado que se va a construir un módulo
Cuando se busca el modelo de su especificación
Entonces existe
Y trae secciones para datos, reglas de negocio, comportamiento, permisos y pruebas
```

**Cómo validarlo:**

1. Abrir la carpeta de modelos del estándar y ubicar el de la especificación.
2. Recorrer sus secciones. Resultado esperado: están las cinco nombradas, cada una con qué va adentro.
3. Llenarlo para un módulo pequeño de prueba. Resultado esperado: no hace falta inventar ninguna sección.
- **Aprobado cuando:** el modelo alcanza para describir un módulo sin agregarle secciones.

### CA-02 — Lo que no aplica queda dicho, no borrado

```gherkin
Dado que un módulo no tiene interfaz de usuario
Cuando se llena su especificación
Entonces la sección de interfaz queda diciendo por qué no aplica
```

**Cómo validarlo:**

1. Llenar el modelo para un módulo sin interfaz.
2. Ir a la sección de interfaz. Resultado esperado: sigue ahí, con la razón escrita.
3. Preguntarse si se sabe que se pensó en eso. Resultado esperado: sí, porque está escrito.
- **Aprobado cuando:** se distingue lo que no aplica de lo que se olvidó.

### CA-03 — El cruce entre módulos queda en los dos lados

```gherkin
Dado que la especificación de un módulo declara que consume otro
Cuando se abre la especificación del módulo consumido
Entonces ahí está registrado quién lo consume y desde cuándo
```

**Cómo validarlo:**

1. Llenar dos especificaciones de prueba, una que consuma a la otra.
2. Declarar el consumo en la primera. Resultado esperado: hay una sección para eso.
3. Abrir la segunda. Resultado esperado: hay dónde registrar que la primera la consume, y queda escrito.
- **Aprobado cuando:** ningún cruce queda escrito en un solo lado.

### CA-04 — Toda regla de negocio dice de dónde baja

```gherkin
Dado que se escribe una regla de negocio en la especificación de un módulo
Cuando se llena la sección de reglas de negocio
Entonces la regla dice de dónde baja, con el identificador del requisito, la historia o la decisión
Y la que no tenga procedencia no se escribe ahí: se sube a la historia que corresponda
```

**Cómo validarlo:**

1. Escribir una regla que baje de un requisito con identificador. Resultado esperado: cabe en el molde y se sabe quién la pidió sin salir del documento.
2. Intentar escribir una regla que no pida nadie. Resultado esperado: el hueco del origen queda a la vista, y el modelo dice qué hacer con ella.
3. Leer una especificación escrita antes de este cambio. Resultado esperado: le falta un dato, no queda inválida.
- **Aprobado cuando:** una regla sin fuente no puede entrar en silencio.

> **Se pide un identificador, no una frase.** «Lo pidió el cliente» no se puede seguir hasta ninguna parte, y el programa que lo comprueba —otra historia, en EP-004— necesita algo que exista de verdad para poder buscarlo.

### Criterios de aceptación transversales

- [ ] **Límites** — un módulo que ya existe sin especificación tiene un camino definido para documentarse.
- [ ] **No regresión** — las especificaciones ya escritas siguen siendo válidas.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Claridad** | Quien no conoce el módulo entiende qué hace leyendo solo este documento |
| **Completitud** | Cubre lo que el código necesita saber, sin volverse un manual |
| **Trazabilidad** | Cada afirmación técnica se puede rastrear hasta dónde quedó implementada |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, es un documento de texto.
- **Documento funcional:** [documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/epica.md](../epica.md), §5.1 y §5.4 fila 6.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Escribir el modelo con sus secciones.
- [ ] Definir dónde vive la especificación de cada módulo dentro del proyecto.
- [ ] Agregar la sección del cruce entre módulos, con sus dos lados.
- [ ] Definir el camino para documentar un módulo que ya tiene código.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-003-HU-004-el-origen-de-la-regla-de-negocio](A-EP-003-HU-004-el-origen-de-la-regla-de-negocio/README.md) | CA-04 | Cerrada 2026-08-16 (v22.0.0) |
| [B-EP-003-HU-004-el-origen-de-las-57-reglas](B-EP-003-HU-004-el-origen-de-las-57-reglas/README.md) | Las 57 reglas de esta casa, con su origen | Cerrada 2026-08-18 |

**Los tres primeros criterios no tienen fase**, y es a propósito: el modelo ya existía cuando la épica se descompuso. Se dan por cumplidos por el documento mismo, no por una fase que lo construyera.

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
| Dependencia | HU-001, porque el modelo usa la marca acordada | Alto |
| Dependencia | EP-001, porque la regla que exige la especificación vive ahí | Alto |
| Riesgo | Que la especificación repita lo que ya dice la historia de usuario | Cada dato tiene un solo dueño; la especificación enlaza la historia |
| Riesgo | Que se escriba después del código, para cumplir | La regla la exige antes, y el procedimiento se detiene ahí |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] El modelo existe y se probó con un módulo real
- [ ] Lo que no aplica se escribe, no se borra
- [ ] El cruce entre módulos queda en los dos lados
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Necesita la marca de HU-001 |
| **N**egociable | Sí | Las secciones se pueden discutir |
| **V**aliosa | Sí | Sin ella, la regla que exige especificación no se puede cumplir |
| **E**stimable | Sí | Es un documento |
| **S**mall (pequeña) | Sí | Un modelo |
| **T**esteable | Sí | Se prueba escribiendo la especificación de un módulo real |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
| 2026-08-16 | Ing. José Dúmar Jiménez Ruíz | Nace el `CA-04`: el §4 pedía el porqué de cada regla de negocio y nunca su procedencia, así que una regla que no pedía nadie entraba sin resistencia. Lo reportó `shopnest-mesa`. Se abre y cierra la fase `A` (v22.0.0) |
