# Funcionalidad implementada — Fase C-EP-008-HU-002-la-ruta-perdida-se-avisa (módulo Proyectos)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-008-HU-002-la-ruta-perdida-se-avisa` |
| **Módulo** | Proyectos |
| **Especificación del módulo** | [documentacion/proyectos/spec.md](../../../../proyectos/spec.md), §6 · `02·F2` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-25 |
| **HU / CA cubiertas** | [HU-002](../HU-002-avisar-la-ruta-perdida.md): `CA-01`, `CA-02`, `CA-03`. Los tres, y con esto la historia queda cerrada |
| **Fecha de cierre** | 2026-08-25 |
| **Versión del estándar al cerrar** | 34.1.0 |
| **Commit** | `ff2248e` |

---

## 1. Qué se implementó — resumen

Cuando la carpeta de un proyecto deja de estar donde estaba, la plataforma lo dice **y dice dónde la buscó**. Desde ahí se corrige la ruta, con confirmación y con registro de dónde a dónde.

Perder la ruta no pierde nada: la documentación vive en la plataforma.

Corregir la ruta comprueba lo mismo que conectar, y **relee la versión de reglas de la carpeta nueva**, porque la carpeta cambió y lo que declara puede ser otra cosa.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| "Al listar proyectos se comprueba si cada ruta existe" (§6) | modelo | `ruta_viva` en [models.py](../../../../../plataforma/nucleo/proyectos/models.py) | ✅ | CP-001, CP-006 |
| "La que no, se marca y se avisa" (§6) | servicio · vista | `avisos_de` en [core.py](../../../../../plataforma/nucleo/proyectos/core.py), y `templates/proyectos/` | ✅ | CP-001 |
| "Su documentación se sigue mostrando igual" (§6) | modelo | La documentación no depende de la ruta | ✅ | CP-002 |
| "Volver a apuntar la ruta quita el aviso" (§6) | servicio · vista | `corregir_ruta` en [core.py](../../../../../plataforma/nucleo/proyectos/core.py) | ✅ | CP-003 |
| "`RN-4` perder la ruta no borra nada" (§4) | modelo | La ficha y los documentos viven en `datos/` | ✅ | CP-002 |
| "`RN-1` registrar un proyecto no modifica nada dentro de su carpeta" (§4) | servicio | Corregir no toca ninguna de las dos carpetas | ✅ | CP-007 |
| `RNF-02` listar cincuenta proyectos en menos de un segundo | modelo | La comprobación de rutas | ✅ | CP-006: 0.010 s |
| "Corregir la ruta sola, buscando la carpeta en otro lado" | — | — | N/A | La historia lo deja fuera a propósito |

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| 1 | Que el aviso diga qué ruta se buscó | ✅ hecha | `avisos_de` en [core.py](../../../../../plataforma/nucleo/proyectos/core.py) | CP-001 |
| 2 | Corregir la ruta de un proyecto | ✅ hecha | `corregir_ruta` en [core.py](../../../../../plataforma/nucleo/proyectos/core.py) y `cambiar` en [views.py](../../../../../plataforma/nucleo/proyectos/views.py) | CP-003 |
| 3 | Comprobar la ruta nueva como al conectar | ✅ hecha | `corregir_ruta`, las tres comprobaciones | CP-004 |
| 4 | Releer la versión de reglas al corregir la ruta | ✅ hecha | `corregir_ruta` | CP-005 |
| 5 | Medir que cincuenta proyectos listan bajo un segundo | ✅ hecha | `RendimientoTests` en [tests.py](../../../../../plataforma/nucleo/proyectos/tests.py) | CP-006: **0.010 s** |

**Correspondencia con el plan:** 5 tareas en el plan, 5 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** el plan no estimó horas. La fase salió más corta de lo que su historia sugería, porque `CA-01` y `CA-02` ya estaban casi construidos desde la fase B, y eso quedó declarado en el plan §2 **antes** de empezar.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Qué | Resultado |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | Cumple |
| **Suites ejecutadas** | `python manage.py test nucleo`, 103 de 103 verdes |
| **Defectos abiertos que se aceptaron** | Ninguno |

**Verificaciones manuales** (`08·T4`):

| # | Qué se verificó | Resultado |
|---|---|---|
| 1 | Que las pruebas cacen lo que dicen cazar | Seis sabotajes. Cinco cazados; el sexto destapó una prueba floja que se reforzó |
| 2 | Que la secuencia real funcione | Se movió la carpeta de un proyecto de verdad y se corrigió la ruta. El documento sobrevivió |
| 3 | Que corregir a una ruta inventada conserve la que tenía | Rechazó y conservó |
| 4 | Que el registro sea legible sin la plataforma | Las tres acciones, con las dos rutas en la corrección |
| 5 | Que los datos de prueba no quedaran | Los dos índices en cero |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

En la lista, un proyecto con la ruta perdida sale marcado con **«Esa carpeta ya no está»** y un enlace para corregirlo. En su pantalla hay un botón **Corregir dónde vive su código**, que lleva a la confirmación.

- **Desde el código:** `core.corregir_ruta(proyecto, ruta_nueva, quien, sesion)`.
- **Los avisos:** `core.avisos_de(ruta, version)` devuelve la lista de lo que hay que decirle al usuario, y el de ruta perdida **nombra la ruta**.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El aviso nombra la ruta que se buscó | Sin ella, el usuario no puede ver si fue un renombre, un movimiento o un disco sin montar. Es `RN-2` de la historia | `avisos_de` en [core.py](../../../../../plataforma/nucleo/proyectos/core.py) |
| Cuando la ruta está perdida, ese es el **único** aviso | Sumarle «no declara versión» y «no tiene control de versiones» sería ruido: no se pueden comprobar sin la carpeta, y afirmarlos sería hablar de lo que no se leyó | `avisos_de` corta ahí |
| Corregir la ruta relee la versión de reglas | La carpeta cambió: lo que declara puede ser otra cosa | `corregir_ruta` |
| Corregir comprueba lo mismo que conectar | Si aceptara lo que conectar rechaza, sería una puerta de atrás. Mismo criterio que la fase H con la versión | `corregir_ruta`, las tres comprobaciones |
| Un proyecto puede apuntar a su propia ruta sin que se rechace | Una comprobación de duplicados escrita sin cuidado haría chocar al proyecto consigo mismo | El `exclude(pk=proyecto.pk)` de `corregir_ruta` |
| La confirmación dice que **ninguna de las dos carpetas se toca** | «Corregir la ruta» suena a «mover el proyecto», y hay que decir que no lo es | `CONFIRMACIONES` en [views.py](../../../../../plataforma/nucleo/proyectos/views.py) |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| La medición de `RNF-02` se hizo con cincuenta carpetas locales y pequeñas. Un disco de red o carpetas grandes cambian el número | Diferido por el plan | Se vuelve a medir cuando haya proyectos reales en volumen. El número de hoy queda escrito para poder comparar |
| La ruta se comprueba al listar, no de forma continua | Diferido por el plan | Es el supuesto declarado en la historia. Si algún día estorba, se revisa ahí |
| Un proyecto desconectado con ruta perdida muestra el aviso de desconectado, no el de la ruta | No previsto | Es lo correcto hoy: el aviso más importante es que está desconectado. Se anota por si algún día hace falta ver los dos |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] Mapa de dependencias: sin cambios.
- [x] Catálogo de módulos: Proyectos ya está registrado.
- [x] Índice de la carpeta de la fase: [README.md](README.md).
- [x] Especificación del módulo: ya describía este comportamiento en su §6. No hizo falta tocarla.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna. El campo de la ruta existe desde la fase B.
- **Qué cambia para quien ya tenía la plataforma:** el aviso de ruta perdida ahora nombra la ruta, y hay un botón para corregirla.
- **Reversión:** se descarta la rama de la fase. Lo que escribe son rutas dentro de fichas que ya existían; nada se borra.
