# Plan de Pruebas — Fase A-EP-005-HU-002-enmascarar-la-clave-antes-de-escribirla   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-005-HU-002 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-005-HU-002-enmascarar-la-clave-antes-de-escribirla` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/planes/pruebas.md)).

**Ninguna clave real entra a este repositorio.** Las cadenas de la prueba se **arman**, se usan en carpeta temporal y se borran ([`00·N6`](../../../../../base/00-nucleo-blindado.md#n6--secretos-y-datos-sensibles-nunca-se-exponen-blindada)).

**Las transcripciones viejas no se reescriben.** Si aparece una clave en una, es un incidente: se para y se reporta.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Unitario | Que el enmascarado tape lo que `secretos.py` reconoce como clave | En memoria | Sí |
| Integración | Que el enganche lo llame antes de escribir, y escriba igual si falla | Carpeta temporal | Sí |
| Legibilidad | Que el resto del mensaje quede intacto y se vea dónde estaba la clave | Carpeta temporal | Sí |
| Falso positivo | Que un ejemplo o un dato de prueba no se tape | Carpeta temporal | Sí |

**Por qué se reusa el reconocimiento de [`secretos.py`](../../../../../validadores/secretos.py).** Dos reconocedores distintos taparían y detectarían cosas distintas, y el peor caso es que uno tape y el otro no.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Seguridad | ☑ | El CA-01 |
| Legibilidad | ☑ | El CA-02, que decide si el enmascarado sirve |
| Negativa | ☑ | El ejemplo que **no** se tapa |
| Recuperación | ☑ | Que la transcripción se escriba aunque el enmascarado falle |

### 3.3 Técnicas de diseño de casos

- **Tapar de más se prueba igual que tapar de menos** — el riesgo `R-01`: si el enmascarado come texto, la transcripción deja de servir como rastro y el remedio es peor que la enfermedad. El CA-02 corre antes de dar la fase por buena.
- **La caída del enmascarado es un caso, no un supuesto** — el riesgo `R-02`: se prueba **rompiendo** el enmascarado a propósito y comprobando que la transcripción se escribe igual y que queda dicho que falló. Perder el rastro de la sesión por un fallo del enmascarado es cambiar un riesgo por otro peor.
- **La marca dice que hubo algo, no qué** — sin marca, quien lea la transcripción no entiende el mensaje; con la clave, no sirvió de nada. Cuál es la marca lo decide la duda 1.
- **Cadenas armadas y limpieza comprobada** — arriba, y cada caso verifica que la carpeta temporal quedó vacía.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera —se toca `hook_historico.py`, que corre en cada mensaje— y las sesiones de prueba contra carpetas temporales.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-002 | [CA-01](../HU-002-enmascarar-claves.md#ca-01--una-clave-pegada-en-el-chat-no-queda-escrita-en-claro) | [CP-001](#cp-001--la-clave-pegada-en-el-chat-no-aparece-en-claro-en-el-archivo) | Seguridad | Crítica | Sí | ☐ |
| HU-002 | [CA-02](../HU-002-enmascarar-claves.md#ca-02--el-texto-sigue-siendo-legible) | [CP-002](#cp-002--el-mensaje-queda-legible-y-se-ve-dónde-estaba-la-clave), [CP-003](#cp-003--el-ejemplo-y-el-dato-de-prueba-no-se-tapan) | Legibilidad | Crítica | Sí | ☐ |
| HU-002 | RNF — que la transcripción siga sirviendo de rastro | [CP-004](#cp-004--si-el-enmascarado-falla-la-transcripción-se-escribe-igual) | Recuperación | Crítica | Sí | ☐ |

**Cobertura:** 2 de 2 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — La clave pegada en el chat no aparece en claro en el archivo

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-01 |
| **Tipo** | Seguridad |
| **Prioridad** | Crítica |
| **Precondiciones** | Carpeta temporal, con su estructura de histórico |
| **Datos de entrada** | Varias cadenas con forma de credencial, **armadas para la prueba**, de formatos distintos |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Pegar la primera cadena armada como si fuera un mensaje | Se registra |
| 2 | Buscar la cadena en el archivo de la transcripción | **No está** |
| 3 | Repetir con los otros formatos | Ninguno aparece en claro |
| 4 | Comprobar que lo que se tapó es lo que `secretos.py` reconoce | Mismo reconocimiento, un solo criterio |
| 5 | Borrar la carpeta temporal y comprobar la limpieza | No queda rastro |

**Resultado esperado final:** la mitad que le faltaba al CA-02 de [EP-001 · HU-003](../../../EP-001-cuerpo-de-reglas-heredable/HU-003-nucleo-que-no-se-sobrescribe/HU-003-nucleo-que-no-se-sobrescribe.md) queda construida.

---

### CP-002 — El mensaje queda legible, y se ve dónde estaba la clave

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-02 |
| **Tipo** | Legibilidad |
| **Prioridad** | Crítica |
| **Precondiciones** | Duda 1 resuelta: con qué marca se tapa |
| **Datos de entrada** | Un mensaje con texto antes y después de la clave |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Mandar el mensaje con la clave en medio | Se registra |
| 2 | Comprobar que el texto de antes quedó intacto | Intacto, palabra por palabra |
| 3 | Comprobar que el texto de después quedó intacto | Intacto |
| 4 | Comprobar que en el lugar de la clave hay una marca | La hay |
| 5 | Comprobar que la marca no se confunde con texto del usuario | No se confunde |
| 6 | Leer el mensaje completo y comprobar que se entiende | Se entiende |

**Resultado esperado final:** la transcripción sigue sirviendo de rastro, que es para lo que existe.

> **El paso 6 es el CA.** Contar caracteres tapados no dice si el mensaje quedó legible; leerlo, sí.

---

### CP-003 — El ejemplo y el dato de prueba no se tapan

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-02 |
| **Tipo** | Negativa |
| **Prioridad** | Crítica |
| **Precondiciones** | Carpeta temporal |
| **Datos de entrada** | Un ejemplo de documentación y un dato de prueba, elegidos por parecerse lo más posible a una clave |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Mandar el ejemplo de documentación | **No** se tapa |
| 2 | Mandar el dato de prueba | No se tapa |
| 3 | Comprobar que el criterio es el mismo que usa `secretos.py` | El mismo |
| 4 | Contar cuánto texto se tapó en total en una sesión normal | Se anota la proporción |

**Resultado esperado final:** el enmascarado no come lo que no es clave.

> **El paso 4 mide el daño posible.** Una proporción alta de texto tapado en una sesión sin claves es la señal de que el remedio está de más.

---

### CP-004 — Si el enmascarado falla, la transcripción se escribe igual

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / RNF |
| **Tipo** | Recuperación |
| **Prioridad** | Crítica |
| **Precondiciones** | Carpeta temporal |
| **Datos de entrada** | Un mensaje cualquiera, con el enmascarado roto a propósito |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Romper el enmascarado a propósito | Queda roto |
| 2 | Mandar un mensaje | La transcripción **se escribe igual** |
| 3 | Comprobar que queda dicho que el enmascarado falló | Queda dicho |
| 4 | Comprobar que el mensaje no se perdió | No se perdió |
| 5 | Arreglar el enmascarado y repetir | Vuelve a tapar |

**Resultado esperado final:** el rastro de la sesión no depende de que el enmascarado funcione.

> **Este caso decide un dilema, y lo decide a favor del rastro.** Perder la transcripción por un fallo del enmascarado es cambiar un riesgo por otro peor.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que una clave quede escrita en claro | Inmediato. El CA-01 queda en «No» |
| **Crítica** | Que aparezca una clave real en una transcripción vieja (riesgo `R-03`) | **Se para, se reporta al usuario y no se reescribe nada por cuenta propia**: es un incidente |
| **Crítica** | Que se pierda la transcripción por un fallo del enmascarado (riesgo `R-02`) | Inmediato — el CP-004 existe para que no pase |
| **Alta** | Que el enmascarado tape de más (riesgo `R-01`) | Antes de dar la fase por buena |
| **Media** | Que la marca se confunda con texto del usuario | Es la duda 1: se resuelve antes de escribirla |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 2 CA y los RNF con caso |
| Casos ejecutados | 4 de 4 |
| Claves reales usadas | **0** |
| Cadenas de prueba que quedaron en el repositorio | **0** |
| Formatos de credencial probados | Al menos 3, todos tapados |
| Ejemplos tapados por error | **0** |
| Mensajes perdidos por un fallo del enmascarado | **0** |
| Transcripciones viejas reescritas | **0** |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
