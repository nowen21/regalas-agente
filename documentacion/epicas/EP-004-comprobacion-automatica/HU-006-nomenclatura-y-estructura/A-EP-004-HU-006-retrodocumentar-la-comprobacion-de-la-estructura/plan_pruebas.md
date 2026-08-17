# Plan de Pruebas — Fase A-EP-004-HU-006-retrodocumentar-la-comprobacion-de-la-estructura   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-004-HU-006 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-004-HU-006-retrodocumentar-la-comprobacion-de-la-estructura` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/planes/pruebas.md)).

**Nada se rompe en el árbol real.** Los casos negativos se arman en carpeta temporal: romper una fase del repositorio lo dejaría en rojo para las demás sesiones.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Negativa | Que el nombre mal armado, el hueco en el consecutivo y la fase incompleta se reporten | Carpetas temporales | Sí |
| Positiva | Que el nombre con complemento válido y el consecutivo sin hueco **no** se reporten | Carpetas temporales | Sí |
| Medición | Que la cuenta de avisos de hoy quede anotada con su fecha | Este repositorio | Parcial |

**Qué queda declarado como no comprobable.** Las partes de [`02·F12`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md) que piden criterio — sobre todo `F12.10`, que una fase represente trabajo real. Una comprobación que se equivoca vale menos que ninguna.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los tres CA |
| Negativa | ☑ | Los tres se prueban con su caso roto |
| Límites | ☑ | El complemento en el nombre, que es el que se confunde con un nombre mal armado |
| No regresión | ☑ | La suite que ya existe, contra su número anotado antes |

### 3.3 Técnicas de diseño de casos

- **Cada CA con su par** — roto y sano. El complemento válido junto al nombre mal armado, el consecutivo con hueco junto al sin hueco, la fase incompleta junto a la completa. Solo el par distingue "lo detecta" de "reporta siempre".
- **Se lee primero qué cubre la suite** — el riesgo `R-02`: antes de escribir se revisa qué prueba ya existe, y se escriben solo las que falten.
- **La cuenta se toma al final** — el riesgo `R-01`: los avisos cambian mientras se trabaja porque se abren fases. Se cuenta al cerrar y se escribe **contra qué día**.
- **Lo que no se comprueba, dicho** — las partes de `F12` que piden criterio quedan declaradas como no comprobables, en vez de simuladas con una comprobación aproximada.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera y `validar.py fases` sobre este repositorio y sobre las carpetas temporales.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-006 | [CA-01](../HU-006-nomenclatura-y-estructura.md#ca-01--un-identificador-fuera-de-convención-se-reporta) | [CP-001](#cp-001--el-nombre-mal-armado-se-reporta-y-el-que-lleva-complemento-válido-no) | Límites | Alta | Sí | ☐ |
| HU-006 | [CA-02](../HU-006-nomenclatura-y-estructura.md#ca-02--un-hueco-en-la-numeración-se-reporta) | [CP-002](#cp-002--el-hueco-en-el-consecutivo-se-reporta-y-el-consecutivo-seguido-no) | Negativa | Alta | Sí | ☐ |
| HU-006 | [CA-03](../HU-006-nomenclatura-y-estructura.md#ca-03--una-fase-sin-sus-documentos-se-reporta) | [CP-003](#cp-003--la-fase-incompleta-se-reporta-diciendo-qué-le-falta) | Negativa | Crítica | Sí | ☐ |
| HU-006 | RNF — que quede dicho qué no se comprueba | [CP-004](#cp-004--lo-que-el-programa-no-comprueba-queda-declarado-y-la-cuenta-fechada) | Documento | Media | No | ☐ |

**Cobertura:** 3 de 3 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — El nombre mal armado se reporta, y el que lleva complemento válido no

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-01 |
| **Tipo** | Límites |
| **Prioridad** | Alta |
| **Precondiciones** | Carpeta temporal |
| **Datos de entrada** | Una fase con el nombre mal armado y otra con complemento válido |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Armar una fase con el identificador fuera de convención | Queda armada |
| 2 | Correr `validar.py fases` sobre la carpeta | Sale el hallazgo, y dice qué está mal del nombre |
| 3 | Armar una fase con complemento válido en el nombre | Queda armada |
| 4 | Correr sobre ella | **No** sale hallazgo |
| 5 | Comprobar que la corrida no escribió nada | Ningún archivo modificado |

**Resultado esperado final:** la convención se comprueba sin castigar la variante que la convención admite.

> **El paso 4 es el que evita el falso positivo.** El complemento es justo lo que se confunde con un nombre mal armado.

---

### CP-002 — El hueco en el consecutivo se reporta, y el consecutivo seguido no

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-02 |
| **Tipo** | Negativa |
| **Prioridad** | Alta |
| **Precondiciones** | Carpeta temporal |
| **Datos de entrada** | Una HU con fases `A` y `C`, y otra con `A` y `B` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Armar la HU con fases `A` y `C` | Queda armada |
| 2 | Correr `validar.py fases` | Sale el hallazgo del hueco |
| 3 | Armar la HU con `A` y `B` | Queda armada |
| 4 | Correr sobre ella | No sale hallazgo |
| 5 | Armar una con dos fases `A` repetidas | Sale el hallazgo de la repetición |

**Resultado esperado final:** el consecutivo no se salta ni se repite, y las dos formas de romperlo se detectan.

---

### CP-003 — La fase incompleta se reporta, diciendo qué le falta

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-03 |
| **Tipo** | Negativa |
| **Prioridad** | Crítica |
| **Precondiciones** | Carpeta temporal |
| **Datos de entrada** | Una fase con solo su plan de trabajo, y otra con sus cinco documentos |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Armar la fase con solo su plan | Queda armada |
| 2 | Correr `validar.py fases` | Sale el hallazgo, y **nombra los cuatro que faltan** |
| 3 | Armar la fase completa | Queda armada |
| 4 | Correr sobre ella | No sale hallazgo |
| 5 | Ir agregando documentos de a uno y correr en cada paso | El hallazgo se achica hasta desaparecer |

**Resultado esperado final:** el aviso dice qué falta, no solo que falta algo.

> **El paso 5 es lo que hace útil el aviso.** Un hallazgo que solo dice "incompleta" obliga a abrir la carpeta a mano.

---

### CP-004 — Lo que el programa no comprueba queda declarado, y la cuenta fechada

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / RNF |
| **Tipo** | Documento |
| **Prioridad** | Media |
| **Precondiciones** | Los tres casos anteriores corridos |
| **Datos de entrada** | Las partes de `F12` y la corrida sobre este repositorio |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Listar las partes de `F12` y cuáles comprueba el programa | Cada una con su veredicto |
| 2 | Declarar como no comprobables las que piden criterio, empezando por `F12.10` | Quedan escritas, no simuladas |
| 3 | Correr `validar.py fases` sobre este repositorio **al final de la fase** | Sale la cuenta de avisos |
| 4 | Anotar esa cuenta con la fecha del día | Queda la línea base fechada |

**Resultado esperado final:** hay contra qué comparar, y queda claro qué parte de la regla no la vigila nadie.

> **La cuenta se toma al final a propósito.** Los avisos cambian mientras se trabaja, porque se abren fases; una cuenta tomada al empezar nacería vieja.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que una fase incompleta pase sin hallazgo | Inmediato. El CA-03 queda en «No» |
| **Alta** | Que el complemento válido se reporte como nombre mal armado | Inmediato — el aviso se vuelve ruido y deja de leerse |
| **Media** | Que el hallazgo diga "incompleta" sin decir qué falta | Antes de cerrar |
| **Media** | Que las pruebas nuevas repitan las que ya están (riesgo `R-02`) | Se lee primero qué cubre la suite |
| **Baja** | Que la cuenta de avisos cambie mientras se trabaja | Se cuenta al final y se escribe contra qué día |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 3 CA y los RNF con caso |
| Casos ejecutados | 4 de 4 |
| Fases del árbol real rotas para probar | **0** |
| Partes de `F12` con su veredicto de comprobabilidad | Todas |
| Cuenta de avisos | Anotada, con la fecha del día |
| Pruebas de la suite | Las de la línea base, más las nuevas, todas en verde |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
