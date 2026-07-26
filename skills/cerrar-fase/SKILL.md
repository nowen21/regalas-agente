---
name: cerrar-fase
description: Valida una unidad de trabajo (fase/módulo/tarea) antes de darla por terminada. Corre las pruebas, verifica la triangulación de los cálculos, revisa la calidad y comprueba la trazabilidad spec → implementación ítem por ítem. Úsala cuando se vaya a declarar algo "listo/terminado/cerrado", cuando el usuario pregunte "¿ya está?" o "¿lo cerramos?", o antes del commit final de una fase. Es el rol Verifier.
---

# Cerrar fase (rol Verifier)

Valida antes de cerrar. No cierra nada con pruebas en rojo ni con trazabilidad incompleta. No arregla en silencio: si encuentra un hueco, lo reporta para corregirlo. Respeta el núcleo (`00`): no silencia pruebas (`N3`), no hace commit/push por su cuenta (`N2`).

## Procedimiento (en orden)

### 1. Pruebas — que estén verdes
- Ejecutar las pruebas de la unidad (`02`·F5, `08`·T5) y **reportar el conteo** ("9/9 verdes").
- Si alguna falla: **no cerrar**. Reportar cuál y por qué; proponer el arreglo.
- Verificar que ninguna prueba esté silenciada, saltada o borrada para pasar (`00`·N3).

### 2. Triangulación — que los cálculos sean correctos
- Para la lógica de negocio y los cálculos, confirmar que el **resultado esperado** de las pruebas salió de **fuentes independientes** (spec, cálculo manual, propiedad invariante), **no del propio código** (`08`·T7).
- Confirmar que se cubrieron los **corner cases** (frontera, clases de equivalencia, casos inválidos).

### 3. Calidad
- Lint/formateo sin advertencias (`07`·Q6).
- Sin cambios fuera del alcance de la unidad (`01`·C3).
- Reglas base que aplican al ámbito con evidencia (seguridad `04`, datos `03`, etc.).

### 4. Trazabilidad spec → implementación (el corazón)
- Re-leer la **spec** y extraer **cada afirmación técnica concreta** ("hay un método X", "el selector filtra por Y", "existe el permiso Z").
- Por cada afirmación, verificar en el código/esquema/pruebas/docs que **realmente existe**, y armar la tabla (`13`·DOC3):

| Ítem de la spec | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| (frase de la spec) | (modelo/servicio/vista/prueba/permiso/ruta/doc) | (archivo real) | ✅ / ❌ / N/A / ⚠️ | (enlace `archivo:línea` o prueba) |

- **No cerrar** si hay ítems `❌` sin justificar. Los `N/A` y `⚠️` llevan justificación.
- Si aparece un `❌`, es un **hueco**: se corrige **en su lugar** (no se abre unidad nueva) y se vuelve a verificar.

### 5. Persistir y dar veredicto
- Guardar la tabla de trazabilidad en la documentación de la unidad (`13`·DOC1).
- **Veredicto:** "Cerrada" solo si pruebas verdes + triangulación ok + trazabilidad sin faltantes. Si no, reportar qué falta.

## Salida

```
Veredicto: CERRADA / NO CERRADA
- Pruebas: «9/9 verdes»
- Triangulación: «ok / faltó en X»
- Trazabilidad: «sin faltantes / N ítems ❌: …»
- Huecos a corregir: «lista o ninguno»
```

Si el veredicto es CERRADA, recordar que el commit lo pide el usuario (`00`·N2) — no hacerlo por iniciativa propia.
