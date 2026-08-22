# Plan de Pruebas — Fase A-EP-003-HU-010-glosario-de-la-terminologia

**Para qué sirve este documento.** Dice cómo se comprueba que el glosario hace lo que [documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/HU-010-glosario-de-la-terminologia.md](../HU-010-glosario-de-la-terminologia.md) pidió: con qué casos, sobre qué términos y qué resultado se espera de cada paso. Su exigencia central es que ningún criterio de aceptación quede sin al menos un caso. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar: lo que pase al correrlas va en el `resultado_pruebas.md` de esta fase. La lista de tareas vive en el [plan_trabajo.md](plan_trabajo.md).

| Campo | Valor |
|---|---|
| **Código** | PP-EP003-HU010-A |
| **Versión** | 1.2 |
| **Alcance del plan** | [documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/HU-010-glosario-de-la-terminologia.md](../HU-010-glosario-de-la-terminologia.md), fase A |
| **Fecha** | 2026-08-14 |
| **Elaborado por** | Ing. José Dúmar Jiménez Ruíz |
| **Aprobado por** | Pendiente |
| **Estado** | Borrador |

Va junto con el [plan_trabajo.md](plan_trabajo.md) de esta fase. Por proporcionalidad, una fase sola usa las secciones 3, 5, 6, 9 y 12 de la plantilla; el resto queda fuera a propósito.

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

El entregable es un documento de referencia, no código. No hay nada que ejecutar, así que los niveles se leen distinto de lo habitual.

| Nivel | Objetivo | Responsable | Automatizado |
|---|---|---|---|
| Revisión de cobertura | Que los términos que el estándar usa estén, y que no sobre ninguno inventado | Quien escribe | No |
| Prueba de uso | Que buscar un término desconocido lo encuentre y lo explique | Quien escribe | No |
| Recorrido de enlaces | Que cada entrada lleve al detalle en un paso, sin enlaces rotos | Quien escribe | Parcial |
| Prueba de ruptura | Buscar a propósito un término que no es del estándar, y comprobar que no está | Quien escribe | No |
| Lectura por alguien ajeno | Que las definiciones las entienda quien no sabe del tema | Usuario | No |

**Qué está automatizado y qué no.** Los enlaces los revisa [`validadores/enlaces.py`](../../../../../validadores/enlaces.py), que ya existe: eso cubre que ninguno esté roto. Lo que ningún programa puede decir es si la definición se entiende, si el término sobra o si falta uno. Eso se lee.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | Sí | Los criterios de aceptación de HU-010 |
| Usabilidad | Sí | El glosario se entiende sin explicación previa |
| Seguridad | No | No hay sistema, ni usuarios, ni datos |
| Rendimiento | No | No hay nada que ejecutar |
| Compatibilidad | No | Son archivos de texto |
| Migración de datos | No | No hay datos |

### 3.3 Técnicas de diseño de casos

- **Partición de equivalencia.** Términos que sí son del estándar contra términos que no lo son. Y dentro de los que sí: los que tienen traducción usada y los que no.
- **Valores límite.** El término que aparece en una sola regla, el que aparece en cuatro capítulos con matices distintos, y el que está en otro idioma sin traducción. Son los casos donde la definición de una línea puede quedarse corta.
- **Muestreo dirigido.** Cinco términos de capítulos distintos, no cinco del mismo, para que la prueba no pase por haber cubierto bien un solo rincón.
- **Prueba de ruptura.** Buscar un término que no es del estándar, para comprobar que el glosario tiene borde y no se llenó de palabras sueltas.

### 3.4 Priorización

| Prioridad | Criterio | Casos |
|---|---|---|
| Crítica | Sin esto el glosario no sirve para lo que se pidió | CP-001, CP-002 |
| Alta | Lo que el glosario promete y tiene que cumplir | CP-004, CP-005 |
| Media | El borde del glosario y su legibilidad | CP-003, CP-006, CP-007, CP-008 |

### 3.5 Alcance de la corrida automatizada

Solo [`validadores/enlaces.py`](../../../../../validadores/enlaces.py), sobre los archivos tocados en esta fase. No se corre la suite completa del repositorio: `02·F5` pide corrida quirúrgica, y ningún otro validador toca lo que esta fase escribe.

## 5. Matriz de trazabilidad

| HU | CA | Casos de prueba | Tipo | Prioridad | Estado |
|---|---|---|---|---|---|
| HU-010 | [CA-01](../HU-010-glosario-de-la-terminologia.md#ca-01--cada-término-está-definido-en-una-línea) | CP-001, CP-002 | Funcional | Crítica | Pendiente |
| HU-010 | [CA-02](../HU-010-glosario-de-la-terminologia.md#ca-02--cada-entrada-dice-dónde-vive-y-qué-regla-lo-manda) | CP-004, CP-005 | Funcional | Alta | Pendiente |
| HU-010 | [CA-03](../HU-010-glosario-de-la-terminologia.md#ca-03--se-ve-qué-quedó-en-otro-idioma) | CP-008 | Funcional | Media | Pendiente |
| HU-010 | RNF-01, se entiende sin saber del tema | CP-006 | Usabilidad | Media | Pendiente |
| HU-010 | RNF-02, enlaza y no copia | CP-007 | Funcional | Media | Pendiente |
| HU-010 | Transversal, el borde del glosario | CP-003 | Funcional | Media | Pendiente |

**Cobertura:** 3 criterios de aceptación de 3, más los dos requisitos no funcionales y el transversal de borde. 100%.

## 6. Casos de prueba

### CP-001 — Los términos que el estándar usa están en el glosario

| Campo | Valor |
|---|---|
| **HU y CA** | HU-010, CA-01 |
| **Tipo** | Funcional, cobertura |
| **Prioridad** | Crítica |
| **Precondiciones** | El glosario está escrito en `base/glosario.md` |
| **Datos de entrada** | La lista de términos levantada en T-01, agrupada en los cuatro grupos |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tomar la lista de términos levantada en T-01 | Queda a la vista la lista de origen, con el archivo donde está |
| 2 | Contar cuántos términos tiene por grupo | Queda un número por grupo, no una impresión |
| 3 | Buscar cada uno en el glosario | Están todos, o los que falten quedan anotados con el motivo |
| 4 | Contar los términos del glosario que no estaban en la lista | Cero, o cada uno justificado con dónde aparece en el estándar |

**Resultado esperado final:** la lista levantada y el glosario coinciden, y cualquier diferencia tiene motivo escrito.
**Postcondiciones:** ninguna. La revisión no modifica el glosario.

### CP-002 — Cinco términos de capítulos distintos se encuentran definidos

| Campo | Valor |
|---|---|
| **HU y CA** | HU-010, CA-01 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | El glosario está escrito |
| **Datos de entrada** | Cinco términos tomados de cinco capítulos distintos de `base/`, elegidos antes de mirar el glosario |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Elegir los cinco términos leyendo los capítulos, no el glosario | Quedan cinco, de cinco capítulos distintos |
| 2 | Buscar cada uno en el glosario | Los cinco están |
| 3 | Contar los renglones de cada definición | Cada una cabe en una línea |
| 4 | Comprobar que la definición no usa otra palabra técnica sin explicar | Ninguna definición manda a buscar otro término para poder entenderla |

**Resultado esperado final:** los cinco están, en una línea, y se entienden sin salto a otro término.
**Postcondiciones:** ninguna.

### CP-003 — Un término que no es del estándar no está

| Campo | Valor |
|---|---|
| **HU y CA** | HU-010, transversal del borde |
| **Tipo** | Funcional, ruptura |
| **Prioridad** | Media |
| **Precondiciones** | El glosario está escrito |
| **Datos de entrada** | Tres palabras del oficio que el estándar no usa en ninguna regla ni plantilla |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Comprobar con una búsqueda en `base/`, `plantillas/` y `skills/` que las tres no aparecen | Cero apariciones |
| 2 | Buscarlas en el glosario | No están |
| 3 | Si alguna está, comprobar de dónde salió | Se quita, o se anota dónde sí aparece y la búsqueda del paso 1 estaba mal hecha |

**Resultado esperado final:** el glosario tiene borde: solo entra lo que el estándar usa (RN-05 de la HU).
**Postcondiciones:** el término que sobraba se quita.

### CP-004 — Cada entrada lleva al detalle en un paso

| Campo | Valor |
|---|---|
| **HU y CA** | HU-010, CA-02 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Alta |
| **Precondiciones** | El glosario tiene sus entradas con regla y ubicación |
| **Datos de entrada** | Tres entradas de tres grupos distintos |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Elegir tres entradas de tres grupos distintos del glosario | Quedan tres anotadas, una por grupo |
| 2 | Anotar qué regla dice cada una que lo manda | Las tres nombran una regla, ninguna dice "ver el capítulo" |
| 3 | Seguir el enlace de la regla | Llega a la regla, no al índice del capítulo |
| 4 | Comprobar que esa regla de verdad exige lo que la entrada dice | Coincide |
| 5 | Seguir el enlace de dónde vive el documento | El documento está donde dice |

**Resultado esperado final:** las tres entradas llevan al detalle en un paso y lo que prometen es cierto.
**Postcondiciones:** ninguna.

### CP-005 — Ningún enlace del glosario está roto

| Campo | Valor |
|---|---|
| **HU y CA** | HU-010, CA-02 |
| **Tipo** | Funcional, automatizado |
| **Prioridad** | Alta |
| **Precondiciones** | El glosario está escrito y los tres índices lo enlazan |
| **Datos de entrada** | `base/glosario.md`, `base/README.md`, `README.md`, `anatomia/mapa-del-sitio.md` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validadores/enlaces.py` sobre los archivos tocados | Termina sin señalar enlaces rotos |
| 2 | Desde cada una de las tres puertas de entrada, seguir el enlace al glosario | Las tres llegan |
| 3 | Romper a propósito un enlace del glosario | El archivo queda con un enlace que no resuelve |
| 4 | Volver a correr el validador | Lo señala |
| 5 | Deshacer el enlace roto | El archivo vuelve a como estaba |
| 6 | Correr el validador otra vez | Vuelve a quedar limpio |

**Resultado esperado final:** los enlaces resuelven, y el validador de verdad los está mirando.
**Postcondiciones:** se deshace el cambio del paso 3.

### CP-006 — Las definiciones se entienden sin saber del tema

| Campo | Valor |
|---|---|
| **HU y CA** | HU-010, RNF-01 |
| **Tipo** | Usabilidad |
| **Prioridad** | Media |
| **Precondiciones** | El glosario está escrito |
| **Datos de entrada** | Cinco entradas, leídas por alguien que no participó en escribirlas |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Conseguir a alguien que no haya participado en escribir el glosario | Queda quién va a leer, con su nombre |
| 2 | Entregarle las cinco entradas sin explicación previa | Las lee de corrido |
| 3 | Pedirle que diga con sus palabras qué es cada una | Lo dice, sin volver a leer la entrada |
| 4 | Anotar cada pregunta que tuvo que hacer | Cada pregunta es un defecto de redacción de esa entrada |
| 5 | Releer el glosario entero contra la lista de marcadores de generación automática | Ninguna de las ocho secciones de la lista aparece |

**Resultado esperado final:** alguien de fuera entiende las cinco a la primera.
**Postcondiciones:** cada pregunta del paso 4 se corrige en su entrada antes de cerrar la fase.

### CP-007 — Ninguna entrada copia el texto de su regla

| Campo | Valor |
|---|---|
| **HU y CA** | HU-010, RNF-02 |
| **Tipo** | Funcional, mantenimiento |
| **Prioridad** | Media |
| **Precondiciones** | El glosario tiene sus entradas con su regla |
| **Datos de entrada** | El glosario entero |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir, por cada entrada, la regla que nombra | Queda a la vista el texto de la regla junto al de la entrada |
| 2 | Comparar renglón contra renglón | Ninguna frase de la regla aparece igual en la entrada |
| 3 | Comprobar que la entrada dice qué es el término, no qué exige la regla | La entrada define; la regla exige. Son dos cosas distintas |
| 4 | Cambiar mentalmente el texto de una regla y ver si la entrada quedaría falsa | No queda falsa: la entrada define el término, que es lo que no cambia |

**Resultado esperado final:** el glosario no es una segunda copia de las reglas y no se puede desincronizar.
**Postcondiciones:** la entrada que copie se reescribe.

### CP-008 — Queda la lista de lo que falta traducir

| Campo | Valor |
|---|---|
| **HU y CA** | HU-010, CA-03 |
| **Tipo** | Funcional |
| **Prioridad** | Media |
| **Precondiciones** | El glosario está completo |
| **Datos de entrada** | El glosario entero, y los nombres de los roles que hoy están en inglés |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Anotar, recorriendo el glosario, los términos que no están en español | Queda una lista |
| 2 | Leer la justificación de cada uno | Cada uno dice por qué no tiene traducción usada, o queda marcado como pendiente de traducir |
| 3 | Contrastar la lista contra los nombres de los roles en `skills/`, `base/00-identidad-y-rol/reglas/ID6…` y `plantillas/ciclo-vida-proyectos/10-estado-fase.md` | Se ve cuáles hay que cambiar y en qué archivos |
| 4 | Comprobar que la tabla dice que renombrar es trabajo aparte | Lo dice, y la fase no lo hace |

**Resultado esperado final:** la lista de lo que falta traducir queda escrita, con dónde vive cada uno.
**Postcondiciones:** la lista alimenta la HU que renombre los roles, que no es esta.

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Definición acá | Atención |
|---|---|---|
| Crítica | Falta un término que el estándar usa a diario, o el glosario contradice a la regla que cita | Antes de cerrar la fase, sin excepción |
| Alta | Una entrada enlaza a una regla que no exige lo que dice, o el enlace no llega | Dentro de la fase |
| Media | Una definición hay que preguntarla para entenderla | Dentro de la fase |
| Baja | Redacción, orden dentro de un grupo | Antes de cerrar la fase |

### 9.2 Flujo del defecto

Nuevo, en corrección, listo para revisar, verificado, cerrado. Si al verificar sigue fallando, vuelve a en corrección.

### 9.3 Contenido mínimo de un reporte

- Identificador y título.
- Severidad.
- Qué caso de prueba lo destapó.
- Qué entrada del glosario falla y qué se esperaba de ella.
- El término con el que se reprodujo.

### 9.4 Registro

| ID | Título | Caso | Severidad | Estado |
|---|---|---|---|---|
| Ninguno todavía | | | | |

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de criterios | Criterios con caso sobre criterios totales | 100% |
| Casos ejecutados | Ejecutados sobre diseñados | 100%, porque son ocho |
| Términos del estándar que faltan en el glosario | Conteo en CP-001 | Cero |
| Términos del glosario que el estándar no usa | Conteo en CP-001 y CP-003 | Cero |
| Preguntas que tuvo que hacer quien leyó | Conteo en CP-006 | Cero |
| Enlaces rotos | Salida de `validadores/enlaces.py` | Cero |

### 12.2 Resumen de ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos |
|---|---:|---:|---:|---:|
| 1 | 8 | 0 | 0 | 0 |

### 12.3 Concepto final

Pendiente. Se llena al terminar la ejecución.

## 14. Control de versiones

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0 | 2026-08-14 | Ing. José Dúmar Jiménez Ruíz | Versión inicial, junto con el plan de trabajo |
| 1.2 | 2026-08-15 | Ing. José Dúmar Jiménez Ruíz | Cada caso arranca desde cero: se agregó el paso de partida donde faltaba. CP-004 gana "elegir tres entradas de tres grupos distintos" y CP-006 gana «conseguir a alguien que no haya participado en escribir el glosario». Estaban dados por supuestos, y en CP-006 ese supuesto era justo lo que bloqueaba el caso. Lo exige [plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md](../../../../../plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md), §2: se arranca desde cero |
| 1.1 | 2026-08-15 | Ing. José Dúmar Jiménez Ruíz | Se partieron los pasos que traían dos acciones en una fila. El de CP-001 —"tomar la lista de T-01 **y** contar cuántos términos tiene"— fue el que se vio primero: al ejecutar quedó anotado el conteo y se perdió de dónde salió la lista. Igual en CP-002 (3), CP-004 (1), CP-005 (3 y 4), CP-007 (1) y CP-008 (1). CP-001 pasa de 3 pasos a 4, CP-005 de 4 a 6 y CP-007 de 3 a 4. Ningún caso cambia lo que comprueba. Lo exige ahora [plantillas/ciclo-vida-proyectos/08-plan-pruebas.md](../../../../../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md), §6: un paso, una acción |
