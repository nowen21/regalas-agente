# Plan de Trabajo — Fase D-EP-009-HU-001-la-constancia-va-antes-que-el-efecto (módulo Auditoría)   ·   `[CAPA 3]`

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `D-EP-009-HU-001-la-constancia-va-antes-que-el-efecto` |
| **Épica** | [EP-009 Todo lo que se hace queda registrado](../../epica.md) |
| **HU** | [HU-001 Registrar cada acción](../HU-001-registrar-cada-accion.md), una sola |
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

## 2. Análisis previo: línea base verificada

**Qué se leyó antes de escribir.** La especificación del módulo Auditoría, la historia y sus cinco criterios, la decisión `DA-08`, y el código de [validadores/enmascarar.py](../../../../../validadores/enmascarar.py) y [validadores/secretos.py](../../../../../validadores/secretos.py).

**Qué existe hoy que se parece, y es más de lo que parecía.** El estándar ya tiene resuelto el tapado de credenciales: `enmascarar.py` reconoce la clave entre comillas y la pegada sin ellas, no tapa los moldes (`tu-clave`, `changeme`) ni la línea que lee del entorno, y se apoya en las ocho formas de secreto que `secretos.py` ya conoce. Escribir un enmascarador nuevo para la plataforma dejaría **dos listas que se separan**, que es justo lo que el propio archivo advierte que no se haga (`M12`).

**Por qué esta fase va antes que B y que C.** Lo dice el orden aprobado en [cvds/implementacion/README.md](../../../../../cvds/implementacion/README.md) §5: registrar desde el primer día evita tener un tramo sin historia. Si se conectaran proyectos primero, esas conexiones quedarían sin registro y el `CA` transversal de `EP-008 HU-001` no se podría cumplir sin volver atrás.

**La dependencia cruzada, y cómo se rompe.** La historia declara que depende de `EP-008 HU-001` "para saber en qué proyecto ocurrió la acción", y esa historia se completa en la fase B. No es un bloqueo: la especificación §6 dice que una acción sin proyecto asociado **se registra igual, con el campo de proyecto vacío**. Esta fase construye el registro contra `A`; la fase B llega después y lo usa.

### 2.1 Archivos que se crean o modifican

Archivos nuevos dentro de `plataforma/nucleo/auditoria/`. Se modifica `config/settings/base.py` para dar de alta el componente nuevo. **Nada de esta fase toca `interfaz/`, ni la carpeta de un proyecto, ni el cuerpo de reglas.** `validadores/enmascarar.py` se lee, nunca se modifica.

**Ampliación del 2026-08-25, autorizada por el usuario.** Se suma `plataforma/nucleo/almacen/` y un módulo nuevo, `plataforma/nucleo/constancia.py`.

**Por qué hubo que ampliar.** Con el plan original construido, `CP-007` encontró un hueco: `almacen.guardar` se podía llamar directo y el archivo cambiaba sin dejar registro. Con eso abierto no se cumplía `CA-01`, que pide que toda acción que cambia algo quede registrada, y la fase habría cerrado en **No cumple**.

**Por qué se cierra ahora y no en la fase B.** Hoy no hay un solo llamador de `almacen.guardar` fuera de las pruebas. Cerrar la puerta con un llamador cuesta poco; con la fase B encima ya son varios, y el que se olvide no se nota. El usuario lo autorizó el 2026-08-25 sobre esas dos opciones, escritas con su costo.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Por qué |
|---|---|---|
| El registro se escribe con lo que la fase A ya construyó | Un almacenamiento propio de la auditoría | `DA-01`. El registro es texto como todo lo demás, y su índice se rehace igual |
| Solo se agrega: no hay operación de editar ni de borrar | Dejarlas y confiar en que nadie las use | `DA-08`. Un registro editable no demuestra nada, y lo que no existe no se usa por error |
| Primero se escribe la constancia, después se ejecuta | Ejecutar y registrar después | Especificación §6. Si falla en medio, queda un cambio del que nadie sabe |
| El tapado de credenciales se importa de `validadores/`, no se copia ni se mueve | Un enmascarador propio, o mover el del estándar | `M12`, y el aviso del propio archivo: dos listas de secretos se separan y una queda vieja. Mover obligaba a tocar el estándar sin comprar nada |
| El registro guarda el identificador de sesión que el histórico ya escribe | Guardar el nombre del archivo | El archivo se renombra cuando se le pone el tema, y el nombre dejaría el enlace roto. Es la razón por la que esa marca existe |
| Una acción sin proyecto se registra con el campo vacío | Rechazarla hasta que exista el módulo Proyectos | Especificación §6, y es lo que permite construir esta fase antes que la B |

### 2.7 Dudas por resolver antes de escribir

Las dos se cerraron el 2026-08-25, **mirando el código y no decidiendo**. Ninguna terminó necesitando una decisión del usuario, y por eso ninguna detiene ya la fase.

| # | Duda | Cómo se resolvió |
|---|---|---|
| 1 | ¿Cómo llega el enmascarador del estándar a la plataforma? | **Se importa desde `validadores/`.** Se probó antes de decidir: la plataforma lo importa, tapa `password: "…"` y `API_KEY=…`, y deja intacto `clave: tu-clave`. Cuesta agregar la ruta; cero cambios en `validadores/` |
| 2 | ¿Qué identifica una sesión, para poder enlazarla? | **El identificador que el histórico ya escribe.** No había que elegir nada |

**Qué se encontró en la duda 1.** La prueba corrió contra el módulo real, no contra una suposición:

```
password: "inventada123" y API_KEY=inventada456   ->  las dos tapadas
clave: tu-clave                                   ->  intacto, 0 tapadas
```

Mover el archivo a un sitio compartido no compra nada que esto no dé ya, y sí obligaba a tocar el estándar con su versión y su registro. Se descarta por costo, no por preferencia.

**Qué se encontró en la duda 2, y por qué la propuesta inicial era peor.** El agente había propuesto guardar el nombre del archivo del histórico. Leer [validadores/historico.py](../../../../../validadores/historico.py) mostró que eso ya se había resuelto y descartado: la primera línea de cada archivo lleva `<!-- sesion: <id> -->`, y el comentario del módulo dice por qué: **se busca esa marca, no el nombre, así el archivo se puede renombrar sin que la sesión pierda el hilo**. Renombrar es lo normal acá: el archivo nace `AAAA-MM-DD-sesion.md` y recibe su tema después. Guardar el nombre habría roto el enlace en cada renombre.

**Qué guarda entonces el campo `sesión`:** ese identificador. La especificación aprobada dice «un campo para enlazar el registro con lo que esa sesión dejó escrito» sin decir con qué; esto lo precisa, no la contradice, así que no hay cambio que anotar en su línea base.

## 3. Desglose de tareas

| # | Tarea | Entregable |
|---|---|---|
| 1 | Resolver las dos dudas de la sección 2.7 | ✅ Resueltas el 2026-08-25, con su porqué escrito y su prueba |
| 2 | Escribir el registro que solo se agrega | Una acción queda escrita, con sus seis datos |
| 3 | Cerrar la edición y el borrado, y registrar el intento | Intentar editar no cambia nada, y queda constancia del intento |
| 4 | Detener la acción cuando el registro no se puede escribir | Con el registro bloqueado, nada cambia |
| 5 | Tapar las credenciales antes de escribir | Una clave con comillas y otra sin ellas quedan tapadas; el molde no |
| 6 | Enlazar la acción con la sesión que la produjo | El registro trae el enlace, y vacío cuando no vino de una sesión |
| 7 | Cerrar el camino que escribía sin constancia | `almacen.guardar` rechaza si no se le entrega la constancia de la acción |

## 4. Secuencia de ejecución

1 → 2 → 3 → 4 → 5 → 6 → 7. La 7 se agregó el 2026-08-25, después de que `CP-007` encontrara el hueco. La tarea 1 era la puerta, y ya está pasada: la duda 1 decidía de dónde sale el código de la tarea 5, y la duda 2 el dato de la tarea 6.

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
| `01·C7` ante dos lecturas, preguntar | Las dos dudas se plantearon antes de escribir. Se cerraron leyendo el código, no suponiendo |
| `20·M12` buscar antes de crear | El enmascarador ya existe; por eso la duda 1 pregunta cómo llega, no si se escribe |
| `00·N6` una credencial no se escribe | Se prueba con claves inventadas, y el tapado es tarea propia |

## 10. Riesgos y bloqueos

| # | Riesgo | Qué se hace |
|---|---|---|
| 1 | Que amarrar la plataforma a `validadores/` la vuelva dependiente del estándar en el código, y no solo en las reglas | Se aceptó a sabiendas: hoy la plataforma vive en el mismo repositorio que el estándar. El día que se separen, esto es lo primero que hay que mover, y queda dicho acá |
| 2 | Que registrar antes de ejecutar haga lento el trabajo | Se mide en el uso. Hoy no hay volumen que lo muestre |
| 3 | Que la fase crezca más allá de una jornada, por ser seis tareas | Si pasa, se parte: registrar e integridad por un lado, credenciales y sesión por otro |

## 11. Definition of Done

- ☐ Las dos dudas resueltas y escritas.
- ☐ Una acción queda registrada con sus seis datos.
- ☐ Editar y borrar un registro no se puede, y el intento queda.
- ☐ Con el registro bloqueado, ninguna acción surte efecto.
- ☐ Una clave con comillas y otra sin ellas quedan tapadas.
- ☐ El registro trae el enlace a la sesión, y vacío cuando no la hay.
- ☐ No queda camino que escriba sin dejar constancia.

## 12. Seguimiento

El estado vive en [estado-fase.md](estado-fase.md), y se actualiza al cambiar de estación.

## 13. Cierre

La fase cierra cuando los seis puntos de la sección 11 tengan veredicto. Lo que quede sin hacer se declara como deuda en el documento de cierre.

---

**Aprobado por Ing. José Dúmar Jiménez Ruíz, el 2026-08-25.** Se aprueba junto con [plan_pruebas.md](plan_pruebas.md), con las dos dudas ya cerradas.
