# Las palabras con que se le pide algo al agente

> Anexo del capítulo [`01 · Conducta del agente`](../01-conducta.md). **No es una regla**: no lleva molde de regla ni identificador propio. Es la lista que [`01·C28`](../01-conducta.md#c28--sin-la-palabra-que-diga-qué-se-espera-el-agente-no-actúa) exige, y nada más.

## Por qué existe

El agente decide por su cuenta qué clase de pedido recibió, y se equivoca hacia el lado caro: entiende una pregunta como una orden y cambia el proyecto. [`00·N1`](../00-nucleo-blindado.md#n1--ningún-cambio-de-estado-sin-aprobación-explícita-blindada) ya pide aprobación para cambiar el estado, y aun así pasa, porque el agente lee la pregunta **como si fuera** esa aprobación.

La salida no es una segunda aprobación: es que el pedido diga qué se espera antes de que haya nada que interpretar.

## Las palabras

**Ninguna de estas toca nada.**

| Palabra | Qué autoriza |
|---|---|
| **Pregunta** | Responder lo que se pregunta |
| **Explique** | Desarrollar algo que ya existe, para entenderlo |
| **Analicemos** | Estudiar y dar una lectura |
| **Revise** | Mirar y reportar lo que se encuentre, sin corregirlo |
| **Proponga** | Dar opciones con su costo, sin elegir |
| **Busque** | Encontrar algo y decir dónde está |
| **Compare** | Poner dos cosas lado a lado |
| **Verifique** | Correr las comprobaciones y reportar el resultado |

**Estas cambian el proyecto.**

| Palabra | Qué autoriza |
|---|---|
| **Hágalo**, aplique | Ejecutar lo pedido, y nada más |
| **Corrija** | Arreglar lo que se le señala |
| **Escriba**, redacte | Producir un documento nuevo |
| **Suba** | Guardar y publicar en el control de versiones |
| **Recuerde** | Escribir el recuerdo en la memoria del proyecto |
| **Registre** | Escribir la señal o el pendiente |
| **Revierta** | Deshacer lo último |

**Estas mandan sobre el trabajo mismo.**

| Palabra | Qué autoriza |
|---|---|
| **Apruebo** | Firmar lo que estaba en borrador |
| **Continúe** | Seguir con lo que se estaba haciendo |
| **Pare** | Detenerse donde va |

## Cómo se usa

Va al empezar el pedido, y alcanza para todo ese pedido. No hay que repetirla en cada frase.

## Lo que la lista no admite

**Una palabra parecida no cuenta.** «Arregle» se parece a «corrija» y no está: el agente pide la palabra en vez de suponer cuál quiso decir. Aceptar parecidos devuelve el problema que la lista vino a quitar.

**La palabra fija el máximo, no el mínimo.** Con `revise` se reporta y no se corrige, aunque el arreglo sea de un renglón y el agente lo vea claro.

**No hay palabra que autorice actuar por adelantado.** Si el agente propone algo y quiere hacerlo, espera un pedido nuevo con su palabra.

## Qué pasa si el pedido no trae ninguna

El agente responde diciendo que falta, y trae la lista. No rechaza el pedido ni lo interpreta a medias: lo deja quieto hasta que se le diga qué se espera.
