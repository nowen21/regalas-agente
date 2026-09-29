# HU-009 — Lo que gobierna cada frase llega a tiempo

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-009 |
| **Épica / Feature** | [EP-005 Automatismos que no dependen de la memoria](../epica.md) |
| **Módulo / Componente** | Automatismos |
| **Tipo** | Técnica |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Terminada |
---

## 2. Narrativa

- **Como** quien confía en que el agente cumple las reglas
- **Quiero** que las reglas que gobiernan cada frase que escribe le lleguen con su texto al abrir la sesión
- **Para** que no incumpla una regla que nunca leyó

---

## 3. Contexto y descripción

**Esto ya funciona: la historia se escribe después del programa.** [`validadores/cargador.py`](../../../../validadores/cargador.py) existe desde la versión 5.0.0 y ya reparte `base/` en dos: manda **completo** todo lo que cuelga de `00-` y `01-`, y del resto manda una línea con la ruta, el peso y el título. Verificado el 2026-08-15: llegan puestos `00-nucleo-blindado.md`, `00-identidad-y-rol/` y `01-conducta.md`, 73 KB en total.

Lo que falta no es construirlo: es que exista escrito **qué se exige** de ese reparto, para que nadie lo cambie sin saber qué rompía. Hoy la única explicación vive en un comentario dentro del programa, y una decisión que solo vive en el código se deshace en el primer cambio ([`13·DOC6`](../../../../base/13-documentacion/reglas/DOC6-retro-documenta-el-modulo-sin-especificacion-antes-de-tocarlo.md)).

**Lo que el reparto no cubre, y no es de esta historia.** El capítulo [`02 · flujo de trabajo`](../../../../base/02-flujo-de-trabajo/base.md) llega como índice, y ahí está lo que gobierna cada movimiento de una fase. Eso es [HU-010](../HU-010-la-regla-llega-al-escribir-el-archivo/HU-010-la-regla-llega-al-escribir-el-archivo.md).

**Y una advertencia que esta historia no resuelve.** El 2026-08-14 se incumplió [`00·ID8`](../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) durante toda una sesión, y esa regla **sí llegaba completa**. Que la regla llegue es necesario y no es suficiente: lo que falta después es comprobar lo que se entregó ([EP-004, HU-013](../../EP-004-comprobacion-automatica/HU-013-comparar-el-plan-con-lo-hecho/HU-013-comparar-el-plan-con-lo-hecho.md)).

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | **Reemplazada por RN-06.** Al abrir la sesión llegan con su texto completo los capítulos que gobiernan cómo se escribe y cómo se responde: [`00 · identidad`](../../../../base/00-identidad-y-rol/base.md) y [`01 · conducta`](../../../../base/01-conducta.md) |
| RN-02 | **Reemplazada por RN-06.** Llegan también sus anexos, incluida la [lista de marcadores de generación automática](../../../../base/00-identidad-y-rol/marcadores-de-ia.md), que es la que se relee antes de entregar |
| RN-03 | **Reemplazada por RN-06.** El resto de `base/` sigue llegando como índice: se consulta cuando el tema lo pide |
| RN-04 | Lo que llega puesto se dice, para que se sepa qué se cargó y qué no |
| RN-05 | Vale igual en cualquier proyecto que herede el estándar: es el mismo programa el que carga |
| RN-06 | Todo lo que entrega el arranque cabe en el tope de la herramienta: 10.000 caracteres por enganche. Las reglas no van en el arranque, porque desde la versión 39.3.0 llegan con cada mensaje por el recuperador; va la instrucción de cómo llegan y dónde está el mapa de tareas. **Reemplaza a RN-01, RN-02 y RN-03**, que pedían mandar `00` y `01` completos y no caben. Viene del [pendiente 101](../../../../pendientes/101-el-arranque-deja-de-mandar-las-reglas.md) |

### 3.2 Supuestos

- **Reemplazado por RN-06.** Lo que se carga cabe en el arranque sin que se note. Si no cabe, se decide qué parte del capítulo `01` va puesta, pero la lista de marcadores va completa.

### 3.3 Fuera de alcance

- Lo que llega según el archivo que se está escribiendo, que es [HU-010](../HU-010-la-regla-llega-al-escribir-el-archivo/HU-010-la-regla-llega-al-escribir-el-archivo.md).
- Comprobar que la regla se cumplió: eso es EP-004.

---

## 4. Criterios de aceptación

### CA-01 — Los capítulos que rigen cada frase llegan con su texto

**Reemplazado por el CA-04.** Se cumplió en la fase `A` y dejó de valer en la fase `C`: el texto no cabía en el canal de la herramienta.

```gherkin
Dado que se abre una sesión en un proyecto con el estándar instalado
Cuando el agente recibe su contexto
Entonces los capítulos 00 y 01 están completos, con sus anexos
Y el resto de base/ sigue como índice
```

**Cómo validarlo:**

1. Abrir una sesión en un proyecto de prueba.
2. Mirar lo que se le entregó. Resultado esperado: el texto de las reglas de esos dos capítulos, no sus títulos.
3. Mirar un capítulo cualquiera de los otros. Resultado esperado: sigue como una línea de índice.
Se aprobaba cuando una regla de esos capítulos se puede citar sin abrir ningún archivo.

### CA-02 — Se dice qué llegó puesto y qué llegó como índice

```gherkin
Dado que el contexto se armó
Cuando el agente lo lee
Entonces sabe cuáles capítulos tiene completos y cuáles tiene que abrir
```

**Cómo validarlo:**

1. Abrir la sesión y leer el encabezado del contexto.
2. Resultado esperado: dice cuáles van puestos y cuáles no.
Se aprueba cuando no hay que adivinar si una regla se leyó o solo se nombró.

### CA-03 — El arranque no se vuelve lento

```gherkin
Dado que ahora llega más texto
Cuando se abre la sesión
Entonces la demora sigue sin notarse
```

**Cómo validarlo:**

1. Medir el arranque antes del cambio.
2. Medirlo después. Resultado esperado: la diferencia no cambia cómo se trabaja.
Se aprueba cuando lo que se gana en cumplimiento no se paga con una espera.

### CA-04 · Lo que entrega el arranque cabe entero, y dice cómo llegan las reglas

```gherkin
Dado que se abre una sesión, en el estándar o en un proyecto instalado
Cuando el enganche de arranque entrega su texto
Entonces tiene 10.000 caracteres o menos, y la herramienta no lo guarda aparte
Y dice que las reglas llegan con cada mensaje y dónde está el mapa de tareas
```

**Cómo validarlo:**

1. Correr `adaptadores/claude-code/hook_sesion.py` en la carpeta del estándar y contar los caracteres de lo que entrega. Resultado esperado: 10.000 o menos.
2. Hacer lo mismo en un proyecto de prueba instalado. Resultado esperado: 10.000 o menos.
3. Leer lo que entrega. Resultado esperado: dice que las reglas llegan con cada mensaje y nombra `base/mapa-de-tareas.md`; trae el índice de los recuerdos.
4. Abrir el `CLAUDE.md` del estándar y la plantilla del de los proyectos. Resultado esperado: ninguno pide cargar todos los archivos de `base/` al arrancar.
Se aprueba cuando los cuatro pasos dan lo esperado. **Reemplaza al CA-01**, que pedía `00` y `01` completos al abrir.

### Criterios de aceptación transversales

- [x] **Inocuidad** — no cambia ningún archivo del proyecto.
- [x] **Límites** — un proyecto sin `base/` no se ve afectado.
- [x] **Errores** — si un capítulo no se puede leer, se dice y la sesión sigue.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | Lo que suma al arranque no cambia cómo se trabaja |
| RNF-02 | **Transparencia** | Queda dicho qué se cargó completo y qué no |

---

## 6. Diseño y referencias

- El documento funcional es el [pendiente 25](../../../../pendientes/hecho/las-reglas-de-como-se-escribe-si-llegaban-puestas.md) y el hallazgo H-4 del 2026-08-14 · `el-enganche-del-resumen-no-crea-el-resumen`.
- No afecta ningún modelo de datos.

---

## 7. Tareas técnicas derivadas

- [x] Escribir qué entra completo y qué se queda en índice, con su motivo.
- [x] Probar el reparto, y comprobar que la prueba caza un reparto roto.
- [x] Comprobar que el contexto dice qué va puesto y qué no.
- [x] Medir el peso y el tiempo del arranque.

> El reparto **no se cambió**: ya hacía lo que la historia pide. Lo que faltaba era escribirlo y probarlo.

---

## 8. Fases que la implementan

| Fase | Qué CA cubre | Estado |
|---|---|---|
| [A-EP-005-HU-009-retrodocumentar-el-reparto-de-las-reglas](A-EP-005-HU-009-retrodocumentar-el-reparto-de-las-reglas/README.md) | CA-01, CA-02 y CA-03 | Cerrada el 2026-08-15 |
| [B-EP-005-HU-009-las-reglas-llegan-tambien-al-propio-estandar](B-EP-005-HU-009-las-reglas-llegan-tambien-al-propio-estandar/README.md) | CA-01, en la carpeta del propio estándar, donde no se cumplía | Cerrada el 2026-08-20: Cumple, 7 de 7 casos |
| [C-EP-005-HU-009-el-arranque-cabe-en-el-canal](C-EP-005-HU-009-el-arranque-cabe-en-el-canal/) | CA-04, que reemplaza al CA-01 | Cerrada el 2026-09-28: Cumple, 5 de 5 casos |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | Ninguna: el cargador ya existe y ya reparte | — |
| Riesgo | Que el arranque crezca tanto que estorbe | Se mide antes de decidir, y se ajusta qué parte va puesta |
| Riesgo | Que se cargue mucho y se lea poco | Va solo lo que rige cada frase, no todo el cuerpo de reglas |

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas

## 11. Definition of Done (DoD)

- [x] Los dos capítulos llegan completos, con sus anexos
- [x] Queda dicho qué llegó puesto y qué como índice
- [x] El arranque medido: 73 KB y 0,21 s, el 2026-08-15
- [x] Todos los criterios de aceptación verificados

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | El cargador ya existe |
| **N**egociable | Sí | Qué capítulos entran completos se puede discutir |
| **V**aliosa | Sí | Sin esto, el agente incumple reglas que nunca leyó |
| **E**stimable | Sí | Es un cambio en el reparto, más la medición |
| **S**mall (pequeña) | Sí | Un programa, un criterio de reparto |
| **T**esteable | Sí | Se abre una sesión de prueba y se mira lo que llegó |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-15 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU desde el hallazgo H-4 del 2026-08-14 · `el-enganche-del-resumen-no-crea-el-resumen` |
| 2026-08-15 | Ing. José Dúmar Jiménez Ruíz | Fase A cerrada: el reparto queda escrito en la especificación del módulo, con diez pruebas y la medición del arranque. `CA-03` lo decidió el usuario: 0,21 s no se nota |
| 2026-08-15 | Ing. José Dúmar Jiménez Ruíz | Corregido el contexto contra el programa real: el reparto ya manda literales `00` y `01` desde la 5.0.0, así que la historia no construye, **retro-documenta**. Se cae la premisa de que `ID8` llegaba como índice: llegaba completa y se incumplió igual, y eso queda escrito como advertencia |
| 2026-08-20 | Ing. José Dúmar Jiménez Ruíz | Se abre la fase B: el `CA-01` no se cumplía en la carpeta del propio estándar (pendiente 66). La `RN-05` decía «cualquier proyecto que herede» y la carpeta del estándar no hereda: por eso nadie lo midió |
| 2026-08-20 | Ing. José Dúmar Jiménez Ruíz | Fase B ejecutada y cerrada: `hook_sesion.py` entrega `base/` también en la carpeta del estándar, con caso en `evals/`. 27.1.0 |
| 2026-09-28 | El agente | Suma RN-06 y CA-04 del pendiente 101, aprobado por el usuario, y se abre la fase `C`. El tope del canal es de 10.000 caracteres (documentación de la herramienta), no de 72 KB: el arranque de 103 KB llegaba cortado a un avance de 2.000. Las reglas pasan a llegar con cada mensaje (HU-023), así que el arranque deja de mandarlas |
| 2026-09-28 | El agente | El título pasa de «llega puesto al abrir la sesión» a «llega a tiempo», decidido por el usuario: al abrir ya no llegan las reglas. La carpeta conserva su nombre para no romper los enlaces |
| 2026-09-28 | El agente | Fase C ejecutada y cerrada: el arranque entrega 9.499 caracteres en el estándar, 960 en un proyecto y 4.735 con el gate; ningún texto vigente dice que las reglas llegan al abrir. Lo de la plataforma lo cerró la fase `A` de EP-016 HU-005. 39.4.0 |
