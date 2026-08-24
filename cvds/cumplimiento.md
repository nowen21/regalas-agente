# Qué del proyecto ya cumple el ciclo de vida   ·   `[CAPA 3]`

**Para qué sirve este documento.** Contrasta lo que este repositorio **tiene hoy** contra lo que exigen los siete documentos de etapa de [cvds/README.md](README.md), y dice, exigencia por exigencia, qué la cumple y dónde está. Lo que no se encontró se dice así, con nombre.

**Analizado el 2026-08-24 sobre la versión 33.4.0.**

> **Cómo se hizo.** Se recorrió el árbol del repositorio y se contó: 249 reglas en los 23 capítulos de `base/` (84 con archivo propio y 165 como sección de su capítulo), 7 épicas, 102 historias, 119 fases, 115 resultados de prueba, 101 cierres de funcionalidad, 68 pruebas de los validadores, 10 destrezas y 81 pendientes cerrados. Lo que aparece como cumplido es porque el archivo existe y se abrió; lo que aparece como ausente es porque se buscó y no está.

---

## 1. El resumen

| Etapa | Cumple | A medias | No existe |
|---|---|---|---|
| 1 · Planificación | 4 | 5 | 8 |
| 2 · Análisis de requisitos | 6 | 2 | 3 |
| 3 · Diseño | 3 | 5 | 3 |
| 4 · Implementación | 7 | 2 | 1 |
| 5 · Pruebas | 5 | 4 | 0 |
| 6 · Despliegue | 3 | 5 | 3 |
| 7 · Mantenimiento | 5 | 4 | 4 |
| **Total** | **33** | **27** | **22** |

**Dónde es fuerte y dónde es débil, dicho de una vez.** El proyecto cumple casi entero la mitad de en medio del ciclo, que es construir y comprobar: ahí está lo que se hizo con método, con evidencia y con documento. Lo que falta se concentra en los dos extremos: **lo que se decide antes de empezar** y **lo que sostiene el sistema después de entregado**.

Es coherente con cómo nació: el estándar se escribió resolviendo incumplimientos concretos del agente, uno por uno, y por eso tiene músculo donde hubo dolor y hueco donde nunca lo hubo.

---

## 2. Etapa 1 · Planificación

| Qué exige el ciclo | Qué lo cumple hoy | Dónde está |
|---|---|---|
| El problema y la necesidad | El brief del proyecto, con las palabras del usuario | [planteamiento.md](../planteamiento.md) |
| El alcance, y qué queda fuera | La regla que impide meter en `base/` lo que sirve a un solo stack o cliente | `M3` y `M13` en [base/20-meta-reglas/](../base/20-meta-reglas/) |
| Modelo de desarrollo | Iterativo, en fases que caben en una jornada y se revierten | `02·F12` |
| Roles y quién aprueba | El agente escribe, el usuario aprueba, y aprobar el cambio no es aprobar el commit | [CLAUDE.md](../CLAUDE.md) |
| Plan de calidad | Lista de 20 filas que toda regla debe pasar, con su sello y su fecha | [base/20-meta-reglas/checklist.md](../base/20-meta-reglas/checklist.md) |

**A medias**

| # | Qué |
|---|---|
| 1 | el desglose del trabajo existe como las 7 épicas pero nunca se hizo antes de empezar |
| 2 | el registro de riesgos vive disperso en `pendientes/` sin probabilidad ni impacto |
| 3 | los interesados no están escritos, aunque de hecho son tres |
| 4 | las restricciones se cumplen en la práctica (sin infraestructura propia, biblioteca estándar) pero no están declaradas |
| 5 | los entregables de la etapa no tienen tabla |

**No existe**

| # | Qué |
|---|---|
| 1 | estudio de viabilidad |
| 2 | acta de constitución |
| 3 | supuestos |
| 4 | dependencias de terceros |
| 5 | estimación de esfuerzo |
| 6 | presupuesto |
| 7 | cronograma con hitos |
| 8 | la decisión formal de cierre de la etapa |

---

## 3. Etapa 2 · Análisis de requisitos

| Qué exige el ciclo | Qué lo cumple hoy | Dónde está |
|---|---|---|
| De dónde salió cada requisito | Lo que el usuario pidió, con sus palabras y sin reescribir | [prompts/](../prompts/) |
| Las reglas del negocio | Las seis del núcleo blindado, que ninguna otra puede contradecir | [base/00-nucleo-blindado.md](../base/00-nucleo-blindado.md) |
| Los actores y sus permisos | Qué puede hacer el agente, qué no, y qué cuesta deshacer cada acción | [base/00-identidad-y-rol/acciones-y-riesgo.md](../base/00-identidad-y-rol/acciones-y-riesgo.md) |
| El glosario del proyecto | Los términos del estándar, con una definición cada uno | [base/glosario.md](../base/glosario.md) |
| Las dudas abiertas | Las preguntas se escriben y detienen el trabajo en vez de resolverse inventando | Las 42 dudas que detuvieron 26 fases, en [pendientes/hecho/](../pendientes/hecho/) |
| La trazabilidad | Tabla de cinco columnas obligatoria, y comprobación antes de cerrar | `13·DOC11` y `13·DOC3` |
| Control de cambios sobre lo acordado | Todo cambio versiona, y nada se borra: se deroga | `M10` y `M11`, con [CHANGELOG.md](../CHANGELOG.md) |

**A medias**

| # | Qué |
|---|---|
| 1 | los requisitos funcionales existen como 102 historias con criterios, pero no hay catálogo con identificador propio ni prioridad |
| 2 | los casos de uso no se escribieron como tales, aunque los criterios de aceptación cumplen parte de esa función |

**No existe**

| # | Qué |
|---|---|
| 1 | requisitos no funcionales, ninguno escrito hasta el llenado de prueba de [cvds/analisis-requisitos/](analisis-requisitos/README.md) |
| 2 | el inventario de funcionalidades del propio proyecto, que es **la puerta que el estándar le exige a los demás** (`02·F26`) y que él mismo no tiene |
| 3 | la línea base aprobada |

---

## 4. Etapa 3 · Diseño

| Qué exige el ciclo | Qué lo cumple hoy | Dónde está |
|---|---|---|
| Los módulos y sus límites | Qué archivo hace qué, y qué está amarrado a la herramienta | [anatomia/](../anatomia/mapa-del-sitio.md) |
| La seguridad | Capítulo propio, con el enmascarado de credenciales corriendo solo | [base/04-seguridad.md](../base/04-seguridad.md) y [validadores/secretos.py](../validadores/secretos.py) |
| Entorno técnico y estándares | Calidad de código, dependencias, entornos y estructura, cada uno con su capítulo | Capítulos 07, 10, 11 y 14 de [base/](../base/README.md) |

**A medias**

| # | Qué |
|---|---|
| 1 | la arquitectura está en las tres capas del [README.md](../README.md) pero sin dibujo ni contrato entre piezas |
| 2 | el porqué de las decisiones vive en [notas/](../notas/README.md), que no es el molde de decisión y no lista alternativas descartadas |
| 3 | el modelo de datos existe como [memoria/esquema.sql](../memoria/esquema.sql) sin diccionario de campos |
| 4 | la interfaz tiene su [README](../interfaz/README.md) pero no documento de diseño |
| 5 | la trazabilidad requisito a módulo no está escrita |

**No existe**

| # | Qué |
|---|---|
| 1 | ninguna decisión de arquitectura escrita con el molde de [plantillas/ADR.md](../plantillas/ADR.md) |
| 2 | documentación de la interfaz de programación de la app local |
| 3 | la tabla que dice cómo se cumple cada requisito no funcional |

---

## 5. Etapa 4 · Implementación

| Qué exige el ciclo | Qué lo cumple hoy | Dónde está |
|---|---|---|
| Cómo se parte el trabajo | 119 fases, cada una con su plan, sus pruebas y su cierre | [documentacion/epicas/](../documentacion/epicas/README.md) |
| Con qué se trabaja | Versiones exactas fijadas, y estáticos con huella verificada | [interfaz/requirements/](../interfaz/README.md) |
| Orden y dependencias | Mapa de dependencias, que se actualiza al cerrar cada unidad | `13·DOC18` |
| Cómo se escribe el código | Capítulos de calidad y de estructura, comprobados por programa | [validadores/codigo.py](../validadores/codigo.py) y [validadores/calidad.py](../validadores/calidad.py) |
| Documentar mientras se construye | El estado de la fase se escribe en el repositorio, no en el chat | `13·DOC1` y el molde 10 del ciclo |
| Cómo se sabe cómo va | Lo planeado contra lo hecho, y las historias sin fase, comprobados solos | [validadores/plan_vs_hecho.py](../validadores/plan_vs_hecho.py) |
| La deuda que se declara | Cada cierre de funcionalidad declara qué quedó sin hacer | Molde 11 del ciclo, 101 escritos |
| Cómo se deshace | Todo cambio de estado pide aprobación, y el plan dice cómo se revierte | `00·N1` y `02·F14` |

**A medias**

| # | Qué |
|---|---|
| 1 | la revisión del código la hace una destreza del propio agente, [skills/revisar-critico](../skills/revisar-critico), y no una persona distinta de quien escribió |
| 2 | el registro de avance no mide tiempo, solo estado |

**No existe:** integración continua. El repositorio no tiene canalización de ninguna clase, y **el propio validador que la exige lo detectaría** ([validadores/ci.py](../validadores/ci.py), `09·G6`). Lo que hay son enganches locales en `.githooks`, que corren solo en esta máquina.

---

## 6. Etapa 5 · Pruebas

| Qué exige el ciclo | Qué lo cumple hoy | Dónde está |
|---|---|---|
| Plan de pruebas junto al de trabajo | Se aprueban juntos, y sin eso no se ejecuta | `02·F4` |
| Probar que lo que no debe pasar no pase | Buena parte de las pruebas comprueban el rechazo, no el caso feliz | Las 38 pruebas de la versión 33.1.0, en [CHANGELOG.md](../CHANGELOG.md) |
| La evidencia | 115 resultados de prueba con lo que se ejecutó y su salida | [documentacion/epicas/](../documentacion/epicas/README.md) |
| Veredicto por criterio | Comprobado por programa, no por lectura | [validadores/veredicto.py](../validadores/veredicto.py) |
| Qué quedó sin probar | Lo no probado se declara «sin verificar», y esa es la regla | `08·T1` y el molde 09 del ciclo |

**A medias**

| # | Qué |
|---|---|
| 1 | los niveles de prueba existen de hecho (68 pruebas de validadores más [evals/](../evals/README.md)) pero nadie los declaró como tales |
| 2 | los defectos se registran en [pendientes/](../pendientes/README.md) sin gravedad ni tiempo de respuesta |
| 3 | la corrida completa existe como [validadores/validar.py](../validadores/validar.py) pero no hay política escrita de qué se vuelve a correr antes de entregar |
| 4 | el usuario acepta cada cambio, pero sin acta de aceptación |

**No existe:** nada de esta etapa falta por completo. Es la más cumplida de las siete.

---

## 7. Etapa 6 · Despliegue

| Qué exige el ciclo | Qué lo cumple hoy | Dónde está |
|---|---|---|
| Instalación desde cero | Un programa que la hace, y que no pisa lo que ya existe | [validadores/instalar.py](../validadores/instalar.py) |
| Lista previa que se marca | Existe como molde, y como recordatorio de lo que la instalación olvida | [plantillas/checklist-despliegue.md](../plantillas/checklist-despliegue.md) |
| Qué trae cada versión, para quien la usa | Registro escrito en castellano llano, exigido por `M17` | [CHANGELOG.md](../CHANGELOG.md) y [documentacion/versiones/](../documentacion/versiones/README.md) |

**A medias**

| # | Qué |
|---|---|
| 1 | los ambientes no están escritos, aunque de hecho son tres |
| 2 | la estrategia de entrada existe como adopción por versión, sin documento |
| 3 | la migración tiene programa ([validadores/migraciones.py](../validadores/migraciones.py)) pero sin ensayo previo con datos reales |
| 4 | la vuelta atrás depende del control de versiones y no está escrita como plan |
| 5 | el manual está repartido entre el [README.md](../README.md) y `Manual-Estandar-Agente.docx`, que no salen del mismo sitio |

**No existe**

| # | Qué |
|---|---|
| 1 | acta de entrega |
| 2 | lo que recibe quien va a operar el sistema |
| 3 | **y la instalación desde cero nunca la ejecutó alguien ajeno al autor**, que es lo único que demostraría que el manual dice lo que hay que hacer y no lo que el autor cree |

---

## 8. Etapa 7 · Mantenimiento

| Qué exige el ciclo | Qué lo cumple hoy | Dónde está |
|---|---|---|
| Por dónde entra una solicitud | Todo pedido se escribe como pendiente; 81 cerrados y 3 abiertos | [pendientes/](../pendientes/README.md) |
| Un cambio grande vuelve a entrar por el ciclo | El pendiente no se ejecuta desde su archivo: baja a historia y se construye como fase | `02·F23` |
| Rutinas periódicas | Al cerrar cada versión se barre lo que el usuario pidió dos veces | `M20` y [plantillas/candidatas-a-regla.md](../plantillas/candidatas-a-regla.md) |
| Versiones y su numeración | Mayor, menor y parche, con la regla de qué obliga a migrar | [CHANGELOG.md](../CHANGELOG.md) y [VERSION](../VERSION) |
| Quién sostiene | Una sola persona, y está dicho | [CLAUDE.md](../CLAUDE.md) |

**A medias**

| # | Qué |
|---|---|
| 1 | los cuatro tipos de trabajo no se distinguen, así que no se puede decir cuánto se va en corregir |
| 2 | el impacto de un cambio se evalúa como grado de versión, no como qué se rompe |
| 3 | la vigilancia existe como [metricas/](../metricas/README.md) y [validadores/rendimiento.py](../validadores/rendimiento.py), sin umbrales ni aviso |
| 4 | qué hacer cuando falla está en [prompts/](../prompts/) como casos sueltos |

**No existe**

| # | Qué |
|---|---|
| 1 | gravedad con tiempos de respuesta |
| 2 | bitácora de operación |
| 3 | plan de mantenimiento |
| 4 | fin de vida |

Y **ningún respaldo se ha restaurado nunca**: [validadores/respaldo.py](../validadores/respaldo.py) comprueba el respaldo de los proyectos que heredan, no el de este.

---

## 9. Los cinco huecos que importan

De los 22 ausentes, estos cinco son los que cambian algo si se llenan. El resto son papeles que un proyecto de una persona puede no necesitar, y decirlo así es más honesto que fingir que faltan.

| # | Hueco | Por qué importa |
|---|---|---|
| 1 | Nadie ajeno al autor instaló el estándar siguiendo solo el manual | Es lo único que separa un estándar de una preferencia personal. Sostiene el proyecto entero y sigue sin comprobarse |
| 2 | El proyecto no tiene inventario de funcionalidades | Es la puerta que le exige a todos los demás (`02·F26`). Incumple escribiendo lo que exige |
| 3 | Sin integración continua | El propio validador la exige y aquí no existe. Las pruebas corren porque alguien se acuerda, que es justo lo que el estándar prohíbe |
| 4 | Ningún respaldo restaurado | Un respaldo sin restaurar es un archivo. Vale para el repositorio y para la base de la memoria |
| 5 | Ninguna decisión de arquitectura escrita | Hay cinco decisiones grandes tomadas y ninguna con sus alternativas descartadas. Dentro de seis meses no se podrán defender |

---

## 10. Lo que este análisis no puede decir

- **No mide calidad, mide existencia.** Que un documento exista no dice que esté bien escrito ni que se siga.
- **No leyó las 249 reglas una por una.** Se verificó qué capítulos existen y qué comprueba cada validador, no el contenido de cada regla.
- **Cuenta lo que el repositorio muestra hoy.** Un archivo puede estar sin usar desde hace meses y aquí aparece igual.
