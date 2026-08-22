# Plan de Trabajo — Fase A-EP-001-HU-002-capas-y-precedencia

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en [HU-002](../HU-002-capas-y-precedencia.md); el detalle de las pruebas, en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase; lo que dieron al correrlas, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-001-HU-002-capas-y-precedencia` |
| **Épica** | [EP-001](../../epica.md) |
| **HU** | [HU-002 Capas de reglas y orden de precedencia](../HU-002-capas-y-precedencia.md) |
| **Módulo** | Cuerpo de reglas |
| **Especificación del módulo** | No hay especificación aparte. El entregable es texto normativo, no código, y su especificación son los criterios de aceptación de la HU. Igual que en la fase A de HU-001, y sujeto a la misma respuesta del usuario |
| **Fecha apertura** | 2026-08-14 |
| **Rama** | `feature/A-EP-001-HU-002-capas-y-precedencia` |

**ORIGEN** — ✨ **Funcionalidad nueva** (`DOC12`). Existe el molde de regla que dejó la fase A de HU-001, pero no existe la separación en capas ni el orden que desempata cuando dos reglas dicen cosas distintas.

**Por qué una sola fase para los tres CA.** Los tres se prueban provocando el mismo choque desde tres lados: el ajuste que sí manda, el ajuste que no puede mandar y la instrucción del chat que tampoco. Ninguno se puede probar sin el orden de precedencia escrito, que es un solo documento. Partirlos daría fases que existen solo para cumplir la nomenclatura, que es justo lo que prohíbe `02·F12.10`.

**CA de la HU que cubre esta fase**

| CA de HU-002 | Qué valida | Estado |
|---|---|---|
| CA-01 | Una regla del proyecto ajusta una convención y manda | Pendiente |
| CA-02 | Un intento de aflojar la capa protegida no procede | Pendiente |
| CA-03 | Una instrucción del chat no cambia el orden | Pendiente |

## 1. Objetivo y alcance

**Objetivo.** Dejar escrito en cuántas capas se reparten las reglas, qué va en cada una, cómo se ve la capa de una regla al abrirla, y cuál gana cuando dos se contradicen.

**Resumen de CA a cubrir**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Camino feliz: el ajuste declarado del proyecto manda sobre la convención | Funcional | Media |
| CA-02 | La excepción escrita contra una regla protegida no aplica | Funcional | Media |
| CA-03 | La instrucción del chat no mueve la precedencia | Funcional | Baja |
| Transversal, límites | Dos reglas de la misma capa se contradicen | Funcional | Media |
| Transversal, no regresión | Las reglas ya escritas conservan su marca de capa | Funcional | Baja |
| RNF-01 | La capa se ve al abrir la regla, sin ir a otro documento | No funcional | Baja |

**Fuera de alcance**

- El contenido de la capa protegida. Acá se define la capa y su marca, no las reglas que van adentro. Eso es HU-003.
- El contenido de las convenciones ajustables. Eso es HU-005.
- El mecanismo por el que un proyecto declara su capa propia y dónde vive. Eso es HU-006. Acá solo se nombra en el orden de precedencia, porque sin nombrarla el orden queda incompleto.
- Que un programa compruebe la marca de capa. Es de EP-004. Esta fase solo deja marcado qué parte es comprobable.
- El registro de que una regla cambió de capa. Es EP-002, versionado.

## 2. Análisis previo

### 2.1 Archivos que se crean o modifican

| Archivo | Tipo | Qué es |
|---|---|---|
| `base/README.md` | Modificado | Gana la tabla de las clases de capítulo, con qué puede tocar un proyecto en cada una |
| `base/20-meta-reglas/reglas/M6-ante-un-conflicto-el-desempate-es-este-y-en-este-orden.md` | Nuevo | La regla que fija el orden de desempate completo |
| `base/20-meta-reglas/estructura-regla.md` | Modificado | La marca de capa entra al molde como parte obligatoria |
| `base/20-meta-reglas/base.md` | Modificado | El capítulo declara su clase en el encabezado, y su índice suma `M6` |
| `base/00-nucleo-blindado.md` | Nuevo | El capítulo de la capa protegida, con su marca y la frase de que no se sobrescribe. Sin reglas adentro: esas son de HU-003 |
| `base/00-identidad-y-rol/base.md` | Modificado | Declara su clase en el encabezado |

La marca de capa se aplica a los capítulos que existan al momento de esta fase. Los capítulos que nazcan después la traen puesta desde el molde, no como un repaso posterior.

### 2.2 Matriz de dependencias del refactor

| Lo que se toca | Qué depende de eso hoy | Qué se rompe si cambia |
|---|---|---|
| `estructura-regla.md`, al sumarle la marca de capa | Las dos reglas escritas en la fase A de HU-001, `M4` y `M5` | Quedarían incompletas contra su propio molde. Se les pone la marca dentro de esta misma fase, en T-10 |
| `base/README.md` | Nada todavía. Es un índice recién creado | Nada |

### 2.3 Rutas y control de acceso

No aplica porque el entregable son archivos de texto del repositorio. No hay sistema con usuarios ni endpoints.

### 2.4 Punto de entrada en la interfaz

No aplica porque la fase no introduce interfaz. El entregable se lee abriendo los archivos.

### 2.5 Permisos o roles a sembrar

Ninguno. El control de quién edita lo da el acceso al repositorio.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| La capa se declara en el capítulo, y la regla la hereda | Escribir la capa en cada regla, una por una | Con la capa repetida en cada regla hay dos fuentes para el mismo dato, y tarde o temprano dicen cosas distintas |
| La regla que puede tocar una capa distinta a la de su capítulo lleva su propia marca, y esa gana | Prohibir que una regla se salga de la capa de su capítulo | Hay reglas de seguridad dentro de capítulos ajustables. Prohibirlo obligaría a partir capítulos por motivo equivocado |
| El desempate se escribe como una lista numerada de pasos, no como prosa | Explicar en un párrafo cuál gana | Un choque se resuelve leyendo de arriba abajo y parando en el primer paso que aplica. En prosa hay que interpretar, y ahí es donde se cuela la decisión del agente |
| El último paso del desempate es pausar y reportar, no elegir | Dejar una regla de última instancia que siempre resuelva | Si el estándar no resuelve un choque, eso es un defecto del estándar. Taparlo con una regla comodín lo vuelve invisible |
| La instrucción del chat no entra en el orden de capas | Ponerla como la capa de más abajo | Ponerla en el orden la vuelve negociable: bastaría con estar por encima de algo. Queda escrito que no participa |
| La capa propia del proyecto solo gana si el proyecto la declaró como ajuste explícito | Que gane siempre que exista | El silencio no es una decisión. Sin declaración explícita no hay a quién atribuirle el ajuste |

Estas decisiones se registran como señal cuando exista la memoria (EP-006). Mientras tanto quedan acá.

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | Si el preámbulo es una capa más o queda fuera del orden de capas, porque no exige nada: dice quién es el agente y cómo funcionan las reglas | Usuario | **Resuelta** el 2026-08-22 mirando lo que ya está construido, no decidiendo de nuevo: queda **fuera del orden de capas**. El README lo lista como preámbulo y no como capa, y la razón es la que la duda misma da: no exige nada, dice quién es el agente |
| 2 | Cuántas capas hay en total, contando la del proyecto que todavía no existe, y cómo se nombran | Usuario | **Resuelta** el 2026-08-22 mirando lo que ya está construido, no decidiendo de nuevo: **tres**, y así las nombra el README: núcleo blindado, convenciones base y capa de proyecto. La del proyecto ya existe: son las plantillas que se copian |
| 3 | Si una convención puede marcarse como opcional dentro de su capa, o si eso es una capa aparte | Usuario | **Resuelta** el 2026-08-22 mirando lo que ya está construido, no decidiendo de nuevo: **sí, dentro de su capa**. Los capítulos `15`, `18`, `19`, `21` y `22` están marcados *opt-in* y siguen siendo capa 2 |

Ninguna tarea de construcción arranca con una duda abierta que la bloquee. Las tres bloquean T-02 en adelante.

## 3. Desglose de tareas por criterio de aceptación

Sin columna de estado, a propósito: este plan se aprueba y no se vuelve a tocar. El avance en vivo va en [estado-fase.md](estado-fase.md) §1.2, y la verificación de qué se hizo, en el documento de cierre §2.2.

### CA-01 — Una regla del proyecto ajusta una convención

| ID | Tarea | Est. | Depende de | Evidencia |
|---|---|:--:|---|---|
| T-01 | Resolver las tres dudas de §2.7 con el usuario | 1 h | — | EV-01 |
| T-02 | Escribir la tabla de clases de capítulo: cuáles hay, qué significa cada una y qué puede tocar un proyecto | 2 h | T-01 | EV-02 |
| T-03 | Escribir el paso del desempate que le da la capa del proyecto sobre la convención, con la condición de que el ajuste esté declarado | 2 h | T-02 | EV-03 |
| T-04 | Escribir con qué forma el proyecto nombra la convención que está ajustando | 1 h | T-03 | EV-03 |

### CA-02 — Un intento de aflojar la capa protegida no procede

| ID | Tarea | Est. | Depende de | Evidencia |
|---|---|:--:|---|---|
| T-05 | Escribir el primer paso del desempate: si una regla está marcada como protegida, gana y no hay paso siguiente | 1 h | T-02 | EV-03 |
| T-06 | Crear el capítulo de la capa protegida con su marca y la frase de que ninguna capa la desactiva | 2 h | T-02 | EV-04 |
| T-07 | Escribir a propósito, en un proyecto de prueba, una excepción a una regla protegida y comprobar qué gana | 1 h | T-05, T-06 | EV-05 |

### CA-03 — Una instrucción del chat no cambia el orden

| ID | Tarea | Est. | Depende de | Evidencia |
|---|---|:--:|---|---|
| T-08 | Escribir que una instrucción puntual no participa del orden de precedencia, y qué se hace cuando contradice una regla | 2 h | T-05 | EV-03 |
| T-09 | Probarlo en una sesión real, insistiendo una segunda vez | 1 h | T-08 | EV-06 |

### Criterios transversales

| ID | Tarea | Est. | Depende de | Evidencia |
|---|---|:--:|---|---|
| T-10 | Sumarle al molde la marca de capa como parte obligatoria y ponérsela a las reglas ya escritas | 2 h | T-02 | EV-07 |
| T-11 | Escribir los pasos del desempate para dos reglas de la misma capa: la más específica, la más restrictiva, y pausar si sigue empatado | 2 h | T-05 | EV-03 |

### Requisitos no funcionales

| ID | Tarea | Categoría | Est. | Evidencia |
|---|---|---|:--:|---|
| T-12 | Comprobar que la capa de una regla se ve al abrirla, sin abrir otro documento | Claridad | 1 h | EV-08 |
| T-13 | Marcar en el molde qué parte de la marca de capa puede comprobar un programa | Comprobabilidad | 1 h | EV-07 |

**Total estimado:** 19 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03, T-05, T-06, T-08.

**En paralelo:** T-10 y T-11 pueden avanzar apenas exista la tabla de clases en T-02. T-07, T-09 y T-12 se hacen al final, sobre lo escrito.

Solo se tocan los archivos declarados en §2.1. Si aparece uno nuevo, se pausa, se reporta y se amplía el plan con visto bueno. No se edita por iniciativa.

## 5. Verificación de criterios de aceptación

| CA | Método de verificación | Evidencia | Estado |
|---|---|---|---|
| CA-01 | Se declara un ajuste en un proyecto de prueba y se comprueba cuál forma manda | EV-03, EV-05 | Pendiente |
| CA-02 | Se escribe una excepción contra una regla protegida y se comprueba que no aplica | EV-05 | Pendiente |
| CA-03 | Se da la instrucción en el chat, dos veces, y se compara la respuesta | EV-06 | Pendiente |
| Transversal, límites | Se provoca un choque entre dos reglas de la misma capa | EV-03 | Pendiente |
| Transversal, no regresión | Se revisan las reglas ya escritas y su marca de capa | EV-07 | Pendiente |
| RNF-01 | Se abre una regla cualquiera y se busca su capa sin salir del archivo | EV-08 | Pendiente |

**Registro de evidencias**

| ID | Tipo | Dónde queda |
|---|---|---|
| EV-01 | Respuestas del usuario a las tres dudas | En este plan, §2.7 actualizado |
| EV-02 | La tabla de clases de capítulo | `base/README.md` |
| EV-03 | La regla del desempate, con sus pasos | `base/20-meta-reglas/reglas/M6-...md` |
| EV-04 | El capítulo de la capa protegida | `base/00-nucleo-blindado.md` |
| EV-05 | El ajuste y la excepción del proyecto de prueba, con lo que ganó cada vez | Anotado en el cierre de la fase |
| EV-06 | La sesión donde se dio la instrucción y la respuesta que dio | Anotado en el cierre de la fase |
| EV-07 | La marca de capa en el molde y en las reglas ya escritas | `base/20-meta-reglas/` |
| EV-08 | Resultado de la revisión de claridad | Anotado en el cierre de la fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | El repositorio del estándar, en una rama aparte, más un proyecto de prueba que solo tiene su capa propia escrita a mano |
| Usuarios de prueba | No aplica porque no hay sistema con usuarios |
| Datos precargados | No aplica. La prueba se hace sobre los propios documentos y sobre una sesión real |

El detalle de casos va en el `plan_pruebas` de esta misma fase.

## 7. Reversión

Casi todo lo de esta fase son archivos nuevos en una rama aparte: se descarta la rama y no queda nada que deshacer. Lo único que se modifica sobre algo existente es el molde de regla, y ese cambio es aditivo: agrega una parte, no le quita ninguna. Si el molde con marca de capa no sirve, se quita la parte y las reglas escritas siguen siendo válidas.

## 8. Producción y migración

No aplica porque nada de esto está en producción todavía. No hay proyecto que haya adoptado el estándar.

## 9. Reglas aplicadas

| Regla | Cómo se aplica acá |
|---|---|
| [`20·M4`](../../../../../base/20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md) | La regla nueva del desempate toma un identificador libre del capítulo, y no se renumera nada |
| [`20·M5`](../../../../../base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md) | La regla del desempate se escribe con el molde que dejó la fase A de HU-001 |
| [`02·F12.9`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md) | La fase cubre los tres criterios juntos porque no se pueden delimitar por separado |

Es la primera fase que puede citar reglas del estándar: las que escribió la fase anterior.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Las tres dudas de §2.7 sin resolver | Bloquea T-02 en adelante, que es casi toda la fase | Resolverlas con el usuario en T-01, antes de escribir nada | Abierto |
| R-01 | Que la capa protegida crezca hasta volverlo todo rígido | Se descubriría tarde, cuando ya nadie pueda ajustar nada | Escribir en esta fase el criterio de qué merece estar ahí: solo lo que no se puede deshacer | Abierto |
| R-02 | Que la precedencia quede escrita y nadie la aplique | El documento existe pero los choques se siguen resolviendo a criterio | El paso final del desempate obliga a pausar y reportar, así que un choque sin resolver se ve | Abierto |
| R-03 | Que la marca de capa quede en dos lugares, el capítulo y la regla, y digan cosas distintas | Alto: la marca deja de ser confiable | La decisión de §2.6 fija cuál manda: la del capítulo, salvo que la regla traiga la suya | Abierto |
| R-04 | Que el orden de precedencia nombre una capa de proyecto que todavía no existe, y quede colgando hasta HU-006 | Medio: el orden se lee incompleto | Se nombra la capa y se declara expresamente que su mecanismo es HU-006, para que no se lea como olvido | Abierto |

## 11. Definition of Done

- [ ] Los tres CA de §0 verificados con su evidencia
- [ ] Los dos criterios transversales verificados
- [ ] La tabla de clases de capítulo escrita, con qué puede tocar un proyecto en cada una
- [ ] El orden de desempate escrito paso a paso, con su ejemplo de choque
- [ ] El capítulo de la capa protegida creado y marcado
- [ ] Las reglas ya escritas conservan o ganan su marca de capa
- [ ] La instrucción del chat no logra aflojar una regla protegida en ningún intento
- [ ] Las decisiones de §2.6 quedan escritas donde se puedan recuperar después
- [ ] Rama lista para el commit único de la fase
- [ ] Aprobada por el usuario

## 12. Cierre

No se escribe acá. El cierre de la fase vive en el `funcionalidad_implementada.md`: qué se hizo de cada tarea, qué se probó, qué se decidió y qué deuda quedó. Este plan se queda como se aprobó, para poder comparar lo que se dijo contra lo que pasó.