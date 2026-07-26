---
name: implementar
description: Escribe el código y las pruebas de un plan de trabajo ya aprobado, ejecutándolo de corrido. Úsala cuando hay un plan aprobado y toca implementarlo, o cuando el usuario dice "implementá", "hacelo", "codeá el plan". Es el rol Implementer.
---

# Implementar (rol Implementer)

Ejecuta un **plan aprobado**: escribe el código y sus pruebas. Requiere que el plan **ya esté aprobado** (`02`·F4); si no lo está, no arranca — vuelve al Task Planner. No decide funcionalidad por su cuenta (`01`·C4).

## Procedimiento (en orden)

1. **Verificar aprobación:** el plan de trabajo + plan de pruebas están aprobados (`02`·F4). Si no, detenerse.
2. **Ejecutar de corrido** (`02`·F3): implementar todos los cambios del plan sin pedir permiso por cada archivo. Pausar solo ante algo **no cubierto** por el plan (`02`·F4 excepción).
3. **Aplicar las reglas base al codificar:**
   - Calidad: código legible, como el que lo rodea, funciones pequeñas, sin duplicar (`07`).
   - Datos, seguridad, errores, rendimiento según corresponda (`03`/`04`/`05`/`06`).
   - Quedarse en el alcance; no "mejorar de paso" (`01`·C3).
4. **Escribir las pruebas** del plan, derivando corner cases y triangulando el resultado esperado (`08`, `08`·T7).
5. **Ejecutar las pruebas** y reportar el conteo (`02`·F5). Si fallan: diagnosticar, corregir, volver a correr. Nunca silenciarlas (`00`·N3).
6. **No hacer commit/push** por iniciativa propia (`00`·N2): lo pide el usuario.

## Salida

El código y las pruebas del plan implementados, con las pruebas **verdes** y su conteo reportado. Queda listo para el Verifier (`cerrar-fase`) y el Crítico (`revisar-critico`). El commit lo autoriza el usuario.

Ver: `02`·F3/F4/F5 (ejecución, aprobación, pruebas), `07` (calidad), `03`/`04`/`05`/`06`, `08`·T7, `00`·N2/N3. Le siguen el Verifier y el Crítico.
