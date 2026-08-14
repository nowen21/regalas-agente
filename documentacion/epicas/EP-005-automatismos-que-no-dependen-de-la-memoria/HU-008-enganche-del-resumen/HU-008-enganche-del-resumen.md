# HU-008 — El enganche que sostiene el resumen de la sesión

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-008 |
| **Épica / Feature** | [EP-005 Automatismos que no dependen de la memoria](../epica.md) |
| **Módulo / Componente** | Automatismos |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Backlog |

---

## 2. Narrativa

- **Como** quien retoma el trabajo días después
- **Quiero** que el resumen de la sesión exista aunque nadie se acuerde de escribirlo
- **Para** no depender de la memoria del agente para saber qué quedó

---

## 3. Contexto y descripción

El modelo del resumen y su carpeta ya existen. Llenarlos depende de que el agente se acuerde, y esa es exactamente la forma en que se pierde: un chat no tiene final, así que lo que se deja para el cierre no se escribe.

Es lo mismo que pasaba con la transcripción, que solo empezó a escribirse siempre cuando la escribió un programa.

Lo que un programa no puede hacer es reconocer el hallazgo ni redactarlo: eso es criterio. Lo que sí puede es que el hueco se vea.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | El archivo del resumen se crea solo al abrir la sesión, con el modelo puesto |
| RN-02 | Cuando la sesión ya produjo algo y el resumen sigue vacío, se avisa una sola vez |
| RN-03 | Al abrir la sesión siguiente, lo que quedó sin cerrar en la anterior se muestra |
| RN-04 | El enganche no escribe hallazgos: solo crea, avisa y arrastra |
| RN-05 | No detiene el trabajo |

### 3.2 Supuestos

- "La sesión ya produjo algo" se puede detectar: hubo un commit, o cambió el cuerpo de reglas.

### 3.3 Fuera de alcance

- El modelo del resumen, que es de EP-003.
- Decidir qué es un hallazgo.

---

## 4. Criterios de aceptación

### CA-01 — El archivo nace solo

```gherkin
Dado que se abre una sesión
Cuando se mira la carpeta de resúmenes del día
Entonces existe el archivo de esa sesión, con el modelo puesto y sin hallazgos
```

**Cómo validarlo:**

1. Abrir una sesión en un proyecto de prueba.
2. Mirar la carpeta del día. Resultado esperado: está el archivo, con los campos del modelo.
3. Abrir una segunda sesión el mismo día. Resultado esperado: aparece su propio archivo, sin pisar el anterior.
- **Aprobado cuando:** el hueco se ve, en vez de no existir.

### CA-02 — Avisa cuando la sesión ya produjo algo y el resumen sigue vacío

```gherkin
Dado que la sesión hizo un commit o cambió una regla
Cuando el resumen todavía no tiene hallazgos
Entonces se avisa una sola vez
```

**Cómo validarlo:**

1. En la sesión de prueba, hacer un cambio y guardarlo sin escribir el resumen.
2. Seguir trabajando. Resultado esperado: aparece el aviso, una vez.
3. Escribir un hallazgo y seguir. Resultado esperado: no vuelve a avisar.
- **Aprobado cuando:** avisa cuando falta y calla cuando no.

### CA-03 — Lo que no se cerró aparece en la sesión siguiente

```gherkin
Dado que la sesión anterior quedó con hallazgos abiertos
Cuando se abre una sesión nueva
Entonces se muestra qué quedó sin cerrar y dónde está
```

**Cómo validarlo:**

1. Dejar una sesión con dos hallazgos abiertos.
2. Abrir una sesión nueva. Resultado esperado: se listan los dos, con su archivo.
3. Cerrarlos y abrir otra. Resultado esperado: ya no aparecen.
- **Aprobado cuando:** lo abierto se persigue solo.

### Criterios de aceptación transversales

- [ ] **Inocuidad** — el enganche no modifica los hallazgos ya escritos.
- [ ] **Límites** — un proyecto sin carpeta de resúmenes no se ve afectado.
- [ ] **Errores** — si no puede escribir, avisa y la sesión sigue.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Oportunidad** | Avisa durante la sesión, no al cerrarla |
| **Silencio** | Una sola vez por sesión |
| **Rendimiento** | No demora el arranque |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** el pendiente 17 y el hallazgo H-4 del 2026-08-14.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Crear el archivo del resumen al abrir la sesión.
- [ ] Detectar que la sesión ya produjo algo.
- [ ] Avisar una sola vez, con la marca que evita repetirlo.
- [ ] Arrastrar a la sesión siguiente lo que quedó abierto.

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
| Dependencia | EP-003 · HU-009, porque crea el archivo con ese modelo | Alto |
| Dependencia | HU-001 de esta épica, porque comparte el momento de la sesión | Medio |
| Riesgo | Que el aviso se vuelva ruido | Una vez por sesión, y solo cuando falta |
| Riesgo | Que el archivo vacío se quede vacío igual | Se arrastra a la sesión siguiente, así que no desaparece |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] El archivo se crea solo
- [ ] Avisa una vez cuando falta
- [ ] Lo abierto aparece en la sesión siguiente
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | No | Necesita el modelo de EP-003 |
| **N**egociable | Sí | La señal que dispara el aviso se puede discutir |
| **V**aliosa | Sí | Es lo que hace que el resumen exista siempre |
| **E**stimable | Sí | Alcance acotado |
| **S**mall (pequeña) | Sí | Tres comportamientos |
| **T**esteable | Sí | Se prueba abriendo sesiones de prueba |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde el hallazgo H-4 del 2026-08-14 |
