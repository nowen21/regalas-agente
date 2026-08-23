# Pendiente · El aviso de quedarse atrás existe, y no llega a donde tiene que llegar

**Estado:** cerrado el 2026-08-22, en la fase [`B-EP-002-HU-004-el-aviso-llega-al-abrir-y-dice-que-cambio`](../../documentacion/epicas/EP-002-versionado-y-adopcion/HU-004-aviso-al-quedar-atras/B-EP-002-HU-004-el-aviso-llega-al-abrir-y-dice-que-cambio/funcionalidad_implementada.md) · anotado ese mismo día.

| | |
|---|---|
| **Historia de usuario** | [EP-002 · HU-004 — Aviso al quedar atrás](../../documentacion/epicas/EP-002-versionado-y-adopcion/HU-004-aviso-al-quedar-atras/HU-004-aviso-al-quedar-atras.md), cuyo CA-01 quedó en rojo por esto |
| **De dónde sale** | Ejecutar la fase [`A-EP-002-HU-004`](../../documentacion/epicas/EP-002-versionado-y-adopcion/HU-004-aviso-al-quedar-atras/A-EP-002-HU-004-retrodocumentar-el-aviso-de-desfase/resultado_pruebas.md), defectos D-01 y D-02 |
| **Proyecto de origen** | El estándar mismo |

## El problema

El aviso está construido y dice lo correcto:

```
[AVISO] CLAUDE.md — el proyecto declara v27.2.0, el estándar va en v32.0.1:
        subir es decisión del usuario; las fases cerradas quedan selladas
```

**Pero hay que pedirlo a mano.** El enganche de apertura es `hook_sesion.py`, y lo que hace es llamar a `sesion.revisar()` y a `cargador.contexto()`. Ninguno de los dos mira la versión, y tampoco `cargador.py`. Corrido `sesion.revisar()` sobre un proyecto atrasado dos versiones mayores, devuelve un solo hallazgo, y es otro.

O sea: **el aviso al quedar atrás no avisa**, salvo que alguien escriba el comando.

Y hay un segundo hueco, este ya previsto: el mensaje nombra las dos versiones y **no dice qué cambió entre ellas**. La decisión 24 del [pendiente 59](las-42-dudas-que-detenian-26-fases.md) ya fijó qué debería decir —la versión, su tipo y su título, al nivel de entrada del registro— y sigue sin implementarse.

## Por qué importa

Es la funcionalidad central de su historia, y lleva sin conectarse desde que se escribió.

**Y explica por qué nadie lo notó:** el aviso se ve todos los días **en el repositorio del estándar**, donde el agente corre las comprobaciones a mano. En un proyecto instalado, que es donde tiene que llegar, no aparece nunca. Una funcionalidad que se ve funcionar en el único sitio donde no hace falta es la más fácil de dar por hecha.

El daño es lento: un proyecto se queda atrás y nadie se entera hasta que algo se rompe por una regla que cambió hace tres versiones.

## Qué falta

**Primero, que llegue.** Que el arranque incluya el aviso junto con lo que ya entrega. `sesion.revisar()` es el sitio: ya devuelve hallazgos que el enganche imprime, y agregar el de la versión no cambia el contrato de nadie.

**Después, que diga qué cambió.** Entre la versión declarada y la vigente hay un tramo del registro de cambios; el mensaje debería nombrarlo al nivel que fijó la decisión 24: la versión, su tipo y su título. Ni menos, porque «estás atrasado» no ayuda a decidir; ni más, porque obligaría a mantener dos textos que dicen lo mismo.

**Y hay un orden entre los dos, con un motivo:** conectar el aviso sin que diga qué cambió ya sirve; decir qué cambió en un aviso que nadie recibe, no.

## El límite

No migra nada ni detiene nada. Eso el CA-03 de la historia ya lo comprueba y quedó cumplido: el aviso es aviso, sale con código 0 y no toca un archivo.

No cubre el caso de la derogación sin adoptar, que **sí** detiene la fase por [`02·F22`](../../base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md). Ese es otro camino y ya está escrito.

No arregla que la versión declarada pueda ser falsa: eso es el [pendiente 82](la-version-adoptada-no-se-comprueba-contra-nada.md), y conviene hacerlo antes, porque un aviso que se calcula sobre un número inventado llega igual de mal.

## Cómo se sabrá que cerró

Se abre una sesión en un proyecto atrasado y el aviso aparece **sin pedirlo**, nombrando las dos versiones y el tramo que las separa. Se abre en uno al día y no aparece nada. Y una prueba nueva comprueba las dos cosas sin depender de que alguien mire la pantalla.

---

## Cómo se cerró — 2026-08-22

**Primero llegar, después decir qué cambió**, que es el orden que este pendiente pedía y por el motivo que daba.

El arranque de sesión ya pregunta por la versión: sobre un proyecto atrasado pasó de **un** hallazgo a **tres**. Y el aviso trae el tramo, con lo que obliga a migrar adelante: sobre shopnest-mesa, **40 versiones, 5 de ellas MAYOR**.
