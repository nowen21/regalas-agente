# 04 · Seguridad de la aplicación  ·  `[CAPA 2]`

Seguridad más allá de los archivos. El núcleo (`00`) blinda los mínimos; aquí el detalle. La capa 3 declara los mecanismos concretos (permisos, plantillas, almacenamiento).

---

## S1 · Autorización en cada acción sensible

Toda acción que lee o cambia datos no públicos verifica **autenticación y permiso en el servidor**, antes de ejecutarse. Ocultar un botón es UX, no seguridad.

- Verifica el permiso en el punto de entrada (controlador/endpoint/comando).
- Valida el **scope**: el usuario solo accede a sus registros (su proyecto, su organización), no basta el permiso genérico.
- Acciones de peso (anular, eliminar, masivas, admin) llevan **permiso propio**.

```
INCORRECTO: oculto el botón "Eliminar" y confío en que no llamen al endpoint
CORRECTO:   verifico permiso en el servidor + valido el scope del registro
```

## S2 · Valida y sanea toda entrada externa

Todo dato de afuera (formularios, URL, cabeceras, archivos, APIs) es **no confiable** hasta validarlo.

- Valida tipo, rango, formato y valores permitidos en el servidor.
- Escapa según el destino: HTML (XSS), consultas, rutas de archivo, comandos.
- **Lista blanca** antes que lista negra.
- Archivos: valida tipo real y tamaño; nunca tipos ejecutables.

```
INCORRECTO: renderizar directo lo que escribió el usuario
CORRECTO:   escapar la salida al renderizar (XSS)
```

## S3 · Nunca construyas consultas ni comandos por concatenación

- **BD:** consultas parametrizadas / ORM. Nunca concatenar entrada en la consulta (inyección SQL).
- **Shell:** evita comandos con entrada del usuario; si es inevitable, separa comando y argumentos y escapa (inyección de comandos).
- **Asignación masiva:** declara qué campos son asignables; no vuelques todo el payload al modelo (evita que seteen `es_admin`).

```
INCORRECTO: "SELECT * FROM users WHERE email = '" + input + "'"
CORRECTO:   consulta parametrizada con el input como parámetro

INCORRECTO: crear el registro volcando todo el payload de la petición
CORRECTO:   asignar solo los campos permitidos explícitamente
```

## S4 · Gestión de secretos

El mínimo está en [`00·N6`](00-nucleo-blindado.md#n6--secretos-y-datos-sensibles-nunca-se-exponen-blindada). Además:

- Secretos (claves, credenciales, tokens) en **configuración de entorno**, fuera del código (ver `11`).
- El archivo de entorno real está **ignorado** por el control de versiones; se versiona solo una plantilla sin valores.
- Un secreto expuesto por accidente se **rota** (no basta borrarlo).

```
INCORRECTO: const API_KEY = "sk-live-abc123"
CORRECTO:   leerla de la configuración de entorno; el valor real no se versiona
```

## S5 · CSRF, sesiones y transporte

- **CSRF:** token anti-falsificación en acciones que cambian estado por navegador; no lo desactives por comodidad.
- **Sesiones:** cookies `HttpOnly` y `Secure`; invalidar al cerrar sesión; expiración razonable.
- **Transporte:** datos sensibles siempre por HTTPS.
- **Contraseñas:** hashing fuerte con salt, nunca en texto plano.

## S6 · Archivos sensibles: privado + acceso controlado

Todo archivo no público (financiero, jurídico, personal):

- **Almacenamiento privado**, nunca en ubicación pública ni con URL adivinable.
- Acceso por un **punto controlado** (auth + permiso + scope); forzar descarga.
- Guarda metadatos (ubicación, tipo, tamaño) para poder migrar de almacenamiento sin tocar código.
- **Preservación:** al borrar (lógico) la entidad padre, el archivo **no se elimina físico**. La purga física es operación admin con preview ([`00·N5`](00-nucleo-blindado.md#n5--operaciones-masivas-previsualizar-antes-de-aplicar-blindada)).
- **Backup** junto con la BD. Carga con lista blanca de tipos y tamaño máximo.

```
INCORRECTO: documento sensible en carpeta pública con URL directa
CORRECTO:   almacenamiento privado + endpoint con auth/permiso/scope
```

## S7 · Dependencias sin vulnerabilidades conocidas

Mantén las dependencias al día y **audita vulnerabilidades** con la herramienta del ecosistema. No introduzcas una con vulnerabilidades sin resolver (detalle en `10`).

## S8 · No filtres información en errores

Los errores de cara al usuario no exponen internos (trazas, consultas, rutas, versiones). El detalle va al log; al usuario, un mensaje genérico y accionable (detalle en `05`).

```
INCORRECTO: mostrar la traza y el SQL en una página de error
CORRECTO:   loguear el detalle; al usuario, mensaje claro sin internos
```

## S9 · No toques rutas del sistema fuera del proyecto · solo autorizadas exactas

El agente **solo escribe, mueve, elimina o modifica archivos dentro de la carpeta del proyecto** o dentro de rutas **explícitamente autorizadas** por el usuario (ubicaciones estándar declaradas en la capa 3, como la carpeta central de la base común del agente).

- **Rutas del sistema operativo prohibidas por defecto:** carpetas de usuario ajenas al proyecto, ubicaciones globales del OS (Program Files, `/usr/`, `/etc/`, `%SystemRoot%`, `%APPDATA%` de otros programas), carpetas de terceros (otros proyectos del usuario, IDEs, entornos virtuales de otros repos).
- **Ruta autorizada = ruta exacta**, no "una ruta parecida" ni "un padre común". Si el usuario autoriza `C:\proyectos\repo-A\config.json`, no se autoriza `C:\proyectos\repo-B\config.json` ni `C:\proyectos\`.
- **Lectura permitida** sin autorización cuando el archivo es de referencia declarada (docs abiertas del usuario, path que el usuario mencionó). Escritura NO.
- **Ampliación de rutas autorizadas** requiere autorización explícita del usuario en el chat. No se infiere de "es evidente que también necesito Y".

Este comportamiento aplica incluso cuando el cambio "obviamente ayuda" ("agrego una entrada a tu `hosts` para que funcione la prueba"). La disponibilidad técnica no autoriza — la aprobación explícita sí.

```
INCORRECTO: durante una fase, escribir en la carpeta home del usuario o en Program Files
            "porque es más práctico" → efecto lateral fuera del alcance del proyecto,
            imposible de auditar desde el repo
CORRECTO:   quedarse dentro del proyecto; si algo fuera realmente es necesario,
            reportarlo y esperar autorización de la ruta exacta
```

## S10 · No mates procesos globales · solo PID exacto y estrictamente necesario

El agente **no mata procesos** del sistema operativo con criterios amplios (por nombre de binario, por patrón, "todos los `node`", "todos los `php`"). Matar procesos globales puede tumbar servicios que el usuario está usando en paralelo (otras terminales, IDEs, servidores de desarrollo de otros proyectos, tareas de fondo del OS).

**Reglas:**

- Matar procesos por **PID exacto**, no por nombre ni patrón.
- Solo cuando el proceso a matar sea **claramente del proyecto** y su terminación sea **estrictamente necesaria** para la tarea (por ejemplo, un servidor de desarrollo que arrancó el agente en la fase actual y quedó colgado).
- **Prohibido** por defecto: `killall`, `pkill -f <patrón>`, `taskkill /IM <binario> /F`, "matar todos los procesos de X".
- Si es realmente necesario terminar por patrón (caso extremo), **pausar y pedir autorización explícita** al usuario indicando qué PID/nombre y por qué.
- Al arrancar un proceso persistente (servidor, watcher), guarda el PID para poder terminarlo puntualmente al cerrar la tarea.

```
INCORRECTO: "hay procesos node colgados" → `killall node` → matas el IDE del usuario
            y los watchers de otros repos
CORRECTO:   identificar el PID exacto del proceso que arrancó la fase actual y matar
            solo ese PID
```

## S11 · Escritura contra el almacén productivo requiere autorización por operación

`00 N4` cubre el principio general de proteger los datos reales. S11 lo refina con dos matices operativos que evitan escapes silenciosos.

**Regla 1 — Autorización por operación, no por sesión.** Cada `create/update/delete` contra el almacén productivo requiere **autorización explícita del usuario para esa operación puntual**. Autorizar una operación previa **no** autoriza las siguientes, aunque sean del mismo tipo. La autorización viaja con la acción, no con la sesión.

**Motivo:** una autorización de sesión abre la puerta a que el agente encadene operaciones no previstas ("ya que estamos, aprovecho y también"), rompiendo el control. Por operación fuerza a que cada acción tenga su OK, con el archivo/tabla/filas concretas nombrados.

**Regla 2 — El borrado lógico cuenta como escritura.** `destroy()`, `SoftDeletes`, `archivar`, `desactivar` y equivalentes que en realidad marcan un campo (`deleted_at`, `activo=false`, `archivado_at`, etc.) son **escrituras** contra el almacén productivo. Requieren autorización explícita como cualquier `update`, aunque el nombre del método sugiera "eliminar".

**Motivo:** el nombre del método puede ocultar la naturaleza de escritura. `destroy()` en un modelo con trait de soft-delete no borra físicamente pero sí modifica una fila productiva — cuenta.

**Antes de escribir contra el almacén productivo:**

- Describir en el chat: qué operación, qué tabla, qué filas concretas (`WHERE ...` o el subconjunto), qué campos.
- Esperar OK explícito del usuario para esa descripción concreta.
- No encadenar operaciones "aprovechando que ya me autorizó lo anterior".

```
INCORRECTO: usuario autoriza "corregí el estado del registro X" → agente aprovecha y
            también corrige los registros Y y Z que "estaban con el mismo bug"
CORRECTO:   agente ejecuta solo X · reporta el hallazgo de Y y Z como recomendación ·
            espera OK explícito antes de tocar cada uno

INCORRECTO: "vamos a limpiar los registros huérfanos con destroy()" — se ejecuta sin
            aviso porque "no es delete físico, es solo soft-delete"
CORRECTO:   `destroy()` con soft-delete = escritura productiva · describir cuántas
            filas afecta + esperar OK
```

**Encadenamiento:** `00 N4` (protege los datos reales) es el principio blindado · `S11` es la especificación operativa · `01 C1` (avisa antes de tocar) — en el contexto de BD productiva, "avisar" significa autorización explícita por operación, no permiso de sesión.

---

Ver: `00` N6 (secretos), `03` (integridad de datos), `05` (errores), `10` (dependencias), `12` (privacidad).
