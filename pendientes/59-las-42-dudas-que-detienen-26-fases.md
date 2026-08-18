# Pendiente · Las 42 dudas que detienen 26 fases

**Estado:** abierto · anotado 2026-08-17.

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
| 18 | [`A-EP-001-HU-010`](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/A-EP-001-HU-010-cuando-la-historia-hace-de-especificacion/plan_trabajo.md) | ¿Cuál de los dos caminos del [pendiente 20](20-f2-no-dice-cuando-no-aplica.md)? |
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
| 36 | [`A-EP-002-HU-006`](../documentacion/epicas/EP-002-versionado-y-adopcion/HU-006-quien-sube-la-version/A-EP-002-HU-006-quien-manda-sobre-la-version/plan_trabajo.md) | ¿Cuál de las tres salidas del [pendiente 22](22-dos-sesiones-versionando-a-la-vez.md)? |
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
| **21** · si la comprobación de marcas cubre todo el repositorio | El [pendiente 11](hecho/../11-limpiar-marcadores-de-ia-del-texto-del-estandar.md), paso 3, desde el 2026-08-10 | *«No tocar el histórico: es transcripción literal»*. **Ya está construido así** — se cuenta aparte, y `validar.py marcas` mira solo `base/` y `plantillas/` |
| **18** · cuál de los dos caminos del pendiente 20 | Sigue abierta, pero el [20](20-f2-no-dice-cuando-no-aplica.md) ya trae las dos salidas evaluadas | No hace falta pensarla de cero: hay que elegir |

### Y cuatro más las contesta lo que ya está construido

| # | Duda | Qué hay hoy |
|---|---|---|
| **23** | ¿La corrida completa incluye linter, pruebas y audit? | **No.** `validar.py estandar` no los llama; `linter`, `suite` y `audit` son subcomandos aparte. Ya se decidió al construirlo — falta escribirlo, no decidirlo |
| **31** · **33** | ¿Esperan a la corrida completa de `EP-004·HU-008`? | **No esperan: está construida.** `validar.py estandar` corre desde la fase `A` de esa historia |
| **38** | ¿Un subcomando con dos modos, o dos subcomandos? | **Uno con dos modos.** `validar.py metareglas --catalogo` ya funciona así |

**Las cuatro se contestan mirando el programa, no decidiendo.** Lo que falta es escribir la respuesta en el plan de cada fase.

**Quedan 35 que sí necesitan una respuesta.**

> **Y dos que parecían contestadas y no lo están:** la **26** y la **27** —desde cuándo se exige que el pendiente cerrado nombre su fase, y dónde se declara—. Solo **uno de los 35** archivos de `hecho/` lleva la fila fija, y `pendientes.py` no la comprueba. La convención no está asentada.

> **La 16 y la 21 llevaban un día y ocho días detenidas, y las dos estaban escritas.** Es el mismo defecto que `C23` vino a cerrar, y es la segunda vez que aparece hoy.

---

## Por dónde conviene empezar

1. **El grupo G**, porque hay un daño vivo: las claves se escriben en claro y se versionan.
2. **El grupo B**, porque es una sola decisión que desbloquea cuatro fases, y hay evidencia de esta sesión a favor de detener.
3. **El grupo C**, porque nombrar un proyecto desbloquea cuatro fases de un golpe.

## Cómo se sabrá que cerró

Las 26 fases pasan de la estación 6 detenida a ejecutarse, y el [inventario 48](48-inventario-hu.md) llega a 68 completas.
