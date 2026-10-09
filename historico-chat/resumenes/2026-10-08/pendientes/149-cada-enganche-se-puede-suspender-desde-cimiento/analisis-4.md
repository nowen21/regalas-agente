# Análisis 4: la revisión de git suspendida dice la hora de vencimiento en UTC

> **Aprobado** por el usuario el 2026-10-09, en el turno 51, con la versión 56.8.0. Desde ese momento este análisis no se reescribe.

> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Un análisis aprobado no se reescribe. Si al ejecutar el plan aparece un hallazgo que obliga a tocar algo que el plan no declara, se abre `analisis-5.md`, que trata solo lo que falló y sus implicaciones sobre lo ya hecho.

---

## Recomendaciones

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-6 | Se leyeron el análisis 1 (acuerdo 3) y el plan de la fase B: `suspendidos.py` es de esa fase |
| R-15 | El defecto salió en la prueba en el proyecto (`02·F29`); se detuvo ahí y se anotó en `prueba-en-el-proyecto.md` |
| Las demás | No aplican: no se cambia ninguna regla (R-3, R-4) y no hay piloto (R-16) |

---

## Hallazgo

### H-7 · La revisión de git suspendida dice la hora de vencimiento en UTC

| Campo | Valor |
|---|---|
| Qué pasó | En la prueba en scilit (2026-10-09), `validar.py marcas` suspendida dijo «hasta el 2026-10-09 19:29»; en Colombia eran las 14:29. `suspendidos.py` lee el vencimiento con `UNIX_TIMESTAMP`, que toma la hora UTC guardada como si fuera de Colombia y le suma cinco horas |
| Por qué importa | Quien lee el aviso cree que la suspensión dura cinco horas más de lo que dura; la prueba en el proyecto quedó en «falla» y scilit no recibe el aviso de resuelto |
| Pendiente | El mismo pendiente 149: se trata en su análisis 4 |

## Pendiente

**De dónde sale:** proyecto scilit, hallazgo 1 del resumen del 2026-10-08; H-3 y H-4 de la sesión del 2026-10-09.

**El problema.** De los enganches, solo el freno se podía suspender desde Cimiento; en git la única salida era `--no-verify`.

**Por qué importa.** Un enganche que estorba no se podía apagar sin que el checklist marcara la instalación como incompleta.

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 49 · Usuario, 2026-10-09 13:32:34
> Analicemos: el pendiente 149

**Agente**, 2026-10-09 13:33:50
<!-- agente: dff71fb6-4e73-4b49-9760-a35a2b38efd8 -->

Anoto el defecto como H-7 en el resumen, porque el análisis tiene que nombrar su hallazgo, y escribo el análisis 4.

El análisis 4 quedó escrito en [analisis-4.md](../../../../../historico-chat/resumenes/2026-10-08/pendientes/149-cada-enganche-se-puede-suspender-desde-cimiento/analisis-4.md). **¿Se corrige reabriendo la fase B de la EP-025·HU-032?** Recomiendo que sí.

La corrección:

1. **Reabrir la fase B.** `suspendidos.py` es de esa fase, y su plan ya lo incluye.
2. **Cambiar una línea:** el vencimiento se lee de una forma que no suma las cinco horas.
3. **Agregar una prueba que consulte la base de verdad.** Las pruebas de hoy simulan la consulta, y por eso no podían ver este error.
4. **Volver a cerrar la fase y repetir la prueba en scilit,** para que esta vez quede en «pasa».

Revisé el resto de Cimiento: es la única consulta que lee las fechas de esta forma.

### 50 · Usuario, 2026-10-09 13:58:11
> Respondo que bueno que llegó esa pregunta porque estaba por proponerlo la idea no es estar creando fases, pruebas, hu, etc ... sino primero validar de donde salió es hallazgo y corregir allá por que al final lo que interesa es contruir la documentación con lo que quedó bien. No interesa mostrar las HU que quedaron mal sino las que dieron solución a la aplicación final que se entrega

**Agente**, 2026-10-09 13:58:47
<!-- agente: 60225bf5-8ce4-48b3-b40c-eaef724f3034 -->

Anoto en el análisis lo que acaba de decidir: un hallazgo se corrige donde nació, sin crear fases ni HU nuevas.

Quedó anotado en el análisis 4. Se reabre la fase B, que es donde nació `suspendidos.py`; ahí se corrige la línea y se ajusta su prueba para que consulte la base. Después se vuelve a cerrar la fase y se repite la prueba en scilit. No se crean fases ni HU nuevas.

**Escriba «Apruebo el análisis»** y lo hago.

Ese criterio, corregir el hallazgo donde nació para que la documentación muestre lo que quedó funcionando, sirve para todos los proyectos. Si quiere que se guarde como recuerdo, escriba «Recuerde» y lo dejo propuesto en Cimiento.

### 51 · Usuario, 2026-10-09 13:59:45
> Apruebo el análisis

**Agente**, 2026-10-09 14:06:37
<!-- agente: 5b0e1913-9541-47ba-9f1b-d6780151773f -->

Aprobado. Registro la lección y reabro la fase B.

La fase B quedó reabierta. Corrijo la consulta.

Al terminar, la prueba intentó borrar el proyecto que creó, y el registro de versiones de Cimiento lo protege. La paso a la clase de pruebas de Django, que deshace sola lo que se crea.

Fase B cerrada otra vez y HU-032 terminada. Repito la prueba en scilit con la corrección.

Ahora sí dice 15:05, la hora de Colombia. Levanto las suspensiones, compruebo que todo vuelve a correr y anoto el resultado.

La prueba en scilit quedó en «pasa». La hora de vencimiento ahora sale bien: la suspensión de prueba decía «hasta las 15:05», que era la hora de Colombia.

El error se corrigió donde nació, sin crear fases ni HU nuevas:

- Se reabrió la fase B y se cambió la línea que leía la hora.
- Su prueba ahora consulta la base de datos. Además, la dañé a propósito con el comando `danar_a_proposito`, y la prueba detectó el daño.
- La fase B volvió a cerrarse, y la HU-032 sigue terminada.
- Las suspensiones de prueba en scilit quedaron levantadas.

Con la prueba en «pasa», el próximo commit le deja a scilit el aviso de que su pendiente 037 quedó resuelto. **¿Hago el commit y lo subo?** Llevaría el análisis 4, el pendiente 149 en su versión 5, la corrección y la prueba de la fase B, `prueba-en-el-proyecto.md` y la lista de daños de `historico-chat/scripts/2026-10-09/`.

> acá termina la conversación

---

## Lo acordado

1. Dónde se corrige: un hallazgo se corrige en el sitio de donde salió, sin crear fases, pruebas ni HU nuevas; la documentación muestra lo que quedó funcionando, no lo que salió mal. Aquí, se reabre la fase B de la EP-025·HU-032, donde nació `suspendidos.py` (turno 50).
2. La corrección: la consulta lee el vencimiento con `TIMESTAMPDIFF(SECOND, '1970-01-01', s.vence)` en vez de `UNIX_TIMESTAMP(s.vence)`; la prueba de la fase B que corresponde pasa a consultar la base de pruebas; se vuelve a cerrar la fase y se repite la prueba en scilit (turno 50).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `02·F29` (la corrección se comprueba en el proyecto que reportó antes de avisar), `02·F30` (`reabrir_fase` es la contraria de `cerrar_fase`) y `08·T1`. No choca ninguna.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| La consulta | `_CONSULTA` de `core/enganches/suspendidos.py` trae `UNIX_TIMESTAMP(s.vence)` |
| Lo que hace MySQL | Su zona es la del sistema, `America/Bogota`. `UNIX_TIMESTAMP('2026-10-09 19:29:10')` da 1791592150, que es 19:29 en Colombia; `TIMESTAMPDIFF(SECOND, '1970-01-01', …)` da 1791574150, que es 14:29, la hora correcta |
| Dónde se nota | En el aviso de la revisión de git suspendida, y en la comparación con la hora actual dentro de la lista ya leída. La base ya descarta lo vencido con `UTC_TIMESTAMP()`, así que nada queda suspendido de más entre un mensaje y otro |
| Las pruebas | Simulan la consulta y no pasan por MySQL: no podían verlo |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| `S-363` | La misma causa: MySQL de WAMP no tiene las zonas cargadas y convierte con la del sistema |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | Ninguno: es la consulta de Cimiento |
| Normas y leyes | Ninguna |
| Herramientas | MySQL convierte con la zona de su sesión; `TIMESTAMPDIFF` desde 1970 no convierte |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Otra consulta con `UNIX_TIMESTAMP` | `core/` | La misma diferencia de cinco horas | No hay otra: se buscó en `proyectos/cimiento/core` |
| Una prueba que no pase por MySQL | `tests_suspendidos.py` | El error vuelve sin que nadie lo vea | Punto 3: la prueba de la fase B consulta la base de pruebas |

---

## Propuesta final: hallazgo y pendiente V5, épica y HU

### Hallazgo V5. Igual que H-7

### Pendiente V5. Igual al pendiente 149, con H-7 sumado a «De dónde sale»

### Épica y HU que salen del análisis

La misma EP-025·HU-032, en su fase B reabierta (acuerdo 1): ni HU ni fase nuevas.

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Una consulta que convierte fechas se prueba contra la base real, no con la consulta simulada | Falló | S-373 | No aplica |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Pasar el pendiente a su versión siguiente, con H-7 en «De dónde sale» | `13·DOC26` | Este análisis, de una y sin fase: `historico-chat/resumenes/2026-10-08/pendientes/149-cada-enganche-se-puede-suspender-desde-cimiento/pendiente.md`, hecho el 2026-10-09 |
| 2 | Reabrir la fase B de la EP-025·HU-032 con `reabrir_fase`, con H-7 como motivo | 1 | EP-025·HU-032 |
| 3 | En `core/enganches/suspendidos.py`, leer el vencimiento con `TIMESTAMPDIFF(SECOND, '1970-01-01', s.vence)`; en `core/enganches/tests_suspendidos.py`, que la prueba lea una suspensión de la base de pruebas y compruebe su hora; volver a cerrar la fase B | 2 | EP-025·HU-032 |
| 4 | Repetir la prueba en scilit y anotar `prueba-en-el-proyecto.md` | 2 | EP-025·HU-032 |

## Lo que aporta al análisis principal

**Resultado:** aclara.

**Lo que suma al análisis principal:** Lo que se suspende dice hasta cuándo en la hora de Colombia.
