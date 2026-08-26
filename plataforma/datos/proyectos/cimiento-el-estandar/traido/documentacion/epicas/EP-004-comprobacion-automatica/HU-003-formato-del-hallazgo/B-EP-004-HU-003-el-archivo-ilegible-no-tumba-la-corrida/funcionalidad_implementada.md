# Funcionalidad implementada — Fase B-EP-004-HU-003-el-archivo-ilegible-no-tumba-la-corrida

**Para qué sirve este documento.** Dice qué quedó hecho al cerrar la fase, con la trazabilidad hasta el archivo donde vive cada cosa.

> **Cerrada el 2026-08-22, con el estándar en la versión 31.5.0.** Es el sello que dice **bajo qué reglas** cerró este trabajo: una regla escrita después no lo reabre ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).

## 0. Qué quedó, en una frase

**Un archivo que no se puede leer ya no tumba la corrida: se anota, se dice con su ruta, y todo lo demás se sigue revisando.**

## 1. Trazabilidad ([`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md))

| Ítem de la especificación | Categoría | Ubicación esperada | Estado | Evidencia |
|---|---|---|---|---|
| La lectura tolera ausente, sin permisos y mal codificado | código | [`validadores/comun.py`](../../../../../validadores/comun.py) | ✅ | `leer` con sus tres salidas |
| Quien lea puede saber que la lectura falló, sin cambiar la firma | código | el mismo | ✅ | el registro `ILEGIBLES` y la función `ilegibles()` |
| La corrida reporta el archivo ilegible con su ruta | código | el mismo | ✅ | `reportar` los agrega solo, como AVISO |
| La prueba que lo denunciaba queda destapada | prueba | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py) | ✅ | sin `expectedFailure`, y pasa |
| Un caso nuevo: la corrida sigue y reporta lo demás | prueba | el mismo | ✅ | `test_errores_la_corrida_sigue_y_reporta_lo_demas` |
| `pendientes.py` vuelve a usar la lectura común | código | [`validadores/pendientes.py`](../../../../../validadores/pendientes.py) | ✅ | su `_leer` es ahora `comun.leer` |
| El contrato dice qué pasa con el archivo ilegible | doc | [`validadores/docs/comun.md`](../../../../../validadores/docs/comun.md) | ✅ | tabla de las tres salidas y el porqué |
| El inventario de HU vuelve a estar al día | doc | `pendientes/48-inventario-hu.md` | ❌ | **no se toca:** el 48 es uno de los dos pendientes que el usuario excluyó |

## 2. Lo que cambia para un proyecto que hereda

**Nada que hacer, y una corrida más honesta.** Los validadores que el proyecto ya corre dejan de caerse ante un archivo con codificación rara —cosa que pasa con lo que viene de Word o de un editor viejo— y en cambio lo nombran.

**Lo que sí conviene saber:** si un archivo aparece en el reporte como ilegible, lo que los validadores digan **de ese archivo** puede estar incompleto. El mensaje lo advierte con esas palabras.

## 3. Lo que queda abierto

**El inventario de HU del pendiente 48 quedó atrás** (el programa cuenta 101 historias y 51 completas; el pendiente dice 78, 47 y 31), y su prueba está en rojo por eso. Es exactamente lo que ese pendiente vino a resolver, y el usuario lo excluyó de esta tanda; se deja dicho, no arreglado.

**Ocho pruebas más se destaparon de paso.** Estaban en rojo desde el 2026-08-21 citando moldes que se habían movido, y el error de lectura las tapaba: reventaban antes de comparar nada. Ya apuntan a `plantillas/ciclo-vida-proyectos/`.
