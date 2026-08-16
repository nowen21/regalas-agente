# `base/` — las reglas que el agente obedece

Acá viven **las reglas del agente**: qué puede hacer, qué no, y cómo tiene que trabajar. El usuario las escribe; el agente las obedece. Funcionan como un contrato entre los dos.

Son las reglas que sirven para **cualquier** proyecto. Lo que solo vale para un lenguaje, un cliente o un negocio no va acá ([`20·M3`](20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md)): eso lo declara cada proyecto por su cuenta.

Cada proyecto que use el estándar recibe esta carpeta entera. Al empezar a trabajar, [`validadores/cargador.py`](../validadores/cargador.py) arma con ella el texto que se le entrega al agente.

**¿Se atravesó una palabra?** Está en el [glosario](glosario.md): cada término del estándar explicado en una línea, con qué regla lo manda y dónde vive.

## Cómo está organizado

Las reglas están repartidas por tema en **capítulos numerados**. Cada capítulo está guardado de una de dos formas, según cuánto tenga adentro:

| Forma | Ejemplo | Cuándo se usa |
|---|---|---|
| Un archivo suelto | `01-conducta.md` | El capítulo cabe cómodo en un archivo. |
| Una carpeta | `00-identidad-y-rol/`, con su `base.md` y su `reglas/` | Creció, y se le da un archivo a cada regla. |

Dentro de un capítulo, cada regla tiene un **código corto** que no cambia nunca. Se nombran entre ellas por ese código, poniéndole adelante el número del capítulo cuando la regla vive en otro: [`01·C5`](01-conducta.md#c5--responde-corto) es *"Responde corto"*, y [`02·F13`](02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md) es *"Deja la estructura base puesta antes de trabajar"*. Ese código es la referencia que usan los planes, los commits y las fases ya cerradas, así que una regla nunca se renumera ni se borra: se **deroga** y su texto se queda ([`20·M11`](20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md)).

**Los números no son prioridad, son historia.** Cada capítulo lleva el número que le tocó al nacer. Por eso no están en orden de importancia y hay huecos.

## Las tres clases de capítulo

| Clase | Qué significa | ¿Un proyecto puede cambiarla? |
|---|---|---|
| `[PREÁMBULO]` | Quién es el agente y cómo funcionan las reglas. Se lee antes que todo lo demás. | No. |
| `[CAPA 1]` | Seguridad innegociable. Sus reglas van marcadas `[BLINDADA]`. | **Nunca.** |
| `[CAPA 2]` | Buenas prácticas por tema. | Solo puede ajustarlas, no contradecirlas. |
| `[CAPA 2 · opt-in]` | Igual que la anterior, pero solo aplica si el proyecto la enciende en su `CLAUDE.md`. | El proyecto decide si la usa. |

Cuando dos reglas parecen chocar, gana la de más arriba en esa tabla. El orden completo para desempatar está en [`20·M6`](20-meta-reglas/reglas/M6-ante-un-conflicto-el-desempate-es-este-y-en-este-orden.md).

## Los capítulos, uno por uno

### Se leen primero

| Capítulo | De qué trata |
|---|---|
| [`00 · Identidad y rol`](00-identidad-y-rol/base.md) `[PREÁMBULO]` | Quién es el agente, qué asume y dónde está el borde de lo que le toca. |
| [`20 · Meta-reglas`](20-meta-reglas/base.md) `[PREÁMBULO]` | Cómo son las reglas: dónde vive cada una, qué forma tiene, cuál gana cuando dos chocan y cómo se agrega una nueva. |
| [`00 · Núcleo blindado`](00-nucleo-blindado.md) `[CAPA 1]` | Lo innegociable. No admite excepciones ni las puede tocar ningún proyecto. |

### Cómo se trabaja

| Capítulo | De qué trata |
|---|---|
| [`01 · Conducta del agente`](01-conducta.md) | Cómo se porta en toda tarea: avisar antes de tocar, no inventar, no decidir por su cuenta. |
| [`02 · Flujo de trabajo`](02-flujo-de-trabajo/base.md) | El orden en que se hace el trabajo: especificación, plan, aprobación, implementación, cierre. |
| [`09 · Control de versiones`](09-git.md) | Ramas, commits y qué se sube al repositorio. |
| [`13 · Documentación`](13-documentacion/base.md) | Qué queda escrito de cada trabajo y dónde. |

### Cómo se escribe el código

| Capítulo | De qué trata |
|---|---|
| [`03 · Datos y persistencia`](03-datos.md) | Cómo se guardan los datos y cómo se cambian las tablas. |
| [`04 · Seguridad de la aplicación`](04-seguridad.md) | Que nadie entre ni vea lo que no le toca. |
| [`05 · Manejo de errores y logging`](05-errores-y-logging.md) | Qué se hace cuando algo falla y qué queda anotado. |
| [`06 · Rendimiento y eficiencia`](06-rendimiento.md) | Que no se pida de más ni se repita trabajo. |
| [`07 · Calidad de código`](07-calidad-de-codigo.md) | Que el código se pueda leer y cambiar sin miedo. |
| [`08 · Estrategia de pruebas`](08-pruebas.md) | Qué se prueba y cómo, para que las pruebas sirvan. |
| [`10 · Dependencias de terceros`](10-dependencias.md) | Qué se usa de afuera y bajo qué condiciones. |
| [`11 · Configuración y entornos`](11-configuracion-entornos.md) | Cómo se separa lo de cada máquina de lo que va en el repositorio. |
| [`12 · Privacidad y datos personales`](12-privacidad-datos.md) | Qué se puede hacer con los datos de gente de verdad. |
| [`14 · Estructura del código y nomenclatura`](14-estructura-codigo.md) | Dónde vive cada archivo y cómo se nombra. |

### Se encienden si el proyecto los necesita

| Capítulo | De qué trata |
|---|---|
| [`15 · Registros inmutables`](15-registros-inmutables.md) | Para lo que, una vez guardado, no se puede cambiar ni borrar: facturas, asientos contables. |
| [`16 · Cumplimiento y calidad`](16-cumplimiento-y-calidad.md) | Para proyectos con normas legales o de auditoría encima. |
| [`17 · Interfaz y experiencia de usuario`](17-interfaz.md) | Para lo que ve y usa una persona en pantalla. |
| [`18 · Despliegue e infraestructura`](18-despliegue-e-infraestructura.md) | Cómo llega el sistema al servidor donde corre de verdad. |
| [`19 · Observabilidad y operación`](19-observabilidad-y-operacion.md) | Cómo se sabe, ya en marcha, si el sistema está sano. |

## Cómo se agrega o se cambia una regla

No se escribe una regla nueva a mano y ya. El procedimiento completo —dónde va, qué forma tiene, cómo se versiona— está en [`20 · Meta-reglas`](20-meta-reglas/base.md), y lo que quedó bien se comprueba con el [checklist del estándar](20-meta-reglas/checklist.md).

En corto: buscar si ya existe antes de crear, ponerla en el capítulo dueño del tema, escribirla en el formato de siempre con su ejemplo de qué está mal y qué está bien, y anotar el cambio en el [CHANGELOG](../CHANGELOG.md) subiendo la [VERSION](../VERSION).
