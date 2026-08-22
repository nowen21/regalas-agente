# Plan de Pruebas — Fase A-EP-001-HU-005-retrodocumentar-las-convenciones-agnosticas   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-001-HU-005 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-001-HU-005-retrodocumentar-las-convenciones-agnosticas` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md)).

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Lectura del cuerpo de reglas | Que en los diecisiete capítulos no aparezca ningún nombre propio de tecnología | Este repositorio | No — la fila 5 del checklist pide leer |
| Contraste entre proyectos | Que la misma convención se cumpla en dos proyectos de lenguajes distintos | Copia local de los dos proyectos, solo lectura | No |
| Revisión de marcas | Que los capítulos opcionales lleven la marca de la lista cerrada | Este repositorio | Parcial — `validar.py estandar` mira la forma de la cabecera |

**Por qué nada de esto lo cierra un programa.** Los tres CA son de los que la fila 4 y la fila 5 del [checklist](../../../../../base/20-meta-reglas/checklist.md) mandan **leer**: un tema se repite aunque cambien las palabras, y una convención puede nombrar un stack sin escribir su nombre. Buscar cadenas encontraría lo obvio y dejaría pasar lo que importa.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los tres CA |
| Compatibilidad | ☑ | El CA-01: la misma convención en dos lenguajes distintos |
| Documento | ☑ | Los CA-02 y CA-03, que son propiedades del cuerpo de texto |
| No regresión | ☐ | No aplica: la fase no toca `base/`, solo lee y anota |

### 3.3 Técnicas de diseño de casos

- **Dos proyectos reales, no de juguete** — un proyecto de juguete cumple cualquier convención porque no tiene código donde la convención estorbe. Los dos proyectos los elige la duda 1 del plan.
- **Criterio escrito antes de llenar la tabla** — el riesgo `R-02`: la tabla tema → capítulo dueño se llena con un criterio fijado de antemano, y cada fila cita el párrafo que la sostiene. Si no, dos personas la llenarían distinto y el CA-02 quedaría a gusto de quien lo revisa.
- **Recorrido exhaustivo, no muestreo** — los diecisiete capítulos se recorren enteros buscando nombre de lenguaje, framework, motor, nube o herramienta. Cada aparición se anota con su archivo y su línea.
- **Hallazgo numerado, no corregido** — lo que aparezca mal se lista con número para poder citarlo desde otra fase ([procedimiento de retro-documentación](../../../../../base/13-documentacion/retrodocumentacion.md), paso 5). Corregir al pasar sería salirse del CA ([`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)).

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validar.py estandar` y `enlaces` sobre este repositorio, como línea base. Los dos proyectos del CA-01 **no se corren**: se leen.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-005 | [CA-01](../HU-005-convenciones-de-ingenieria.md#ca-01--una-convención-sirve-igual-en-dos-proyectos-de-lenguajes-distintos) | [CP-001](#cp-001--la-misma-convención-se-cumple-en-dos-proyectos-de-lenguajes-distintos), [CP-002](#cp-002--ningún-capítulo-nombra-una-tecnología) | Compatibilidad | Crítica | No | ☐ |
| HU-005 | [CA-02](../HU-005-convenciones-de-ingenieria.md#ca-02--un-tema-no-aparece-en-dos-capítulos) | [CP-003](#cp-003--cada-tema-tiene-un-solo-capítulo-dueño) | Documento | Alta | No | ☐ |
| HU-005 | [CA-03](../HU-005-convenciones-de-ingenieria.md#ca-03--una-convención-que-solo-sirve-a-cierto-tipo-de-proyecto-queda-marcada-como-opcional) | [CP-004](#cp-004--lo-opcional-está-marcado-y-no-encenderlo-no-es-incumplir) | Documento | Alta | Parcial | ☐ |

**Cobertura:** 3 de 3 CA = 100%.

---

## 6. Casos de prueba

### CP-001 — La misma convención se cumple en dos proyectos de lenguajes distintos

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-01 |
| **Tipo** | Compatibilidad |
| **Prioridad** | Crítica |
| **Precondiciones** | La duda 1 resuelta: los dos proyectos elegidos y sus lenguajes, y las convenciones que se ponen a prueba |
| **Datos de entrada** | Copia local de los dos proyectos, en solo lectura |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Tomar la convención elegida del capítulo que la manda | Queda a la vista, con su capítulo e identificador |
| 2 | Buscar cómo la cumple el primer proyecto | Se cumple, y lo que cambia está declarado en su capa 3 |
| 3 | Buscar cómo la cumple el segundo, de otro lenguaje | Se cumple igual, con su propia capa 3 |
| 4 | Comparar los dos: qué exige el capítulo y qué pone cada proyecto | Lo que exige el capítulo es lo mismo; lo que cambia es solo de la capa 3 |
| 5 | Comprobar que no se escribió nada en ninguno de los dos | Ningún archivo modificado |

**Resultado esperado final:** la convención vive en la capa 2 sin arrastrar stack, que es lo que exige [`20·M3`](../../../../../base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md).

> **El paso 4 es el que decide.** Que los dos proyectos cumplan no basta: si el capítulo dijera cómo se cumple en vez de qué se exige, uno de los dos estaría forzando su stack sobre el otro.

---

### CP-002 — Ningún capítulo nombra una tecnología

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-01 |
| **Tipo** | Documento |
| **Prioridad** | Crítica |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Los diecisiete capítulos, del `03` al `19` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Listar los diecisiete capítulos que se van a recorrer | Queda el listado, y son diecisiete |
| 2 | Recorrer cada uno buscando nombre de lenguaje, framework, motor, nube o herramienta | Cada aparición queda anotada con su archivo y su línea |
| 3 | Separar las que son ejemplo declarado de las que exigen | Las que exigen son hallazgo; las que ilustran, no |
| 4 | Numerar los hallazgos, sin corregir ninguno | Quedan citables desde otra fase |

**Resultado esperado final:** o el cuerpo está limpio, o queda dicho exactamente dónde no lo está.

> **El paso 3 es el que evita el falso positivo.** Un capítulo puede nombrar una herramienta para ilustrar sin exigirla; lo que rompe el CA es exigirla.

---

### CP-003 — Cada tema tiene un solo capítulo dueño

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-02 |
| **Tipo** | Documento |
| **Prioridad** | Alta |
| **Precondiciones** | El criterio de "qué cuenta como el mismo tema" escrito **antes** de llenar la tabla (riesgo `R-02`) |
| **Datos de entrada** | La tabla tema → capítulo dueño levantada en la tarea T-04 |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir el criterio de qué cuenta como el mismo tema | Queda fijado antes de mirar los capítulos |
| 2 | Levantar la tabla tema → capítulo dueño | Cada fila cita el párrafo que la sostiene |
| 3 | Aislar los temas que aparecen en dos capítulos | Queda la lista de candidatos a solape |
| 4 | Por cada candidato, ver si la segunda aparición **enlaza** o **repite** | Enlazar está bien ([`20·M2`](../../../../../base/20-meta-reglas/reglas/M2-un-tema-un-capitulo-un-dueno.md)); repetir es hallazgo |
| 5 | Numerar las repeticiones, sin corregirlas | Quedan citables |

**Resultado esperado final:** el solape queda medido con un criterio escrito, no con una impresión.

---

### CP-004 — Lo opcional está marcado, y no encenderlo no es incumplir

| Campo | Valor |
|---|---|
| **HU / CA** | HU-005 / CA-03 |
| **Tipo** | Documento |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Los cinco capítulos `opt-in` (`15` a `19`) y los doce restantes |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Comprobar que los cinco llevan la marca de la lista cerrada en su cabecera | Los cinco, con la misma marca |
| 2 | Tomar un proyecto que no los enciende y correr `validar.py estandar` sobre él | Ninguna falla por no encenderlos |
| 3 | Revisar los doce capítulos sin marca, uno por uno | Ninguno sirve solo a cierto tipo de proyecto; el que lo haga queda anotado |
| 4 | Numerar lo anotado en el paso 3, sin corregirlo | Queda citable desde otra fase |

**Resultado esperado final:** lo opcional se distingue de lo obligatorio, y no encenderlo no deja al proyecto en falta.

> **El paso 2 es el que le da valor al 1.** Que la marca esté escrita no prueba que sirva: lo que prueba el CA es que el proyecto que no la enciende no queda incumpliendo.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que un capítulo de capa 2 exija una tecnología concreta | Se numera como hallazgo. **Corregirlo es otra fase**: esta retrodocumenta, no limpia |
| **Alta** | Que un tema esté escrito completo en dos capítulos en vez de enlazado | Se numera y se propone quién debería ser el dueño |
| **Media** | Que un capítulo sin marca resulte ser de cierto tipo de proyecto | Se numera; ponerle la marca cambia `base/` y lo decide el usuario |
| **Baja** | Que el recorrido encuentre nombres de tecnología en ejemplos declarados | No es hallazgo; se deja anotado por qué no lo es |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 3 CA con caso |
| Casos ejecutados | 4 de 4 |
| Capítulos recorridos | 17 de 17 |
| Archivos modificados en los dos proyectos del CA-01 | **0** — la prueba es de lectura |
| Archivos de `base/` modificados por esta fase | **0** |
| Hallazgos | Los que salgan, todos numerados y ninguno corregido acá |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
