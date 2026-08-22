# Plan de Trabajo — Fase A-EP-003-HU-010-glosario-de-la-terminologia

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en [documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/HU-010-glosario-de-la-terminologia.md](../HU-010-glosario-de-la-terminologia.md); el detalle de las pruebas, en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase; lo que den al correrlas, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-003-HU-010-glosario-de-la-terminologia` |
| **Épica** | [documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/epica.md](../../epica.md) |
| **HU** | [documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/HU-010-glosario-de-la-terminologia.md](../HU-010-glosario-de-la-terminologia.md) |
| **Módulo** | Documentos modelo |
| **Especificación del módulo** | [documentacion/documentos-modelo/spec.md](../../../../documentos-modelo/spec.md). Existe y crece por incrementos; esta fase le agrega el suyo (`02·F2`) |
| **Fecha apertura** | 2026-08-14 |
| **Rama** | `main`, la que está abierta. Si el usuario prefiere rama aparte, se abre `feature/A-EP-003-HU-010-glosario-de-la-terminologia` antes de T-01 |

**Origen:** funcionalidad nueva. Nace del hallazgo H-8 del 2026-08-14, [historico-chat/resumenes/2026-08-14/hu-de-la-comprobacion-automatica.md](../../../../../historico-chat/resumenes/2026-08-14/hu-de-la-comprobacion-automatica.md), y su pendiente es el [pendientes/hecho/los-nombres-de-rol-en-espanol.md](../../../../../pendientes/hecho/los-nombres-de-rol-en-espanol.md).

**Por qué una sola fase para los tres criterios.** Los tres se validan sobre el mismo documento, el glosario, y ninguno se puede probar sin él. Partirlos daría fases que existen solo para cumplir la nomenclatura, que es lo que prohíbe `02·F12.10`.

**CA de la HU que cubre esta fase**

| CA de HU-010 | Qué valida | Estado |
|---|---|---|
| [CA-01](../HU-010-glosario-de-la-terminologia.md#ca-01--cada-término-está-definido-en-una-línea) | Cada término está definido en una línea | Pendiente |
| [CA-02](../HU-010-glosario-de-la-terminologia.md#ca-02--cada-entrada-dice-dónde-vive-y-qué-regla-lo-manda) | Cada entrada dice dónde vive y qué regla lo manda | Pendiente |
| [CA-03](../HU-010-glosario-de-la-terminologia.md#ca-03--se-ve-qué-quedó-en-otro-idioma) | Se ve qué quedó en otro idioma | Pendiente |

## 1. Objetivo y alcance

**Objetivo.** Dejar escrito el glosario de la terminología del estándar, enlazado desde donde se entra a leerlo, y con la lista de los términos que siguen en otro idioma.

**Resumen de CA a cubrir**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Camino feliz: se busca un término y está, en una línea | Funcional | Media |
| CA-02 | La entrada lleva al detalle en un paso | Funcional | Media |
| CA-03 | Queda la lista de lo que falta traducir | Funcional | Baja |
| RNF-01 | Cada definición se entiende sin saber del tema | No funcional | Media |
| RNF-02 | El glosario enlaza a la regla dueña, no copia su texto | No funcional | Baja |

**Fuera de alcance**

- **Renombrar los roles.** Lo dice la propia HU en §3.3. Esta fase deja la lista de qué está en inglés; cambiarlo es trabajo aparte, con su HU, porque toca diez archivos de `skills/`, `base/` y `plantillas/` y rompe citas.
- **Definir términos del dominio de un proyecto.** Eso va en su capa 3.
- **El programa que comprueba el glosario.** Es de EP-004.
- **Reescribir las reglas** para que usen el término del glosario. Acá se define, no se corrige lo escrito.

## 2. Análisis previo

Todo lo de esta sección se verificó contra el repositorio el 2026-08-14.

### 2.1 Archivos que se crean o modifican

| Archivo | Tipo | Qué es |
|---|---|---|
| [base/glosario.md](../../../../../base/glosario.md) | Nuevo | El glosario: cada término en una línea, con quién lo escribe, dónde vive y qué regla lo manda |
| [base/README.md](../../../../../base/README.md) | Modificar | Enlazarlo. Es la puerta de entrada a `base/`, la carpeta que heredan los proyectos |
| [README.md](../../../../../README.md) | Modificar | Enlazarlo. Es la puerta de entrada al repositorio, y su §"capítulos" ya lista lo que hay en `base/` |
| [anatomia/mapa-del-sitio.md](../../../../../anatomia/mapa-del-sitio.md) | Modificar | El árbol de §2 y el conteo de `base/`. Lo exige su propia tabla de mantenimiento, fila "agrega un archivo de `base/`" |
| [documentacion/documentos-modelo/spec.md](../../../../documentos-modelo/spec.md) | Modificar | Sumarle el incremento de HU-010, como ya hicieron HU-001 y HU-009 |
| [CHANGELOG.md](../../../../../CHANGELOG.md) | Modificar | Entrada 15.3.0 (`20·M10`) |
| [VERSION](../../../../../VERSION) | Modificar | De 15.2.0 a 15.3.0 |
| [documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/HU-010-glosario-de-la-terminologia.md](../HU-010-glosario-de-la-terminologia.md) | Modificar | §8, que hoy dice "Todavía no se descompuso en fases", y §13 bitácora |
| [documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-010-glosario-de-la-terminologia/README.md](../README.md) | Modificar | Listar la fase, que hoy dice "Todavía no tiene fases" |
| [resultado_pruebas.md](resultado_pruebas.md) | Nuevo | Qué se ejecutó y con qué resultado |
| [funcionalidad_implementada.md](funcionalidad_implementada.md) | Nuevo | El cierre de la fase |
| [estado-fase.md](estado-fase.md) | Nuevo | En qué estación va |
| [README.md](README.md) | Nuevo | El índice de esta carpeta (`13·DOC17`) |

### 2.2 Matriz de dependencias del refactor

No aplica. El glosario es un documento nuevo que no le cambia el contrato a nada: ninguna regla se edita, ningún identificador se mueve y ninguna cita existente deja de resolver. Los cuatro archivos que se modifican solo reciben un enlace más.

### 2.3 Rutas y control de acceso

No aplica. El entregable son archivos de texto del repositorio. No hay sistema con usuarios ni endpoints.

### 2.4 Punto de entrada

El glosario se entra por tres puertas, y por eso las tres se tocan en §2.1: [README.md](../../../../../README.md) de la raíz para quien llega al repositorio, [base/README.md](../../../../../base/README.md) para quien llega a las reglas, y [anatomia/mapa-del-sitio.md](../../../../../anatomia/mapa-del-sitio.md) para quien busca dónde está cada cosa. Un glosario que no se enlaza desde donde se entra no lo encuentra nadie, y el CA-01 se cumpliría en el papel.

### 2.5 Permisos o roles a sembrar

Ninguno. El control de quién edita lo da el acceso al repositorio.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| El glosario vive en `base/glosario.md` | `documentacion/glosario.md` | `base/` es lo que heredan los proyectos (`00·M13`). Un proyecto que recibe las reglas y no la explicación de sus palabras recibe media cosa |
| Sin número de capítulo, al lado de `base/README.md` | Numerarlo como capítulo 21 | No es un capítulo de reglas: es un anexo, como [`base/00-identidad-y-rol/marcadores-de-ia.md`](../../../../../base/00-identidad-y-rol/marcadores-de-ia.md). Numerarlo lo cargaría en cada sesión sin que exija nada |
| Sin checklist del estándar | Aplicarle el checklist como a una regla | El checklist evalúa reglas y el glosario no exige nada. Lo dice el límite del pendiente 21 |
| Los términos se agrupan en cuatro: la cadena de trabajo, las reglas, lo que comprueba y lo que se guarda | Una sola lista alfabética | La lista alfabética sirve para buscar lo que ya se sabe cómo se llama. Los grupos sirven para entrar sin saber nada, que es el lector de la narrativa de la HU. Cada grupo lleva su lista alfabética adentro |
| Cada entrada define en una línea y enlaza a la regla dueña | Copiar el texto de la regla en la entrada | Dos copias se desincronizan (`20·M5`). Lo pide además el RNF de mantenimiento de la HU |
| El término que sigue en otro idioma queda marcado dentro de su propia entrada, y el cierre del glosario los recoge en una tabla | Una lista aparte, fuera del glosario | Fuera del glosario se desactualiza sola. Dentro, quien edita la entrada ve la marca |
| La versión sube a 15.3.0 (MENOR) | MAYOR | Es aditivo: nadie tiene que hacer nada nuevo para cumplir. Nace un documento y tres índices lo enlazan (`20·M10`) |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | A quién se consulta | Estado |
|---|---|---|---|
| 1 | Si el glosario va en `base/` (viaja a los proyectos que heredan) o en `documentacion/` (se queda en el estándar) | Usuario | Propuesta en §2.6: `base/`. Se cierra al aprobar este plan |
| 2 | Si se trabaja sobre `main` o se abre rama de la fase | Usuario | Se cierra al aprobar este plan |

Ninguna bloquea la escritura del contenido: las dos deciden dónde se guarda, no qué dice. Se responden aprobando el plan.

## 3. Desglose de tareas por criterio de aceptación

Sin columna de estado, a propósito: este plan se aprueba y no se vuelve a tocar. El avance en vivo va en [estado-fase.md](estado-fase.md) §1.2, y la verificación de qué se hizo, en el documento de cierre §2.2.

### CA-01 — Cada término está definido en una línea

| ID | Tarea | Est. | Depende de | Evidencia |
|---|---|:--:|---|---|
| T-01 | Recorrer `base/`, `plantillas/` y `skills/` y listar los términos que aparecen, agrupados en los cuatro grupos de §2.6 | 2 h | — | EV-01 |
| T-02 | Descartar los que no aparecen en ninguna regla ni plantilla, que no son del estándar (RN-05 de la HU) | 1 h | T-01 | EV-01 |
| T-03 | Escribir la definición de cada término en una línea, en palabras de todos los días | 3 h | T-02 | EV-02 |
| T-04 | Armar el documento con su encabezado, sus cuatro grupos y su orden alfabético dentro de cada grupo | 1 h | T-03 | EV-02 |

### CA-02 — Cada entrada dice dónde vive y qué regla lo manda

| ID | Tarea | Est. | Depende de | Evidencia |
|---|---|:--:|---|---|
| T-05 | Agregarle a cada entrada quién lo escribe, dónde vive y qué regla lo manda, con el enlace resuelto (`13·DOC14`, `20·M15`) | 2 h | T-04 | EV-02 |
| T-06 | Enlazar el glosario desde las tres puertas de entrada de §2.4 | 1 h | T-04 | EV-03 |
| T-07 | Seguir uno por uno los enlaces del glosario y comprobar que ninguno queda roto | 1 h | T-05, T-06 | EV-04 |

### CA-03 — Se ve qué quedó en otro idioma

| ID | Tarea | Est. | Depende de | Evidencia |
|---|---|:--:|---|---|
| T-08 | Marcar dentro de su entrada cada término que sigue en otro idioma, con por qué no tiene traducción usada (`01·C20`) | 1 h | T-05 | EV-02 |
| T-09 | Cerrar el glosario con la tabla de lo que falta traducir, contrastada contra los nombres de los roles de `skills/`, `base/00-identidad-y-rol/reglas/ID6…` y `plantillas/ciclo-vida-proyectos/10-estado-fase.md` | 1 h | T-08 | EV-05 |

### Requisitos no funcionales

| ID | Tarea | Categoría | Est. | Evidencia |
|---|---|---|:--:|---|
| T-10 | Releer el glosario entero contra la exigencia de que lo entienda quien no sabe del tema (`00·ID7`) y contra la lista de marcadores (`00·ID8`) | Legibilidad | 1 h | EV-06 |
| T-11 | Comprobar que ninguna entrada copia el texto de su regla | Mantenimiento | 1 h | EV-06 |

### Cierre de la fase

| ID | Tarea | Est. | Depende de | Evidencia |
|---|---|:--:|---|---|
| T-12 | Sumarle el incremento de HU-010 a la especificación del módulo | 1 h | T-09 | EV-07 |
| T-13 | Escribir la entrada 15.3.0 del registro de cambios y subir `VERSION` | 1 h | T-12 | EV-07 |
| T-14 | Actualizar §8 y la bitácora de la HU, su README, el árbol del mapa del sitio y el `funcionalidad_implementada.md` | 1 h | T-13 | EV-07 |
| T-15 | Cerrar el pendiente 21 en su parte del glosario, dejando abierta la parte de los roles | 1 h | T-14 | EV-07 |

**Total estimado:** 19 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03, T-04, T-05, T-07, luego el cierre T-12 a T-15.

**En paralelo:** T-06 puede arrancar apenas exista el archivo en T-04. T-08 y T-09 avanzan sobre las entradas ya escritas, sin esperar a que estén todas. T-10 y T-11 se hacen al final, sobre lo escrito.

Solo se tocan los archivos declarados en §2.1 (`02·F8`). Si aparece uno nuevo, se pausa, se reporta y se amplía el plan con el visto bueno. No se edita por iniciativa.

## 5. Verificación de criterios de aceptación

| CA | Método de verificación | Evidencia | Estado |
|---|---|---|---|
| CA-01 | Se toman cinco términos de capítulos distintos y se buscan en el glosario | EV-02, EV-08 | Pendiente |
| CA-02 | Se toman tres entradas y se sigue lo que dicen: la regla existe y el documento está donde dice | EV-04 | Pendiente |
| CA-03 | Se recorre el glosario entero y se lista lo que no está en español, contra los nombres de los roles | EV-05 | Pendiente |
| RNF-01 | Relectura contra `00·ID7` y `00·ID8` | EV-06 | Pendiente |
| RNF-02 | Revisión entrada por entrada buscando texto copiado de la regla | EV-06 | Pendiente |

**Registro de evidencias**

| ID | Tipo | Dónde queda |
|---|---|---|
| EV-01 | La lista de términos por grupo, antes de definirlos | En el `resultado_pruebas.md`, caso CP-001 |
| EV-02 | El glosario escrito | [base/glosario.md](../../../../../base/glosario.md) |
| EV-03 | Los tres enlaces desde las puertas de entrada | `README.md`, `base/README.md`, `anatomia/mapa-del-sitio.md` |
| EV-04 | El recorrido de enlaces, uno por uno | En el `resultado_pruebas.md`, caso CP-004 |
| EV-05 | La tabla de lo que falta traducir | Cierre de [base/glosario.md](../../../../../base/glosario.md) |
| EV-06 | Resultado de las dos relecturas | En el `resultado_pruebas.md`, casos CP-006 y CP-007 |
| EV-07 | Los documentos de cierre al día | Especificación del módulo, registro de cambios, HU y mapa del sitio |
| EV-08 | Los cinco términos buscados y encontrados | En el `resultado_pruebas.md`, caso CP-002 |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | El repositorio del estándar. No hay base de datos ni datos reales |
| Usuarios de prueba | No aplica porque no hay sistema con usuarios. La prueba de lectura de CP-006 la hace el usuario |
| Datos precargados | No aplica. La prueba se hace sobre los propios documentos |

El detalle de casos va en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase.

## 7. Reversión

Un archivo nuevo y cuatro enlaces agregados. Si el glosario no sirve, se borra `base/glosario.md`, se quitan los tres enlaces y se revierte la entrada del registro de cambios con `VERSION`. Nada se sobrescribe y ninguna regla se edita, así que no hay nada que reconstruir.

## 8. Producción y migración

No aplica en el sentido de datos. Lo que sí viaja: `base/` llega a cada proyecto que hereda el estándar, así que el archivo nuevo aparece en todos en su próxima sesión. Es aditivo y no obliga a nadie a hacer nada, por eso la versión sube MENOR.

**Cruce con el hallazgo H-9.** Si hay otra sesión abierta versionando al mismo tiempo, el número 15.3.0 puede chocar. Antes de T-13 se relee `VERSION` y se toma el siguiente libre.

## 9. Reglas aplicadas

- **Base:** [`00·ID7`](../../../../../base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md) y [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) (cómo se escribe) · [`01·C8`](../../../../../base/01-conducta.md#c8--habla-el-idioma-del-proyecto) y [`01·C20`](../../../../../base/01-conducta.md#c20--la-palabra-de-otro-idioma-se-traduce-y-si-no-se-puede-se-explica) (el idioma y el término que no lo tiene, que es lo que dispara la fase) · [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md) (solo los archivos del plan) · [`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md) y `F12.13` (nombre y ruta de la fase) · [`13·DOC14`](../../../../../base/13-documentacion/reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md) (los enlaces) · [`13·DOC17`](../../../../../base/13-documentacion/reglas/DOC17-manten-un-readme-en-cada-nivel-del-arbol-de-trabajo.md) (README de la carpeta) · [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md) (versionar) · [`20·M13`](../../../../../base/20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md) (dónde va lo que no es regla) · [`20·M15`](../../../../../base/20-meta-reglas/reglas/M15-toda-cita-a-otra-regla-lleva-su-enlace.md) (toda cita con su enlace).
- **Proyecto:** el `CLAUDE.md` de este repositorio, §2 y §3.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Las dos dudas de §2.7 sin responder | Bajo: no bloquean el contenido, solo dónde se guarda | Se cierran aprobando este plan | Abierto |
| R-01 | Que el glosario se llene de términos que nadie usa | Se vuelve una lista que nadie lee | T-02 descarta lo que no aparece en ninguna regla ni plantilla | Abierto |
| R-02 | Que las entradas copien el texto de la regla y se desincronicen | Alto: dos versiones de la misma norma, y manda la que nadie mira | Definir en una línea y enlazar. T-11 lo revisa entrada por entrada | Abierto |
| R-03 | Que la lista de lo que falta traducir se lea como una orden de renombrar ya | Se mete en la fase un trabajo que rompe diez archivos y sus citas | El glosario dice explícitamente que la lista es inventario, y que el cambio es trabajo aparte con su HU | Abierto |
| R-04 | Choque de número de versión con otra sesión abierta (H-9) | Dos numeraciones vivas | Releer `VERSION` justo antes de T-13 | Abierto |

## 11. Definition of Done

- [ ] Los tres CA de §0 verificados con su evidencia
- [ ] El glosario existe con los términos de los cuatro grupos
- [ ] Cada entrada dice dónde vive y qué regla lo manda, y el enlace resuelve
- [ ] Queda la tabla de lo que sigue en otro idioma
- [ ] El glosario se alcanza desde las tres puertas de entrada de §2.4
- [ ] Ninguna entrada copia el texto de su regla
- [ ] La especificación del módulo, el registro de cambios y `VERSION` al día
- [ ] La HU con su §8 y su bitácora, y el README de la HU listando la fase
- [ ] El pendiente 21 cerrado en su parte del glosario, abierto en la de los roles
- [ ] Aprobado por el usuario

## 12. Cierre

No se escribe acá. El cierre de la fase vive en el `funcionalidad_implementada.md`: qué se hizo de cada tarea, qué se probó, qué se decidió y qué deuda quedó. Este plan se queda como se aprobó, para poder comparar lo que se dijo contra lo que pasó.
