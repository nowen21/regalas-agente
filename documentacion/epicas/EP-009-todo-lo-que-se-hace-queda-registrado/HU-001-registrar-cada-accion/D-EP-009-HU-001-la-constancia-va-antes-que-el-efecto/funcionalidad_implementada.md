# Funcionalidad implementada — Fase D-EP-009-HU-001-la-constancia-va-antes-que-el-efecto (módulo Auditoría)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `D-EP-009-HU-001-la-constancia-va-antes-que-el-efecto` |
| **Módulo** | Auditoría |
| **Especificación del módulo** | [documentacion/auditoria/spec.md](../../../../auditoria/spec.md), aprobada el 2026-08-25 · `02·F2` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-25, ampliado ese mismo día |
| **HU / CA cubiertas** | [HU-001](../HU-001-registrar-cada-accion.md): `CA-01`, `CA-02`, `CA-03`, `CA-04`, `CA-05`. Los cinco |
| **Fecha de cierre** | 2026-08-25 |
| **Versión del estándar al cerrar** | 34.1.0 |
| **Commit** | `5231022` |

---

## 1. Qué se implementó — resumen

La plataforma ya no puede cambiar nada sin dejar constancia. Cada acción se registra antes de ejecutarse, con quién, cuándo, sobre qué, qué cambió, en qué proyecto y en qué sesión. Si el registro no se puede escribir, la acción no ocurre.

Lo registrado no se edita ni se borra, y el intento de hacerlo también queda escrito. Ninguna clave entra: el texto pasa por el enmascarador que el estándar ya tenía.

El registro es una tabla de texto que se lee con cualquier editor, y su índice se puede borrar y rehacer.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| "Se agrega al final del registro y se indexa" (§6) | servicio | [nucleo/auditoria/core.py](../../../../../plataforma/nucleo/auditoria/core.py) | ✅ | CP-001 |
| "Si el registro no se puede escribir, la acción no se da por hecha" (§6) | servicio | `con_constancia` en [core.py](../../../../../plataforma/nucleo/auditoria/core.py) | ✅ | CP-003, con el orden espiado |
| "Texto que solo se agrega. No hay operación de editar ni de borrar" (§5) | modelo · servicio | [nucleo/auditoria/models.py](../../../../../plataforma/nucleo/auditoria/models.py) | ✅ | CP-002 |
| "Acción sin proyecto asociado: se registra igual, con el campo vacío" (§6) | servicio | `registrar` en [core.py](../../../../../plataforma/nucleo/auditoria/core.py) | ✅ | CP-001 paso 3 |
| "Campo `sesión`, para enlazar el registro con lo que esa sesión dejó escrito" (§5) | modelo | [models.py](../../../../../plataforma/nucleo/auditoria/models.py) | ✅ | CP-006, probado contra el renombre |
| "Texto que trae algo parecido a una credencial: se tapa antes de escribir" (§6) | servicio | [nucleo/seguridad/claves.py](../../../../../plataforma/nucleo/seguridad/claves.py) | ✅ | CP-004 y CP-005 |
| "`RN-2` si el registro no se puede escribir, la acción no se ejecuta" (§4) | servicio | `con_constancia`, y `almacen.guardar` que exige el comprobante | ✅ | CP-003 y CP-007 |
| "`RN-4` se registra la acción, no la conversación" (§4) | servicio | El registro guarda siete campos y el identificador de sesión, nunca el texto de la conversación | ✅ | Se ve en el archivo del registro, EV-03 |
| "Índice por proyecto y por fecha" (§5) | modelo | [models.py](../../../../../plataforma/nucleo/auditoria/models.py) | parcial | Hay orden por fecha y campo de proyecto; el índice afinado se necesita cuando llegue `F-019` en la versión 4 |
| "En la versión 1 no tiene pantalla: solo registra" (§7) | vista | — | N/A | A propósito. La pantalla `P-09` es de la versión 4 |
| "Consultar lo registrado con filtros" (`F-019`, §1) | — | — | N/A | Versión 4 |

**Faltantes / diferimientos:** el afinado del índice y la pantalla, los dos declarados por la propia especificación para la versión 4.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| 1 | Resolver las dos dudas de la sección 2.7 | ✅ hecha | [plan_trabajo.md](plan_trabajo.md) §2.7 | Las dos, resueltas leyendo el código, no decidiendo |
| 2 | Escribir el registro que solo se agrega | ✅ hecha | [auditoria/core.py](../../../../../plataforma/nucleo/auditoria/core.py) | CP-001, EV-03 |
| 3 | Cerrar la edición y el borrado, y registrar el intento | ✅ hecha | [auditoria/models.py](../../../../../plataforma/nucleo/auditoria/models.py) y `editar`/`borrar` en `core.py` | CP-002 |
| 4 | Detener la acción cuando el registro no se puede escribir | ✅ hecha | `con_constancia` en [core.py](../../../../../plataforma/nucleo/auditoria/core.py) | CP-003 |
| 5 | Tapar las credenciales antes de escribir | ✅ hecha | [nucleo/seguridad/claves.py](../../../../../plataforma/nucleo/seguridad/claves.py) | CP-004, CP-005 |
| 6 | Enlazar la acción con la sesión que la produjo | ✅ hecha | El campo `sesion` de [models.py](../../../../../plataforma/nucleo/auditoria/models.py) | CP-006 |
| 7 | Cerrar el camino que escribía sin constancia | ✅ hecha | [nucleo/constancia.py](../../../../../plataforma/nucleo/constancia.py) y `guardar` en [almacen/core.py](../../../../../plataforma/nucleo/almacen/core.py) | CP-007 ciclo 2, EV-04 |

**Correspondencia con el plan:** 6 tareas en el plan original, 7 acá. La 7 se agregó el 2026-08-25 con autorización del usuario, después de que `CP-007` encontrara el hueco.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`):

| Archivo | Por qué hubo que tocarlo | Quién autorizó ampliar el plan |
|---|---|---|
| `plataforma/nucleo/almacen/core.py` y `tests.py` | `CP-007` encontró que se podía escribir sin dejar registro. Con ese camino abierto, `CA-01` no se cumplía | El usuario, el 2026-08-25, sobre dos opciones escritas con su costo |
| `plataforma/nucleo/constancia.py` (nuevo) | El comprobante lo emite la auditoría y lo exige el almacén; ponerlo en cualquiera de los dos los habría dejado dependiendo uno del otro | La misma autorización |

**La fase se detuvo antes de tocarlos.** Es lo que `02·F8` pide, y es la razón por la que este cuadro dice quién autorizó en vez de estar vacío.

**Esfuerzo real contra estimado:** el plan no estimó horas. El riesgo 3 avisaba que seis tareas podían pasarse de una jornada y mandaba partir la fase; con la séptima encima siguió cabiendo.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Qué | Resultado |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | Cumple, en el ciclo 2 |
| **Suites ejecutadas** | `python manage.py test nucleo`, 37 de 37 verdes |
| **Defectos abiertos que se aceptaron** | Ninguno. `DEF-01` se corrigió y se verificó |

**Verificaciones manuales** (`08·T4`), lo que el entorno automático no reproduce:

| # | Qué se verificó | Resultado |
|---|---|---|
| 1 | Que las pruebas cacen lo que dicen cazar | Cuatro sabotajes, cuatro veces fallaron las pruebas correctas |
| 2 | Que el registro se lea sin la plataforma | `cat` mostró la tabla completa |
| 3 | Que el índice del registro se rehaga desde el texto | 3 acciones recuperadas |
| 4 | Que el enmascarador del estándar se importe de verdad | Tapó las dos formas de clave, dejó el molde |
| 5 | Que los datos de mentira no quedaran | Los dos índices en cero |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

**La forma correcta de cambiar algo** es `con_constancia`, que registra y solo entonces ejecuta:

```python
from nucleo.auditoria import core

core.con_constancia(
    lambda comprobante: almacen.guardar("uno.md", "# Uno\n", comprobante),
    que_se_hizo="guardar un documento",
    sobre_que="uno.md",
    quien="el agente",
    sesion="5f06ce4e-64bf-41e5-b58e-87959b32bf62")
```

- **Comando propio:** `python manage.py reconstruir_auditoria` rehace el índice del registro leyendo `datos/auditoria/`.
- **Dónde queda el registro:** `datos/auditoria/AAAA-MM.md`, un archivo por mes.
- **Permisos o datos base sembrados:** ninguno.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El comprobante vive en su propio módulo, no en la auditoría ni en el almacén | Los dos lo necesitan y ninguno debe depender del otro: la auditoría lo emite, el almacén lo exige. Ponerlo en cualquiera de los dos habría creado un ciclo | [nucleo/constancia.py](../../../../../plataforma/nucleo/constancia.py) |
| El comprobante solo vale para el archivo sobre el que se registró | Rechazar cuando no hay constancia cubre el olvido total. El descuido probable es reutilizar el que uno tiene a mano para escribir otra cosa, y eso solo se cierra atando el comprobante a su archivo | CP-007 paso 5 |
| Se promete que escribir sin constancia sea **deliberado y visible**, no imposible | En este lenguaje el objeto se puede construir a mano. Prometer una barrera dura sería mentir, y quien leyera el código después confiaría de más | Escrito en el propio [constancia.py](../../../../../plataforma/nucleo/constancia.py) |
| El enmascarador se importa del estándar; si no está, no se escribe nada | Devolver el texto sin tapar sería el daño exacto que esto viene a evitar. Es preferible detenerse (`00·N6`) | [nucleo/seguridad/claves.py](../../../../../plataforma/nucleo/seguridad/claves.py) |
| `editar` y `borrar` existen, y solo sirven para rechazar y dejar constancia | `CA-02` pide dos cosas: que no se pueda, y que el intento quede. Sin las funciones, el intento no tendría dónde registrarse | `editar`/`borrar` en [auditoria/core.py](../../../../../plataforma/nucleo/auditoria/core.py) |
| `Registro.objects.todos()` es el único camino que puede borrar filas | El índice se reconstruye, así que alguien tiene que poder vaciarlo. Se dejó un solo camino, con nombre distinto y su porqué escrito, en vez de dejar el borrado abierto | [auditoria/models.py](../../../../../plataforma/nucleo/auditoria/models.py) |
| `CP-003` se prueba poniendo un archivo donde va la carpeta | En Windows quitarle la escritura a una carpeta no impide crear archivos dentro. Lo que se prueba es el comportamiento ante la falla, no la forma de provocarla | [auditoria/tests.py](../../../../../plataforma/nucleo/auditoria/tests.py) |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| El índice del registro ordena por fecha y guarda el proyecto, pero no está afinado para consultar un año de historial | Diferido por el plan | Versión 4, con `F-019`, que es la que consulta |
| Nadie exige todavía llenar el campo de sesión: una acción puede registrarse sin él por descuido, no solo por no venir de una sesión | No previsto | Fase B, donde nacen las acciones que sí vienen de una sesión |
| La plataforma depende de la ruta de `validadores/` para tapar claves | Atajo decidido, por el usuario el 2026-08-25 | El día que la plataforma y el estándar vivan en repositorios distintos, esto es lo primero que hay que mover |
| Registrar antes de ejecutar podría hacer lento el trabajo. Hoy no hay volumen que lo muestre | Diferido por el plan | Se mide en el uso, según la épica |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] Mapa de dependencias: el módulo Auditoría depende del almacén, y el almacén ahora exige el comprobante que la auditoría emite. El acoplamiento se rompió con [constancia.py](../../../../../plataforma/nucleo/constancia.py).
- [x] Catálogo de módulos: Auditoría ya está registrado con su especificación aprobada.
- [x] Índice de la carpeta de la fase: [README.md](README.md).
- [x] Especificación del módulo: no hizo falta cambiarla. La sección 5 decía «un campo para enlazar el registro con lo que esa sesión dejó escrito» sin decir con qué; la fase lo precisó sin contradecirla.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

No hay producción: la plataforma corre en la máquina del usuario.

- **Migraciones a correr:** `python manage.py migrate`.
- **Datos base:** ninguno.
- **Qué cambia para quien ya tenía la plataforma:** `almacen.guardar` ahora pide un tercer argumento. Es un cambio que rompe a quien lo llamara, y por eso se hizo ahora: no había ningún llamador fuera de las pruebas.
- **Reversión:** se descarta la rama de la fase. Nada de lo hecho toca proyectos, reglas ni documentación existente.
