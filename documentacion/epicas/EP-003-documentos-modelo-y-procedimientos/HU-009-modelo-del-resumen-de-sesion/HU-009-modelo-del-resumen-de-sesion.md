# HU-009 — Crear el modelo del resumen de sesión

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-009 |
| **Épica / Feature** | [EP-003 Documentos modelo y procedimientos guiados](../epica.md) |
| **Módulo / Componente** | Documentos modelo |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | En implementación |

---

## 2. Narrativa

- **Como** quien retoma un trabajo días después
- **Quiero** un modelo fijo donde quede lo que cada sesión dejó
- **Para** encontrarlo sin releer la conversación entera

---

## 3. Contexto y descripción

La transcripción de la sesión guarda lo que se dijo, literal y completo. Es la prueba de lo que pasó, y por eso es larga: nadie la relee.

Lo que quedó —los hallazgos, las decisiones, las preguntas vivas— no tenía forma ni sitio, así que se perdía dentro de esa transcripción. Una sesión entera produjo cinco aprendizajes y nueve pendientes que había que ir a rescatar leyendo el chat.

El modelo existe desde el 2026-08-14, con doce campos por hallazgo. Lo que falta es decidir dos cosas que hoy no dice: desde dónde se enlaza el resumen para que se encuentre, y qué se hace con un hallazgo que viene arrastrado de otra sesión. Comprobar que el modelo sirve no es trabajo de esta historia: eso lo dicen sus criterios de aceptación.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | El resumen es un documento aparte de la transcripción, y vive dentro del histórico |
| RN-02 | Una carpeta por día y un archivo por sesión |
| RN-03 | Cada hallazgo dice si está resuelto o abierto, y dónde queda |
| RN-04 | Cada hallazgo dice a qué trabajo ya pedido responde y qué trabajo nuevo dispara |
| RN-05 | El hallazgo abierto dice con qué pregunta se retoma |
| RN-06 | Se anotan todos, resueltos y abiertos |
| RN-07 | El resumen dice si la sesión se puede cerrar |

### 3.2 Supuestos

- Quien llena el resumen es el agente, en el momento en que aparece el hallazgo, no al final.

### 3.3 Fuera de alcance

- El enganche que lo recuerda y lo crea solo. Eso es de EP-005.
- La transcripción, que sigue su curso y no cambia.

---

## 4. Criterios de aceptación

### CA-01 — El modelo existe y se distingue de la transcripción

```gherkin
Dado que se busca qué dejó una sesión
Cuando se abre su resumen
Entonces trae los hallazgos con sus campos
Y no repite la conversación
```

**Cómo validarlo:**

1. Abrir el resumen de una sesión y su transcripción.
2. Comparar. Resultado esperado: el resumen no copia diálogo; la transcripción no interpreta.
3. Buscar en el resumen qué quedó abierto. Resultado esperado: se responde sin abrir la transcripción.
- **Aprobado cuando:** los dos documentos responden preguntas distintas.

### CA-02 — Un hallazgo dice si está cerrado y por dónde sigue

```gherkin
Dado que un hallazgo quedó abierto
Cuando alguien lo retoma meses después
Entonces sabe qué falta, qué historia dispara y con qué pregunta seguir
```

**Cómo validarlo:**

1. Tomar un hallazgo abierto de un resumen real.
2. Leerlo sin haber estado en esa sesión. Resultado esperado: se entiende qué falta y por dónde arrancar.
3. Mirar si dispara alguna historia. Resultado esperado: la nombra, y esa historia existe o está declarada como faltante.
- **Aprobado cuando:** se puede retomar sin preguntarle a quien estuvo.

### CA-03 — El resumen dice si la sesión se puede cerrar

```gherkin
Dado que se quiere cerrar una sesión
Cuando se abre su resumen
Entonces dice qué falta para poder cerrarla
```

**Cómo validarlo:**

1. Abrir un resumen con hallazgos abiertos. Resultado esperado: la sección de cierre dice que todavía no.
2. Completar lo que falta y volver a mirar. Resultado esperado: dice que sí.
- **Aprobado cuando:** cerrar deja de ser una decisión de memoria.

### Criterios de aceptación transversales

- [x] **Límites** — una sesión que no dejó nada escribe "nada", que es un dato.
- [x] **No regresión** — la transcripción no cambia de forma por esto.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Brevedad** | El resumen se lee de una vez; si no, no cumple su función |
| RNF-02 | **Autonomía** | Se entiende sin abrir la transcripción |
| RNF-03 | **Uniformidad** | Todos los resúmenes traen los mismos campos |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** el modelo escrito el 2026-08-14 y el primer resumen hecho con él.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [x] Dejar enlazado el resumen desde el índice del histórico.
- [x] Definir qué se hace con un hallazgo que se arrastra de otra sesión.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-003-HU-009-modelo-del-resumen-de-sesion](A-EP-003-HU-009-modelo-del-resumen-de-sesion/README.md) | CA-01, CA-02 y CA-03 | Estación 11: las seis exigencias en verde, esperando el commit |

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
| Dependencia | HU-001, porque usa la marca de espacio por llenar | Alto |
| Dependencia | EP-006, porque lo que se aprende termina en las señales | Medio |
| Riesgo | Que el resumen crezca hasta parecerse a la transcripción | Los campos son fijos y pocos |
| Riesgo | Que nadie lo llene | Lo resuelve el enganche de EP-005, no este modelo |

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas

## 11. Definition of Done (DoD)

- [x] El modelo existe, con sus campos decididos
- [x] El resumen se distingue de la transcripción
- [x] Dice si la sesión se puede cerrar
- [x] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Necesita la marca de HU-001 |
| **N**egociable | Sí | Los campos se pueden discutir |
| **V**aliosa | Sí | Sin él, lo que dejó una sesión se pierde en la transcripción |
| **E**stimable | Sí | Es un documento |
| **S**mall (pequeña) | Sí | Un modelo |
| **T**esteable | Sí | Se prueba retomando una sesión vieja |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde el hallazgo H-4 del 2026-08-14 |
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Se quita de las tareas "probar el modelo con más de una sesión": eso lo comprueban los CA, no es trabajo de la HU |
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Se abre la fase A con sus dos planes. Los requisitos no funcionales quedan numerados |
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Fase ejecutada: nace `13·DOC22`, el índice del histórico enlaza cada resumen, y el modelo dice cómo se nombra y se hereda un hallazgo |
