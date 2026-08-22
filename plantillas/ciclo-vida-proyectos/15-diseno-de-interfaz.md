# Diseño de interfaz   ·   `[CAPA 3]`

**Para qué sirve este documento.** Fija cómo se navega y qué hace cada pantalla **antes** de construirla, para que la conversación sobre la interfaz ocurra sobre este documento y no sobre código ya escrito. Y queda como el inventario de pantallas del sistema: quien llega ve el todo sin recorrer la aplicación.

> Plantilla. Acompaña a la estación 06 y madura con el sistema: cada fase que agregue o cambie una pantalla actualiza acá su fila. Si el proyecto no tiene interfaz de usuario, el documento existe igual y dice: «No aplica porque «el porqué»». Reemplaza los `«…»` y borra esta caja.

## 1. El mapa de navegación

> Desde dónde se llega a qué. Como texto (Mermaid), para que se pueda editar.

```mermaid
flowchart TD
    Entrada --> «Pantalla-A»
    «Pantalla-A» --> «Pantalla-B»
```

## 2. Inventario de pantallas

> Una fila por pantalla. «Quién la ve» es el permiso o rol que la enciende; una pantalla sin dueño de permiso es una pantalla pública, y eso se dice.

| # | Pantalla | Qué hace, para quien la usa | Quién la ve | Estado |
|---|---|---|---|---|
| 1 | «…» | «…» | «rol / permiso / pública» | «Existe / Por construir» |

## 3. Los flujos que importan

> Los recorridos completos que el usuario hace para lograr algo, paso a paso. El flujo feliz y qué pasa cuando algo falla.

### «Nombre del flujo»

1. «El usuario entra a «pantalla» y hace «acción».»
2. «El sistema responde «qué», y si falla, «qué ve el usuario».»

## 4. Convenciones visuales

«Lo que toda pantalla respeta: dónde van las acciones, cómo se avisan los errores, qué se confirma antes de borrar. Si el proyecto declara un sistema de diseño o una librería, se nombra acá y no se re-explica.»
