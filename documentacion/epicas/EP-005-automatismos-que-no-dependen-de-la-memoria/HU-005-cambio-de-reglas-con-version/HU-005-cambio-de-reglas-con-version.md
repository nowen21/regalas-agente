# HU-005 — Impedir guardar un cambio de reglas sin versión ni registro

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-005 |
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

- **Como** quien adopta las reglas en varios proyectos
- **Quiero** que no se pueda guardar un cambio de reglas sin su versión y su registro
- **Para** que ningún cambio llegue a los proyectos sin que se sepa qué cambió

---

## 3. Contexto y descripción

La regla que obliga a versionar cada cambio existe, y aun así se olvida: se afina una redacción, se guarda, y el registro queda "para después". Ese después no llega, y el proyecto que hereda las reglas no puede saber qué cambió.

Pedírselo por escrito a quien trabaja ya se probó. Lo que falta es que el momento de guardar lo exija.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Si el cambio toca las reglas, tiene que traer la versión subida y su entrada en el registro |
| RN-02 | Si falta alguna de las dos, el cambio no se guarda |
| RN-03 | El aviso dice cuál de las dos falta |
| RN-04 | Un cambio que no toca las reglas no se ve afectado |
| RN-05 | La comprobación mira lo que va a quedar guardado, no lo que está suelto en la carpeta |

### 3.2 Supuestos

- Quien cambia una regla puede escribir la entrada del registro en el mismo momento; es lo más barato que va a estar.

### 3.3 Fuera de alcance

- Decidir qué parte del número sube. Eso lo decide quien cambia la regla, con el criterio de EP-002.
- Escribir la entrada por él.

---

## 4. Criterios de aceptación

### CA-01 — Un cambio de reglas sin versión no se guarda

```gherkin
Dado que se cambia una regla
Cuando no se subió la versión
Entonces el cambio no se guarda
Y el aviso dice que falta subir la versión
```

**Cómo validarlo:**

1. Cambiar el texto de una regla en un repositorio de prueba, sin tocar la versión.
2. Intentar guardar. Resultado esperado: no se guarda, y el aviso nombra la versión.
3. Subir la versión y agregar la entrada. Resultado esperado: se guarda.
- **Aprobado cuando:** no se puede cambiar una regla en silencio.

### CA-02 — Un cambio que no toca reglas no se ve afectado

```gherkin
Dado que se cambia algo que no son las reglas
Cuando se guarda
Entonces no se exige ni versión ni registro
```

**Cómo validarlo:**

1. Cambiar un archivo que no sea de reglas ni de modelos.
2. Guardar. Resultado esperado: se guarda sin pedir nada.
- **Aprobado cuando:** el control no estorba al trabajo que no le toca.

### Criterios de aceptación transversales

- [ ] **Límites** — un cambio que toca reglas y otras cosas a la vez tiene comportamiento definido.
- [ ] **Errores** — el aviso dice exactamente cuál de las dos cosas falta.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Oportunidad** | Corre antes de aceptar el cambio |
| **Precisión** | Distingue el cambio de reglas del que no lo es |
| **Claridad** | El aviso dice qué falta, no solo que algo falta |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/epica.md](../epica.md), criterio CAE-05.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Detectar si lo que se va a guardar toca las reglas o los modelos.
- [ ] Comprobar que la versión subió y que hay entrada en el registro.
- [ ] Redactar el aviso diciendo cuál falta.

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
| Dependencia | EP-002, porque la versión y el registro los define esa épica | Alto |
| Riesgo | Que se salte el control para "guardar rápido" | Escribir la entrada cuesta menos que saltarse el control |
| Riesgo | Que confunda un cambio de reglas con uno de documentación | Se declara qué carpetas cuentan como reglas |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Un cambio de reglas sin versión o sin registro no se guarda
- [ ] El aviso dice cuál falta
- [ ] El trabajo que no toca reglas no se ve afectado
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | No | Necesita el versionado de EP-002 |
| **N**egociable | Sí | Qué carpetas cuentan como reglas se puede discutir |
| **V**aliosa | Sí | Evita que un cambio llegue sin que se sepa |
| **E**stimable | Sí | Alcance corto |
| **S**mall (pequeña) | Sí | Una comprobación en el momento de guardar |
| **T**esteable | Sí | Se prueba cambiando una regla sin versionar |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
