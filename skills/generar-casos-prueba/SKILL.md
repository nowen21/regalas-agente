---
name: generar-casos-prueba
description: Deriva con método la matriz de casos de prueba (incluidos los corner cases) de una especificación, regla o cálculo, y triangula el resultado esperado de cada caso. Úsala al armar el plan de pruebas o antes de escribir tests, cuando el usuario pida "generá los casos de prueba", "qué casos hay que probar", "la matriz de casos". Operacionaliza la regla 08·T7. Alimenta al Planificador de tareas, al Implementador y al Verificador.
---

# Generar casos de prueba

Convierte una especificación/regla/cálculo en una **matriz de casos derivada con método** — no elegidos a ojo — con el **resultado esperado triangulado** desde fuentes independientes (`08`·T7). No escribe los tests; produce la matriz que el Implementador convierte en tests y el Verificador usa para comprobar cobertura.

## Procedimiento (en orden)

### 1. Delimitar qué se prueba
La regla de negocio, el cálculo o el comportamiento (de la especificación). Identificar sus entradas y su salida esperada.

### 2. Derivar los casos con método
- **Valores de frontera:** 0, el máximo, vacío, uno más y uno menos del límite.
- **Clases de equivalencia:** agrupar entradas que se comportan igual; un caso por grupo.
- **Tablas de decisión:** combinaciones cuando varias condiciones/banderas se cruzan.
- **Casos negativos / adversariales:** entradas inválidas, fuera de rango, maliciosas.
- **Permisos y validaciones:** con permiso / sin permiso; input válido / inválido.

### 3. Triangular el resultado esperado
Por cada caso, el valor esperado sale de **fuentes independientes que coinciden**, **no del código** (`08`·T7):
- **Mínimo 2** fuentes; **3** para lógica crítica (dinero, seguridad, legal).
- Fuentes: la **especificación**, un **cálculo manual**, una **propiedad invariante**, un **oráculo** conocido.
- Si no coinciden, hay un error en la especificación o en el diseño: resolver antes de dar el caso por bueno.

### 4. Armar la matriz

| # | Caso | Entrada / estado | Esperado | Fuente(s) del esperado | Tipo |
|---|---|---|---|---|---|
| 1 | «...» | «...» | «...» | especificación + cálculo manual | frontera / equivalencia / negativo / permiso |

## Salida

La matriz completa, lista para que el Implementador escriba los tests contra el valor esperado triangulado y el Verificador compruebe que están cubiertos los caminos (feliz, límites, errores, permisos). Marcar los casos que requieren **verificación manual** (lo que el entorno de pruebas no cubre — `08`·T4).

Ver: `08`·T7 (triangulación), `08`·T2/T6 (comportamiento observable, cobertura con criterio), `08`·T4 (verificación manual). Alimenta al Planificador de tareas, al Implementador y al Verificador.
