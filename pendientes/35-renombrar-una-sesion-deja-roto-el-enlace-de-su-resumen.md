# Pendiente · Renombrar una sesión deja roto el enlace de su propio resumen

**Estado:** abierto · anotado 2026-08-16.

| | |
|---|---|
| **Proyecto de origen** | **`shopnest-mesa`** · `C:/DesarrollosClaude/personales/shopnest-mesa` |
| **Su pendiente de seguimiento** | `pendientes/03-el-renombrado-deja-roto-el-enlace-del-resumen.md` — queda **abierto allá** hasta que este se corrija |
| **A quién avisar al cerrar** | a `shopnest-mesa`, para que cierre el suyo |

El proyecto no tocó nada del estándar: corrigió el enlace en su propio archivo y reportó acá.

## El problema

[`historico.py --renombrar`](../validadores/historico.py) hace cuatro cosas bien: mueve la transcripción, le cambia el título, corrige su línea en el índice y **arrastra el resumen** a su nuevo nombre.

Lo que no hace: dentro del resumen, la primera línea nombra la transcripción con un enlace, y ese enlace se queda apuntando al nombre viejo.

```
Hallazgos de la sesión transcrita en [historico-chat/2026-08-16-sesion.md](../../2026-08-16-sesion.md).
                                                        ^^^^^^^^^^^^^^^^^^^^^ ya no existe
```

## Cómo se reprodujo

En `shopnest-mesa`, el 2026-08-16:

```
python validadores/historico.py --renombrar ".../historico-chat/2026-08-16-sesion.md" --tema "..." --resumen "..."
→ Sesión guardada como 2026-08-16-el-defecto-de-cimiento-se-reporta-no-se-arregla.md; índice al día.
```

El validador de enlaces, que antes daba cero, quedó con uno:

```
[FALLA] historico-chat/resumenes/2026-08-16/el-defecto-de-cimiento-se-reporta-no-se-arregla.md:3
        enlace roto: ../../2026-08-16-sesion.md
```

## Por qué importa

Es el propio estándar el que pide ponerle nombre a la sesión —el enganche lo reclama en el primer mensaje— y el comando que ofrece para hacerlo deja el repositorio peor de como estaba. El resumen es la puerta de entrada a lo que dejó una sesión; si su enlace a la transcripción no abre, hay que buscarla a mano.

## Qué falta

Que `--renombrar` reescriba también el enlace dentro del resumen que arrastra. Es el mismo nombre nuevo que ya calculó para mover el archivo.

Conviene mirarlo junto con el [pendiente 33 · punto 4](33-defectos-que-destaparon-los-resumenes-viejos.md), que es el mismo agujero visto desde fuera: renombrar no toca a quien citaba la sesión desde otro archivo. Este es el caso de adentro, y es el más barato — el resumen es un archivo conocido y de nombre fijo.

## Cómo se sabe que cerró

Se renombra una sesión que ya tenga resumen y el validador de enlaces sigue en cero, sin arreglar nada a mano.
