# Especificación del módulo Medición  ·  `[CAPA 3]`

- **Slug del módulo:** `medicion`
- **Estado:** aprobada, el 2026-08-31 por Ing. José Dúmar Jiménez Ruíz
- **Versión del producto:** 2, según [cvds/implementacion/README.md](../../cvds/implementacion/README.md)

---

## 1. Propósito y alcance

Que lo que ya se conversó con el agente se pueda **buscar**, y que lo que el usuario tuvo que repetir se pueda **contar**. Una corrección que se repite no es un descuido de quien corrige: es una regla que falta, y hoy ese patrón se pierde en archivos que nadie vuelve a abrir.

- **Dentro de alcance:** indexar las conversaciones que el histórico ya escribe y buscar en ellas (`F-033`), y decir qué correcciones se repiten, con cuántas veces y en qué sesiones (`F-034`).
- **Fuera de alcance:** medir el tiempo que se gasta revisando (`F-032`, versión 5); traer conversaciones de otras herramientas; y **decidir la regla que falta**, que la sigue decidiendo el usuario por la cadena.

## 2. Contexto — qué hay hoy

Las conversaciones **ya se escriben**: [validadores/historico.py](../../validadores/historico.py), llamado por el enganche de la herramienta, anota cada mensaje del usuario y cada respuesta del agente en `historico-chat/` del proyecto, con la hora del reloj de la máquina y **con las claves ya tapadas** por [validadores/enmascarar.py](../../validadores/enmascarar.py).

Lo que no hay es forma de buscar en ellas. Para saber cuándo se dijo algo hay que abrir archivo por archivo, y para saber cuántas veces, no hay forma.

Del lado de la plataforma ya existe lo que hace falta: [plataforma/nucleo/almacen/core.py](../../plataforma/nucleo/almacen/core.py) guarda texto y mantiene un índice que se puede borrar y rehacer, y el módulo Proyectos sabe dónde vive el código de cada proyecto conectado.

**Este módulo no cambia cómo se escribe la conversación.** El enganche sigue siendo el que escribe; la plataforma solo lee lo que ya está.

## 3. Supuestos, dependencias y preguntas abiertas

- **Supuestos:** que lo que el enganche escribe alcanza. Si algún día una conversación no pasa por ahí, no se indexa y **nadie se entera**. Está declarado en la `HU-001` como el supuesto que puede fallar en silencio.
- **Dependencias:** el módulo Proyectos (`F-001`), que dice dónde vive cada proyecto conectado. `F-034` depende de `F-033`: sin lo indexado no hay qué contar.
- **Preguntas abiertas:** agrupar dos formas distintas de decir lo mismo (`CA-3` de `F-034`) puede no salir sin instalar algo que salga a la red. Si no sale, se entrega el conteo exacto y se declara la deuda; no se simula el agrupamiento.

## 4. Reglas de negocio

1. **El texto sigue siendo la fuente; el índice se puede borrar y rehacer.** Baja de [`DA-01`](../../cvds/diseno/decisiones-de-arquitectura.md): la base solo guarda lo que hace falta para buscar.
2. **Ninguna credencial entra a lo indexado.** Baja de `RN-9` del análisis. Ya se cumple antes de llegar acá: lo que se escribe viene tapado desde el enganche. Este módulo **lo comprueba**, no lo supone.
3. **Indexar no modifica, no mueve y no borra ningún archivo del histórico.** Es el caso de «que NO pase» del módulo.
4. **El texto de la conversación no se copia a la plataforma.** Se indexa donde ya vive, versionado en el repositorio del proyecto. Es la excepción declarada a `DA-01`, y su porqué está en la §12.
5. **Mostrar el patrón, nunca decidir la regla.** El reporte dice qué se repitió; escribir la regla que falta sigue siendo del usuario, por la cadena.
6. **Qué cuenta como corrección: todo mensaje del usuario, menos una lista cerrada de confirmaciones.** Decidido con el usuario el 2026-08-31. Ningún programa lee intención; lo que sí puede es no contar «si», «hágale», «siga» ni «ok», que son la mitad de lo que se escribe y no corrigen nada. La lista está escrita en el código, es corta, y se lee.

## 5. Modelo de datos

- **Entidades:** `Sesión` y `Mensaje`, las dos ya nombradas en la sección 2 del [modelo de datos](../../cvds/diseno/modelo-de-datos.md), acá con su diccionario.

**Sesión** — un tramo de trabajo con el agente, uno por archivo del histórico.

| Campo | Qué significa | Valores | Obligatorio |
|---|---|---|---|
| `proyecto` | De cuál salió | Identificador de proyecto | Sí |
| `archivo` | Dónde vive el texto, relativo a la raíz del proyecto | Ruta | Sí |
| `fecha` | El día de la sesión | Fecha | Sí |
| `tema` | Cómo se llama la sesión, si tiene nombre | Texto, o vacío | No |
| `huella` | La del archivo cuando se indexó | Texto | Sí |

**Mensaje** — cada turno de la conversación.

| Campo | Qué significa | Valores | Obligatorio |
|---|---|---|---|
| `sesión` | A cuál pertenece | Identificador de sesión | Sí |
| `orden` | En qué lugar de la conversación va | Entero | Sí |
| `quién` | Quién habló | `usuario` o `agente` | Sí |
| `cuándo` | La hora que el enganche anotó | Fecha y hora | Sí |
| `texto` | Lo dicho, tal como quedó escrito | Texto | Sí |

- **Dónde vive:** el texto, en `historico-chat/` del proyecto, que es donde el enganche lo escribió. El índice, en la base local, **reconstruible leyendo esos archivos**.
- **Valores configurables:** ninguno en esta versión.
- **Migración:** no aplica. Lo ya conversado entra al indexar por primera vez.

## 6. Comportamiento y flujos

**Indexar un proyecto.** Se recorre `historico-chat/` del proyecto conectado, se lee cada archivo de sesión y se parte en mensajes por las marcas que el enganche escribe. Cada sesión y cada mensaje entran al índice. La `huella` del archivo se guarda para saber qué cambió.

- Archivo que no se puede leer: se reporta y **no se detiene el resto**. Un archivo roto no puede llevarse lo que ya se sabía.
- Archivo sin marcas reconocibles: se cuenta como sesión sin mensajes, y se dice. Cero mensajes es un dato, no un silencio.
- Proyecto con la ruta perdida: no se indexa, y se responde con la ruta que se buscó. Lo ya indexado se sigue pudiendo buscar.

**Rehacer el índice.** Se borra entero y se vuelve a leer desde los archivos. Es la comprobación de que perder la base no pierde información.

**Buscar.** Se recibe una palabra o una frase y se responde con las sesiones donde aparece, y **en qué mensaje** de cada una. Sin coincidencias, se dice que no hubo ninguna, en vez de devolver una lista vacía sin explicación.

**Decir qué se repite** (`F-034`). Se recibe un período. Se miran los mensajes del usuario, se agrupan los que dicen lo mismo y se responde con los más repetidos, cada uno con cuántas veces y en qué sesiones. Si no hay nada repetido, se dice; no se rellena.

## 7. Interfaz

Una pantalla de búsqueda y una de lo repetido, dentro de la vista de un proyecto. `F-033` puede terminarse **sin pantalla**: su usuario es el sistema, y su valor lo cobra `F-034`.

## 8. Permisos y autorización

**Desde `EP-022` hay cuentas, dos grupos y permisos.** Quién puede qué está en la [especificación de Acceso](../acceso/spec.md) §8. Acá vale la regla general: **el agente no aprueba, no publica versiones, no deroga reglas y no administra cuentas.**

## 9. Marco normativo

**Sí aplica, y es lo delicado del módulo.** Una conversación de trabajo puede traer nombres de personas, de clientes y de sistemas. Lo que este módulo guarda es texto que **el usuario ya escribió y ya versionó** en su propio repositorio: no se recoge nada nuevo ni se saca nada afuera. Las credenciales no entran, y eso se comprueba (`RN-2`), no se supone.

## 10. Plan de pruebas

| Qué se prueba | Casos |
|---|---|
| Indexar | Sesión con mensajes · archivo ilegible · archivo sin marcas · proyecto con la ruta perdida |
| Rehacer | Índice borrado entero y reconstruido; tiene que volver completo |
| Buscar | Palabra que se dijo · palabra que no se dijo nunca · palabra que aparece en varias sesiones |
| Credenciales | Buscar en lo indexado las formas de clave que `secretos.py` conoce; no debe aparecer ninguna |
| Rendimiento | Indexar lo acumulado hoy, que es volumen real, y decir cuánto tardó |
| Que NO pase | Que indexar modifique, mueva o borre un archivo del histórico |

## 11. Criterios de aceptación

- `CA-1` Lo que una sesión conversó se encuentra buscando una palabra suya, y se ve en qué mensaje se dijo.
- `CA-2` El índice se borra entero y se rehace completo, leído desde los archivos.
- `CA-3` Ninguna credencial aparece en lo indexado.
- `CA-4` Indexar no modifica, no mueve y no borra ningún archivo del histórico.
- `CA-5` Una búsqueda sin coincidencias lo dice.
- `CA-6` Se pide un período y salen las correcciones más repetidas, cada una con cuántas veces y en qué sesiones.
- `CA-7` Si no hay nada repetido, se dice.

Los cinco primeros son de `F-033`; los dos últimos, de `F-034`.

## 12. Decisiones tomadas

| Decisión | Alternativa descartada | Por qué |
|---|---|---|
| **El texto no se copia a la plataforma: se indexa donde vive** | Copiarlo a `datos/`, como el resto de lo que la plataforma guarda | Ya está escrito y versionado en el repositorio del proyecto. Copiarlo crea una segunda verdad que envejece, y duplica en la plataforma un texto que el proyecto puede seguir cambiando. Es una excepción a `DA-01` y por eso se escribe acá: **lo que `DA-01` protege —que perder la base no pierda información— se cumple igual**, porque el índice se rehace leyendo esos archivos |
| El índice guarda el texto del mensaje | Guardar solo dónde está y volver a abrir el archivo al mostrar | `CA-1` pide ver **en qué mensaje** se dijo; abrir el archivo en cada resultado leería el disco entero para una búsqueda |
| Un archivo ilegible se reporta y no detiene el resto | Fallar la indexación entera | Un archivo roto no puede llevarse lo que ya se sabía |
| `F-033` puede cerrarse sin pantalla | Exigirle interfaz | Su usuario es el sistema; el valor para el usuario lo cobra `F-034`, y atarlas obligaría a construir las dos juntas |
| Si agrupar frases parecidas no sale sin red, se entrega el conteo exacto | Simular el agrupamiento con una lista de sinónimos escrita a mano | Una lista escrita a mano acierta en los casos que uno se imagina y falla en los que duelen. Contar exacto y **declarar lo que no agrupa** dice la verdad |

## 13. Trazabilidad

| Funcionalidad | Requisito | Historia | Fase que lo construye |
|---|---|---|---|
| F-033 | RF-33 | [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-001-buscar-en-lo-conversado/HU-001-buscar-en-lo-conversado.md](../epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-001-buscar-en-lo-conversado/HU-001-buscar-en-lo-conversado.md) | [A-EP-011-HU-001-lo-conversado-se-indexa-y-se-busca](../epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-001-buscar-en-lo-conversado/A-EP-011-HU-001-lo-conversado-se-indexa-y-se-busca/estado-fase.md), cerrada el 2026-08-31 |
| F-034 | RF-34 | [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-002-ver-que-correccion-se-repite/HU-002-ver-que-correccion-se-repite.md](../epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-002-ver-que-correccion-se-repite/HU-002-ver-que-correccion-se-repite.md) | [A-EP-011-HU-002-lo-que-se-repitio-sale-contado](../epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-002-ver-que-correccion-se-repite/A-EP-011-HU-002-lo-que-se-repitio-sale-contado/estado-fase.md), cerrada el 2026-08-31 |
| F-032 | RF-32 | [HU-003 Medir el tiempo que se gasta revisando](../epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-003-medir-el-tiempo-que-se-gasta-revisando/HU-003-medir-el-tiempo-que-se-gasta-revisando.md) | [Y-EP-011-HU-003-la-linea-base-dice-que-es-reconstruida](../epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-003-medir-el-tiempo-que-se-gasta-revisando/Y-EP-011-HU-003-la-linea-base-dice-que-es-reconstruida/estado-fase.md), cerrada el 2026-09-01 |

## 14. Cruces con otros módulos

- **Proyectos:** dice dónde vive el código de cada proyecto conectado; sin eso no hay dónde buscar el histórico.
- **Almacén:** aporta el índice reconstruible y la huella; este módulo indexa por fuera de `datos/`, que es la excepción de la §12.
- **Auditoría:** guarda **qué se hizo**; esto guarda **qué se conversó**. No son lo mismo, y `RN-4` de Auditoría sigue diciendo que la conversación no entra allá.
- **Memoria:** una corrección que se repite es candidata a anotación, pero **la anotación la escribe el usuario**, no este módulo.

---

## 15. Cambios después de aprobada

| Fecha | Qué cambió | Por qué | Aprobado por |
|---|---|---|---|
| 2026-08-31 | Entra la `RN-6` de la §4: qué cuenta como corrección | La `HU-002` no podía abrirse sin eso, y era el único ítem que le faltaba a su lista de listo. La especificación decía **qué se cuenta** y no **qué es lo que se cuenta** | Ing. José Dúmar Jiménez Ruíz |
