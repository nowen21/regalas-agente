# Resultado de Pruebas — Fase `A-EP-012-HU-002-el-entregable-sale-del-texto`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó, con qué resultado y si cada criterio quedó cumplido**. Los casos están en el [plan_pruebas.md](plan_pruebas.md).

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-012-HU-002-el-entregable-sale-del-texto` |
| **HU** | [documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/HU-002-generar-el-entregable-de-ofimatica/HU-002-generar-el-entregable-de-ofimatica.md](../HU-002-generar-el-entregable-de-ofimatica.md) |
| **Fecha de ejecución** | 2026-08-31 |
| **Ejecutó** | El agente, sobre el expediente de este repositorio |
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

**El entregable de este repositorio, medido:**

| | Cuánto |
|---|---|
| Tamaño | **8 093 097** caracteres |
| Documentos | 762 |
| Tablas convertidas | 6 205 |
| **Listas dentro de una celda** | **1 697** |
| Marcas del origen a la vista, fuera de código | **15**, todas de énfasis anidado |
| Barras de tabla a la vista | **0** |
| Dependencias nuevas | **0** |

Quince marcas en ocho millones de caracteres: **dos milésimas de por mil**.

---

## 2. Ejecución caso por caso

### CP-001 — El entregable trae todo

Los 762 documentos aparecen con su ruta, agrupados en el orden del expediente, y el archivo trae su propia tabla de contenido. Un proyecto sin documentos no genera nada y lo dice.

**Resultado: pasa.**

### CP-002 — Sin marcas del texto de origen a la vista

**El criterio que decide, y el que encontró tres defectos.**

| Entrada | Salió |
|---|---|
| Una celda con dos valores separados | dos elementos de lista |
| Una negrita que contiene el separador | una sola negrita |
| Una cita con una tabla adentro | tabla |
| Un bloque cercado con barras | tal cual |

**Sobre el archivo real:** cero barras de tabla a la vista y **15 asteriscos**, todos del mismo caso — énfasis dentro de énfasis, que este convertidor no resuelve. Está declarado y no se arregló: son 15 en ocho millones, y resolverlo bien pide un analizador de verdad.

**Resultado: pasa.**

### CP-003 — Dos corridas dan el mismo archivo

Generar dos veces sobre lo mismo produce el mismo contenido, y el archivo **no trae ninguna fecha de generación adentro**. Cuándo se generó vive en la auditoría, que es donde va esa pregunta.

**Resultado: pasa.**

### CP-004 — Avisa sin impedir

```
Faltan 22 documento(s) que el ciclo espera.
Hay 31 documento(s) con espacios sin llenar.

Entregable generado: proyectos/cimiento-el-estandar/entregable/expediente.html
```

Y lo mismo queda **dentro del archivo**, en un recuadro al principio: quien lo recibe ve lo que vio quien lo generó.

**Resultado: pasa.**

### CP-005 — No se inventa marcado

Un texto con etiquetas sale escapado, no interpretado. Y el código con asteriscos adentro **ya no se vuelve negrita**, que era un defecto real: es justamente lo que se escribe para mostrar el marcado sin que actúe.

**Resultado: pasa.**

### CP-006 — El archivo no sale a la red

Ni guiones, ni hojas de estilo, ni fuentes de un servidor: el estilo va adentro. Y ningún documento traído cambia.

**Resultado: pasa.**

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| Qué se miró | Resultado |
|---|---|
| Las 15 marcas que quedaron | Todas son énfasis dentro de énfasis. Ninguna rompe una tabla ni una lista |
| Las barras que aparecían | Todas están **dentro de código**, donde deben quedar literales |
| El recuadro de lo que falta | Sale primero, antes del índice |

---

## 4. Defectos encontrados

| # | Qué pasó | Severidad | Dónde quedó |
|---|---|---|---|
| D-01 | **El separador de una celda partía una negrita que lo contenía.** «1 · Ver lo que hay», en negrita, salía en dos trozos con los asteriscos a la vista: **174 marcas** | Alta | Arreglado: no se parte si el corte rompe una negrita o un trozo de código |
| D-02 | **Una cita con una tabla adentro salía cruda**, con las barras a la vista: **31 marcas** | Alta | Arreglado: lo citado se convierte por dentro, no se pega como prosa |
| D-03 | **El código con asteriscos se volvía negrita.** `**esto no es negrita**` salía en negrita | Alta | Arreglado: lo que va en código se aparta antes de convertir el resto y no se vuelve a tocar |

**Los tres se vieron contando sobre el archivo real**, no leyendo el código: con documentos de mentiras el convertidor se veía perfecto.

---

## 5. Veredicto por criterio de aceptación

| CA | Evidencia | Veredicto |
|---|---|---|
| [CA-01](../HU-002-generar-el-entregable-de-ofimatica.md#ca-01--un-expediente-completo-se-genera-con-todas-sus-secciones) | CP-001 | **Cumple** |
| [CA-02](../HU-002-generar-el-entregable-de-ofimatica.md#ca-02--las-listas-y-las-tablas-salen-como-listas-y-tablas) | CP-002 | **Cumple**, con la salvedad de las 15 marcas de énfasis anidado, declaradas |
| [CA-03](../HU-002-generar-el-entregable-de-ofimatica.md#ca-03--generar-dos-veces-da-el-mismo-resultado) | CP-003 | **Cumple** |
| [CA-04](../HU-002-generar-el-entregable-de-ofimatica.md#ca-04--con-espacios-sin-llenar-avisa-antes-de-generar) | CP-004 | **Cumple** |

## 5.1 Lo que el plan exigía

| Lo que el plan pedía | Qué pasó |
|---|---|
| Con la librería estándar | Hecho: **cero dependencias nuevas** |
| Tablas, y listas dentro de una celda | 6 205 tablas y 1 697 listas dentro de celdas |
| Nada de la red en el archivo | Hecho |
| La fecha fuera del archivo | Hecha |
| Lo que falta, dentro del archivo | Hecho |
| El entregable medido | Hecho, y los números están arriba |

---

## 6. Veredicto de la fase

**Concepto: Cumple.**

El expediente ya se convierte en un archivo que se abre y se entrega, generado desde el texto y sin una sola dependencia nueva. El criterio que la historia llamaba difícil se comprobó **contando** sobre ocho millones de caracteres, no mirando un ejemplo.

**Lo que no quedó, y está declarado:** quince marcas de énfasis dentro de énfasis. Resolverlo bien pide un analizador de verdad, y por quince en ocho millones no se justifica hoy.

**Y lo que esta fase no puede decir:** si el archivo se ve presentable. Se cuenta lo que quedó a la vista; que el resultado sirva para entregarlo lo decide una persona abriéndolo.

---

## 7. Evidencias

| ID | Qué es | Dónde |
|---|---|---|
| EV-01 | Las 20 pruebas del entregable | `plataforma/nucleo/expediente/tests_entregable.py` |
| EV-02 | El entregable medido | §1 y §2 |

---

## 8. Ciclos anteriores

No hay: es el primer ciclo de la fase.
