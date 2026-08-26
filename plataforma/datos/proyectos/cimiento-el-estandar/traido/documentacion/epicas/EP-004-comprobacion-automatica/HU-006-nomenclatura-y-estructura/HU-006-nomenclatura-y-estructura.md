# HU-006 — Comprobar la nomenclatura y la estructura de carpetas del trabajo

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-006 |
| **Épica / Feature** | [EP-004 Comprobación automática de lo que no admite discusión](../epica.md) |
| **Módulo / Componente** | Programas de comprobación |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Cumplida — los tres CA y los dos transversales verificados el 2026-08-17 |

---

## 2. Narrativa

- **Como** quien retoma un trabajo meses después
- **Quiero** que un programa compruebe que cada épica, historia y fase está donde debe y se llama como debe
- **Para** encontrar cualquier documento por convención, sin buscarlo

---

## 3. Contexto y descripción

El trabajo se organiza en tres niveles: la épica, la historia de usuario y la fase. Cada uno tiene su carpeta, su nombre y sus documentos obligatorios. Si eso se respeta, cualquiera encuentra lo que busca sin preguntar.

Cuando no se respeta, aparecen las mismas cosas: una fase que cuelga de dos historias, un número repetido, un hueco en la numeración que hace dudar si falta algo, una carpeta con nombre libre que nadie vuelve a encontrar.

Todo eso se responde con un sí o un no mirando los nombres y las carpetas, sin entender el contenido.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | La jerarquía es épica, historia y fase, y cada nivel cuelga de uno solo del nivel de arriba |
| RN-02 | El identificador de cada nivel es único y sigue la nomenclatura acordada |
| RN-03 | La numeración va corrida y sin huecos |
| RN-04 | Cada fase tiene los documentos que el estándar le exige |
| RN-05 | La ruta física refleja la jerarquía, no la reinventa |
| RN-06 | Cada nivel tiene su índice, que dice qué cuelga de él |

### 3.2 Supuestos

- La estructura de carpetas del trabajo la crea el agente siguiendo el estándar, así que las desviaciones son errores y no decisiones.

### 3.3 Fuera de alcance

- La estructura del código del proyecto. Depende de lo que cada proyecto declare, y se trata aparte.
- El contenido de cada documento. Eso es HU-004.

---

## 4. Criterios de aceptación

### CA-01 — Un identificador fuera de convención se reporta

```gherkin
Dado que existe una carpeta de fase con nombre libre
Cuando se corre la comprobación de estructura
Entonces reporta la carpeta y dice qué nomenclatura se esperaba
```

**Cómo validarlo:**

1. Crear en el árbol de prueba una carpeta de fase con un nombre que no siga la convención.
2. Correr la comprobación de estructura. Resultado esperado: reporta la carpeta, con la nomenclatura esperada en el mensaje.
3. Renombrarla como corresponde y volver a correr. Resultado esperado: no reporta nada.
- **Aprobado cuando:** el nombre libre se reporta y el correcto no.

### CA-02 — Un hueco en la numeración se reporta

```gherkin
Dado que una épica tiene historias numeradas
Cuando falta un número en el medio
Entonces la comprobación reporta el hueco
```

**Cómo validarlo:**

1. En el árbol de prueba, borrar la carpeta de una historia intermedia.
2. Correr la comprobación. Resultado esperado: reporta qué número falta.
3. Restituirla y volver a correr. Resultado esperado: no reporta nada.
- **Aprobado cuando:** el hueco se reporta con el número que falta.

### CA-03 — Una fase sin sus documentos se reporta

```gherkin
Dado que existe una carpeta de fase
Cuando le falta alguno de los documentos que el estándar exige
Entonces la comprobación lo reporta como aviso
Y nombra el documento que falta
```

**Cómo validarlo:**

1. Crear una fase de prueba con solo uno de sus documentos.
2. Correr la comprobación. Resultado esperado: nombra cada documento faltante, como aviso.
3. Agregar los documentos y volver a correr. Resultado esperado: no reporta nada.
- **Aprobado cuando:** los faltantes se nombran uno por uno y salen como aviso, porque una fase recién abierta todavía no los tiene.

### Criterios de aceptación transversales

- [ ] **Límites** — una épica sin historias, una historia sin fases y una carpeta vacía tienen comportamiento definido.
- [ ] **No regresión** — el trabajo ya cerrado sigue pasando la comprobación.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Determinismo** | El mismo árbol da el mismo resultado |
| **Compatibilidad** | Funciona con rutas largas de Windows, con espacios y con tildes |
| **Claridad** | El mensaje dice el nombre esperado, no solo que está mal |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, la salida es texto en la terminal.
- **Documento funcional:** [documentacion/epicas/EP-004-comprobacion-automatica/epica.md](../epica.md), §5.1.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Recorrer el árbol de épicas, historias y fases.
- [ ] Comprobar identificador, nomenclatura y unicidad en cada nivel.
- [ ] Comprobar la numeración corrida.
- [ ] Comprobar los documentos obligatorios de la fase.
- [ ] Comprobar que cada nivel tiene su índice.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-004-HU-006-retrodocumentar-la-comprobacion-de-la-estructura](A-EP-004-HU-006-retrodocumentar-la-comprobacion-de-la-estructura/README.md) | CA-01, CA-02 y CA-03 | **Ejecutada el 2026-08-17.** Veredicto: [**Cumple**](A-EP-004-HU-006-retrodocumentar-la-comprobacion-de-la-estructura/resultado_pruebas.md#6-veredicto-de-la-fase) — los tres CA y los dos transversales verificados. Pendiente el commit |

**La fase retro-documenta y deja la línea base.** El programa comprueba nueve partes de `02·F12` y hoy reporta 0 fallas y 54 avisos. Sin ese número escrito, mañana no se puede decir si bajaron.

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
| Dependencia | EP-003, porque la estructura del trabajo la define esa épica | Alto |
| Riesgo | Que el trabajo viejo, hecho antes de la convención, se llene de hallazgos | Se reporta como aviso y se documenta que es correcto |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] La jerarquía se comprueba en sus tres niveles
- [ ] La nomenclatura y la numeración se comprueban
- [ ] Los documentos obligatorios de la fase se comprueban
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Necesita la forma del hallazgo de HU-003 |
| **N**egociable | Sí | Qué documentos son obligatorios se puede discutir |
| **V**aliosa | Sí | Encontrar un documento deja de depender de la memoria |
| **E**stimable | Sí | El alcance lo fija la estructura acordada |
| **S**mall (pequeña) | Sí | Un programa que recorre carpetas |
| **T**esteable | Sí | Se prueba con árboles de prueba mal formados a propósito |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
| 2026-08-17 | Ing. José Dúmar Jiménez Ruíz | Se ejecuta la fase A. Los tres CA verificados, incluido el caso que faltaba: la fase incompleta nombra cuáles cuatro documentos le faltan. Queda escrito qué parte de `F12` se comprueba y qué parte no |
