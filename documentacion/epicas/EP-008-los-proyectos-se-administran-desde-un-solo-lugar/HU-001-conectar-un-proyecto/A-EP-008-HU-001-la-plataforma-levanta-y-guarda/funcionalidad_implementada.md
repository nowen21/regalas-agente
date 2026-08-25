# Funcionalidad implementada — Fase A-EP-008-HU-001-la-plataforma-levanta-y-guarda (módulo Proyectos)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-008-HU-001-la-plataforma-levanta-y-guarda` |
| **Módulo** | Proyectos |
| **Especificación del módulo** | [documentacion/proyectos/spec.md](../../../../proyectos/spec.md), aprobada el 2026-08-25 · `02·F2` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-25 |
| **HU / CA cubiertas** | Ninguno. Esta fase construye la base sobre la que la fase B cumple los criterios de [HU-001](../HU-001-conectar-un-proyecto.md), y así se declaró en el plan §5 antes de aprobarlo |
| **Fecha de cierre** | 2026-08-25 |
| **Versión del estándar al cerrar** | 34.1.0 |
| **Commit** | Se completa al commitear |

---

## 1. Qué se implementó — resumen

La plataforma ya existe y corre en la máquina: levanta sin salir a la red, guarda en archivos de texto y los vuelve a leer después de apagarla. Tiene un índice local que se puede borrar entero y rehacer desde el texto, sin perder nada.

Todavía no conecta ningún proyecto ni muestra pantallas: lo único que responde es una página que dice que está viva. Lo que quedó es el piso.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| "El texto en la carpeta del proyecto dentro del repositorio de la plataforma" (§5) | servicio | [plataforma/nucleo/almacen/core.py](../../../../../plataforma/nucleo/almacen/core.py) | ✅ | CP-004: `cat` leyó el archivo sin la plataforma |
| "El índice en la base local, reconstruible" (§5) | modelo | [plataforma/nucleo/almacen/models.py](../../../../../plataforma/nucleo/almacen/models.py), [core.py](../../../../../plataforma/nucleo/almacen/core.py) | ✅ | CP-003: se borró `indice.sqlite3` entero y volvió con la misma huella |
| "Registrar un proyecto no toca su código" (§4.1) | servicio | `_ruta_real` en [core.py](../../../../../plataforma/nucleo/almacen/core.py) | parcial | CP-006 prueba que no se escribe fuera de `datos/`. Registrar todavía no existe: es la fase B |
| "Módulo nuevo, no hay código previo" (§2) | esquema | [plataforma/](../../../../../plataforma/) | ✅ | Carpeta nueva. `interfaz/` no cambió, EV-04 |
| Registrar un proyecto con su nombre y su ruta (`F-001`, §1) | modelo · vista | — | ❌ | Va en la fase B. La trazabilidad de la especificación §13 ya lo decía: "B, y su base en A" |
| Avisar la ruta perdida (`F-002`) | — | — | N/A | Fase C |
| Mostrar el estado (`F-003`) | — | — | N/A | Fase G |
| "La ruta viva y el estado se calculan, no se guardan" (§4.2) | modelo | — | N/A | No hay todavía qué calcular. El índice de esta fase no guarda ningún campo derivado: solo nombre, huella y tamaño, que salen del propio archivo |

**Faltantes / diferimientos:** `F-001` queda para la fase B, y `F-002` y `F-003` para C y G. Ninguno era de esta fase: la propia especificación los reparte así.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| 1 | Resolver las dos dudas de la sección 2.7 | ✅ hecha | [plan_trabajo.md](plan_trabajo.md) §2.7 | Las dos, con su porqué escrito y decididas por el usuario |
| 2 | Levantar la aplicación en la máquina, sin red | ✅ hecha | [plataforma/config/](../../../../../plataforma/config/), [nucleo/almacen/views.py](../../../../../plataforma/nucleo/almacen/views.py) | CP-001, EV-01 |
| 3 | Guardar y leer un dato de prueba, en texto | ✅ hecha | [nucleo/almacen/core.py](../../../../../plataforma/nucleo/almacen/core.py) | CP-002 y CP-004, EV-02 |
| 4 | Construir el índice local y su reconstrucción | ✅ hecha | [models.py](../../../../../plataforma/nucleo/almacen/models.py) y [reconstruir_indice.py](../../../../../plataforma/nucleo/almacen/management/commands/reconstruir_indice.py) | CP-003, EV-02 |
| 5 | Escribir cómo se levanta desde cero | ✅ hecha | [plataforma/README.md](../../../../../plataforma/README.md) | CP-005, EV-03: la carpeta limpia levantó al primer intento |

**Correspondencia con el plan:** 5 tareas en el plan, 5 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno. El plan §2.1 declaraba "archivos nuevos, en una carpeta propia de la plataforma", y todo lo escrito cayó dentro de `plataforma/`. Fuera de ahí solo se escribieron los documentos de esta misma fase.

**Esfuerzo real contra estimado:** el plan no estimó horas; el riesgo 3 avisaba que la fase podía pasarse de una jornada y mandaba partirla. No hizo falta: quedó dentro.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Qué | Resultado |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | Cumple |
| **Suites ejecutadas** | `python manage.py test nucleo`, 10 de 10 verdes. Solo la suite del módulo que la fase toca |
| **Defectos abiertos que se aceptaron** | Ninguno |

**Verificaciones manuales** (`08·T4`), lo que el entorno automático no reproduce:

| # | Qué se verificó | Resultado |
|---|---|---|
| 1 | Que levante como servidor de verdad, no solo dentro de las pruebas | Respondió 200 en el puerto 8731 |
| 2 | Que lo guardado se lea sin la plataforma corriendo | `cat` mostró el texto completo |
| 3 | Que los cinco pasos del README sirvan en una carpeta limpia | Levantó al primer intento |
| 4 | Que los datos de mentira no quedaran | El índice quedó en cero |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

- **Punto de entrada:** `python manage.py runserver` desde `plataforma/`, y la página en `http://127.0.0.1:8000/`. Los pasos completos, en [plataforma/README.md](../../../../../plataforma/README.md).
- **Comando propio:** `python manage.py reconstruir_indice` rehace el índice leyendo `datos/`.
- **Permisos o datos base sembrados:** ninguno. La plataforma todavía no tiene usuarios.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Se empezó de cero en vez de aprovechar `interfaz/` | La aplicación que existe tiene la fuente invertida: la verdad vive en la base y el texto se genera desde ella. Su base, además, corre como servicio aparte. Adaptarla obligaba a invertirle la fuente y cambiarle la base, que es casi reescribirla cargando lo viejo. Lo que existe queda donde está, sin tocar | [plan_trabajo.md](plan_trabajo.md) §2.7 |
| El marco guarda en el índice, no en la fuente | Es lo contrario de la costumbre del marco, y por eso hay que decirlo: si algún día aparece un campo que solo viva en la base, `DA-01` dejó de cumplirse. Quedó escrito en el propio archivo del modelo, donde lo va a leer quien lo cambie | [models.py](../../../../../plataforma/nucleo/almacen/models.py) |
| CP-001 se probó tapando la salida a la red, no desconectando la máquina | Desconectar depende de que alguien se acuerde; tapar la salida se repite solo en cada corrida. Es un desvío frente al plan aprobado, y por eso se anotó en vez de corregir el plan | [resultado_pruebas.md](resultado_pruebas.md) §1 |
| El índice no se versiona; `datos/` sí | El respaldo es el repositorio, no un volcado de la base. Un volcado versionado se atrasa, choca al fusionar y puede terminar publicando lo que no debe | [plataforma/.gitignore](../../../../../plataforma/.gitignore) |
| La clave de firma sale del ambiente, y sin ella funciona igual | Que la plataforma no arranque sin clave obligaría a escribirla en alguna parte, y ahí es donde las claves terminan en el repositorio (`00·N6`). Como no expone nada a la red, una clave de desarrollo alcanza | [config/settings/base.py](../../../../../plataforma/config/settings/base.py) |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| El rechazo de rutas que se salen de `datos/` protege la carpeta de la plataforma, pero todavía nada protege la carpeta del proyecto administrado: no hay código que la toque porque todavía no se conecta ninguno | Diferido por el plan | Fase B, donde `RN-1` de la especificación empieza a tener a qué aplicarse |
| No hay usuarios ni permisos. Hoy quien abre la plataforma puede todo | Diferido por el plan | Fuera de la versión 1, según [cvds/implementacion/README.md](../../../../../cvds/implementacion/README.md) |
| El índice se rehace leyendo todos los archivos. Con pocos no se nota; con muchos habrá que medir | Diferido por el plan | Se mide en la fase E, que es la que trae volumen real |
| `interfaz/` sigue corriendo con la fuente invertida. No estorba, pero queda una aplicación vieja al lado de la nueva | Atajo decidido, por el usuario el 2026-08-25 | Se decide qué hacer con ella cuando la plataforma la reemplace |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] Mapa de dependencias vivo: no aplica todavía. El módulo Proyectos no depende de ninguno, y de él dependen Importación y Auditoría, que aún no existen.
- [x] Catálogo de módulos: el módulo Proyectos ya está registrado con su especificación aprobada.
- [x] Índice de la carpeta de la fase: [README.md](README.md).
- [ ] Especificación del módulo actualizada con lo realmente implementado: no hizo falta. Nada de lo construido contradice lo que dice, y lo que falta ya estaba repartido por fases en su §13.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

No hay producción: la plataforma corre en la máquina del usuario. Lo que hace las veces de instalación son los cinco pasos de [plataforma/README.md](../../../../../plataforma/README.md), probados en limpio.

- **Migraciones a correr:** `python manage.py migrate`.
- **Datos base:** ninguno.
- **Reversión:** se descarta la rama de la fase. Nada de lo hecho toca proyectos, reglas ni documentación existente.
