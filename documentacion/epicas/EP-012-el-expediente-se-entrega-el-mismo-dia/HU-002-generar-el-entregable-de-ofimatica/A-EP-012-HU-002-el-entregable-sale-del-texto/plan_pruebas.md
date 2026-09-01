# Plan de Pruebas — Fase `A-EP-012-HU-002-el-entregable-sale-del-texto`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/HU-002-generar-el-entregable-de-ofimatica/HU-002-generar-el-entregable-de-ofimatica.md](../HU-002-generar-el-entregable-de-ofimatica.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que el entregable trae todo, **no deja marcas del texto de origen a la vista**, se genera igual dos veces, y avisa de lo incompleto sin impedir.

### 1.2 Alcance

**Entra:** el convertidor, la envoltura, el índice, los avisos y el guardado con constancia.

**No entra:** recibir cambios encima del entregable, la plantilla visual del cliente, ni la pantalla.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las seis decisiones, y por qué se mantuvo la librería estándar |
| [documentacion/expediente/spec.md](../../../../expediente/spec.md) | La `RN-6` y el `CA-7` del módulo |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| El convertidor | Encabezados, tablas, listas, citas, código y lo que no se reconoce |
| **Las listas dentro de una celda** | Que salgan como listas, sin el separador a la vista |
| **El separador dentro de una negrita** | Que no parta lo resaltado |
| **La tabla dentro de una cita** | Que se convierta, en vez de salir cruda |
| El archivo | Que traiga todo, su índice, y nada de la red |
| Dos corridas | Que den lo mismo |
| Los avisos | Que salgan y no impidan |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De fidelidad** | Es el `CA-02`, y se mide contando lo que quedó a la vista sobre el archivo real |
| **De borde del marcado** | El separador dentro de una negrita, el código con asteriscos, la cita con tabla |
| **De repetición** | Dos corridas, comparadas enteras |
| **De que NO pase** | Que el convertidor invente una etiqueta, y que el archivo salga a la red |
| **Sobre lo real** | Los 762 documentos, que es donde el marcado deja de ser de mentiras |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-002 | **Es el criterio que la historia llama lo difícil**, y sin él el cliente ve la marca del texto |
| Crítica | CP-005 | Un convertidor que inventa etiquetas produce un documento que dice otra cosa |
| Alta | CP-001, CP-003 | Que traiga todo y que dos corridas den lo mismo |
| Media | CP-004, CP-006 | Los avisos y que no salga a la red |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/expediente/` entera, y las dos baterías completas.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Los dos planes, aprobados, y el expediente ya armándose de la fase anterior.
- La decisión de con qué se genera, tomada.

### 4.2 Criterios de salida

- Los seis casos ejecutados.
- El entregable de este repositorio generado, **con las marcas contadas**.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **el archivo sale con marcas del origen por todas partes**. Un entregable que muestra la sintaxis del texto no se puede entregar, y ahí el camino de la librería estándar habría que volver a discutirlo con el número en la mano.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01 — todas las secciones | CP-001 | De sistema |
| CA-02 — sin marcas a la vista | CP-002 | **De fidelidad** |
| CA-03 — dos corridas iguales | CP-003 | De repetición |
| CA-04 — avisa sin impedir | CP-004 | De partición |
| Transversal — no se inventa marcado | CP-005 | Que **no** pase |
| Transversal — no sale a la red | CP-006 | Que **no** pase |

---

## 6. Casos de prueba

### CP-001 — El entregable trae todo

- Cada documento del expediente aparece, con su ruta.
- Los grupos salen en el orden del expediente.
- Trae **su propia tabla de contenido**.
- Un proyecto sin documentos no genera nada, y lo dice.

### CP-002 — Sin marcas del texto de origen a la vista

Cuatro casos de borde, cada uno salido de un defecto real:

| Entrada | Se espera |
|---|---|
| Una celda con dos valores separados | dos elementos de lista, sin el separador |
| Una negrita que contiene el separador | **una sola** negrita, no dos trozos partidos |
| Una cita con una tabla adentro | tabla, no barras a la vista |
| Un bloque cercado con barras | **queda tal cual**: es un dibujo, no una tabla |

**Y sobre el archivo real:** se cuenta cuántas marcas quedaron fuera de los bloques de código. El número queda escrito, sea el que sea.

### CP-003 — Dos corridas dan el mismo archivo

- Generar dos veces y comparar el contenido entero.
- **Y comprobar que no hay una fecha adentro**, que es lo que haría distintos dos archivos idénticos.

### CP-004 — Avisa sin impedir

- Con documentos faltantes: avisa cuántos.
- Con huecos sin llenar: avisa cuántos.
- **Genera igual**, y lo que falta queda escrito **dentro del archivo**, no solo en la consola.

### CP-005 — No se inventa marcado

- Un texto con etiquetas adentro sale **escapado**, no interpretado.
- El código con asteriscos adentro no se vuelve negrita: es justamente lo que se escribe para mostrar el marcado sin que actúe.

### CP-006 — El archivo no sale a la red

- Ni guiones, ni hojas de estilo, ni fuentes de un servidor.
- **Y no toca ningún documento traído:** retrato antes y después.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Carpetas temporales con documentos de mentiras, y el expediente real para la medición. No aplican usuarios.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Si el archivo se ve bien.** Se cuenta lo que quedó a la vista, que es medible; que el resultado le parezca presentable a quien lo recibe lo decide una persona abriéndolo.

**Y no se prueba con el procesador de texto del cliente.** Se genera en un formato abierto que esos programas abren; que cada uno lo muestre igual está fuera de lo que esta fase puede comprobar.

---

## 8. Herramientas

El corredor de la plataforma y la librería estándar. **Ninguna dependencia nueva, y ese es un requisito de la fase.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | El convertidor inventa una etiqueta · el archivo sale a la red |
| **Alta** | Marcas del origen a la vista · dos corridas distintas |
| **Media** | Un aviso que no sale |

### 9.2 Flujo · 9.3 Contenido mínimo · 9.4 Registro

En el `resultado_pruebas.md` de esta fase, con qué se corrió, qué salió y qué se esperaba.

---

## 10. Cronograma

Una jornada, la del 2026-08-31.

---

## 11. Roles y responsabilidades

Una sola persona cumple los roles. Quien aprueba es el usuario.

---

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Objetivo |
|---|---|
| Marcas del origen a la vista, fuera de bloques de código | Lo más cerca de cero que se pueda, y **el número escrito** |
| Listas dentro de celdas convertidas | Se cuenta |
| Dependencias nuevas | **Cero** |

### 12.2 Dónde se miden

Sobre el archivo generado, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Probar el convertidor solo con ejemplos inventados | Se mide sobre los 762 documentos reales |
| Dar por bueno «no se ven marcas» sin contarlas | Se cuentan, y el número va en el resultado |

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
