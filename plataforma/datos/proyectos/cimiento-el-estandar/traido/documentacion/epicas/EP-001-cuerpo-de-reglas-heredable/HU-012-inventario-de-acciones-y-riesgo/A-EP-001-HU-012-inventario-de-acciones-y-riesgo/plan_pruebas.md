# Plan de Pruebas — Fase A-EP-001-HU-012-inventario-de-acciones-y-riesgo   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos se comprueba cada criterio**. Su exigencia central es que **ningún CA quede sin al menos un caso**. Se aprueba **antes** de ejecutar y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md`.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-001-HU-012 |
| **Alcance** | Fase `A-EP-001-HU-012-inventario-de-acciones-y-riesgo` |
| **Fecha** | 2026-08-18 |
| **Aprobado por** | Sin aprobar — se presenta junto al [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |

> Fase chica: se llenan las secciones **3, 5, 6 y 9** ([proporcionalidad](../../../../../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md)).

---

## 3. Estrategia

### 3.1 Niveles

| Nivel | Qué comprueba | Automatizado |
|---|---|---|
| Contenido del anexo | Que la tabla esté completa y bien formada | **Sí** — `validar.py acciones` |
| Cobertura | Que las diez herramientas de `CA-01` tengan clase | **Sí** |
| Utilidad de la clasificación | Que dos niveles opuestos exijan cosas distintas | **Sí**, comparando los textos |
| No regresión | Que `N1`–`N6` sigan diciendo lo mismo | **Sí** — huella del archivo del núcleo |

### 3.2 Lo que **no** se comprueba, y se declara

**Que la clasificación sea la correcta.** Que borrar un archivo no versionado merezca el nivel alto y no el medio **lo decide quien lee**, no un programa. Se comprueba que **esté clasificado y con ejemplo**, no que el juicio sea bueno.

Esto va también a `reglas-validables.md`: [`20·M9`](../../../../../base/20-meta-reglas/reglas/M9-toda-regla-declara-si-es-validable.md) pide declarar qué se puede comprobar, y **una comprobación honesta sobre lo que no cubre vale más que una que finge cubrirlo todo**.

---

## 5. Matriz de trazabilidad — ningún CA sin caso

| CA | Caso |
|---|---|
| `CA-01` · la lista cubre todo | CP-001, CP-002 |
| `CA-02` · cada clase con su nivel y su ejemplo | CP-003, CP-004, CP-005 |
| `CA-03` · dos riesgos distintos no piden lo mismo | CP-006 |
| `CA-04` · lo no nombrado se trata como lo peor | CP-007 |
| Transversal · límites | CP-008 |
| Transversal · no regresión | CP-009 |

---

## 6. Casos

### CP-001 — Las diez herramientas tienen clase

1. Tomar la lista literal del `CA-01`: leer · escribir un archivo del repositorio · borrar · correr un comando local · correr algo que sale a la red · tocar git · tocar datos · tocar la máquina fuera del repositorio · escribir en el histórico · escribir en la memoria.
2. Buscar cada una en el anexo.
- **Esperado:** las diez encontradas. **Huérfanas: cero.**

### CP-002 — Una herramienta que falte se reporta

1. Quitar una clase del anexo, sobre una copia.
2. Correr la comprobación.
- **Esperado:** la reporta por su nombre. **Es el caso que hace útil al CP-001:** sin este, «cero huérfanas» podría significar que el programa no busca nada.

### CP-003 — Ninguna fila con nivel y sin ejemplo

1. Recorrer la tabla.
- **Esperado:** ninguna. **Por qué importa:** `CA-02` pide los dos campos, y el ejemplo es el que hace que el nivel se entienda sin discutirlo.

### CP-004 — Un nivel fuera de la escala se reporta

1. Sobre una copia, poner en una fila un nivel inventado.
- **Esperado:** lo reporta. La escala es cerrada, no texto libre.

### CP-005 — Una fila sin ejemplo se reporta

1. Sobre una copia, vaciar el ejemplo de una fila con nivel.
- **Esperado:** lo reporta.

### CP-006 — Dos niveles opuestos exigen cosas distintas

1. Tomar la fila de menor nivel y la de mayor.
2. Comparar lo que exige cada una **antes de ejecutarse**.
- **Esperado:** son distintas. **Si son iguales, la fase falló aunque todo lo demás pase** — es el defecto que la historia corrige.

### CP-007 — Lo que la lista no nombra

1. Inventar una acción que el anexo no cubra.
2. Leer qué manda hacer.
- **Esperado:** dice las tres: tratarla como el nivel más alto, **decirlo**, y anotarla para clasificarla.

### CP-008 — La acción que cae en dos clases

1. Buscar una que encaje en dos — por ejemplo, un comando local que además sale a la red.
- **Esperado:** el anexo define qué manda. **Si no lo define, el caso queda como defecto abierto**, no como aprobado.

### CP-009 — `N1` a `N6` no cambiaron

1. Comparar el texto de las seis reglas del núcleo contra lo guardado.
- **Esperado:** idéntico. **La lista organiza, no reemplaza.**

---

## 9. Criterios de aceptación de la corrida

**Pasa** si los nueve casos pasan, y `tests/` y `pruebas.py` quedan en verde.

**No pasa** si CP-006 sale igual en las dos filas, aunque todo lo demás pase: sin diferencia de exigencia, el inventario es una tabla decorativa.
