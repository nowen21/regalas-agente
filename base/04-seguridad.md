# 04 · Seguridad de la aplicación

> **Capa 2 · agnóstica al stack.** Buenas prácticas de seguridad que aplican a todo desarrollo, más allá del almacenamiento de archivos. El núcleo (`00`) blinda los mínimos innegociables (secretos, datos reales); esta sección desarrolla el resto con matiz y ejemplos. La capa 3 declara los mecanismos concretos (sistema de permisos, motor de plantillas, disco de almacenamiento).

---

## S1 · Autorización en cada acción sensible

Toda acción que lea o modifique datos no públicos verifica **autenticación y permiso** en el servidor, antes de ejecutarse. La validación en el cliente (ocultar un botón, deshabilitar un campo) es UX, **no** seguridad: nunca reemplaza la verificación server-side.

- Verificar el permiso **en el punto de entrada** de la acción (controlador, endpoint, comando), no confiar en que "no se llega por la UI".
- Validar el **alcance (scope)**: el usuario solo accede a los registros a los que tiene derecho (su proyecto, su organización, su grupo) — no basta con tener el permiso genérico.
- Las acciones de mayor peso (anular, eliminar, operaciones masivas, administración) llevan un **permiso propio**, distinto del permiso de lectura o edición corriente.

```
INCORRECTO: ocultar el botón "Eliminar" en la vista y confiar en que el usuario no llame al endpoint
CORRECTO:   verificar el permiso en el servidor al inicio de la acción + validar el scope del registro
```

---

## S2 · Validar y sanear toda entrada externa

Todo dato que viene de afuera (formularios, parámetros de URL, cabeceras, cargas de archivos, APIs de terceros) es **no confiable** hasta validarlo.

- **Validar** tipo, rango, formato y pertenencia a valores permitidos en el servidor.
- **Escapar/sanear** según el destino: al renderizar en HTML (evitar XSS), al construir consultas, al usar el dato en rutas de archivos o comandos.
- Aplicar **lista blanca** (lo permitido) antes que lista negra (lo prohibido).
- En cargas de archivos: validar tipo real y tamaño; **nunca** aceptar tipos ejecutables.

```
INCORRECTO: renderizar directo el nombre que escribió el usuario en el HTML
CORRECTO:   escapar la salida al renderizar (defensa contra XSS)
```

---

## S3 · Nunca construir consultas ni comandos por concatenación

- **Consultas a BD:** usar siempre sentencias parametrizadas / consultas preparadas / el ORM. **Nunca** concatenar entrada del usuario dentro de una consulta (inyección SQL).
- **Comandos del sistema:** evitar construir comandos de shell con entrada del usuario; si es inevitable, usar APIs que separen el comando de sus argumentos y escapar rigurosamente (inyección de comandos).
- **Asignación masiva:** no volcar ciegamente todo el payload de una petición a un modelo; declarar explícitamente qué campos son asignables (evita que el usuario setee campos que no debería, como `es_admin`).

```
INCORRECTO: "SELECT * FROM users WHERE email = '" + input + "'"
CORRECTO:   consulta parametrizada con el input como parámetro enlazado

INCORRECTO: Modelo::create(request.all())   // asignación masiva sin filtro
CORRECTO:   asignar solo los campos permitidos explícitamente
```

---

## S4 · Gestión de secretos

> El mínimo está blindado en el núcleo (`00` · N6): nunca hardcodear ni exponer secretos. Aquí, las prácticas para gestionarlos bien.

- Los secretos (claves de API, credenciales de BD, tokens, claves de firma) viven en **configuración de entorno**, fuera del código versionado (ver `11-configuracion-entornos.md`).
- El archivo de entorno real y sus variantes con secretos están **ignorados por el control de versiones**. Se versiona solo una plantilla de ejemplo, sin valores reales.
- **Rotar** un secreto que se haya expuesto por accidente (commit, log, captura); no basta con borrarlo, hay que invalidarlo.
- No enviar secretos a servicios externos (incluido logging de terceros) sin cifrar y sin necesidad.

```
INCORRECTO: const API_KEY = "sk-live-abc123" en el código
CORRECTO:   leer la clave de la configuración de entorno; el valor real nunca se versiona
```

---

## S5 · Proteger CSRF, sesiones y transporte

- **CSRF:** las acciones que cambian estado por navegador llevan protección contra falsificación de petición (token anti-CSRF); usar el mecanismo del framework, no desactivarlo por comodidad.
- **Sesiones y cookies:** cookies de sesión marcadas como `HttpOnly` y `Secure`; invalidar la sesión al cerrar sesión; expiración razonable.
- **Transporte:** los datos sensibles viajan siempre sobre canal cifrado (HTTPS). No enviar credenciales ni datos personales por canales sin cifrar.
- **Contraseñas y secretos de usuario:** se almacenan con hashing fuerte y salt, nunca en texto plano ni con hashing reversible.

---

## S6 · Archivos sensibles: almacenamiento privado + acceso controlado

Todo archivo cargado que contenga información no pública (financiera, jurídica, personal, confidencial) cumple:

- **Almacenamiento privado**, nunca en una ubicación servida públicamente ni con URL adivinable.
- **Acceso solo por un punto controlado** con autenticación + permiso + validación de scope (el usuario solo descarga lo que le corresponde). Forzar descarga, no incrustar sin control.
- El modelo guarda metadatos mínimos del archivo (ubicación, tipo, tamaño) para poder migrar de almacenamiento sin cambiar código.
- **Preservación:** al borrar (lógicamente) la entidad padre, el archivo **no se elimina físicamente** — se conserva para trazabilidad. La purga física es una operación administrativa explícita y con preview (núcleo `00` · N5).
- **Backup:** el almacenamiento de archivos se respalda junto con la BD.
- **Validación de carga:** tipos permitidos por lista blanca y tamaño máximo; nunca tipos ejecutables.

```
INCORRECTO: guardar un documento sensible en una carpeta pública con URL directa
CORRECTO:   almacenamiento privado + endpoint con auth/permiso/scope que sirve el archivo

INCORRECTO: al borrar la entidad, eliminar físicamente su archivo de soporte
CORRECTO:   preservar el archivo; la purga física es un comando administrativo con preview
```

---

## S7 · Dependencias sin vulnerabilidades conocidas

Las librerías de terceros son superficie de ataque. Mantener las dependencias actualizadas y **auditar vulnerabilidades conocidas** con la herramienta del ecosistema. No introducir una dependencia con vulnerabilidades sin resolver. (Detalle en `10-dependencias.md`.)

---

## S8 · No filtrar información en errores

Los mensajes de error de cara al usuario **no exponen** detalles internos (trazas de pila, consultas, rutas del sistema, versiones). Se registra el detalle en el log del servidor y se muestra al usuario un mensaje genérico y accionable. (Detalle en `05-errores-y-logging.md`.)

```
INCORRECTO: mostrar la traza completa y la consulta SQL en una página de error 500
CORRECTO:   loguear el detalle en el servidor; al usuario, un mensaje claro sin internos
```

---

## Relación con el resto del estándar

- **Núcleo `00` · N6** — secretos y datos sensibles nunca se exponen; archivos sensibles nunca públicos.
- **`03-datos.md`** — integridad de esquema y validación en la app se complementan con estas defensas.
- **`05-errores-y-logging.md`** — no filtrar datos ni internos en errores y logs.
- **`10-dependencias.md`** — vetting y auditoría de librerías de terceros.
- **`12-privacidad-datos.md`** — protección específica de datos personales.
