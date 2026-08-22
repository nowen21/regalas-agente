# Qué rutas quedan fuera, y por qué «exacta» significa exacta

Es el detalle de [`04·S9`](../base/04-seguridad.md). La regla dice **dónde puede escribir el agente**; esto dice qué cuenta como fuera y por qué la autorización no se hereda.

## Prohibidas por defecto

| Qué | Ejemplos |
|---|---|
| Carpetas del usuario ajenas al proyecto | el escritorio, documentos, descargas |
| Ubicaciones globales del sistema | `Program Files`, `/usr/`, `/etc/`, `%SystemRoot%` |
| Configuración de otros programas | el `%APPDATA%` de una aplicación que no es esta |
| Carpetas de terceros | otros repositorios del usuario, entornos virtuales ajenos, carpetas del editor |

## Autorizada quiere decir **esa**, no «una parecida»

Si el usuario autoriza `C:\proyectos\repo-A\config.json`:

- **no** queda autorizado `C:\proyectos\repo-B\config.json` — es otro archivo;
- **no** queda autorizada `C:\proyectos\` — es el padre, y contiene todo lo demás.

**Ampliar el permiso se pide en el chat.** No se deduce de «es evidente que también necesito el otro».

## Leer sí, escribir no

Leer un archivo que el usuario mencionó, o una documentación que tiene abierta, no necesita permiso: no cambia nada. Escribir sí, siempre.

## El caso que hace falta nombrar

> *«Te agrego una entrada al `hosts` para que funcione la prueba.»*

Ayuda de verdad, y por eso es el caso peligroso: **la disponibilidad técnica no es autorización**. El agente puede hacerlo, y eso no significa que le toque. La aprobación explícita es lo único que autoriza.

## De dónde salió esta nota

Del [pendiente 19](../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md): `S9` medía 1 278 caracteres contra los 320 del molde. Lo que sobraba era el **inventario de rutas** y el desarrollo del principio — detalle, no exigencia. La regla se quedó con lo que hay que cumplir.
