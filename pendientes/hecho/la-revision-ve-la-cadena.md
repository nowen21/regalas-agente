# Hecho · La revisión ve la cadena

Origen: pendiente 30, abierto el 2026-08-15 y cerrado el 2026-08-16, versión **23.0.0**.

| | |
|---|---|
| **Proyecto de origen** | **`shopnest-mesa`** · `C:/DesarrollosClaude/personales/shopnest-mesa` |
| **A quién avisar al cerrar** | a `shopnest-mesa`, que lo reportó |
| **Dónde se construyó** | Fase [`A-EP-007-HU-007-la-revision-ve-la-cadena`](../../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-007-revisar-que-falta/A-EP-007-HU-007-la-revision-ve-la-cadena/) |

## Qué pasaba

`02·F0` exige `planteamiento → épica → HU → especificación → plan → código` y dice que ningún eslabón se salta. La revisión de la instalación no miraba ninguno de los tres primeros: recorría los trece componentes del stack, y ahí el planteamiento **no era uno**.

Resultado: un proyecto podía tener código commiteado, `prompts/` sin un solo archivo, ninguna épica, ninguna historia, y el arranque diciendo **«13 de 13, instalación completa»**. Fue lo que pasó en `shopnest-mesa`: un esqueleto Django funcionando contra MySQL, construido y commiteado sin que existiera el planteamiento. **Lo notó el usuario preguntando, no el estándar.**

## Cómo cerró

La lista de componentes gana un punto —`cadena`— y la revisión pasa de 13 a 14. Un proyecto sin planteamiento dice ahora «13 de 14» y nombra qué le falta.

**Es el único punto que el instalador no instala**, y su columna lo dice con todas las letras. No es un descuido: el planteamiento lo escribe el agente con lo que el usuario quiere, y el instalador no pregunta. Copiar la plantilla con los marcadores sin llenar sería peor — parecería un planteamiento y la revisión lo daría por cumplido. **Lo que faltaba no era dejarlo puesto: era decir que falta.**

La épica se exige **solo si ya hay código** en `proyectos/`. Pedírsela a un proyecto recién instalado es ruido, y el ruido se deja de leer.

## Qué se supo al construirlo

**Esta casa reprueba su propio punto.** `prompts/` del estándar tiene 40 archivos y ninguno es un planteamiento. El «6 de 14» que sale acá hay que leerlo con cuidado —el estándar no se instala a sí mismo, así que ocho puntos no le aplican—, pero el de la cadena sí: el trabajo del estándar también es desarrollo. Escribir el planteamiento de este proyecto es decidir qué es este proyecto, y eso no es tarea de una fase de código.

**Una prueba anterior quedó desactualizada:** exigía que después de instalar no faltara nada, y ahora hay un punto que el instalador no puede poner. Se ajustó la afirmación, no la exigencia.

## Lo que no se hizo

- **Comprobar la cadena hacia abajo** —que cada historia tenga fase, que cada fase tenga plan—: eso ya lo mira `flujo.py`, y tenerlo en dos sitios es peor que en uno.
- **Detener el trabajo.** El aviso avisa; la `RN-06` de la historia lo prohíbe expresamente.

## Cómo se supo que cerró

Un proyecto de mentira con código y sin planteamiento se revisa y sale «3 de 14», con el punto nombrado y su arreglo escrito; se le escribe el planteamiento y el punto se apaga. Está automatizado en [`validadores/tests/test_checklist_cadena.py`](../../validadores/tests/test_checklist_cadena.py), y el caso se vio fallar a propósito quitando el punto de la lista.
