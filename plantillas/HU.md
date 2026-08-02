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

### CA-01 — [Nombre del escenario: camino feliz]

```gherkin
Dado que [precondición]
Cuando [acción del usuario]
Entonces [resultado observable]
Y [efecto secundario verificable]
```

### CA-02 — [Nombre del escenario: validación / error]

```gherkin
Dado que [precondición]
Cuando [acción inválida]
Entonces [mensaje o comportamiento esperado]
Y [el estado del sistema no cambia]
```

### CA-03 — [Nombre del escenario: caso borde]

```gherkin
Dado que [condición límite]
Cuando [acción]
Entonces [resultado esperado]
```

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