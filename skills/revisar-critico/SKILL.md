---
name: revisar-critico
description: Revisión adversarial e independiente de un cambio antes de cerrarlo. Intenta refutar que esté bien: busca bugs, agujeros de seguridad y casos que la spec no anticipó. Úsala cuando se quiera una segunda mirada crítica sobre un cambio/diff, cuando el usuario pida "revisá esto", "qué puede salir mal", "buscá bugs/problemas", o antes de cerrar algo importante. Es el rol Reviewer/Crítico — complementa al Verifier, no lo reemplaza.
---

# Revisar crítico (rol Reviewer/Crítico)

Segunda mirada **independiente y adversarial**. Mientras el Verifier comprueba que el cambio **cumple la spec**, el Crítico pregunta **"¿qué puede salir mal?"** — busca lo que la spec **no anticipó**. Solo lee y reporta; **no arregla** (propone). No inventa hallazgos (`01`·C2): cada uno se apoya en el código real.

## Mentalidad

Asumir que el código **está mal** hasta demostrar lo contrario. El objetivo no es aprobar, es **encontrar el fallo**. Un hallazgo débil no aportado con un escenario concreto no cuenta.

## Dimensiones a atacar

Revisar el cambio contra cada una:

- **Correctitud / bugs:** ¿hay un input que produce un resultado incorrecto o un crash? Off-by-one, nulos, orden de operaciones, condiciones invertidas.
- **Casos límite no cubiertos:** vacío, 0, negativo, máximo, duplicado, concurrencia (`08`·T7).
- **Seguridad:** authz ausente o evadible, inyección, entrada sin validar, secretos expuestos, scope no verificado (`04`).
- **Manejo de errores:** errores tragados, estado inconsistente al fallar, fuga de internos al usuario (`05`).
- **Datos:** rompe integridad, migración no retrocompatible, hardcode que debía ir a catálogo (`03`).
- **Rendimiento:** N+1, consultas sin límite, cargar de más (`06`).

## Procedimiento

1. **Delimitar** qué se revisa (el diff / los archivos del cambio).
2. **Atacar** cada dimensión buscando un fallo concreto.
3. Por cada hallazgo, escribir un **escenario de fallo**: *inputs/estado → resultado incorrecto/crash*. Sin escenario, no es hallazgo.
4. **Verificar** cada hallazgo contra el código real antes de reportarlo (no "cry wolf"). Descartar los que no se sostienen.
5. **Ordenar** por severidad (seguridad/corrupción de datos primero; cosmético último).

## Salida

Lista de hallazgos confirmados, del más grave al menos:

```
[severidad] título corto
- Dónde: archivo:línea
- Escenario de fallo: <inputs/estado → qué sale mal>
- Por qué: <la causa>
- Propuesta: <el arreglo sugerido>
```

Si no sobrevive ningún hallazgo tras verificar: decirlo explícito ("sin hallazgos que se sostengan"). No inventar problemas para justificar la revisión.

No arreglar desde aquí: el Crítico reporta, el usuario decide qué se corrige.

Ver: `08`·T7 (triangulación), `04` (seguridad), `05` (errores), `03` (datos), `06` (rendimiento); complementa `cerrar-fase` (Verifier).
