# Plan de Trabajo — Fase H-EP-008-HU-004-un-proyecto-conectado-se-administra (módulo Proyectos)   ·   `[CAPA 3]`

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `H-EP-008-HU-004-un-proyecto-conectado-se-administra` |
| **Épica** | [EP-008 Los proyectos se administran desde un solo lugar](../../epica.md) |
| **HU** | [HU-004 Administrar un proyecto conectado](../HU-004-administrar-un-proyecto-conectado.md), una sola |
| **Módulo** | Proyectos |
| **Especificación** | [documentacion/proyectos/spec.md](../../../../proyectos/spec.md), §1, §6, §7 y §12 |
| **Versión del producto** | 1, fase H de ocho |
| **Fecha apertura** | 2026-08-25 |
| **Rama** | Una rama propia de la fase, que se integra al cerrarla |

---

## 1. Objetivo y alcance

**Qué se busca.** Que equivocarse al conectar un proyecto deje de ser permanente.

**Qué entra.** Desconectar un proyecto sin borrar su documentación, renombrarlo sin mover su carpeta, corregir la versión de reglas que declara, y la confirmación de los tres. También la confirmación al conectar, que la especificación exige desde el principio y la fase B no construyó.

**Qué no entra.** Borrar la documentación de un proyecto: desconectar no borra, y eso ya está decidido. Corregir la ruta perdida, que es la fase C. Configurar qué reglas rigen ahí, que es de la versión 5.

## 2. Análisis previo: línea base verificada

**Qué se leyó antes de escribir.** La historia con sus cinco criterios, la especificación del módulo, y el código de la fase B: [nucleo/proyectos/core.py](../../../../../plataforma/nucleo/proyectos/core.py) y [models.py](../../../../../plataforma/nucleo/proyectos/models.py).

**Qué ya está construido y se usa tal cual.**

| Qué se necesita | Qué ya existe |
|---|---|
| Escribir sobre la ficha de un proyecto | El almacén, con el comprobante de la auditoría |
| Que el cambio quede registrado | `con_constancia`, que la fase B ya usa para conectar |
| Que renombrar no mueva la carpeta | El identificador se guarda aparte del nombre desde la fase B, **a propósito para esto**. Hoy nada lo usa |
| Comprobar la versión declarada | `nucleo/seguridad/reglas.py`, tal cual |
| Rehacer el índice desde el texto | `reconstruir_indice`, que hay que enseñarle a leer el campo nuevo |

**Qué falta y hay que decidir acá.** Cómo se marca un proyecto desconectado. Como el índice se rehace desde el texto, **la marca tiene que estar en la ficha**, no solo en la base.

### 2.1 Archivos que se crean o modifican

`plataforma/nucleo/proyectos/` y sus plantillas. Se modifica `config/urls.py` para las rutas nuevas.

**Nada de esta fase escribe dentro de la carpeta del proyecto**, ni siquiera al desconectarlo. Es `CA-05` de la historia y el caso de «que NO pase» del plan de pruebas.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Por qué |
|---|---|---|
| Desconectar escribe una fecha en la ficha; no borra ni mueve nada | Borrar la ficha, o mover su carpeta a otro lado | Desconectar tiene que ser reversible, y borrar no lo es. Mover la carpeta rompe cualquier enlace que apunte a ella |
| La marca va en la ficha, no solo en el índice | Marcarlo en la base | `DA-01`. Si la marca vive solo en la base, rehacer el índice resucita al proyecto desconectado |
| Los desconectados se siguen viendo, en una sección aparte | Que desaparezcan de la pantalla | Si desaparecen, nadie sabe que su documentación sigue ahí, y el usuario no tiene cómo volver a conectarlos ni cómo mirar lo que quedó |
| Renombrar cambia el nombre en la ficha, y el identificador nunca | Recalcular el identificador con el nombre nuevo | Mover la carpeta al renombrar rompe los enlaces y la historia. Por eso el identificador se guardó aparte desde la fase B |
| Corregir la versión la vuelve a leer del proyecto, no la pide escrita | Que el usuario la teclee | La misma razón de la fase B: teclearla es la forma de que quede un número que no existe |
| Los cambios piden confirmación en una pantalla propia | Una ventana del navegador | La confirmación tiene que decir **qué va a pasar y qué no**, y eso no cabe en una ventana del navegador. En particular: que la documentación se queda al desconectar, y que vuelve al reconectar |
| Reconectar una ruta de un desconectado lo reactiva | Crear un proyecto nuevo que herede esa carpeta | Decidido por el usuario el 2026-08-25. Crear uno nuevo dejaría la documentación del anterior sin dueño |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | Cómo se resolvió |
|---|---|---|
| 1 | Un proyecto desconectado, ¿libera su ruta para que se pueda volver a conectar? | **Sí la libera, y volver a conectar esa carpeta reactiva el proyecto desconectado**: mismo identificador, misma documentación. No se crea uno nuevo. Decidido por el usuario el 2026-08-25 |

**Por qué esa y no las otras dos.** Si la ruta siguiera tomada, desconectar no serviría para lo que se pidió: conectar mal y no poder volver a conectar bien es el mismo problema con otro nombre. Y si al reconectar se creara un proyecto nuevo, la documentación del anterior quedaría huérfana: una carpeta con cosas adentro que ya no es de nadie.

**Qué agrega esta decisión al trabajo.** Reconectar deja de ser un caso de `conectar` y pasa a ser uno propio: hay que reconocer que esa ruta pertenece a un desconectado y reactivarlo. Y **la pantalla tiene que avisarlo antes de confirmar**, con un «este proyecto ya estuvo conectado, con documentación guardada», porque si el usuario quería empezar de cero con esa carpeta, va a recibir la historia vieja sin haberla pedido.

## 3. Desglose de tareas

| # | Tarea | Entregable |
|---|---|---|
| 1 | Resolver la duda de la sección 2.7 | ✅ Resuelta el 2026-08-25, con su porqué escrito |
| 2 | Desconectar, dejando la documentación | El proyecto sale de la lista y su carpeta sigue con lo que tenía |
| 3 | Renombrar, sin mover la carpeta | El nombre cambia y la carpeta es la misma |
| 4 | Corregir la versión declarada | Se relee del proyecto y se comprueba contra las publicadas |
| 5 | La confirmación de los cuatro, y su registro | Cada uno pregunta antes, y queda en la auditoría |
| 6 | La sección de desconectados en la pantalla | Se ven, y se ve que su documentación sigue ahí |
| 7 | Reconectar: reactivar el desconectado en vez de crear uno nuevo | Vuelve con su identificador y su documentación, avisando antes de confirmar |

## 4. Secuencia de ejecución

1 → 2 → 3 → 4 → 5 → 6 → 7. La tarea 1 era la puerta y ya está pasada: su respuesta agregó la tarea 7, que no estaba en el plan original.

## 5. Verificación de criterios de aceptación

| Criterio | Cómo se verifica |
|---|---|
| `CA-01` desconectar saca el proyecto y deja su documentación | Se desconecta y se busca su carpeta, que tiene que seguir con lo suyo |
| `CA-02` renombrar no mueve la carpeta | Se anota dónde está antes, se renombra, y se comprueba que es la misma |
| `CA-03` la versión corregida se vuelve a comprobar | Se corrige contra una versión que no existe |
| `CA-04` los cuatro piden confirmación y quedan registrados | Se cuentan los registros antes y después de cada uno |
| `CA-05` que NO pase: desconectar toca el proyecto | Se compara la carpeta del proyecto archivo por archivo |

## 6. Datos y ambiente de prueba

La propia máquina, sin red. Proyectos de mentira creados y borrados por la propia prueba. **Ninguna carpeta real del usuario como conejillo**, y menos en una fase que desconecta.

## 7. Reversión

Se descarta la rama de la fase. Lo que esta fase escribe son fechas y nombres dentro de fichas que ya existen; nada se borra, así que revertir no pierde nada.

## 8. Producción y migración

Las fichas escritas por la fase B no tienen el campo nuevo. **Una ficha sin ese campo se lee como un proyecto conectado**, que es lo correcto: no hay que migrar nada.

## 9. Reglas del estándar aplicadas

| Regla | Cómo se cumple acá |
|---|---|
| `02·F2` sin especificación acordada no hay código | La del módulo Proyectos ya define cómo se comporta desconectar |
| `02·F4` el plan va con su plan de pruebas | Se presentan y se aprueban juntos |
| `01·C7` ante dos lecturas, preguntar | La duda de la sección 2.7 detiene la fase |
| `00·N1` ningún cambio de estado sin aprobación | Los cuatro piden confirmación, que es la tarea 5 |
| `20·M12` buscar antes de crear | El identificador aparte del nombre ya existía desde la fase B, hecho para esto |

## 10. Riesgos y bloqueos

| # | Riesgo | Qué se hace |
|---|---|---|
| 1 | Que desconectar termine borrando algo por descuido | Es `CA-01` y el caso de «que NO pase». Se comprueba que la carpeta de documentación siga con lo que tenía, no solo que exista |
| 2 | Que renombrar mueva la carpeta sin que nadie lo note | Se anota la ruta de la carpeta antes y se compara después. Un nombre nuevo con la carpeta movida se ve igual de bien en la pantalla |
| 3 | Que la confirmación se convierta en un clic más y nadie la lea | La confirmación dice qué va a pasar **y qué no**: en particular, que la documentación se queda |

## 11. Definition of Done

- ☐ La duda resuelta y escrita.
- ☐ Desconectar saca el proyecto de la lista y su documentación sigue con lo que tenía.
- ☐ Renombrar cambia el nombre y la carpeta es la misma de antes.
- ☐ Corregir la versión la vuelve a comprobar, y una que no existe no se guarda.
- ☐ Los cuatro cambios piden confirmación y quedan en la auditoría.
- ☐ Los desconectados se ven, y se ve que su documentación sigue ahí.
- ☐ Reconectar la ruta de un desconectado lo reactiva, con su documentación, avisando antes.
- ☐ Comprobado que la carpeta del proyecto no cambió al desconectarlo.

## 12. Seguimiento

El estado vive en [estado-fase.md](estado-fase.md), y se actualiza al cambiar de estación.

## 13. Cierre

La fase cierra cuando los ocho puntos de la sección 11 tengan veredicto. Lo que quede sin hacer se declara como deuda en el documento de cierre.

---

**Aprobado por Ing. José Dúmar Jiménez Ruíz, el 2026-08-25.** Se aprobó junto con [plan_pruebas.md](plan_pruebas.md) y con la [HU-004](../HU-004-administrar-un-proyecto-conectado.md).
