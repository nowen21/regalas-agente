# 04 · Seguridad de la aplicación

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

INCORRECTO: Modelo::create(request.all())
CORRECTO:   asignar solo los campos permitidos
```

## S4 · Gestión de secretos

El mínimo está en `00` · N6. Además:

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
- **Preservación:** al borrar (lógico) la entidad padre, el archivo **no se elimina físico**. La purga física es operación admin con preview (`00` · N5).
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

---

Ver: `00` N6 (secretos), `03` (integridad de datos), `05` (errores), `10` (dependencias), `12` (privacidad).
