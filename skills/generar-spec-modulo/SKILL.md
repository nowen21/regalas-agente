---
name: generar-spec-modulo
description: Redacta la especificación de un módulo antes de programarlo, guiando el llenado de la plantilla de especificación. Úsala cuando se vaya a construir un módulo o funcionalidad nueva y no exista su especificación (regla base 02·F2), o cuando el usuario pida "redactá la especificación", "necesito el prompt del módulo", "diseñemos X antes de codear". Es el rol Escritor de especificación. No escribe código.
---

# Generar especificación de módulo (rol Escritor de especificación)

Produce la **especificación** que la regla `02`·F2 exige antes de tocar código: el contrato de diseño del módulo. Solo redacta documentación; **no implementa**. No inventa datos (`01`·C2) ni decide funcionalidad por su cuenta (`01`·C4): deduce lo que puede del proyecto y **pregunta** lo demás.

## Procedimiento (en orden)

### 1. Cargar contexto
- Revisar la documentación y el código existentes relacionados (`02`·F1). Si el proyecto es grande o desconocido, apoyarse en la skill `analizar-proyecto`.
- Confirmar el **slug** del módulo y dónde vive la documentación (lo declara la capa 3).

### 2. Partir de la plantilla
- Copiar `plantillas/ciclo-vida-proyectos/06-especificacion-modulo.md` a `documentacion/«slug-modulo»/spec.md`.
- Recorrer sus 13 secciones una por una.

### 3. Llenar cada sección
- **Lo que se deduce del proyecto** (contexto actual, archivos existentes, stack): llenarlo, con enlaces `archivo:línea`.
- **Lo que NO se puede deducir** (reglas de negocio, alcance, sector, normas, decisiones): **preguntar al usuario**. No asumir.
- **Ambigüedad** (más de una lectura razonable): registrarla en §3 (supuestos/preguntas abiertas) y resolverla con el usuario **antes** de cerrar la especificación (`01`·C7). Ninguna pregunta abierta queda viva al aprobar.
- Aplicar las reglas base al diseñar: datos (`03`), seguridad/permisos (`04`), pruebas + triangulación (`08`/`T7`), cumplimiento (`16`) si aplica. Usar los nombres concretos del proyecto (capa 3: `mapeo-nombres.md`).

### 4. Revisar completitud
- Ninguna sección vacía: si no aplica, dejar "No aplica porque …".
- El plan de pruebas (§10) debe existir; los criterios de aceptación (§11) deben ser **medibles**.

### 5. Presentar para aprobación
- Mostrar la especificación al usuario con un resumen corto y las preguntas abiertas que falten.
- **La especificación no está lista hasta que el usuario la aprueba** (`02`·F2). Solo entonces se pasa al plan y al código.

## Salida

Un archivo `spec.md` en la carpeta del módulo, completo salvo las preguntas abiertas pendientes, listo para que el usuario lo apruebe o corrija. No arrancar a implementar desde aquí: la especificación informa, el usuario aprueba.

Ver: plantilla `plantillas/ciclo-vida-proyectos/06-especificacion-modulo.md`, reglas `02`·F1/F2, `01`·C2/C4/C7, `13`·DOC2.
