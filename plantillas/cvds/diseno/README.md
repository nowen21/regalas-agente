# Diseño: ¿cómo lo va a hacer?   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito **cómo** el sistema va a cumplir lo que la etapa anterior exigió, antes de escribir código. Su valor está en las decisiones con su porqué: sin ellas, dentro de seis meses nadie sabe por qué está armado así y todos lo cambian a ciegas.

> Plantilla. Se llena durante la etapa y se cierra al pasar a la siguiente. La envergadura ajusta la profundidad, nunca la existencia: la sección sin materia se llena con `N/A porque «…»`, nunca se borra. Reemplaza los `«…»` y borra esta caja.

> **Cómo se redacta lo que va dentro de cada `«…»`.** En el idioma del proyecto ([`01·C8`](«RUTA-ESTANDAR»/base/01-conducta.md#c8--habla-el-idioma-del-proyecto)) y en la menor cantidad de palabras con la que se entienda ([`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md)): el dato primero, sin repaso, sin justificación que nadie pidió y sin paso a paso. Lo que no cabe se escribe en su documento y se enlaza.

**Estado: «BORRADOR / APROBADO»** («AAAA-MM-DD», aprobado por «quién»).

---

## 1. Qué entra a esta etapa

| Qué se recibe | De dónde viene | ¿Aprobado? |
|---|---|---|
| Requisitos funcionales y no funcionales | Análisis | «Sí / No, y qué falta» |
| Historias con criterios de aceptación | Análisis | «…» |
| Restricciones de plataforma y formato | Planificación | «…» |

## 2. Los módulos y sus límites

> **Un módulo se define por lo que deja afuera.** Si no se puede decir qué NO hace, todavía no está separado de los demás.

| Módulo | Qué hace | Qué deja explícitamente fuera | Requisitos que cubre |
|---|---|---|---|
| «…» | «…» | «…» | «1, 3» |

## 3. Las decisiones de arquitectura

> **Una decisión de arquitectura es la que cuesta cara de revertir.** Se escribe con las alternativas que se descartaron: sin ellas no se puede defender ni revisar después. Cada una va a su propio documento, y acá queda la lista.

| # | Qué se decidió | Alternativas descartadas | Por qué | Documento |
|---|---|---|---|---|
| 1 | «…» | «…» | «…» | [plantillas/ADR.md](../../ADR.md) |

## 4. Los datos

| Qué se define | Dónde queda |
|---|---|
| Entidades, relaciones y el diccionario de cada campo | [plantillas/ciclo-vida-proyectos/14-modelo-de-datos.md](../../ciclo-vida-proyectos/14-modelo-de-datos.md) |
| Qué se guarda, cuánto tiempo y quién lo puede leer | «…» |
| Qué pasa con los datos que ya existen | «…» |

## 5. La interfaz y la navegación

| Qué se define | Dónde queda |
|---|---|
| Inventario de pantallas y los flujos que importan | [plantillas/ciclo-vida-proyectos/15-diseno-de-interfaz.md](../../ciclo-vida-proyectos/15-diseno-de-interfaz.md) |
| Qué ve cada actor de la sección 5 del análisis | «…» |

## 6. El contrato con quien integra

| Qué se define | Dónde queda |
|---|---|
| Las operaciones, sus entradas, sus salidas y sus errores | [plantillas/ciclo-vida-proyectos/16-documentacion-de-api.md](../../ciclo-vida-proyectos/16-documentacion-de-api.md) |
| Qué se promete que no va a cambiar | «…» |

## 7. Cómo se cumple lo no funcional

> Los requisitos no funcionales del análisis no se cumplen solos: cada uno necesita una decisión de diseño. La fila sin decisión es un requisito que nadie va a cumplir.

| Exigencia del análisis | Cómo la cumple el diseño |
|---|---|
| «…» | «…» |

## 8. Qué puede salir mal, y qué se hace

| Qué falla | Qué ve quien lo usa | Cómo se recupera |
|---|---|---|
| «…» | «…» | «…» |

## 9. Los entregables de esta etapa, y a quién van

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Especificación por módulo | [plantillas/ciclo-vida-proyectos/06-especificacion-modulo.md](../../ciclo-vida-proyectos/06-especificacion-modulo.md) | Cliente, se acuerda | «…» |
| Modelo de datos | [plantillas/ciclo-vida-proyectos/14-modelo-de-datos.md](../../ciclo-vida-proyectos/14-modelo-de-datos.md) | Equipo | «…» |
| Diseño de interfaz | [plantillas/ciclo-vida-proyectos/15-diseno-de-interfaz.md](../../ciclo-vida-proyectos/15-diseno-de-interfaz.md) | Cliente | «…» |
| Documentación de la API | [plantillas/ciclo-vida-proyectos/16-documentacion-de-api.md](../../ciclo-vida-proyectos/16-documentacion-de-api.md) | Quien integra | «…» |
| Decisiones de arquitectura | [plantillas/ADR.md](../../ADR.md) | Equipo | «…» |

## 10. Las puertas de esta etapa

| Qué no se puede hacer | Hasta que | Regla |
|---|---|---|
| Escribir código | la especificación del módulo esté acordada | [`02·F2`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md) |
| Dar por diseñado | cada requisito no funcional tenga su fila en la sección 7 | «…» |

## 11. La decisión de cierre

**«Se pasa a implementación / No se pasa»**, decidido por «quién» el «AAAA-MM-DD».

«Qué quedó sin diseñar a propósito, y con qué riesgo se acepta.»
