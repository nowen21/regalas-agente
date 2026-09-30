import glob, io

p = glob.glob(r"C:\Ing. Jose\ia\agente\documentacion\epicas\EP-005-*\HU-023-*\HU-023-*.md")[0]
crudo = io.open(p, encoding="utf-8", newline="").read()
crlf = "\r\n" in crudo
s = crudo.replace("\r\n", "\n")


def c(viejo, nuevo):
    global s
    assert viejo in s, viejo[:60]
    s = s.replace(viejo, nuevo, 1)


c("| **Estado** | Terminada |", "| **Estado** | En curso: la fase `C` suma RN-07 a RN-09 y CA-08 a CA-10 |")

i = s.index("| RN-06 |")
j = s.index("\n", i)
s = s[:j] + """
| RN-07 | **Nada se elige adivinando.** Con cada mensaje, las tareas salen de la palabra clave de [`01·C28`](../../../../base/01-conducta.md#c28--sin-la-palabra-que-diga-qué-se-espera-el-agente-no-actúa), que es una lista cerrada, y no de las demás palabras del mensaje. Antes de cada acción del agente, las tareas salen de la acción misma: el comando que va a correr, el archivo que va a escribir o el servicio que va a consultar. Las dos correspondencias están escritas en `base/tareas.md`. **Reemplaza la elección por palabras del mensaje de RN-06**, que tomó «reglas» como pedido de cambiar el estándar |
| RN-08 | Las reglas de cada tarea se juntan, con su texto completo, en un archivo por tarea que escribe un programa, como el mapa. El agente lee ese archivo con la herramienta de lectura, así que le llega entero: el texto de un enganche se corta en 10.000 caracteres, y las reglas de una tarea suman de 9.946 a 217.871 |
| RN-09 | Antes de una acción, si el agente no leyó en esta sesión el archivo de alguna de sus tareas, el enganche detiene la acción y le dice qué archivo leer. Leído, la acción pasa. Cuando la conversación se resume, lo leído se olvida y se vuelve a pedir. Viene de lo decidido por el usuario el 2026-09-28: *«el agente debe saber las reglas en todo momento»* y *«nada de adivinar»* |""" + s[j:]

c("- El enganche que le muestra al agente la regla en el momento de actuar.\n", "")

c("### Criterios de aceptación transversales", """### CA-08 · La palabra clave dice las tareas del mensaje

```gherkin
Dado que el usuario escribe un mensaje
Cuando el recuperador elige las reglas
Entonces las tareas salen solo de la palabra clave del mensaje
Y un mensaje sin palabra clave trae solo las reglas que rigen todo mensaje
```

**Cómo validarlo:**

1. Pasarle «Suba». Resultado esperado: las tareas son `tocar-git`, `recibir-pedido` y `responder`.
2. Pasarle «es sencillo, debe entender las reglas». Resultado esperado: solo `recibir-pedido` y `responder`; ninguna de `cambiar-estandar`.
3. Pasarle «Escriba el plan del estándar». Resultado esperado: `escribir-documento`, sin `cambiar-estandar` ni `trabajar-cadena`.

Se aprueba cuando ninguna tarea sale de una palabra que no sea la clave.

### CA-09 · Antes de actuar, el agente tiene completas las reglas de esa acción

```gherkin
Dado que el agente va a correr un comando, escribir un archivo o consultar un servicio de afuera
Cuando no ha leído en esta sesión el archivo de reglas de esa tarea
Entonces la acción se detiene y el agente recibe el archivo que tiene que leer
Y después de leerlo la acción pasa
```

**Cómo validarlo:**

1. Simular un `git commit` sin haber leído el archivo de `tocar-git`. Resultado esperado: se detiene y nombra ese archivo.
2. Simular la lectura de ese archivo y repetir. Resultado esperado: pasa.
3. Simular `python -m unittest` sin haber leído el de `correr-comando`. Resultado esperado: se detiene; el archivo trae `02·F5` completa.
4. Simular que la conversación se resumió y repetir el paso 2. Resultado esperado: se vuelve a detener.

Se aprueba cuando ninguna acción de una tarea pasa sin que su archivo se haya leído en la sesión.

### CA-10 · Los archivos de reglas por tarea no envejecen

```gherkin
Dado que una regla cambia o cambia la línea de sus tareas
Cuando corre el validador de tareas
Entonces falla si algún archivo de reglas por tarea no coincide con lo que dicen las reglas
```

**Cómo validarlo:**

1. Escribir los archivos y correr `validar.py tareas`. Resultado esperado: sin fallas.
2. En una copia, cambiar una regla sin volver a escribirlos. Resultado esperado: falla nombrando el archivo viejo.

Se aprueba cuando el archivo de una tarea no puede quedar distinto de sus reglas.

### Criterios de aceptación transversales""")

i = s.index("| [`B-EP-005-HU-023-todas-las-reglas-declaran-sus-tareas`]")
j = s.index("\n", i)
s = s[:j] + "\n| [`C-EP-005-HU-023-las-reglas-llegan-antes-de-actuar`](C-EP-005-HU-023-las-reglas-llegan-antes-de-actuar/) | CA-08, CA-09, CA-10 | CA-07 | [plan_trabajo](C-EP-005-HU-023-las-reglas-llegan-antes-de-actuar/plan_trabajo.md) | [plan_pruebas](C-EP-005-HU-023-las-reglas-llegan-antes-de-actuar/plan_pruebas.md) | | Abierta 2026-09-28, planes por aprobar |" + s[j:]

s = s.rstrip("\n") + "\n| 2026-09-28 | El agente | Suma RN-07 a RN-09 y CA-08 a CA-10, y abre la fase `C`. El agente corrió las 568 pruebas de `pruebas.py` contra `02·F5`, que le había llegado solo por su nombre; y la elección por palabras tomó «reglas» como pedido de cambiar el estándar. El usuario decidió que las reglas se elijan sin adivinar y que el agente las tenga completas antes de actuar. Se reabre H-1 de la sesión, que es el mismo problema |\n"

if crlf:
    s = s.replace("\n", "\r\n")
io.open(p, "w", encoding="utf-8", newline="").write(s)
print("ok")
