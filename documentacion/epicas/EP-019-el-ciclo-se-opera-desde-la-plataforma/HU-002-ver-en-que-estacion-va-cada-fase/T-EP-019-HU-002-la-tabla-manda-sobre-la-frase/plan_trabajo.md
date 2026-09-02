# Plan de Trabajo — Fase `T-EP-019-HU-002-la-tabla-manda-sobre-la-frase` (módulo Ciclo de vida)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación. El requisito vive en la HU; las pruebas, en el `plan_pruebas`; lo que quedó hecho, en el `funcionalidad_implementada.md`.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `T-EP-019-HU-002-la-tabla-manda-sobre-la-frase` |
| **Épica** | [EP-019](../../epica.md) |
| **HU** | [HU-002 Ver en qué estación va cada fase](../HU-002-ver-en-que-estacion-va-cada-fase.md), una sola (`F12.1`) |
| **Módulo** | Ciclo de vida |
| **Especificación del módulo** | [documentacion/ciclo-de-vida/spec.md](../../../../ciclo-de-vida/spec.md) |
| **Fecha apertura** | 2026-09-01 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- 📋 **Ficha de `F-012`:** *«sirve para ver todas las fases a la vez: una sola se ve mirando su documento»*.
- 🩹 **Y el caso real:** este repositorio tiene **209 fases**. Nadie las ha mirado todas nunca, porque no había cómo.

> **El usuario autorizó ejecutar sin aprobar paso por paso** el 2026-09-01.

**CA de la HU que cubre esta fase:** los tres, todos ☑.

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** decir en qué estación va cada fase y qué puerta le falta, leyendo lo escrito.

**El estado lo fija lo escrito, no la opinión** (`RN-5` de la ficha). Un `estado-fase.md` lo dice dos veces —una frase y una tabla—, y manda la tabla.

**Fuera de alcance:** marcar las estaciones, que las marca quien hace el trabajo; y reescribir las fases viejas.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo que ya existe y se reutiliza:** los `estado-fase.md` que las 209 fases ya tienen escritos.

**Lo verificado, y es lo que cambió el diseño:** al leerlas todas salió que **107 no usan la tabla de trece estaciones** —83 traen once y 24 traen menos o ninguna— y que **76 cierran con `✅` en vez de `☑`**. Reconociendo solo `☑` daban 18 fases terminadas; reconociendo las dos, 76.

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/ciclo_de_vida/estaciones.py` | Crear | Servicio | Leer la tabla |
| `plataforma/nucleo/ciclo_de_vida/management/commands/en_que_va.py` | Crear | Consola | La orden |
| `plataforma/nucleo/ciclo_de_vida/tests_operacion.py` | Modificar | Prueba | Los tres CA |
| `documentacion/ciclo-de-vida/spec.md` | Modificar | Especificación | Su §13 |

**Ninguna entidad y ninguna migración:** el estado está en el texto, `DA-01`.

### 2.2 Matriz de dependencias del refactor

**Nada existente se toca.** Esta fase solo lee.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican: órdenes de consola.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **Manda la tabla sobre la frase** | Creerle a la frase, que es más fácil de leer | La frase se actualiza a mano y la tabla también, pero la tabla es la que se marca al hacer el trabajo |
| **Las dos marcas valen: `☑` y `✅`** | Reescribir las 76 fases viejas | Reescribir una fase cerrada es peor que tener dos marcas. El que se adapta es el que lee |
| **«Sin marcar» no es «pendiente»** | Contarlas como pendientes | Las fases viejas escriben qué pasó con la estación en vez de marcarla; decir que está pendiente inventa un estado que nadie declaró |
| **Solo se compara si la tabla es de trece** | Comparar siempre | La estación 12 de una tabla de once no existe, y la de trece quiere decir otra cosa |
| **La menos avanzada sale primero** | Ordenar por nombre | Lo que hay que mirar primero es lo que lleva más tiempo sin moverse |

### 2.7 Dudas por resolver antes de codificar

Ninguna al empezar. **Las tres que aparecieron salieron de correrlo**, no de pensarlo: los dos modelos, las dos marcas y la casilla sin marcar.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | Leer la tabla de estaciones | Servicio | 1,5 h | — | CA-01 | EV-01 |
| T-02 | Aceptar las dos marcas de cumplida | Servicio | 30 min | T-01 | CA-01 | EV-01 |
| T-03 | Separar «sin marcar» de «pendiente» | Servicio | 1 h | T-01 | CA-02 | EV-01 |
| T-04 | Comparar la frase solo si el modelo coincide | Servicio | 1 h | T-01 | Transversal | EV-01 |
| T-05 | Decir desde cuándo, y cuándo no se sabe | Servicio | 1 h | T-01 | CA-03 | EV-01 |
| T-06 | La orden de consola, con el resumen | Consola | 1 h | T-05 | — | EV-01 |
| T-07 | Las pruebas de los tres CA | Test | 2 h | T-06 | Todos | EV-01 |

**Total estimado:** 8 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-04 → T-07. Las tres primeras salieron al correrlo contra las fases reales, no antes.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Con tablas de trece, de once y con las dos marcas | EV-01 | 2026-09-01 | ☑ |
| CA-02 | Mirando la puerta que sale | EV-01 | 2026-09-01 | ☑ |
| CA-03 | Con una fase con fecha y otra sin ella | EV-01 | 2026-09-01 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas de la fase | `plataforma/nucleo/ciclo_de_vida/tests_operacion.py` |

---

## 6. Datos y ambiente de prueba

Tablas de estaciones de mentiras, de trece y de menos, con las dos marcas. Y **la corrida contra las 209 fases reales del repositorio**, que es de solo lectura.

---

## 7. Reversión / rollback  ·  Q11

**Estas dos fases solo leen.** Se quita el archivo y no queda rastro; ninguna fase del repositorio se modifica.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna migración, ninguna dependencia nueva.

---

## 9. Reglas aplicadas  ·  Q13

- Base: `03·DA-01` (el texto es la verdad) y el capítulo [`15`](../../../../../base/15-registros-inmutables.md), porque ninguna fase cerrada se reescribe.
- Producto: las `RN-1` a `RN-6` de la historia.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | **Acusar de contradicción a una fase de otro modelo** | **Alto: 107 fases acusadas en falso** | Solo se compara cuando la tabla es de trece | Cerrado |
| B-02 | **Dar por pendiente una fase que solo no marcó** | Alto | «Sin marcar» tiene su propio nombre | Cerrado |
| B-03 | Contar como sin cerrar a las que usan `✅` | Alto | Las dos marcas valen | Cerrado |
| B-04 | Que queden 33 fases con la frase y la tabla en desacuerdo | Medio | **Se declara:** son reales, y arreglarlas es reescribir fases cerradas | Declarado |

---

## 11. Definition of Done

- [x] Los tres CA verificados con evidencia
- [x] Corrido contra las 209 fases reales
- [x] Ninguna fase cerrada reescrita
- [x] Las dos baterías en verde
- [x] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
