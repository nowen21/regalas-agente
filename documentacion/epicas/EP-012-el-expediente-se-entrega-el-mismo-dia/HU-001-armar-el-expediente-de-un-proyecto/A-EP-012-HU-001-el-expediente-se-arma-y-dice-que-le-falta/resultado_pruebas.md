# Resultado de Pruebas — Fase `A-EP-012-HU-001-el-expediente-se-arma-y-dice-que-le-falta`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué resultado y si cada criterio quedó cumplido**. Los casos están en el [plan_pruebas.md](plan_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-012-HU-001-el-expediente-se-arma-y-dice-que-le-falta` |
| **HU** | [documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/HU-001-armar-el-expediente-de-un-proyecto/HU-001-armar-el-expediente-de-un-proyecto.md](../HU-001-armar-el-expediente-de-un-proyecto.md) |
| **Fecha de ejecución** | 2026-08-31 |
| **Ejecutó** | El agente, sobre lo traído de este repositorio |
| **Ciclo** | 1 |

---

## 1. Resumen de la ejecución

| | Cuántos |
|---|---|
| Casos del plan | 6 |
| Ejecutados | 6 |
| Pasaron | 6 |
| Fallaron | 0 |
| Pruebas automáticas nuevas | **20** |

**El expediente de este repositorio, armado:**

```
Planificación                     9 documento(s)
Análisis de requisitos            1
Diseño                            4
Especificaciones de módulo        5
Épicas                           11
Historias de usuario            112
Fases                           619
Registros de versión              1

762 documento(s) en el expediente.

Falta: 22
A medio llenar: 31
No encaja en ningún grupo: 0
Fuera del alcance pedido: 0
```

---

## 2. Ejecución caso por caso

### CP-001 — El orden es el del ciclo

Entre grupos sale planificación, diseño y épicas en ese orden.

**Dentro de una fase, el primer intento salió mal**, y la prueba lo cazó: los cinco documentos salían por nombre de archivo —el estado y el cierre antes que el plan—, que es exactamente el orden del disco que el criterio descarta. Se corrigió ordenando por la posición del tipo dentro de su grupo.

Un proyecto sin documentos devuelve las listas en cero y lo dice.

**Resultado: pasa.**

### CP-002 — Lo que falta se nombra, y no se inventa

Con una fase a la que le falta el estado: aparece en la lista con qué documento y de qué fase, el expediente trae cuatro y no cinco, y **el ausente no entra vacío**. Una fase completa no reporta nada.

**Sobre lo real, la lista dice algo que nadie había visto: 22 faltantes**, y los 22 son el mismo documento —`funcionalidad implementada`— en fases de retro-documentación viejas.

**Resultado: pasa.**

### CP-003 — Lo incompleto se marca, y una cita no es un hueco

| Entrada | Salió |
|---|---|
| Dos marcas de la casa | 2 huecos |
| Un documento lleno | 0 |
| Una cita entre comillas angulares | **0** |
| Dos documentos con distinto número | de más a menos |

**Y este caso encontró el defecto que más habría dolido.** La primera versión contaba como hueco cualquier texto entre comillas angulares, y en esta casa se cita así todo el tiempo: **559 documentos salían «a medio llenar»**. Contando solo la marca que `13·DOC19` fija, quedan **31**.

**Resultado: pasa.**

### CP-004 — La memoria no entra

Las señales no aparecen, el índice de una carpeta tampoco, y **ninguno de los dos se reporta como «no encaja»**: se excluyen a propósito, y meterlos en esa lista los haría ver como un defecto del proyecto.

**Resultado: pasa.**

### CP-005 — El alcance acotado dice qué dejó fuera

Completo trae diez documentos de dos fases; acotado hasta la primera trae cinco, y **lista los cinco que dejó fuera con su fase**. Y no reporta como faltante lo que se pidió no mirar.

**Resultado: pasa.**

### CP-006 — Armar no toca nada

Retrato de la carpeta antes y después: idénticos.

**Resultado: pasa.**

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| Qué se miró | Resultado |
|---|---|
| Los 22 faltantes | Son reales: `funcionalidad implementada` que esas fases nunca escribieron |
| Los 31 a medio llenar | La mayoría son de verdad. **Algunos son documentos que hablan de la marca**, y por eso la traen escrita: es el mismo caso de nombrar contra ser que ya apareció en el mapa del amarre |
| La lista de lo que no encaja | Vacía: los 19 tipos que Importación reconoce están todos ubicados |

---

## 4. Defectos encontrados

| # | Qué pasó | Severidad | Dónde quedó |
|---|---|---|---|
| D-01 | **Dentro de una fase, el orden salía el del disco**: el cierre antes que el plan | Alta | Arreglado acá, ordenando por la posición del tipo dentro de su grupo. Lo cazó la prueba, no la lectura |
| D-02 | **Se contaban las citas como huecos**: 559 documentos «a medio llenar» donde hay 31 | Alta | Arreglado contando solo la marca que el estándar fija, y el porqué quedó escrito en el propio código |

---

## 5. Veredicto por criterio de aceptación

| CA | Evidencia | Veredicto |
|---|---|---|
| [CA-01](../HU-001-armar-el-expediente-de-un-proyecto.md#ca-01--el-expediente-se-arma-en-el-orden-del-ciclo) | CP-001 | **Cumple** |
| [CA-02](../HU-001-armar-el-expediente-de-un-proyecto.md#ca-02--lo-que-falta-se-lista-y-no-se-inventa) | CP-002 | **Cumple** |
| [CA-03](../HU-001-armar-el-expediente-de-un-proyecto.md#ca-03--lo-que-está-a-medio-llenar-se-marca) | CP-003 | **Cumple** |
| [CA-04](../HU-001-armar-el-expediente-de-un-proyecto.md#ca-04--la-auditoría-y-la-memoria-no-entran) | CP-004 | **Cumple** |
| [CA-05](../HU-001-armar-el-expediente-de-un-proyecto.md#ca-05--se-puede-pedir-hasta-cierto-alcance) | CP-005 | **Cumple** |

## 5.1 Lo que el plan exigía

| Lo que el plan pedía | Qué pasó |
|---|---|
| El orden declarado en su propio archivo | `orden.py`, con los ocho grupos |
| Lo que falta, calculado contra lo que el ciclo espera | Hecho: sale de los cinco documentos de una fase, que el estándar ya fija |
| Lo incompleto, leyendo el texto | Hecho, contando solo la marca |
| La memoria fuera, por tipo | Hecho |
| Lo que no encaja, aparte | Hecho, y sobre lo real está vacío |
| El alcance acotado, diciéndolo | Hecho |
| El expediente de este repositorio, armado | Hecho, y sus cuatro números están arriba |

---

## 6. Veredicto de la fase

**Concepto: Cumple.**

Los cinco criterios quedaron cumplidos con evidencia, y los dos defectos que aparecieron eran de la misma familia: **dar por bueno un orden y un conteo sin mirar qué producían de verdad**. Los dos los cazó una prueba o la corrida sobre datos reales, no la lectura del código.

**Lo que la fase no puede decir, y queda escrito:**

- **El expediente refleja lo que Importación trajo**, no lo que el proyecto tiene hoy. Lo traído es del 25 de agosto; si el proyecto avanzó, hay que traerlo otra vez, y esta fase no lo hace ni lo avisa.
- Algunos de los 31 «a medio llenar» son documentos que **hablan** de la marca. Contarlos aparte exigiría leer.

---

## 7. Evidencias

| ID | Qué es | Dónde |
|---|---|---|
| EV-01 | Las 20 pruebas del módulo | `plataforma/nucleo/expediente/tests.py` |
| EV-02 | El expediente de este repositorio | §1 y §2 |

---

## 8. Ciclos anteriores

No hay: es el primer ciclo de la fase.
