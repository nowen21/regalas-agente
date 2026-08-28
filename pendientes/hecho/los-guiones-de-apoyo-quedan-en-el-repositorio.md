# Pendiente · Nada hace cumplir que los guiones de apoyo queden en el repositorio

**Estado:** cerrado el 2026-08-27, versión 35.4.0 · anotado el 2026-08-27.

> **Se construyó por la cadena** (`02·F23`): bajó a la [HU-018](../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-018-los-guiones-de-apoyo-quedan-en-el-repositorio/HU-018-los-guiones-de-apoyo-quedan-en-el-repositorio.md) y se construyó en su fase [`A-EP-005-HU-018-el-enganche-avisa-al-escribir-afuera`](../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-018-los-guiones-de-apoyo-quedan-en-el-repositorio/A-EP-005-HU-018-el-enganche-avisa-al-escribir-afuera/funcionalidad_implementada.md), con las salidas **1 y 3**. La **2** —un validador que compare al cierre— la dejó fuera el usuario: detecta lo que el enganche evita.

> **Queda un resto, y ahora se ve solo:** los guiones de sabotaje guardan su copia de restauración en la carpeta temporal del sistema. **El enganche nuevo lo va a avisar la próxima vez que corran**, que es exactamente para lo que se construyó.

| | |
|---|---|
| **Historia de usuario** | Por crear. Sale de este pendiente cuando se apruebe |
| **De dónde sale** | La señal `S-057`. El usuario preguntó por qué el agente seguía escribiendo en la carpeta temporal del sistema |
| **Proyecto de origen** | El estándar mismo |

## El problema

La regla existe y es del usuario: **los guiones de apoyo se escriben dentro del repositorio**, en `historico-chat/scripts/AAAA-MM-DD/`, y se quedan ahí versionados. La fijó el 2026-08-20 y la precisó el 2026-08-22, con estas palabras: *«nada se debe escribir por fuera, todo debe quedar en historico-chat»*.

**Se dejó de cumplir el 2026-08-24**, al día siguiente de precisarla.

| Día | Programas escritos afuera |
|---|---|
| 2026-08-24 | 1 |
| 2026-08-25 | 15 |
| 2026-08-26 | 14 |
| 2026-08-27 | 8 |

**Treinta y ocho**, más dos clones enteros de la plataforma con su entorno virtual — 6.831 archivos.

## Por qué pasa

**La regla vive en un recuerdo, y nada la hace cumplir.** Un recuerdo se consulta cuando uno se acuerda de consultarlo, que es justo cuando ya no hace falta.

Y hay algo peor que el olvido: **la herramienta ofrece una carpeta temporal en cada sesión y la nombra como el sitio recomendado**. El camino cómodo apunta al lado contrario de la regla. Ahí no gana la buena intención.

## Por qué importa

El daño no es de orden. El **resultado** de cada cambio quedaba versionado y **el cómo se borraba con el temporal**.

Cuatro días de sabotajes, guiones de cierre y mediciones sin respuesta a *«¿con qué se hizo esto?»*. Es la segunda vez que esa pregunta se queda sin respuesta: la primera fue la que originó la regla.

**Y es el argumento central de este estándar, aplicado a él mismo:** lo que depende de que el agente se acuerde se incumple sin que nadie se entere.

## Qué falta

Hay tres salidas, y conviene decidir cuál antes de construir:

1. **Un enganche que avise al escribir fuera del proyecto.** Es lo único que actúa en el momento del incumplimiento, no después.
2. **Un validador que compare** los guiones que la sesión corrió contra los que están en `historico-chat/scripts/`. Detecta al cierre, no evita.
3. **Que la regla suba de un recuerdo a `base/`**, donde ya vive `04·S9`, con su identificador y su comprobación. Hoy `04·S9` dice que no se toquen rutas fuera del proyecto; lo que falta es la mitad que dice **dónde sí van** los guiones.

**La 1 y la 3 no se estorban.** La 1 lo evita; la 3 lo deja escrito donde se carga solo al abrir sesión, en vez de en un archivo que hay que ir a leer.

### Y un caso que se descubrió al construir, y que cualquiera de las tres tiene que resolver

**Los guiones de sabotaje guardan su copia de restauración fuera del repositorio.** Todos: copian a la carpeta temporal del sistema el archivo que van a romper, para devolverlo intacto. **También es escribir por fuera**, y salió el 2026-08-27 saboteando la fase `C` de la `HU-021`.

Es pequeño y es legítimo —la copia tiene que estar en un sitio que el sabotaje no toque— pero **`historico-chat/scripts/` sirve igual**, y además deja constancia. Un enganche que avise al escribir afuera lo marcaría en cada corrida, así que conviene decidirlo junto con la salida que se elija.

## El límite

Este pendiente **no** cubre:

- **Los 38 guiones que estaban afuera.** Se trajeron el 2026-08-27, con la fecha real de cada uno y su README. Eso tapó los casos, no la causa.
- **Los dos clones de la plataforma.** No se traen: son 6.831 archivos con un entorno virtual, y lo que valía era el resultado del experimento, ya escrito en su fase.
- **Leer** lo que la herramienta guarda por fuera —su transcripción, lo que inyectó cada enganche—, que sí vale. Lo que no se hace es escribir allá.

## Cómo se sabrá que cerró

Que pase una jornada entera de trabajo y **los guiones de esa jornada estén en `historico-chat/scripts/` sin que nadie los haya movido después**, comprobable porque la carpeta del día tiene su README escrito el mismo día.
