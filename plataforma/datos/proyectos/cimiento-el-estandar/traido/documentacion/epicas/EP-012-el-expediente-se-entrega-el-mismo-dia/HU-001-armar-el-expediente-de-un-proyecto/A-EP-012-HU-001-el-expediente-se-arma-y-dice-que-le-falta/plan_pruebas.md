# Plan de Pruebas — Fase `A-EP-012-HU-001-el-expediente-se-arma-y-dice-que-le-falta`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/HU-001-armar-el-expediente-de-un-proyecto/HU-001-armar-el-expediente-de-un-proyecto.md](../HU-001-armar-el-expediente-de-un-proyecto.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que el expediente se arma en el orden del ciclo y que **dice en qué estado está**: qué falta, qué está a medio llenar y qué no encaja. Y que armar no toca ningún documento.

### 1.2 Alcance

**Entra:** el orden, las tres listas, el alcance acotado y la exclusión de la memoria.

**No entra:** generar el archivo de ofimática, que es la `HU-002`, ni la pantalla.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las seis decisiones y la línea base de 1 002 documentos |
| [documentacion/expediente/spec.md](../../../../expediente/spec.md) | El orden del ciclo de la §5.1 y las siete reglas |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| El orden | Entre grupos, y **dentro de una fase** |
| Lo que falta | Que se nombre, y que no aparezca vacío en el expediente |
| Lo incompleto | Que cuente huecos y **no cuente citas** |
| Lo excluido | Que la memoria no entre, y que no se reporte como defecto |
| Lo que no encaja | Que se liste aparte, con su tipo |
| El alcance | Que lo acotado diga qué dejó fuera |
| El disco | Que armar no cambie nada |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De que NO pase** | La memoria fuera, y ningún documento tocado |
| **De partición** | Fase completa · fase a la que le falta uno · documento con huecos · documento con citas |
| **De orden** | El del ciclo contra el del disco, que es donde se cae solo |
| **Sobre lo real** | Los 1 002 documentos traídos, que es donde los números dejan de ser de mentiras |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-002 | **Si lo que falta no se nombra, el expediente se entrega incompleto sin que nadie lo note** |
| Crítica | CP-006 | Armar no puede tocar nada: son los documentos del proyecto |
| Alta | CP-001, CP-003 | El orden y los huecos |
| Media | CP-004, CP-005 | La exclusión y el alcance |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/expediente/` entera, y las dos baterías completas por la no regresión.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Los dos planes, aprobados, y la especificación del módulo también.
- La línea base contada: cuántos documentos hay traídos y de qué tipos.

### 4.2 Criterios de salida

- Los seis casos ejecutados.
- El expediente de este repositorio armado, **con sus cuatro números escritos**.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **la lista de lo que falta sale tan larga que deja de leerse**. Un expediente que reporta cuatrocientos faltantes no informa: abruma, y quien lo recibe deja de mirarlo. Ahí el criterio de qué espera el ciclo está mal puesto, no el proyecto.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01 — el orden del ciclo | CP-001 | De orden |
| CA-02 — lo que falta, con nombre | CP-002 | Que **no** pase |
| CA-03 — lo incompleto, marcado | CP-003 | De partición |
| CA-04 — la memoria no entra | CP-004 | Que **no** pase |
| CA-05 — el alcance acotado | CP-005 | De partición |
| Transversal — no se toca nada | CP-006 | De retrato |

---

## 6. Casos de prueba

### CP-001 — El orden es el del ciclo

- **Entre grupos:** planificación antes que diseño, y diseño antes que épicas.
- **Dentro de una fase:** los cinco en su orden —plan, pruebas, resultado, estado, cierre—. **Por nombre de archivo saldrían al revés**, con el cierre antes que el plan, y ese es justamente el orden del disco que el criterio descarta.
- **Un proyecto sin documentos:** lo dice, en vez de devolver un expediente vacío.

### CP-002 — Lo que falta se nombra, y no se inventa

- **Precondición:** una fase a la que le falta uno de sus cinco documentos.
- **Resultado esperado:** aparece en la lista, con **qué documento y de qué fase**; y el expediente trae cuatro, no cinco con uno vacío.
- **Y una fase completa no reporta nada**, que es lo que impide que la lista se vuelva ruido.

### CP-003 — Lo incompleto se marca, y una cita no es un hueco

| Entrada | Se espera |
|---|---|
| Un documento con dos marcas de la casa | dos huecos |
| Un documento lleno | ninguno |
| «el usuario dijo *no hacer*», entre comillas angulares | **cero huecos** |
| Dos documentos con distinto número | de más huecos a menos |

**El tercero es el que importa.** En esta casa se cita con esas mismas comillas todo el tiempo: contarlas daría por incompleto cualquier documento bien escrito.

### CP-004 — La memoria no entra

- **Resultado esperado:** las señales no aparecen; el índice de una carpeta tampoco.
- **Y no se reportan como «no encaja»:** se excluyen a propósito, y meterlas en esa lista las haría ver como un defecto.

### CP-005 — El alcance acotado dice qué dejó fuera

- Completo: las dos fases. Acotado hasta la primera: solo esa, y las cinco de la otra **listadas** como fuera del alcance.
- **Y lo acotado no reporta como faltante lo que se pidió no mirar.**

### CP-006 — Armar no toca nada

- **Acción:** retratar la carpeta de datos, armar, y volver a retratar.
- **Resultado esperado:** idénticos.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Carpetas temporales que la prueba crea y borra, con documentos de mentiras; y lo traído de verdad para la corrida final. No aplican usuarios.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Que lo traído esté al día.** El expediente refleja lo que Importación trajo el día que se corrió, no lo que el proyecto tiene hoy. Si el proyecto avanzó, hay que traerlo otra vez — y esta fase no lo hace ni lo avisa.

**Y si un documento «a medio llenar» lo está de verdad.** Se cuenta la marca de la casa; un documento que **habla** de esa marca la trae escrita y se cuenta igual. Es el mismo caso de nombrar contra ser.

---

## 8. Herramientas

El corredor de la plataforma. Ninguna dependencia nueva.

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | Armar modifica un documento · un faltante no se nombra |
| **Alta** | El orden sale el del disco · la memoria entra |
| **Media** | Una cita se cuenta como hueco |

### 9.2 Flujo · 9.3 Contenido mínimo · 9.4 Registro

En el `resultado_pruebas.md` de esta fase.

---

## 10. Cronograma

Una jornada, la del 2026-08-31.

---

## 11. Roles y responsabilidades

Una sola persona cumple los roles. Quien aprueba es el usuario.

---

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Antes | Después |
|---|---|---|
| Formas de juntar la documentación | ninguna | una orden |
| Documentos en el expediente | — | se cuenta |
| Faltantes que nadie veía | desconocidos | se nombran |

### 12.2 Dónde se miden

La salida de la orden, escrita en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Probar el orden solo con un grupo | El `CP-001` prueba también dentro de una fase, que es donde se cae |
| Dar por bueno el conteo de huecos sin mirar qué contó | El `CP-003` incluye una cita, y el resultado escribe la cifra antes y después |

---

## 14. Control de versiones

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-31 | Ing. José Dúmar Jiménez Ruíz | Creación del plan de pruebas de la fase |

---

## 15. Aprobación

| Rol | Nombre | Aprobación |
|---|---|---|
| Usuario | Ing. José Dúmar Jiménez Ruíz | ☐ |
