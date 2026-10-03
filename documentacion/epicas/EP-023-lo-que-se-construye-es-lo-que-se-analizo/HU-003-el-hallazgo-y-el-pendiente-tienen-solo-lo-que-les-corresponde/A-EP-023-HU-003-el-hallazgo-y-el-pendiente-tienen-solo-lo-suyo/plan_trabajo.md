# Plan de Trabajo · Fase `A-EP-023-HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-suyo` (módulo `plantillas/`, `validadores/` y `base/`)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué se hace en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio. Se aprueba antes de tocar nada. El requisito vive en la HU y las pruebas en el `plan_pruebas` de esta fase.

## 0. Identificación y origen  ·  `02·F14` Q1-Q2 · `13·DOC12`

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-023-HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-suyo` |
| **Épica** | [EP-023](../../epica.md) |
| **HU** | [HU-003](../HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde.md), una sola (`F12.1`) |
| **Módulo** | `plantillas/`, `validadores/`, `base/02-flujo-de-trabajo/`, `base/13-documentacion/` y `base/20-meta-reglas/` |
| **Especificación del módulo** | Los CA-01 a CA-08 de la HU-003 |
| **Fecha apertura** | 2026-10-02 |
| **Rama** | `main` |

**ORIGEN** (`13·DOC12`): primera fase de la HU-003. Sale de los puntos 7, 10, 11, 12, 19, 20 y 21 de «Lo que se tiene que hacer» del [análisis 1](../../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-1.md) y del punto 10 del [análisis 8](../../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-8.md).

**Carencias que cierra** (`02·F14` Q3): el hallazgo y el pendiente cargan campos que son del análisis, el cierre se marca a mano de tres formas que no coinciden, y los pendientes viven en una carpeta aparte de lo que los origina (análisis 1, conclusiones 11, 14 a 16 y 34 a 38).

**Aprobación** (`02·F4`): el usuario aprobó el plan el 2026-10-02.

**Disparo** (`02·F15`, etapa 2): el usuario pidió seguir con la HU-003 el 2026-10-02 con «Continúe».

**CA de la HU que cubre esta fase** (`13·DOC11`):

| CA de HU-003 | Estado |
|---|---|
| CA-01 · El pendiente vive dentro de lo que lo genera | ☑ |
| CA-02 · Las plantillas del hallazgo y del pendiente tienen solo sus campos | ☑ |
| CA-03 · Los validadores no exigen los campos viejos | ☑ |
| CA-04 · El cierre lo marca el plan | ☑ |
| CA-05 · El hallazgo de dos campos, con estado y retoma calculados | ☑ |
| CA-06 · El pendiente sin «Proyecto de origen» | ☑ |
| CA-07 · `pendientes/` queda como historia | ☑ |
| CA-08 · La carpeta `pendientes/` vive dentro de lo que origina cada pendiente | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** que el hallazgo tenga solo qué pasó, por qué importa y el enlace a su pendiente; que el pendiente tenga solo de dónde sale, el problema y por qué importa; que su estado y por dónde se retoma se calculen siguiendo los enlaces, y que cada pendiente nuevo viva en una carpeta `pendientes/` dentro de lo que lo origina.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | La regla dice dónde vive el pendiente | Regla | Baja |
| CA-02 | Las tres plantillas del pendiente y la del resumen tienen solo sus campos | Plantilla | Media |
| CA-03 | `pendientes.py` y `resumen.py` aceptan el hallazgo y el pendiente con solo sus campos | Validador | Media |
| CA-04 | El estado del pendiente se calcula: cerrado cuando su plan se cumplió | Programa | Alta |
| CA-05 | `13·DOC22`, la plantilla del resumen y `resumen.py` con el hallazgo de dos campos, estado y retoma calculados | Regla, plantilla y programa | Alta |
| CA-06 | Nadie exige «Proyecto de origen»; el seguimiento cierra con el plan de su padre | Regla, plantilla y validador | Media |
| CA-07 | `pendientes/` no recibe nuevos, acepta el formato viejo, el instalador no la crea; `02·F13` y `20·M13` lo dicen | Regla, validador e instalador | Media |
| CA-08 | La carpeta `pendientes/` dentro de lo que origina; numeración única; índice armado por un programa; el validador de fases la acepta | Validador y programa | Alta |

**Fuera de alcance:**

- Pasar a la forma nueva los pendientes que ya existen en `pendientes/`: pasan uno por uno cuando se vayan a trabajar (análisis 1, conclusión 38).
- Los hallazgos de los resúmenes ya escritos: quedan con sus campos viejos, y los programas los siguen leyendo.
- `validadores/cerrar.py`: sigue cerrando los pendientes viejos como hoy; los nuevos no se cierran a mano.

## 2. Análisis previo, línea base verificada  ·  `02·F17`

Medido el 2026-10-02, sobre la versión 44.0.0:

- `plantillas/pendiente.md` pide «Estado», «Historia de usuario», «De dónde sale», «Proyecto de origen», y las secciones El problema, Por qué importa, Qué falta, El límite y Cómo se sabrá que cerró. `pendiente-de-seguimiento.md` pide «Estado», «Dónde está el defecto», «Qué se reportó allá», «Qué se espera» y «Cuándo cierra». `pendiente-reportado.md` pide «Estado», «Historia de usuario», «Proyecto de origen», «Su pendiente de seguimiento» y «A quién avisar al cerrar».
- `plantillas/sesion.md` define doce campos por hallazgo, una tabla «Orden de resolución» y una lista para cerrar que pide la decisión escrita en el hallazgo.
- `validadores/pendientes.py` mira solo `pendientes/` de la raíz; falla si no existe; exige la fila «Historia de usuario» a todo archivo numerado (hoy falla con `pendientes/103-cada-documento-de-la-cadena-sale-del-anterior.md`, que no la trae) y nombrar el proyecto si existe la fila «Proyecto de origen».
- `validadores/resumen.py` lee el «Estado» y «Con qué se retoma» escritos en cada hallazgo; no calcula nada.
- `validadores/fases.py` trata toda subcarpeta de una épica como HU y toda subcarpeta de una HU como fase: hoy falla con `EP-023/103-cada-documento-de-la-cadena-sale-del-anterior` y con `HU-036/pendientes`.
- `validadores/instalar.py` crea `pendientes/` en todo proyecto (`CARPETAS_BASE`, línea 1017). `validadores/andamio.py` crea el pendiente nuevo como `pendientes/NN-slug.md` y lo agrega al índice escrito a mano, `pendientes/README.md`.
- No hay un programa que arme el índice: `pendientes/README.md` se mantiene a mano.
- `13·DOC22` pide que cada hallazgo diga si quedó resuelto o abierto, dónde quedó, qué dispara y con qué se retoma. `02·F24` pide nombrar el proyecto de origen. `02·F13` crea `pendientes/`. `20·M13` (tabla de `base.md`, línea 170), el glosario (línea 121) y `00-identidad-y-rol/acciones-y-riesgo.md` (línea 58) mandan la mejora acordada a `pendientes/`.
- En la forma nueva existen el 103 (`EP-023/103-cada-documento-de-la-cadena-sale-del-anterior/pendiente.md`, directamente en la épica) y el 108 (`EP-001/HU-036/pendientes/108-la-respuesta-corta-a-una-pregunta-cuenta-como-respuesta/pendiente.md`). Los dos tienen solo «De dónde sale», «El problema» y «Por qué importa».

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `plantillas/pendiente.md`, `plantillas/pendiente-de-seguimiento.md`, `plantillas/pendiente-reportado.md` | Modificar | Plantilla | Solo «De dónde sale», «El problema» y «Por qué importa» |
| `plantillas/sesion.md` | Modificar | Plantilla | El hallazgo con «Qué pasó», «Por qué importa» y «Pendiente» |
| `validadores/pendientes.py` | Modificar | Validador | La forma nueva, el estado calculado, la numeración única y el índice |
| `validadores/resumen.py` | Modificar | Validador | Estado y retoma calculados para el hallazgo de la forma nueva |
| `validadores/fases.py` | Modificar | Validador | Acepta `pendientes/` dentro de una épica, una HU o un resumen del día |
| `validadores/origen.py` | Modificar | Validador | La épica de un pendiente que vive en `pendientes/` |
| `documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/103-cada-documento-de-la-cadena-sale-del-anterior/` | Mover | Documentación | A `EP-023/pendientes/`, con sus enlaces |
| `documentacion/pendientes.md` | Nuevo | Documentación | El índice, que escribe el programa |
| `validadores/andamio.py` | Modificar | Programa | El pendiente nuevo nace como carpeta en la forma nueva |
| `validadores/instalar.py` | Modificar | Instalador | Deja de crear `pendientes/` |
| `base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md` | Modificar | Regla | El hallazgo de dos campos y su enlace |
| `base/02-flujo-de-trabajo/reglas/F24-el-defecto-del-estandar-se-reporta-no-se-corrige.md` | Modificar | Regla | Sin «Proyecto de origen» |
| `base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md` | Modificar | Regla | Sin `pendientes/` |
| `base/20-meta-reglas/base.md`, `base/glosario.md`, `base/00-identidad-y-rol/acciones-y-riesgo.md` | Modificar | Regla | Dónde vive el pendiente |
| `base/reglas-por-tarea/` y `base/mapa-de-tareas.md` | Regenerar | Regla | Con `mapa_tareas.py` |
| `validadores/tests/` | Modificar | Pruebas | Los casos del plan de pruebas |
| `anatomia/mapa-del-sitio.md` | Modificar | Documentación | Lo que cambia de cada programa |
| `CHANGELOG.md` y `VERSION` | Modificar | Versión | 45.0.0 |
| Los documentos de esta fase y la HU-003 | Modificar | Documentación | Cierre |

### 2.2 Matriz de dependencias del refactor  ·  `02·F17`

| Lo que cambia | Quién lo usa | Qué se hace |
|---|---|---|
| `resumen.py` deja de exigir «Estado» en el hallazgo nuevo | `hook_resumen`, el aviso de vuelta, `sin_resolver()`, `proposito()` | Leen el estado calculado; los hallazgos viejos siguen leyendo el escrito |
| `pendientes.py` mira más carpetas | `validar.py pendientes`, `andamio.py`, la línea del próximo libre | El próximo libre cuenta todos los números del proyecto |
| `instalar.py` no crea `pendientes/` | Proyectos nuevos y `pendientes.py`, que hoy falla si no existe | `pendientes.py` deja de fallar sin la carpeta |
| `fases.py` acepta `pendientes/` | La revisión de épicas y HU | Las carpetas de pendiente no se tratan como HU ni como fase |
| El 103 cambia de carpeta | 35 archivos con 127 enlaces, entre ellos fases cerradas y los análisis aprobados del 103; `origen.py`, que agrupa los análisis por épica | Un guion corrige solo la ruta; `origen.py` sube un nivel cuando la carpeta del pendiente está en `pendientes/` |

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Un pendiente está cerrado cuando tiene al menos un análisis aprobado y toda HU que nombra su «Lo que se tiene que hacer» está terminada; las filas que dicen «Este análisis» no esperan nada | Leer una marca de cierre | El cierre lo dice el plan al cumplirse, no una marca (análisis 1, conclusión 16) |
| El pendiente de seguimiento sigue el enlace de su «De dónde sale» hasta el pendiente padre y toma su estado | Una fila «Cuándo cierra» | El enlace ya dice de dónde viene (análisis 1, conclusión 36) |
| El hallazgo de la forma nueva es el que no trae la fila «Estado»: su estado es «sin pendiente», «anotado» o «resuelto», y se retoma por el último análisis de su pendiente | Exigir la forma nueva a todos | Los resúmenes ya escritos no se reabren (`20·M10`) |
| El pendiente nuevo que todavía no sabe a dónde va nace en `historico-chat/resumenes/AAAA-MM-DD/pendientes/NNN-slug/` | Seguir usando la raíz | Así lo acordó el análisis 1 (conclusión 11) |
| `pendientes.py` sigue aceptando el formato viejo dentro de `pendientes/` y deja de pedir ahí la fila «Historia de usuario» | Seguir pidiéndola | La historia la decide el análisis (análisis 1, conclusión 15); el formato viejo se acepta tal como está |
| El índice de pendientes se escribe en `documentacion/pendientes.md`, que el programa reescribe completo cada vez; `pendientes/README.md` queda como historia | Escribirlo dentro de `pendientes/` | Lo decidió el usuario; `pendientes/` ya no recibe nada nuevo |
| El 103 pasa a `EP-023/pendientes/`, y el validador de fases acepta la carpeta `pendientes/` dentro de una épica, de una HU o de un resumen del día, y nada más | Aceptar el 103 suelto en la épica | Su dueño es EP-023, y el análisis 8 (punto 15 de «Lo acordado») pide `pendientes/` y nada más; se pasa ahora porque se está trabajando |
| La versión sube a 45.0.0, MAYOR | MENOR | Los pendientes y hallazgos nuevos cambian de forma y de sitio |

### 2.7 Dudas por resolver antes de codificar

Ninguna. Las dos de la primera redacción las decidió el usuario el 2026-10-02, y quedan en 2.6.

### 2.8 Qué cambia técnicamente  ·  `02·F14` Q5

| Artefacto | Hoy | Después | Regla que aplica |
|---|---|---|---|
| Pendiente | Archivo en `pendientes/` con estado, historia, origen y cinco secciones | Carpeta con `pendiente.md` («De dónde sale», «El problema», «Por qué importa») y sus análisis, dentro de lo que lo origina | `20·M13`, `02·F23` |
| Hallazgo | Doce campos | «Qué pasó», «Por qué importa» y «Pendiente» | `13·DOC22` |
| Estado del pendiente y del hallazgo | Escrito a mano | Calculado siguiendo los enlaces | `13·DOC22` |
| `pendientes/` | Se crea en todo proyecto y recibe todo pendiente | Historia: no se crea ni recibe nuevos | `02·F13`, `20·M13` |
| Índice de pendientes | `pendientes/README.md`, a mano | Lo arma un programa | `20·M13` |

## 3. Desglose de tareas por criterio de aceptación

Cada tarea dice qué y cómo, dónde, por qué e impacto (`02·F16`).

### CA-02 · Las plantillas del hallazgo y del pendiente tienen solo sus campos

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-01 | Dejar las tres plantillas del pendiente con el título, la ficha «De dónde sale» y las secciones «El problema» y «Por qué importa»; en la de seguimiento, «De dónde sale» enlaza el pendiente padre en el estándar | `plantillas/pendiente.md`, `plantillas/pendiente-de-seguimiento.md`, `plantillas/pendiente-reportado.md` | CA-02 | Los pendientes nuevos | 0,5 h | Ninguna | CP-002 |
| T-02 | Dejar el hallazgo de la plantilla del resumen con «Qué pasó», «Por qué importa» y «Pendiente»; quitar los doce campos, la tabla de orden de resolución, y ajustar la lista para cerrar: todo hallazgo enlaza su pendiente | `plantillas/sesion.md` | CA-02, CA-05 | Los resúmenes nuevos | 0,7 h | Ninguna | CP-002, CP-005 |

### CA-03 · Los validadores no exigen los campos viejos

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-03 | Quitar la exigencia de la fila «Historia de usuario»; en la forma nueva exigir solo las tres partes; no fallar si `pendientes/` no existe | `validadores/pendientes.py` | CA-03, CA-07 | Ninguno en los viejos | 1 h | Ninguna | CP-003 |
| T-04 | Aceptar el hallazgo con solo sus tres filas; el que trae «Estado» se lee como hoy | `validadores/resumen.py` | CA-03 | Ninguno en los resúmenes viejos | 0,5 h | Ninguna | CP-003 |

### CA-04 · El cierre lo marca el plan

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-05 | `estado(carpeta)`: «abierto» o «cerrado» según 2.6, leyendo los análisis aprobados de la carpeta, sus filas de «Lo que se tiene que hacer» y el estado de cada HU que nombran | `validadores/pendientes.py` | CA-04 | Ninguno: solo lee | 1,5 h | Ninguna | CP-004 |

### CA-05 · El hallazgo de dos campos, con estado y retoma calculados

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-06 | Cambiar el texto de `DOC22`: cada hallazgo dice qué pasó y por qué importa, y enlaza su pendiente; el estado y la retoma se calculan siguiendo los enlaces; ejemplo nuevo; checklist contra 45.0.0 | `base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md` | CA-05 | Todo proyecto que adopte la versión | 0,5 h | Ninguna | CP-005 |
| T-07 | Para el hallazgo de la forma nueva, calcular su estado («sin pendiente», «anotado», «resuelto») con `pendientes.estado()` y su retoma, que es el último análisis de su pendiente | `validadores/resumen.py` | CA-05 | Los avisos que leen el estado | 1 h | T-04, T-05 | CP-005 |

### CA-06 · El pendiente sin «Proyecto de origen»

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-08 | Quitar «Proyecto de origen» de `02·F24` (el pendiente de allá enlaza el de acá en «De dónde sale») y de `pendientes.py`; el seguimiento toma el estado de su padre (2.6); checklist contra 45.0.0 | `base/02-flujo-de-trabajo/reglas/F24-el-defecto-del-estandar-se-reporta-no-se-corrige.md`, `validadores/pendientes.py` | CA-06 | Todo proyecto que adopte la versión | 1 h | T-05 | CP-006 |

### CA-01 · El pendiente vive dentro de lo que lo genera

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-09 | Decir que la mejora acordada vive en una carpeta `pendientes/` dentro de lo que la origina (épica, HU o resumen del día), y que `pendientes/` de la raíz queda como historia | `base/20-meta-reglas/base.md`, `base/glosario.md`, `base/00-identidad-y-rol/acciones-y-riesgo.md` | CA-01, CA-07 | Todo proyecto que adopte la versión | 0,5 h | Ninguna | CP-001, CP-007 |

### CA-07 · `pendientes/` queda como historia

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-10 | Quitar `pendientes/` de las carpetas que crea `02·F13` y de `CARPETAS_BASE`; checklist contra 45.0.0 | `base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md`, `validadores/instalar.py` | CA-07 | Los proyectos nuevos | 0,5 h | Ninguna | CP-007 |

### CA-08 · La carpeta `pendientes/` vive dentro de lo que origina cada pendiente

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-11 | Aceptar `pendientes/` dentro de una épica, de una HU o de un resumen del día, y nada más (2.6) | `validadores/fases.py` | CA-08 | La revisión de épicas y HU | 1 h | Ninguna | CP-008 |
| T-12 | Numeración única: el próximo libre cuenta `pendientes/`, `hecho/` y toda carpeta de pendiente del proyecto | `validadores/pendientes.py` | CA-08 | `andamio.py` y la línea del próximo libre | 0,5 h | Ninguna | CP-008 |
| T-13 | Programa del índice: lista cada pendiente con su número, dónde vive y si su plan cerró (T-05); los viejos, con su estado escrito; lo escribe en `documentacion/pendientes.md` (2.6) | `validadores/pendientes.py`, `validadores/validar.py` | CA-08 | Un archivo nuevo | 1,5 h | T-05, T-12 | CP-008 |
| T-16 | Pasar la carpeta del 103 a `EP-023/pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/` con un guion: mueve la carpeta, corrige los enlaces relativos de sus archivos (un nivel más) y los 127 enlaces que la nombran en 35 archivos; `origen.py` toma como épica la carpeta que contiene `pendientes/` | `documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/`, `validadores/origen.py` | CA-08 | Los 35 archivos que enlazan el 103; solo cambia la ruta | 1 h | T-11 | CP-008 |
| T-14 | El pendiente nuevo nace como carpeta con `pendiente.md` en la carpeta `pendientes/` del resumen del día, o de la HU cuando se le dice cuál; deja de tocar `pendientes/README.md` | `validadores/andamio.py` | CA-01, CA-08 | Los pendientes nuevos | 1 h | T-01, T-12 | CP-001, CP-008 |

### Cierre

| ID | Qué y cómo | Dónde | Por qué | Impacto | Est. | Depende de | Ev. |
|---|---|---|---|---|:--:|---|---|
| T-15 | Regenerar `base/reglas-por-tarea/` y el mapa de tareas; poner al día el mapa del sitio; escribir los casos del plan de pruebas; subir a 45.0.0 con «⚠ obliga a migrar» y lo que cada proyecto tiene que hacer (`20·M10`) | `base/`, `anatomia/mapa-del-sitio.md`, `validadores/tests/`, `VERSION`, `CHANGELOG.md` | CA-01 a CA-08 | Todo proyecto adopta la versión | 2 h | T-01 a T-14 y T-16 | CP-001 a CP-009 |

## 4. Secuencia de ejecución

Primero las plantillas y las reglas: T-01, T-02, T-06, T-09 y T-10. Después el estado: T-05 y T-08. Luego los validadores: T-03, T-04, T-07, T-11 y T-12. Luego el traslado del 103, el índice y el andamio: T-16, T-13 y T-14. Al final T-15, con los validadores, las pruebas de la fase y la medición de marcas (`02·F5`).

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Cómo se comprueba | Caso |
|---|---|---|
| CA-01 | Leer la regla; crear un pendiente con el andamio | CP-001 |
| CA-02 | Leer las cuatro plantillas | CP-002 |
| CA-03 | Los validadores sobre un hallazgo y un pendiente con solo sus campos | CP-003 |
| CA-04 | El estado de un pendiente cuyo plan se cumplió, y su archivo sin cambios | CP-004 |
| CA-05 | Leer `DOC22` y la plantilla; `resumen.py` sobre un resumen de prueba | CP-005 |
| CA-06 | Buscar «Proyecto de origen»; el estado de un seguimiento cuyo padre cerró | CP-006 |
| CA-07 | Leer `F13` y `M13`; `pendientes.py` sobre `pendientes/`; instalar un proyecto nuevo | CP-007 |
| CA-08 | El validador de fases; el programa del índice | CP-008 |

## 6. Datos y ambiente de prueba

El repositorio del estándar, y carpetas temporales con épicas, HU, resúmenes y pendientes de prueba.

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  `02·F14` Q12 · `02·F10`

Cada proyecto adopta la 45.0.0 con el instalador. No se mueve ni se reescribe nada: los pendientes y los hallazgos que ya existen quedan como están y los programas los siguen leyendo; los nuevos nacen con la forma nueva; un pendiente viejo pasa a la nueva cuando se vaya a trabajar (análisis 1, conclusión 38).

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

`13·DOC22`, `02·F13`, `02·F23`, `02·F24`, `20·M13`, `20·M10`, `20·M11`, `02·F27`, `00·ID8`, `00·ID9`, `02·F5`, `02·F18`, `04·S9`.

## 10. Riesgos y bloqueos

| Riesgo | Qué se hace |
|---|---|
| Que los avisos que leen el estado del hallazgo dejen de funcionar con los resúmenes viejos | El hallazgo con «Estado» escrito se sigue leyendo como hoy; lo prueba el CP-003 |
| Que el próximo número libre choque con uno ya tomado en otra carpeta | El próximo libre cuenta todas las carpetas; lo prueba el CP-008 |
| Que el estado calculado diga «cerrado» antes de tiempo | Solo cierra con un análisis aprobado y todas sus HU terminadas; lo prueba el CP-004 |
| Que un enlace al 103 quede roto al pasarlo | El guion cuenta los enlaces antes y después, y `validar.py estandar` revisa los rotos |

## 11. Definition of Done

- [ ] CA-01 a CA-08 con veredicto y evidencia en `resultado_pruebas.md`.
- [ ] Los validadores y las pruebas sin fallas nuevas, y cero marcas nuevas.
- [ ] `VERSION` y `CHANGELOG.md` en 45.0.0.
- [ ] Aprobación del usuario.

## 12. Seguimiento diario

N/A.

## 13. Cierre

Se llena al cerrar la fase.
