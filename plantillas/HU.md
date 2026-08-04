# HU-000 — [Título corto en lenguaje de negocio]

> Plantilla general de Historia de Usuario. Elimine las secciones que no apliquen y las notas entre paréntesis.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-000 |
| **Épica / Feature** | [Épica padre] |
| **Módulo / Componente** | [Módulo del sistema] |
| **Tipo** | Funcional / Técnica / Spike / Bug |
| **Prioridad** | Must / Should / Could / Won't (MoSCoW) |
| **Estimación** | [Story points] |
| **Sprint** | [Sprint asignado] |
| **Solicitante** | [Product Owner / área usuaria] |
| **Responsable** | [Dev asignado] |
| **Estado** | Backlog / Ready / En curso / En QA / Done |

---

## 2. Narrativa

**Como** [rol específico — evite "usuario" genérico]
**Quiero** [acción o capacidad concreta]
**Para** [beneficio de negocio medible]

---

## 3. Contexto y descripción

[Situación actual, problema que se resuelve, antecedentes relevantes.]

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | [Regla que debe cumplirse siempre] |
| RN-02 | |

### 3.2 Supuestos

- [Lo que se asume verdadero al iniciar]

### 3.3 Fuera de alcance

- [Lo que explícitamente NO incluye esta HU]

---

## 4. Criterios de aceptación

> Formato Gherkin. Cubra: camino feliz, casos borde, errores y validaciones.
>
> **Cada CA lleva, debajo de su Gherkin, un apartado `Cómo validarlo`** que describe de forma **clara, detallada y secuencial** cómo verificar el CA. **No asume** que quien valida conoce el sistema, la ubicación de la funcionalidad ni dónde se evidencia el resultado. Los pasos guían al validador **de principio a fin**, indicando cuando corresponda:
> - **Dónde** ingresar / desde qué módulo, pantalla o funcionalidad iniciar.
> - **Qué acción** realizar y con qué datos o condiciones.
> - **Qué resultado** debe observarse después de cada acción.
> - **Dónde verificar** la evidencia de que el comportamiento esperado se cumplió.
> - **Qué condición** determina que el CA está aprobado.
>
> Cada paso es **verificable** y con resultado esperado claro. El CA se aprueba **solo** cuando **todos** sus pasos se ejecutan satisfactoriamente. **Prohibido** lenguaje ambiguo — "verificar que funcione correctamente", "comprobar que se procese", "validar que aparezca" — sin indicar exactamente **cómo, dónde y qué** comprobar.

### CA-01 — [Nombre del escenario: camino feliz]

```gherkin
Dado que [precondición]
Cuando [acción del usuario]
Entonces [resultado observable]
Y [efecto secundario verificable]
```

**Cómo validarlo:**
1. [Dónde iniciar — módulo / pantalla / URL / menú]: …
2. [Qué acción realizar y con qué datos/condiciones]: … → resultado esperado: …
3. [Dónde verificar la evidencia del resultado]: …
- **Aprobado cuando:** [condición concreta y observable].

### CA-02 — [Nombre del escenario: validación / error]

```gherkin
Dado que [precondición]
Cuando [acción inválida]
Entonces [mensaje o comportamiento esperado]
Y [el estado del sistema no cambia]
```

**Cómo validarlo:**
1. [Dónde iniciar — módulo / pantalla / URL / menú]: …
2. [Qué acción inválida realizar y con qué datos]: … → resultado esperado: [mensaje/comportamiento] …
3. [Dónde verificar que el estado NO cambió]: …
- **Aprobado cuando:** [condición concreta y observable].

### CA-03 — [Nombre del escenario: caso borde]

```gherkin
Dado que [condición límite]
Cuando [acción]
Entonces [resultado esperado]
```

**Cómo validarlo:**
1. [Dónde iniciar — módulo / pantalla / URL / menú]: …
2. [Qué acción realizar en la condición límite y con qué datos]: … → resultado esperado: …
3. [Dónde verificar la evidencia del resultado]: …
- **Aprobado cuando:** [condición concreta y observable].

### Criterios de aceptación transversales

> Calidad que aplica a casi toda HU (no son de negocio). **Marque los que apliquen** y elimine el resto — una HU de solo lectura no necesita atomicidad de escritura, etc. Se verifican como los CA funcionales.

- [ ] **Validación** — toda entrada obligatoria se valida; un dato inválido se rechaza con mensaje claro y **el estado no cambia** (`04`, `03`).
- [ ] **Límites** — vacío, nulo, mínimo, máximo y duplicado tienen comportamiento definido (`08`).
- [ ] **Autorización** — solo quien tiene permiso ejecuta la acción; sin permiso se deniega **sin filtrar datos ni su existencia**, y no se elude cambiando parámetros/ruta (`04`).
- [ ] **Errores** — un fallo previsto da mensaje accionable **sin exponer detalles internos**; el sistema queda consistente, sin datos a medias (`05`, `00·N3`).
- [ ] **Atomicidad** — las operaciones que escriben son todo-o-nada (`03`).
- [ ] **Idempotencia** — reintentar o doble-enviar **no duplica** efectos (`03·D6`).
- [ ] **Privacidad** — datos personales/sensibles no se exponen ni se registran en claro; se tratan según `marco-normativo` (`12`, `00·N4`).
- [ ] **Auditoría** — las acciones relevantes quedan registradas (quién, qué, cuándo) (`05`, `15`).
- [ ] **Rendimiento** — responde dentro del umbral acordado con un **volumen realista** (`06`).
- [ ] **No regresión** — lo existente sigue funcionando; la suite relacionada queda verde (`08`, `02·F5`).

---

## 5. Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| **Rendimiento** | [p. ej. respuesta < 2 s con 500 registros] |
| **Seguridad** | [autenticación, autorización, roles con acceso] |
| **Auditoría** | [eventos a registrar en bitácora] |
| **Accesibilidad** | [nivel WCAG aplicable] |
| **Compatibilidad** | [navegadores, dispositivos, versiones] |
| **Trazabilidad** | [norma o requisito legal asociado] |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** [enlace]
- **Documento funcional:** [enlace]
- **Contrato de API:** [endpoint, método, request/response]
- **Modelo de datos afectado:** [tablas o entidades]

---

## 7. Tareas técnicas derivadas

- [ ] [Backend] …
- [ ] [Frontend] …
- [ ] [Base de datos] …
- [ ] [Pruebas] …
- [ ] [Documentación] …

---

## 8. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | [HU o servicio previo requerido] | Alto / Medio / Bajo |
| Riesgo | [Riesgo identificado] | [Mitigación] |

---

## 9. Definition of Ready (DoR)

- [ ] Narrativa clara con rol, acción y beneficio
- [ ] Criterios de aceptación definidos y testeables
- [ ] Reglas de negocio documentadas
- [ ] Diseño / mockup disponible
- [ ] Dependencias identificadas y desbloqueadas
- [ ] Estimada por el equipo
- [ ] Cumple criterios INVEST

## 10. Definition of Done (DoD)

- [ ] Código implementado y en rama principal
- [ ] Pruebas unitarias e integración pasando
- [ ] Code review aprobado
- [ ] Todos los criterios de aceptación verificados
- [ ] Requisitos no funcionales validados
- [ ] Documentación técnica y de usuario actualizada
- [ ] Desplegada en ambiente de pruebas
- [ ] Aceptada por el Product Owner

---

## 11. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | ☐ | |
| **N**egociable | ☐ | |
| **V**aliosa | ☐ | |
| **E**stimable | ☐ | |
| **S**mall (pequeña) | ☐ | |
| **T**esteable | ☐ | |

---

## 12. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| AAAA-MM-DD | [Nombre] | Creación de la HU |