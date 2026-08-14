# Plan de Pruebas — Fase A-EP-001-HU-001-molde-de-regla

**Para qué sirve este documento.** Dice cómo se comprueba que el molde hace lo que [HU-001](../HU-001-formato-unico-de-regla.md) pidió: con qué casos, sobre qué reglas de ejemplo y qué resultado se espera de cada paso. Su exigencia central es que ningún criterio de aceptación quede sin al menos un caso. Existe antes de correr la primera prueba; los resultados se van anotando encima. La lista de tareas vive en el [plan_trabajo.md](plan_trabajo.md) de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-001 |
| **Versión** | 1.0 |
| **Alcance del plan** | [HU-001](../HU-001-formato-unico-de-regla.md), fase A |
| **Fecha** | 2026-08-13 |
| **Elaborado por** | Ing. José Dúmar Jiménez Ruíz |
| **Aprobado por** | Pendiente |
| **Estado** | Borrador |

Va junto con el [plan_trabajo.md](plan_trabajo.md) de esta fase. Por proporcionalidad, una fase sola usa las secciones 3, 5, 6, 9 y 12 de la plantilla; el resto queda fuera a propósito.

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

El entregable de esta fase es texto normativo, no código. No hay nada que ejecutar, así que los niveles se leen distinto de lo habitual.

| Nivel | Objetivo | Responsable | Automatizado |
|---|---|---|---|
| Revisión contra el molde | Que cada regla escrita tenga todas las partes que el molde exige | Quien escribe | No |
| Prueba de uso | Que se pueda citar una regla desde otro documento y el enlace llegue | Quien escribe | No |
| Prueba de ruptura | Escribir a propósito una regla mal formada y comprobar que se detecta | Quien escribe | No |
| Lectura por alguien ajeno | Que el molde lo entienda quien no sabe del tema | Usuario | No |

**Por qué nada está automatizado.** El programa que comprueba la forma de una regla es de [EP-004](../../../EP-004-comprobacion-automatica/epica.md), y todavía no existe. Esta fase deja marcado en el molde qué partes son comprobables, para que ese programa se pueda escribir después sin volver a leer todas las reglas.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | Sí | Los criterios de aceptación de HU-001 |
| Usabilidad | Sí | El molde se entiende sin capacitación ni instructivo aparte |
| Seguridad | No | No hay sistema, ni usuarios, ni datos |
| Rendimiento | No | No hay nada que ejecutar |
| Compatibilidad | No | Son archivos de texto |
| Migración de datos | No | No hay datos |

### 3.3 Técnicas de diseño de casos

- **Partición de equivalencia.** Reglas bien formadas contra reglas mal formadas, y dentro de las mal formadas, cada forma de estarlo por separado: sin ejemplo, con dos exigencias, con identificador repetido.
- **Valores límite.** La regla que no admite ejemplo, la que no depende de ninguna otra, la que no tiene excepciones. Son los casos donde el molde puede quedarse corto.
- **Prueba de ruptura.** Escribir a propósito lo que el molde prohíbe, para comprobar que la revisión lo detecta y no que simplemente nunca aparece.

### 3.4 Priorización

| Prioridad | Criterio | Casos |
|---|---|---|
| Crítica | Sin esto, ninguna regla posterior se puede citar ni comprobar | CP-001, CP-002 |
| Alta | Lo que el molde promete detectar y tiene que detectar | CP-003, CP-005 |
| Media | Los casos límite del molde | CP-004, CP-006, CP-007 |

### 3.5 Alcance de la corrida automatizada

Ninguna. No hay suite que correr en esta fase. Cuando exista el programa de EP-004, la corrida de las fases siguientes sí lo incluirá.

## 5. Matriz de trazabilidad

| HU | CA | Casos de prueba | Tipo | Prioridad | Estado |
|---|---|---|---|---|---|
| HU-001 | CA-01 | CP-001, CP-002 | Funcional | Crítica | Pendiente |
| HU-001 | CA-02 | CP-003, CP-004 | Funcional | Alta | Pendiente |
| HU-001 | CA-03 | CP-005 | Funcional | Alta | Pendiente |
| HU-001 | RNF-01 | CP-006 | Usabilidad | Media | Pendiente |
| HU-001 | Transversal, límites | CP-007 | Funcional | Media | Pendiente |

**Cobertura:** 3 criterios de aceptación de 3, más el requisito no funcional y el transversal de límites. 100%.

## 6. Casos de prueba

### CP-001 — Una regla escrita con el molde queda completa

| Campo | Valor |
|---|---|
| **HU y CA** | HU-001, CA-01 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | El molde está escrito en `base/20-meta-reglas/estructura-regla.md` |
| **Datos de entrada** | La regla del identificador, escrita con el molde |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir el molde y anotar la lista de partes obligatorias | Queda una lista cerrada, sin ambigüedad sobre qué es obligatorio |
| 2 | Abrir la regla escrita y buscar cada parte de esa lista | Están todas: identificador, título, exigencia, ejemplo incorrecto, ejemplo correcto |
| 3 | Contar cuántas cosas exige la regla | Exige una sola |

**Resultado esperado final:** la regla tiene todas las partes obligatorias y una sola exigencia.
**Postcondiciones:** ninguna. La revisión no modifica nada.

### CP-002 — Una cita desde otro documento llega a la regla

| Campo | Valor |
|---|---|
| **HU y CA** | HU-001, CA-01 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | Existen las dos reglas del capítulo y su índice |
| **Datos de entrada** | Una cita escrita con la forma que define el molde |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | En un documento cualquiera, escribir una cita a la regla usando solo capítulo e identificador | La cita queda escrita con la forma acordada |
| 2 | Seguir la cita | Lleva a la regla, no a un enlace roto ni al capítulo entero |
| 3 | Cambiarle el identificador a uno que no existe y seguir la cita otra vez | No llega a ninguna parte, que es lo esperado |

**Resultado esperado final:** la cita bien escrita llega, la mal escrita no.
**Postcondiciones:** se deshace el cambio del paso 3.

### CP-003 — Una regla con dos exigencias se detecta

| Campo | Valor |
|---|---|
| **HU y CA** | HU-001, CA-02 |
| **Tipo** | Funcional, ruptura |
| **Prioridad** | Alta |
| **Precondiciones** | El molde exige una sola cosa por regla |
| **Datos de entrada** | Una regla escrita a propósito con dos exigencias: dónde se guarda un documento y en qué idioma se escribe |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir la regla doble | Queda escrita, porque nada impide escribir un archivo |
| 2 | Revisarla contra el molde, parte por parte | La revisión señala que hay más de una exigencia |
| 3 | Anotar en qué parte del molde se apoya la señal | El molde dice explícitamente que la exigencia es una sola |

**Resultado esperado final:** la regla doble no pasa la revisión, y el motivo se puede señalar en el molde.
**Postcondiciones:** la regla de prueba se borra o se parte, según CP-004.

### CP-004 — La regla partida en dos sí pasa

| Campo | Valor |
|---|---|
| **HU y CA** | HU-001, CA-02 |
| **Tipo** | Funcional, recuperación |
| **Prioridad** | Media |
| **Precondiciones** | CP-003 ejecutado |
| **Datos de entrada** | La regla doble de CP-003 |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Partir la regla en dos, cada una con su identificador libre | Quedan dos reglas |
| 2 | Revisar cada una contra el molde | Las dos pasan |
| 3 | Comprobar que los dos identificadores son distintos y libres | No hay choque |

**Resultado esperado final:** las dos reglas pasan la revisión.

### CP-005 — Un identificador repetido se detecta

| Campo | Valor |
|---|---|
| **HU y CA** | HU-001, CA-03 |
| **Tipo** | Funcional, ruptura |
| **Prioridad** | Alta |
| **Precondiciones** | El capítulo tiene al menos dos reglas |
| **Datos de entrada** | El identificador de una regla que ya existe |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Ponerle a una regla el identificador de otra | Quedan dos reglas con el mismo identificador |
| 2 | Revisar el índice del capítulo | El identificador aparece dos veces |
| 3 | Cambiar el de la segunda por uno libre y revisar otra vez | Cada identificador aparece una sola vez |

**Resultado esperado final:** la repetición se ve en el índice y el cambio la resuelve.
**Postcondiciones:** el capítulo queda sin identificadores repetidos.

### CP-006 — El molde se entiende sin saber del tema

| Campo | Valor |
|---|---|
| **HU y CA** | HU-001, RNF-01 |
| **Tipo** | Usabilidad |
| **Prioridad** | Media |
| **Precondiciones** | El molde y las dos reglas están escritos |
| **Datos de entrada** | El molde, leído por alguien que no participó en escribirlo |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Entregar el molde a alguien que no lo escribió, sin explicación previa | Lo lee de corrido |
| 2 | Pedirle que escriba una regla siguiéndolo, sobre cualquier tema | La escribe sin hacer preguntas sobre el molde mismo |
| 3 | Revisar esa regla contra el molde | Tiene todas las partes obligatorias |

**Resultado esperado final:** alguien que no escribió el molde puede usarlo a la primera.
**Postcondiciones:** cada pregunta que sí haya tenido que hacer se anota como defecto de redacción del molde.

### CP-007 — Una regla que no admite ejemplo

| Campo | Valor |
|---|---|
| **HU y CA** | HU-001, transversal de límites |
| **Tipo** | Funcional, valor límite |
| **Prioridad** | Media |
| **Precondiciones** | El molde está escrito |
| **Datos de entrada** | Una exigencia que no se puede mostrar con un ejemplo de incorrecto y correcto |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar en el molde qué hacer cuando no hay ejemplo posible | El molde lo dice, no queda al criterio de cada quien |
| 2 | Escribir la regla siguiendo esa salida | Queda escrita y la ausencia de ejemplo está justificada en la regla |
| 3 | Revisarla contra el molde | Pasa, y se ve por qué no lleva ejemplo |

**Resultado esperado final:** el molde tiene una salida escrita para este caso y la regla la usa.

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición acá | Atención |
|---|---|---|
| Crítica | El molde deja pasar una regla que no se puede citar, o el esquema de identificadores obliga a renumerar | Antes de escribir cualquier otra regla |
| Alta | El molde no detecta algo que prometió detectar | Dentro de la fase |
| Media | El molde se entiende mal y hay que preguntar para usarlo | Dentro de la fase |
| Baja | Redacción, ejemplo poco claro | Antes de cerrar la fase |

### 9.2 Flujo del defecto

Nuevo, asignado, en corrección, listo para revisar, verificado, cerrado. Si al verificar sigue fallando, vuelve a en corrección.

### 9.3 Contenido mínimo de un reporte

- Identificador y título.
- Severidad.
- Qué caso de prueba lo destapó.
- Qué parte del molde falla y qué se esperaba de ella.
- La regla de ejemplo con la que se reprodujo.

### 9.4 Registro

| ID | Título | Caso | Severidad | Estado |
|---|---|---|---|---|
| Ninguno todavía | | | | |

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de criterios | Criterios con caso sobre criterios totales | 100% |
| Casos ejecutados | Ejecutados sobre diseñados | 100%, porque son siete |
| Preguntas que tuvo que hacer quien leyó el molde | Conteo en CP-006 | Cero |

### 12.2 Resumen de ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos |
|---|---:|---:|---:|---:|
| 1 | 7 | 0 | 0 | 0 |

### 12.3 Concepto final

Pendiente. Se llena al terminar la ejecución.

## 14. Control de versiones

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0 | 2026-08-13 | Ing. José Dúmar Jiménez Ruíz | Versión inicial, junto con el plan de trabajo |
