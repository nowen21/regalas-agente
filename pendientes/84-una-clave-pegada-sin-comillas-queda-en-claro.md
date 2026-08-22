# Pendiente · Una clave pegada sin comillas queda escrita en claro en la transcripción

**Estado:** abierto, anotado el 2026-08-22.

| | |
|---|---|
| **Historia de usuario** | [EP-005 · HU-002 — Enmascarar claves](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-002-enmascarar-claves/HU-002-enmascarar-claves.md) |
| **De dónde sale** | Ejecutar la fase [`A-EP-001-HU-003`](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-003-nucleo-que-no-se-sobrescribe/A-EP-001-HU-003-retrodocumentar-el-nucleo-blindado/resultado_pruebas.md), defectos D-01 y D-02. Su CA-02 quedó en rojo por esto |
| **Proyecto de origen** | El estándar mismo |

## El problema

El enmascarador existe, el histórico lo usa antes de escribir, y funciona. **Para algunas formas de clave.** Probado el 2026-08-22:

| Lo que se pega en el chat | Se enmascara |
|---|---|
| `AKIA1234567890ABCDEF` | sí |
| `ghp_abcdefghijklmnopqrstuvwxyz12` | sí |
| `API_KEY="supersecreto123456"` | sí |
| `API_KEY=supersecreto123456` | **no** |
| `password: MiClave123456` | **no** |
| `la clave del servidor es Patito2026Segura` | **no** |

**El motivo es un préstamo que no se revisó.** `enmascarar.py` reusa `secretos._ASIGNA`, y ese patrón se escribió para buscar secretos **en código fuente**, donde el valor va entre comillas:

```
(?P<clave>pass(?:word|wd)?|secret|api[_-]?key|…)\s*[:=]>?\s*(?P<comilla>['"])(?P<valor>[^'"]{6,})(?P=comilla)
```

En un chat nadie escribe comillas. **Las tres formas que fallan son las tres que una persona teclea de verdad.**

## Por qué importa

Es núcleo blindado: [`00·N6`](../base/00-nucleo-blindado.md) dice que una credencial no se escribe, no se registra y no se guarda. La transcripción **se versiona**, así que una clave que se cuela ahí queda en el historial del repositorio, y de ahí no se saca reescribiendo el archivo.

Y el enmascarador da la sensación contraria: existe, corre y tapa lo que reconoce. Quien vio funcionar el caso de `AKIA…` da por hecho que cubre lo demás.

**Reusar el patrón fue lo correcto** —no inventar una lista nueva es lo que dice el propio módulo— pero **buscar secretos en código y taparlos en una conversación son dos problemas distintos con la misma cara**, y eso no se notó al reusarlo.

## Qué falta

Que el enmascarador reconozca las formas de una conversación, además de las de un archivo:

1. **La asignación sin comillas:** `API_KEY=valor`, `password: valor`. La palabra clave ya está en la lista; lo que sobra es exigir las comillas.
2. **La clave dicha en prosa:** «la clave es X», «el token es X». Más difícil, y es donde hay que tener cuidado.

**El riesgo de esto es taparlo todo**, y hay que decirlo antes de empezar: un patrón muy ancho convierte la transcripción en un texto lleno de huecos, y ahí el histórico deja de servir para lo que sirve. Conviene empezar por el punto 1, que es acotado y cubre el caso más común, y medir cuántas líneas del histórico existente cambiarían antes de tocar el punto 2.

## El límite

No cubre las claves que ya estén escritas en el histórico. Para eso está la decisión 30 del [pendiente 59](hecho/las-42-dudas-que-detenian-26-fases.md): la vieja se enmascara igual y queda dicho en el archivo que se hizo, sin borrar el bloque.

No toca `secretos.py`, que para su trabajo —código fuente— está bien como está. Lo que hay que separar es el uso, no el módulo.

## Cómo se sabrá que cerró

Las seis formas de la tabla de arriba se enmascaran, y una prueba nueva las cubre una por una. Y se corre sobre el histórico existente contando cuántas líneas cambiarían: si son muchas, el patrón se está pasando de ancho y hay que acotarlo antes de dejarlo.
