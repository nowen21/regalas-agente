# Diseño: ¿cómo lo va a hacer?   ·   `[CAPA 3]`

**Para qué sirve este documento.** Deja escrito **cómo** el sistema va a cumplir lo que la etapa anterior exigió, antes de escribir código. Su valor está en las decisiones con su porqué: sin ellas, dentro de seis meses nadie sabe por qué está armado así y todos lo cambian a ciegas.

> Plantilla. Se llena durante la etapa y se cierra al pasar a la siguiente. La envergadura ajusta la profundidad, nunca la existencia: la sección sin materia se llena con `N/A porque «…»`, nunca se borra. Reemplaza los `«…»` y borra esta caja.

> **Cómo se redacta lo que va dentro de cada `«…»`.** En el idioma del proyecto ([`01·C8`](«RUTA-ESTANDAR»/base/01-conducta.md#c8--habla-el-idioma-del-proyecto)) y en la menor cantidad de palabras con la que se entienda ([`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md)): el dato primero, sin repaso, sin justificación que nadie pidió y sin paso a paso. Lo que no cabe se escribe en su documento y se enlaza. **Si en una celda va más de una cosa, se escribe como lista:** una por renglón, con `<br>` entre ellas y viñeta al empezar. Separarlas con puntos medios en un solo párrafo las vuelve ilegibles.

**Estado: «BORRADOR / APROBADO»** («AAAA-MM-DD», aprobado por «quién»).

---

## 1. Qué entra a esta etapa

| Qué se recibe | De dónde viene | ¿Aprobado? |
|---|---|---|
| Requisitos funcionales y no funcionales | Análisis | «Sí / No, y qué falta» |
| Casos de uso con sus flujos de error | Análisis | «…» |
| Restricciones de plataforma y formato | Planificación | «…» |

## 2. La arquitectura, en una frase y un dibujo

> **El diseño tiene dos niveles y se confunden seguido.** El **alto nivel** dice qué piezas hay y cómo se hablan; el **bajo nivel** dice qué hace cada pieza por dentro. Esta sección es el alto nivel, y cabe en un párrafo: si no cabe, es que todavía no está decidida.

**Cómo está armado:** «Monolito, servicios separados, cliente y servidor, por capas, por eventos. En una frase, y por qué ese.»

**El dibujo:** «Dónde está, y qué muestra: las piezas, quién llama a quién y por dónde entran los datos.»

## 3. Los módulos y sus límites

> **Un módulo se define por lo que deja afuera.** Si no se puede decir qué NO hace, todavía no está separado de los demás.

| Módulo | Qué hace | Qué deja explícitamente fuera | Requisitos que cubre | Con qué otros habla |
|---|---|---|---|---|
| «…» | «…» | «…» | «RF-01, RF-03» | «…» |

## 4. Las decisiones de arquitectura

> **Una decisión de arquitectura es la que cuesta cara de revertir.** Se escribe con las alternativas que se descartaron: sin ellas no se puede defender ni revisar después. Cada una va a su propio documento, y acá queda la lista.

> **`DA` es de decisión de arquitectura.** Es el número con que se cita cada una desde cualquier otro documento, y no se reutiliza.

| # | Qué se decidió | Alternativas descartadas | Por qué | Documento |
|---|---|---|---|---|
| DA-01 | «…» | «…» | «…» | [decisiones-de-arquitectura.md](decisiones-de-arquitectura.md) |
| DA-02 | «…» | «…» | «…» | «…» |

## 5. Los datos

| Qué se define | Cómo queda |
|---|---|
| Entidades, relaciones y el diccionario de cada campo | [plantillas/ciclo-vida-proyectos/14-modelo-de-datos.md](../../ciclo-vida-proyectos/14-modelo-de-datos.md) |
| Qué se guarda, cuánto tiempo y quién lo puede leer | «…» |
| Qué pasa con los datos que ya existen | «…» |
| Qué se indexa, y por qué consulta | «…» |
| Qué se respalda y cada cuánto | «…» |

## 6. La interfaz y la navegación

| Qué se define | Cómo queda |
|---|---|
| Inventario de pantallas y los flujos que importan | [plantillas/ciclo-vida-proyectos/15-diseno-de-interfaz.md](../../ciclo-vida-proyectos/15-diseno-de-interfaz.md) |
| Qué ve cada actor de la sección 6 del análisis | «…» |
| Qué mensajes ve quien se equivoca | «…» |

## 7. El contrato con quien integra

| Qué se define | Cómo queda |
|---|---|
| Las operaciones, sus entradas, sus salidas y sus errores | [plantillas/ciclo-vida-proyectos/16-documentacion-de-api.md](../../ciclo-vida-proyectos/16-documentacion-de-api.md) |
| Qué se promete que no va a cambiar | «…» |
| Qué pasa cuando el otro lado no responde | «…» |

## 8. La seguridad

> No es un capítulo aparte del diseño: es parte de cada módulo. Acá queda lo que atraviesa a todos.

| Qué se define | Cómo queda |
|---|---|
| Quién entra, y cómo se comprueba que es quien dice | «…» |
| Qué puede hacer cada perfil | «…» |
| Qué se cifra, guardado y en tránsito | «…» |
| Qué queda registrado para auditar, y quién lo lee | «…» |
| Dónde viven las credenciales, que no es el código | «…» |

## 9. El entorno técnico y los estándares

| Qué se define | Cómo queda |
|---|---|
| Lenguaje, marco de trabajo y versiones exactas | «…» |
| Ambientes: desarrollo, pruebas, producción | «…» |
| Cómo se nombran archivos, tablas y funciones | «…» |
| Cómo se ramifica y se integra el trabajo | «…» |
| Qué se registra en el diario del sistema, y con qué detalle | «…» |

## 10. Cómo se cumple lo no funcional

> Los requisitos no funcionales del análisis no se cumplen solos: cada uno necesita una decisión de diseño. La fila sin decisión es un requisito que nadie va a cumplir.

| Exigencia del análisis | Cómo la cumple el diseño |
|---|---|
| «RNF-01» | «…» |

## 11. Qué puede salir mal, y qué se hace

| Qué falla | Qué ve quien lo usa | Cómo se recupera |
|---|---|---|
| «…» | «…» | «…» |

## 12. La trazabilidad

| Requisito | Módulo que lo implementa | Decisión de la que depende |
|---|---|---|
| «RF-01» | «…» | «…» |

**Requisitos sin módulo:** «ninguno, o cuáles y por qué.»

## 13. Los entregables de esta etapa, y a quién van

| Documento | Molde | Va a | Estado |
|---|---|---|---|
| Especificación por módulo | [plantillas/ciclo-vida-proyectos/06-especificacion-modulo.md](../../ciclo-vida-proyectos/06-especificacion-modulo.md) | Cliente, se acuerda | «…» |
| Modelo de datos | [plantillas/ciclo-vida-proyectos/14-modelo-de-datos.md](../../ciclo-vida-proyectos/14-modelo-de-datos.md) | Equipo | «…» |
| Diseño de interfaz | [plantillas/ciclo-vida-proyectos/15-diseno-de-interfaz.md](../../ciclo-vida-proyectos/15-diseno-de-interfaz.md) | Cliente | «…» |
| Documentación de la API | [plantillas/ciclo-vida-proyectos/16-documentacion-de-api.md](../../ciclo-vida-proyectos/16-documentacion-de-api.md) | Quien integra | «…» |
| Decisiones de arquitectura | [decisiones-de-arquitectura.md](decisiones-de-arquitectura.md), o una por archivo con [plantillas/ADR.md](../../ADR.md) | Equipo | «…» |
| Diseño de seguridad | Sección 8 de este documento | Cliente y quien opera | «…» |
| Entorno técnico y estándares | Sección 9 de este documento | Equipo y quien instala | «…» |

## 14. Las puertas de esta etapa

| Qué no se puede hacer | Hasta que | Regla |
|---|---|---|
| Escribir código | la especificación del módulo esté acordada | [`02·F2`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md) |
| Dar por diseñado | cada requisito no funcional tenga su fila en la sección 10 | «…» |
| Dar por diseñado | ningún requisito quede sin módulo en la sección 12 | «…» |

## 15. La decisión de cierre

**«Se pasa a implementación / No se pasa»**, decidido por «quién» el «AAAA-MM-DD».

«Qué quedó sin diseñar a propósito, y con qué riesgo se acepta.»
