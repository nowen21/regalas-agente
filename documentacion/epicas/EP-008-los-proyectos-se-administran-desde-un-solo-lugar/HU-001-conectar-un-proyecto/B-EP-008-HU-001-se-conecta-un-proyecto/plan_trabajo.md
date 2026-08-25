# Plan de Trabajo — Fase B-EP-008-HU-001-se-conecta-un-proyecto (módulo Proyectos)   ·   `[CAPA 3]`

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `B-EP-008-HU-001-se-conecta-un-proyecto` |
| **Épica** | [EP-008 Los proyectos se administran desde un solo lugar](../../epica.md) |
| **HU** | [HU-001 Conectar un proyecto](../HU-001-conectar-un-proyecto.md), la misma de la fase A |
| **Módulo** | Proyectos |
| **Especificación** | [documentacion/proyectos/spec.md](../../../../proyectos/spec.md), aprobada el 2026-08-25 |
| **Versión del producto** | 1, fase B de siete |
| **Fecha apertura** | 2026-08-25 |
| **Rama** | Una rama propia de la fase, que se integra al cerrarla |

---

## 1. Objetivo y alcance

**Qué se busca.** Que se pueda conectar un proyecto a la plataforma: guardar su nombre y dónde vive su código, crear su carpeta de documentación, y dejar la acción registrada.

**Qué entra.** El registro del proyecto, las tres comprobaciones que lo rechazan o lo advierten, la carpeta de documentación, la acción en la auditoría, y **la primera pantalla**: la lista de proyectos y la de uno solo.

**Qué no entra.** Avisar cuando la ruta se pierde, que es la fase C. Traer la documentación que el proyecto ya tenga escrita, que es la fase E. Calcular el estado a partir de sus documentos, que es la fase G: acá el estado responde `sin empezar` porque todavía no hay documentos que mirar.

## 2. Análisis previo: línea base verificada

**Qué se leyó antes de escribir.** La especificación del módulo Proyectos, la historia con sus cuatro criterios, la ficha `Proyecto` del modelo de datos, las pantallas `P-01` y `P-02` del diseño de interfaz, `DA-02`, y el código de [validadores/version.py](../../../../../validadores/version.py).

**Qué ya está construido y se usa tal cual.** La fase A dejó el almacenamiento en texto con su índice; la fase D dejó la auditoría y el comprobante que el almacén exige. Conectar un proyecto pasa por los dos: se registra la acción y **con ese comprobante** se escribe. `RN-3` de la historia -la acción queda en la auditoría- se cumple sin construir nada nuevo.

**Qué ya está resuelto en el estándar, y no se reescribe.** `RN-3` de la especificación pide que la versión de reglas que declara un proyecto **exista de verdad**, porque un número inventado mayor que el real apagaría el aviso de desfase en vez de dispararlo. Eso ya está construido en [validadores/version.py](../../../../../validadores/version.py):

| Qué se necesita | Qué ya existe |
|---|---|
| Leer qué versión declara un proyecto | `extraer_adoptada(texto)`, sobre su `CLAUDE.md` |
| Saber qué versiones existen de verdad | `versiones_publicadas()`, que las lee del registro de cambios y no de `VERSION`, porque la pregunta es si el número existió alguna vez |
| Saber si el proyecto quedó atrás | `comparar(adoptada, estandar)` |

Se importa igual que el enmascarador en la fase D, por el puente de `nucleo/seguridad/`. Escribir otro lector dejaría dos formas de leer la misma línea, y una quedaría vieja (`M12`).

**La versión adoptada no se pregunta: se lee.** El molde de `CLAUDE.md` que el estándar instala trae la línea `**Versión del estándar adoptada:**`, y de ahí sale. Preguntársela al usuario al conectar sería pedirle un dato que la máquina puede leer, y abrir la puerta a que lo teclee mal, que es justo lo que `RN-3` quiere evitar.

### 2.1 Archivos que se crean o modifican

Archivos nuevos dentro de `plataforma/nucleo/proyectos/`, y las plantillas de sus dos pantallas. Se modifican `config/settings/base.py` y `config/urls.py` para dar de alta el componente y sus rutas, y `nucleo/seguridad/` para sumar el puente hacia el lector de versiones.

**Nada de esta fase escribe dentro de la carpeta del proyecto que se conecta.** Es `RN-1` de la historia, y es el caso de «que NO pase» del plan de pruebas.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Por qué |
|---|---|---|
| El proyecto se guarda como texto, con el comprobante de la auditoría | Escribir directo con el almacén | La fase D cerró ese camino a propósito, y esta es la primera fase que lo usa de verdad |
| La carpeta del proyecto se nombra con un identificador derivado del nombre, no con el nombre tal cual | Usar el nombre como está | Un nombre lleva espacios, acentos y mayúsculas; la carpeta tiene que servir igual en cualquier máquina y en cualquier sistema |
| El identificador se guarda, y el nombre también | Derivar la carpeta cada vez que se necesite | Si el usuario renombra el proyecto, la carpeta no debe moverse: es lo mismo que el histórico ya aprendió con sus archivos de sesión |
| La versión adoptada se lee del `CLAUDE.md` del proyecto | Pedírsela al usuario al conectar | La máquina puede leerla, y teclearla es la forma de que quede un número que no existe |
| Se comprueba contra las versiones publicadas, no contra `VERSION` | Comparar solo con la vigente | Un número inventado **mayor** que el real pasaría la comparación y apagaría el aviso. Es el pendiente 82, ya resuelto en el estándar |
| Un proyecto sin estándar instalado se conecta con el campo vacío y su aviso | Rechazarlo hasta que lo instale | Decidido por el usuario el 2026-08-25: la plataforma administra **todos** los proyectos, y los que no adoptaron el estándar son los que más falta le hacen |
| El estado responde `sin empezar` y no se guarda | Guardar el estado al conectar | El modelo dice que se calcula. Guardarlo crea una segunda verdad que envejece |
| La pantalla usa lo que el marco trae, sin nada que salga a la red | Traer una biblioteca de interfaz | `RNF-03` y `DA-03`. La plataforma tiene que servir sin conexión |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | Cómo se resolvió |
|---|---|---|
| 1 | ¿Qué pasa cuando el proyecto que se conecta **todavía no tiene el estándar instalado**, y por eso no declara ninguna versión? | **Se conecta igual**, con el campo vacío y su aviso. Decidido por el usuario el 2026-08-25 |

**Por qué esa y no la otra.** Rechazarlo dejaba la plataforma sirviendo solo a los proyectos que ya adoptaron el estándar, y el problema declarado era administrar **todos**. Los que todavía no lo adoptaron son justo los que más falta le hacen.

**Qué arrastró la decisión.** El modelo de datos aprobado decía que ese campo era obligatorio, así que hubo que cambiarlo. El cambio quedó anotado en la sección 15.1 del [diseño](../../../../../cvds/diseno/README.md), con quién lo aprobó, en vez de editar la línea base en silencio.

**Qué no cambia.** `RN-3` sigue igual: la versión que un proyecto **sí** declare tiene que existir. Vacío y falso no son lo mismo.

Las otras dos que parecían dudas resultaron ya resueltas, y quedaron escritas arriba como línea base en vez de como preguntas.

## 3. Desglose de tareas

| # | Tarea | Entregable |
|---|---|---|
| 1 | Resolver la duda de la sección 2.7 | ✅ Resuelta el 2026-08-25, con su porqué escrito |
| 2 | Guardar un proyecto, con su carpeta de documentación | El proyecto queda registrado y su carpeta existe |
| 3 | Rechazar la ruta que no existe, y la ya registrada | Los dos rechazos dicen qué pasó |
| 4 | Leer y comprobar la versión de reglas que declara | Una versión que no existe se rechaza; una vieja se advierte; ninguna se acepta con aviso |
| 5 | Advertir la carpeta sin control de versiones | Se registra igual, con la advertencia |
| 6 | Dejar la acción en la auditoría | Conectar deja su registro, con el proyecto y la sesión |
| 7 | Las dos pantallas: la lista y un proyecto | Se ve la lista, se entra a uno, se conecta desde ahí |

## 4. Secuencia de ejecución

1 → 2 → 3 → 4 → 5 → 6 → 7. La tarea 1 era la puerta y ya está pasada: su respuesta decidía si la tarea 4 rechaza o avisa. La 7 va al final porque una pantalla sin nada que mostrar no se puede probar.

## 5. Verificación de criterios de aceptación

| Criterio | Cómo se verifica |
|---|---|
| `CA-01` un proyecto queda registrado | Se conecta una carpeta y se comprueba que aparece y que su carpeta de documentación existe |
| `CA-02` una ruta que no existe no se registra | Se intenta con una ruta inventada |
| `CA-03` registrar dos veces la misma ruta avisa | Se intenta con una ya registrada, y se comprueba que dice cuál la tiene |
| `CA-04` registrar no toca el código | Se compara la carpeta del proyecto antes y después |
| Transversal: la acción queda en la auditoría | Se busca el registro después de conectar |
| Transversal: sin control de versiones se advierte | Se conecta una carpeta que no lo tenga |

## 6. Datos y ambiente de prueba

La propia máquina, sin red. **Los proyectos de prueba se crean y se borran por la propia prueba**: ninguna carpeta real del usuario se usa como conejillo. Ninguna credencial.

## 7. Reversión

Se descarta la rama de la fase. Lo que esta fase escribe vive en `datos/proyectos/`, y borrarlo no toca ningún proyecto administrado, porque nunca se escribió dentro de ellos.

## 8. Producción y migración

No aplica: no hay proyectos conectados todavía.

## 9. Reglas del estándar aplicadas

| Regla | Cómo se cumple acá |
|---|---|
| `02·F2` sin especificación acordada no hay código | La del módulo Proyectos está aprobada |
| `02·F4` el plan va con su plan de pruebas | Se presentan y se aprueban juntos |
| `01·C7` ante dos lecturas, preguntar | La duda de la sección 2.7 se planteó antes de escribir, y la decidió el usuario |
| `20·M12` buscar antes de crear | El lector de versiones ya existe; por eso no aparece como tarea de construcción |
| `00·N1` ningún cambio de estado sin aprobación | Conectar y desconectar piden confirmación, según la especificación §7 |

## 10. Riesgos y bloqueos

| # | Riesgo | Qué se hace |
|---|---|---|
| 1 | Que algo de esta fase escriba dentro de la carpeta del proyecto | Es `CP-006`, el caso de «que NO pase». Se compara la carpeta entera antes y después |
| 2 | Que la primera pantalla se lleve más tiempo que las seis tareas anteriores juntas | Se deja al final y se hace mínima: la de la versión 1 muestra y conecta, nada más |
| 3 | Que conectar el propio repositorio del estándar como primer proyecto tenga casos que otro proyecto no tiene | Se prueba con proyectos de mentira primero, y con el repositorio real solo al final, sin escribir en él |

## 11. Definition of Done

- ☐ La duda resuelta y escrita.
- ☐ Un proyecto queda registrado, con su carpeta de documentación.
- ☐ La ruta que no existe y la ya registrada se rechazan, diciendo qué pasó.
- ☐ Una versión de reglas que no existe se rechaza.
- ☐ Un proyecto sin estándar instalado se conecta, con su aviso.
- ☐ La carpeta sin control de versiones se registra con su advertencia.
- ☐ Conectar deja su registro en la auditoría.
- ☐ Se ve la lista de proyectos y se entra a uno.
- ☐ Comprobado que la carpeta del proyecto no cambió.

## 12. Seguimiento

El estado vive en [estado-fase.md](estado-fase.md), y se actualiza al cambiar de estación.

## 13. Cierre

La fase cierra cuando los ocho puntos de la sección 11 tengan veredicto. Lo que quede sin hacer se declara como deuda en el documento de cierre.

---

**Aprobado por Ing. José Dúmar Jiménez Ruíz, el 2026-08-25.** Se aprueba junto con [plan_pruebas.md](plan_pruebas.md), con la duda ya cerrada.
