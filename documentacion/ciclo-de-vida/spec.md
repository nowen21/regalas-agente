# Especificación del módulo Ciclo de vida  ·  `[CAPA 3]`

- **Slug del módulo:** `ciclo_de_vida`
- **Estado:** aprobada, el 2026-09-01 por Ing. José Dúmar Jiménez Ruíz
- **Versión del producto:** 2, según [cvds/implementacion/README.md](../../cvds/implementacion/README.md)

---

## 1. Propósito y alcance

Que un documento del ciclo se complete sin salir de la plataforma: se dice qué molde sigue, qué huecos le faltan, y se escribe lo que va en cada uno.

- **Dentro de alcance:** llenar los documentos del ciclo desde la plataforma (`F-014`), que es lo que la versión 2 necesita.
- **Fuera de alcance:** crear épicas, historias y fases (`F-011`), ver en qué estación va cada fase (`F-012`) e impedir avanzar sin la puerta cumplida (`F-013`). Las tres son de la versión 5 y esta especificación se amplía cuando lleguen.
- **Fuera también:** redactar libre. Decidido con el usuario el 2026-09-01: la plataforma llena huecos, no reemplaza al editor.

## 2. Contexto — qué hay hoy

Los documentos entran a la plataforma **solo por importación**. El módulo Importación reconoce cada archivo por su nombre y su ubicación, y trajo 1 054 documentos de este repositorio. Lo que no hay es forma de escribir en ellos: la plataforma mira.

Cada documento del ciclo tiene su molde en `plantillas/ciclo-vida-proyectos/`, y los moldes marcan sus huecos con la convención de [`13·DOC19`](../../base/13-documentacion/reglas/DOC19-marca-con-la-misma-marca-los-espacios-por-llenar.md).

**Lo que cuesta hoy, medido.** El expediente del 2026-08-31 contó **31 documentos de este repositorio con espacios sin llenar**. Nadie los vio: se descubrieron contando la marca, que es justo lo que una persona no hace releyendo.

**Módulo nuevo, sin código previo.**

## 3. Supuestos, dependencias y preguntas abiertas

- **Supuestos:** que los moldes marcan sus huecos con la convención del estándar. Un molde que no la use queda al descubierto, en vez de taparse.
- **Dependencias:** Importación, que dice qué tipo es cada archivo; Proyectos, que dice de cuál son y dónde vive; Auditoría, donde queda registrado lo que se escribe.
- **Lo que no bloquea:** la ficha de `F-014` dice depender de `F-011`. Esa columna dice qué tiene que existir, no qué construir antes, y lo que se necesita lo trae la importación. Comprobado el 2026-09-01 sobre las 35 fichas.
- **Preguntas abiertas:** si llenar por huecos resulta cómodo de verdad. Se responde llenando un documento real de punta a punta, no un ejemplo de tres huecos.

## 4. Reglas de negocio

1. **El molde de un documento se decide por su tipo**, que Importación ya reconoce. Nunca por parecido.
2. **Un hueco se cuenta por su marca**, no por parecer incompleto. La convención no se amplía por cuenta propia.
3. **Lo que llena la instalación no se le pregunta al usuario**, y se dice aparte para que nadie crea que se perdió.
3.1. **Solo el hueco cierto entra en la cuenta.** El posible se lista aparte: en un documento escrito no se distingue de una cita.
4. **La fuente es el texto, y el texto es el del proyecto.** Lo escrito va al **archivo original**, no a la copia de `datos/`. La copia es índice; la base tampoco guarda contenido ([`DA-01`](../../cvds/diseno/decisiones-de-arquitectura.md)).
5. **Se toca solo el hueco.** Ni una línea más del documento cambia al guardar.
6. **Si el archivo cambió por fuera, se avisa y no se escribe encima.**
7. **Escribir queda registrado en la auditoría** ([`DA-12`](../../cvds/diseno/decisiones-de-arquitectura.md)): quién, cuándo, qué documento y qué hueco.
8. **Un tipo que no se reconoce lo dice**, en vez de recibir el molde de otro.

## 5. Modelo de datos

- **Entidades:** ninguna nueva que se guarde. **Los huecos se calculan al pedirlos**, leyendo el archivo. Guardarlos crearía una segunda verdad que envejece en cuanto alguien edite el documento por fuera, que es lo que `DA-01` viene a evitar.

| Qué | Dónde vive | Por qué ahí |
|---|---|---|
| Los huecos de un documento | En ninguna parte: se calculan | El archivo puede cambiar por fuera en cualquier momento |
| Lo que se escribe | En el archivo del proyecto | Es la fuente, y se lee sin la plataforma |
| Que se escribió, y qué | Auditoría | `DA-08`: se registra cada acción que cambia algo |

- **Valores configurables:** ninguno en esta versión.
- **Migración:** no aplica.

### 5.1 Las clases de hueco, y cuál es cierta

Es lo que la `HU-001` pedía declarar. **Se midió antes de construir, y la medición cambió el diseño.**

| Clase | Cómo se escribe | Qué se hace con ella |
|---|---|---|
| **Cierto** | `«…»` | Se cuenta y se pregunta. Es lo que el usuario tiene que llenar |
| **Posible** | `«NOMBRE»` que también está en el molde | Se lista **aparte**, sin entrar en la cuenta |
| **De instalación** | `«RUTA-ESTANDAR»` | No se pregunta: la reemplaza [validadores/instalar.py](../../validadores/instalar.py). Se dice aparte |
| **Citada** | La marca dentro de código, cercado o en la misma línea | **No es un hueco.** Ahí se escribe para que se vea |

**Por qué el hueco con nombre no es cierto.** En un documento ya escrito **no se distingue de una cita**, porque en esta casa se cita con esas mismas comillas. Medido el 2026-09-01 sobre las 130 historias de usuario reales:

| Prueba | Marcas que sobreviven |
|---|---|
| Cualquier `«...»` | 341 |
| Solo las que están en el molde | 75, en 17 documentos |
| Las que además siguen en la línea del molde | **0** |

Las 75 son el autor usando el vocabulario del molde como etiqueta, del estilo de `«Documentación»`, `«Backend»` y `«Pruebas»`, y ninguna es un hueco. Contarlas daría por incompleto un documento bien escrito, que es el mismo error que ya costó 559 documentos incompletos en vez de 31.

**Por qué se listan igual, en vez de ignorarlas.** Cuando `F-011` cree documentos desde el molde, en la versión 5, el documento **será** el molde y entonces cada hueco con nombre sí es cierto. Dejarlas listadas ahora evita rehacer la pieza; meterlas en la cuenta arruinaría la cuenta hoy.

**La cuenta que manda es la de los ciertos**, y coincide con la que ya da el módulo Expediente. Que las dos digan lo mismo no es casualidad: sale del mismo sitio.

### 5.2 Qué molde le toca a cada tipo

Importación reconoce **19 tipos**. De ellos, **17 tienen molde** y dos no. Se declara acá porque deducirlo del nombre falla: tres viven fuera de `plantillas/ciclo-vida-proyectos/`.

| Tipo de documento | Molde |
|---|---|
| épica | `ciclo-vida-proyectos/03-epica.md` |
| historia de usuario | `ciclo-vida-proyectos/04-HU.md` |
| especificación de módulo | `ciclo-vida-proyectos/06-especificacion-modulo.md` |
| plan de trabajo | `ciclo-vida-proyectos/07-plan-trabajo.md` |
| plan de pruebas | `ciclo-vida-proyectos/08-plan-pruebas.md` |
| resultado de pruebas | `ciclo-vida-proyectos/09-resultado-pruebas.md` |
| estado de fase | `ciclo-vida-proyectos/10-estado-fase.md` |
| funcionalidad implementada | `ciclo-vida-proyectos/11-funcionalidad-implementada.md` |
| inventario de funcionalidades | `ciclo-vida-proyectos/02-inventario-funcionalidades.md` |
| estudio de factibilidad | `ciclo-vida-proyectos/12-estudio-factibilidad.md` |
| acta de constitución | `ciclo-vida-proyectos/13-acta-de-constitucion-y-plan-de-proyecto.md` |
| modelo de datos | `ciclo-vida-proyectos/14-modelo-de-datos.md` |
| diseño de interfaz | `ciclo-vida-proyectos/15-diseno-de-interfaz.md` |
| contrato de la interfaz | `ciclo-vida-proyectos/16-documentacion-de-api.md` |
| señales | `senales.md` |
| decisiones de arquitectura | `cvds/diseno/decisiones-de-arquitectura.md` |
| etapa del ciclo de vida | `cvds/<etapa>/README.md`, la de su etapa |

**Los dos que no tienen molde, y se dicen:**

| Tipo | Por qué no tiene |
|---|---|
| índice | Es el `README.md` de una carpeta cualquiera. No sigue un molde: describe lo que hay dentro |
| registro de versión | La adopción de una versión se anota, y nunca se escribió su molde |

**No se les asigna el más parecido.** Se listan como reconocidos y sin molde, que es un dato; acomodarlos lo convertiría en una suposición.

## 6. Comportamiento y flujos

**Ver qué le falta a un documento.** Se recibe qué documento. Se mira su tipo, se nombra su molde y se recorre el texto buscando la marca. Se devuelve:

- **Cuántos huecos** le faltan al usuario.
- **Cada uno** con su clase, su línea y el texto que lo rodea.
- **Los posibles**, en su propia lista y fuera de la cuenta.
- **Los de instalación**, contados aparte.
- Si el tipo no se reconoce, o si no tiene molde, se dice y no se inventa uno.

Un documento sin huecos lo dice, en vez de devolver una lista vacía.

**Llenar un hueco.** Se recibe qué documento, qué hueco y qué se escribe.

- Antes de escribir se comprueba que **el archivo sigue como estaba** cuando se leyó. Si cambió, se avisa y no se escribe.
- Se reemplaza **solo** ese hueco. El resto del archivo queda idéntico, carácter por carácter.
- Se escribe de forma que **el archivo nunca quede a medias**: se prepara completo y se pone en su sitio de un golpe.
- Queda registrado en la auditoría.
- Se devuelve cuántos huecos quedan.

**Dónde se escribe: en el archivo original del proyecto.** Decidido con el usuario el 2026-09-01. **Es la primera vez que la plataforma escribe fuera de `datos/`**: hasta hoy solo lee los proyectos y escribe sus propias copias. Escribir en la copia dejaría el proyecto igual, que es no hacer nada; y la copia se rehace importando, así que lo escrito ahí se perdería a la primera.

**Y después de escribir se vuelve a traer ese documento**, para que la copia y el original no se separen. Si no, la cuenta de huecos seguiría mostrando el que ya se llenó.

**Cómo se sabe que el archivo cambió por fuera.** Se guarda la huella del contenido leído y se compara antes de escribir. No hace falta más: si la huella no coincide, alguien lo tocó, y ahí la respuesta correcta es avisar, no adivinar cuál de los dos cambios vale.

**Cómo se ubica un hueco.** Por su posición **y** por el texto que lo rodea. La posición sola no basta: si el documento cambió, apunta a otra parte.

## 7. Interfaz

Una pantalla dentro de la vista de un documento: la lista de lo que falta, y un campo por hueco. **La `HU-001` puede terminarse sin pantalla**, con orden de consola, como se hizo en Medición y en Expediente.

## 8. Permisos y autorización

Un solo usuario, sin credenciales propias, igual que el resto de la plataforma. Lo que el registro distingue es **quién escribió**: el usuario o el agente.

## 9. Marco normativo

**Aplica más de lo que parecía.** Este módulo no saca nada del sistema, pero **es el primero que escribe fuera de `datos/`**: toca los archivos del proyecto del usuario. Lo que lo hace seguro no es prohibirlo, es que todo cambio quede registrado y que nada se escriba encima sin avisar. Lo que sí aplica es que **ninguna credencial se escriba en un documento** ([`00·N6`](../../base/00-nucleo-blindado.md)): lo que se guarda es lo que el usuario tecleó, y eso no se filtra por cuenta del programa. Que un documento del ciclo no es sitio para una clave es una regla del estándar, no de este módulo.

## 10. Plan de pruebas

| Qué se prueba | Casos |
|---|---|
| Ver qué falta | Documento con huecos · sin huecos · de tipo desconocido · de tipo reconocido sin molde |
| Las tres clases | Con nombre · sin nombre · de instalación, sobre un molde que tenga las tres |
| Llenar | Un hueco cualquiera · el último que quedaba · uno de un documento con tablas |
| **Que nada más cambie** | Comparar el archivo entero antes y después, con el hueco descontado |
| Que NO pase | Guardar cuando el archivo cambió por fuera · llenar un documento sin huecos |
| Integridad | Que un guardado interrumpido no deje el archivo a medias |
| Registro | Que escribir quede en la auditoría, con el hueco nombrado |
| Sobre lo real | Los 31 documentos incompletos de este repositorio |

## 11. Criterios de aceptación

- `CA-1` Se dice qué molde sigue el documento.
- `CA-2` Se listan los huecos, con cuántos son y dónde.
- `CA-3` Solo el hueco cierto entra en la cuenta; el posible se lista aparte.
- `CA-4` Lo que llena la instalación no se cuenta como pendiente, y no desaparece en silencio.
- `CA-5` Un tipo desconocido lo dice.
- `CA-6` Lo escrito queda en el archivo y se lee sin la plataforma.
- `CA-7` **Nada cambia fuera del hueco.**
- `CA-8` La cuenta de huecos baja en uno.
- `CA-9` Si el archivo cambió por fuera, se avisa y no se escribe encima.
- `CA-10` Escribir queda registrado.

Los cinco primeros son de la `HU-001`; los cinco últimos, de la `HU-002`.

## 12. Decisiones tomadas

| Decisión | Alternativa descartada | Por qué |
|---|---|---|
| **Se llena por huecos** | Un cuadro de texto libre por documento | Decidido con el usuario el 2026-09-01. Redactar libre compite con el editor del usuario y pierde; pedir el hueco con su molde es lo que el editor no puede hacer |
| **Los huecos se calculan al pedirlos** | Guardarlos en la base | El archivo puede cambiar por fuera, y una lista guardada envejece sin avisar (`DA-01`) |
| **Solo el hueco cierto entra en la cuenta** | Contar también los que tienen nombre | Medido: de 341 marcas en las 130 historias reales, **ninguna** es un hueco con nombre sin llenar. Contarlas daría por incompleto un documento bien escrito |
| **El posible se lista aparte, en vez de ignorarse** | Descartarlo | Cuando `F-011` cree documentos desde el molde, el documento será el molde y entonces sí serán ciertos |
| **La marca de instalación se aparta** | Tratar toda marca igual | Sin apartarla, el usuario recibe 134 preguntas que no le tocan |
| **Un hueco se ubica por posición y por su contexto** | Solo por posición | Si el documento cambió, la posición sola apunta a otra parte |
| **Se escribe en el archivo original del proyecto** | Escribir en la copia de `datos/` | Decidido el 2026-09-01. La copia se rehace al importar, así que lo escrito ahí se pierde; y el proyecto quedaría igual, que es no hacer nada |
| **Se compara la huella del archivo antes de escribir** | Escribir y confiar | Es lo único que distingue «nadie lo tocó» de «alguien más escribió» |
| **Un tipo sin molde se lista como tal** | Asignarle el molde más parecido | Acomodarlo a la fuerza convierte un dato en una suposición |

## 13. Trazabilidad

| Funcionalidad | Requisito | Historia | Fase que lo construye |
|---|---|---|---|
| F-014 | RF-14 | [HU-001 Ver qué le falta a un documento](../epicas/EP-013-los-documentos-se-llenan-sin-salir-de-la-plataforma/HU-001-ver-que-le-falta-a-un-documento/HU-001-ver-que-le-falta-a-un-documento.md) | [A-EP-013-HU-001-los-huecos-de-un-documento-se-ven](../epicas/EP-013-los-documentos-se-llenan-sin-salir-de-la-plataforma/HU-001-ver-que-le-falta-a-un-documento/A-EP-013-HU-001-los-huecos-de-un-documento-se-ven/estado-fase.md), cerrada el 2026-09-01 |
| F-011 | RF-11 | [HU-001 Abrir una fase con sus documentos](../epicas/EP-019-el-ciclo-se-opera-desde-la-plataforma/HU-001-abrir-una-fase-con-sus-documentos/HU-001-abrir-una-fase-con-sus-documentos.md) | [S-EP-019-HU-001-el-nombre-sale-del-identificador](../epicas/EP-019-el-ciclo-se-opera-desde-la-plataforma/HU-001-abrir-una-fase-con-sus-documentos/S-EP-019-HU-001-el-nombre-sale-del-identificador/estado-fase.md), cerrada el 2026-09-01 |
| F-012 | RF-12 | [HU-002 Ver en qué estación va cada fase](../epicas/EP-019-el-ciclo-se-opera-desde-la-plataforma/HU-002-ver-en-que-estacion-va-cada-fase/HU-002-ver-en-que-estacion-va-cada-fase.md) | [T-EP-019-HU-002-la-tabla-manda-sobre-la-frase](../epicas/EP-019-el-ciclo-se-opera-desde-la-plataforma/HU-002-ver-en-que-estacion-va-cada-fase/T-EP-019-HU-002-la-tabla-manda-sobre-la-frase/estado-fase.md), cerrada el 2026-09-01 |
| F-013 | RF-13 | [HU-003 Impedir avanzar sin la puerta cumplida](../epicas/EP-019-el-ciclo-se-opera-desde-la-plataforma/HU-003-impedir-avanzar-sin-la-puerta-cumplida/HU-003-impedir-avanzar-sin-la-puerta-cumplida.md) | [U-EP-019-HU-003-el-rechazo-dice-cual-puerta-falta](../epicas/EP-019-el-ciclo-se-opera-desde-la-plataforma/HU-003-impedir-avanzar-sin-la-puerta-cumplida/U-EP-019-HU-003-el-rechazo-dice-cual-puerta-falta/estado-fase.md), cerrada el 2026-09-01 |
| F-014 | RF-14 | [HU-002 Llenar un hueco desde la plataforma](../epicas/EP-013-los-documentos-se-llenan-sin-salir-de-la-plataforma/HU-002-llenar-un-hueco-desde-la-plataforma/HU-002-llenar-un-hueco-desde-la-plataforma.md) | [B-EP-013-HU-002-el-hueco-se-llena-sin-tocar-lo-demas](../epicas/EP-013-los-documentos-se-llenan-sin-salir-de-la-plataforma/HU-002-llenar-un-hueco-desde-la-plataforma/B-EP-013-HU-002-el-hueco-se-llena-sin-tocar-lo-demas/estado-fase.md), cerrada el 2026-09-01 |

## 14. Cruces con otros módulos

- **Importación:** dice qué tipo es cada archivo. Este módulo **no vuelve a reconocer** nada por su cuenta.
- **Proyectos:** dice de qué proyecto es el documento y dónde vive en el disco.
- **Auditoría:** guarda quién escribió qué, cuándo y en qué hueco.
- **Expediente:** ya cuenta huecos para decir qué está incompleto. **Los dos módulos tienen que contar igual**, o el expediente diría una cosa y esta pantalla otra. La cuenta vive acá y el expediente la usa.

---

## 15. Cambios después de aprobada

| Fecha | Qué cambió | Por qué | Aprobado por |
|---|---|---|---|
| 2026-09-01 | La §5.1 suma la clase **citada**: la marca dentro de código no es un hueco | Corriendo sobre lo real, **51 de 77 marcas contadas estaban dentro de código en línea**. La peor era la especificación de la propia marca | Ing. José Dúmar Jiménez Ruíz |
| 2026-09-01 | La §5.1 pasó de tres clases parejas a una cierta y una posible | Se midió sobre las 130 historias reales: de 341 marcas, ninguna era un hueco con nombre sin llenar | Ing. José Dúmar Jiménez Ruíz |
