# Plan de Pruebas — Fase A-EP-005-HU-005-el-cambio-de-reglas-no-se-guarda-sin-version   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-005-HU-005 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-005-HU-005-el-cambio-de-reglas-no-se-guarda-sin-version` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/planes/pruebas.md)).

**El CA-02 pesa más que el CA-01.** Casi todos los cambios no tocan reglas: si el enganche los molesta, se apaga, y entonces el CA-01 tampoco se cumple.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Unitario | Que la decisión de «esto toca reglas» se tome por los archivos del cambio | En memoria | Sí |
| Integración | Que al guardar un cambio de reglas sin versión, el enganche actúe | Carpeta temporal con su control de versiones | Sí |
| Silencio | Que un cambio que no toca reglas no note nada | Carpeta temporal | Sí |

**Por qué se miran los archivos y no el mensaje.** El mensaje lo escribe quien guarda; los archivos del cambio son un hecho.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los dos CA |
| Negativa | ☑ | El CA-02: el cambio que no toca reglas **no** debe notar nada |
| Límites | ☑ | Un cambio que toca `base/` y `documentacion/` a la vez |
| Recuperación | ☑ | Que el rechazo diga exactamente qué falta |

### 3.3 Técnicas de diseño de casos

- **La mezcla** — un cambio que toca una regla **y** documentación a la vez. Es el caso donde una decisión mal hecha se cae: si mira solo el primer archivo, deja pasar el cambio de regla.
- **Exigir la existencia, no juzgar el tipo** — el enganche comprueba que **haya** entrada y subida, no si la subida es MAYOR o MENOR. Juzgar eso es criterio, y un enganche que se equivoca ahí traba cambios legítimos.
- **El rechazo accionable** — el riesgo `R-02`: si detiene, dice qué falta —la entrada, la subida, o las dos—. Un "no" sin motivo traba el trabajo urgente.
- **El caso que el enganche no cubre, dicho** — el riesgo `R-03`: si el archivo entró en otro commit, el enganche no lo ve. Se escribe qué caso queda fuera, en vez de dar por cubierto lo que no lo está.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera y los casos en carpetas temporales con su propio control de versiones.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-005 | [CA-01](../HU-005-cambio-de-reglas-con-version.md#ca-01--un-cambio-de-reglas-sin-versión-no-se-guarda) | [CP-001](#cp-001--el-cambio-de-regla-sin-entrada-ni-subida-no-pasa-y-con-las-dos-sí), [CP-002](#cp-002--el-cambio-mezclado-se-detecta-igual) | Funcional | Crítica | Sí | ☐ |
| HU-005 | [CA-02](../HU-005-cambio-de-reglas-con-version.md#ca-02--un-cambio-que-no-toca-reglas-no-se-ve-afectado) | [CP-003](#cp-003--el-cambio-que-no-toca-reglas-no-nota-nada) | Negativa | Crítica | Sí | ☐ |
| HU-005 | RNF — que el resto de los cambios no note nada | [CP-003](#cp-003--el-cambio-que-no-toca-reglas-no-nota-nada), [CP-004](#cp-004--el-rechazo-dice-qué-falta-y-lo-que-no-cubre-queda-escrito) | Recuperación | Alta | Parcial | ☐ |

**Cobertura:** 2 de 2 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — El cambio de regla sin entrada ni subida no pasa, y con las dos sí

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Crítica |
| **Precondiciones** | Dudas 1 y 2 resueltas: si detiene o avisa, y de quién es el disparo |
| **Datos de entrada** | Un cambio en una regla de `base/`, en carpeta temporal |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Cambiar una regla sin tocar el registro ni la versión, y guardar | El enganche actúa: detiene o avisa, según la duda 1 |
| 2 | Agregar solo la entrada al registro y guardar | Sigue faltando la subida: se dice cuál |
| 3 | Agregar solo la subida y guardar | Sigue faltando la entrada: se dice cuál |
| 4 | Poner las dos y guardar | Pasa |
| 5 | Repetir con un cambio en `plantillas/` | Mismo comportamiento |

**Resultado esperado final:** [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md) deja de depender de que quien edita se acuerde.

> **Los pasos 2 y 3 son los que hacen accionable el rechazo.** Decir "falta versionar" sin decir qué mitad obliga a adivinar.

---

### CP-002 — El cambio mezclado se detecta igual

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-01 |
| **Tipo** | Límites |
| **Prioridad** | Crítica |
| **Precondiciones** | El CP-001 corrido |
| **Datos de entrada** | Un cambio que toca una regla de `base/` **y** un archivo de `documentacion/` a la vez |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Guardar el cambio mezclado, sin entrada ni subida | El enganche actúa: la regla está adentro |
| 2 | Comprobar que no se decidió por el primer archivo de la lista | Se miran todos |
| 3 | Invertir el orden de los archivos y repetir | Mismo resultado |
| 4 | Poner entrada y subida, y guardar | Pasa |

**Resultado esperado final:** un cambio de regla escondido entre otros no se cuela.

---

### CP-003 — El cambio que no toca reglas no nota nada

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-02 y RNF |
| **Tipo** | Negativa |
| **Prioridad** | Crítica |
| **Precondiciones** | Carpeta temporal |
| **Datos de entrada** | Cambios en `documentacion/`, en `pendientes/` y en `historico-chat/` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Guardar un cambio en `documentacion/` | No exige nada |
| 2 | Guardar uno en `pendientes/` | No exige nada |
| 3 | Guardar uno en `historico-chat/` | No exige nada |
| 4 | Comprobar que el enganche **corrió** en los tres | Corrió y decidió callar |
| 5 | Guardar uno en `base/` sin versión | Ahora sí actúa: la diferencia es dónde está el archivo |

**Resultado esperado final:** el enganche se puede vivir con él, que es la condición para que siga instalado.

> **El paso 5 es el que da valor a los cuatro anteriores.** Sin él, el caso pasaría con un enganche desconectado.

---

### CP-004 — El rechazo dice qué falta, y lo que no cubre queda escrito

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / RNF |
| **Tipo** | Recuperación |
| **Prioridad** | Alta |
| **Precondiciones** | Los tres casos anteriores corridos |
| **Datos de entrada** | Los mensajes de rechazo, y el caso del archivo que entró en otro commit |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer cada mensaje de rechazo | Dice qué falta y dónde ponerlo |
| 2 | Comprobar que un cambio urgente se puede resolver con lo que el mensaje dice | Se puede, sin abrir el enganche |
| 3 | Probar el caso del archivo de regla que entró en un commit anterior | El enganche no lo ve |
| 4 | Escribir ese caso como límite conocido | Queda escrito, no dado por cubierto |
| 5 | Comprobar la coordinación con el disparo de [HU-004](../../HU-004-control-del-mensaje-de-cambio/HU-004-control-del-mensaje-de-cambio.md) | Un solo enganche llama a las dos comprobaciones |

**Resultado esperado final:** lo que el enganche no cubre queda dicho, en vez de parecer cubierto.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que un cambio que no toca reglas quede trabado | Inmediato. El enganche se apagaría y el CA-01 tampoco se cumpliría |
| **Crítica** | Que un cambio de regla mezclado con otros se cuele | Inmediato. El CA-01 queda en «No» |
| **Alta** | Que trabe un cambio urgente sin decir qué falta (riesgo `R-02`) | Es la duda 1: si detiene, tiene que ser accionable |
| **Media** | Que el enganche empeore el cruce de dos sesiones versionando (riesgo `R-01`) | Se coordina con [EP-002 · HU-006](../../../EP-002-versionado-y-adopcion/HU-006-quien-sube-la-version/HU-006-quien-sube-la-version.md) |
| **Media** | Que el archivo entrara en otro commit y el enganche no lo vea (riesgo `R-03`) | Se escribe qué caso no cubre |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 2 CA y los RNF con caso |
| Casos ejecutados | 4 de 4 |
| Cambios que no tocan reglas trabados | **0** |
| Cambios de regla sin versión que pasan | **0** |
| Rechazos sin motivo accionable | **0** |
| Casos no cubiertos por el enganche | Todos escritos |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
