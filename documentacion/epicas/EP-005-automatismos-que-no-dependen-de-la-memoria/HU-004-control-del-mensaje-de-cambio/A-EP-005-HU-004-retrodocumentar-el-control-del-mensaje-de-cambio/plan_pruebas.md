# Plan de Pruebas — Fase A-EP-005-HU-004-retrodocumentar-el-control-del-mensaje-de-cambio   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-005-HU-004 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-005-HU-004-retrodocumentar-el-control-del-mensaje-de-cambio` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/planes/pruebas.md)).

**Los mensajes ya guardados no se revisan.** El historial es rastro y no se reescribe; auditarlo sería otra unidad de trabajo.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Unitario | Que la comprobación distinga un mensaje vacío de uno que dice qué se hizo | En memoria | Sí |
| Detección | Que la firma de la herramienta se detecte | En memoria | Sí |
| Integración | Que la comprobación corra **al guardar**, sin que nadie la llame | Carpeta temporal con su control de versiones | Sí |
| Documento | Que el cuerpo ponga primero la idea del usuario | Este repositorio | No |

**Lo que falta hoy no es la comprobación: es el disparo.** [`commits.py`](../../../../../validadores/commits.py) existe y funciona; ningún enganche lo llama.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los dos CA |
| Negativa | ☑ | El mensaje vacío y el firmado tienen que salir reportados |
| Límites | ☑ | Un mensaje corto pero informativo, que **sí** debe pasar |
| Recuperación | ☑ | Que un mensaje rechazado diga exactamente qué arreglar |

### 3.3 Técnicas de diseño de casos

- **El corto que sí pasa** — el caso de límites es un mensaje breve pero informativo. Sin él, la comprobación podría estar midiendo largo en vez de contenido, y rechazaría mensajes buenos.
- **La comprobación a mano se queda** — correrla **antes** de guardar sirve para arreglar el mensaje sin que el commit falle. El disparo automático se suma, no reemplaza.
- **Un rechazo tiene que ser accionable** — el riesgo `R-01`: si el enganche detiene, el mensaje del rechazo tiene que decir qué arreglar. Un "no pasa" sin motivo bloquea el trabajo en el peor momento.
- **Un solo enganche para dos comprobaciones** — el riesgo `R-02`: la fase de [HU-005](../../HU-005-cambio-de-reglas-con-version/HU-005-cambio-de-reglas-con-version.md) necesita disparar en el mismo momento. Dos enganches se estorban y se ordenan mal.
- **Nada se prueba sobre el historial real** — arriba.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera y `validar.py commit` sobre mensajes de prueba, en carpeta temporal con su propio control de versiones.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-004 | [CA-01](../HU-004-control-del-mensaje-de-cambio.md#ca-01--un-mensaje-sin-contenido-no-pasa) | [CP-001](#cp-001--el-mensaje-vacío-no-pasa-y-el-corto-pero-informativo-sí), [CP-002](#cp-002--la-comprobación-corre-al-guardar-sin-que-nadie-la-llame) | Negativa | Crítica | Sí | ☐ |
| HU-004 | [CA-02](../HU-004-control-del-mensaje-de-cambio.md#ca-02--el-rastro-de-la-herramienta-se-detecta) | [CP-003](#cp-003--la-firma-de-la-herramienta-se-detecta) | Negativa | Crítica | Sí | ☐ |
| HU-004 | RNF — que el control no dependa de la memoria de nadie | [CP-004](#cp-004--el-cuerpo-pone-primero-la-idea-del-usuario) | Documento | Media | No | ☐ |

**Cobertura:** 2 de 2 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — El mensaje vacío no pasa, y el corto pero informativo sí

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-01 |
| **Tipo** | Negativa |
| **Prioridad** | Crítica |
| **Precondiciones** | Ninguna: se prueba la comprobación |
| **Datos de entrada** | Un mensaje vacío, uno de una palabra, y uno corto pero que dice qué se hizo |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr sobre el mensaje vacío | No pasa |
| 2 | Correr sobre el de una palabra | No pasa |
| 3 | Correr sobre el corto pero informativo | **Pasa** |
| 4 | Leer el motivo del rechazo en los dos primeros | Dice qué le falta al mensaje, no solo que no pasa |

**Resultado esperado final:** se mide contenido, no largo.

> **El paso 3 es el que evita el rechazo injusto.** Una comprobación que mide caracteres rechazaría un mensaje bueno y corto.

---

### CP-002 — La comprobación corre al guardar, sin que nadie la llame

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-01 |
| **Tipo** | Integración |
| **Prioridad** | Crítica |
| **Precondiciones** | Dudas 1 y 2 resueltas: dónde vive el disparo y si detiene o avisa |
| **Datos de entrada** | Carpeta temporal con su propio control de versiones |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Guardar un cambio con un mensaje vacío, sin correr nada a mano | La comprobación se dispara sola |
| 2 | Comprobar qué hace: detener o avisar | Lo que decidió la duda 2 |
| 3 | Si detiene, leer el mensaje | Dice exactamente qué arreglar |
| 4 | Corregir el mensaje y volver a guardar | Ahora pasa |
| 5 | Comprobar que la comprobación a mano sigue funcionando | Sigue: el disparo se suma, no reemplaza |

**Resultado esperado final:** el control deja de depender de que alguien se acuerde de correrlo.

---

### CP-003 — La firma de la herramienta se detecta

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / CA-02 |
| **Tipo** | Negativa |
| **Prioridad** | Crítica |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Un mensaje con la firma de la herramienta, y el mismo sin ella |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr sobre el mensaje con la firma | Se detecta, y el motivo la nombra |
| 2 | Correr sobre el mismo sin la firma | Pasa |
| 3 | Probar variantes de la firma | Todas se detectan |
| 4 | Comprobar que un texto que solo menciona la herramienta **no** se confunde con la firma | No se confunde |

**Resultado esperado final:** el acuerdo de no firmar los commits con la herramienta deja de depender de la memoria.

---

### CP-004 — El cuerpo pone primero la idea del usuario

| Campo | Valor |
|---|---|
| **HU / CA** | HU-004 / RNF |
| **Tipo** | Documento |
| **Prioridad** | Media |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Tres mensajes de prueba, con el orden correcto y con el invertido |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer qué pide el `CLAUDE.md` de este repositorio sobre el orden del cuerpo | Primero la idea del usuario, después lo que hizo el agente |
| 2 | Revisar los tres mensajes contra ese orden | Cada uno con su veredicto |
| 3 | Decidir si un programa puede comprobar ese orden | Sale una respuesta, fundada en lo que costó revisarlo a mano |
| 4 | Registrar esa decisión | Queda escrita, comprobable o no |

**Resultado esperado final:** o el orden se comprueba, o queda dicho que lo decide quien escribe.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que el enganche impida guardar sin decir qué arreglar (riesgo `R-01`) | Inmediato — bloquea el trabajo en el peor momento |
| **Alta** | Que un mensaje corto pero informativo se rechace | Inmediato: la comprobación estaría midiendo largo |
| **Alta** | Que la firma de la herramienta pase sin detectarse | El CA-02 queda en «No» |
| **Media** | Cruce con la fase de [HU-005](../../HU-005-cambio-de-reglas-con-version/HU-005-cambio-de-reglas-con-version.md), que necesita el mismo disparo (riesgo `R-02`) | Se coordinan: un enganche llama a las dos comprobaciones |
| **Media** | Que el enganche corra en proyectos que no lo esperan (riesgo `R-03`) | Entra por el camino de puesta al día, con su entrada en el registro de cambios |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 2 CA y los RNF con caso |
| Casos ejecutados | 4 de 4 |
| Mensajes buenos rechazados | **0** |
| Variantes de la firma que pasan sin detectarse | **0** |
| Rechazos sin motivo accionable | **0** |
| Mensajes del historial revisados o reescritos | **0** |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
