# Funcionalidad implementada — Fase A-EP-005-HU-005-el-cambio-de-reglas-no-se-guarda-sin-version

**Para qué sirve este documento.** Dice qué quedó hecho al cerrar la fase, con la trazabilidad hasta donde vive cada cosa.

## 0. Qué quedó, en una frase

**Un commit que cambia una regla y no sube la versión ni escribe su entrada en el registro, no se guarda.**

## 1. Trazabilidad ([`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))

| Ítem de la especificación | Categoría | Ubicación esperada | Estado | Evidencia |
|---|---|---|---|---|
| Al guardar se mira si el cambio toca `base/` o `plantillas/` | código | [`validadores/guardian_version.py`](../../../../../validadores/guardian_version.py) | ✅ | `reglas_tocadas` |
| Si toca, exige versión y entrada, y detiene | código | el mismo | ✅ | hallazgo de severidad FALLA |
| Si no toca, se calla | código | el mismo | ✅ | `CP-003`, el caso que decide |
| Corre en el momento de guardar | código | `validar.py versionado --preparados`, que ejecuta el `pre-commit` | ✅ | sin enganche nuevo: se suma al que ya existía |
| Los casos que lo protegen | prueba | [`test_el_cambio_de_reglas_lleva_su_version.py`](../../../../../validadores/tests/test_el_cambio_de_reglas_lleva_su_version.py) | ✅ | siete, todos en verde |
| El contrato dice qué exige y qué no | doc | [`validadores/docs/guardian_version.md`](../../../../../validadores/docs/guardian_version.md) | ✅ | con la tabla de cuándo se calla |
| El incremento de la especificación | doc | [`documentacion/automatismos/spec.md`](../../../../../documentacion/automatismos/spec.md) | ✅ | RN-57 a RN-61 y su fila de trazabilidad |
| La fila del inventario de HU | doc | `pendientes/48-inventario-hu.md` | ❌ | **no se toca:** el 48 es uno de los dos que el usuario excluyó |

## 2. Lo que cambia para un proyecto que hereda

**Nada obligatorio, y algo que gana el que lo quiera.** La comprobación vive en el estándar y vigila el estándar. Un proyecto que herede y tenga su propia `base/` local no la usa; lo que sí puede usar es el mismo subcomando, que ya corre en su `pre-commit`.

## 3. Lo que queda abierto

**Un `--no-verify` la esquiva.** Es así por diseño: un enganche local nunca es garantía, y por eso la regla sigue siendo `20·M10` y esto es su recordatorio mecánico. Lo que no se puede esquivar es el registro: una versión sin entrada la reporta `numeracion.py` sobre el repositorio entero.

**No juzga la calidad de la entrada.** Que el registro describa de verdad el cambio, y que el tipo de versión sea el correcto, siguen siendo de quien escribe. `20·M17` es la regla que lo exige, y su comprobación mide la forma, no la verdad.
