# HU-009-las-rutas-largas-no-detienen-el-guardado

Contenido inmediato de esta carpeta.

| Qué | De qué se trata |
|---|---|
| [HU-009-las-rutas-largas-no-detienen-el-guardado.md](HU-009-las-rutas-largas-no-detienen-el-guardado.md) | La historia de usuario: que el instalador deje puesto el ajuste que permite guardar rutas de más de 260 caracteres, y que quien clone sepa qué hacer |

Todavía no tiene fases. Nace del hallazgo `H-28` y de la señal `S-042`: guardar 1005 archivos traídos se detuvo con `Filename too long`, porque 59 rutas pasaban de 260 caracteres.

**Lo que se midió antes de escribirla:** acortar nombres no alcanza. La ruta más larga de este repositorio mide 252 **en su propio sitio**, con 8 caracteres de holgura, y anidar necesita 55. Ninguna combinación de nombres los crea.

**Y lo que esta historia no puede prometer:** la configuración de git **no viaja al clonar**, comprobado sobre un repositorio de prueba. Ponerla al instalar sirve para la copia donde se instala, y para ninguna otra.
