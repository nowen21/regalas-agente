# EP-002 — Versionado de las reglas y adopción por proyecto

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-002 |
| **Brief de origen** | [brief.md](../../../brief.md) |
| **Iniciativa** | Que una IA que programa trabaje siempre igual |
| **Producto** | Estándar de agente para desarrollo de software |
| **Tipo** | Técnica (habilitadora) |
| **Prioridad** | Must |
| **Estimación** | M |
| **Horizonte** | Primera entrega |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Propuesta |

## 2. Resumen ejecutivo

Las reglas van a cambiar con el tiempo, y los proyectos que las heredan no cambian al mismo ritmo. Si no hay forma de saber en qué punto quedó cada proyecto, aparecen dos problemas: un proyecto que se quedó atrás cree que está al día, y otro que sí está al día no puede demostrarlo.

Esta épica pone número a las reglas y fecha a la adopción. Cada proyecto declara qué versión sigue, y al abrir sesión se le avisa si quedó atrás. No se migra solo: avisar es una cosa, decidir cambiar es otra.

También fija qué pasa con el trabajo ya cerrado cuando una regla cambia. Lo cerrado queda sellado con la versión que tenía y no se reabre, para que afinar una redacción no obligue a volver sobre lo terminado.

## 3. Problema y oportunidad

### 3.1 Situación actual

No existe todavía ninguna regla escrita, así que tampoco hay forma de decir cuál versión sigue un proyecto. Apenas las reglas empiecen a cambiar, la pregunta va a aparecer en la primera sesión.

### 3.2 Impacto de no hacerlo

Un proyecto puede estar incumpliendo una regla que se agregó hace meses y nadie se entera. Y una regla corregida no se puede distinguir de una regla nueva que obliga a hacer algo distinto, así que cada cambio genera duda sobre si hay que revisar todo otra vez.

### 3.3 Evidencia

| Fuente | Hallazgo |
|---|---|
| Experiencia con librerías compartidas entre proyectos | Sin número de versión, nadie sabe qué tiene instalado ni qué le falta |

## 4. Objetivo y propuesta de valor

**Objetivo.** Que cualquiera pueda saber, sin leer las reglas una por una, si un proyecto quedó atrás y qué cambió desde la versión que adoptó.

**Hipótesis de valor.** Si cada cambio de reglas sube un número y deja escrito qué cambió, la persona va a poder decidir cuándo actualizar cada proyecto en vez de vivir con la duda. Se sabrá cuando se pueda responder "este proyecto está al día" mirando un solo dato.

### 4.1 Beneficios esperados

| Beneficiario | Beneficio | Tipo |
|---|---|---|
| La persona | Sabe qué proyectos actualizar y cuáles no | Cualitativo |
| Un proyecto viejo | No se le reabre trabajo cerrado por un cambio de redacción | Cualitativo |
| La IA | Sabe qué reglas aplican a este proyecto y desde cuándo | Cualitativo |

## 5. Alcance

### 5.1 Dentro del alcance

- Un número de versión de las reglas, con criterio claro de cuándo sube cada parte del número.
- Un registro de qué cambió en cada versión.
- La declaración, dentro de cada proyecto, de qué versión adoptó y en qué fecha.
- El aviso al abrir sesión cuando el proyecto quedó atrás.
- La regla de que el trabajo cerrado queda sellado con su versión.

### 5.2 Fuera del alcance

- Migrar un proyecto solo. El aviso informa, la decisión es de la persona.
- Actualizar los archivos instalados en el proyecto. Eso es EP-007.

### 5.3 Diferido

- Un reporte que muestre de un vistazo el estado de varios proyectos a la vez. Se retoma cuando haya suficientes proyectos como para que valga la pena.

## 5.4 Alcance funcional completo

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Finalidad | Saber en qué punto de las reglas está cada proyecto, y qué cambió entre un punto y otro |
| 2 | Actores | Quien cambia una regla, quien adopta una versión en un proyecto, la IA que avisa al abrir sesión |
| 3 | Información | El número de versión vigente, la lista de cambios por versión, y la versión adoptada por cada proyecto con su fecha |
| 4 | Campos | La entrada del registro de cambios tiene campos definidos: versión, fecha, tipo de cambio, qué cambió y por qué. El detalle baja a la historia de usuario |
| 5 | Validaciones | Un cambio de reglas sin subir versión no se acepta; el número declarado por el proyecto tiene que existir en el registro |
| 6 | Reglas de negocio | Sube la parte mayor cuando un proyecto al día queda obligado a hacer algo nuevo; la menor cuando se agrega algo que no obliga; la última cuando solo cambia la redacción |
| 7 | Estados y transiciones | Un proyecto está al día o quedado atrás. Pasa a quedado atrás solo cuando la versión vigente cambia |
| 8 | Operaciones | Subir versión, registrar el cambio, declarar la adopción en un proyecto, comparar la adoptada con la vigente |
| 9 | Restricciones | No se cambia una regla sin subir versión y dejar registro; no se migra un proyecto sin que la persona lo decida |
| 10 | Relaciones | Cada entrada del registro apunta a las reglas que cambiaron; cada proyecto apunta a una versión |
| 11 | Consultas | Ver la versión vigente, ver qué cambió entre dos versiones, ver si un proyecto quedó atrás |
| 12 | Mensajes | Un aviso al abrir sesión cuando el proyecto quedó atrás, que diga cuánto atrás y qué cambió |
| 13 | Errores | Un proyecto que declara una versión que no existe; un cambio de reglas que no subió versión |
| 14 | Permisos | No aplica porque el control lo da el repositorio |
| 15 | Auditoría | El registro de cambios es el rastro. No se borran entradas |
| 16 | Resultado final | La épica está completa cuando cualquiera puede saber, con un solo dato, si un proyecto quedó atrás, y leer qué cambió desde entonces |

**Detalle adicional**

| # | Pregunta | Respuesta |
|---|---|---|
| 25 | Convivencia | El trabajo cerrado antes de un cambio queda con su versión sellada y no se reabre |
| 26 | Idioma | El registro de cambios se escribe en español, entendible por quien no siguió el detalle |

## 6. Usuarios y actores

| Actor | Rol en el proceso | Necesidad principal |
|---|---|---|
| La persona que cambia una regla | Sube la versión y escribe qué cambió | Que el criterio de qué parte del número sube sea claro |
| La persona que administra un proyecto | Decide cuándo adoptar una versión nueva | Saber qué le implicaría actualizar |
| La IA | Compara y avisa | Un dato que se pueda comparar sin interpretar |

## 7. Criterios de aceptación de la épica

- [ ] **CAE-01** Existe un número de versión de las reglas con criterio escrito de cuándo sube cada parte.
- [ ] **CAE-02** Todo cambio de reglas deja entrada en el registro de cambios.
- [ ] **CAE-03** Cada proyecto declara la versión que adoptó y la fecha.
- [ ] **CAE-04** Al abrir sesión se avisa si el proyecto quedó atrás, y no se migra solo.
- [ ] **CAE-05** El trabajo ya cerrado no se reabre por un cambio de reglas.

## 8. Métricas de éxito

| Métrica | Línea base | Meta | Cuándo se mide | Dónde |
|---|---|---|---|---|
| Cambios de reglas sin registro | Sin medir | Cero | Cada cambio | Revisión del registro |
| Tiempo en responder si un proyecto está al día | Hoy no se puede responder | Un vistazo | Al terminar la épica | Sesión real |

## 9. Historias de usuario

| ID | Título | Prioridad | Estimación |
|---|---|---|---|
| HU-001 | Fijar el número de versión y qué significa cada parte | Must | S |
| HU-002 | Llevar el registro de qué cambió en cada versión | Must | S |
| HU-003 | Declarar en el proyecto la versión adoptada y la fecha | Must | S |
| HU-004 | Avisar al abrir sesión cuando el proyecto quedó atrás | Must | M |
| HU-005 | Sellar el trabajo cerrado con su versión | Should | S |

## 10. Consideraciones técnicas

### 10.1 Componentes afectados

| Componente | Impacto | Observaciones |
|---|---|---|
| Cuerpo de reglas | Modificado | Se le agrega la regla de versionar |
| Capa de proyecto | Modificado | Se le agrega la declaración de versión adoptada |

### 10.2 Decisiones de arquitectura

- El número vive en un archivo aparte, de una sola línea, para que un programa lo pueda leer sin interpretar texto.
- Quien decide si el cambio es mayor, menor o de redacción es la persona. Eso es criterio y no se automatiza.

### 10.4 Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| Comparabilidad | El dato de versión se compara sin leer prosa |
| Trazabilidad | Cada entrada del registro deja saber qué reglas tocó |

## 11. Dependencias

| ID | Dependencia | Tipo | Estado |
|---|---|---|---|
| DEP-01 | EP-001, porque no se versiona lo que todavía no existe | Interna | Bloqueante |

## 12. Riesgos

| ID | Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|---|
| R-01 | Que alguien cambie una regla y olvide subir la versión | Alta | Alto | Se cubre en EP-005 con un automatismo que lo impida al publicar |
| R-02 | Que el aviso de desactualización se vuelva ruido y se ignore | Media | Medio | Que diga qué cambió, no solo que hay diferencia |

## 13. Supuestos y restricciones

**Supuestos**

- Los proyectos que heredan las reglas se actualizan de a uno, cuando la persona lo decide.

**Restricciones**

- El dato de versión tiene que poder leerse sin internet y sin herramientas especiales.

## 14. Hoja de ruta

| Fase | Contenido | HU |
|---|---|---|
| Fase 1 | Número y registro de cambios | HU-001, HU-002 |
| Fase 2 | Adopción y aviso | HU-003, HU-004 |
| Fase 3 | Sellado del trabajo cerrado | HU-005 |

## 15. Definition of Ready

- [ ] Criterio de subida de versión acordado
- [ ] Formato del registro de cambios definido

## 16. Definition of Done

- [ ] Todas las historias obligatorias aceptadas
- [ ] Criterios de aceptación verificados
- [ ] Un proyecto de prueba declara versión y recibe el aviso cuando la vigente cambia

## 17. Bitácora de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-13 | Ing. José Dúmar Jiménez Ruíz | Creación de la épica desde el brief |
