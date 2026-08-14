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

### 5.4 Alcance funcional completo — el detalle que la épica resuelve ANTES de crear las HU

La épica **no se limita a un título** (ej. *"Gestión de socios"*) dejando que el alcance se descubra al crear las HU. Debe dar la **visión completa del proceso, de inicio a fin**. Las **HU son la descomposición** de este alcance en unidades implementables y verificables — por eso el alcance se define **primero**, aquí. Con este detalle se identifican las funcionalidades, se dividen en HU, se derivan sus CA y se fijan dependencias y orden de implementación.

> **Agnóstico:** las preguntas aplican a **cualquier** épica de **cualquier** proyecto. Reemplaza el ejemplo por tu caso. Marca **"No aplica porque …"** en las que no correspondan — no se omiten en silencio.
>
> **Nivel de detalle — de alcance, no de especificación.** La épica dice **QUÉ existe y su forma**, no el detalle exhaustivo. Ej.: reconoce que la entidad **tiene campos** (y qué se debe definir de cada uno) — pero **no los nombra ni los especifica** aquí. El detalle fino (lista de campos con tipos/longitudes/formatos, validaciones exactas, Gherkin) **baja a la HU / especificación de módulo**. Si la épica specea campo por campo, **duplica las HU** y se vuelve inmanejable.

**La épica debe responder, como mínimo:**

| # | Pregunta | Qué precisar |
|---|---|---|
| 1 | **Finalidad** | qué problema resuelve y qué objetivo funcional persigue |
| 2 | **Actores / roles** | quién puede consultar, crear, modificar, eliminar, activar, inactivar, administrar |
| 3 | **Información** | qué datos identifican a la entidad y qué información adicional se maneja |
| 4 | **Campos** | que la entidad **tiene** campos y qué dimensiones se definirán de cada uno (nombre, tipo, obligatoriedad, formato, longitud, valores) — **sin listarlos ni especificarlos**; ese detalle es de la HU o de la especificación |
| 5 | **Validaciones** | obligatoriedad, formato, rangos, unicidad, existencia, duplicidad, dependencias entre campos |
| 6 | **Reglas de negocio** | condiciones para crear, modificar, activar, inactivar u otras operaciones |
| 7 | **Estados y transiciones** | qué estados existen, qué significan, qué operaciones se permiten en cada uno (máquina de estados) |
| 8 | **Operaciones** | crear, consultar, editar, cambiar estado, buscar, filtrar, asociar, ver detalle, etc. |
| 9 | **Restricciones** | qué NO se permite, quién y bajo qué condiciones |
| 10 | **Relaciones** | con qué entidades/módulos se relaciona y con qué cardinalidad |
| 11 | **Consultas y listados** | columnas, filtros, ordenamiento, paginación, búsquedas, acciones disponibles |
| 12 | **Mensajes / notificaciones** | éxito, error, advertencia, validación, confirmaciones; a quién y por qué canal |
| 13 | **Errores y excepciones** | qué pasa ante dato inválido, duplicado, no encontrado, sin permiso, fallo de operación |
| 14 | **Permisos y control de acceso** | qué rol puede cada operación y qué restringe el sistema |
| 15 | **Auditoría / trazabilidad** | qué acciones se registran, qué se conserva, quién hizo cada operación |
| 16 | **Resultado final** | cómo debe quedar el sistema al terminar y qué condiciones dan la épica por completa |

**Detalle adicional (cuando aplique):**

| # | Pregunta | Qué precisar |
|---|---|---|
| 17 | **Ciclo de vida completo** | del alta al archivado/baja/eliminación (¿borrado lógico o físico? ¿reactivable?) |
| 18 | **Integraciones externas** | qué sistemas/APIs de terceros intervienen y con qué contrato |
| 19 | **Datos maestros / catálogos** | qué catálogos consume o alimenta, y quién los administra |
| 20 | **Importación / exportación** | carga masiva, exportación, formatos |
| 21 | **Reportes e indicadores** | qué reportes/KPIs debe producir el proceso |
| 22 | **Configurabilidad** | qué es parametrizable sin tocar código (reglas, catálogos, umbrales) |
| 23 | **Concurrencia y volumen** | usuarios/registros simultáneos esperados y comportamiento bajo carga |
| 24 | **Datos sensibles / privacidad** | qué datos son personales/sensibles, cómo se protegen y quién los ve |
| 25 | **Migración / convivencia** | si reemplaza o convive con algo existente y cómo migran los datos |
| 26 | **Idioma / formato / zona** | idioma de textos, formato de fechas/números/moneda, zona horaria (si aplica) |

**Cierre:** la épica da la **visión completa** de lo que se quiere lograr; las **HU** son la **descomposición** de ese alcance en unidades implementables y verificables (§9). Sin este detalle, el alcance se "descubre" a mitad de camino — lo que rompe la trazabilidad y la estimación.

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

- **ADR-00:** [Decisión y justificación breve] → [enlace al ADR completo · plantilla `plantillas/ADR.md`]

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