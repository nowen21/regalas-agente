Analiza todas las reglas que se encuentran actualmente en la carpeta `prompts`, **exceptuando `sin-marcadores-de-ia`**, ya que esta regla ya cuenta con su correspondiente regla creada.

Para cada una de las demás reglas, determina qué se debe hacer con ella y clasifícala en una de las siguientes opciones:

1. **Crear como una nueva regla** del agente.
2. **Complementar una regla existente**, cuando su contenido amplíe, precise o fortalezca una regla que ya existe. En este **caso, debe identificarse explícitamente cuál es la regla que se debe complementar, indicando su nombre**, ubicación y la razón por la cual el contenido analizado debe incorporarse en ella.
3. **Complementar varias reglas existentes**, cuando su contenido amplíe, precise o fortalezca el contenido de **dos o más reglas ya existentes**. En este caso, **deben identificarse explícitamente todas las reglas que se deben complementar**, indicando para cada una su nombre, ubicación y la razón por la cual el contenido analizado debe incorporarse en ella..
4. **Crear como regla hija de una regla existente**, cuando su contenido corresponda a una especialización, ampliación o desarrollo específico de una regla existente. En este caso, **debe identificarse explícitamente la regla padre**, indicando su nombre, ubicación y la razón por la cual la nueva regla debe depender de ella. También debe explicarse qué relación jerárquica existe entre ambas reglas.
5. **Crear como regla hija de varias reglas**, cuando su contenido dependa, se derive o requiera el cumplimiento de **dos o más reglas existentes**. En este caso, **deben identificarse explícitamente todas las reglas padre**, indicando para cada una su nombre, ubicación y la razón por la cual la nueva regla debe depender de ella. Además, debe explicarse cómo se relacionan entre sí las reglas padre y por qué, en conjunto, justifican la creación de la nueva regla hija..
6. **No convertirla en regla**, cuando su contenido no tenga las características necesarias para constituir una regla del agente.

Para realizar el análisis, primero revisa las reglas existentes del agente y determina las relaciones, dependencias, duplicidades y posibles complementariedades antes de tomar una decisión.

No crees ni modifiques las reglas todavía. **En esta etapa únicamente debes analizar y determinar qué se debería hacer con cada elemento encontrado en `prompts`.**

Crea el archivo:

`prompts/analisis/analisis-reglas.md`

En este archivo documenta el análisis de **cada elemento de `prompts`**, indicando como mínimo:

* Nombre del elemento analizado.
* Qué establece o cuál es su propósito.
* Si realmente debe convertirse en una regla.
* Regla existente relacionada, si aplica.
* Acción recomendada: nueva, complementar, complementar varias, hija, hija de varias o no convertir en regla.
* Justificación de la decisión.
* Si debe convertirse en regla, indicar brevemente dónde debería ubicarse y qué relación debería tener con las demás reglas.

El objetivo es obtener un **mapa claro de qué hacer con cada elemento existente en `prompts` antes de crear o modificar cualquier regla del agente**.
