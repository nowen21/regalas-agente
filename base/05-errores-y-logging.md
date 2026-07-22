# 05 · Manejo de errores y logging

> **Capa 2 · agnóstica al stack.** Cómo tratar los fallos y qué registrar. Un buen manejo de errores hace el sistema diagnosticable sin filtrar información ni ocultar problemas. La capa 3 declara el framework de logging concreto y los destinos (archivo, servicio, consola).

---

## E1 · No tragarse los errores en silencio

Un error capturado se maneja de forma **visible y trazable**. Nunca un bloque que atrapa la excepción y no hace nada, ni un catch que oculta el fallo para "que no moleste".

- Si el error es recuperable: manejarlo explícitamente y dejar constancia (log) de que ocurrió.
- Si no es recuperable: **dejarlo propagar** hasta un manejador central que lo registre y responda de forma controlada.
- No convertir un error en un valor de retorno ambiguo (`null`, `false`, `0`) sin registrar la causa: el siguiente que lea el código no sabrá si fue éxito vacío o fallo.

```
INCORRECTO: try { ... } catch (e) { }          // silencia el fallo
CORRECTO:   try { ... } catch (e) { log.error(...); rethrow o manejar explícito }
```

---

## E2 · Fallar de forma controlada, no rodear el problema

Ante un error que bloquea la operación, el sistema (y el agente que lo desarrolla) **reporta y detiene de forma limpia**, no fuerza el paso.

- Validar las precondiciones al inicio y **abortar temprano** con un mensaje claro si no se cumplen, en vez de fallar a mitad con un estado inconsistente.
- Las operaciones que tocan varios registros que deben quedar consistentes van en una **transacción**: o se aplican todas, o ninguna.
- No dejar el sistema en estado a medias por atrapar un error y seguir como si nada.

> Para el agente: la variante destructiva de "no rodear el obstáculo" (no `--no-verify`, no borrar el test que falla) está blindada en el núcleo (`00` · N3).

```
INCORRECTO: crear el registro padre, fallar al crear el hijo, y dejar el padre huérfano
CORRECTO:   envolver ambos en una transacción → si el hijo falla, se revierte el padre
```

---

## E3 · Mensajes de error en dos niveles: usuario y diagnóstico

Separar siempre lo que ve el usuario de lo que necesita quien diagnostica:

- **Al usuario:** un mensaje claro, en su idioma, **accionable** ("No se pudo guardar: el correo ya está registrado"), sin jerga técnica ni internos.
- **Al log:** el detalle completo para diagnosticar (tipo de excepción, contexto, identificador de correlación).
- **Nunca** exponer al usuario trazas de pila, consultas, rutas del sistema o versiones (es fuga de información — `04-seguridad.md` S8).

```
INCORRECTO: al usuario: "SQLSTATE[23000]: Integrity constraint violation... INSERT INTO..."
CORRECTO:   al usuario: "Ese registro ya existe."   ·   al log: la excepción completa
```

---

## E4 · Loguear con niveles y con propósito

Cada registro de log tiene un **nivel** acorde a su gravedad y un contenido útil para diagnosticar:

- **error / crítico:** fallos que requieren atención (excepción no manejada, operación abortada).
- **warning:** situaciones anómalas pero manejadas (reintento, dato faltante con fallback, archivo no encontrado).
- **info:** hitos operativos relevantes (operación masiva ejecutada, proceso batch completado).
- **debug:** detalle fino, normalmente apagado en producción.

Buenas prácticas:

- Incluir **contexto** que permita rastrear (identificadores de entidad, de usuario, de correlación), no solo "algo falló".
- No loguear en exceso: ruido constante entierra las señales reales.
- Registrar las **operaciones sensibles y masivas** para auditoría (quién, qué, cuántos, cuándo) — núcleo `00` · N5.

```
INCORRECTO: log.error("error")                       // sin contexto, inservible
CORRECTO:   log.error("Falló causar factura", { factura_id, usuario_id, causa })
```

---

## E5 · Nunca registrar secretos ni datos sensibles

> Blindado en el núcleo (`00` · N6).

Los logs **no** contienen contraseñas, tokens, claves, ni más datos personales de los estrictamente necesarios. Enmascarar o excluir esos campos antes de registrar. Un log es un artefacto que se copia, se envía a terceros y se conserva: tratarlo como potencialmente público.

```
INCORRECTO: log.info("Login", { email, password })       // secreto en el log
CORRECTO:   log.info("Login", { usuario_id })            // sin credenciales
```

---

## Relación con el resto del estándar

- **Núcleo `00` · N3/N5/N6** — no rodear obstáculos con acciones destructivas; auditar operaciones masivas; no exponer secretos.
- **`04-seguridad.md`** — no filtrar internos ni datos sensibles.
- **`01-conducta.md` C9** — para el agente: reportar el obstáculo, no esconderlo.
- **`12-privacidad-datos.md`** — minimización de datos personales, también en logs.
