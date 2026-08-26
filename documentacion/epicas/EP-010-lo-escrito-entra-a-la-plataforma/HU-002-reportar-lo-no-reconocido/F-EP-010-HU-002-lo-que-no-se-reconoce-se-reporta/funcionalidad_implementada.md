# Funcionalidad implementada — Fase F-EP-010-HU-002-lo-que-no-se-reconoce-se-reporta (módulo Importación)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `F-EP-010-HU-002-lo-que-no-se-reconoce-se-reporta` |
| **Módulo** | Importación |
| **Especificación del módulo** | [documentacion/importacion/spec.md](../../../../importacion/spec.md), aprobada el 2026-08-25 · `02·F2` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-25 |
| **HU / CA cubiertas** | [HU-002](../HU-002-reportar-lo-no-reconocido.md): `CA-01`, `CA-02`, `CA-03` y su transversal. Los cuatro |
| **Fecha de cierre** | 2026-08-25 |
| **Versión del estándar al cerrar** | 34.1.0 |
| **Commit** | Se completa al commitear |

---

## 1. Qué se implementó — resumen

Cada traída deja **un reporte escrito** de lo que no entró, con su fecha. Se puede volver a mirar sin traer otra vez, y dos reportes de fechas distintas se comparan para ver qué se corrigió.

**El registro de auditoría lo enlaza en vez de repetir la lista.** Antes decía «994 reconocidos, 1 sin reconocer»: cuántos, no cuáles.

El reporte se escribe **siempre**, también cuando no quedó nada afuera, y también cuando no entró nada. Dice además **qué carpetas no se miraron y por qué**.

**Con esta fase termina la versión 1 del producto.**

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| "Al terminar, se lista qué quedó afuera y dónde está cada archivo" (§6) | servicio | `_texto_del_reporte` en [nucleo/importacion/core.py](../../../../../plataforma/nucleo/importacion/core.py) | ✅ | CP-001 |
| "Si todo se reconoció, se dice, en vez de mostrar una lista vacía" (§6) | servicio | El mismo, con su rama para cuando no quedó nada | ✅ | CP-003 |
| "`RN-2` lo que no se reconoce no se transforma" (§4) | servicio | No entra y no se toca | ✅ | CP-008 |
| "`RN-4` nada se pierde en silencio" (§4) | servicio | Lo no reconocido **y** las carpetas que no se miraron | ✅ | CP-001, CP-004 |
| "`RN-1` traer no modifica el proyecto de origen" (§4) | servicio | El reporte se escribe en `datos/`, nunca en el proyecto | ✅ | CP-008 |
| "Traer queda registrado, con cuántos documentos entraron y cuántos no" (§14) | servicio | El registro, que además **enlaza** el reporte | ✅ | CP-005 |
| Transversal: el reporte queda guardado con la acción de traer | servicio · vista | `_donde_va_el_reporte`, `reportes_de` y sus dos pantallas | ✅ | CP-002, CP-007 |
| "Pantalla `P-11`" (§7) | vista | `templates/importacion/` | parcial | Muestra y deja mirar los reportes; la forma final es de la versión 2 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| 1 | Escribir el reporte como documento, con su fecha | ✅ hecha | `_donde_va_el_reporte` en [core.py](../../../../../plataforma/nucleo/importacion/core.py) | CP-001 |
| 2 | Que diga lo no reconocido, con su ruta, y cuántos son | ✅ hecha | `_texto_del_reporte` | CP-001 |
| 3 | Que diga qué carpetas no se miraron, y por qué | ✅ hecha | El mismo | CP-004 |
| 4 | Que se escriba también cuando no quedó nada afuera | ✅ hecha | El mismo, y el arreglo de `DEF-01` | CP-003, CP-008 |
| 5 | Enlazarlo desde el registro de auditoría | ✅ hecha | `traer` | CP-005 |
| 6 | Verlos desde la pantalla del proyecto | ✅ hecha | [views.py](../../../../../plataforma/nucleo/importacion/views.py) y sus dos plantillas | CP-007 |

**Correspondencia con el plan:** 6 tareas en el plan, 6 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** el plan no estimó horas. Tres de los cuatro criterios ya venían construidos de la fase E, y eso quedó declarado en el plan §2 antes de empezar.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Qué | Resultado |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | Cumple, en el ciclo 2 |
| **Suites ejecutadas** | `python manage.py test nucleo`, 165 de 165 verdes |
| **Defectos abiertos que se aceptaron** | Ninguno. `DEF-01` corregido y verificado |

**Verificaciones manuales** (`08·T4`):

| # | Qué se verificó | Resultado |
|---|---|---|
| 1 | Que las pruebas cacen lo que dicen cazar | Ocho sabotajes, los ocho cazados |
| 2 | Que el reporte real diga la verdad | 1000 entraron, 1 no, 8 carpetas sin mirar |
| 3 | Que el registro enlace y no copie | Trae la ruta, no la lista |
| 4 | Que el reporte se lea sin la plataforma | Se lee completo con `cat` |
| 5 | Que los datos de prueba no quedaran | Los tres índices en cero |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

En la pantalla de un proyecto hay un enlace **Ver qué no entró en cada traída**. Lleva a la lista de reportes, del más nuevo al más viejo, y desde ahí se abre cualquiera.

- **Desde el código:** `core.reportes_de(proyecto)` da los pares `(cuándo, ruta)`; `core.leer_reporte(ruta)` da su texto.
- **Dónde viven:** `datos/proyectos/<identificador>/reportes/`, uno por traída, con la fecha y la hora en el nombre.
- **Desde el registro de auditoría:** la acción de traer trae la ruta del reporte en su campo de qué cambió.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El reporte es un documento, no una fila del registro | Un proyecto que siga el estándar a medias puede dejar cientos de rutas, y el registro quedaría ilegible justo cuando más falta hace. Y la auditoría guarda la acción, no el contenido | El comentario junto al registro, en `traer` |
| El registro **enlaza** el reporte, y no repite la lista | Dos copias de lo mismo se separan con el tiempo | `CP-005`, que comprueba las dos mitades: que no copie y que sí lleve |
| El reporte se escribe **siempre** | Su ausencia no distinguiría entre «salió limpio» y «no se corrió» | `_texto_del_reporte`, con su rama para cuando no quedó nada |
| **Traer sin que entre nada también es una traída** | Es `DEF-01`: antes se salía sin escribir reporte ni registro, y ese es el caso donde más falta hacen | El comentario en `traer`, con su porqué |
| Uno por traída, con la fecha y la hora en el nombre | Poder comparar dos es la mitad del valor: muestra qué se corrigió | `_donde_va_el_reporte` |
| Mirar un reporte **no** deja registro | Mirar no cambia nada. Un registro por cada vez que alguien mira algo volvería el registro inútil | `CP-002` paso 4 |
| El reporte distingue el singular | Decía «Estos 1 archivos». Un reporte que se lee mal se lee menos | `_texto_del_reporte` |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| Los reportes se acumulan, uno por traída, sin límite | Diferido por el plan | Hoy no estorba. Si algún día son cientos, se decide qué hacer con los viejos |
| `cvds/cumplimiento.md` sigue sin molde en el estándar | No previsto, viene de la fase G | Es correcto que se reporte. Si ese documento se vuelve común, el estándar tendrá que darle molde |
| La pantalla muestra el reporte tal cual, sin resaltar nada | Diferido por el plan | La forma final de `P-11` es de la versión 2 |
| Dos reportes se comparan a ojo: la plataforma no los enfrenta | No previsto | Hoy con dos alcanza. Con veinte haría falta que la plataforma diga qué cambió entre uno y otro |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] Mapa de dependencias: sin cambios. Importación sigue dependiendo de Proyectos y de Auditoría.
- [x] Catálogo de módulos: los dos ya están registrados.
- [x] Índice de la carpeta de la fase: [README.md](README.md).
- [x] Especificación del módulo: ya describía este comportamiento en su §6. No hizo falta tocarla.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna. Los reportes son archivos, no filas.
- **Qué cambia para quien ya tenía la plataforma:** aparece el enlace a los reportes en cada proyecto. **Las traídas anteriores no tienen reporte, y no se inventa uno hacia atrás**: sería afirmar sobre algo que no se observó. Basta con volver a traer.
- **Reversión:** se descarta la rama de la fase. Los reportes viven en `datos/`, y borrarlos no toca ningún proyecto.
