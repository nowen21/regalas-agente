# HU-012 — Inventario de las acciones del agente y su riesgo

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | HU-012 |
| **Épica / Feature** | [EP-001 Cuerpo de reglas heredable](../epica.md) |
| **Módulo / Componente** | Capítulo `00 · Núcleo blindado` |
| **Tipo** | Funcional |
| **Prioridad** | Must |
| **Estimación** | M |
| **Sprint** | No aplica: el trabajo lo lleva una sola persona, sin sprints |
| **Solicitante** | Quien define el estándar |
| **Responsable** | Una sola persona cumple los roles de dueño de producto y líder técnico |
| **Estado** | Backlog |

---

## 2. Narrativa

- **Como** quien autoriza lo que el agente hace en su máquina
- **Quiero** la lista completa de lo que el agente puede hacer, cada cosa con qué tan difícil es deshacerla
- **Para** que la aprobación pese distinto según lo que se aprueba, y no se apruebe todo en bloque

---

## 3. Contexto y descripción

Nadie ha hecho esa lista. El [base/00-nucleo-blindado.md](../../../../base/00-nucleo-blindado.md) cubre los casos que alguien recordó: datos reales (`N4`), commit y push (`N2`), secretos (`N6`) y operaciones masivas (`N5`). Son los casos que dolieron. Lo que nunca se hizo fue enumerar qué más puede hacer el agente y preguntarse, por cada cosa, qué pasa si sale mal.

De ahí salen dos consecuencias.

**La primera:** hay acciones sin clasificar. Borrar un archivo que no está en git, reescribir la configuración de la máquina, correr un script del proyecto que sale a la red. Ninguna aparece en `N1` a `N6` por su nombre, así que caen en la regla general `N1` —ningún cambio de estado sin aprobación explícita— junto con cambiarle una coma a un README.

**La segunda, que es la grave:** un control que trata igual todo lo que toca se termina relajando de una sola vez. Cuando la misma exigencia cubre el cambio de coma y el borrado de la base, en la práctica se aprueba en bloque — y entonces también quedó aprobado el borrado. La rigidez pareja no protege más: protege menos.

**De dónde sale el criterio.** De los apuntes del diplomado, módulo 2, sobre administración de la IA: *«sin inventario no hay nada más»* y *«un modelo que ordena un catálogo y uno que niega un crédito no pueden tener el mismo control»*. Y de la lámina de sistemas autónomos: mientras la máquina sugiere, el error lo filtra una persona; cuando la máquina ejecuta, el error ya ocurrió. El agente de este repositorio ejecuta.

### 3.1 Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Existe una lista escrita de las clases de acción que el agente puede ejecutar |
| RN-02 | Cada clase de acción declara qué tan difícil es deshacerla, en una escala fija |
| RN-03 | De ese nivel sale qué necesita aprobación de una persona y qué no |
| RN-04 | Una acción que no está en la lista se trata como del nivel más alto hasta que se clasifique |
| RN-05 | La lista se revisa cuando el agente gana una herramienta nueva, no en una fecha del calendario |

### 3.2 Supuestos

- El conjunto de cosas que el agente puede hacer cambia poco, y cambia por herramienta nueva. Por eso la revisión se dispara con la herramienta y no con el tiempo.

### 3.3 Fuera de alcance

- Clasificar los modelos de IA de un proyecto. Eso reusa esta misma tabla de riesgo pero es el capítulo opt-in de [HU-013](../HU-013-capitulos-opt-in-de-dominio/HU-013-capitulos-opt-in-de-dominio.md).
- Construir la pieza que impide la acción. Acá se escribe la lista y el nivel; hacerla cumplir es de EP-005.

---

## 4. Criterios de aceptación

### CA-01 — La lista cubre todo lo que el agente puede hacer

```gherkin
Dado que el agente tiene un conjunto de herramientas
Cuando se recorre ese conjunto contra la lista
Entonces cada herramienta cae en al menos una clase de acción de la lista
Y ninguna queda sin clase
```

**Cómo validarlo:**

1. Escribir el conjunto de herramientas que el agente tiene hoy: leer, escribir un archivo del repositorio, borrar, correr un comando local, correr algo que sale a la red, tocar git, tocar datos, tocar la máquina fuera del repositorio, escribir en el histórico y escribir en la memoria.
2. Para cada una, buscar su clase en la lista del anexo.
3. Contar las que no tienen clase. Resultado esperado: cero.
- **Aprobado cuando:** las diez quedan clasificadas y el conteo de huérfanas es cero.

### CA-02 — Cada clase declara qué tan difícil es deshacerla

```gherkin
Dado que la lista tiene sus clases de acción
Cuando se lee cualquier fila
Entonces trae su nivel en la escala fija
Y trae el ejemplo concreto de qué pasa si sale mal
```

**Cómo validarlo:**

1. Abrir el anexo y recorrer la tabla fila por fila.
2. Comprobar que cada fila tiene los dos campos llenos, y que el nivel es uno de los valores de la escala — no un texto libre.
3. Buscar una fila donde el nivel esté puesto sin ejemplo. Resultado esperado: no existe.
- **Aprobado cuando:** ninguna fila tiene el nivel sin su ejemplo, y ningún nivel está fuera de la escala.

### CA-03 — Dos acciones de riesgo distinto no piden lo mismo

```gherkin
Dado que la lista clasifica una acción reversible y una que no lo es
Cuando se compara qué exige cada una
Entonces lo que exigen es distinto
```

**Cómo validarlo:**

1. Tomar dos filas de niveles opuestos — por ejemplo, corregir una coma en un README y borrar un archivo que no está en git.
2. Leer qué exige cada una antes de ejecutarse.
3. Comparar. Resultado esperado: la de nivel alto pide algo que la de nivel bajo no pide.
- **Aprobado cuando:** las dos exigencias son distintas. Si son iguales, la clasificación no sirvió de nada, que es el defecto que esta historia corrige.

### CA-04 — Lo que no está en la lista se trata como lo peor

```gherkin
Dado que el agente va a ejecutar una acción que la lista no nombra
Cuando busca su clase y no la encuentra
Entonces la trata con la exigencia del nivel más alto
Y lo dice
```

**Cómo validarlo:**

1. Inventar una acción que la lista no cubra.
2. Leer qué manda hacer el anexo en ese caso.
3. Resultado esperado: manda tratarla como del nivel más alto y anotarla para clasificarla.
- **Aprobado cuando:** el caso está escrito. Una lista sin esta cláusula deja el hueco abierto justo donde aparece lo que nadie previó.

### Criterios de aceptación transversales

- [ ] **Límites** — la acción que cae en dos clases, y la que la lista no nombra, tienen comportamiento definido.
- [ ] **No regresión** — `N1` a `N6` siguen vigentes tal como están; la lista los organiza, no los reemplaza.

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
| RNF-01 | **Trazabilidad** | Cada clase de acción cita la regla del núcleo que ya la cubría, si alguna la cubría |
| RNF-02 | **Claridad** | La escala tiene pocos niveles y cada uno se distingue por qué tan difícil es deshacer, no por qué tan grave suena |

---

## 6. Diseño y referencias

- **Mockup / Prototipo:** no aplica, es una tabla en un documento.
- **Documento funcional:** [documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/epica.md](../epica.md).
- **Contrato de API:** no aplica.
- **Modelo de datos afectado:** ninguno.

---

## 7. Tareas técnicas derivadas

- [ ] Escribir la lista de clases de acción como anexo del capítulo `00`.
- [ ] Definir la escala de reversibilidad y sus niveles.
- [ ] Clasificar cada clase y escribir su ejemplo de qué pasa si sale mal.
- [ ] Escribir qué exige cada nivel, de forma que dos niveles no exijan lo mismo.
- [ ] Escribir la cláusula de lo no clasificado.
- [ ] Versionar el cambio (`20·M10`).

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados: la fase declara qué CA cubre y aquí se nombra la fase con sus documentos.

| Fase (`02·F12.6`) | CA que cubre | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|
| — | — | — | — | — | Sin empezar |

**De dónde sale esta historia:** el [pendientes/13-inventario-y-riesgo-de-las-acciones-del-agente.md](../../../../pendientes/13-inventario-y-riesgo-de-las-acciones-del-agente.md).

**Qué documento responde qué**, para no buscar en el que no es:

| Pregunta | Documento |
|---|---|
| Qué se pide y cuándo se da por aceptado | Esta HU |
| Qué se va a hacer, en qué orden y sobre qué archivos | `plan_trabajo.md` de la fase |
| Con qué casos se comprueba cada CA | `plan_pruebas.md` de la fase |
| Qué se ejecutó, con qué resultado, y si el CA quedó cumplido | `resultado_pruebas.md` de la fase |
| En qué estación va y qué la tiene detenida | `estado-fase.md` de la fase |
| Qué quedó hecho al final | `funcionalidad_implementada.md` de la fase |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
| Dependencia | [HU-003](../HU-003-nucleo-que-no-se-sobrescribe/HU-003-nucleo-que-no-se-sobrescribe.md), porque el anexo cuelga del núcleo y el núcleo no se relaja | Alto |
| Riesgo | Que la escala se vuelva tan fina que clasificar cueste más que la acción | Pocos niveles, y el criterio es uno solo: qué tan difícil es deshacerla |
| Riesgo | Que bajar la exigencia de las acciones reversibles se lea como relajar el núcleo | Se escribe que `N1`–`N6` no cambian; lo que cambia es lo que hoy no está nombrado en ninguna |

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Dependencias identificadas
- [ ] Decidida la escala de niveles

## 11. Definition of Done (DoD)

- [ ] El anexo escrito, con su lista y su escala
- [ ] Los cuatro criterios de aceptación verificados
- [ ] `N1`–`N6` intactos y citados desde las filas que ya cubrían
- [ ] Versionada (`20·M10`)
- [ ] El pendiente 13 cerrado nombrando la fase

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | Sí | Es leer y escribir; no espera a ninguna construcción |
| **N**egociable | Sí | La escala y el corte de la aprobación se discuten |
| **V**aliosa | Sí | Desbloquea la clasificación de riesgo de [HU-013](../HU-013-capitulos-opt-in-de-dominio/HU-013-capitulos-opt-in-de-dominio.md) y el ítem 15 del pendiente 09 |
| **E**stimable | Sí | El alcance lo fija el conjunto de herramientas del agente |
| **S**mall (pequeña) | Sí | Una lista y una tabla |
| **T**esteable | Sí | Se cuenta cuántas acciones quedan sin clase |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-17 | Ing. José Dúmar Jiménez Ruíz | Creación de la HU, para que el pendiente 13 deje de estar suelto |
