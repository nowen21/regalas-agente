# Resultado de Pruebas — Fase `B-EP-006-HU-003-la-busqueda-dice-donde-esta`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-006-HU-003-la-busqueda-dice-donde-esta` |
| **Plan de pruebas** | [plan_pruebas.md](plan_pruebas.md), versión 1 |
| **Fecha de ejecución** | 2026-08-30 |
| **Ciclo** | 1 |

---

## 2. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** el defecto que la fase `A-EP-006-HU-003-retrodocumentar-la-busqueda-por-palabra` dejó probado con fallo esperado quedó arreglado, y su prueba pasó a correr como cualquier otra.

| Métrica | Meta | Real |
|---|---|---|
| Pruebas de la memoria en verde | 59 | **59** |
| Pruebas marcadas como fallo esperado | 0 | **0**, eran 5 |

---

## 3. Qué se arregló

**Dos defectos, y el segundo no se veía.**

El primero es el que la historia pedía: la búsqueda encontraba y **no decía dónde está lo que encontró**, así que el resultado no alcanzaba para abrirlo. Ahora la consulta trae también ese dato y lo imprime **debajo** de cada resultado, en su propia línea: una línea de más por resultado se lee, una columna más en la misma línea no.

El segundo lo destapó la fase `A` al probarlo de una forma que vale la pena copiar: el camino «(sin señales relevantes)» **retornaba sin cerrar la conexión**, y eso no se deduce leyendo. La prueba borra el archivo después de buscar, porque en Windows no se puede borrar lo que está tomado. El descuido se ve en vez de suponerse.

| Antes | Ahora |
|---|---|
| La búsqueda encuentra y no dice dónde | Imprime la ubicación debajo de cada resultado |
| El camino sin resultados deja la conexión tomada | La cierra antes de salir |

---

## 4. Verificaciones manuales  ·  `08·T4`

### 4.1 El fallo esperado se destapa, no se borra

La fase `A` no podía arreglar esto: su plan declaraba que no se tocaba el programa (`02·F8`). Dejó el defecto **probado y marcado como fallo esperado**, que es la forma de que no se pierda: el día que se arregle, la prueba pasa a «éxito inesperado» y obliga a volver.

Es exactamente lo que ocurrió acá: al arreglar, la corrida reportó éxitos inesperados y hubo que volver a destaparlas una por una.

### 4.2 La corrida completa

```
Ran 59 tests in 5.7s
OK
```

Sin un solo fallo esperado en el archivo, donde había cinco.

---

## 5. Defectos encontrados

**Ninguno nuevo.**

---

## 6. Evidencias

- `memoria/memoria.py` y `memoria/semantica.py`
- `memoria/pruebas.py`, con las pruebas destapadas
