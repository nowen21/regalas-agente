# Inventario de funcionalidades: lo que Cimiento es y lo que le falta   ·   `[CAPA 3]`

**Estado: EN REVISIÓN DEL USUARIO** (2026-08-22). Este inventario es **el punto de partida de las épicas**: lo que ya existe queda declarado; lo nuevo no se deriva hasta que el usuario lo apruebe. Lo que diga «por confirmar» es una pregunta, no una decisión.

**Por qué existe:** `02·F26` exige a todo proyecto un inventario aprobado antes de derivar épicas, y Cimiento no tenía el suyo. Acompaña al [planteamiento](cimiento-planteamiento.md). Lo escribió el agente con lo que el proyecto ya tiene construido, por instrucción del usuario.

**Destino del documento:** madura con el sistema hasta ser el manual de Cimiento: cada ítem que se construya gana acá su descripción de uso.

## 0. Lo que el usuario ya definió

1. Cimiento es el mecanismo que obliga a cada proyecto a cumplir los estándares y reglas definidos; los proyectos se administran desde su interfaz, no desde archivos a mano (2026-08-21).
2. El ciclo de vida no hace excepciones: todos sus entregables existen en todo proyecto (2026-08-21).
3. La base de Cimiento es MariaDB en el puerto 3307 (2026-08-22).
4. La interfaz cumple la estructura estándar de un proyecto Django (2026-08-21).

## 1. El cuerpo de reglas

| # | Funcionalidad | Estado |
|---|---|---|
| 1.1 | Núcleo blindado (`00`) que ningún proyecto, prompt ni instrucción relaja | Existe |
| 1.2 | Convenciones agnósticas de stack (`01` a `17`) que cada proyecto ajusta en su capa 3 | Existe |
| 1.3 | Capítulos opt-in: registros inmutables, despliegue, observabilidad, automatización, sistemas que aprenden (`15`, `18`, `19`, `21`, `22`) | Existe (sin ejemplos en `18` y `19`: pendiente 19) |
| 1.4 | Meta-reglas (`20`): cómo nace, se enruta, se versiona, se deroga y se automatiza una regla | Existe |
| 1.5 | Guía de entrada: el ciclo y las cualidades del producto en lenguaje llano | Existe |
| 1.6 | Capítulos opt-in de RPA y de IA | Por confirmar (P-1) |

**Cuenta:** 5 existen, 0 parciales, 0 por construir, 1 por confirmar, de 6.

## 2. El ciclo de vida y sus entregables

| # | Funcionalidad | Estado |
|---|---|---|
| 2.1 | La cadena obligatoria: planteamiento → inventario → épica → HU → fase → especificación → planes → pruebas → cierre | Existe |
| 2.2 | Los 22 moldes del ciclo, numerados por estación | Existe |
| 2.3 | El inventario de funcionalidades como puerta de las épicas, aprobado por el usuario (`F26`) | Existe (sin validador todavía, por `M19`) |
| 2.4 | Las vistas consolidadas que se generan desde lo escrito: SRS, matriz de trazabilidad, registro de defectos, documento de arquitectura | Por construir |
| 2.5 | Los entregables finales en `.docx`, generados desde el expediente vivo | Por construir |

**Cuenta:** 3 existen, 0 parciales, 2 por construir, de 5.

## 3. La comprobación automática

| # | Funcionalidad | Estado |
|---|---|---|
| 3.1 | `validar.py` con sus subcomandos: enlaces, citas, fases, trazabilidad, flujo, versionado, secretos, marcas, metareglas, vigencia, traza, expediente y los demás | Existe |
| 3.2 | Enganches de git (pre-commit con el trinquete de marcas y el guardián de versión; pre-push con la batería) | Existe |
| 3.3 | Enganches de sesión: carga de reglas, histórico, resumen, recuerdos, presupuesto, checkpoint, portero de lo externo | Existe |
| 3.4 | El expediente del ciclo por proyecto: qué entregables hay, cuáles faltan, qué tan llenos están | Existe |
| 3.5 | El veredicto único de cumplimiento por proyecto (instalación + expediente + cadena) en una sola medida | Por construir |

**Cuenta:** 4 existen, 0 parciales, 1 por construir, de 5.

## 4. La memoria entre sesiones

| # | Funcionalidad | Estado |
|---|---|---|
| 4.1 | Transcripción literal de cada sesión, con hora, escrita por el programa | Existe |
| 4.2 | Resumen de lo que cada sesión dejó, hallazgo por hallazgo | Existe |
| 4.3 | Señales de lo aprendido, buscables por palabra y por significado | Existe |
| 4.4 | Recuerdos de cómo trabaja el usuario, versionados en el repo | Existe |
| 4.5 | La traza de la sesión paso a paso (qué ejecutó el agente) | Existe |

**Cuenta:** 5 existen, de 5.

## 5. Instalación y administración de proyectos

| # | Funcionalidad | Estado |
|---|---|---|
| 5.1 | Instalador que lleva reglas, moldes, enganches y memoria a cualquier proyecto, y los pone al día | Existe |
| 5.2 | Aviso de desfase de versión en el primer mensaje de cada proyecto | Existe |
| 5.3 | El canal de defectos de ida y vuelta: el proyecto reporta, el estándar corrige, el aviso vuelve a todos | Existe |
| 5.4 | El registro de proyectos en la interfaz: registrar, editar, dar de baja, medir | Existe |
| 5.5 | El instalador escribe las altas directo en el registro (no en el `.md` generado) | Existe |
| 5.6 | La interfaz mide todos los proyectos de una vez y muestra el veredicto de cada uno | Por construir |

**Cuenta:** 5 existen, 0 parciales, 1 por construir, de 6.

## 6. Proyección: por confirmar con el usuario

| # | Funcionalidad candidata | Estado |
|---|---|---|
| 6.1 | Capítulos opt-in de RPA y de IA (pendientes 08 y 12) | **Por confirmar** (P-1) |
| 6.2 | Un segundo agente real que use el estándar (el contrato del adaptador ya lo prevé) | **Por confirmar** (P-2) |
| 6.3 | El panel de la interfaz como tablero de todos los proyectos, con alertas | **Por confirmar** (P-3) |

## 7. Preguntas abiertas: las contesta el usuario

- **P-1 · ¿Se escriben los capítulos de RPA y de IA ahora, o cuando haya un proyecto que los estrene?** Propuesta del agente: cuando haya proyecto (un capítulo sin proyecto se llena de lo que uno se imagina).
- **P-2 · ¿Entra un segundo agente en el horizonte?** Propuesta: no por ahora; el contrato ya deja el costo medido.
- **P-3 · ¿La interfaz debe ser tablero de todos los proyectos (cumplimiento de un vistazo, alertas)?** Propuesta: sí, como evolución natural de 5.6.

## 8. Qué pasa cuando el usuario apruebe

1. El planteamiento ya dice esto; las siete épicas existentes quedan enlazadas a él.
2. Los ítems «por construir» (2.4, 2.5, 3.5, 5.6) bajan a sus épicas (EP-003, EP-004, EP-007) como historias, citando estos ítems.
3. Este documento sigue madurando con cada ítem construido, camino a ser el manual de Cimiento.

---

*Lo escribió el agente el 2026-08-22 a partir de lo construido y de las decisiones del usuario; nada de §6 y §7 se da por decidido hasta que el usuario lo marque.*
