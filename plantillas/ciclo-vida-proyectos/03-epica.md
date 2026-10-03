# EP-000 · «Título de la épica»

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Plantilla general de Épica. Una épica agrupa historias de usuario que comparten un objetivo de negocio común y suele abarcar varios sprints. Reemplaza los `«…»` y borra esta caja. La sección que no aplique se escribe `N/A`, no se borra ([`13·DOC21`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC21-escribe-n-a-en-la-seccion-que-no-aplica.md)).

## 1. Identificación

> Identifica la épica, de dónde sale, a qué objetivo responde, su prioridad y su tamaño, y quién responde por ella.

| Campo | Valor |
|---|---|
| **ID** | EP-000 |
| **Planteamiento de origen** | `prompts/«slug»-planteamiento.md`, del paso 0 del flujo |
| **Iniciativa / Objetivo estratégico** | «Iniciativa padre o OKR» |
| **Producto / Sistema** | «Sistema al que pertenece» |
| **Tipo** | Negocio / Técnica (habilitadora) / Cumplimiento |
| **Prioridad** | Must / Should / Could / Won't |
| **Estimación** | «T-shirt size: S / M / L / XL o rango de puntos» |
| **Horizonte** | «Trimestre / release objetivo» |
| **Product Owner** | «Nombre» |
| **Tech Lead / Arquitecto** | «Nombre» |
| **Estado** | Uno de [los estados del glosario](«RUTA-ESTANDAR»/base/glosario.md#5--en-qué-estado-está-algo): Propuesta, Aprobada, En curso, Terminada o Cancelada |

## 2. Resumen ejecutivo

> Es la presentación de la épica, para leerla sin entrar al detalle.

«Dos o tres párrafos que expliquen, en lenguaje de negocio, qué se va a construir y por qué. Debe entenderlo alguien ajeno al equipo técnico.»

## 3. Problema y oportunidad

> Explica por qué hace falta la épica.

### 3.1 Situación actual

> Describe el problema tal como se vive hoy.

«Cómo se resuelve hoy el problema y qué duele: procesos manuales, costos, tiempos, incumplimientos, quejas de usuarios.»

### 3.2 Impacto de no hacerlo

> Dice qué se pierde o se arriesga si la épica no se hace.

«Consecuencias de mantener el estado actual: riesgo operativo, legal, financiero o reputacional.»

### 3.3 Evidencia

> Son los datos que prueban que el problema existe, cada uno con su fuente.

| Fuente | Hallazgo |
|---|---|
| «Métrica, entrevista, incidente, auditoría» | «Dato concreto» |

## 4. Objetivo y propuesta de valor

> Dice qué resultado se espera y cómo se sabrá que la épica aportó valor.

**Objetivo:** «Una frase con el resultado esperado.»

**Hipótesis de valor:**
> Creemos que «esta solución» para «este segmento de usuarios» logrará «este resultado». Lo sabremos cuando observemos «esta métrica».

### 4.1 Beneficios esperados

> Son los beneficios concretos para cada rol o área.

| Beneficiario | Beneficio | Tipo |
|---|---|---|
| «Rol / área» | «Beneficio concreto» | Cuantitativo / Cualitativo |

## 5. Alcance

> Delimita qué entra en la épica y qué no.

### 5.1 Dentro del alcance

> Son las capacidades o procesos que la épica incluye.

- «Capacidad o proceso incluido»

### 5.2 Fuera del alcance

> Es lo que la épica deja fuera, para cerrar expectativas.

- «Lo que explícitamente no se abordará en esta épica»

### 5.3 Diferido a fases posteriores

> Es lo que se pospone, con la condición para retomarlo. Si no se difiere nada, se escribe «Ninguno».

- «Funcionalidad postergada y en qué condiciones se retomaría»

### 5.4 Alcance funcional completo · el detalle que la épica resuelve ANTES de crear las HU

> Es la visión completa del proceso, de inicio a fin, que la épica fija antes de crear las HU: las HU son la descomposición de este alcance en unidades implementables y verificables (§9), y con él se identifican las funcionalidades, se derivan sus CA y se fijan las dependencias y el orden de implementación. Una épica que se queda en un título (por ejemplo *"Gestión de socios"*) deja que el alcance se descubra a mitad de camino, y eso rompe la trazabilidad y la estimación.
>
> **Agnóstico.** Las preguntas aplican a cualquier épica de cualquier proyecto. Reemplaza el ejemplo por tu caso. Marca "No aplica porque..." en las que no correspondan: no se omiten en silencio.
>
> **Nivel de detalle.** Es de alcance y no de especificación: la épica dice qué existe y su forma. Por ejemplo, reconoce que la entidad tiene campos y qué se debe definir de cada uno, pero no los nombra ni los especifica aquí. El detalle fino (lista de campos con tipos, longitudes y formatos, validaciones exactas, Gherkin) baja a la HU o a la especificación de módulo. Si la épica especifica campo por campo, duplica las HU y se vuelve inmanejable.

La épica debe responder, como mínimo:

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

Detalle adicional, cuando aplique:

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

## 6. Usuarios y actores

> Son los perfiles que participan en el proceso, qué hace cada uno y qué espera, y cuánto uso se prevé.

| Actor | Rol en el proceso | Necesidad principal |
|---|---|---|
| «Perfil» | «Qué hace en el flujo» | «Qué espera obtener» |

**Volumetría estimada:** «usuarios concurrentes, transacciones/día, registros esperados»

## 7. Criterios de aceptación de la épica

> Son los resultados de negocio que dan la épica por lograda; el comportamiento de pantalla va en los CA de cada HU. Cada uno debe ser verificable.

- [ ] **CAE-01** — «Resultado observable a nivel de negocio»
- [ ] **CAE-02** — «Capacidad completa disponible en producción»
- [ ] **CAE-03** — «Cumplimiento normativo o técnico verificado»

## 8. Métricas de éxito

> Son los indicadores que dicen si la épica cumplió su objetivo, con su valor de hoy, su meta y dónde se miden.

| Métrica | Línea base | Meta | Plazo de medición | Instrumento |
|---|---|---|---|---|
| «KPI» | «Valor actual» | «Valor objetivo» | «30/60/90 días» | «Dónde se mide» |

## 9. Historias de usuario

> Son las HU en que se descompone el alcance de la sección 5.4.

| ID | Título | Prioridad | Estimación | Sprint | Estado |
|---|---|---|---|---|---|
| HU-001 | «Título» | Must | 5 | S1 | Backlog |
| HU-002 | «Título» | Must | 8 | S1 | Backlog |
| HU-003 | «Título» | Should | 3 | S2 | Backlog |

**Total estimado:** «suma de puntos», **Sprints previstos:** «n»

## 10. Consideraciones técnicas

> Reúne lo técnico que la épica afecta o exige.

### 10.1 Arquitectura y componentes afectados

> Son los componentes que la épica crea o cambia, y cómo los afecta.

| Componente | Impacto | Observaciones |
|---|---|---|
| «Servicio, módulo, BD» | Nuevo / Modificado / Sin cambio | |

### 10.2 Decisiones de arquitectura (ADR)

> Son las decisiones de arquitectura que la épica toma, cada una con su ADR. Si no hay, se escribe «Ninguna».

- **ADR-00:** «Decisión y justificación breve». Enlace: «enlace al ADR completo, plantilla `plantillas/ADR.md`»

### 10.3 Integraciones

> Son los sistemas externos con que se conecta la épica y el estado del acuerdo con cada uno. Si no hay, se escribe «Ninguna».

| Sistema externo | Protocolo | Responsable | Estado del acuerdo |
|---|---|---|---|

### 10.4 Requisitos no funcionales transversales

> Son los requisitos de calidad que valen para toda la épica, por categoría.

| Categoría | Requisito |
|---|---|
| **Rendimiento** | |
| **Seguridad** | |
| **Disponibilidad** | |
| **Auditoría y trazabilidad** | |
| **Escalabilidad** | |
| **Accesibilidad** | |

### 10.5 Deuda técnica generada o pagada

> Es la deuda técnica que la épica crea o salda, con su plan. Si no hay, se escribe «Ninguna».

- «Elemento y plan de atención»

## 11. Cumplimiento y normativa

> Son las normas y políticas que aplican a la épica y cómo se cumple cada una.

| Norma / Política | Requisito aplicable | Cómo se cumple |
|---|---|---|
| «Ley, ISO, política interna» | | |

## 12. Dependencias

> Es lo que la épica necesita de otros para avanzar. Si no depende de nada, se escribe «Ninguna».

| ID | Dependencia | Tipo | Responsable | Fecha requerida | Estado |
|---|---|---|---|---|---|
| DEP-01 | «Descripción» | Interna / Externa / Técnica | | | Bloqueante / Resuelta |

## 13. Riesgos

> Es lo que puede frenar o dañar la épica y cómo se mitiga.

| ID | Riesgo | Probabilidad | Impacto | Mitigación | Responsable |
|---|---|:--:|:--:|---|---|
| R-01 | | Alta/Media/Baja | Alto/Medio/Bajo | | |

## 14. Supuestos y restricciones

> Es lo que se da por cierto sin haberlo confirmado y los límites dentro de los que se trabaja.

**Supuestos**
- «Condición que se asume verdadera»

**Restricciones**
- «Presupuesto, tecnología obligatoria, fecha inamovible, personal disponible»

## 15. Hoja de ruta

> El orden en que se construyen las HU, copiado de la tabla de HU del análisis que las sacó. Una HU no va antes de otra de la que depende, y cada puesto dice por qué va ahí.

| Orden | HU | Depende de | Por qué en ese orden | Estado |
|---|---|---|---|---|
| 1 | HU-001 | Ninguna | | |
| 2 | HU-002 | HU-001 | | |

## 16. Estrategia de entrega

> Dice cómo llega la épica a los usuarios y cómo se deshace si falla.

- **Despliegue:** «progresivo, big bang, feature flags»
- **Migración de datos:** «aplica / no aplica, estrategia»
- **Plan de reversión:** «rollback previsto»
- **Capacitación y gestión del cambio:** «acciones con usuarios finales»
- **Soporte post-despliegue:** «ventana de acompañamiento»

## 17. Definition of Ready (épica)

> Es la lista de condiciones que la épica cumple antes de empezar a construirla.

- [ ] Problema y objetivo validados con el negocio
- [ ] Alcance delimitado (dentro y fuera)
- [ ] Métricas de éxito definidas y medibles
- [ ] Historias de usuario identificadas y estimadas a alto nivel
- [ ] Dependencias y riesgos registrados
- [ ] Viabilidad técnica evaluada por el equipo
- [ ] Presupuesto y capacidad confirmados

## 18. Definition of Done (épica)

> Es la lista de condiciones que deben cumplirse para dar la épica por terminada.

- [ ] Todas las HU obligatorias completadas y aceptadas
- [ ] Criterios de aceptación de la épica verificados
- [ ] Requisitos no funcionales validados en producción
- [ ] Documentación técnica y manuales de usuario entregados
- [ ] Usuarios finales capacitados
- [ ] Métricas instrumentadas y midiendo
- [ ] Deuda técnica registrada en el backlog
- [ ] Aceptación formal del Product Owner y del área usuaria

## 19. Referencias

> Son los documentos de apoyo de la épica.

- **Documento de visión:** «enlace»
- **Prototipos / Figma:** «enlace»
- **Diagramas de arquitectura:** «enlace»
- **Actas de reunión relevantes:** «enlace»

## 20. Bitácora de cambios

> Registra cada cambio de la épica: cuándo, quién y qué.

| Fecha | Autor | Cambio |
|---|---|---|
| AAAA-MM-DD | «Nombre» | Creación de la épica |