# Recomendaciones del análisis

> Lo que conviene hacer en todo análisis, sacado de lo que funcionó y de lo que falló en los análisis anteriores. Se lee antes de empezar, y el análisis dice en su sección «Recomendaciones» cuáles consultó y cuáles aplican.

## Los dos niveles

| Nivel | Dónde vive | Quién lo usa |
|---|---|---|
| Cimiento | Este archivo | Todo proyecto que hereda Cimiento |
| Proyecto | `analisis/recomendaciones.md` del proyecto, con la misma forma y números `RP-«n»`; nace con la primera recomendación propia | Solo ese proyecto |

## Cómo se escribe una recomendación

| Columna | Qué lleva |
|---|---|
| Qué se hace | Una acción, en infinitivo |
| Por qué | Lo que pasa si no se hace |
| Sale de | El análisis y la lección de donde salió; sin origen no entra |

Dos recomendaciones no dicen lo mismo: si una lección nueva repite una que ya está, se suma su origen a la existente.

## Las recomendaciones de Cimiento

Arrancan con las 36 lecciones de los análisis 1 a 8 del pendiente 103, juntando las que dicen lo mismo.

| # | Qué se hace | Por qué | Sale de |
|---|---|---|---|
| R-1 | Considerar todos los casos en que puede pasar lo mismo, en cualquier proyecto y herramienta, y decir cuáles cubre cada propuesta | Una solución para un solo caso deja abiertos los demás, y el hallazgo vuelve por otro lado | Análisis 8, lecciones 1 y 2 |
| R-2 | Revisar lo que ya existe en el proyecto y buscar qué reglas citan la que se toca, antes de decidir | Los choques que no se buscan en el análisis salen al ejecutar | Análisis 1, lección 10; análisis 6, lecciones 1 y 3; análisis 1 del pendiente 141, lección 2 |
| R-3 | Aplicar el checklist de las reglas a toda regla que el análisis crea o cambia | Una regla que no pasa su checklist choca con otra cuando ya se está construyendo | Análisis 5, lección 1 |
| R-4 | Al exigir un campo o una sección nueva, revisar las plantillas que lo tienen que llevar y medir qué documentos ya cumplen | Los documentos hechos con la plantilla incumplen la regla desde que nacen | Análisis 7, lecciones 1 y 2 |
| R-5 | Revisar las cuatro partes de «Lo que aportó cada parte» contra cada punto de «Lo que se tiene que hacer» | Revisadas por encima, dejan pasar los hallazgos que salen al escribir los planes | Análisis 8, lección 4 |
| R-6 | Leer completos los análisis anteriores y sacar el trabajo de «Lo que se tiene que hacer», no de la conversación | Lo que se saca de la conversación inventa choques y abre análisis sin necesidad | Análisis 3, lecciones 1 y 2 |
| R-7 | Preguntar en el análisis lo que nadie pidió, en vez de agregarlo a la épica, la HU o el plan | Lo que entra sin origen es lo que produce los hallazgos al ejecutar | Análisis 1, lección 5; análisis 3, lección 3 |
| R-8 | Preguntar antes de actuar cuando un pedido admite dos lecturas, y no escribir archivos cuando la palabra solo autoriza analizar | El agente que interpreta solo arranca torcido y escribe lo que no se acordó | Análisis 1, lecciones 2, 3, 4 y 6 |
| R-9 | Escribir el hallazgo y el pendiente precisos, y cambiarlos en sus originales solo después de aprobar el análisis | Si se cambia la copia o se cambia antes de aprobar, la conversación deja de entenderse | Análisis 1, lecciones 1, 12 y 13 |
| R-10 | Explicar con un ejemplo sencillo o un dibujo lo que no se entiende, como para un niño | El texto técnico esconde malentendidos que el ejemplo destapa | Análisis 1, lecciones 7, 8 y 9; análisis 3, lección 4; análisis 6, lección 4; análisis 1 del pendiente 141, lección 1 |
| R-11 | Medir con las reglas del documento todo lo que entra a él, también lo copiado y lo escrito con guiones | Lo que entra por otro camino trae marcas que nadie revisó | Análisis 1, lección 11; análisis 2, lección 2 |
| R-12 | Construir lo del estándar para cualquier análisis de cualquier proyecto, y probarlo recorriendo un ejemplo en otro proyecto | Lo hecho para un solo caso hay que apagarlo a mano y falla en el siguiente | Análisis 2, lecciones 1 y 4 |
| R-13 | Enlazar el texto que ya está en la épica, en vez de copiarlo en cada HU | La misma frase en siete sitios envejece distinto en cada uno | Análisis 4, lección 1 |
| R-14 | Confirmar con el usuario cuál es el hallazgo que abre el análisis | Un análisis abierto con el hallazgo equivocado trata otro problema | Análisis 4, lección 2 |
| R-15 | Detener la ejecución en cuanto aparece un hallazgo, antes de tocar otro archivo | El hallazgo atendido a tiempo no deja trabajo a medias | Análisis 2, lección 3; análisis 5, lección 2; análisis 6, lección 2 |
| R-16 | Corregir dentro del piloto lo que falla de su propia herramienta | Lo que falla en el piloto vuelve a fallar en todos los análisis siguientes | Análisis 8, lección 3 |
| R-17 | Medir la respuesta contra `00·ID9` antes de entregarla | Medida después, el usuario tiene que pedir una y otra vez que se acorte | Análisis 8, lección 5 |
| R-18 | Escribir «Lo acordado» en el turno en que se acuerda: uno por tema, el más nuevo reemplaza al anterior, y solo con lo que el usuario respondió | Escrito al final, mezcla acuerdos viejos con nuevos y lecturas del agente, y el usuario tiene que pedir que se revise una y otra vez | Análisis 1 del pendiente 136, lección 1; análisis 1 del pendiente 141, lección 3 |
| R-19 | Antes de escribir el plan de una fase, buscar todo lo que el cambio va a pedir y ponerlo en el plan: las migraciones que pide el marco del proyecto (en Django, `manage.py makemigrations --dry-run`) y las piezas que las pruebas exigen a toda pantalla nueva (menú, tablas, ayuda, manual) | El archivo que el plan no declara detiene la fase y abre otro análisis | Análisis 2 del pendiente 141, lección 1; análisis 3 del pendiente 141, lección 1 |
