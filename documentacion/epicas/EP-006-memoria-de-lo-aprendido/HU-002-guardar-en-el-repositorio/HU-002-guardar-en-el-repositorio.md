# HU-002 — Guardar lo aprendido en el repositorio

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-002 |
| **Épica / Feature** | [EP-006 Memoria de lo aprendido](../epica.md) |
| **Módulo / Componente** | Memoria |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Backlog |

---

## 2. Narrativa

- **Como** quien trabaja en el proyecto desde otra máquina
- **Quiero** que lo aprendido esté dentro del repositorio
- **Para** que se vea en el historial, se pueda revisar y viaje con el proyecto

---

## 3. Contexto y descripción

Lo que se guarda fuera del repositorio no existe para los demás: no se ve en el historial, nadie lo revisa y se queda en una sola máquina.

Guardarlo adentro cambia las tres cosas. Se ve quién lo escribió y cuándo, se puede corregir como cualquier otro documento y llega a cualquier copia del proyecto.

También significa que lo guardado se somete a las mismas reglas que el resto: se revisa antes de aceptarlo y no lleva claves ni datos personales.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Lo aprendido se guarda dentro del repositorio del proyecto |
| RN-02 | Un archivo por cosa guardada, con su tipo y su alcance |
| RN-03 | Hay un índice que dice de qué trata cada uno |
| RN-04 | Lo guardado no lleva claves ni datos personales |
| RN-05 | Lo que sirve a cualquier proyecto queda donde otros proyectos lo puedan leer |

### 3.2 Supuestos

- El proyecto tiene un repositorio y lo que se guarda ahí viaja con él.

### 3.3 Fuera de alcance

- Buscar en lo guardado. Eso es HU-003 y HU-004.
- Recoger lo que quedó en la carpeta de la herramienta. Eso es HU-006.

---

## 4. Criterios de aceptación

### CA-01 — Lo guardado vive en el repositorio y se ve en el historial

```gherkin
Dado que se guarda algo aprendido
Cuando se mira el historial del proyecto
Entonces aparece cuándo se guardó y quién lo escribió
```

**Cómo validarlo:**

1. Guardar algo aprendido en un proyecto de prueba.
2. Mirar el historial. Resultado esperado: aparece el archivo nuevo.
3. Clonar el proyecto en otra carpeta. Resultado esperado: lo guardado está ahí.
- **Aprobado cuando:** lo aprendido viaja con el proyecto.

### CA-02 — Hay un índice que dice de qué trata cada cosa

```gherkin
Dado que hay varias cosas guardadas
Cuando se abre el índice
Entonces cada una aparece con una línea que dice de qué trata
```

**Cómo validarlo:**

1. Guardar tres cosas distintas.
2. Abrir el índice. Resultado esperado: las tres aparecen, cada una con su descripción.
3. Elegir una por el índice y abrirla. Resultado esperado: trata de lo que el índice decía.
- **Aprobado cuando:** se puede elegir qué abrir sin abrirlas todas.

### Criterios de aceptación transversales

- [ ] **Privacidad** — lo guardado no lleva claves ni datos personales.
- [ ] **Límites** — un proyecto sin nada guardado tiene un índice válido, vacío.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Portabilidad** | Viaja con el repositorio, sin depender de la máquina |
| **Revisabilidad** | Se corrige como cualquier otro documento |
| **Legibilidad** | Se lee sin herramienta especial |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica.
- **Documento funcional:** [documentacion/epicas/EP-006-memoria-de-lo-aprendido/epica.md](../epica.md), criterios CAE-01 y CAE-02.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Definir dónde se guarda dentro del repositorio.
- [ ] Definir la forma de cada archivo guardado.
- [ ] Mantener el índice al día.
- [ ] Definir dónde queda lo que sirve a cualquier proyecto.

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
| Dependencia | HU-001, porque cada cosa guardada declara su tipo y su alcance | Alto |
| Riesgo | Que el índice quede viejo | Se comprueba que todo lo guardado esté en el índice |
| Riesgo | Que se guarde algo con datos sensibles | Lo guardado pasa por la misma revisión que el resto |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] Lo aprendido se guarda dentro del repositorio
- [ ] Hay un índice al día
- [ ] Lo que sirve a cualquier proyecto queda donde otros lo lean
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Parcial | Necesita los tipos y alcances de HU-001 |
| **N**egociable | Sí | Dónde vive se puede discutir |
| **V**aliosa | Sí | Sin esto, lo aprendido no viaja ni se revisa |
| **E**stimable | Sí | Alcance acotado |
| **S**mall (pequeña) | Sí | Una carpeta, un formato y un índice |
| **T**esteable | Sí | Se prueba clonando el proyecto |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
