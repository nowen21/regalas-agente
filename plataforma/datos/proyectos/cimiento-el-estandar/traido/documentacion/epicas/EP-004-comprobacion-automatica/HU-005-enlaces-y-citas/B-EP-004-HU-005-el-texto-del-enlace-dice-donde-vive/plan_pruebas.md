# Plan de Pruebas — Fase B-EP-004-HU-005: el texto del enlace dice dónde vive

**Para qué sirve este documento.** Dice **con qué casos se comprueba** lo construido. Se aprueba antes de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el [resultado_pruebas.md](resultado_pruebas.md).

| Campo | Valor |
|---|---|
| **Código** | PP-B-EP-004-HU-005 |
| **Versión** | 1.0 |
| **Fecha** | 2026-08-18 |
| **Aprobado por** | Pendiente — el usuario |

---

## 3. Estrategia de pruebas

**Un programa que reescribe 284 enlaces en 89 archivos tiene un modo de fallar que importa más que los otros: tocar lo que no era.** Por eso la mitad de los casos son de silencio — qué **no** se reescribe y por qué.

| Nivel | Objetivo | Ambiente |
|---|---|---|
| Unitarias | Qué se reescribe, qué no, y que el destino nunca cambie | Repositorios de mentira |
| Coherencia | Que el que reporta y el que arregla miren igual | Repositorio de mentira |
| Sobre el repo real | Cero entre carpetas, y ningún enlace roto | El repositorio |
| Regresión | Las dos suites | — |

**Técnicas:** repositorio de mentira con carpetas de verdad —la exclusión de `prompts/` depende de la ruta y sobre un árbol plano no se probaría—; comparación de lo reportado contra lo reparado; y `validar.py estandar` como red final, porque es el que sabe si un enlace resuelve.

---

## 5. Matriz de trazabilidad

| CA / exigencia | Caso | Estado |
|---|---|---|
| `RN-03` · el texto pasa a decir la ruta | [CP-001](#cp-001--el-texto-pasa-a-decir-la-ruta) | ☐ |
| Seguridad · el destino nunca cambia | [CP-002](#cp-002--el-destino-no-se-toca) | ☐ |
| Forma · la carpeta conserva su barra | [CP-003](#cp-003--la-carpeta-conserva-su-barra) | ☐ |
| Exclusión · texto descriptivo | [CP-004](#cp-004--el-texto-descriptivo-se-queda) | ☐ |
| Exclusión · palabras del usuario | [CP-005](#cp-005--prompts-no-se-toca) | ☐ |
| Exclusión · el vecino de la misma carpeta | [CP-006](#cp-006--el-vecino-se-deja-aparte) | ☐ |
| Ruido · el que ya está bien, el externo | [CP-007](#cp-007--lo-que-ya-está-bien-no-se-reescribe) | ☐ |
| Seguridad · simular no escribe | [CP-008](#cp-008--simular-no-escribe) | ☐ |
| Coherencia · reportar y arreglar | [CP-009](#cp-009--lo-que-se-repara-es-lo-que-se-reporta) | ☐ |
| Límite conocido · comillas invertidas | [CP-010](#cp-010--el-texto-entre-comillas-invertidas-no-se-ve) | ☐ |
| Sobre el repo real | [CP-011](#cp-011--cero-entre-carpetas-y-ningún-enlace-roto) | ☐ |

**Cobertura:** 11 de 11 = 100%.

---

## 6. Casos de prueba

### CP-001 — El texto pasa a decir la ruta

`[x.md](../../base/x.md)` → `[base/x.md](../../base/x.md)`.

### CP-002 — El destino no se toca

Tras reparar, el destino es **carácter por carácter el mismo**.

> Es lo único que puede romper un enlace que hoy funciona. Si este caso cae, el arreglo es peor que el defecto.

### CP-003 — La carpeta conserva su barra

`[area/](area/)` → `[doc/area/](area/)`, con la barra final.

### CP-004 — El texto descriptivo se queda

`[la guía](../base/x.md)` no se toca: la propia regla lo permite cuando quien lee ya sabe dónde vive.

### CP-005 — `prompts/` no se toca

Un enlace mal escrito dentro de `prompts/` **se queda como está**.

> Son palabras del usuario. Reescribirle un enlace ahí es editarle la frase. **Y la exclusión se prueba sobre carpetas de verdad**, porque se cuenta por la ruta: sobre un árbol plano el caso pasaría sin comprobar nada.

### CP-006 — El vecino se deja aparte

`[plan.md](plan.md)` no se toca por defecto; **pidiéndolo expresamente, sí**.

> Es lo que esta fase descubrió. La puerta queda abierta para el día que se decida, y cerrada mientras tanto.

### CP-007 — Lo que ya está bien no se reescribe

Ni el que ya dice la ruta, ni el enlace externo.

### CP-008 — Simular no escribe

Sin `escribir`, dice cuántos tocaría y no toca ninguno.

### CP-009 — Lo que se repara es lo que se reporta

Dos pasos: la cuenta de lo reportado **es** la de lo reparado; y después de reparar, **no queda nada que reportar**.

> Si el que reporta y el que arregla miran distinto, el arreglo deja hallazgos vivos o toca lo que nadie pidió. Es el caso que mantiene las dos mitades pegadas.

### CP-010 — El texto entre comillas invertidas no se ve

``[`x.md`](destino)`` **no se toca**, y el caso lo declara.

> `comun.enlaces()` borra los trozos entre comillas invertidas antes de buscar enlaces, y con eso el texto queda vacío: deja de parecer una ruta. **No es un defecto de esta fase** y quitarlo cambiaría cómo se leen los enlaces en todo el repositorio. Queda escrito para que se vea, en vez de descubrirlo dentro de un año preguntándose por qué el número no llegaba a cero.

### CP-011 — Cero entre carpetas, y ningún enlace roto

Sobre el repositorio real: `reparar_formato()` devuelve **cero**, y `validar.py estandar` no reporta ningún enlace roto.

> **No se exige cero total**, a propósito: los 747 vecinos esperan la decisión sobre `DOC14`. Exigir cero obligaría a aplicar lo que se acaba de revertir.

---

## 9. Gestión de defectos

| Severidad | Qué sería acá | Atención |
|---|---|---|
| **Crítica** | Romper un enlace, o escribir en `prompts/` | Inmediato |
| **Alta** | Que reportar y reparar se separen | Antes de cerrar |
| **Media** | La forma del texto reescrito | Se reporta |

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Enlaces rotos después de reparar | **0** |
| Archivos de `prompts/` tocados | **0** |
| Enlaces entre carpetas mal escritos | **0** |
| Diferencia entre lo reportado y lo reparado | **0** |
| Cobertura de exigencias | 100% — 11 de 11 |

Un solo concepto: **Cumple** o **No cumple**.
