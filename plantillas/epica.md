# EP-000 — [Título de la épica]

> Plantilla general de Épica. Una épica agrupa historias de usuario que comparten un objetivo de negocio común y suele abarcar varios sprints. Elimine las secciones que no apliquen.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-000 |
| **Brief de origen** | [`prompts/<slug>-brief.md` · paso 0 del flujo] |
| **Iniciativa / Objetivo estratégico** | [Iniciativa padre o OKR] |
| **Producto / Sistema** | [Sistema al que pertenece] |
| **Tipo** | Negocio / Técnica (habilitadora) / Cumplimiento |
| **Prioridad** | Must / Should / Could / Won't |
| **Estimación** | [T-shirt size: S / M / L / XL o rango de puntos] |
| **Horizonte** | [Trimestre / release objetivo] |
| **Product Owner** | [Nombre] |
| **Tech Lead / Arquitecto** | [Nombre] |
| **Estado** | Propuesta / Aprobada / En curso / Completada / Cancelada |

---

## 2. Resumen ejecutivo

[Dos o tres párrafos que expliquen, en lenguaje de negocio, qué se va a construir y por qué. Debe entenderlo alguien ajeno al equipo técnico.]

---

## 3. Problema y oportunidad

### 3.1 Situación actual

[Cómo se resuelve hoy el problema y qué duele: procesos manuales, costos, tiempos, incumplimientos, quejas de usuarios.]

### 3.2 Impacto de no hacerlo

[Consecuencias de mantener el estado actual: riesgo operativo, legal, financiero o reputacional.]

### 3.3 Evidencia

| Fuente | Hallazgo |
|---|---|
| [Métrica, entrevista, incidente, auditoría] | [Dato concreto] |

---

## 4. Objetivo y propuesta de valor

**Objetivo:** [Una frase con el resultado esperado.]

**Hipótesis de valor:**
> Creemos que [esta solución] para [este segmento de usuarios] logrará [este resultado]. Lo sabremos cuando observemos [esta métrica].

### 4.1 Beneficios esperados

| Beneficiario | Beneficio | Tipo |
|---|---|---|
| [Rol / área] | [Beneficio concreto] | Cuantitativo / Cualitativo |

---

## 5. Alcance

### 5.1 Dentro del alcance

- [Capacidad o proceso incluido]

### 5.2 Fuera del alcance

- [Lo que explícitamente NO se abordará en esta épica]

### 5.3 Diferido a fases posteriores

- [Funcionalidad postergada y en qué condiciones se retomaría]

---

## 6. Usuarios y actores

| Actor | Rol en el proceso | Necesidad principal |
|---|---|---|
| [Perfil] | [Qué hace en el flujo] | [Qué espera obtener] |

**Volumetría estimada:** [usuarios concurrentes, transacciones/día, registros esperados]

---

## 7. Criterios de aceptación de la épica

> A nivel de épica los criterios son de resultado, no de comportamiento de pantalla. Cada uno debe ser verificable.

- [ ] **CAE-01** — [Resultado observable a nivel de negocio]
- [ ] **CAE-02** — [Capacidad completa disponible en producción]
- [ ] **CAE-03** — [Cumplimiento normativo o técnico verificado]

---

## 8. Métricas de éxito

| Métrica | Línea base | Meta | Plazo de medición | Instrumento |
|---|---|---|---|---|
| [KPI] | [Valor actual] | [Valor objetivo] | [30/60/90 días] | [Dónde se mide] |

---

## 9. Historias de usuario

| ID | Título | Prioridad | Estimación | Sprint | Estado |
|---|---|---|---|---|---|
| HU-001 | [Título] | Must | 5 | S1 | Backlog |
| HU-002 | [Título] | Must | 8 | S1 | Backlog |
| HU-003 | [Título] | Should | 3 | S2 | Backlog |

**Total estimado:** [suma de puntos]  ·  **Sprints previstos:** [n]

---

## 10. Consideraciones técnicas

### 10.1 Arquitectura y componentes afectados

| Componente | Impacto | Observaciones |
|---|---|---|
| [Servicio, módulo, BD] | Nuevo / Modificado / Sin cambio | |

### 10.2 Decisiones de arquitectura (ADR)

- **ADR-00:** [Decisión y justificación breve] → [enlace al ADR completo]

### 10.3 Integraciones

| Sistema externo | Protocolo | Responsable | Estado del acuerdo |
|---|---|---|---|

### 10.4 Requisitos no funcionales transversales

| Categoría | Requisito |
|---|---|
| **Rendimiento** | |
| **Seguridad** | |
| **Disponibilidad** | |
| **Auditoría y trazabilidad** | |
| **Escalabilidad** | |
| **Accesibilidad** | |

### 10.5 Deuda técnica generada o pagada

- [Elemento y plan de atención]

---

## 11. Cumplimiento y normativa

| Norma / Política | Requisito aplicable | Cómo se cumple |
|---|---|---|
| [Ley, ISO, política interna] | | |

---

## 12. Dependencias

| ID | Dependencia | Tipo | Responsable | Fecha requerida | Estado |
|---|---|---|---|---|---|
| DEP-01 | [Descripción] | Interna / Externa / Técnica | | | Bloqueante / Resuelta |

---

## 13. Riesgos

| ID | Riesgo | Probabilidad | Impacto | Mitigación | Responsable |
|---|---|:--:|:--:|---|---|
| R-01 | | Alta/Media/Baja | Alto/Medio/Bajo | | |

---

## 14. Supuestos y restricciones

**Supuestos**
- [Condición que se asume verdadera]

**Restricciones**
- [Presupuesto, tecnología obligatoria, fecha inamovible, personal disponible]

---

## 15. Hoja de ruta

| Fase | Contenido | HU incluidas | Fecha objetivo | Entregable |
|---|---|---|---|---|
| Fase 1 — MVP | | HU-001, HU-002 | | |
| Fase 2 | | HU-003 | | |
| Fase 3 | | | | |

---

## 16. Estrategia de entrega

- **Despliegue:** [progresivo, big bang, feature flags]
- **Migración de datos:** [aplica / no aplica, estrategia]
- **Plan de reversión:** [rollback previsto]
- **Capacitación y gestión del cambio:** [acciones con usuarios finales]
- **Soporte post-despliegue:** [ventana de acompañamiento]

---

## 17. Definition of Ready (épica)

- [ ] Problema y objetivo validados con el negocio
- [ ] Alcance delimitado (dentro y fuera)
- [ ] Métricas de éxito definidas y medibles
- [ ] Historias de usuario identificadas y estimadas a alto nivel
- [ ] Dependencias y riesgos registrados
- [ ] Viabilidad técnica evaluada por el equipo
- [ ] Presupuesto y capacidad confirmados

## 18. Definition of Done (épica)

- [ ] Todas las HU obligatorias completadas y aceptadas
- [ ] Criterios de aceptación de la épica verificados
- [ ] Requisitos no funcionales validados en producción
- [ ] Documentación técnica y manuales de usuario entregados
- [ ] Usuarios finales capacitados
- [ ] Métricas instrumentadas y midiendo
- [ ] Deuda técnica registrada en el backlog
- [ ] Aceptación formal del Product Owner y del área usuaria

---

## 19. Referencias

- **Documento de visión:** [enlace]
- **Prototipos / Figma:** [enlace]
- **Diagramas de arquitectura:** [enlace]
- **Actas de reunión relevantes:** [enlace]

---

## 20. Bitácora de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| AAAA-MM-DD | [Nombre] | Creación de la épica |