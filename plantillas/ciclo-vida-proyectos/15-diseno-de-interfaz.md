# Diseño de interfaz   ·   `[CAPA 3]`

**Para qué sirve este documento.** Fija cómo se navega y qué hace cada pantalla **antes** de construirla, para que la conversación sobre la interfaz ocurra sobre este documento y no sobre código ya escrito. Y queda como el inventario de pantallas del sistema: quien llega ve el todo sin recorrer la aplicación.

> Todo documento creado con esta plantilla se redacta aplicando estas reglas. Esta nota se borra al llenarla.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |

> Plantilla del diseño de interfaz. Acompaña a la estación 06 y madura con el sistema: cada fase que agregue o cambie una pantalla actualiza aquí su fila. Si el proyecto no tiene interfaz de usuario, el documento existe igual y dice: «No aplica porque «el porqué»».
>
> Al llenarla se reemplazan los `«…»` y se borran todas las notas como esta. El párrafo «Para qué sirve este documento» se queda.

## 1. El mapa de navegación

> Es el dibujo de desde dónde se llega a cada pantalla. Va en Mermaid, como texto, para que se pueda editar.

```mermaid
flowchart TD
    Entrada --> «Pantalla-A»
    «Pantalla-A» --> «Pantalla-B»
```

## 2. Inventario de pantallas

> Lista las pantallas del sistema, una por fila. La columna Quién la ve lleva el permiso o rol que la habilita; una pantalla sin permiso asignado es pública, y eso se dice.

| # | Pantalla | Qué hace, para quien la usa | Quién la ve | Estado |
|---|---|---|---|---|
| 1 | «…» | «…» | «rol / permiso / pública» | «Existe / Por construir» |

## 3. Los flujos que importan

> Describe paso a paso los recorridos completos que el usuario hace para lograr algo: el camino feliz y qué pasa cuando algo falla.

### «Nombre del flujo»

> Agrupa los pasos de un flujo, con lo que hace el usuario y lo que responde el sistema. Va un bloque por flujo.

1. «El usuario entra a «pantalla» y hace «acción».»
2. «El sistema responde «qué», y si falla, «qué ve el usuario».»

## 4. Convenciones visuales

> Son las reglas de presentación que comparten todas las pantallas.

«Lo que toda pantalla respeta: dónde van las acciones, cómo se avisan los errores, qué se confirma antes de borrar. Si el proyecto declara un sistema de diseño o una librería, se nombra acá y no se re-explica.»

## 5. Qué se ve cuando falta algo

> Dice qué muestra la pantalla cuando no tiene el dato completo, que es la mitad del diseño de una pantalla y la que se olvida. Una pantalla que muestra vacío sin decir por qué hace creer que el dato no existe. Cada fila es una situación real, no un error de programa.

| Situación | Qué se ve |
|---|---|
| «Todavía no hay nada que mostrar» | «Se dice que no hay, no se muestra en blanco» |
| «El dato existe pero no se pudo leer» | «Se dice qué falló y qué sí se pudo mostrar» |
| «Lo que se buscó no coincide con nada» | «Se dice que no hay, sin sugerir nada inventado» |
| «El registro está incompleto» | «Se muestra, señalando qué le falta» |

## 6. Qué pide confirmación, y qué no

> Dice qué acciones de la pantalla piden algo antes de ejecutarse. Lo que se puede deshacer se hace y se registra; lo que no se puede deshacer se confirma antes, cada vez.

| Qué se hace desde la pantalla | Qué pide antes |
|---|---|
| «…» | «Nada · Confirmación · Aprobación registrada» |

## 7. Lo que la interfaz NO hace

> Es lo que alguien podría esperar hacer desde la interfaz y se dejó fuera a propósito. Si no hay nada, se escribe «Ninguno».

- **«Qué no se puede hacer desde acá».** «Y dónde se hace, si se puede hacer en otro lado.»
