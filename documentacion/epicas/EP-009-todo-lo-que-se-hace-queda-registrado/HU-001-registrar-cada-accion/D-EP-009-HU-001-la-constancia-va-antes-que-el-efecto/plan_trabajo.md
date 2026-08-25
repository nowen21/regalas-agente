# Plan de Trabajo — Fase D-EP-009-HU-001-la-constancia-va-antes-que-el-efecto (módulo Auditoría)   ·   `[CAPA 3]`

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `D-EP-009-HU-001-la-constancia-va-antes-que-el-efecto` |
| **Épica** | [EP-009 Todo lo que se hace queda registrado](../../epica.md) |
| **HU** | [HU-001 Registrar cada acción](../HU-001-registrar-cada-accion.md) — una sola |
| **Módulo** | Auditoría |
| **Especificación** | [documentacion/auditoria/spec.md](../../../../auditoria/spec.md), aprobada el 2026-08-25 |
| **Versión del producto** | 1, fase D de siete |
| **Fecha apertura** | 2026-08-25 |
| **Rama** | Una rama propia de la fase, que se integra al cerrarla |

---

## 1. Objetivo y alcance

**Qué se busca.** Que ninguna acción cambie algo sin dejar constancia, y que la constancia quede **antes** del cambio, no después.

**Qué entra.** El registro que solo se agrega, con quién, cuándo, sobre qué y qué cambió; el enlace a la sesión que produjo la acción; el tapado de credenciales antes de escribir; y la detención de la acción cuando el registro no se puede escribir.

**Qué no entra.** Pantalla para consultar lo registrado, que es de la versión 4. Guardar la conversación de la sesión, que la especificación deja fuera a propósito.

## 2. Análisis previo — línea base verificada

**Qué se leyó antes de escribir.** La especificación del módulo Auditoría, la historia y sus cinco criterios, la decisión `DA-08`, y el código de [validadores/enmascarar.py](../../../../../validadores/enmascarar.py) y [validadores/secretos.py](../../../../../validadores/secretos.py).

**Qué existe hoy que se parece, y es más de lo que parecía.** El estándar ya tiene resuelto el tapado de credenciales: `enmascarar.py` reconoce la clave entre comillas y la pegada sin ellas, no tapa los moldes (`tu-clave`, `changeme`) ni la línea que lee del entorno, y se apoya en las ocho formas de secreto que `secretos.py` ya conoce. Escribir un enmascarador nuevo para la plataforma dejaría **dos listas que se separan**, que es justo lo que el propio archivo advierte que no se haga (`M12`).

**Por qué esta fase va antes que B y que C.** Lo dice el orden aprobado en [cvds/implementacion/README.md](../../../../../cvds/implementacion/README.md) §5: registrar desde el primer día evita tener un tramo sin historia. Si se conectaran proyectos primero, esas conexiones quedarían sin registro y el `CA` transversal de `EP-008 HU-001` no se podría cumplir sin volver atrás.

**La dependencia cruzada, y cómo se rompe.** La historia declara que depende de `EP-008 HU-001` "para saber en qué proyecto ocurrió la acción", y esa historia se completa en la fase B. No es un bloqueo: la especificación §6 dice que una acción sin proyecto asociado **se registra igual, con el campo de proyecto vacío**. Esta fase construye el registro contra `A`; la fase B llega después y lo usa.

### 2.1 Archivos que se crean o modifican

Archivos nuevos dentro de `plataforma/nucleo/auditoria/`. Se modifica `config/settings/base.py` para dar de alta el componente nuevo. **Nada de esta fase toca `interfaz/`, ni la carpeta de un proyecto, ni el cuerpo de reglas.** Si la duda 1 se resuelve por reutilizar, se lee `validadores/enmascarar.py` sin modificarlo.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Por qué |
|---|---|---|
| El registro se escribe con lo que la fase A ya construyó | Un almacenamiento propio de la auditoría | `DA-01`. El registro es texto como todo lo demás, y su índice se rehace igual |
| Solo se agrega: no hay operación de editar ni de borrar | Dejarlas y confiar en que nadie las use | `DA-08`. Un registro editable no demuestra nada, y lo que no existe no se usa por error |
| Primero se escribe la constancia, después se ejecuta | Ejecutar y registrar después | Especificación §6. Si falla en medio, queda un cambio del que nadie sabe |
| El tapado de credenciales se reutiliza, no se reescribe | Un enmascarador propio de la plataforma | `M12`, y el aviso del propio archivo: dos listas de secretos se separan y una queda vieja |
| Una acción sin proyecto se registra con el campo vacío | Rechazarla hasta que exista el módulo Proyectos | Especificación §6, y es lo que permite construir esta fase antes que la B |

### 2.7 Dudas por resolver antes de escribir

| # | Duda | Por qué detiene |
|---|---|---|
| 1 | ¿Cómo llega el enmascarador del estándar a la plataforma: se importa desde `validadores/`, o se mueve a un sitio que las dos usen? | Copiarlo está descartado. Importarlo amarra la plataforma a la ruta del estándar; moverlo toca `validadores/`, que hoy funciona, y eso es cambio del estándar con su versión y su registro |
| 2 | ¿Qué identifica una sesión, para poder enlazarla? | `CA-04` pide el enlace a lo que la sesión dejó escrito. Hoy el histórico las nombra por fecha y tema. Si el registro guarda algo distinto, el enlace no resuelve |

**Ninguna de las dos se decide sin el usuario.** La 1 puede terminar tocando el estándar, que es una acción que pide su propia aprobación; la 2 fija un dato que después no se cambia sin reescribir lo registrado.

## 3. Desglose de tareas

| # | Tarea | Entregable |
|---|---|---|
| 1 | Resolver las dos dudas de la sección 2.7 | Las dos, con su porqué escrito |
| 2 | Escribir el registro que solo se agrega | Una acción queda escrita, con sus seis datos |
| 3 | Cerrar la edición y el borrado, y registrar el intento | Intentar editar no cambia nada, y queda constancia del intento |
| 4 | Detener la acción cuando el registro no se puede escribir | Con el registro bloqueado, nada cambia |
| 5 | Tapar las credenciales antes de escribir | Una clave con comillas y otra sin ellas quedan tapadas; el molde no |
| 6 | Enlazar la acción con la sesión que la produjo | El registro trae el enlace, y vacío cuando no vino de una sesión |

## 4. Secuencia de ejecución

1 → 2 → 3 → 4 → 5 → 6. La tarea 1 es una puerta: la duda 1 decide de dónde sale el código de la tarea 5, y la duda 2 decide el dato de la tarea 6.

## 5. Verificación de criterios de aceptación

| Criterio | Cómo se verifica |
|---|---|
| `CA-01` toda acción que cambia algo queda registrada | Se ejecuta una acción y se busca su registro |
| `CA-02` lo registrado no se puede editar ni borrar | Se intenta, y se comprueba que el archivo no cambió |
| `CA-03` sin constancia no hay efecto | Se bloquea el registro y se pide una acción |
| `CA-04` la acción de una sesión queda enlazada | Se registra dentro de una sesión y se sigue el enlace |
| `CA-05` ninguna credencial entra al registro | Se registra un texto con clave, con comillas y sin ellas |

## 6. Datos y ambiente de prueba

La propia máquina, sin red. Datos de mentira creados y borrados por la prueba. **Ninguna credencial real**, ni siquiera para probar el tapado: se usan claves inventadas (`00·N6`).

## 7. Reversión

Se descarta la rama de la fase. Si la duda 1 se resuelve moviendo el enmascarador, eso se hace como cambio del estándar aparte, con su versión, y se revierte por su cuenta.

## 8. Producción y migración

No aplica: no hay registros previos.

## 9. Reglas del estándar aplicadas

| Regla | Cómo se cumple acá |
|---|---|
| `02·F2` sin especificación acordada no hay código | La del módulo Auditoría está aprobada |
| `02·F4` el plan va con su plan de pruebas | Se presentan y se aprueban juntos |
| `01·C7` ante dos lecturas, preguntar | Las dos dudas de la sección 2.7 detienen la fase |
| `20·M12` buscar antes de crear | El enmascarador ya existe; por eso la duda 1 pregunta cómo llega, no si se escribe |
| `00·N6` una credencial no se escribe | Se prueba con claves inventadas, y el tapado es tarea propia |

## 10. Riesgos y bloqueos

| # | Riesgo | Qué se hace |
|---|---|---|
| 1 | Que amarrar la plataforma a `validadores/` la vuelva dependiente del estándar en el código, y no solo en las reglas | Es la duda 1. Se decide antes de escribir, no después |
| 2 | Que registrar antes de ejecutar haga lento el trabajo | Se mide en el uso. Hoy no hay volumen que lo muestre |
| 3 | Que la fase crezca más allá de una jornada, por ser seis tareas | Si pasa, se parte: registrar e integridad por un lado, credenciales y sesión por otro |

## 11. Definition of Done

- ☐ Las dos dudas resueltas y escritas.
- ☐ Una acción queda registrada con sus seis datos.
- ☐ Editar y borrar un registro no se puede, y el intento queda.
- ☐ Con el registro bloqueado, ninguna acción surte efecto.
- ☐ Una clave con comillas y otra sin ellas quedan tapadas.
- ☐ El registro trae el enlace a la sesión, y vacío cuando no la hay.

## 12. Seguimiento

El estado vive en [estado-fase.md](estado-fase.md), y se actualiza al cambiar de estación.

## 13. Cierre

La fase cierra cuando los seis puntos de la sección 11 tengan veredicto. Lo que quede sin hacer se declara como deuda en el documento de cierre.

---

**Pendiente de aprobación.** Se presenta junto con [plan_pruebas.md](plan_pruebas.md).
