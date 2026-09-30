# `recuperar.py`

Con cada mensaje del usuario, le entrega al agente las reglas de las tareas que el mensaje pide.

## Qué hace

**Las tareas salen solo de la palabra clave** de `01·C28`, y solo donde esa regla dice que va: abriendo el mensaje o una de sus frases. Las demás palabras no cuentan. Hasta la fase `C` de `EP-005·HU-023` contaba cualquier palabra, y «reglas» en una pregunta traía las reglas de cambiar el estándar.

| Mensaje | Tareas |
|---|---|
| «Suba» | `tocar-git` |
| «Escriba el plan del estándar» | `escribir-documento` |
| «Apruebo los dos planes. Hágalo» | `trabajar-cadena` |
| «como así que entendió que yo quería cambiar el estándar?» | Ninguna más que las de todo mensaje |

Siempre suma las de `recibir-pedido` y `responder`, porque todo mensaje es un pedido y lleva respuesta. Una regla que el mensaje cita por su identificador llega aunque su tarea no.

**Entrega completas las que caben** en el tope del enganche, en este orden: las citadas, las blindadas, las que rigen todo mensaje y después el orden de `base/`. Las que no caben salen nombradas, con el archivo de `reglas-por-tarea/` donde están completas. Las de un capítulo opcional que el proyecto dejó apagado no se entregan.

## De qué depende y quién lo usa

```
recuperar.py
   ├── mapa_tareas.py ··· palabras_clave(), siempre(), reglas_por_tarea(), cuerpo() y archivos_de()
   ├── metareglas.py ···· reglas()
   └── comun.py ········· RAIZ y leer
```

Lo usa `hook_reglas.py`, con `como_texto()`.

## Qué tiene adentro

| Función | Qué retorna |
|---|---|
| `palabras_de_inicio(mensaje)` | La primera palabra de cada frase |
| `tareas_del_mensaje(mensaje)` | `{tarea: palabras clave que la piden}` |
| `elegir(mensaje)` | Las que entran completas, las que no cupieron y las de todo mensaje |
| `como_texto(mensaje)` | El bloque que se le entrega al agente |
