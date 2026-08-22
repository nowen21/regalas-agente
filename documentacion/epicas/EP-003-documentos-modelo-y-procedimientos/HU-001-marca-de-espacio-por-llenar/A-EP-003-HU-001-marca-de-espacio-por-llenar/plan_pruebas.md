# Plan de Pruebas — Fase A-EP-003-HU-001-marca-de-espacio-por-llenar

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó al correrlas va en el [resultado_pruebas.md](resultado_pruebas.md) de esta misma fase. La lista de tareas vive en el [plan_trabajo.md](plan_trabajo.md).

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-003-HU-001 |
| **Versión** | 1.1 |
| **Alcance del plan** | Fase `A-EP-003-HU-001-marca-de-espacio-por-llenar` |
| **Fecha** | 2026-08-14 |
| **Elaborado por** | Ing. José Dúmar Jiménez Ruíz |
| **Estado** | Borrador |

> **Proporcionalidad.** Es una sola fase de una HU pequeña, así que se llenan solo las secciones 3, 5, 6, 9 y 12, como manda la plantilla. Inflarla con un plan de release sería ruido.

## Control de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0 | 2026-08-14 | Versión aprobada |
| 1.1 | 2026-08-14 | CP-002 no se podía juzgar: decía "los que se declaró" sin decir dónde, así que quien ejecutaba decidía la lista. Ahora enlaza la declaración y dice que un archivo en cero fuera de esa lista reprueba. El título pasa de "las 30 plantillas" a "todo modelo", porque cuatro archivos de la carpeta no son modelos |

---

## 3. Estrategia de pruebas

Lo que se entrega es texto: una regla y unas plantillas. No hay código que ejecutar, así que **la prueba es lectura y recuento**, no una suite. Eso no la hace menos verificable: los tres criterios se comprueban contando marcas y leyendo, y los dos resultados se pueden repetir.

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Lectura | Que la marca se vea sin buscarla | El repositorio | No |
| Recuento | Que sea la misma en las 30 plantillas y que no aparezca ninguna otra | El repositorio | Parcial: `grep` cuenta, la persona decide |
| Regresión | Que la corrida de comprobaciones del estándar siga en verde | El repositorio | Sí |

**Tipos que aplican:** funcional (los tres CA) y usabilidad (que la marca no estorbe la lectura). No aplican seguridad, rendimiento, migración de datos ni recuperación: no hay datos ni servicio.

**Alcance de la corrida automatizada ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)):** solo `python validadores/validar.py estandar`. No se corre la suite entera "por si acaso".

---

## 5. Matriz de trazabilidad

> Ningún criterio de aceptación puede quedar sin al menos un caso de prueba.

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-001 | [CA-01](../HU-001-marca-de-espacio-por-llenar.md#ca-01--la-marca-se-ve-y-se-distingue-del-texto) | [CP-001](#cp-001--la-marca-se-ve-sin-buscarla) | Funcional | Crítica | No | ☐ |
| HU-001 | [CA-02](../HU-001-marca-de-espacio-por-llenar.md#ca-02--todos-los-modelos-usan-la-misma-marca) | [CP-002](#cp-002--todo-modelo-usa-la-misma-marca), [CP-003](#cp-003--no-sobrevive-ninguna-marca-de-las-descartadas) | Funcional | Crítica | Parcial | ☐ |
| HU-001 | [CA-03](../HU-001-marca-de-espacio-por-llenar.md#ca-03--un-documento-con-marcas-sin-llenar-no-se-da-por-terminado) | [CP-004](#cp-004--un-documento-con-marcas-sin-llenar-no-está-terminado) | Funcional | Alta | No | ☐ |
| HU-001 | [RNF-01](../HU-001-marca-de-espacio-por-llenar.md#5-requisitos-no-funcionales) | [CP-005](#cp-005--la-marca-no-estorba-la-lectura-ni-rompe-la-corrida) | Usabilidad | Alta | No | ☐ |
| HU-001 | [RNF-02](../HU-001-marca-de-espacio-por-llenar.md#5-requisitos-no-funcionales) | [CP-003](#cp-003--no-sobrevive-ninguna-marca-de-las-descartadas) | Funcional | Crítica | Parcial | ☐ |
| HU-001 | [RNF-03](../HU-001-marca-de-espacio-por-llenar.md#5-requisitos-no-funcionales) | [CP-002](#cp-002--todo-modelo-usa-la-misma-marca) | Funcional | Crítica | Parcial | ☐ |

**Cobertura:** 6 de 6 = 100%. Tres criterios de aceptación y tres requisitos no funcionales.

---

## 6. Casos de prueba

### CP-001 — La marca se ve sin buscarla

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / [CA-01](../HU-001-marca-de-espacio-por-llenar.md#ca-01--la-marca-se-ve-y-se-distingue-del-texto) |
| **Tipo** | Funcional — camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | La regla escrita y las plantillas pasadas a la marca acordada |
| **Datos de entrada** | Tres plantillas de tamaños distintos: `plantillas/ciclo-vida-proyectos/04-HU.md`, `plantillas/ciclo-vida-proyectos/03-epica.md` y `plantillas/senales.md` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir cada una y recorrerla de arriba abajo una sola vez | Se pueden señalar los huecos sin volver atrás |
| 2 | Contar los huecos a ojo | Sale un número |
| 3 | Contarlos otra vez buscando la marca con `grep` | El mismo número del paso 2 |

**Resultado esperado final:** los dos recuentos coinciden en las tres plantillas.

### CP-002 — Todo modelo usa la misma marca

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / [CA-02](../HU-001-marca-de-espacio-por-llenar.md#ca-02--todos-los-modelos-usan-la-misma-marca) |
| **Tipo** | Funcional — cobertura |
| **Prioridad** | Crítica |
| **Precondiciones** | T-04 a T-07 hechas |
| **Datos de entrada** | Todos los archivos de `plantillas/`, incluidos `planes/`, `prompts/` y `CLAUDE.md.plantilla` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Contar la marca acordada en cada archivo | Ningún archivo con huecos queda en cero |
| 2 | Anotar los que dan cero | Solo quedan los que [`notas/marca-del-espacio-por-llenar.md`](../../../../../notas/marca-del-espacio-por-llenar.md) declara sin huecos, con su motivo escrito. Un archivo en cero que no esté en esa lista reprueba el caso |

### CP-003 — No sobrevive ninguna marca de las descartadas

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / [CA-02](../HU-001-marca-de-espacio-por-llenar.md#ca-02--todos-los-modelos-usan-la-misma-marca) |
| **Tipo** | Funcional — negativo |
| **Prioridad** | Crítica |
| **Precondiciones** | Las mismas de CP-002 |
| **Datos de entrada** | Las cuatro marcas descartadas: `[texto]`, `<texto>`, `{{texto}}`, `XXX` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar cada una en `plantillas/` | Los únicos aciertos son enlaces de markdown, casillas `[ ]` y sintaxis de comandos |
| 2 | Revisar acierto por acierto | Ninguno es un hueco del modelo |

> Este caso es el que protege del falso positivo: si no se distingue el hueco de la sintaxis, el programa de EP-004 va a reportar de más.

### CP-004 — Un documento con marcas sin llenar no está terminado

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / [CA-03](../HU-001-marca-de-espacio-por-llenar.md#ca-03--un-documento-con-marcas-sin-llenar-no-se-da-por-terminado) |
| **Tipo** | Funcional — negativo |
| **Prioridad** | Alta |
| **Precondiciones** | La regla escrita, con la condición de terminado |
| **Datos de entrada** | Una copia de `plantillas/senales.md` llenada dejando dos marcas a propósito |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Presentar la copia como terminada | La regla dice que no lo está y se puede señalar cuáles son las dos |
| 2 | Reemplazar las dos marcas | Ahora sí se puede dar por terminado |
| 3 | Dejar una sección que no aplica con la marca puesta | Sigue sin estar terminado: lo que se escribe en ese caso está definido |

### CP-005 — La marca no estorba la lectura ni rompe la corrida

| Campo | Valor |
|---|---|
| **HU / CA** | HU-001 / [RNF-01](../HU-001-marca-de-espacio-por-llenar.md#5-requisitos-no-funcionales) |
| **Tipo** | Usabilidad y regresión |
| **Prioridad** | Alta |
| **Precondiciones** | Todas las tareas hechas |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer completa una plantilla ya pasada | La marca no interrumpe la frase donde está |
| 2 | Correr `python validadores/validar.py estandar` | Las fallas son las mismas de antes de la fase, ni una más |

---

## 9. Gestión de defectos

| Severidad | Qué sería, acá | Atención |
|---|---|---|
| **Crítica** | Una plantilla queda con dos marcas distintas, o la regla no permite decidir si algo es hueco | Antes de cerrar la fase |
| **Alta** | Un hueco sin marcar en una plantilla | Antes de cerrar la fase |
| **Media** | La marca queda en un sitio donde estorba la lectura | Se anota y se corrige en la misma fase |
| **Baja** | Diferencia de estilo al escribir el texto dentro de la marca | Backlog |

Se registran en el [resultado_pruebas.md](resultado_pruebas.md), no acá.

---

## 12. Métricas e informe

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de criterios | CA con caso / CA totales | 100% |
| Plantillas con una sola marca | Archivos conformes / archivos con huecos | 100% |
| Marcas descartadas sobrevivientes | Aciertos que sí eran huecos | 0 |
| Fallas nuevas en la corrida del estándar | Fallas después − fallas antes | 0 |

El resultado de medirlas va en el [resultado_pruebas.md](resultado_pruebas.md). Este plan dice **qué** se mide; aquel dice **cuánto dio**.
