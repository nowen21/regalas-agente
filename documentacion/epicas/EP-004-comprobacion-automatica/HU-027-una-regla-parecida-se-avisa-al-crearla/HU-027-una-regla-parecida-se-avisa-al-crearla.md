# HU-027 · Una regla parecida se avisa al crearla

> Sus criterios salen de «Lo que se tiene que hacer» del [análisis 1 del pendiente 116](../../../../historico-chat/resumenes/2026-10-04/pendientes/116-el-codigo-de-cimiento-se-repite-en-vez-de-reusarse/analisis-1.md), punto 7, que sale de su acuerdo 5. Los campos que no son alcance (módulo, tipo, estimación y responsable) son propuesta del agente y esperan la aprobación del usuario.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-027 |
| **Épica / Feature** | [EP-004 Comprobación automática](../epica.md) |
| **Módulo / Componente** | `proyectos/cimiento/core/validadores/`, `adaptadores/claude-code/` |
| **Tipo** | Técnica |
| **Prioridad** | Tercera del análisis 1 del pendiente 116 |
| **Estimación** | M |
| **Sprint** | N/A |
| **Solicitante** | Ing. José Dúmar Jiménez Ruíz |
| **Responsable** | Claude |
| **Estado** | Terminada |

---

## 2. Narrativa

- **Como** el usuario, que no quiere reglas que se contradigan
- **Quiero** que al crear o cambiar una regla se avise qué reglas se le parecen
- **Para** leerlas antes y afinar la que ya existe en vez de crear otra, como pide `20·M12`

---

## 3. Contexto y descripción

[`20·M12`](../../../../base/20-meta-reglas/reglas/M12-antes-de-crear-una-regla-buscar-la-duplicacion-es-el-defecto-mas-caro.md) manda buscar por concepto antes de crear una regla, y nada lo hace. En la sesión del 2026-10-04 el usuario mostró el choque entre `02·F4` y `02·F25`, y pidió que las reglas sigan el mismo camino que el código (acuerdo 5).

### 3.1 Reglas de negocio

| ID | Regla | Sale de |
|---|---|---|
| RN-01 | Al crear o cambiar una regla, un control busca por significado las reglas parecidas y avisa cuáles leer antes | Análisis 1 del pendiente 116, acuerdo 5 |
| RN-02 | Reutiliza la búsqueda por significado de `memoria/` y la lectura de reglas de `metareglas` | Acuerdo 5 |
| RN-03 | Avisa y no frena | Acuerdo 5 y `20·M12` |
| RN-04 | Sin la búsqueda por significado instalada, lo dice; no adivina por palabras sueltas | `memoria/parecidas.py` |

### 3.2 Supuestos

- Que `memoria/semantica.py` está disponible en el estándar (hoy lo está).

### 3.3 Fuera de alcance

- Decidir si dos reglas se contradicen: eso es criterio de quien escribe.

---

## 4. Criterios de aceptación

### CA-01 · Al escribir una regla llegan las parecidas

**Sale de:** análisis 1, punto 7 (del pendiente 116).

```gherkin
Dado que el agente escribe o cambia una regla de base/
Cuando termina de escribirla
Entonces el enganche de reglas relacionadas le entrega, además de las que cita, las reglas que se le parecen por significado
Y no detiene nada
```

**Cómo validarlo:**
1. Pasarle al enganche `hook_relacionadas.py` la escritura de `base/02-flujo-de-trabajo/reglas/F25-autorizar-el-arranque-no-aprueba-el-plan.md`.

**Aprobado cuando:** la salida nombra `02·F4` entre las parecidas y el código de salida es 0.

### CA-02 · Se puede pedir para una regla o para lo que entra en el commit

**Sale de:** análisis 1, punto 7 (del pendiente 116).

```gherkin
Dado una regla, o un commit que trae reglas nuevas o cambiadas
Cuando se corre validar.py parecidas
Entonces sale un aviso por cada regla con las que se le parecen
```

**Cómo validarlo:**
1. Correr `python validadores/validar.py parecidas --regla F25`.
2. Preparar un cambio en una regla y correr `python validadores/validar.py parecidas --preparados`.

**Aprobado cuando:** los dos dan avisos con las parecidas y código de salida 0.

### CA-03 · Sin la búsqueda por significado, lo dice

**Sale de:** análisis 1, punto 7 (del pendiente 116).

```gherkin
Dado un ambiente sin la búsqueda por significado
Cuando se pide la lista de parecidas
Entonces dice que no pudo buscar, en vez de callar o adivinar
```

**Cómo validarlo:**
1. Correr las pruebas del caso con la búsqueda apagada.

**Aprobado cuando:** sale el aviso de que no se pudo buscar y ninguna regla inventada.

### Criterios de aceptación transversales

- [x] Rendimiento: responde dentro del umbral acordado con un **volumen realista** (`06`).
- [x] No regresión: lo existente sigue funcionando; la suite relacionada queda verde (`08`, [`02·F5`](../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)).

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Rendimiento** | El enganche responde en menos de 3 segundos sobre las reglas de hoy |

---

## 6. Diseño y referencias

- Documento funcional: [análisis 1 del pendiente 116](../../../../historico-chat/resumenes/2026-10-04/pendientes/116-el-codigo-de-cimiento-se-repite-en-vez-de-reusarse/analisis-1.md), acuerdo 5 y punto 7.

---

## 7. Tareas técnicas derivadas

- [x] La búsqueda de reglas parecidas, con la de `memoria/`.
- [x] Sumarla al enganche de reglas relacionadas y a `validar.py`.
- [x] Pruebas.

---

## 8. Fases que la implementan

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| `A-EP-004-HU-027-el-control-avisa-las-reglas-parecidas` | CA-01, CA-02, CA-03 | (vacío) | [plan_trabajo.md](A-EP-004-HU-027-el-control-avisa-las-reglas-parecidas/plan_trabajo.md) | [plan_pruebas.md](A-EP-004-HU-027-el-control-avisa-las-reglas-parecidas/plan_pruebas.md) | [resultado_pruebas.md](A-EP-004-HU-027-el-control-avisa-las-reglas-parecidas/resultado_pruebas.md) | Terminada |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Riesgo | Que la lista salga larga y se deje de leer | Umbral medido sobre las reglas de hoy y tope de cinco |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-10-04 | Claude | Creación de la HU desde el análisis 1 del pendiente 116 |
| 2026-10-05 | Claude | Terminada en la fase `A-EP-004-HU-027`, versión 54.3.0 |
