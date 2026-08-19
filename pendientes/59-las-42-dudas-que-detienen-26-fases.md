# Pendiente · Las 42 dudas que detienen 26 fases

**Estado:** **decidido** el 2026-08-18; **abierto** hasta que las 26 fases lleven su respuesta al plan y arranquen. Abierto · anotado 2026-08-17.

| | |
|---|---|
| **Historia de usuario** | [EP-004 · HU-017 — Inventario de HU sin fase](../documentacion/epicas/EP-004-comprobacion-automatica/HU-017-inventario-de-hu-sin-fase/HU-017-inventario-de-hu-sin-fase.md) — las 42 dudas detienen justamente las fases que ese inventario cuenta |
| **De dónde sale** | Ejecutar los 51 planes de trabajo del [48](48-inventario-hu.md). 25 fases corrieron enteras; **26 se detuvieron** en la estación 6 |
| **Qué lo desbloquea** | Que el usuario conteste. Ninguna de las 42 la puede decidir el agente |
| **Qué pasa mientras tanto** | Las 26 fases están **aprobadas y detenidas**. No es que falte trabajo: falta la respuesta |

## El problema

Los 51 planes se aprobaron el 2026-08-17. **25 fases se ejecutaron completas**; las otras **26 no arrancaron**, porque su §2.7 —«dudas por resolver antes de escribir»— tiene preguntas que solo el usuario puede contestar.

No son dudas de implementación. Son **decisiones de diseño del estándar**: si una regla entra a `base/` o se difiere, sobre qué proyecto se prueba, si un enganche detiene el commit o solo avisa. Decidirlas el agente sería exactamente lo que el recuerdo [decidir es del usuario](../historico-chat/memory/decidir-es-del-usuario.md) prohíbe.

## Las 42, agrupadas por lo que hay que decidir

Están agrupadas para poder contestarlas de corrido: varias son la misma pregunta hecha en fases distintas.

### A · ¿Esto entra a `base/` como regla, o se queda donde está? (6)

| # | Fase | Duda |
|---|---|---|
| 1 | [`A-EP-001-HU-003`](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-003-nucleo-que-no-se-sobrescribe/A-EP-001-HU-003-retrodocumentar-el-nucleo-blindado/plan_trabajo.md) | ¿El criterio de entrada al núcleo entra en esta fase, o se difiere a HU-007? |
| 2 | [`A-EP-001-HU-004`](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-004-conducta-de-la-ia/A-EP-001-HU-004-retrodocumentar-la-conducta-de-la-ia/plan_trabajo.md) | ¿Las dos exigencias suben a regla del capítulo `01`? |
| 3 | La misma | Si suben, ¿el recuerdo se queda con su texto o se recorta a un puntero? |
| 4 | [`A-EP-003-HU-008`](../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-008-puntos-de-aprobacion/A-EP-003-HU-008-retrodocumentar-los-puntos-de-aprobacion/plan_trabajo.md) | ¿La lista de puntos de aprobación entra a `base/` como regla, o como documento sin ser regla? |
| 5 | [`A-EP-004-HU-001`](../documentacion/epicas/EP-004-comprobacion-automatica/HU-001-criterio-de-lo-comprobable/A-EP-004-HU-001-retrodocumentar-el-criterio-de-lo-comprobable/plan_trabajo.md) | ¿El criterio de lo comprobable entra al cuerpo de `M9`, o `M9` lo enlaza y el criterio vive en `validadores/`? |
| 6 | [`A-EP-002-HU-006`](../documentacion/epicas/EP-002-versionado-y-adopcion/HU-006-quien-sube-la-version/A-EP-002-HU-006-quien-manda-sobre-la-version/plan_trabajo.md) | ¿En qué capítulo cae la regla de quién sube la versión? |

### B · ¿Detiene, o solo avisa? (4)

Es la misma pregunta cuatro veces, y la respuesta debería ser una sola.

| # | Fase | Duda |
|---|---|---|
| 7 | [`A-EP-002-HU-005`](../documentacion/epicas/EP-002-versionado-y-adopcion/HU-005-sellar-el-trabajo-cerrado/A-EP-002-HU-005-el-sello-de-version-en-el-cierre/plan_trabajo.md) | El sello de versión: ¿el validador lo exige o solo lo avisa? |
| 8 | [`A-EP-005-HU-004`](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-004-control-del-mensaje-de-cambio/A-EP-005-HU-004-retrodocumentar-el-control-del-mensaje-de-cambio/plan_trabajo.md) | Un mensaje de commit que no pasa: ¿detiene el commit o avisa? |
| 9 | [`A-EP-005-HU-005`](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-005-cambio-de-reglas-con-version/A-EP-005-HU-005-el-cambio-de-reglas-no-se-guarda-sin-version/plan_trabajo.md) | Cambiar reglas sin subir versión: ¿detiene o avisa? ¿Depende del tipo de cambio? |
| 10 | [`A-EP-004-HU-013`](../documentacion/epicas/EP-004-comprobacion-automatica/HU-013-comparar-el-plan-con-lo-hecho/A-EP-004-HU-013-comparar-lo-hecho-con-el-plan-aprobado/plan_trabajo.md) | El CA-03: ¿se intenta comprobar o se declara criterio humano? |

> **Hay un dato de esta sesión que ayuda a decidir:** la fase [`A-EP-005-HU-003`](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-003-disparo-al-escribir-un-archivo/A-EP-005-HU-003-retrodocumentar-el-disparo-al-escribir/resultado_pruebas.md) cerró en «No cumple» justamente porque **nada detiene**. Y este repositorio tiene constancia de un aviso ignorado durante una sesión entera.

### C · ¿Sobre qué proyecto o con qué caso se prueba? (5)

Todas necesitan que el usuario nombre algo concreto que solo él conoce.

| # | Fase | Duda |
|---|---|---|
| 11 | [`A-EP-001-HU-005`](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-005-convenciones-de-ingenieria/A-EP-001-HU-005-retrodocumentar-las-convenciones-agnosticas/plan_trabajo.md) | ¿Cuáles dos proyectos, y de qué lenguajes? |
| 12 | [`A-EP-001-HU-006`](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-006-capa-propia-del-proyecto/A-EP-001-HU-006-retrodocumentar-la-capa-del-proyecto/plan_trabajo.md) | ¿Sobre qué proyecto instalado se prueba? |
| 13 | [`A-EP-002-HU-003`](../documentacion/epicas/EP-002-versionado-y-adopcion/HU-003-version-adoptada-por-el-proyecto/A-EP-002-HU-003-retrodocumentar-la-version-adoptada/plan_trabajo.md) | ¿Sobre qué proyecto instalado se prueban el CA-01 y el CA-03? |
| 14 | [`A-EP-003-HU-006`](../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-006-procedimientos-por-rol/A-EP-003-HU-006-retrodocumentar-los-procedimientos-por-rol/plan_trabajo.md) | ¿Con qué encargo real y chico se prueba, corrido dos veces? |
| 15 | [`A-EP-003-HU-007`](../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-007-procedimiento-que-dirige/A-EP-003-HU-007-retrodocumentar-el-procedimiento-que-dirige/plan_trabajo.md) | ¿Con qué encargo chico se recorren las estaciones? |

> Las 12, 13, 14 y 15 se pueden contestar con **el mismo proyecto**, si el usuario quiere. Sería una sola respuesta para cuatro fases.

### D · Lo que solo el usuario recuerda (2)

| # | Fase | Duda |
|---|---|---|
| 16 | [`A-EP-001-HU-007`](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/A-EP-001-HU-007-retrodocumentar-el-procedimiento-de-la-regla/plan_trabajo.md) | ¿Cuáles reglas candidatas se propusieron y **no** entraron? |
| 17 | [`A-EP-002-HU-002`](../documentacion/epicas/EP-002-versionado-y-adopcion/HU-002-registro-de-cambios/A-EP-002-HU-002-retrodocumentar-el-registro-de-cambios/plan_trabajo.md) | ¿Quién hace de lector del CA-03? Tiene que ser alguien que no siguió los cambios |

### E · Qué alcance tiene la comprobación (7)

| # | Fase | Duda |
|---|---|---|
| 18 | [`A-EP-001-HU-010`](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/A-EP-001-HU-010-cuando-la-historia-hace-de-especificacion/plan_trabajo.md) | ¿Cuál de los dos caminos del [pendiente 20](hecho/cuando-la-historia-hace-de-especificacion.md)? |
| 19 | La misma | ¿Cubre solo al estándar, o a cualquier proyecto cuyo entregable no sea código? |
| 20 | La misma | ¿`flujo.py` distingue las dos formas de llenar la casilla, o le basta con que el archivo exista? |
| 21 | [`A-EP-004-HU-012`](../documentacion/epicas/EP-004-comprobacion-automatica/HU-012-marcas-de-generacion-automatica/A-EP-004-HU-012-contar-las-marcas-de-generacion-automatica/plan_trabajo.md) | ¿Aplica a todo el repositorio o solo a lo que se entrega? El histórico es transcripción, no entregable |
| 22 | [`A-EP-004-HU-013`](../documentacion/epicas/EP-004-comprobacion-automatica/HU-013-comparar-el-plan-con-lo-hecho/A-EP-004-HU-013-comparar-lo-hecho-con-el-plan-aprobado/plan_trabajo.md) | ¿Contra qué se comparan los archivos tocados: la rama, el commit, o lo que está sin guardar? |
| 23 | [`A-EP-004-HU-008`](../documentacion/epicas/EP-004-comprobacion-automatica/HU-008-corrida-completa/A-EP-004-HU-008-la-corrida-completa-en-una-linea/plan_trabajo.md) | ¿La corrida completa incluye linter, pruebas y audit, que son lentos, o esos van aparte? |
| 24 | [`A-EP-002-HU-004`](../documentacion/epicas/EP-002-versionado-y-adopcion/HU-004-aviso-al-quedar-atras/A-EP-002-HU-004-retrodocumentar-el-aviso-de-desfase/plan_trabajo.md) | ¿El aviso de desfase pasa a decir **qué** cambió, y con qué detalle? |

### F · Dónde vive el dato (4)

| # | Fase | Duda |
|---|---|---|
| 25 | [`A-EP-004-HU-009`](../documentacion/epicas/EP-004-comprobacion-automatica/HU-009-conteo-por-regla/A-EP-004-HU-009-el-conteo-de-hallazgos-por-regla/plan_trabajo.md) | El registro de conteos: ¿en lo versionado, en lo no versionado, o solo en la salida? |
| 26 | [`A-EP-004-HU-016`](../documentacion/epicas/EP-004-comprobacion-automatica/HU-016-el-pendiente-cerrado-nombra-su-fase/A-EP-004-HU-016-el-pendiente-cerrado-declara-su-fase/plan_trabajo.md) | ¿Desde cuándo se exige que el pendiente cerrado nombre su fase? |
| 27 | La misma | ¿Dónde se declara: una línea fija al principio, o una sección? |
| 28 | [`A-EP-002-HU-005`](../documentacion/epicas/EP-002-versionado-y-adopcion/HU-005-sellar-el-trabajo-cerrado/A-EP-002-HU-005-el-sello-de-version-en-el-cierre/plan_trabajo.md) | ¿El campo del sello entra en los dos modelos o solo en el del cierre? |

### G · Cómo se enmascara una clave (2)

Es lo que le falta al transversal de privacidad de tres fases ya ejecutadas.

| # | Fase | Duda |
|---|---|---|
| 29 | [`A-EP-005-HU-002`](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-002-enmascarar-claves/A-EP-005-HU-002-enmascarar-la-clave-antes-de-escribirla/plan_trabajo.md) | ¿Con qué marca se tapa, para que se vea que hubo algo? |
| 30 | La misma | ¿Qué se hace si aparece una clave en una transcripción vieja? |

> **Esta es la más urgente de las 42.** La fase [`A-EP-005-HU-001`](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-001-transcripcion-de-la-sesion/A-EP-005-HU-001-retrodocumentar-la-transcripcion-de-la-sesion/resultado_pruebas.md) comprobó que **una clave pegada en el chat queda escrita en claro en la transcripción, que se versiona**. Nada enmascara hoy.

### H · Orden entre fases (4)

Cuatro fases preguntan si esperan a otra. Se contestan mirando el orden, no una a una.

| # | Fase | Duda |
|---|---|---|
| 31 | [`A-EP-004-HU-009`](../documentacion/epicas/EP-004-comprobacion-automatica/HU-009-conteo-por-regla/A-EP-004-HU-009-el-conteo-de-hallazgos-por-regla/plan_trabajo.md) | ¿Espera a la corrida completa de HU-008? |
| 32 | [`A-EP-005-HU-005`](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-005-cambio-de-reglas-con-version/A-EP-005-HU-005-el-cambio-de-reglas-no-se-guarda-sin-version/plan_trabajo.md) | ¿Va después de HU-004, o esta crea el disparo y aquella se suma? |
| 33 | [`A-EP-005-HU-006`](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-006-bateria-antes-de-publicar/A-EP-005-HU-006-la-bateria-antes-de-publicar/plan_trabajo.md) | ¿Espera a la corrida completa de EP-004 · HU-008? |
| 34 | [`A-EP-003-HU-008`](../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-008-puntos-de-aprobacion/A-EP-003-HU-008-retrodocumentar-los-puntos-de-aprobacion/plan_trabajo.md) | ¿El procedimiento del director enlaza la lista en esta fase o en otra? |

### I · Las que quedan (8)

| # | Fase | Duda |
|---|---|---|
| 35 | [`A-EP-001-HU-006`](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-006-capa-propia-del-proyecto/A-EP-001-HU-006-retrodocumentar-la-capa-del-proyecto/plan_trabajo.md) | ¿El ajuste que contradice el núcleo se escribe en el proyecto de prueba, o basta simularlo? |
| 36 | [`A-EP-002-HU-006`](../documentacion/epicas/EP-002-versionado-y-adopcion/HU-006-quien-sube-la-version/A-EP-002-HU-006-quien-manda-sobre-la-version/plan_trabajo.md) | ¿Cuál de las tres salidas del [pendiente 22](hecho/dos-sesiones-versionando-a-la-vez.md)? |
| 37 | La misma | ¿Cubre cualquier archivo único compartido, o solo `VERSION` y el registro? |
| 38 | [`A-EP-004-HU-011`](../documentacion/epicas/EP-004-comprobacion-automatica/HU-011-molde-de-las-reglas/A-EP-004-HU-011-la-comprobacion-del-molde-se-puede-correr/plan_trabajo.md) | ¿Un subcomando con dos modos, o dos subcomandos? |
| 39 | [`A-EP-005-HU-004`](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-004-control-del-mensaje-de-cambio/A-EP-005-HU-004-retrodocumentar-el-control-del-mensaje-de-cambio/plan_trabajo.md) | ¿El disparo es enganche de la herramienta o del control de versiones? |
| 40 | [`A-EP-005-HU-006`](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-006-bateria-antes-de-publicar/A-EP-005-HU-006-la-bateria-antes-de-publicar/plan_trabajo.md) | ¿Qué cuenta como «publicar»: el commit a la principal, el despliegue, o los dos? |
| 41 | [`A-EP-005-HU-010`](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-010-la-regla-llega-al-escribir-el-archivo/A-EP-005-HU-010-el-capitulo-llega-al-escribir-el-archivo/plan_trabajo.md) | ¿Qué capítulo rige cada tipo de documento? |
| 42 | La misma | ¿Llega el capítulo completo o solo la regla que aplica, dado lo que pesa? |

## Tres ya están contestadas en el repositorio — 2026-08-18

Buscadas antes de volver a preguntarlas ([`01·C23`](../base/01-conducta.md#c23--busca-en-el-repositorio-antes-de-preguntar)).

| # | Estaba en | Qué dice |
|---|---|---|
| **16** · qué reglas candidatas no entraron | [prompts/analisis/reglas-2026-08-13-candidatas-a-regla.md](../prompts/analisis/reglas-2026-08-13-candidatas-a-regla.md) | Las 22 fichas con su salida: **17 no entraron como regla nueva** —doce «ya está cubierta», tres «no es regla», dos «afinar una existente»— y la tabla dice por cuál quedó cubierta cada una |
| **21** · si la comprobación de marcas cubre todo el repositorio | El [pendiente 11](hecho/limpiar-marcadores-de-ia-del-texto-del-estandar.md), paso 3, desde el 2026-08-10 | *«No tocar el histórico: es transcripción literal»*. **Ya está construido así** — se cuenta aparte, y `validar.py marcas` mira solo `base/` y `plantillas/` |
| **18** · cuál de los dos caminos del pendiente 20 | Sigue abierta, pero el [20](hecho/cuando-la-historia-hace-de-especificacion.md) ya trae las dos salidas evaluadas | No hace falta pensarla de cero: hay que elegir |

### Y cuatro más las contesta lo que ya está construido

| # | Duda | Qué hay hoy |
|---|---|---|
| **23** | ¿La corrida completa incluye linter, pruebas y audit? | **No.** `validar.py estandar` no los llama; `linter`, `suite` y `audit` son subcomandos aparte. Ya se decidió al construirlo — falta escribirlo, no decidirlo |
| **31** · **33** | ¿Esperan a la corrida completa de `EP-004·HU-008`? | **No esperan: está construida.** `validar.py estandar` corre desde la fase `A` de esa historia |
| **38** | ¿Un subcomando con dos modos, o dos subcomandos? | **Uno con dos modos.** `validar.py metareglas --catalogo` ya funciona así |

**Las cuatro se contestan mirando el programa, no decidiendo.** Lo que falta es escribir la respuesta en el plan de cada fase.

### Y dos que el cuerpo de reglas ya resuelve

| # | Duda | Qué dice el cuerpo |
|---|---|---|
| **25** | El registro de conteos: ¿versionado, no versionado, o solo en la salida? | [`09·G3`](../base/09-git.md#g3--deja-fuera-del-control-de-versiones-los-secretos-y-lo-generado) deja fuera del control de versiones **lo generado**, y un conteo lo es. Va a lo no versionado, con el precedente de [`plantillas/proyectos.md`](../plantillas/proyectos.md) |
| **40** | ¿Qué cuenta como «publicar»? | [`09·G7`](../base/09-git.md#g7--todo-commit-se-muestra-al-usuario-y-se-aprueba-antes-de-ejecutarlo) los nombra como dos actos —confirmar y publicar— y publicar es subir al repositorio compartido. **El despliegue es del capítulo `18`, que es opt-in y ningún proyecto lo tiene encendido** |

**Quedan 33 que sí necesitan una respuesta.**

**Nueve contestadas sin preguntar**: tres estaban escritas en el repositorio, cuatro las resuelve el programa que ya corre, y dos las resuelve el cuerpo de reglas.

> **Y dos que parecían contestadas y no lo están:** la **26** y la **27** —desde cuándo se exige que el pendiente cerrado nombre su fase, y dónde se declara—. Solo **uno de los 35** archivos de `hecho/` lleva la fila fija, y `pendientes.py` no la comprueba. La convención no está asentada.

> **La 16 y la 21 llevaban un día y ocho días detenidas, y las dos estaban escritas.** Es el mismo defecto que `C23` vino a cerrar, y es la segunda vez que aparece hoy.

---

## Las 33 resueltas — 2026-08-18

El usuario pidió resolverlas. Cada una lleva **su motivo**, y casi todos salen de algo que este repositorio ya demostró. **Lo que no se puede decidir sin un dato suyo va marcado 👤.**

### A · ¿Entra a `base/` como regla? (6)

El criterio no hay que inventarlo: es la fila 1 del checklist, [`20·M13`](../base/20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md). **Entra a `base/` lo que le exige algo a cualquier proyecto; lo demás tiene su sitio.**

| # | Decisión | Por qué |
|---|---|---|
| 1 | **Se difiere a HU-007.** El criterio de entrada al núcleo es *la regla de las reglas*, y esa es HU-007 | `M13` y `M2`: un tema, un dueño |
| 2 | **Sí suben** al capítulo `01` | Le exigen algo al agente en cualquier proyecto |
| 3 | **El recuerdo se recorta a un puntero.** Si la exigencia vive en `base/`, el recuerdo repitiéndola es texto prestado | La fila 11, y lo que hoy costó `07·Q7` y `12·PR4` |
| 4 | **Documento, no regla.** Una lista de puntos de aprobación es un mapa; la exigencia de aprobar ya está en `02·F4` | `M13`: *«no es regla del estándar»*. Precedente: [`base/20-meta-reglas/checklist.md`](../base/20-meta-reglas/checklist.md) |
| 5 | **`M9` lo enlaza; el criterio vive en `validadores/`.** Meter el criterio en el cuerpo de `M9` la saca del molde de cuatro líneas | La fila 10, y hoy se acortaron diez reglas por eso |
| 6 | **Capítulo `02`.** Quién sube la versión es un paso del flujo, no del control de versiones | Es el mismo razonamiento con el que `02·F24` fue al `02` y no a la épica de instalación |

### B · ¿Detiene, o solo avisa? (4)

**Una sola respuesta para las cuatro: detiene lo que se puede comprobar sin criterio; avisa lo que necesita juicio.**

| # | Decisión | Por qué |
|---|---|---|
| 7 | **Detiene.** Que falte el sello de versión se comprueba mirando el archivo | Sin criterio de por medio |
| 8 | **Detiene.** El molde del mensaje es forma, y la forma se comprueba | Igual |
| 9 | **Detiene**, y no depende del tipo de cambio: si `base/` cambió y `VERSION` no, falta la versión | `20·M10` no admite excepción por tamaño |
| 10 | **Criterio humano, y se declara.** Comparar lo hecho con lo planeado necesita leer los dos | Fingir que se comprueba es peor que decir que no |

> **La evidencia de esta sesión está toda del mismo lado.** La fase `A-EP-005-HU-003` cerró en «No cumple» porque nada detiene; `ID9` se incumplió todo un día y nada avisó; las marcas de `ID8` crecieron ocho días después de registrarse. **Un aviso que nada respalda se ignora.**

### C · Sobre qué se prueba (5)  ·  👤

Estas necesitan un dato que solo el usuario tiene. **Se proponen, con lo que dice [`plantillas/proyectos.md`](../plantillas/proyectos.md):**

| # | Propuesta | Por qué |
|---|---|---|
| 11 | **AgroSystem** (Laravel · PHP) y **RNI** (Angular + Python) | Son los dos stacks más distintos del registro, que es lo que la prueba necesita |
| 12–15 | **shopnest-mesa** para las cuatro | Es el único que ya reporta al estándar, tiene estructura completa y carpeta de pendientes. Una respuesta para cuatro fases |

**Falta el encargo chico y real de las dudas 14 y 15**, y ese no está en ningún archivo.

### D · Lo que solo el usuario recuerda (1)  ·  👤

| # | Propuesta | Por qué |
|---|---|---|
| 17 | **El usuario, leyendo una entrada del registro de una versión que no siguió** | Es el único lector disponible que cumple la condición: no siguió esos cambios |

### E · Qué alcance tiene la comprobación (5)

| # | Decisión | Por qué |
|---|---|---|
| 18 | **El camino 2 del [pendiente 20](hecho/cuando-la-historia-hace-de-especificacion.md):** la historia hace de especificación cuando el entregable no es código | El camino 1 abre una excepción en `F2`, y una excepción es la puerta que después nadie cierra. `08·T1` es el ejemplo vivo |
| 19 | **Cualquier proyecto cuyo entregable no sea código**, no solo el estándar | `20·M3`: la base no se escribe para un caso |
| 20 | **Le basta con que el archivo exista.** Distinguir las dos formas de llenar la casilla es criterio | Igual que la 10 |
| 22 | **Contra el commit del que salió la fase.** Ni la rama —que arrastra lo ajeno— ni lo sin guardar, que cambia mientras se mira | Es lo que hizo falta hoy, dos sesiones sobre el mismo árbol |
| 24 | **Sí dice qué cambió, al nivel de entrada del registro:** la versión, su tipo y su título | El detalle mayor obliga a mantener dos textos que dicen lo mismo |

### F · Dónde vive el dato (3)

| # | Decisión | Por qué |
|---|---|---|
| 26 | **Desde el 2026-08-16**, que es cuando nació la exigencia. Lo cerrado antes no se reabre | [`20·M10`](../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md): un cambio de norma no reabre lo cerrado |
| 27 | **Una fila fija en la ficha de cabecera**, como la de «Historia de usuario» | Una sección se olvida; una fila de la ficha se ve vacía. **Hoy solo 1 de 35 la lleva** |
| 28 | **Solo en el modelo del cierre.** El sello dice bajo qué versión cerró algo, y solo el cierre cierra | Ponerlo en los dos obliga a llenarlo cuando todavía no hay nada que sellar |

### G · Cómo se enmascara una clave (2)

| # | Decisión | Por qué |
|---|---|---|
| 29 | **`«enmascarado»`**, la misma marca que el estándar ya usa para el espacio por llenar | No se inventa una marca nueva; se ve que hubo algo y se distingue del texto |
| 30 | **La vieja se enmascara igual, y queda dicho en el archivo que se hizo.** No se borra el bloque | Borrar un bloque de una transcripción pierde lo dicho — es lo que hoy casi pasa con el pendiente 29 |

### H · Orden entre fases (2)

| # | Decisión | Por qué |
|---|---|---|
| 32 | **`HU-004` crea el disparo y `HU-005` se suma.** Dos enganches sobre el mismo momento se pisan | Un solo dueño por punto de disparo |
| 34 | **En otra fase.** Enlazar la lista desde el procedimiento del director es trabajo de ese procedimiento | `M2`: un tema, un dueño |

### I · Las que quedan (6)

| # | Decisión | Por qué |
|---|---|---|
| 35 | **Se escribe en un proyecto de mentira, en carpeta temporal.** Nunca en uno real | [`00·N4`](../base/00-nucleo-blindado.md#n4--proteger-los-datos-reales-blindada) |
| 36 | **La salida 1 del [pendiente 22](hecho/dos-sesiones-versionando-a-la-vez.md):** la versión se sube al guardar, no al editar | La 3 —una sola sesión— ya se incumplió dos veces esta semana. Una regla que la práctica salta no es una regla |
| 37 | **Cualquier archivo único compartido**, no solo `VERSION` y el registro | Ya pasó con `pendientes/README.md`, y está escrito en el propio 22 |
| 39 | ~~Enganche de la herramienta~~ → **CORREGIDA el 2026-08-18: enganche del control de versiones**, que es lo que ya está construido y funciona | **La decisión original era falsa.** Decía que el del control de versiones no corre cuando el agente escribe, y cada commit de esa sesión imprimió su comprobación: sí corre. Y corta el commit **venga de donde venga**, no solo del agente |
| 41 | **Por carpeta, no por tipo de documento.** `base/` → capítulo `20`; `documentacion/epicas/` → `02` y `13`; `pendientes/` → `02·F23` | El tipo hay que adivinarlo; la carpeta se lee de la ruta, que es lo mismo que hace `cargador.py` |
| 42 | ~~Solo la regla que aplica~~ → **DEVUELTA el 2026-08-18: no era mía para decidir** | **Contradecía el `CA-01` de la historia**, que pide el capítulo **completo**. Por [`02·F19`](../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md) manda el criterio de aceptación, no una decisión tomada aparte. **La decidí sin leer los criterios de la historia** — el mismo defecto de `M12`, tercera vez en el día |

### Y una decisión devuelta

**La 42 se anuló el mismo día que se tomó.** Decía «solo la regla que aplica»; el `CA-01` de [EP-005 · HU-010](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-010-la-regla-llega-al-escribir-el-archivo/HU-010-la-regla-llega-al-escribir-el-archivo.md) pide el capítulo **completo**.

**Por [`02·F19`](../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md), la redacción del CA es la especificación**, así que una decisión tomada en un pendiente no puede cambiarla. Si el criterio tiene que cambiar, se cambia **en la historia y con su aprobación** — no de costado.

**Lo que la duda planteaba sigue siendo real:** el capítulo `02` entero pesa **98 KB** y mandarlo en cada escritura llena la ventana de contexto, que es el problema que `cargador.py` ya resolvió con índices. Pero eso no lo decide el pendiente: **lo decide quien apruebe la historia.**

> **Es la tercera vez en el día que decido sin leer lo que ya estaba escrito.** Las dos anteriores fueron `F2` contra `F0`, y la 39 contra la evidencia de esta misma sesión.

---

## Lo que sigue

**Las decisiones están escritas; las 26 fases siguen detenidas.** Cada una tiene que llevar su respuesta a la §2.7 de su plan y arrancar. Eso es trabajo de cada fase, no de este pendiente.

**Cuatro siguen necesitando un dato del usuario:** las 11 a 15 —qué proyectos y qué encargo— y la 17 —quién lee—. Van con propuesta, y una propuesta que nadie corrige se toma por aceptada.

---

## Por dónde conviene empezar

1. **El grupo G**, porque hay un daño vivo: las claves se escriben en claro y se versionan.
2. **El grupo B**, porque es una sola decisión que desbloquea cuatro fases, y hay evidencia de esta sesión a favor de detener.
3. **El grupo C**, porque nombrar un proyecto desbloquea cuatro fases de un golpe.

## Cómo se sabrá que cerró

Las 26 fases pasan de la estación 6 detenida a ejecutarse, y el [inventario 48](48-inventario-hu.md) llega a 68 completas.
