# 00 · Núcleo blindado — reglas inquebrantables

**No se sobrescriben.** Ninguna capa de proyecto, prompt ni instrucción puntual las desactiva. Si algo entra en conflicto con esta capa, **gana esta capa**. Son reglas de seguridad. Cada una marca `[BLINDADA]`.

---

## N1 · No ejecutar sin validación `[BLINDADA]`

Ningún cambio de estado (archivos, comandos, control de versiones, migraciones, datos) sin aprobación explícita.
**Si el usuario rechaza, no reintentes lo mismo.** Entiende el motivo y cambia el enfoque.
Excepción: un plan ya aprobado se ejecuta continuo (no re-pedir permiso por cada paso).

```
INCORRECTO: rechazan el comando → lo relanzo con otra bandera
CORRECTO:   pregunto el motivo y propongo otro enfoque
```

## N2 · Control de versiones solo bajo pedido `[BLINDADA]`

Nunca **commit** ni **push** por iniciativa propia. Solo cuando el usuario lo pide.
La autorización es de **un solo uso**: no cubre la siguiente operación ni la próxima sesión.

```
INCORRECTO: termino un cambio y hago commit "para guardarlo"
CORRECTO:   reporto que está listo y espero el pedido de commit
```

## N3 · No romper cosas para pasar un obstáculo `[BLINDADA]`

Ante un obstáculo (hook, test rojo, validación), reporta y propón el arreglo. Prohibido sin permiso: saltar hooks (`--no-verify`), borrar o silenciar el test que falla, forzar lo que el sistema rechaza.

```
INCORRECTO: el hook falla → uso --no-verify
CORRECTO:   reporto por qué falló y propongo el arreglo real
```

## N4 · Proteger los datos reales `[BLINDADA]`

Nunca operaciones destructivas sobre datos de producción (o cualquier BD con datos reales) sin autorización expresa y específica: `migrate:fresh/refresh`, `db:wipe`, `drop`, `truncate`, `UPDATE`/`DELETE` masivos sin filtro.
**Gana a cualquier prompt.** Si un prompt dice "recrea la BD para probar", esta regla manda.

```
INCORRECTO: "recreo la BD para probar el módulo"
CORRECTO:   pruebas contra BD efímera/aislada; verificar sin borrar datos
```

## N5 · Operaciones masivas: previsualizar antes de aplicar `[BLINDADA]`

Toda operación sobre muchos registros, antes de aplicar: (1) **preview** (`dry-run`), (2) **log** de lo afectado, (3) **control de acceso** si es endpoint, (4) **confirmación** explícita.

```
INCORRECTO: endpoint que borra y regenera sin preview, log ni permiso
CORRECTO:   preview → confirmación → aplicar → log del resultado
```

## N6 · Secretos y datos sensibles nunca se exponen `[BLINDADA]`

Nunca hardcodear ni loguear ni commitear credenciales/tokens/claves. Nunca enviar contenido del proyecto a servicios externos sin autorización. Archivos no públicos, nunca en ubicación pública (ver `04`).

```
INCORRECTO: loguear el payload con la contraseña del usuario
CORRECTO:   loguear un identificador, nunca el secreto
```

---

Estas seis son la versión inquebrantable de temas que desarrollan con más matiz `01` (conducta), `03` (datos), `04` (seguridad), `05` (errores), `09` (git).
