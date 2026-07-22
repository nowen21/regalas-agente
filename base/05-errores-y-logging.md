# 05 · Manejo de errores y logging

Cómo tratar fallos y qué registrar, sin filtrar información ni ocultar problemas. La capa 3 declara el framework de logging y los destinos.

---

## E1 · No te tragues los errores en silencio

Un error capturado se maneja **visible y trazable**. Nada de `catch` vacío.

- Recuperable: manéjalo y deja constancia (log).
- No recuperable: déjalo **propagar** a un manejador central que lo registre y responda controlado.
- No lo conviertas en un retorno ambiguo (`null`/`false`) sin registrar la causa.

```
INCORRECTO: try { ... } catch (e) { }
CORRECTO:   try { ... } catch (e) { log.error(...); manejar o propagar }
```

## E2 · Falla controlado, no rodees el problema

- Valida precondiciones al inicio y **aborta temprano** con mensaje claro, en vez de fallar a mitad con estado inconsistente.
- Operaciones que dejan varios registros consistentes van en **transacción**: todo o nada.

> La variante destructiva ("no `--no-verify`, no borrar el test") está en `00` · N3.

```
INCORRECTO: creo el padre, falla el hijo, y dejo el padre huérfano
CORRECTO:   ambos en transacción → si falla el hijo, se revierte el padre
```

## E3 · Mensajes en dos niveles: usuario y diagnóstico

- **Al usuario:** claro, en su idioma, **accionable** ("Ese correo ya está registrado"), sin jerga ni internos.
- **Al log:** el detalle completo (excepción, contexto, id de correlación).
- **Nunca** trazas/consultas/rutas al usuario (es fuga de info — `04` · S8).

```
INCORRECTO: al usuario: "SQLSTATE[23000]... INSERT INTO..."
CORRECTO:   al usuario: "Ese registro ya existe."  ·  al log: la excepción completa
```

## E4 · Loguea con niveles y con propósito

- **error/crítico:** fallos que requieren atención.
- **warning:** anómalo pero manejado (reintento, fallback, no encontrado).
- **info:** hitos operativos (masiva ejecutada, batch completado).
- **debug:** detalle fino, apagado en producción.

Incluye **contexto** para rastrear (ids de entidad/usuario/correlación). No loguees de más (el ruido entierra la señal). Registra las operaciones masivas para auditoría (`00` · N5).

```
INCORRECTO: log.error("error")
CORRECTO:   log.error("Falló causar factura", { factura_id, usuario_id, causa })
```

## E5 · Nunca registres secretos ni datos sensibles

Blindado en `00` · N6. Los logs no llevan contraseñas, tokens, ni más datos personales de los necesarios. Enmascara o excluye. Trata el log como potencialmente público.

```
INCORRECTO: log.info("Login", { email, password })
CORRECTO:   log.info("Login", { usuario_id })
```

---

Ver: `00` N3/N5/N6, `04` S8 (no filtrar), `01` C9 (reportar, no esconder), `12` (privacidad en logs).
