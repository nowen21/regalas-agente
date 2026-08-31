# Pendiente · Veintiséis documentos traen un carácter de control invisible que rompe tablas

**Estado:** **hecho** el 2026-08-30, en la misma sesión que lo anotó.

| | |
|---|---|
| **Historia de usuario** | [EP-004 · HU-025](../documentacion/epicas/EP-004-comprobacion-automatica/HU-025-los-caracteres-de-control-invisibles-se-cuentan/HU-025-los-caracteres-de-control-invisibles-se-cuentan.md), aprobada el 2026-08-30 |
| **De dónde sale** | El hallazgo `H-5` de la sesión [2026-08-28 · plantilla-manual-instalacion](../historico-chat/resumenes/2026-08-28/plantilla-manual-instalacion.md) |
| **Proyecto de origen** | El estándar mismo |

## El problema

Al ir a agregarle una fila a la tabla de fases de una historia, la fila que ya estaba no empezaba con la barra de la tabla sino con un `U+0001`. Esa fila **no se renderiza como fila**: en cualquier visor de markdown desaparece del cuadro y queda como un párrafo suelto debajo.

Buscándolo aparece en **26 archivos `.md`**, trece de ellos en `documentacion/`. Se encuentran con:

```
grep -rlP "\x01" --include=*.md .
```

El primero que se vio es [`HU-003-version-adoptada-por-el-proyecto.md`](../documentacion/epicas/EP-002-versionado-y-adopcion/HU-003-version-adoptada-por-el-proyecto/HU-003-version-adoptada-por-el-proyecto.md), en la fila de su fase `A`.

**No lo cuenta nadie.** La sección 3 del anexo [`marcadores-de-ia.md`](../base/00-identidad-y-rol/marcadores-de-ia.md) lista siete caracteres invisibles (espacio duro, ancho cero, guion suave y compañía), y [`validadores/marcas.py`](../validadores/marcas.py) los cuenta y los limpia. `U+0001` no está en esa lista, ni ningún otro carácter de control.

## Por qué importa

No bloquea ninguna corrida y por eso lleva meses ahí. Lo que hace es más lento: **una historia muestra una fase menos de las que tiene**, y quien la lea en un visor va a creer que ese trabajo no existe. Es exactamente la clase de dato falso que este repositorio persigue en todas partes, escondido donde nadie mira porque no se ve.

Y sobrevive a cualquier reescritura del contenido: se copia y se pega con el texto.

## Qué falta

1. **Ampliar la lista de invisibles de `marcas.py`** para que cuente los caracteres de control. Hay dos formas: agregar los que aparecieron, o barrer el rango `U+0000` a `U+001F` completo salvo el salto de línea y el tabulador. La segunda cuesta lo mismo y no deja que el próximo se cuele; la primera deja el trabajo a medias por definición.
2. **Limpiar los 26 archivos**, en su propio commit y sin mezclarlo con otro trabajo.
3. **Agregar la fila al anexo** de marcadores, en la sección 3, para que la lista y el programa digan lo mismo.

## El límite

Esto **no** cubre los caracteres invisibles que sí son legítimos, como el tabulador dentro de un bloque de código. Y no cubre el problema de dónde salen: nadie sabe todavía qué los metió, y averiguarlo no es condición para limpiarlos.

## Cómo se sabrá que cerró

```
grep -rlP "\x01" --include=*.md .
```

Sin resultados, y `python validadores/validar.py marcas` reportando el carácter de control si alguien vuelve a meter uno.
