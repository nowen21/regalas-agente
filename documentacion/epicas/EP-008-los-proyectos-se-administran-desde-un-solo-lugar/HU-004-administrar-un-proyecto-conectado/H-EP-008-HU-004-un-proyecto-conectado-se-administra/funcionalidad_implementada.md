# Funcionalidad implementada — Fase H-EP-008-HU-004-un-proyecto-conectado-se-administra (módulo Proyectos)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `H-EP-008-HU-004-un-proyecto-conectado-se-administra` |
| **Módulo** | Proyectos |
| **Especificación del módulo** | [documentacion/proyectos/spec.md](../../../../proyectos/spec.md) · `02·F2` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-25 |
| **HU / CA cubiertas** | [HU-004](../HU-004-administrar-un-proyecto-conectado.md): `CA-01` a `CA-05`. Los cinco, y con esto la historia queda cerrada |
| **Fecha de cierre** | 2026-08-25 |
| **Versión del estándar al cerrar** | 34.1.0 |
| **Commit** | `5bf4ebb` |

---

## 1. Qué se implementó — resumen

**Equivocarse al conectar un proyecto dejó de ser permanente.** Se puede desconectar, renombrar y corregir la versión de reglas que declara, y ninguna de las tres borra ni mueve nada: desconectar deja la documentación donde está, y renombrar deja la carpeta donde está.

Las cuatro operaciones piden confirmación, y la confirmación dice **qué va a pasar y qué no**.

Un proyecto desconectado libera su ruta, y volver a conectar esa carpeta **lo reactiva** con lo que tenía, avisando antes por si el usuario quería empezar de cero.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| "Desconectar: sale de la lista y su documentación se queda en la plataforma" (§6) | servicio | `desconectar` en [nucleo/proyectos/core.py](../../../../../plataforma/nucleo/proyectos/core.py) | ✅ | CP-001 |
| "Renombrar: cambia el nombre y su carpeta no se mueve" (§6) | servicio | `renombrar` en [core.py](../../../../../plataforma/nucleo/proyectos/core.py) | ✅ | CP-003 |
| "Corregir la versión declarada: se vuelve a leer del proyecto y se comprueba" (§6) | servicio | `corregir_version` en [core.py](../../../../../plataforma/nucleo/proyectos/core.py) | ✅ | CP-004 |
| "Los tres piden confirmación y los tres quedan en la auditoría" (§6) | vista · servicio | `cambiar` en [views.py](../../../../../plataforma/nucleo/proyectos/views.py) y `templates/proyectos/confirmar.html` | ✅ | CP-005 |
| "Conectar y desconectar piden confirmación" (§7) | vista | `conectar` y `cambiar` en [views.py](../../../../../plataforma/nucleo/proyectos/views.py) | parcial | Conectar solo pregunta cuando va a **reactivar** un desconectado, que es cuando hay algo que advertir. Conectar una carpeta nueva sigue sin preguntar: no hay nada que se pueda perder |
| "Desconectar no borra la documentación" (§12) | servicio | `desconectar` no toca la carpeta: solo reescribe la ficha | ✅ | CP-001 paso 4 |
| "`RN-1` registrar un proyecto no modifica nada dentro de su carpeta" (§4) | servicio | Ninguna de las tres escribe fuera de `datos/` | ✅ | CP-008 |
| "El texto es la fuente; el índice se rehace" (§5) | modelo | La fecha de desconexión va en la ficha | ✅ | CP-002 |
| "Configurar qué rige en cada proyecto" (`F-004`) | — | — | N/A | Versión 5 |

**Faltantes / diferimientos:** la confirmación al conectar una carpeta nueva. Está declarada arriba como parcial, con su porqué, y queda como deuda.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| 1 | Resolver la duda de la sección 2.7 | ✅ hecha | [plan_trabajo.md](plan_trabajo.md) §2.7 | Resuelta con el usuario el 2026-08-25 |
| 2 | Desconectar, dejando la documentación | ✅ hecha | `desconectar` en [core.py](../../../../../plataforma/nucleo/proyectos/core.py) | CP-001 |
| 3 | Renombrar, sin mover la carpeta | ✅ hecha | `renombrar` en [core.py](../../../../../plataforma/nucleo/proyectos/core.py) | CP-003 |
| 4 | Corregir la versión declarada | ✅ hecha | `corregir_version` en [core.py](../../../../../plataforma/nucleo/proyectos/core.py) | CP-004 |
| 5 | La confirmación de los cuatro, y su registro | ✅ hecha | `CONFIRMACIONES` y `cambiar` en [views.py](../../../../../plataforma/nucleo/proyectos/views.py) | CP-005, EV-04 |
| 6 | La sección de desconectados en la pantalla | ✅ hecha | `templates/proyectos/lista.html` | CP-006 |
| 7 | Reconectar: reactivar en vez de crear uno nuevo | ✅ hecha | `reconectar` y `desconectado_en` en [core.py](../../../../../plataforma/nucleo/proyectos/core.py) | CP-007 |

**Correspondencia con el plan:** 6 tareas en el plan original, 7 acá. La 7 la agregó la respuesta a la duda, y quedó anotada en el plan antes de escribirla.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno. Todo cayó dentro de `plataforma/nucleo/proyectos/`, sus plantillas y `config/urls.py`, que el plan §2.1 declaraba.

**Esfuerzo real contra estimado:** el plan no estimó horas.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Qué | Resultado |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | Cumple |
| **Suites ejecutadas** | `python manage.py test nucleo`, 86 de 86 verdes |
| **Defectos abiertos que se aceptaron** | Ninguno |

**Verificaciones manuales** (`08·T4`), lo que el entorno automático no reproduce:

| # | Qué se verificó | Resultado |
|---|---|---|
| 1 | Que las pruebas cacen lo que dicen cazar | Seis sabotajes. Cinco cazados a la primera; el sexto pasó y resultó ser un sabotaje que no saboteaba |
| 2 | Que la secuencia completa sirva | Se conectó el repositorio con el nombre mal escrito, se le guardó un documento, se renombró, se desconectó y se reconectó. El documento sobrevivió a las cuatro |
| 3 | Que la confirmación diga qué NO va a pasar | Las tres cosas que no pasan, incluida la documentación |
| 4 | Que la ficha y el registro se lean sin la plataforma | Los dos legibles; el registro trae las cinco acciones |
| 5 | Que los dos índices se rehagan desde el texto | 1 proyecto y 5 acciones recuperados |
| 6 | Que los datos de prueba no quedaran | Los dos índices en cero |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

En la pantalla de un proyecto, `/proyecto/<identificador>/`, hay tres botones: **Renombrar**, **Corregir la versión de reglas** y **Desconectar**. Los tres llevan a una pantalla de confirmación antes de hacer nada.

Los desconectados se ven en su propia sección de la lista, y se vuelve a conectar uno escribiendo su misma ruta en el formulario de conectar.

- **Desde el código:** `core.desconectar(proyecto)`, `core.renombrar(proyecto, nombre)`, `core.corregir_version(proyecto)`. Y `core.desconectado_en(ruta)` para saber, antes de conectar, si esa carpeta tiene una historia guardada.
- **Comando propio:** `python manage.py reconstruir_proyectos` rehace el índice, respetando quién está desconectado.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La fecha de desconexión va en la ficha, no solo en el índice | Si viviera solo en la base, rehacer el índice resucitaría al proyecto. `CP-002` lo comprueba borrando el índice entero | [core.py](../../../../../plataforma/nucleo/proyectos/core.py), `_texto_de_la_ficha` |
| Una ficha sin ese campo se lee como un proyecto conectado | Es lo que hizo que no hubiera que migrar las fichas de la fase B | `reconstruir_indice` en [core.py](../../../../../plataforma/nucleo/proyectos/core.py) |
| Reconectar avisa antes, aunque reactivar sea lo correcto casi siempre | Reactivar es lo que el usuario quiere cuando está corrigiendo un error. **No** es lo que quiere si pensaba empezar de cero con esa carpeta, y entonces recibiría la historia vieja sin pedirla | `desconectado_en` y `templates/proyectos/confirmar.html` |
| La confirmación vive en una pantalla propia, no en una ventana del navegador | Tiene que decir **qué NO va a pasar**, y eso no cabe en una ventana del navegador. Es la mitad que permite confirmar en vez de adivinar | `CONFIRMACIONES` en [views.py](../../../../../plataforma/nucleo/proyectos/views.py) |
| Conectar una carpeta nueva **no** pregunta; reconectar sí | Preguntar por todo entrena a confirmar sin leer. Se pregunta donde hay algo que se pueda perder o recibir sin querer | `conectar` en [views.py](../../../../../plataforma/nucleo/proyectos/views.py) |
| La ruta de un desconectado queda libre | Si siguiera tomada, desconectar no serviría para corregir el error que motivó la fase | La consulta de `conectar` filtra por `desconectado=""` |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| **El orden de dos registros de auditoría del mismo segundo es indeterminado.** La marca de tiempo tiene precisión de segundos, así que `Registro.objects.last()` no dice cuál fue la última acción | No previsto | Se descubrió escribiendo `CP-001`. Hoy no hace daño: nada de la plataforma depende del orden dentro del mismo segundo. Se paga cuando llegue `F-019`, la consulta de la auditoría, que sí va a ordenar |
| Conectar una carpeta nueva no pide confirmación, aunque la especificación §7 dice que conectar la pide | Atajo decidido | Se decidió preguntar solo donde hay algo que perder. Si el usuario quiere la pregunta siempre, es un cambio de una línea y una prueba |
| Un proyecto desconectado no se puede borrar de la lista de desconectados | Diferido por el plan | Fuera de alcance a propósito: borrar no es reversible, y la especificación lo descartó |
| El estado sigue respondiendo `sin empezar` | Diferido por el plan | Fase G |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] Mapa de dependencias: sin cambios. Proyectos sigue usando el almacén y la auditoría.
- [x] Catálogo de módulos: Proyectos ya está registrado.
- [x] Índice de la carpeta de la fase: [README.md](README.md).
- [x] Especificación del módulo: ya describía este comportamiento desde la fase B, cuando se corrigió su §1. No hizo falta tocarla.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** `python manage.py migrate`. Agrega un campo, que queda vacío en los proyectos existentes.
- **Qué cambia para quien ya tenía la plataforma:** nada se rompe. Las fichas escritas antes no traen la fecha de desconexión y se leen como proyectos conectados, que es lo correcto.
- **Datos base:** ninguno.
- **Reversión:** se descarta la rama de la fase. Lo que esta fase escribe son fechas y nombres dentro de fichas que ya existían; nada se borra.
