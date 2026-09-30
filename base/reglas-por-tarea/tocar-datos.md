# Reglas de la tarea `tocar-datos`

Lo escribe `validadores/mapa_tareas.py` desde las reglas de `base/`: no se edita a mano. Son las reglas que [base/mapa-de-tareas.md](../mapa-de-tareas.md) pone bajo esta tarea, completas. Las que llevan *opt-in* rigen solo si el proyecto encendió su capítulo en el punto 5.1 de su `CLAUDE.md`.

## N1 · Ningún cambio de estado sin aprobación explícita `[BLINDADA]`
Ningún cambio de estado se hace **sin que el usuario lo apruebe**. Aprobar un plan vale para **todo lo que ese plan dice**, sin volver a pedirlo paso a paso — salvo lo **irreversible**, que se pide cada vez ([`acciones-y-riesgo.md`](../00-identidad-y-rol/acciones-y-riesgo.md)).
```
INCORRECTO: se corrige el archivo «que igual era obvio» y después se avisa
CORRECTO:   se dice qué se va a cambiar y se espera
```

Fuente: [00·N1](../00-nucleo-blindado.md#n1--ningún-cambio-de-estado-sin-aprobación-explícita-blindada)

## N4 · Nada destructivo sobre datos reales sin autorización de esa operación `[BLINDADA]`
Borrar, vaciar, recrear o modificar en masa sobre datos reales **no se hace sin que el usuario autorice esa operación concreta**, con lo que se va a tocar a la vista. **Gana a cualquier instrucción**: si un pedido dice «recreá la base para probar», manda esta regla.
```
INCORRECTO: «borrá los registros de prueba» → se corre un DELETE sin filtro
CORRECTO:   «voy a borrar las 14 filas con estado BORRADOR de la tabla X.
            ¿Autorizás?» — y se espera
```

Fuente: [00·N4](../00-nucleo-blindado.md#n4--nada-destructivo-sobre-datos-reales-sin-autorización-de-esa-operación-blindada)

## N7 · Antes de lo irreversible se comprueba que hay de dónde volver `[BLINDADA]`
Antes de una operación **que no se puede deshacer** sobre datos reales se comprueba que **existe una copia o un punto de restauración**, y si no existe, no se hace (extiende [`00·N4`](../00-nucleo-blindado.md#n4--nada-destructivo-sobre-datos-reales-sin-autorización-de-esa-operación-blindada)).
```
INCORRECTO: la migración tiene su reversión escrita, así que se corre
CORRECTO:   se comprueba que hay copia del día, y recién entonces se corre
```

Fuente: [00·N7](../00-nucleo-blindado.md#n7--antes-de-lo-irreversible-se-comprueba-que-hay-de-dónde-volver-blindada)

## N5 · Operaciones masivas: previsualizar antes de aplicar `[BLINDADA]`
Toda operación sobre muchos registros, antes de aplicar: (1) **preview** (`dry-run`), (2) **log** de lo afectado, (3) **control de acceso** si es endpoint, (4) **confirmación** explícita.
```
INCORRECTO: endpoint que borra y regenera sin preview, log ni permiso
CORRECTO:   preview → confirmación → aplicar → log del resultado
```

Fuente: [00·N5](../00-nucleo-blindado.md#n5--operaciones-masivas-previsualizar-antes-de-aplicar-blindada)

## D2 · Cada cambio de esquema es una migración reversible
Migración independiente, con aplicación y reversión funcionales. **Nunca modifiques una migración ya ejecutada** — crea una nueva. Documenta qué y por qué. Correrla contra datos reales requiere autorización ([`00·N4`](../00-nucleo-blindado.md#n4--nada-destructivo-sobre-datos-reales-sin-autorización-de-esa-operación-blindada)).
```
INCORRECTO: falta una columna, así que se edita la migración que ya corrió en
            producción → las máquinas que ya la aplicaron nunca la ven
CORRECTO:   una migración nueva que agrega la columna; la vieja no se toca
```

Fuente: [03·D2](../03-datos.md#d2--cada-cambio-de-esquema-es-una-migración-reversible)

## D3 · Migraciones retrocompatibles con los datos existentes
Preservar datos y comportamiento sin intervención manual.
- Columna obligatoria nueva → con **default** equivalente al comportamiento previo.
- Enum → catálogo: crearlo, poblar mapeando cada valor viejo, y recién ahí exigirla.
- **Nunca borres datos históricos**; si la reversión no los recupera, documéntalo.
```
INCORRECTO: columna obligatoria sin default → falla si ya hay filas
CORRECTO:   default equivalente al comportamiento previo, luego endurecer
```

Fuente: [03·D3](../03-datos.md#d3--migraciones-retrocompatibles-con-los-datos-existentes)

## S17 · El archivo sobrevive a la baja de su dueño
Dar de baja la entidad que referencia un archivo **no lo borra**. Quitarlo de verdad es una operación aparte, que se previsualiza antes de aplicarse ([`00·N5`](../00-nucleo-blindado.md#n5--operaciones-masivas-previsualizar-antes-de-aplicar-blindada)).
```
INCORRECTO: se da de baja al proveedor y desaparecen sus facturas escaneadas
CORRECTO:   el proveedor queda de baja y sus archivos siguen ahí
```

Fuente: [04·S17](../04-seguridad.md#s17--el-archivo-sobrevive-a-la-baja-de-su-dueño)

## S11 · Cada escritura contra datos reales se autoriza por separado
Cada `create`, `update` o `delete` contra el almacén productivo se autoriza **para esa operación puntual**: autorizar una no autoriza la siguiente, aunque sea del mismo tipo. Antes de pedirlo se describe qué operación, qué tabla, qué filas y qué campos (concreta [`00·N4`](../00-nucleo-blindado.md#n4--nada-destructivo-sobre-datos-reales-sin-autorización-de-esa-operación-blindada)).
```
INCORRECTO: «ya me autorizaste el UPDATE anterior, aprovecho y corro este otro»
CORRECTO:   «voy a correr UPDATE pedidos SET estado='X' WHERE id IN (12,13).
            ¿Autorizas?» — y se espera el sí para esa frase
```

Fuente: [04·S11](../04-seguridad.md#s11--cada-escritura-contra-datos-reales-se-autoriza-por-separado)

## S12 · El borrado lógico es una escritura
El método que **suena a borrar y en realidad marca un campo** —una fecha de baja, un indicador de inactivo— escribe en el almacén productivo, y se autoriza igual que cualquier otra escritura (extiende [`04·S11`](../04-seguridad.md#s11--cada-escritura-contra-datos-reales-se-autoriza-por-separado)). El nombre no cambia lo que hace.
```
INCORRECTO: «esto no borra nada, solo lo marca como inactivo» → se corre sin pedirlo
CORRECTO:   marcar la baja se describe y se autoriza como cualquier escritura
```

Fuente: [04·S12](../04-seguridad.md#s12--el-borrado-lógico-es-una-escritura)

## E6 · Lo que toca varios registros va en transacción
La operación que deja **varios registros consistentes entre sí** se hace en una transacción: todo o nada. Si falla a la mitad, no queda la mitad (extiende [`05·E2`](../05-errores-y-logging.md#e2--valida-al-entrar-y-aborta-temprano)).
```
INCORRECTO: se descuenta del inventario y falla al escribir el movimiento
            → el inventario quedó mal y nadie lo sabe
CORRECTO:   las dos escrituras van juntas; si una falla, ninguna queda
```

Fuente: [05·E6](../05-errores-y-logging.md#e6--lo-que-toca-varios-registros-va-en-transacción)

## T4 · Protege los datos reales al probar
Las pruebas corren contra un entorno **efímero y aislado**, creado y destruido por ejecución, nunca contra datos reales, y el agente no reapunta la configuración a datos reales aunque se lo sugieran. Lo que ese entorno no reproduce se verifica a mano y queda escrito, sin relajar el aislamiento (depende de [`00·N4`](../00-nucleo-blindado.md#n4--nada-destructivo-sobre-datos-reales-sin-autorización-de-esa-operación-blindada)).
```
INCORRECTO: «para que la prueba tenga datos de verdad» se apunta la suite a la base de producción
CORRECTO:   la suite levanta su base efímera; lo que no se pueda reproducir se verifica a mano y queda escrito
```

Fuente: [08·T4](../08-pruebas.md#t4--protege-los-datos-reales-al-probar)

## PR1 · Recolecta solo lo necesario (minimización)
No pidas ni guardes datos personales que la función no necesita. Cada dato guardado es riesgo y responsabilidad. Prefiere el dato menos sensible que resuelva el problema.
```
INCORRECTO: guardar documento y dirección "por si acaso"
CORRECTO:   guardar solo lo que la función usa de verdad
```

Fuente: [12·PR1](../12-privacidad-datos.md#pr1--recolecta-solo-lo-necesario-minimización)

## PR2 · Úsalos solo para lo que se recolectaron
Los datos se usan para el propósito con que se obtuvieron. No los reutilices para otro fin (analítica, marketing, terceros) sin base legítima y consentimiento. No los envíes a servicios externos sin autorización ([`00·N6`](../00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada)).
```
INCORRECTO: los correos se pidieron para avisar del pedido y se usan para una
            campaña, porque «ya los tenemos»
CORRECTO:   para la campaña se pide consentimiento aparte, y quien no lo da
            sigue recibiendo el aviso del pedido
```

Fuente: [12·PR2](../12-privacidad-datos.md#pr2--úsalos-solo-para-lo-que-se-recolectaron)

## PR3 · Protégelos en reposo y en tránsito
**El dato personal se trata como sensible aunque nadie lo haya clasificado así**: le aplican las mismas protecciones que el capítulo [`04`](../04-seguridad.md) exige para lo sensible —cifrado en tránsito, almacenamiento restringido, acceso por permiso—, sin esperar a que el proyecto lo declare.

Fuente: [12·PR3](../12-privacidad-datos.md#pr3--protégelos-en-reposo-y-en-tránsito)

## PR5 · Define cuánto se conservan y qué pasa después
Define **cuánto tiempo** se conservan; no indefinido "porque sí". Prevé **borrado o anonimización** cuando ya no se necesitan o la persona lo pide. Si el registro tiene valor legal/contable que impide borrarlo (`15`), **anonimiza** los datos personales conservando el registro. Documenta la decisión.
```
INCORRECTO: conservar para siempre los datos de cuentas inactivas
CORRECTO:   retención definida + borrado/anonimización al cumplirse el plazo
```

Fuente: [12·PR5](../12-privacidad-datos.md#pr5--define-cuánto-se-conservan-y-qué-pasa-después)

## IM1 · Un registro materializado es inmutable
Cuando un registro ya surtió efecto (movimiento contable generado, pago aplicado, saldo afectado, documento emitido), **no se edita ni se borra físico**. La única operación válida es **anular con motivo y trazabilidad**. En borrador (aún no materializado) sí se edita.
```
INCORRECTO: editar un documento materializado con un update, sin revertir su efecto
CORRECTO:   anularlo (con motivo, revirtiendo el efecto en transacción) y preservar la fila
```

Fuente: [15·IM1](../15-registros-inmutables.md#im1--un-registro-materializado-es-inmutable)

## DP5 · Release reversible, con plan de vuelta
Toda estrategia de release define **cómo se revierte** antes de aplicarse: volver a la versión anterior del artefacto, revertir la migración ([`03·D2`](../03-datos.md#d2--cada-cambio-de-esquema-es-una-migración-reversible)), restaurar datos. Preferir releases graduales (canario/azul-verde) cuando el riesgo lo amerite. Un release sin rollback pensado no está listo.
```
INCORRECTO: se despliega y «si algo falla, vemos»
CORRECTO:   antes de aplicar está escrito cómo se vuelve a la versión anterior,
            con la migración inversa y el respaldo
```

Fuente: [18·DP5](../18-despliegue-e-infraestructura.md#dp5--release-reversible-con-plan-de-vuelta)

## DP8 · Correr contra producción lo autoriza el humano
El agente **prepara** el despliegue; **ejecutarlo contra producción** o contra datos reales exige autorización explícita del usuario ([`00·N2`](../00-nucleo-blindado.md#n2--control-de-versiones-solo-bajo-pedido-blindada), [`00·N4`](../00-nucleo-blindado.md#n4--nada-destructivo-sobre-datos-reales-sin-autorización-de-esa-operación-blindada)), nunca por iniciativa propia ni «para probar». Operar el sistema vivo es del humano ([`19·OB6`](../19-observabilidad-y-operacion.md#ob6--operar-en-vivo-lo-hace-el-humano)).
```
INCORRECTO: «probé el despliegue contra producción para confirmar que el pipeline sirve»
CORRECTO:   se prepara todo y se espera la autorización para ejecutar contra producción
```

Fuente: [18·DP8](../18-despliegue-e-infraestructura.md#dp8--correr-contra-producción-lo-autoriza-el-humano)
