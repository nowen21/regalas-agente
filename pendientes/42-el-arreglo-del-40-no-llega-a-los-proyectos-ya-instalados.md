# 42 · El arreglo del 40 no llega a los proyectos ya instalados

| | |
|---|---|
| **Quién lo reportó** | **`shopnest-mesa`** · `C:/DesarrollosClaude/personales/shopnest-mesa` |
| **Su pendiente de seguimiento** | `pendientes/01-los-enlaces-a-las-reglas-nacen-rotos.md`, que **sigue abierto** allá |
| **De dónde sale** | De comprobar el [40](40-el-instalador-copia-sin-rellenar-los-marcadores.md) apenas se cerró, en la v21.1.0 |
| **Qué le falta al 40** | Su punto 3 — «decir qué tiene que hacer un proyecto ya instalado para quedar al día, probablemente reinstalar». Reinstalar **no** basta |

## Qué se encontró

`shopnest-mesa` corrió el instalador con la v21.1.0 recién cerrado el 40. El instalador dijo:

```
· stack de instalación ya estaba al día
```

y no reescribió el archivo. El marcador sigue literal en `.agente/stack-instalacion.md`, línea 25:

```
([`02·F13`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F13-…md))
```

El arreglo del 40 alcanza a los proyectos que se instalen **desde ahora**. Los que ya estaban instalados se quedan con la copia mala, y **volver a instalar no los repara**.

## Por qué

Lo dejó dicho el propio 40: la huella se calcula del stack central, no del texto del archivo copiado. Eso es lo que permitió arreglar los puntos de copia sin romper la comparación — y es lo mismo que ahora impide que el arreglo baje. La plantilla no cambió de huella, así que para el instalador no hay nada que hacer, aunque el contenido del proyecto sí esté mal.

No hay salida por la línea de comandos: `instalar.py` solo acepta `--todos` y `--aplicar`. No existe una forma de forzar la reescritura.

## Qué habría que decidir

Son tres salidas y **elegir es de acá, no del proyecto**:

1. **Que la huella se calcule también del archivo copiado**, no solo del central. Repara solo y para siempre, y es el cambio más grande.
2. **Una bandera de reescritura** (`--forzar`) y una línea en el `CHANGELOG` diciendo que los proyectos ya instalados la necesitan una vez.
3. **Subir la huella de las plantillas afectadas** a mano en esta versión, para que el instalador las dé por viejas y las reescriba. Barato, y hay que acordarse cada vez que pase.

Sea cual sea, conviene que la prueba que nació con el 40 cubra también este caso: instalar, ensuciar la copia, reinstalar y comprobar que quedó limpia.

## Cómo se sabe que cerró

Un proyecto que ya estaba instalado antes de la 21.1.0 corre lo que la salida elegida diga, y el enlace de la línea 25 de su `.agente/stack-instalacion.md` abre la regla que cita.

**Al cerrar hay que avisarle a `shopnest-mesa`**, que es donde se comprobó.
