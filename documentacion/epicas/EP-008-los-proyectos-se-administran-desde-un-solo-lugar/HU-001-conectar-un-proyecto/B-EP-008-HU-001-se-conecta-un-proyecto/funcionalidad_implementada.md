# Funcionalidad implementada — Fase B-EP-008-HU-001-se-conecta-un-proyecto (módulo Proyectos)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-008-HU-001-se-conecta-un-proyecto` |
| **Módulo** | Proyectos |
| **Especificación del módulo** | [documentacion/proyectos/spec.md](../../../../proyectos/spec.md), aprobada el 2026-08-25 · `02·F2` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-25 |
| **HU / CA cubiertas** | [HU-001](../HU-001-conectar-un-proyecto.md): `CA-01`, `CA-02`, `CA-03`, `CA-04`. Los cuatro, y con esto la historia queda cerrada |
| **Fecha de cierre** | 2026-08-25 |
| **Versión del estándar al cerrar** | 34.1.0 |
| **Commit** | Se completa al commitear |

---

## 1. Qué se implementó — resumen

Ya se pueden conectar proyectos a la plataforma, y **ya hay pantalla**. Se guarda cómo se llama cada uno y dónde vive su código; se rechaza lo que no debe entrar diciendo por qué; y todo queda registrado en la auditoría.

Conectar no toca nada dentro de la carpeta del proyecto: es una anotación de la plataforma, no una intervención.

El primer proyecto conectado de verdad es el propio repositorio del estándar, que es la prueba que la especificación pedía.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| "Se recibe nombre y ruta. Se comprueba que la ruta exista y que no esté ya registrada" (§6) | servicio | [nucleo/proyectos/core.py](../../../../../plataforma/nucleo/proyectos/core.py) | ✅ | CP-002, CP-003 |
| "Se crea la carpeta del proyecto en la plataforma y se guarda el registro" (§6) | servicio | `conectar` en [core.py](../../../../../plataforma/nucleo/proyectos/core.py) | ✅ | CP-001 paso 5 |
| "Se anota la acción en la auditoría" (§6) | servicio | `con_constancia` en `conectar` | ✅ | CP-006 |
| "Ruta que no existe: se responde con la ruta que se buscó" (§6) | servicio | `RutaQueNoExiste` | ✅ | CP-002 paso 2 |
| "Ruta ya registrada: se responde con qué proyecto la tiene" (§6) | servicio | `RutaYaRegistrada` | ✅ | CP-003 paso 3 |
| "Carpeta sin control de versiones: se registra, y se advierte" (§6) | servicio | `avisos_de` | ✅ | CP-005 |
| "`RN-1` registrar un proyecto no modifica nada dentro de su carpeta" (§4) | servicio | Nada de `conectar` escribe fuera de `datos/` | ✅ | CP-009, retrato archivo por archivo |
| "`RN-2` dos proyectos no pueden apuntar a la misma ruta" (§4) | modelo · servicio | `ruta_normalizada` en [models.py](../../../../../plataforma/nucleo/proyectos/models.py) y en `core.py` | ✅ | CP-003 paso 5 |
| "`RN-3` la versión de reglas que declara un proyecto debe existir" (§4) | servicio | [nucleo/seguridad/reglas.py](../../../../../plataforma/nucleo/seguridad/reglas.py) | ✅ | CP-004 |
| "`RN-4` perder la ruta no borra nada" (§4) | modelo | La ficha vive en la plataforma, no en el proyecto | ✅ | CP-009 paso 6 |
| "La ruta viva y el estado se calculan, no se guardan" (§4.2 y §5) | modelo | `ruta_viva` y `estado` de [models.py](../../../../../plataforma/nucleo/proyectos/models.py) | ✅ | Son propiedades, no campos |
| "El texto en la carpeta del proyecto dentro del repositorio de la plataforma; el índice en la base local, reconstruible" (§5) | modelo | `reconstruir_indice` en [core.py](../../../../../plataforma/nucleo/proyectos/core.py) | ✅ | CP-001 paso 7 |
| "Pantallas `P-01` Inicio y `P-02` Un proyecto" (§7) | vista | [views.py](../../../../../plataforma/nucleo/proyectos/views.py) y `templates/proyectos/` | parcial | CP-007. Muestran y conectan; entrar a un documento, abrir una fase y pedir el expediente llegan después |
| "El estado se calcula al pedirlo" (§12) | modelo | `estado` responde `sin empezar` | parcial | Calcularlo de verdad es la fase G, y así lo declaraba el plan |
| "Conectar y desconectar piden confirmación" (§7) | vista | — | ❌ | **Desconectar no existía como funcionalidad.** Se pidió por la cadena: `F-035`, [HU-004](../../HU-004-administrar-un-proyecto-conectado/HU-004-administrar-un-proyecto-conectado.md), fase H |
| "Avisar la ruta perdida" (`F-002`, §6) | — | — | N/A | Fase C |
| "Traer su documentación" (§1) | — | — | N/A | Módulo Importación, fase E |

**Faltantes / diferimientos:** la confirmación al conectar y todo lo de desconectar van en la fase H, que nació de esta misma fase. Lo demás lo reparte la especificación por fases.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| 1 | Resolver la duda de la sección 2.7 | ✅ hecha | [plan_trabajo.md](plan_trabajo.md) §2.7 | Resuelta con el usuario el 2026-08-25 |
| 2 | Guardar un proyecto, con su carpeta de documentación | ✅ hecha | [proyectos/core.py](../../../../../plataforma/nucleo/proyectos/core.py) | CP-001 |
| 3 | Rechazar la ruta que no existe, y la ya registrada | ✅ hecha | `RutaQueNoExiste` y `RutaYaRegistrada` | CP-002, CP-003 |
| 4 | Leer y comprobar la versión de reglas que declara | ✅ hecha | [seguridad/reglas.py](../../../../../plataforma/nucleo/seguridad/reglas.py) | CP-004, CP-008 |
| 5 | Advertir la carpeta sin control de versiones | ✅ hecha | `avisos_de` en `core.py` | CP-005 |
| 6 | Dejar la acción en la auditoría | ✅ hecha | `conectar`, por `con_constancia` | CP-006 |
| 7 | Las dos pantallas: la lista y un proyecto | ✅ hecha | [views.py](../../../../../plataforma/nucleo/proyectos/views.py), `templates/base.html` y `templates/proyectos/` | CP-007, EV-04 |

**Correspondencia con el plan:** 7 tareas en el plan, 7 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`):

| Archivo | Por qué hubo que tocarlo | Quién autorizó ampliar el plan |
|---|---|---|
| `plataforma/nucleo/almacen/tests.py` | La ruta `/` pasó a ser la lista de proyectos, y la comprobación de «la plataforma está viva» apuntaba ahí. Se movió a `/esta-viva/` y su prueba se actualizó | Nadie, y por eso queda escrito acá. El plan sí declaraba modificar `config/urls.py`, y mover la ruta raíz obliga a actualizar la prueba que la usaba: es la misma edición vista desde el otro lado. **No se agregó comportamiento nuevo, solo la ruta cambiada** |

**Esfuerzo real contra estimado:** el plan no estimó horas. El riesgo 2 avisaba que la pantalla podía llevarse más tiempo que las seis tareas anteriores juntas; no pasó, porque se dejó al final y se hizo mínima.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Qué | Resultado |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | Cumple |
| **Suites ejecutadas** | `python manage.py test nucleo`, 62 de 62 verdes |
| **Defectos abiertos que se aceptaron** | Ninguno |

**Verificaciones manuales** (`08·T4`), lo que el entorno automático no reproduce:

| # | Qué se verificó | Resultado |
|---|---|---|
| 1 | Que las pruebas cacen lo que dicen cazar | Cinco sabotajes, cinco veces fallaron las pruebas correctas |
| 2 | Que la plataforma sirva las dos pantallas de verdad | Respondieron en el puerto 8742, con el proyecto real |
| 3 | Que conectar el repositorio real no lo toque | 13518 archivos antes y después |
| 4 | Que la ficha y el registro se lean sin la plataforma | Los dos legibles con `cat` |
| 5 | Que los dos índices se rehagan desde el texto | 1 proyecto y 1 acción recuperados |
| 6 | Que los datos de prueba no quedaran | Los dos índices en cero |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

- **La pantalla:** `python manage.py runserver` desde `plataforma/`, y `http://127.0.0.1:8000/`. Ahí se ve la lista y se conecta desde el formulario.
- **Un proyecto:** `/proyecto/<identificador>/`.
- **Saber si la plataforma responde:** `/esta-viva/`, que se movió ahí al ocupar la raíz la lista de proyectos.
- **Comando propio:** `python manage.py reconstruir_proyectos` rehace el índice leyendo las fichas.
- **Desde el código:** `nucleo.proyectos.core.conectar(nombre, ruta, quien, sesion)`, que devuelve el proyecto y la lista de avisos.
- **Permisos o datos base sembrados:** ninguno.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La ficha del proyecto vive **dentro** de su carpeta de documentación | Así crear la ficha crea la carpeta, y la carpeta queda con algo dentro. Una carpeta vacía no entra al control de versiones, y el respaldo es el repositorio | `_ficha` en [core.py](../../../../../plataforma/nucleo/proyectos/core.py) |
| El identificador se deriva del nombre y **se guarda** | Derivarlo cada vez movería la carpeta al renombrar el proyecto. Es lo mismo que el histórico ya aprendió con sus archivos de sesión | `identificador_de` en [core.py](../../../../../plataforma/nucleo/proyectos/core.py) |
| Dos proyectos con el mismo nombre reciben identificadores distintos | Un identificador derivado del nombre choca en cuanto hay dos que se llaman igual, y eso pasa el primer mes | `_identificador_libre` |
| Las rutas se comparan normalizadas | La misma carpeta escrita en mayúsculas o con barra final es la misma carpeta, y en Windows pasa todo el tiempo | `ruta_normalizada`, y el campo aparte en [models.py](../../../../../plataforma/nucleo/proyectos/models.py) |
| La versión declarada se comprueba contra el **registro de cambios**, no contra la vigente | Un número mayor que el real pasaría la comparación con la vigente y apagaría el aviso de desfase. Es el pendiente 82, ya resuelto en el estándar | [seguridad/reglas.py](../../../../../plataforma/nucleo/seguridad/reglas.py) |
| No declarar versión se acepta; declarar una falsa se rechaza | Los dos casos entran por el mismo camino y es fácil juntarlos. Si se juntan, o entran versiones inventadas o se rechazan proyectos sin estándar | `existe()` en `reglas.py`, y `CP-008` que prueba los dos juntos |
| La pantalla no trae ninguna biblioteca de interfaz | `RNF-03` y `DA-03`: la plataforma tiene que servir sin conexión. Los estilos van en el molde, en unas pocas líneas | `templates/base.html` |
| La comprobación de origen del formulario se puso desde ahora | Hoy la plataforma no se expone a la red, pero el formulario cambia estado. El día que corra en un servidor, ya está puesta | `MIDDLEWARE` en [config/settings/base.py](../../../../../plataforma/config/settings/base.py) |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| **Conectar no tiene reversa.** No se puede desconectar, renombrar ni corregir la versión declarada | No previsto | Fase H, por [pendientes/86](../../../../../pendientes/86-conectar-un-proyecto-no-tiene-reversa.md) y la [HU-004](../../HU-004-administrar-un-proyecto-conectado/HU-004-administrar-un-proyecto-conectado.md), ya escritas |
| Conectar todavía no pide confirmación, aunque la especificación lo exige en su §7 | No previsto | Fase H, junto con lo anterior |
| El estado siempre responde `sin empezar` | Diferido por el plan | Fase G, que es la que lo calcula |
| La plataforma no se entera si el proyecto cambia la versión que declara en su `CLAUDE.md` después de conectado | No previsto | Fase H, `CA-03` de la HU-004 |
| La pantalla es la mínima: no entra a documentos, no abre fases, no pide el expediente | Diferido por el plan | Versiones 2 y 5, según el diseño de interfaz |

**Los dos «no previsto» salieron de lo mismo:** la especificación tenía decidido cómo se comporta desconectar y ninguna funcionalidad lo pedía. Se destapó al ver la pantalla funcionando, no leyendo el documento.

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] Mapa de dependencias: Proyectos usa el almacén y la auditoría. Es el primero que las usa a las dos de verdad.
- [x] Catálogo de módulos: Proyectos ya está registrado con su especificación aprobada.
- [x] Índice de la carpeta de la fase: [README.md](README.md).
- [x] Especificación del módulo actualizada: su §1 no nombraba desconectar aunque §7 y §12 sí lo trataban. Corregida, con su sección de cambios y quién la aprobó.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

No hay producción: la plataforma corre en la máquina del usuario.

- **Migraciones a correr:** `python manage.py migrate`.
- **Datos base:** ninguno.
- **Qué cambia para quien ya tenía la plataforma:** la raíz `/` dejó de ser la página de «está viva» y pasó a ser la lista de proyectos. Esa página sigue existiendo, en `/esta-viva/`.
- **Reversión:** se descarta la rama de la fase. Lo que esta fase escribe vive en `datos/proyectos/`, y borrarlo no toca ningún proyecto administrado, porque nunca se escribió dentro de ellos.
