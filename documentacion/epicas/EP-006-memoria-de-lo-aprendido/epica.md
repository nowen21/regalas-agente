# EP-006 — Memoria de lo aprendido, buscable

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | EP-006 |
| **Brief de origen** | [brief.md](../../../brief.md) |
| **Iniciativa** | Que una IA que programa trabaje siempre igual |
| **Producto** | Estándar de agente para desarrollo de software |
| **Tipo** | Negocio |
| **Prioridad** | Must |
| **Estimación** | M |
| **Horizonte** | Primera entrega |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Propuesta |

## 2. Resumen ejecutivo

Las reglas guardan lo que vale para todos los proyectos. Pero hay otra clase de conocimiento que no cabe ahí: por qué este proyecto usa borrado lógico, cómo se resolvió aquel error raro, qué decidió el cliente sobre el redondeo. Eso no es una regla, es lo que este trabajo aprendió.

Esta épica construye el lugar donde queda ese conocimiento y la forma de encontrarlo. Se guarda separado por alcance: lo que solo le sirve a un proyecto y lo que le sirve a todos. Así una lección aprendida peleando en un proyecto aparece cuando se abre otro, meses después, aunque sea de otro lenguaje.

Se busca por palabra y también por significado, con un modelo que corre en la máquina, porque el contenido no puede salir de ahí.

## 3. Problema y oportunidad

### 3.1 Situación actual

Lo aprendido queda en la cabeza de la persona o en un chat que se borró. Cuando aparece el mismo problema en otro proyecto, se resuelve otra vez desde cero.

### 3.2 Impacto de no hacerlo

Se repite el mismo error en proyectos distintos, y las decisiones ya tomadas se vuelven a discutir porque nadie recuerda por qué se tomaron.

### 3.3 Evidencia

| Fuente | Hallazgo |
|---|---|
| Trabajo en varios proyectos a la vez | Lo aprendido en uno no llegó a los otros, y el mismo error volvió a aparecer |

## 4. Objetivo y propuesta de valor

**Objetivo.** Que lo aprendido quede escrito una sola vez, se pueda buscar y aparezca cuando hace falta, incluso en otro proyecto y meses después.

**Hipótesis de valor.** Si lo aprendido en un proyecto está guardado y se puede buscar, no se repite el error en el siguiente. Se sabrá cuando una búsqueda en un proyecto nuevo devuelva algo aprendido en uno viejo y eso cambie la decisión.

### 4.1 Beneficios esperados

| Beneficiario | Beneficio | Tipo |
|---|---|---|
| La persona | No vuelve a explicar lo mismo ni a resolver dos veces el mismo problema | Cualitativo |
| Un proyecto nuevo | Arranca sabiendo lo que costó aprender en los anteriores | Cualitativo |
| La IA | Encuentra el porqué de una decisión sin preguntarlo otra vez | Cualitativo |

## 5. Alcance

### 5.1 Dentro del alcance

- Un lugar donde se guarda lo aprendido, dentro del repositorio, para que se vea en el historial y viaje a otra máquina.
- La separación por alcance: lo de un proyecto y lo que sirve a todos.
- Los tipos de lo que se guarda: decisión tomada, error resuelto, patrón que se repite, aprendizaje.
- Búsqueda por palabra.
- Búsqueda por significado, opcional, con un modelo que corre en la máquina.
- La distinción entre lo que el proyecto aprendió y cómo el usuario quiere que se trabaje, que son dos cosas distintas.
- Que lo que hay que recordar quede en el repositorio y no en el almacén local de la herramienta.

### 5.2 Fuera del alcance

- Detectar que dos cosas guardadas se contradicen. Decidir eso es criterio, no cálculo.
- Sacar el contenido de la máquina para procesarlo en otro lado.
- Guardar automáticamente todo lo que pasa. Lo que se guarda se decide al guardarlo.

### 5.3 Diferido

- La poda de lo que ya no aplica y la marca de vigencia. Se retoma cuando el volumen lo pida.
- El registro de qué se buscó y si sirvió, para saber si la memoria vale la pena.

## 5.4 Alcance funcional completo

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | Finalidad | Que lo aprendido quede guardado y se pueda encontrar cuando haga falta |
| 2 | Actores | La IA, que guarda y busca; la persona, que decide qué merece guardarse y qué sube de alcance |
| 3 | Información | Cada cosa guardada tiene qué pasó, de qué tipo es, a qué alcance pertenece y cuándo se guardó |
| 4 | Campos | Lo guardado tiene campos definidos: contenido, tipo, alcance, fecha, proyecto de origen. El detalle baja a la historia de usuario |
| 5 | Validaciones | Lo guardado no puede quedar sin tipo ni sin alcance; no se guarda una clave ni un dato personal |
| 6 | Reglas de negocio | Se guarda lo que no se puede recuperar leyendo el código; lo que sirve a todos sube de alcance; lo que dice cómo trabajar es preferencia del usuario y va aparte de lo que el proyecto aprendió |
| 7 | Estados y transiciones | Lo guardado está activo. Cuando deja de aplicar, se marca, no se borra |
| 8 | Operaciones | Guardar, buscar por palabra, buscar por significado, subir de alcance, marcar que ya no aplica |
| 9 | Restricciones | El contenido no sale de la máquina; lo que hay que recordar no se guarda en el almacén local de la herramienta |
| 10 | Relaciones | Lo guardado puede apuntar a otra cosa guardada y al trabajo donde nació |
| 11 | Consultas | Buscar por palabra, por significado, filtrando por tipo, por alcance y por proyecto |
| 12 | Mensajes | Cuando la búsqueda por significado no está disponible, se avisa y se busca solo por palabra |
| 13 | Errores | Búsqueda sin resultados, falta de las dependencias opcionales, base que no se puede abrir |
| 14 | Permisos | No aplica porque corre en la máquina de quien trabaja |
| 15 | Auditoría | Queda la fecha de guardado y el trabajo donde nació |
| 16 | Resultado final | La épica está completa cuando una búsqueda en un proyecto devuelve lo aprendido en otro, sin que el contenido haya salido de la máquina |

**Detalle adicional**

| # | Pregunta | Respuesta |
|---|---|---|
| 17 | Ciclo de vida | Lo que deja de aplicar se marca, no se borra, porque saber que algo se descartó también sirve |
| 23 | Volumen | Cientos de registros por ahora, con espacio para crecer a miles |
| 24 | Datos sensibles | No se guardan claves ni datos personales. Lo que se guarda es la decisión, no el dato |

## 6. Usuarios y actores

| Actor | Rol en el proceso | Necesidad principal |
|---|---|---|
| La IA | Guarda lo aprendido y lo busca al arrancar | Encontrar lo que aplica, sin leerlo todo |
| La persona | Decide qué se guarda y qué sube de alcance | Que no se llene de ruido |

**Volumetría estimada.** Cientos de registros, un usuario, varios proyectos.

## 7. Criterios de aceptación de la épica

- [ ] **CAE-01** Lo aprendido queda guardado dentro del repositorio, visible en el historial.
- [ ] **CAE-02** Lo guardado se separa por alcance, entre lo de un proyecto y lo que sirve a todos.
- [ ] **CAE-03** Se puede buscar por palabra sin instalar nada.
- [ ] **CAE-04** Se puede buscar por significado con un modelo que corre en la máquina, y si falta, la búsqueda sigue funcionando por palabra.
- [ ] **CAE-05** El contenido de lo guardado no sale de la máquina.
- [ ] **CAE-06** Lo que hay que recordar queda en el repositorio, no en el almacén local de la herramienta.

## 8. Métricas de éxito

| Métrica | Línea base | Meta | Cuándo se mide | Dónde |
|---|---|---|---|---|
| Búsquedas que devuelven algo útil de otro proyecto | Ninguna, hoy | Que ocurra | Después de dos proyectos | Uso real |
| Cosas que hay que volver a explicar en un proyecto nuevo | Todas, hoy | Que bajen | Al abrir el siguiente proyecto | Observación |

## 9. Historias de usuario

| ID | Título | Prioridad | Estimación |
|---|---|---|---|
| HU-001 | Definir qué se guarda, con qué tipos y qué alcances | Must | S |
| HU-002 | Guardar lo aprendido en el repositorio | Must | M |
| HU-003 | Buscar por palabra sin instalar nada | Must | M |
| HU-004 | Buscar por significado con un modelo local y opcional | Should | L |
| HU-005 | Separar lo que el proyecto aprendió de cómo el usuario quiere trabajar | Must | S |
| HU-006 | Sacar del almacén local lo que deba vivir en el repositorio | Must | M |
| HU-007 | Marcar lo que dejó de aplicar sin borrarlo | Should | S |

## 10. Consideraciones técnicas

### 10.1 Componentes afectados

| Componente | Impacto | Observaciones |
|---|---|---|
| Memoria | Nuevo | |
| Automatismos | Modificado | Uno de ellos recoge lo que quedó guardado por fuera |

### 10.2 Decisiones de arquitectura

- Lo aprendido se guarda en archivos del repositorio y en una base de un solo archivo, no en un servicio. Lo local no se ve en el historial, no se puede revisar y no viaja a otra máquina.
- La búsqueda por significado es opcional. Sin ella todo sigue funcionando por palabra, para que nadie tenga que instalar nada obligatoriamente.
- El modelo que traduce texto a números corre en la máquina. Un servicio externo se descarta por privacidad, no solo por poder trabajar sin internet.

### 10.4 Requisitos no funcionales

| Categoría | Requisito |
|---|---|
| Privacidad | El contenido no sale de la máquina |
| Degradación | Si faltan las dependencias opcionales, la búsqueda sigue sirviendo con menos |
| Portabilidad | La memoria viaja con el repositorio a otra máquina |

## 11. Dependencias

| ID | Dependencia | Tipo | Estado |
|---|---|---|---|
| DEP-01 | EP-001, porque la regla que obliga a guardar en el repositorio es parte del cuerpo de reglas | Interna | Bloqueante |

## 12. Riesgos

| ID | Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|---|
| R-01 | Que se guarde todo y la memoria se vuelva ruido | Alta | Alto | Solo se guarda lo que no se recupera leyendo el código |
| R-02 | Que queden dos versiones del mismo recuerdo, una en el repositorio y otra local | Alta | Alto | El almacén local queda vacío, y un automatismo lo recoge |
| R-03 | Que la búsqueda no encuentre lo que existe y nadie lo note | Media | Alto | Se combinan las dos formas de buscar, por palabra y por significado |
| R-04 | Que dos cosas guardadas se contradigan | Media | Medio | Queda fuera del alcance por ahora. Se anota como mejora |

## 13. Supuestos y restricciones

**Supuestos**

- El volumen se queda en cientos de registros por bastante tiempo.

**Restricciones**

- Sin servicios en la nube. Sin extensiones nativas, que en Windows son frágiles.

## 14. Hoja de ruta

| Fase | Contenido | HU |
|---|---|---|
| Fase 1 | Qué se guarda y dónde | HU-001, HU-002, HU-005 |
| Fase 2 | Búsqueda por palabra | HU-003 |
| Fase 3 | Recogida de lo local y marca de lo que no aplica | HU-006, HU-007 |
| Fase 4 | Búsqueda por significado | HU-004 |

## 15. Definition of Ready

- [ ] Tipos y alcances acordados
- [ ] Criterio de qué merece guardarse acordado

## 16. Definition of Done

- [ ] Todas las historias obligatorias aceptadas
- [ ] El almacén local queda vacío
- [ ] La búsqueda funciona sin instalar nada, y mejor si se instala lo opcional
- [ ] Ninguna clave ni dato personal quedó guardado

## 17. Bitácora de cambios

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-13 | Ing. José Dúmar Jiménez Ruíz | Creación de la épica desde el brief |
