# Pertenencia y autoría: por qué se confunden y qué rompe

Es el porqué de [`03·D8`](../base/03-datos.md#d8--distingue-pertenencia-de-autoría-en-el-modelo-de-datos). La regla dice **qué** hay que hacer; esto dice por qué la gente hace lo otro, que es lo que hace falta para no repetirlo.

## Los dos conceptos

| | Qué contesta | Columnas típicas | Para qué sirve |
|---|---|---|---|
| **Pertenencia** | ¿de quién es el dato como entidad de negocio? | `tenant_id`, `organizacion_id`, `proyecto_id`, `cuenta_id`, `equipo_id` | Ancla la entidad al contenedor que la posee |
| **Autoría** | ¿quién lo manipuló? | `usercreate_id`, `userupdate_id` | Auditoría, y nada más |

## La confusión típica

**Anclar la entidad al usuario que la creó** —`Auth::id()`, `usercreate_id`— y filtrar los listados por ahí.

Se ve bien el primer día porque hay un solo usuario. **Rompe en cuanto hay dos:**

- Un segundo usuario del mismo contenedor entra y **no ve nada**.
- El usuario original se va, y las entidades quedan atadas a una cuenta que ya no opera.
- Cualquier reasignación obliga a reescribir filas en vez de cambiar un permiso.

**Es un error que no avisa.** Ninguna prueba falla, ningún dato se corrompe: simplemente el sistema deja de servir cuando entra el segundo usuario, y para entonces el modelo ya tiene datos.

## Qué cambia en la práctica cuando el modelo es correcto

| Dónde | Va por |
|---|---|
| Consultas de listado | **Pertenencia** — según a qué contenedores tiene acceso el usuario actual |
| Permisos y *scope* | **Pertenencia** — «X tiene permiso Y sobre el contenedor Z», no «X creó el registro» |
| Ediciones | **Pertenencia** — no hace falta ser el creador; basta acceso al contenedor y permiso |
| Reportes de auditoría | **Autoría** — quién hizo qué |

## La pregunta que los separa

> **¿Esto es del usuario, o del contenedor donde el usuario está trabajando?**

Si la respuesta es «del usuario» de verdad —un borrador privado, un favorito, una preferencia de interfaz—, la pertenencia **sí** es el usuario, y `D8` lo admite como excepción. Si es «del contenedor», anclarlo al usuario es el defecto.

## De dónde salió esta nota

Del [pendiente 19](../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md): `D8` medía 1 962 caracteres contra los 320 que da el molde, y la fila 10 del checklist dice qué hacer con eso — *«o son dos reglas, o se está contando el **porqué** (va a `notas/`)»*. Era lo segundo: la regla es una sola exigencia y venía con su explicación pegada.
