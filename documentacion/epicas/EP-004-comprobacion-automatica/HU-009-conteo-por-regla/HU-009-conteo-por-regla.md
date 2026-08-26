# HU-009 — Registrar cuántos hallazgos hubo por regla

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-009 |
| **Épica / Feature** | [EP-004 Comprobación automática de lo que no admite discusión](../epica.md) |
| **Módulo / Componente** | Programas de comprobación |
| **Tipo** | Técnica |
| **Prioridad** | Should |
| **Estimación** | S |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Pendiente |
---

## 2. Narrativa

- **Como** quien define el estándar
- **Quiero** ver cuántos hallazgos produjo cada regla
- **Para** descubrir la regla que se incumple siempre, que casi nunca es culpa de quien la incumple sino de cómo está escrita

---

## 3. Contexto y descripción

Una regla que produce hallazgos todos los días está diciendo algo. Puede ser que no se entienda, que pida algo que estorba, o que el trabajo real se haga de otra manera. Sin contar, eso no se ve: cada hallazgo se arregla suelto y nadie nota el patrón.

El conteo también sirve para lo contrario. Una regla que nunca produce hallazgos puede ser que se cumpla sola, o que su comprobación no esté mirando lo que debería.

Esto es lo último de la épica a propósito: contar sin tener qué contar no sirve de nada.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Cada corrida puede dejar el conteo de hallazgos agrupado por regla |
| RN-02 | El conteo distingue falla de aviso |
| RN-03 | El registro es opcional: la corrida normal no lo necesita para funcionar |
| RN-04 | El registro no guarda el contenido de los archivos revisados, solo la cuenta |
| RN-05 | Se puede comparar el conteo de dos corridas para ver si algo mejoró |

### 3.2 Supuestos

- Los hallazgos ya vienen con su regla asociada, porque así se definió el formato del hallazgo.

### 3.3 Fuera de alcance

- Decidir qué hacer con la regla que se incumple siempre. Eso es una discusión, no un programa.
- Sacar gráficos o tableros. La cuenta alcanza.

---

## 4. Criterios de aceptación

### CA-01 — La corrida deja el conteo por regla

```gherkin
Dado que se corren las comprobaciones sobre un proyecto
Cuando se pide el registro del conteo
Entonces queda una cuenta de hallazgos por regla
Y distingue las fallas de los avisos
```

**Cómo validarlo:**

1. Preparar un proyecto de prueba con incumplimientos de dos reglas distintas.
2. Correr las comprobaciones pidiendo el registro. Resultado esperado: queda una cuenta con una fila por regla.
3. Leer la cuenta. Resultado esperado: cada fila dice la regla, cuántas fallas y cuántos avisos.
- **Aprobado cuando:** la cuenta refleja los incumplimientos que se prepararon, separados por severidad.

### CA-02 — El registro no guarda lo revisado

```gherkin
Dado que se deja el registro de una corrida
Cuando se abre el registro
Entonces no aparece el contenido de los archivos revisados
```

**Cómo validarlo:**

1. Provocar un hallazgo en un archivo que tenga texto reconocible.
2. Correr con registro y abrir lo que quedó guardado. Resultado esperado: aparece la regla y la cuenta, no el texto del archivo.
- **Aprobado cuando:** el registro sirve para contar y no para reconstruir lo revisado.

### CA-03 — Dos corridas se pueden comparar

```gherkin
Dado que existe el registro de una corrida anterior
Cuando se corre otra vez después de arreglar algo
Entonces se puede comparar y ver qué regla bajó su cuenta
```

**Cómo validarlo:**

1. Correr con registro sobre el proyecto de prueba y guardar el resultado.
2. Arreglar los incumplimientos de una de las dos reglas.
3. Correr otra vez con registro y comparar. Resultado esperado: la regla arreglada baja a cero y la otra se mantiene.
- **Aprobado cuando:** la comparación muestra el cambio sin tener que leer los hallazgos uno por uno.

### Criterios de aceptación transversales

- [ ] **Límites** — una corrida sin hallazgos deja un registro válido, con todo en cero.
- [ ] **Privacidad** — el registro no guarda rutas de máquina ni datos de quien corrió.

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Determinismo** | Dos corridas sobre lo mismo dan la misma cuenta |
| **Simplicidad** | El registro se lee sin herramienta especial |
| **Autonomía** | No manda nada a ninguna parte |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, la salida es texto.
- **Documento funcional:** [documentacion/epicas/EP-004-comprobacion-automatica/epica.md](../epica.md), §5.4 fila 15 y §8.
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Agrupar los hallazgos de una corrida por regla y severidad.
- [ ] Definir dónde queda el registro y con qué nombre.
- [ ] Escribir la comparación entre dos registros.

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-004-HU-009-el-conteo-de-hallazgos-por-regla](A-EP-004-HU-009-el-conteo-de-hallazgos-por-regla/README.md) | CA-01, CA-02 y CA-03 | Abierta 2026-08-17, con su plan de trabajo escrito y sin aprobar |

**La fase construye: acá no hay nada que retro-documentar.** Ningún validador agrupa por regla. Y la parte delicada es el CA-02: un registro de hallazgos puede terminar guardando el contenido de lo revisado.

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
| Dependencia | HU-003, porque cada hallazgo tiene que traer su regla | Alto |
| Dependencia | HU-008, porque se cuenta lo de una corrida completa | Alto |
| Riesgo | Que el conteo se use para medir personas en vez de reglas | El registro no guarda quién corrió |

---

## 10. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Dependencias identificadas

## 11. Definition of Done (DoD)

- [ ] La corrida puede dejar su conteo por regla
- [ ] El conteo distingue falla de aviso
- [ ] Dos registros se pueden comparar
- [ ] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | No | Necesita la corrida completa de HU-008 |
| **N**egociable | Sí | Dónde queda el registro se puede discutir |
| **V**aliosa | Sí | Muestra la regla mal escrita, que es la que se incumple siempre |
| **E**stimable | Sí | Alcance corto |
| **S**mall (pequeña) | Sí | Agrupar y escribir |
| **T**esteable | Sí | Se prueba comparando dos corridas |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde la épica |
