# HU-010 — Crear el glosario de la terminología del estándar

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-010 |
| **Épica / Feature** | [EP-003 Documentos modelo y procedimientos guiados](../epica.md) |
| **Módulo / Componente** | Documentos modelo |
| **Tipo** | Técnica |
| **Prioridad** | Should |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Terminada el 2026-08-14 |

---

## 2. Narrativa

- **Como** quien lee el estándar por primera vez
- **Quiero** un sitio donde cada término esté definido en una línea
- **Para** entender un documento sin ir preguntando qué significa cada palabra

---

## 3. Contexto y descripción

La terminología del estándar está repartida en las reglas que usan cada palabra. Para saber qué es una especificación hay que encontrar la regla que la exige; para saber qué es una señal, otra; para saber qué es una fase, un capítulo entero.

El caso que lo destapó: el usuario preguntó qué significaba "spec". La respuesta tomó tres intentos y terminó cambiando una regla, porque el término además estaba en inglés.

Con el glosario escrito se ve, de una sola pasada, qué términos siguen en inglés sin necesidad. Por eso va antes de tocar los nombres de los roles: se cambian todos de una vez y no uno por sesión.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Cada término del estándar se define en una línea, entendible sin saber del tema |
| RN-02 | Cada entrada dice quién lo escribe, dónde vive y qué regla lo manda |
| RN-03 | El glosario es un anexo, no una regla: no lleva checklist |
| RN-04 | El término que se queda en otro idioma dice por qué no tiene traducción usada |
| RN-05 | Un término que no aparece en ninguna regla ni plantilla no entra: no es del estándar |

### 3.2 Supuestos

- Son unos treinta términos, en cuatro grupos: la cadena de trabajo, las reglas, lo que comprueba y lo que se guarda.

### 3.3 Fuera de alcance

- Renombrar los roles, que se hace después con el glosario a la vista.
- Definir términos del dominio de un proyecto: eso va en su capa propia.

---

## 4. Criterios de aceptación

### CA-01 — Cada término está definido en una línea

```gherkin
Dado que alguien encuentra un término del estándar que no conoce
Cuando lo busca en el glosario
Entonces está, definido en una línea que se entiende sin saber del tema
```

**Cómo validarlo:**

1. Tomar cinco términos de distintos capítulos.
2. Buscarlos en el glosario. Resultado esperado: los cinco están.
3. Dárselos a leer a alguien que no conoce el estándar. Resultado esperado: puede decir con sus palabras qué es cada uno.
- **Aprobado cuando:** entender un término deja de exigir leer un capítulo.

### CA-02 — Cada entrada dice dónde vive y qué regla lo manda

```gherkin
Dado que se lee una entrada del glosario
Cuando se quiere ir al detalle
Entonces la entrada dice qué regla lo exige y dónde vive el documento
```

**Cómo validarlo:**

1. Tomar tres entradas.
2. Seguir lo que dicen. Resultado esperado: la regla existe y el documento está donde dice.
- **Aprobado cuando:** el glosario lleva al detalle en un paso.

### CA-03 — Se ve qué quedó en otro idioma

```gherkin
Dado que el glosario está escrito
Cuando se recorre entero
Entonces se puede listar qué términos siguen en otro idioma y por qué
```

**Cómo validarlo:**

1. Recorrer el glosario y anotar los términos que no están en español.
2. Leer su justificación. Resultado esperado: cada uno dice por qué no tiene traducción usada.
3. Contrastar con los nombres de los roles. Resultado esperado: se ve cuáles hay que cambiar.
- **Aprobado cuando:** queda la lista de lo que falta traducir.

### Criterios de aceptación transversales

- [ ] **Límites** — un término que cambia de nombre queda con su nombre viejo enlazado, para que las citas viejas resuelvan.
- [ ] **No regresión** — el glosario no redefine lo que ya dice una regla: la enlaza.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Claridad** | Cada definición se entiende sin saber del tema |
| **Mantenimiento** | El glosario enlaza a la regla dueña; no copia su texto |
| **Brevedad** | Una línea por término |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** el pendiente 21, con los cuatro grupos y la lista de términos.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Listar los términos por grupo.
- [ ] Escribir cada definición en una línea, con su regla y su ubicación.
- [ ] Marcar los que siguen en otro idioma y por qué.
- [ ] Enlazarlo desde donde se entra al estándar.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué cubre | CA | Estado |
|---|---|---|---|
| [documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/A-EP-003-HU-010-glosario-de-la-terminologia/](A-EP-003-HU-010-glosario-de-la-terminologia/README.md) | El glosario entero y el inventario de lo que sigue en otro idioma | CA-01, CA-02, CA-03 | Cerrada el 2026-08-14 |

Una sola fase para los tres criterios: los tres se validan sobre el mismo documento y ninguno se puede probar sin él (`02·F12.10`).

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
| Dependencia | EP-001, porque los términos salen de las reglas | Alto |
| Riesgo | Que el glosario repita el texto de las reglas y se desincronice | Define en una línea y enlaza; no copia |
| Riesgo | Que se llene de términos que nadie usa | Solo entra lo que aparece en una regla o una plantilla |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] El glosario existe con los términos de los cuatro grupos
- [ ] Cada entrada dice dónde vive y qué regla lo manda
- [ ] Queda la lista de lo que sigue en otro idioma
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | Se escribe leyendo lo que ya existe |
| **N**egociable | Sí | Qué términos entran se puede discutir |
| **V**aliosa | Sí | Entrar al estándar deja de exigir leerlo entero |
| **E**stimable | Sí | Unos treinta términos |
| **S**mall (pequeña) | Sí | Un documento |
| **T**esteable | Sí | Se prueba dándoselo a leer a alguien de fuera |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde el hallazgo H-8 del 2026-08-14 |
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Se descompone en la fase A y se cierra: el glosario existe, con 67 términos y el inventario de lo que falta traducir |
