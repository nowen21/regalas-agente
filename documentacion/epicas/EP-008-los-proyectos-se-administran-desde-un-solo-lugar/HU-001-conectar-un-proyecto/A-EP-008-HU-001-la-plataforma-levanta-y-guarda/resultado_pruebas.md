# Resultado de Pruebas — Fase A-EP-008-HU-001: la plataforma levanta y guarda   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección "qué se probó" del `funcionalidad_implementada.md`. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar: se aprobó antes y así se queda.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-008-HU-001-la-plataforma-levanta-y-guarda` |
| **HU** | [HU-001 Conectar un proyecto](../HU-001-conectar-un-proyecto.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md), aprobado el 2026-08-25 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-25 |
| **Ejecutado por** | El agente, en la máquina del usuario |
| **Ambiente y versión** | Windows 11, Python 3.11.9, Django 5.2.11. Sobre la carpeta `plataforma/`, sin commit todavía |

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 6 | 6 | 6 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

**Una salvedad sobre CP-001.** El plan pedía desconectar la máquina de la red. Lo que se hizo fue tapar la salida a la red desde adentro: cualquier conexión que no fuera a la propia máquina revienta. Es lo mismo que la desconexión venía a buscar, y tiene una ventaja: queda como comprobación automática que se repite sola en cada corrida, en vez de depender de que alguien se acuerde de desconectar el cable. Se anota acá porque **no es exactamente lo que el plan decía**, y el plan no se toca después de aprobado.

---

## 2. Ejecución caso por caso

### CP-001 · Levanta sin red

**El problema que resuelve:** si algo de la plataforma sale a internet, deja de servir en el momento en que no hay conexión - y una herramienta de trabajo que se cae con la red no es una base sobre la que apoyarse.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Situarse en `plataforma/` y crear el índice con `python manage.py migrate` | Las migraciones aplican sin error | `Applying almacen.0001_initial... OK` |
| 2 | Levantarla con `python manage.py runserver 127.0.0.1:8731 --noreload` | Arranca y queda escuchando | Arrancó |
| 3 | Pedirle la página con `curl -s http://127.0.0.1:8731/` | Responde diciendo que está viva | `La plataforma está viva. / Carpeta de datos: C:\Ing. Jose\ia\agente\plataforma\datos / Archivos en el índice: 1` |
| 4 | Mirar el registro del servidor | La petición quedó en 200, sin errores de red | `"GET / HTTP/1.1" 200 110` |
| 5 | Correr la comprobación `SinRedTests`, que reemplaza la función de conectar de manera que cualquier dirección distinta de la propia máquina lance un error | La plataforma responde y guarda igual, sin intentar salir | `test_responde_y_guarda_con_la_red_tapada ... ok` |

**Cómo se verificó que la pareja cumple:** el paso que decide es el 5, no el 3. Que responda con red puesta no prueba nada: responde igual una aplicación que sí sale afuera. Con la salida tapada, en cambio, cualquier conexión hacia fuera habría reventado la comprobación, y no reventó. Los pasos 1 a 4 dejan escrito que además levanta de verdad como servidor, no solo dentro de las pruebas. La salvedad de la sección 1 aplica acá.

### CP-002 · Lo guardado sobrevive al reinicio

**El problema que resuelve:** si lo que se guarda vive solo en memoria, se pierde al cerrar - y entonces la plataforma no guarda, solo aparenta.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Arrancar un proceso que guarde `proyectos/prueba.md` con el texto `# Proyecto de mentira\nRuta: ninguna.\n`, y **terminarlo** | Devuelve la huella de lo guardado, y el proceso muere | `huella al guardar: 5fda5beb93c8591afb4f3d126dcedd20c576e0a24e2d9c715d5e43bb0b63b400` |
| 2 | Arrancar **otro** proceso, desde cero, y pedirle que lea `proyectos/prueba.md` | Devuelve el mismo texto | `lo leido: '# Proyecto de mentira\nRuta: ninguna.\n'` |
| 3 | Preguntarle a ese proceso nuevo cuántos archivos tiene el índice | Uno | `archivos en el indice: 1` |

**Cómo se verificó que la pareja cumple:** lo que decide es que el paso 2 corre en **otro proceso**. Leer en el mismo proceso que escribió no distingue entre disco y memoria: la memoria habría respondido igual. El proceso del paso 1 ya no existía cuando el del paso 2 leyó, así que lo leído salió del disco.

### CP-003 · El índice se reconstruye

**El problema que resuelve:** si al perder la base se pierde información, la base dejó de ser un índice y se volvió la fuente - que es justo lo que `DA-01` vino a impedir, y el error que tiene hoy la aplicación de `interfaz/`.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Con `proyectos/prueba.md` ya guardado, borrar el archivo del índice: `rm -f indice.sqlite3` | El archivo deja de existir | `el archivo del indice ya no esta` |
| 2 | Crear el índice vacío otra vez con `python manage.py migrate` | Aplica sin error, y queda sin filas | `Applying contenttypes.0002_remove_content_type_name... OK` |
| 3 | Correr `python manage.py reconstruir_indice` | Dice cuántos archivos leyó | `Índice rehecho: 1 archivo(s) leídos.` |
| 4 | Comparar la huella que quedó en el índice contra la huella del texto en disco | Coinciden | `huella tras rehacer: 5fda5beb93c8591afb4f3d126dcedd20c576e0a24e2d9c715d5e43bb0b63b400` · `coincide con el texto: True` |
| 5 | Correr la comprobación automática `test_borrar_el_indice_no_pierde_informacion`, que guarda dos archivos, borra todas las filas del índice y lo rehace | Vuelven los dos, y lo guardado se sigue leyendo | `ok` |

**Cómo se verificó que la pareja cumple:** el paso 4 es el que decide. Que el paso 3 diga "1 archivo" solo prueba que contó algo; comparar la huella prueba que lo que quedó indexado es **el mismo contenido**, no una fila vacía con el nombre correcto. El paso 1 borra el archivo entero del índice, no unas filas: si algún dato viviera solo ahí, no habría de dónde sacarlo.

### CP-004 · Lo guardado se lee sin la plataforma

**El problema que resuelve:** si la información queda en un formato que solo la herramienta entiende, uno queda amarrado a la herramienta - y el día que no levante, la información se fue con ella.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Abrir lo guardado con una orden cualquiera del sistema, sin la plataforma de por medio: `cat datos/proyectos/prueba.md` | Sale el texto, legible | `# Proyecto de mentira` / `Ruta: ninguna.` |
| 2 | Correr `test_lo_guardado_queda_como_texto_en_disco`, que guarda y después abre el archivo directamente en la ruta esperada | El contenido del archivo es idéntico a lo que se pidió guardar | `ok` |

**Cómo se verificó que la pareja cumple:** el paso 1 lo decide, porque `cat` no sabe nada de la plataforma. El paso 2 lo deja automático para que no se rompa en silencio más adelante.

### CP-005 · Alguien la levanta siguiendo solo el texto

**El problema que resuelve:** unos pasos escritos de memoria por quien ya tiene todo instalado sirven para quien ya tiene todo instalado, y para nadie más.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Copiar `plataforma/` a una carpeta vacía **sin** el ambiente, sin el índice y sin lo que el lenguaje deja al correr | Queda solo lo que un clon del repositorio tendría | Quedaron `config`, `nucleo`, `requirements`, `manage.py`, `README.md`, `.gitignore`, `.env.example`, `datos`, `static`, `templates` |
| 2 | Seguir el paso 1 del README: `python -m venv .venv` | Se crea el ambiente | `ambiente creado` |
| 3 | Seguir el paso 3 del README: `pip install -r requirements/local.txt` | Instala lo que necesita | `Django 5.2.17` |
| 4 | Seguir el paso 4 del README: `python manage.py migrate` | Crea el índice vacío | `Applying contenttypes.0002_remove_content_type_name... OK` |
| 5 | Seguir el paso 5 del README: levantarla y pedirle la página | Dice que está viva | `La plataforma está viva. / Archivos en el índice: 0` |
| 6 | Correr `python manage.py test nucleo` en esa carpeta limpia | Las diez comprobaciones pasan | `Found 10 test(s). / OK` |

**Cómo se verificó que la pareja cumple:** lo que decide es el paso 1: la carpeta va **sin ambiente y sin índice**, así que nada de lo que ya estaba instalado en la máquina de trabajo pudo ayudar. Levantó al primer intento, sin agregar ningún paso que no estuviera escrito. Que la versión instalada allá fuera 5.2.17 y acá 5.2.11 no es un desvío: el archivo de requisitos pide un rango, y esa es la prueba de que el rango sirve.

### CP-006 · Que NO pase: que toque algo de afuera

**El problema que resuelve:** una plataforma que administra proyectos ajenos y escribe donde no debe hace daño en carpetas que no son suyas, y nadie se entera hasta que ya pasó.

**Cómo se hizo la prueba, paso a paso:**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr `test_no_se_escribe_fuera_de_la_carpeta`, que pide guardar en `../afuera.md` | Rechaza con `RutaFueraDeLaPlataforma`, y el archivo no aparece | `ok` |
| 2 | Correr `test_no_se_lee_fuera_de_la_carpeta`, que pide leer `../../algo.md` | Rechaza igual | `ok` |
| 3 | Después de todo lo corrido, mirar qué cambió en el repositorio con `git status --porcelain`, descontando la carpeta nueva | Solo aparecen archivos de la documentación de esta fase | Cinco documentos de épicas e historias, el histórico de la sesión, y la carpeta de la fase |
| 4 | Mirar si cambió algo de la aplicación vieja: `git status --porcelain interfaz/` | Sin salida | Sin salida. El último commit que tocó `interfaz/` sigue siendo `fb8beaa`, del 2026-08-22 |

**Cómo se verificó que la pareja cumple:** los pasos 1 y 2 prueban que el rechazo existe en el código; el 3 y el 4 prueban que en la corrida real no se escribió afuera. Hacen falta los cuatro: el rechazo podría existir y algún otro pedazo escribir afuera por su cuenta, y el `git status` limpio podría deberse a que nadie lo intentó. La comprobación del paso 1 además busca el archivo en el disco después del rechazo, porque lanzar el error y haber escrito igual es una falla que el error solo taparía.

**Tabla de casos ejecutados:**

| Caso | Qué exige | Prioridad | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | `RNF-03` | Crítica | 2026-08-25 | Se tapó la salida a la red y se pidió `GET /`: respondió 200 y guardó `uno.md` sin intentar ninguna conexión afuera | Aprobado | EV-01 | — |
| CP-002 | Sobrevivir al reinicio | Crítica | 2026-08-25 | Un proceso guardó `proyectos/prueba.md` y murió; otro proceso nuevo leyó el mismo texto | Aprobado | EV-02 | — |
| CP-003 | `RNF-04` | Crítica | 2026-08-25 | Se borró `indice.sqlite3` entero y se rehizo: volvió `proyectos/prueba.md` con la misma huella `5fda5beb…` | Aprobado | EV-02 | — |
| CP-004 | `DA-01` | Alta | 2026-08-25 | `cat datos/proyectos/prueba.md` mostró el texto sin la plataforma corriendo | Aprobado | EV-02 | — |
| CP-005 | Levantar desde cero | Alta | 2026-08-25 | En una carpeta sin ambiente ni índice, los cinco pasos del README levantaron la plataforma y pasaron las diez comprobaciones | Aprobado | EV-03 | — |
| CP-006 | No tocar nada ajeno | Crítica | 2026-08-25 | Guardar en `../afuera.md` fue rechazado y el archivo no quedó; `git status` de `interfaz/` salió sin una sola línea | Aprobado | EV-04 | — |

**Correspondencia con el plan:** 6 casos en el plan, 6 acá. Ninguno de más, ninguno de menos.

**Qué salió distinto de lo esperado:** nada falló. El único desvío es el de CP-001, explicado en la sección 1.

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que la plataforma levante como servidor, no solo dentro de las pruebas | Se levantó en el puerto 8731 y se pidió la página con `curl` | Respondió 200 |
| 2 | Que lo guardado se lea sin la plataforma | `cat` sobre el archivo | Se leyó completo |
| 3 | Que los pasos del README sirvan en limpio | Carpeta nueva, sin ambiente ni índice | Levantó al primer intento |
| 4 | Que los datos de mentira no quedaran | Se borraron y se rehizo el índice | `Índice rehecho: 0 archivo(s) leídos.` |

---

## 4. Defectos encontrados

Ninguno.

**Defectos abiertos que se aceptan y por qué:** ninguno.

---

## 5. Veredicto por exigencia

Esta fase **no cierra ningún criterio de aceptación de `HU-001`**: construye la base sobre la que la fase B los cumple, y así quedó escrito en el plan de trabajo. Lo que sí verificó:

| Exigencia | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| `RNF-03` la plataforma levanta sin red | CP-001 | Respondió y guardó con la salida a la red tapada | Sí |
| `RNF-04` perder la base no pierde información | CP-003 | El índice borrado entero se rehizo desde el texto, con la misma huella | Sí |
| `DA-01` la fuente es texto legible sin la plataforma | CP-004 | `cat` mostró el contenido | Sí |
| `DA-03` y `RNF-08` no hay servicio aparte que levantar | CP-005 | La carpeta limpia levantó con un archivo local, sin instalar ningún servicio | Sí |
| Lo guardado sobrevive al reinicio | CP-002 | Un proceso nuevo leyó lo que otro escribió | Sí |
| Nada de la fase toca un proyecto ajeno | CP-006 | Rechazo comprobado, y `interfaz/` sin una sola línea cambiada | Sí |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Los seis casos con veredicto escrito | Plan de pruebas §7 | 6 | 6 | Sí |
| Ningún caso en **No cumple** sin corregir | Plan de pruebas §7 | 0 | 0 | Sí |
| Un ciclo, y si algo falla se corre el ciclo completo | Plan de pruebas §3.5 | 1 | 1, sin fallas | Sí |

**Lo que no se cumplió:** nada quedó corto.

---

## 6. Veredicto de la fase

**Concepto:** **Cumple**.

**Justificación:** los seis casos del plan se ejecutaron y los seis pasaron, con la evidencia guardada. Las tres exigencias que le dieron origen a la fase quedaron probadas donde de verdad se prueban: la de reinicio, en otro proceso; la de reconstrucción, borrando el archivo del índice entero; y la de no tocar nada ajeno, mirando el repositorio después de la corrida. El único desvío frente al plan es la forma de CP-001, que se hizo más estricta y automática, y quedó anotado.

**Qué falta para que cumpla:** nada.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Salida de las diez comprobaciones automáticas, con versiones | [evidencias/EV-01-pruebas-automaticas.txt](evidencias/EV-01-pruebas-automaticas.txt) |
| EV-02 | Salida del reinicio y de la reconstrucción del índice | [evidencias/EV-02-reinicio-y-reconstruccion.txt](evidencias/EV-02-reinicio-y-reconstruccion.txt) |
| EV-03 | Salida de levantar en una carpeta limpia siguiendo el README | [evidencias/EV-03-carpeta-limpia.txt](evidencias/EV-03-carpeta-limpia.txt) |
| EV-04 | Estado del repositorio después de la corrida | [evidencias/EV-04-nada-ajeno-cambio.txt](evidencias/EV-04-nada-ajeno-cambio.txt) |

---

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-08-25 | 6 | 0 | Primera ejecución |
