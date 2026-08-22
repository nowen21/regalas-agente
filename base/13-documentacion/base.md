# 13 · Documentación  ·  `[CAPA 2]`

> **Historia dueña del texto:** [EP-001 HU-026](../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-026-el-capitulo-13-documentacion/HU-026-el-capitulo-13-documentacion.md). Todo cambio de este capítulo baja por ella ([`02·F23`](../02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md)).

El chat se pierde y el contexto se comprime; los archivos quedan. Documentar es parte del entregable. La capa 3 declara ubicación, nombres y estructura.

Las reglas viven una por archivo en [`reglas/`](reglas/). El anexo [`render-local-de-md.md`](render-local-de-md.md) no es regla: es el montaje opcional que hace que un enlace `.md` se abra formateado en el navegador local.

---

## Las reglas del capítulo

**(a) Qué se documenta al entregar**

| Regla | Qué exige |
|---|---|
| [`DOC1`](reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md) | Al cerrar, el plan, las pruebas y el resultado quedan en documentación versionada. |
| [`DOC2`](reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) | Lo que el código no dice —por qué X y no Y— se escribe. |
| [`DOC3`](reglas/DOC3-verifica-la-trazabilidad-especificacion-implementacion-antes-de-cerrar.md) | Cada afirmación de la especificación se verifica contra lo construido antes de cerrar. |
| [`DOC4`](reglas/DOC4-documenta-lo-que-produccion-necesita.md) | Los pasos de despliegue se documentan ejecutables, sin volver al código. |
| [`DOC5`](reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md) | *opt-in* · lo que no se puede recuperar del código se registra como señal. |
| [`DOC11`](reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md) | La trazabilidad de [`DOC3`](reglas/DOC3-verifica-la-trazabilidad-especificacion-implementacion-antes-de-cerrar.md) se escribe en una tabla de cinco columnas. |
| [`DOC14`](reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md) | Todo enlace entre `.md` lleva ruta legible como texto y destino relativo. |

**(b) Artefactos del proceso y sus índices vivos**

| Regla | Qué exige |
|---|---|
| [`DOC6`](reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md) | Un módulo productivo sin especificación se retro-documenta antes de intervenirlo. |
| [`DOC7`](reglas/DOC7-registra-el-cruce-en-los-dos-documentos-que-se-referencian.md) | Si A consume a B, los dos lo registran. |
| [`DOC8`](reglas/DOC8-cierra-todo-analisis-con-su-tabla-de-decisiones.md) | Todo análisis termina en un archivo de cierre con qué se decidió. |
| [`DOC9`](reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) | Antes de planificar se consulta el mapa, no se explora de cero. |
| [`DOC10`](reglas/DOC10-registra-en-el-catalogo-del-proyecto-toda-regla-propia.md) | Toda regla propia del proyecto queda numerada en su catálogo. |
| [`DOC12`](reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md) | Toda fase declara de dónde sale: arregla, agrega o ambas. |
| [`DOC13`](reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md) | Un módulo nuevo se registra antes de cerrar la unidad que lo creó. |
| [`DOC15`](reglas/DOC15-crea-la-historia-de-usuario-desde-la-plantilla-central.md) | La HU se parte de la plantilla central, no de memoria. |
| [`DOC16`](reglas/DOC16-crea-la-epica-desde-la-plantilla-central.md) | La épica se parte de la plantilla central, no de memoria. |
| [`DOC17`](reglas/DOC17-manten-un-readme-en-cada-nivel-del-arbol-de-trabajo.md) | Ninguna carpeta del árbol queda muda: cada una lista lo suyo. |
| [`DOC18`](reglas/DOC18-actualiza-el-mapa-de-dependencias-al-cerrar-la-unidad.md) | El mapa se actualiza en el mismo cambio que cierra la unidad. |
| [`DOC23`](reglas/DOC23-escribe-el-glosario-de-los-terminos-del-proyecto.md) | Cada proyecto define en una línea las palabras de su negocio. |

**(c) Cómo se llena un documento modelo**

| Regla | Qué exige |
|---|---|
| [`DOC19`](reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md) | Los espacios por llenar de un modelo se marcan `«…»`, la misma marca en todos. |
| [`DOC20`](reglas/DOC20-no-entregues-como-terminado-un-documento-con-marcas.md) | Un documento que todavía trae una marca no está terminado. |
| [`DOC21`](reglas/DOC21-escribe-n-a-en-la-seccion-que-no-aplica.md) | La sección que no aplica se escribe `N/A`: no se deja marcada ni se borra. |
| [`DOC22`](reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md) | Cada sesión deja su resumen aparte, escrito mientras aparece cada hallazgo. |

---

Ver: [`02·F1`](../02-flujo-de-trabajo/reglas/F1-carga-el-contexto-antes-de-actuar.md) y [`02·F2`](../02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md) (contexto y especificación, de donde sale lo que aquí se persiste), [`08`](../08-pruebas.md) (plan de pruebas y verificaciones manuales), [`07·Q5`](../07-calidad-de-codigo.md#q5--comenta-el-porqué-no-el-qué) (documentar, no solo comentar), [`11·CFG3`](../11-configuracion-entornos.md#cfg3--los-entornos-se-parecen-lo-suficiente-para-que-probar-signifique-algo).

**Anexo del capítulo:** [la tabla canónica de trazabilidad](tabla-de-trazabilidad.md), que [`DOC11`](reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md) manda usar al cerrar una unidad.
