# Pendiente · Dos sesiones versionando a la vez

**Estado:** abierto · anotado 2026-08-14 · nace del hallazgo H-9 de [2026-08-14](../historico-chat/resumenes/2026-08-14/hu-de-la-comprobacion-automatica.md).

## El problema

El 2026-08-14 hubo dos sesiones abiertas sobre el mismo repositorio. Una escribió la versión 10.0.0 mientras la otra subía la 9.0.0, la 9.1.0 y la 9.2.0. Al final del día la versión iba en 12.2.0 con dos numeraciones vivas y entradas del registro escritas por las dos.

`VERSION` y `CHANGELOG.md` son un archivo único cada uno, y ninguna sesión sabe qué está haciendo la otra. La regla de que cada sesión sube solo lo suyo se rompe justo ahí: para guardar lo propio hay que arrastrar lo ajeno.

## Qué falta

Decidir quién manda sobre la versión y escribirlo. Tres opciones sobre la mesa:

**1. La versión se sube al guardar el cambio, no al editarlo.** El número lo pone quien commitea, con lo que haya en ese momento.

**2. Cada sesión escribe su entrada del registro en un archivo aparte** y se juntan al guardar. El registro deja de ser un archivo que dos sesiones editan.

**3. Una sola sesión a la vez toca el estándar.** Es lo más simple y lo más incómodo.

## El límite

Esto no lo resuelve un validador: puede detectar el cruce, no evitarlo. Lo que hace falta primero es el acuerdo.
