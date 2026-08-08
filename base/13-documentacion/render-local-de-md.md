# 13 · Render local de los `.md` — el anexo

> **Qué es.** El montaje que hace que un enlace de [`DOC14`](reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md) se abra formateado en el navegador, sin salir de la máquina.
>
> **No es norma.** Es una receta que el proyecto adopta si quiere. Estaba dentro de [`DOC14`](reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md) y la hacía reprobar dos filas del checklist: pedía una pieza de infraestructura —cumplible por separado del formato del enlace— y para explicarla nombraba herramientas concretas, que en `base/` no van ([`M3`](../20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md), [`M13`](../20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md)).
>
> **Qué gana el proyecto que lo monta.** El mismo enlace que ya exige [`DOC14`](reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md) deja de abrir texto crudo y abre el documento formateado. Sin el montaje, el enlace sigue siendo válido y sigue funcionando en el editor y en el visor del repositorio.

---

## La ruta que atrapa cualquier `.md`

En pseudocódigo, sin atarse a ningún stack:

```
RUTA  GET  /<camino>.md          # el comodín captura también las barras "/"
    si el entorno NO es local            → no encontrado
    candidatos = [ raíz_del_proyecto/<camino>.md,
                   raíz_del_proyecto/<prefijo_canónico>/<camino>.md ]
    archivo = el primer candidato que exista en disco
    si no existe ninguno                 → no encontrado
    devolver  render_markdown_a_html(archivo)
```

`<prefijo_canónico>` es la carpeta donde el proyecto guarda su documentación, declarada por su capa 3.

## Por qué el segundo candidato

Es la parte que se olvida, y sin ella el montaje falla justo donde más se usa.

Cuando el proyecto sirve un documento por una URL corta —sin la carpeta en la ruta—, los enlaces relativos que hay dentro se resuelven **contra la URL del navegador**, no contra la ubicación real del archivo. Un enlace correcto a nivel de disco termina en "no encontrado". Probar el segundo candidato, bajo el prefijo canónico, hace que resuelva igual por los dos caminos.

## Qué queda fuera

Servirlo fuera del entorno local. Estos documentos son de trabajo: exponerlos es publicar la documentación interna del proyecto sin haberlo decidido.
