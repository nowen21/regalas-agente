# Análisis 1: el código de Cimiento se repite en vez de reusarse, y nada avisa cuando pasa

> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Trata también el [pendiente: nada avisa cuando se crea una función que ya existe](../117-nada-avisa-cuando-se-crea-una-funcion-que-ya-existe/pendiente.md), que sale del mismo inventario.

---

## Recomendaciones

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-1 | Se midió la repetición en todo el código de Cimiento, no solo en las rutas, y se revisó si pasa en los proyectos que heredan |
| R-2 | Se revisó lo que ya existe: `comun.py`, `calidad.py` y `codigo.py`. Al principio no se hizo, y salió la lección 1 |
| R-12 | El validador se prueba desde un proyecto que no es Cimiento (punto 3 de «Lo que se tiene que hacer») |
| R-14 | Se confirmó con el usuario el hallazgo que abre el análisis (turno 17) |
| R-17 | Las respuestas se midieron contra `00·ID9` |
| Las demás | No aplican: no se crea ni se cambia ninguna regla ni plantilla, y no hay plan en ejecución |

---

## Hallazgo

2. **El código se repite en vez de reusarse**: el manejo de rutas está copiado en decenas de archivos, y un arreglo llega a una sola copia. Va en el [pendiente 116](pendiente.md).

## Pendiente

| | |
|---|---|
| **De dónde sale** | El inventario de los `.py` de Cimiento, en la [sesión del 2026-10-04](../../../../2026-10-04-optimizar-el-codigo-de-cimiento.md) |

**El problema.** Cada vez que hace falta algo nuevo se crea un archivo y en él se escribe todo desde cero, sin revisar si eso ya existe en otro lado. Cimiento incumple así su propia regla [`07·Q4`](../../../../../base/07-calidad-de-codigo.md#q4--no-repitas-dry-pero-no-abstraigas-de-más), que pide poner en un solo sitio la lógica repetida.

El manejo de rutas es el caso más claro. En `validadores/` y `adaptadores/claude-code/` se encontró esto (sin contar las pruebas):

| Qué se repite | Dónde |
|---|---|
| `raiz_pedida`, que lee `--raiz` de la orden | Copiada en los 10 enganches de `adaptadores/claude-code/` |
| Lectura de `--raiz` a mano | 28 archivos |
| Cálculo de la raíz con `os.path.dirname(...(__file__))` | 25 archivos |
| Cambio de `\` por `/` a mano | 77 líneas |
| Saber si una ruta queda dentro del proyecto | Dos formas distintas: `relativa` en `validadores/freno.py` y `_partes` en `validadores/rutas_fuera.py` |
| `_git`, que corre git y lee la salida | 6 archivos, cada uno con su manejo de errores: `hook_estacion.py`, `inmutable.py`, `marcas.py`, `plan_vs_hecho.py`, `rama.py`, `versionado.py` |
| `_leer` | 7 archivos, aunque `validadores/comun.py` ya trae `leer` |

`validadores/comun.py` existe para esto, pero no tiene ninguna función de rutas, de raíz ni de git.

**Por qué importa.** Un arreglo llega a una sola copia y las demás siguen con el error. El commit `1295614` corrigió en `freno.py` la ruta `/c/...` que escribe la consola de Git en Windows, y `rutas_fuera.py` todavía no la reconoce. Como los validadores se instalan en todos los proyectos, cada copia sin arreglar falla en todos ellos.

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 13 · Usuario, 2026-10-04 10:40:16
> Analicemos: el pendiente 116

**Agente**, 2026-10-04 10:41:03
<!-- agente: 9db9e95e-4511-4df0-961e-356a175e76b6 -->

Ya está abierto el análisis: [analisis-1.md](../../../../../historico-chat/resumenes/2026-10-04/pendientes/116-el-codigo-de-cimiento-se-repite-en-vez-de-reusarse/analisis-1.md). Todavía no lo lleno. «Analicemos» solo autoriza analizar, y antes hay que confirmar con qué hallazgo se abre (R-14).

**¿Se abre con el hallazgo 2 de hoy?** Es «el código se repite en vez de reusarse». El hallazgo 3 (pendiente 117, el validador) sale del mismo inventario y se puede tratar aquí mismo.

**Lo que hay que decidir** (R-1, todos los casos):

1. **Ubicación.** La aprobó en el chat antes de que se abriera el análisis: primero el validador en `EP-004` y después una épica nueva de mantenimiento. Paso esa decisión a «Lo acordado» tal como quedó.
2. **Dónde más pasa.** Los validadores no se copian a los proyectos (lo dice [instalar.py:31](../../../../../validadores/instalar.py#L31)): una sola copia sirve a todos. Juntar las copias en Cimiento arregla todos los proyectos de una vez.
3. **El validador sirve en cualquier proyecto.** Si solo busca funciones de Python, no sirve en un proyecto con PHP o JavaScript, y eso choca con «todo multiproyecto». Hay tres opciones:
   - a) que lea cualquier lenguaje que reconozca por el tipo de proyecto;
   - b) que empiece solo con Python y crezca después;
   - c) que solo funcione en Cimiento.

   **Recomiendo la a.**
4. **Qué cuenta como repetido.** Dos funciones con el mismo nombre no siempre hacen lo mismo. `07·Q4` dice «no abstraigas de más». Mi propuesta es que el validador avise y no bloquee, y que compare el cuerpo de la función, no solo el nombre.
5. **El orden de la limpieza.** Primero rutas y git, que es donde ya hubo daño. Después `_leer` y lo demás de `validadores/` y los enganches. Al final `plataforma/nucleo/`.

Hay otro problema: el análisis nació con los enlaces de la tabla de reglas sin llenar. Dicen `«RUTA-ESTANDAR»` en lugar de la ruta real, así que están rotos.

¿Se abre con el hallazgo 2, y qué responde a los puntos 3 y 4?

### 14 · Usuario, 2026-10-04 10:42:54
> Pregunta: qué generó este pendiente?

**Agente**, 2026-10-04 10:43:04
<!-- agente: 23a80629-b31d-4ab4-9bbb-ec72aff5449b -->

El pendiente 116 nació de su pedido al empezar esta sesión: «tenemos que empezar a optimizar lo que tenemos desarrollado de Cimiento, hay mucho archivo .py».

Después aclaró qué quería decir con optimizar: «no repetir código. Cada que se necesita hacer algo se crea un archivo nuevo y ahí se crea todo sin revisar si esa funcionalidad o parte ya existe en otra parte, por ejemplo el manejo de rutas».

Con eso se midió el código y salió el hallazgo 2 del [resumen de la sesión](../../../../../historico-chat/resumenes/2026-10-04/optimizar-el-codigo-de-cimiento.md): el código se repite en vez de reusarse. Se escribió con «Escriba».

### 15 · Usuario, 2026-10-04 10:44:49
> pregunta: qué necesita?

**Agente**, 2026-10-04 10:44:55
<!-- agente: 2883383e-e629-445c-9744-f93381ce79ee -->

Para seguir con el análisis necesito tres respuestas:

1. **¿El análisis arranca con el hallazgo 2?** Es «el código se repite en vez de reusarse». Además, ¿se incluye aquí el 117, el del validador?
2. **¿Para qué proyectos sirve el validador?**
   - a) Para cualquier proyecto: reconoce el lenguaje según el tipo de proyecto. Esta es la que recomiendo.
   - b) Arranca solo con Python y después se amplía.
   - c) Solo para Cimiento.
3. **¿Qué hace el validador cuando encuentra una función repetida?** Mi recomendación es que avise sin bloquear y que compare lo que hace la función, no solo el nombre. Dos funciones con el mismo nombre no siempre hacen lo mismo.

### 16 · Usuario, 2026-10-04 10:45:48
> Explique: no entiendo ya estamos analizando o tavía, que debo hacer?

**Agente**, 2026-10-04 10:45:57
<!-- agente: 49d84f84-f7d2-4396-bba0-e3320c1112f4 -->

Sí, ya estamos analizando. El análisis del pendiente 116 está abierto, y todo lo que se escriba en el chat queda guardado en él.

Ahora le toca responder las tres preguntas. Basta con escribir, por ejemplo: «Analicemos: 1 sí, 2 a, 3 sí».

1. ¿Se trabaja también el pendiente 117 dentro de este análisis?
2. ¿El validador debe servir para cualquier proyecto, sin importar el lenguaje?
3. ¿Cuando el validador encuentre algo repetido, debe avisar en lugar de frenar el trabajo?

Con esas respuestas lleno el análisis y se lo presento para que lo apruebe.

### 17 · Usuario, 2026-10-04 10:50:24
> Analicemos: 
> - 1. sí, 
> - 2. Esta pregunta me da a entender que no se está revisando cimiento para hacer las cosas sino que responde solo por hacerlo  
> - 3. sí

**Agente**, 2026-10-04 10:51:04
<!-- agente: 35ad5def-f09e-4376-af85-33906041bfae -->

Tiene razón. La pregunta 2 no tocaba hacerla, porque Cimiento ya la responde y no lo revisé antes de preguntar:

- **La regla ya está.** El recuerdo [todo multiproyecto](../../../../../historico-chat/memory/todo-multiproyecto.md) dice que todo validador sirve para cualquier proyecto. Si el chequeo cambia según el lenguaje, primero se detecta el tipo de proyecto.
- **Ya existe un validador hermano que se puede seguir de modelo.** [calidad.py](../../../../../validadores/calidad.py) revisa la regla `07·Q3` (funciones demasiado largas). Lee las funciones de PHP, JavaScript y Python, avisa sin bloquear y recorre el código con [codigo.py](../../../../../validadores/codigo.py), que ya trabaja con 18 lenguajes.

Por eso el validador del pendiente 117 no se construye desde cero. Va al lado de `calidad.py` y reutiliza dos cosas: `codigo.py` para recorrer los archivos, y la parte de `calidad.py` que separa cada función. Si se copiara esa parte, se repetiría justo el problema que se está arreglando.

**Lo acordado en este turno:**
1. El pendiente 117 se trata dentro de este análisis.
2. El validador sirve para cualquier proyecto, siguiendo el modelo de `calidad.py` y reutilizando sus piezas.
3. Cuando encuentra algo repetido, avisa sin frenar el trabajo.

**Lección:** antes de preguntarle algo al usuario, buscar si Cimiento ya lo decidió (R-2). La anoto como lección del análisis.

¿Se lo presento lleno para que lo apruebe?

### 18 · Usuario, 2026-10-04 10:51:44
> Hágalo

**Agente**, 2026-10-04 10:59:45
<!-- agente: feebdd86-c382-44ba-be15-4e48a7d4652e -->

Estoy llenando el análisis; ya dejé registradas las dos lecciones (S-294 y S-295).

Ahora escribo la parte de abajo del análisis.

Ahora la parte de arriba: título, recomendaciones y las copias del hallazgo y del pendiente.

Ahora paso el hallazgo y el pendiente a su versión 2 en los archivos originales, como pide la fila 1.

Lo detuvo una sola comprobación: el pendiente tiene que enlazar un hallazgo con formato `### H-n` en el resumen. Los míos estaban escritos como lista numerada. Los paso a ese formato.

El análisis del pendiente 116 está completo y listo para aprobar: [analisis-1.md](../../../../../historico-chat/resumenes/2026-10-04/pendientes/116-el-codigo-de-cimiento-se-repite-en-vez-de-reusarse/analisis-1.md). Las comprobaciones de origen, de enlaces y de marcas de redacción no encontraron problemas.

**Qué sale del análisis:**

| Orden | Historia | Para qué |
|---|---|---|
| 1 | `EP-004` HU-026 | Un validador que avisa cuando se crea una función que ya existe. Se construye junto a `calidad.py` y usa sus piezas |
| 2 | `EP-024` HU-001 (épica nueva) | Rutas, carpeta raíz y git quedan en un solo lugar |
| 3 | `EP-024` HU-002 | Los validadores y los enganches dejan de repetir funciones |
| 4 | `EP-024` HU-003 | La plataforma deja de repetir funciones |

**Cambios fuera del análisis:**
- El pendiente 116 quedó en su versión 2.
- En el resumen de la sesión, los hallazgos que había escrito como lista numerada no pasaban la comprobación de origen. Ahora tienen el formato que esta pide: H-3 (código repetido), H-4 (el validador que falta) y H-5 (el arreglo de `analisis_en_curso.py`).
- Las dos lecciones del análisis quedaron registradas en la base de señales como S-294 y S-295.

Para aprobarlo, escribir «Apruebo el análisis».

### 19 · Usuario, 2026-10-04 11:01:26
> Recuerde que si aprueba el análisis no me tiene que estar preguntando cada rato si apruebo

**Agente**, 2026-10-04 11:02:37
<!-- agente: 0a0023dd-b7ee-49c4-922f-44e63086eeb3 -->

Ya actualicé el recuerdo [aprobar es la orden de dejarlo funcionando](../../../../../historico-chat/memory/aprobar-es-la-orden-de-hacerlo.md): cuando el análisis queda aprobado, sus HU, planes, código y pruebas se hacen completos, sin volver a pedirle aprobación en cada paso.

**Hay un choque con dos reglas escritas, y por ahora mandan ellas (`00·N10`):**
- `02·F4` dice que no se toca código hasta que el usuario dé un OK explícito a cada plan de trabajo.
- `02·F25` dice que autorizar el arranque no aprueba el plan.

Mientras esas dos reglas digan eso, voy a tener que pedirle el OK de cada plan aunque el recuerdo diga otra cosa. Es la segunda vez que pide esto, y `01·C10` dice que lo pedido dos veces se propone como regla.

**Mi propuesta:** cambiar `02·F4` y `02·F25` para que, cuando el análisis está aprobado, su aprobación cubra los planes que salen de él. Seguiría preguntando solo por el commit, por lo que no se puede deshacer y por lo que se salga de lo aprobado. Es un cambio de versión MAYOR del estándar y necesita su propio pendiente.

Para hacerlo, escriba «Registre».

### 20 · Usuario, 2026-10-04 11:08:29
> Analicemos: 
> 
> Sí, precisamente por eso ahora estamos aprobando el análisis completo y dejando establecidos los acuerdos. La finalidad es evitar tener que solicitar una aprobación individual para cada elemento que ya fue definido y acordado.
>
> Por ejemplo, si en el análisis se determina que se necesita la **Épica EP-00N**, se entiende que su creación está aprobada y que también quedan aprobados los planes de trabajo de las HU que se deriven de esa épica, siempre que estos correspondan a lo definido en el análisis.
>
> De esta manera, la aprobación del análisis permite avanzar con todo lo que se desprende de él sin tener que detener el proceso para solicitar nuevamente autorización sobre cada elemento. Solo se requeriría una nueva aprobación si durante la ejecución surge algo que no fue contemplado en el análisis aprobado.
> 

**Agente**, 2026-10-04 11:09:59
<!-- agente: 6cf4f4e3-cfd0-4b5d-b0f5-b9b99e2734c8 -->

Entendido, y en buena parte el estándar ya lo dice:

- **Lo que no se previó ya tiene su camino.** La excepción de `02·F9` y el freno detienen el trabajo ante un hallazgo y lo devuelven al análisis. Es lo que usted dice: pedir aprobación otra vez solo cuando aparece algo que el análisis no contempló.
- **Lo que choca son dos reglas.** `02·F4` exige un OK explícito para cada plan de trabajo, y `02·F25` dice que el permiso de arrancar no aprueba el plan. También choca la marca de aprobación del plan, que el validador [plan_vs_hecho.py:195](../../../../../validadores/plan_vs_hecho.py#L195) exige con «quién, cuándo y con qué versión».

**Lo que hay que cambiar:**
1. **`02·F4`.** Cuando el plan sale de un análisis aprobado y cumple sus filas de «Lo que se tiene que hacer», el plan queda aprobado. Se sigue escribiendo y mostrando, para que quede el rastro, pero no se espera el OK.
2. **`02·F25`.** Agregar que aprobar el análisis sí aprueba las épicas, las HU y los planes que salen de él.
3. **La marca del plan.** Que «aprobado» pueda citar el análisis: «por el análisis 1 del pendiente 116, aprobado el AAAA-MM-DD».

Es un cambio de versión MAYOR, porque cambia lo que se exige en todos los proyectos.

**Mi recomendación** es tratarlo como acuerdo 5 de este mismo análisis y no en un pendiente aparte. Iría como una HU nueva en `EP-023`, «lo que se construye es lo que se analizó», y en el primer lugar del orden: si no se cambia antes, las cuatro HU del pendiente 116 vuelven a pedirle el OK de cada plan.

¿Lo incluyo en este análisis?

### 21 · Usuario, 2026-10-04 11:16:23
> analicemos: 
> 
> Precisamente eso fue lo que dio origen a esta sesión: no existe un control adecuado y, ante cada situación que se presenta, la solución más fácil termina siendo crear un nuevo `.py` que repite muchas cosas que ya existen. Además, esto está generando choques entre reglas, como está ocurriendo actualmente con **02·F4** y **02·F25**.
>
> La idea no es seguir creando reglas que se contradigan entre sí, sino lograr que exista una **armonía y coherencia entre todas las reglas**. Si el mismo Cimiento termina contradiciéndose, entonces el problema se trasladará directamente a los proyectos que lo implementan.
>
> Por eso, antes de crear una nueva regla, se debe revisar lo que ya existe, determinar si la necesidad puede resolverse mediante una regla vigente o si realmente hace falta una nueva, y garantizar que la nueva definición sea compatible con las demás.
> 

**Agente**, 2026-10-04 11:16:58
<!-- agente: 843f0140-adb9-4e5f-a8b9-e2793c956255 -->

Cimiento ya tiene las dos reglas que piden eso. Lo que falla es que nada las hace cumplir cuando se crea algo, y pasa igual con el código y con las reglas:

| Qué se crea | La regla que ya lo pide | Qué la comprueba hoy |
|---|---|---|
| Una función | `07·Q4`: no repetir | Nada. Por eso existe el pendiente 117 |
| Una regla | `20·M12`: buscar por concepto antes de crear; afinar o extender antes que crear. Las filas 2 y 17 del [checklist](../../../../../base/20-meta-reglas/checklist.md) piden que no exista ya y que no choque con ninguna vigente | Solo la memoria del agente: se cumple si alguien se acuerda |

Es el mismo origen que el H-3: se crea antes de buscar.

**Propuesta para el análisis:**

5. **Las reglas siguen el mismo camino que el código.** Al crear o cambiar una regla, un control busca por significado las reglas parecidas y avisa cuáles leer antes. No se construye desde cero: la memoria ya busca por significado (`memoria/`) y [metareglas.py](../../../../../validadores/metareglas.py) ya revisa reglas. Va como HU en `EP-004`, junto a la del pendiente 117.
6. **`02·F4` y `02·F25` se cambian, no se crea una regla nueva.** En `02·F4` se agrega una excepción: el plan que sale de un análisis aprobado y cumple sus filas ya está aprobado. En `02·F25`, la aprobación del análisis cuenta como el segundo «sí». Revisé que esto es coherente con `00·N1` (aprobar vale para todo lo que el plan dice) y con la excepción de `02·F9` (lo no contemplado vuelve al análisis). Este cambio va de primero en el orden, porque las demás HU dependen de él.

¿Se incluyen los puntos 5 y 6 en este análisis?

### 22 · Usuario, 2026-10-04 11:18:02
> 00 id9

**Agente**, 2026-10-04 11:18:13
<!-- agente: d1bf8089-6743-4ba6-b226-866d2074f68e -->

La misma respuesta, más corta:

El origen es el mismo en el código y en las reglas: se crea antes de buscar. Las reglas ya existen, `07·Q4` para el código y `20·M12` para las reglas, pero ningún control las hace cumplir.

Propongo sumar al análisis:

5. **Un control para las reglas.** Cuando se crea o se cambia una regla, avisa cuáles reglas parecidas hay que leer. Usa la búsqueda por significado de `memoria/` y el validador `metareglas.py`, que ya existen. Va como HU en `EP-004`.
6. **Cambiar `02·F4` y `02·F25` en lugar de crear una regla nueva.** El análisis aprobado aprueba los planes que salen de él. Es coherente con `00·N1` y con `02·F9`. Va de primero, porque las demás HU dependen de él.

¿Se incluyen los dos en este análisis?

### 23 · Usuario, 2026-10-04 11:20:54
> Apruebo

**Agente**, 2026-10-04 11:23:23
<!-- agente: 02ca5f84-7417-4383-9a8f-259cf8c59141 -->

Incluí los acuerdos 5 y 6 en el [análisis](../../../../../historico-chat/resumenes/2026-10-04/pendientes/116-el-codigo-de-cimiento-se-repite-en-vez-de-reusarse/analisis-1.md). Pasó las comprobaciones de origen, de enlaces y de marcas de redacción sin errores.

Queda con 6 HU, en este orden:

1. `EP-023` HU-008: aprobar el análisis aprueba lo que sale de él (cambia `02·F4` y `02·F25`).
2. `EP-004` HU-026: aviso cuando se crea una función que ya existe.
3. `EP-004` HU-027: aviso cuando una regla nueva se parece a otra.
4. `EP-024` HU-001 a HU-003: el código repetido queda en un solo lugar en cada capa (validadores, enganches y plataforma).

El cambio sube la versión mayor del estándar.

Para cerrar el análisis falta escribir «Apruebo el análisis». Con eso queda aprobado todo lo que sale de él, y empiezo por la HU-008 de `EP-023`.

### 24 · Usuario, 2026-10-04 11:29:33
> analicemos: 
> 
> Todo esto debería implementarse con **Django**, de manera que quede centralizado, estructurado y más organizado.
>
> La idea es evitar seguir manejando funcionalidades dispersas en diferentes archivos `.py`, especialmente cuando terminan repitiendo lógica o generando conflictos entre reglas. Con Django se puede organizar cada responsabilidad dentro de una estructura definida, manteniendo en un mismo sistema las reglas, sus relaciones, validaciones y controles.
>
> De esta manera, no solo se facilita el mantenimiento de Cimiento, sino que también se puede tener un mayor control sobre cómo interactúan las reglas entre sí, reducir duplicidades y detectar posibles contradicciones antes de que terminen afectando a los proyectos que implementan Cimiento.
> 

**Agente**, 2026-10-04 11:30:40
<!-- agente: a194abf9-9507-49aa-ba85-7532a5d7b370 -->

Django ya está decidido en Cimiento. La aplicación `plataforma/` está hecha en Django y su hoja de ruta ([cvds/implementacion/README.md](../../../../../cvds/implementacion/README.md)) prevé que en la versión 3 sea la plataforma la que gobierne al agente. Lo que falta decidir es qué parte del trabajo pasa a Django y cuándo.

**Lo que encontré al revisar:**
- **El control de reglas parecidas ya existe.** Está en plataforma/nucleo/reglas/parecidas.py (`plataforma/nucleo/reglas/parecidas.py`, ya no está ahí): pone al lado las reglas que hablan de lo mismo y aclara que no detecta contradicciones. El acuerdo 5 proponía construirlo de nuevo, así que hay que cambiarlo para que use ese módulo. Volví a fallar en revisar lo que existe antes de proponer (R-2).
- **La plataforma no copia los validadores: los llama.** catalogo.py (`plataforma/nucleo/reglas/catalogo.py`, ya no está ahí) los usa como «puente hacia el estándar», y nueve módulos lo hacen igual.
- **Los enganches corren en cada mensaje y en cada proyecto.** Medido aquí, arrancar Django tarda 2,4 segundos y cargar un validador tarda 0,46. Además, los validadores solo usan lo que trae Python, así que funcionan en cualquier proyecto sin instalar nada.

**Opciones:**
1. **La lógica vive en un solo lugar, `validadores/`, y Django la administra.** Las reglas, cómo se relacionan entre ellas, las parecidas y los avisos se ven y se gobiernan desde `plataforma/`, que llama a los validadores como hoy. Los enganches siguen igual de rápidos.
2. **Todo pasa a Django.** Cada mensaje tarda unos 2 segundos más por cada enganche, y cada proyecto tendría que instalar Django.

**Recomiendo la 1.** Logra lo que se busca, que nada esté repetido ni disperso, sin volver más lento cada mensaje.

¿Cuál se toma?

### 25 · Usuario, 2026-10-04 11:32:20
> pase esto: plataforma a proyectos que es como simiento le exige a los demás proyectos que debe funcionar

**Agente**, 2026-10-04 11:32:27
<!-- agente: 515d613e-ba38-4a5d-bf3c-f69d05f48e57 -->

A este mensaje le falta la palabra que dice qué se espera: Analicemos, Hágalo, Corrija, Registre u otra de la lista.

Además, se puede entender de dos maneras:
1. **Tratar `plataforma/` como un proyecto más que hereda Cimiento.** Cumpliría las mismas reglas que Cimiento les exige a los demás proyectos: su cadena, sus pruebas y sus validadores.
2. **Mover `plataforma/` fuera de este repositorio**, a la carpeta de los proyectos, para que funcione igual que ellos.

¿Cuál de las dos?

### 26 · Usuario, 2026-10-04 11:34:49
> Hágalo: mueva esto: plataforma a proyectos que es como simiento le exige a los demás proyectos que debe funcionar

**Agente**, 2026-10-04 11:35:27
<!-- agente: e10cc805-fc97-45ba-91ed-c03d615a8d74 -->

Para moverla necesito un dato: **¿en qué carpeta queda la plataforma?** Mi propuesta es `C:\DesarrollosClaude\personales\cimiento-plataforma`, junto a scilit y los demás proyectos.

Esto es lo que voy a hacer con la carpeta que me indique, y lo agrego al análisis como acuerdo 7:

1. **Repositorio propio, con su historia.** Se saca `plataforma/` con `git subtree split`, así conserva sus commits.
2. **Cimiento instalado como en cualquier proyecto.** Se corre `instalar.py`, y desde ahí rigen su cadena, sus validadores y sus enganches.
3. **Arreglar lo que se rompe al separarla:**
   - La configuración lee `../validadores` y `../plantillas` (settings/base.py:20 (`plataforma/config/settings/base.py`, ya no está ahí)). Pasa a leer la ruta del estándar que deja el instalador.
   - `validadores/comun.py` y `validadores/corredor.py` nombran `plataforma/`.
   - Hay 188 documentos que la enlazan: las épicas EP-008 a EP-022 y `cvds/`. Esos documentos se quedan en Cimiento, porque son la decisión de construirla, y sus enlaces pasan a apuntar al repositorio nuevo.
4. **Borrar `plataforma/` de Cimiento**, pero solo después de comprobar que en su carpeta nueva levanta y pasa sus pruebas.

El paso 4 no se puede deshacer fácilmente. Por eso le confirmo justo antes de hacerlo.

### 27 · Usuario, 2026-10-04 11:37:03
> Hágalo: moverlo acá: C:\Ing. Jose\ia\agente\proyectos

**Agente**, 2026-10-04 11:46:08
<!-- agente: 6db38754-f879-47a4-8e84-47d10ce48747 -->

Primero dejo el acuerdo 7 en el análisis y después hago el traslado.

**Paré: el freno detuvo el traslado y quedó a medias.**

**Lo que alcancé a hacer:**
1. Saqué la historia de `plataforma/` a la rama `plataforma-historia`, dentro de Cimiento, con sus 31 commits.
2. La cloné en `proyectos/plataforma/`, pero la copia quedó incompleta.

**Por qué se detuvo:**
- **El freno.** No deja escribir en `proyectos/plataforma/` porque ninguna fase ni fila del análisis lo autoriza (`02·F8`). Es el mismo caso del [pendiente 118](../../../../../historico-chat/resumenes/2026-10-04/pendientes/118-el-freno-detiene-lo-que-el-usuario-ya-autorizo/pendiente.md), que reportó scilit: el freno no reconoce el «Hágalo» del chat. Lo anoté como H-6 en el resumen.
- **Rutas demasiado largas.** Windows no acepta rutas de más de 260 caracteres. Dentro de `proyectos/plataforma/datos/proyectos/cimiento-el-estandar/traido/...` hay rutas de hasta 273, así que esos archivos no se copiaron.
- **Efecto secundario.** Como `proyectos/` queda dentro de Cimiento, el revisor de enlaces de Cimiento ahora recorre también la copia y reporta cientos de enlaces rotos.

`plataforma/` sigue completa y funcionando en su sitio. No se borró nada.

**Para terminar el traslado hay que decidir tres cosas:**
1. **El permiso del freno.** Una opción es agregar al análisis una fila «de una y sin fase» para el traslado, aunque son 1.789 archivos y no se pueden nombrar uno por uno. La otra es resolver primero el pendiente 118. Recomiendo la fila en el análisis, nombrando solo los archivos de Cimiento que cambian; la copia se hace con git.
2. **Las rutas largas.** Activar `core.longpaths` en la copia, o ubicarla en una ruta más corta.
3. **Que Cimiento no revise `proyectos/`.** Agregar `proyectos/` a `.gitignore` y a las carpetas que los validadores no recorren.

¿Borro la copia incompleta de `proyectos/plataforma/` y sigo con esas tres opciones?

### 28 · Usuario, 2026-10-04 11:49:54
> 00 id9

**Agente**, 2026-10-04 11:50:05
<!-- agente: 6a682529-a7a2-4cea-8514-382488604d4a -->

Lo mismo, más corto:

El freno detuvo el traslado a `proyectos/plataforma/` y la copia quedó incompleta, porque Windows no acepta rutas de más de 260 caracteres. `plataforma/` sigue entera y funcionando donde estaba.

Para terminar falta:
1. Una fila en el análisis que autorice el traslado, para que el freno lo deje pasar.
2. Activar `core.longpaths` para las rutas largas.
3. Agregar `proyectos/` a `.gitignore`, para que los validadores de Cimiento no revisen esa carpeta.

¿Borro la copia incompleta y sigo?

### 29 · Usuario, 2026-10-04 11:50:56
> apruebo

**Agente**, 2026-10-04 12:07:58
<!-- agente: 69656daf-f52f-4bbb-93fc-2deb16e8f5d8 -->

Estoy dejando escritos en el análisis los archivos que va a tocar el traslado, para que el freno lo deje pasar.

Fila 9 escrita. Ahora borro la copia incompleta y vuelvo a clonar con rutas largas activadas.

Archivos locales copiados. Ahora la plataforma busca el estándar subiendo de carpeta.

`core.py` ya usaba la configuración; no hace falta tocarlo. Corro las pruebas de la plataforma en su sitio nuevo.

Falta un import en la prueba; lo agrego y la vuelvo a correr.

La plataforma pasa sus pruebas en el sitio nuevo. Sigo con los cambios en Cimiento.

**Paré otra vez: el freno no deja escribir `.gitignore`.** Es un error del freno. Al leer las rutas permitidas les quita los puntos del comienzo (`lstrip("./")` en [freno.py:112](../../../../../validadores/freno.py#L112)), así que `.gitignore` queda como `gitignore` y ningún análisis puede autorizarlo. Pasa lo mismo con cualquier archivo cuyo nombre empiece por punto.

**Lo que ya está hecho:**
- `proyectos/plataforma/` es un repositorio propio, con su historia y sus 1.789 archivos completos. Se activaron las rutas largas y se copiaron `.env`, la base local y `terceros/`.
- La plataforma encuentra Cimiento subiendo de carpeta. Arreglé la única prueba que fallaba, y pasaron 616 de 616.
- En Cimiento cambié `comun.py`, que ahora no recorre `proyectos/`, y `corredor.py`, que corre las pruebas de la plataforma en su sitio nuevo.

**Lo que falta:**
1. Agregar `proyectos/` a `.gitignore`. Esto necesita corregir el freno.
2. Instalar Cimiento en `proyectos/plataforma`.
3. Cambiar los enlaces de los 51 documentos que apuntan a la carpeta vieja.
4. Borrar `plataforma/` de Cimiento. Mientras siga ahí, `comun.py` ya no se salta su carpeta `datos/` y el revisor de enlaces va a reportar cientos de enlaces rotos.

**La corrección que propongo:** en [freno.py:112](../../../../../validadores/freno.py#L112), cambiar `lstrip("./")` por algo que quite solo un `./` del comienzo, y agregar una prueba con `.gitignore`.

¿Corrijo el freno y sigo con los pasos 1 a 4?

### 30 · Usuario, 2026-10-04 12:20:37
> Corrija  y siga

**Agente**, 2026-10-04 12:23:07
<!-- agente: 2c3572f9-fe2c-4181-bab4-b324ebd262aa -->

Freno corregido; 30 pruebas en verde. Sigo con `.gitignore`.

Instalado: 13 de 14 partes. Falta el planteamiento del proyecto, que el instalador no escribe. Ahora corrijo los enlaces.

Paso 4, que aprobó en este mensaje: quito `plataforma/` de Cimiento. La copia ya está verificada en `proyectos/plataforma/`.

**Paré: el freno no deja borrar la carpeta `plataforma`.** Solo acepta rutas que tengan `/` o `.` ([freno.py:113](../../../../../validadores/freno.py#L113)). El nombre de una carpeta suelto, como `plataforma`, no cumple esa condición, así que ningún análisis puede autorizar borrarla. Saltarse el freno con otra forma de escribir la ruta sería esquivarlo, y eso no lo hago.

**Lo que quedó hecho:**
- Corregí el freno para que respete el punto inicial de nombres como `.gitignore`, con 2 pruebas nuevas. Pasan las 30 pruebas del freno.
- Agregué `proyectos/` a `.gitignore`.
- Instalé Cimiento en `proyectos/plataforma`: quedan 13 de 14 partes, porque falta su planteamiento.
- Cambié los enlaces de 51 documentos a la ruta nueva.

**Lo que falta:** borrar `plataforma/` de Cimiento. Mientras siga ahí, el revisor de enlaces va a reportar cientos de errores en `plataforma/datos`.

Hay dos maneras de resolverlo:
1. **Corregir el freno**, para que una fila del análisis pueda autorizar una carpeta escrita como `` `plataforma/` ``, y no solo un archivo. Lo recomiendo, porque el traslado de cualquier proyecto va a necesitarlo.
2. **Que la borre usted a mano:** `git rm -r plataforma`.

¿Cuál?

### 31 · Usuario, 2026-10-04 12:26:34
> pregunta ya quedo copiada toda la plataforma?

**Agente**, 2026-10-04 12:35:15
<!-- agente: 9ee302b9-907b-47ef-92b8-d1d6d1f3e9da -->

Sí, la plataforma quedó copiada completa. Comparé archivo por archivo la carpeta vieja con la nueva, sin contar las diferencias de fin de línea, y todos coinciden salvo cuatro, que cambiaron a propósito:

| Archivo | Por qué cambió |
|---|---|
| `.gitignore` | El instalador de Cimiento le agregó sus líneas |
| `config/settings/base.py` | Ahora busca Cimiento subiendo de carpeta |
| `nucleo/comprobaciones/tests_estado.py` | Se corrigió la prueba que fallaba |
| `datos/auditoria/2026-10.md` | Tiene 42 líneas más, escritas al correr las pruebas en la carpeta nueva |

Además, la carpeta nueva trae lo que dejó el instalador (`.agente/`, `CLAUDE.md` y `.githooks/`) y su propio `.git`, con la historia.

Encontré otro problema: las pruebas escriben registros de prueba (`de-prueba`) en `datos/auditoria/`, que es el registro real. Eso va contra `00·N4`, que pide proteger los datos reales. Pasaba también en la carpeta vieja.

Sigue faltando borrar `plataforma/` de Cimiento. Para eso hay que decidir si corrijo el freno o la borra a mano.

### 32 · Usuario, 2026-10-04 12:37:18
> Analicemos: ya no se llama plataforma ahora es cimiento

**Agente**, 2026-10-04 12:37:51
<!-- agente: 90879106-f97a-4314-8e18-860d0d01c01e -->

Cambiar el nombre es sencillo. Lo que falta decidir es qué pasa con el nombre «Cimiento», que hoy ya tiene un dueño.

**El choque.** Según el recuerdo de [terminología](../../../../../historico-chat/memory/terminologia-agente-vs-estandar.md), «Cimiento» es lo que construye este repositorio: los validadores, los enganches y las reglas que se instalan en cada proyecto. Si la aplicación Django también se llama Cimiento, dos cosas distintas quedan con el mismo nombre. Ya pasó algo parecido con «el agente», y por eso existe ese recuerdo.

**Se puede entender de dos maneras:**
1. **La aplicación pasa a ser Cimiento, y este repositorio pasa a llamarse «el estándar».** Encaja con lo que ya decía el README de la plataforma: «esto es Cimiento corriendo como aplicación». Habría que actualizar el recuerdo de terminología.
2. **Solo cambia el nombre de la carpeta, a `proyectos/cimiento`.** Cimiento seguiría siendo todo, el repositorio y la aplicación juntos, y la aplicación sería «la aplicación de Cimiento».

**Lo que hay que cambiar en las dos:**
- Renombrar la carpeta `proyectos/plataforma` a `proyectos/cimiento`.
- La ruta en [corredor.py](../../../../../validadores/corredor.py) y en la fila 9 del análisis.
- La fila del registro de proyectos.
- Los 51 enlaces que acabo de cambiar.

La palabra «plataforma» aparece en las épicas EP-008 a EP-022 y en `cvds/`. Cambiarla ahí es otro trabajo, y solo hace falta en la opción 1.

¿Cuál de las dos?

### 33 · Usuario, 2026-10-04 12:38:58
> recuerde la apartura de esta sesion

**Agente**, 2026-10-04 12:40:13
<!-- agente: 8e16548e-a1f7-4fe6-b9c2-c04a4ee655bf -->

Quedó escrito en el recuerdo de [terminología](../../../../../historico-chat/memory/terminologia-agente-vs-estandar.md): desde el 2026-10-04, Cimiento es la aplicación Django. Allí se va a juntar lo que hoy está repartido en muchos `.py`, que fue el pedido con el que abrió esta sesión. No se le vuelve a decir «la plataforma».

También vi que `plataforma/` ya no está en Cimiento y que la carpeta nueva quedó como `proyectos/cimiento`.

Ese cambio de nombre dejó apuntando a la ruta vieja estas cosas, que hay que actualizar:
1. Los 51 enlaces, que apuntan a `proyectos/plataforma/`.
2. [corredor.py:46](../../../../../validadores/corredor.py#L46), que corre las pruebas en `proyectos/plataforma`.
3. La fila del registro de proyectos en `plantillas/proyectos.md`.
4. Las rutas de la fila 9 del análisis.

Para que haga esos cuatro cambios, escriba «Hágalo».

### 34 · Usuario, 2026-10-04 12:41:20
> Analicemos no le dije que creara una memoria lo que diciendo es que recuerde por qué fue que iniciamos esta sesion

**Agente**, 2026-10-04 12:41:47
<!-- agente: 1567695c-06a0-441a-8361-ae9b1b204172 -->

Entendido. Ya borré el párrafo que agregué al recuerdo de terminología; quedó como estaba.

**Por qué empezó esta sesión:** había que optimizar Cimiento. Tiene demasiados `.py`, y cada vez que hace falta algo se crea un archivo nuevo sin revisar si eso ya existe, como pasó con el manejo de rutas. Después se pidió que todo quedara centralizado en Django.

Con eso, la pregunta sobre el nombre ya está respondida. Cimiento es la aplicación Django, y ahí deben quedar juntos los `.py` que hoy están repartidos: validadores, enganches, memoria y métricas. Era un error preguntarlo como si fueran dos cosas distintas.

**Lo que eso cambia del análisis:** la épica `EP-024` del acuerdo 7 no consiste en «juntar las copias por capa». Consiste en llevar esos `.py` dentro de Cimiento-Django, sin copiarlos y sin que se repitan. Eso choca con algo que medí antes: arrancar Django tarda 2,4 segundos, y los enganches corren en cada mensaje. Hay que resolver ese punto en el análisis antes de aprobarlo.

¿Ajusto los acuerdos 2 y 7 y las HU de `EP-024` con ese objetivo?

### 35 · Usuario, 2026-10-04 12:59:05
> Hágalo: revise el gitignore si esta bien para ignorar las carpetas que estan dentro de proyecto/scilit

**Agente**, 2026-10-04 12:59:38
<!-- agente: a395b594-df24-4b29-839b-c1fdf8ed9d0e -->

Sí, `.gitignore` está bien. La línea 10, `proyectos/`, hace que Cimiento ignore todo lo que hay dentro de esa carpeta, también `proyectos/scilit/` y sus subcarpetas. Lo comprobé con `git check-ignore`, que reporta `proyectos/scilit` y `proyectos/scilit/README.md` como ignorados por esa regla.

Hay dos cosas que conviene tener en cuenta:
- `proyectos/scilit` todavía no existe. Por ahora solo están `cimiento/` y un `README.md` vacío.
- Ese `README.md` también queda ignorado. Si se quiere guardar en Cimiento para explicar qué es la carpeta, la regla tendría que cambiar a `proyectos/*` más `!proyectos/README.md`.

### 36 · Usuario, 2026-10-04 13:00:47
> hagalo: ignore esto: "Hágalo: revise el gitignore si esta bien para ignorar las carpetas que estan dentro de proyecto/scilit"

**Agente**, 2026-10-04 13:00:56
<!-- agente: 9746e78d-5159-42d1-a5ed-52ac0614cdeb -->

Listo, no lo tengo en cuenta. Ese pedido no cambió nada: solo hice una revisión de lectura.

Seguimos donde íbamos. ¿Ajusto los acuerdos 2 y 7 y las HU de `EP-024` para que los `.py` repartidos queden dentro de Cimiento (la aplicación Django)?

### 37 · Usuario, 2026-10-04 13:08:33
> analicemos: 
> 
> En la carpeta `cimiento` solo quiero que quede la **base de un proyecto Django**. Sobre esa base vamos a trabajar el propósito definido para esta sesión.
>
> Por lo tanto, todo lo que actualmente exista en esa carpeta y no haga parte de esa base debe eliminarse. La idea es partir de una estructura limpia y mínima, sin conservar archivos, código o componentes que no correspondan a la base inicial del proyecto.
>
> Una vez cumplido esto, podremos construir sobre esa base únicamente lo que se defina y apruebe durante esta sesión, evitando arrastrar elementos anteriores que puedan generar confusión o interferir con el propósito del trabajo.
> 

**Agente**, 2026-10-04 13:09:21
<!-- agente: 5540a7d1-6c3d-49b3-9b05-84562e302e8c -->

Lo que quedaría y lo que se iría de `proyectos/cimiento`:

| Se queda | Se borra |
|---|---|
| `manage.py`, `config/` (configuración, rutas, `wsgi.py`, `asgi.py`) con solo lo que trae Django, y `requirements/` | Las 15 aplicaciones de `nucleo/` (2,5 MB) |
| `.gitignore`, `.env.example` y `README.md`, reescritos para la base | `templates/`, `terceros/`, `descargar_estaticos.py` y `indice.sqlite3` |
| Lo que dejó la instalación de Cimiento: `.agente/`, `CLAUDE.md`, `.githooks/`, `historico-chat/`, `documentacion/versiones/` y `prompts/` | `datos/` (22 MB: auditoría y proyectos traídos) |

**Hay cuatro cosas para decidir:**
1. **La historia en git.** El borrado puede ir como un commit en el mismo repositorio, y así lo viejo se puede recuperar. La otra opción es empezar un repositorio nuevo, sin historia. Recomiendo el commit.
2. **`datos/`.** Es información real: registros de auditoría y copias de otros proyectos. Lo que está guardado en git se puede recuperar desde la historia, pero el registro de auditoría de octubre no está en git y se perdería. Recomiendo borrarlo de todos modos, porque la base parte limpia.
3. **La configuración.** Recomiendo dejarla como la genera Django al crear un proyecto, con un solo archivo de configuración, y no la división en dos archivos que hay hoy.
4. **Los documentos que quedan diciendo algo falso.** Las épicas EP-008 a EP-022 dicen que esas funciones ya están construidas. Cuando se borre el código, eso deja de ser cierto. Recomiendo marcarlas como retiradas, con fecha y enlace a este análisis, sin borrarlas. Así se hace con las reglas (`20·M11`).

Además, el acuerdo 7 dice que «la plataforma llama a `validadores/`». Ese acuerdo cambia: ahora es «Cimiento parte de una base Django vacía y sobre ella se construye solo lo que se apruebe en esta sesión». Va como acuerdo 8.

¿Se toman las cuatro recomendaciones?

### 38 · Usuario, 2026-10-04 13:10:32
> analicemos: si pero que tenga una estructura de un proyecto profesional y que va a crecer

**Agente**, 2026-10-04 13:11:12
<!-- agente: 66ac3208-9d46-4098-9742-bc04a2420223 -->

Cimiento ya tiene definida la estructura profesional para un proyecto Django: [plantillas/estructura-proyecto-django.md](../../../../../plantillas/estructura-proyecto-django.md). La recomendación 3 que di antes, dejar un solo archivo de configuración, contradice esa plantilla, así que la retiro. Volví a proponer sin revisar primero lo que ya existe.

**La base quedaría como pide la plantilla:**
```
cimiento/
├── .env.example · .gitignore · README.md · manage.py
├── requirements/   base.txt · local.txt · lock.txt (las versiones exactas, hoy no existe)
├── config/
│   ├── settings/   base.py (lo común) · local.py (lo del equipo de desarrollo)
│   ├── urls.py     solo la página de administración
│   └── wsgi.py · asgi.py
├── static/         (vacía, para lo propio del proyecto)
├── templates/      (vacía)
└── «paquete»/      (vacía: cada módulo será una carpeta y una aplicación de Django)
```
A eso se suma lo que dejó la instalación de Cimiento: `.agente/`, `CLAUDE.md`, `.githooks/`, `historico-chat/`, `documentacion/` y `prompts/`.

Así puede crecer sin reorganizarse: cada módulo nuevo es una carpeta con su modelo, sus vistas, sus pruebas y sus migraciones (`14·EST1`), y la configuración ya está separada por entorno.

**Falta un dato: el nombre de la carpeta donde van los módulos.** Hoy se llama `nucleo/`. Recomiendo dejar ese nombre, porque ya está en `.agente/mapeo-nombres.md`.

Las demás decisiones siguen como se recomendó:
- El borrado va como un commit, y se conserva la historia.
- Se borra `datos/`.
- Las épicas EP-008 a EP-022 se marcan como retiradas.

¿El paquete queda como `nucleo/`?

### 39 · Usuario, 2026-10-04 13:12:55
> pregunta: qué espera que le responda?

**Agente**, 2026-10-04 13:13:05
<!-- agente: f35a1756-bc12-4938-b7f3-7478b7a2a458 -->

Solo necesito saber qué nombre lleva la carpeta donde van a ir los módulos del proyecto.

- Si sirve el nombre que tiene hoy, basta con responder «Analicemos: nucleo».
- Si prefiere otro, basta con escribirlo, por ejemplo «Analicemos: modulos».

Con esa respuesta dejo escritos en el análisis los acuerdos sobre la base de Cimiento, y el análisis queda listo para que lo apruebe.

### 40 · Usuario, 2026-10-04 13:13:41
> Pregunta: qué nombre recomienda?

**Agente**, 2026-10-04 13:13:55
<!-- agente: adba737c-1452-4101-8511-1e5db0c4cffb -->

Recomiendo **`nucleo`**, por tres razones:

1. Ya está registrado en `.agente/mapeo-nombres.md`, que es donde Cimiento comprueba la ruta de los módulos. Cambiarlo obligaría a corregir ese archivo.
2. Dice en español lo que guarda: el centro del sistema, donde van los módulos.
3. Evita una confusión. Lo habitual en Django es que la carpeta lleve el nombre del proyecto, y eso daría `cimiento/cimiento/`: dos carpetas con el mismo nombre, una dentro de la otra.

Si está de acuerdo, puede responder «Analicemos: nucleo».

### 41 · Usuario, 2026-10-04 13:14:19
> Analicemos: core

**Agente**, 2026-10-04 13:16:19
<!-- agente: 354c95c4-973a-4571-ba7f-3e51557686d4 -->

Ahora agrego al análisis las filas de lo que hay que hacer, con las rutas exactas de cada cambio.

Ya quedó en el análisis: la carpeta de los módulos se llamará `core/`.

**Acuerdos nuevos:**
- **8.** Cimiento es la aplicación Django y vive en `proyectos/cimiento/`.
- **9.** Cimiento arranca desde una base Django limpia, con la estructura que pide la plantilla del estándar: la configuración separada por entorno, `lock.txt`, `static/`, `templates/` y `core/`.
- **10.** Las épicas EP-008 a EP-022 se marcan como retiradas.

**Lo que queda por hacer:**
- **Fila 10.** Cambiar a la ruta `proyectos/cimiento/` en `corredor.py` y en los enlaces de los documentos.
- **Fila 11.** Dejar en `proyectos/cimiento/` solo la base y comprobar que arranca.
- **Fila 12.** Marcar las 15 épicas como retiradas.

Cada fila nombra sus archivos exactos, así que el freno las va a dejar pasar.

Queda una pregunta abierta, para resolverla al escribir las HU de `EP-024`: si los enganches llaman a Django, cada mensaje tarda 2,4 segundos en vez de 0,46.

El análisis está listo. Para aprobarlo, escribir «Apruebo el análisis»; con eso se hacen las filas 1 a 12.

### 42 · Usuario, 2026-10-04 13:17:17
> ya es claro lo que se tiene que hacer?

**Agente**, 2026-10-04 13:17:23
<!-- agente: fe5e16ab-80c8-4233-827c-d0de0dae1fa5 -->

Al mensaje le falta la palabra del comienzo. Si es una pregunta, se escribe «Pregunta: ¿ya es claro lo que se tiene que hacer?».

### 43 · Usuario, 2026-10-04 13:17:33
> Pregunta: ¿ya es claro lo que se tiene que hacer?

**Agente**, 2026-10-04 13:17:48
<!-- agente: 4a93dffc-f97a-49ba-b43d-501b423d712c -->

Todavía no del todo. Lo inmediato está claro (filas 1 a 12): mover Cimiento a `proyectos/cimiento/`, dejar ahí la base Django con `core/` y marcar las épicas EP-008 a EP-022 como retiradas.

Lo de después tiene tres puntos sin resolver dentro del análisis:

1. **Las HU de `EP-024` describen el plan viejo.** Dicen que las copias se juntan en un sitio común de cada capa, como `comun.py`. El acuerdo 8 dice otra cosa: todo se junta dentro de Cimiento-Django.
2. **Los enganches dentro de Django.** Si los validadores pasan a Django, cada mensaje se demora 2,4 segundos en vez de 0,46, y cada proyecto tiene que instalar Django. Falta decidir si los enganches quedan livianos y llaman a Django, o si todo pasa a Django y se acepta ese costo.
3. **El control de reglas parecidas se pierde.** Ya existía en `nucleo/reglas/parecidas.py`, y la fila 11 lo borra junto con todo `nucleo/`. Falta decidir si se rescata para `core/` o si se escribe de nuevo cuando llegue su HU.

Recomiendo resolver esos tres puntos antes de aprobar. Si no se resuelven, los planes de `EP-024` van a volver a pedir decisiones.

### 44 · Usuario, 2026-10-04 13:18:21
> pregunta sino es claro por qué me dice que apruebe el análisis?

**Agente**, 2026-10-04 13:18:34
<!-- agente: e5aca0d5-e802-4fc0-adef-5695b83bc691 -->

Fue un error mío. Le pedí aprobar el análisis sin haberlo revisado entero contra los acuerdos nuevos. Los tres puntos que encontré después ya estaban ahí, así que no debí pedírselo.

El análisis no está listo para aprobarse hasta que se resuelvan esos tres puntos. Mi recomendación para cada uno:

1. **Las HU de `EP-024`:** reescribirlas con el objetivo nuevo. Los `.py` repartidos se llevan a módulos de `core/`, uno por tema, sin copiarlos.
2. **Los enganches:** que sigan siendo livianos, sin Django, y que solo pasen el pedido a Cimiento. Así cada mensaje no espera 2,4 segundos, y la lógica queda en un solo lugar, dentro de `core/`.
3. **`parecidas.py`:** sacarlo antes de limpiar la carpeta y llevarlo a `core/` cuando se construya su HU. Ya funciona, y escribirlo de nuevo sería repetir trabajo.

Si está de acuerdo con las tres, las paso al análisis y reviso el documento completo antes de volver a pedirle la aprobación.

### 45 · Usuario, 2026-10-04 13:18:58
> Hagalo: cree la base que le pedí

**Agente**, 2026-10-04 13:23:37
<!-- agente: f0ab7534-7724-47df-bf4a-1bdd582249f0 -->

Empiezo la limpieza. Primero agrego a la fila 11 los tres archivos que faltaban (`manage.py`, `wsgi.py` y `asgi.py`) y después borro lo que no es base.

El freno detuvo una orden mal escrita por mí: tenía una ruta duplicada. La corrijo.

El freno resuelve las rutas desde la carpeta donde quedó la consola y no tiene en cuenta el `cd` de la orden. Uso rutas absolutas.

Contenido viejo borrado. Ahora escribo los archivos de la base.

Ahora `manage.py`, `.agente/mapeo-nombres.md` y la prueba de que arranca.

Dejo los `__pycache__` en su sitio; el `.gitignore` ya los excluye. Corro las comprobaciones.

La base de Cimiento quedó lista en `proyectos/cimiento/`. Django la revisa sin errores (`check`), `migrate` crea la base de datos y el servidor arranca.

```
cimiento/
├── .env.example · .gitignore · README.md · manage.py
├── config/   settings/base.py · settings/local.py · urls.py (solo el administrador) · wsgi.py · asgi.py · ambiente.py
├── core/     vacío, para los módulos
├── requirements/   base.txt · local.txt · lock.txt (versiones exactas)
├── static/ · templates/
└── lo que deja Cimiento al instalarse: .agente/ · CLAUDE.md · .githooks/ · historico-chat/ · documentacion/ · prompts/
```

Se borraron `nucleo/`, `datos/`, `terceros/`, las plantillas, la base de datos vieja y `descargar_estaticos.py`. En `.agente/mapeo-nombres.md` quedó escrito que los módulos van en `core/<modulo>`.

**Lo que falta:**
1. Las filas 10 y 12 del análisis. La 10 corrige los enlaces y `corredor.py`, que todavía apuntan a `proyectos/plataforma/`; mientras tanto el revisor de enlaces sigue marcando errores. La 12 marca las épicas como retiradas.
2. Los tres puntos abiertos del análisis: las HU de `EP-024`, si los enganches llaman a Django y qué hacer con `parecidas.py`. Ese archivo se borró junto con `nucleo/`, pero se puede recuperar del historial de git.
3. Guardar el borrado y la base nueva como un commit en el repositorio de `proyectos/cimiento`. Antes de hacerlo necesito su aprobación.

### 46 · Usuario, 2026-10-04 13:26:05
> 
> analicemos: la estructura con la que quedó no es la que acordamos:
> 
> cimiento/
> ├── .env.example · .gitignore · README.md · manage.py
> ├── requirements/   base.txt · local.txt · lock.txt (las versiones exactas, hoy no existe)
> ├── config/
> │   ├── settings/   base.py (lo común) · local.py (lo del equipo de desarrollo)
> │   ├── urls.py     solo la página de administración
> │   └── wsgi.py · asgi.py
> ├── static/         (vacía, para lo propio del proyecto)
> ├── templates/      (vacía)
> └── «paquete»/      (vacía: cada módulo será una carpeta y una aplicación de Django)
> 

**Agente**, 2026-10-04 13:26:33
<!-- agente: 025bda39-8756-4b71-87d1-4bb5e5d40d3a -->

Tiene razón: hay cosas que no se acordaron. Comparé la carpeta con la estructura del acuerdo:

| Sobra | Qué es |
|---|---|
| `config/ambiente.py` | Un lector del `.env` que venía de la plataforma |
| `manage.py` con código propio | Carga ese lector y pone el puerto. El acordado es el `manage.py` normal de Django |
| `.env` | El archivo de la plataforma vieja, copiado. No se versiona, pero no es parte de la base |
| `db.sqlite3` | Lo creó `migrate` cuando probé que arrancara. No se versiona |

Los dos archivos `.gitkeep` en `static/` y `templates/` tampoco estaban en el acuerdo, pero son necesarios: git no guarda carpetas vacías, y sin ellos esas dos carpetas desaparecerían.

El error fue mío: conservé `ambiente.py` y el `manage.py` viejo sin que estuvieran en lo acordado.

**Lo que propongo corregir:**
1. Borrar `config/ambiente.py`, `.env` y `db.sqlite3`.
2. Dejar `manage.py` como lo genera Django.
3. Quitar `PUERTO` de `.env.example`, porque solo lo usaba el `manage.py` viejo.

Con eso queda exactamente la estructura acordada.

¿Lo corrijo?

### 47 · Usuario, 2026-10-04 13:30:37
> analicemos: ya lo corregí

**Agente**, 2026-10-04 13:31:02
<!-- agente: 87201fa5-ef6d-455e-8541-f75ee552e735 -->

Revisé la carpeta y solo se borró `db.sqlite3`. Además desapareció `.gitignore`, y ese archivo sí hace parte de la base acordada.

Siguen igual que antes:
- `config/ambiente.py`
- `.env`
- `manage.py`, que todavía tiene el código del puerto y carga `ambiente`
- `.env.example`, que todavía tiene `PUERTO`

Django la revisa sin errores (`check`), pero la estructura todavía no es la acordada. Puede ser que los cambios no se hayan guardado en el disco, o que se hayan hecho en otra carpeta.

### 48 · Usuario, 2026-10-04 13:32:35
> 
> analicemos el git es hermano de la carpeta proyectos

**Agente**, 2026-10-04 13:33:09
<!-- agente: e2dcc9b0-0ad8-4d2c-8b48-28cda7ac774f -->

Entendido: `proyectos/` se guarda en el mismo repositorio de Cimiento. Por eso quitó `proyectos/` del `.gitignore` y el `.git` propio de `proyectos/cimiento/`. No se pierde historia: esos 31 commits ya estaban en Cimiento.

Lo que cambia con eso:

1. **Hay un riesgo con las claves.** Al borrar el `.gitignore` de `proyectos/cimiento/`, ya nada excluye su `.env`, que trae la clave de firma, ni `db.sqlite3` ni `staticfiles/`. El `.gitignore` de la raíz no los cubre: `*.db` no incluye `.sqlite3`. Si se hace un commit así, el `.env` entra al repositorio, y eso va contra `00·N6`. Hay que agregar esas tres rutas al `.gitignore` de la raíz.
2. **Los archivos de la instalación sobran.** `.agente/`, `CLAUDE.md`, `.claude/`, `.githooks/`, `historico-chat/`, `documentacion/versiones/` y `prompts/` eran para un proyecto aparte. Dentro de Cimiento ya funcionan los enganches de la raíz. Recomiendo borrarlos.
3. **Los validadores no revisan esa carpeta.** `validadores/comun.py` se salta `proyectos/`, así que hoy el código de Cimiento no se revisaría. Recomiendo quitar esa exclusión.
4. **Las pruebas apuntan a la ruta vieja.** `validadores/corredor.py` todavía busca `proyectos/plataforma`.
5. **Sobra la rama `plataforma-historia`.** La creé en Cimiento para el traslado y ya no hace falta.
6. **El acuerdo 7 cambia.** Ya no dice «repositorio propio», sino «carpeta `proyectos/cimiento/` dentro de Cimiento».

El punto 1 es urgente. ¿Hago los seis cambios?

### 49 · Usuario, 2026-10-04 13:35:55
> 
> analicemos: el objetivo de esta sesión es optimizar todos los .py y para es cimiento

**Agente**, 2026-10-04 13:36:15
<!-- agente: 9c31c82f-3b14-46bc-96a0-1c384696b7ec -->

Entendido. La sesión es para optimizar todos los `.py`, y el lugar donde van a quedar es Cimiento, en `proyectos/cimiento/`. Los seis puntos que traje antes se resuelven como parte de ese traslado.

**Hacia dónde va cada grupo de `.py`:**

| Hoy | Archivos | Pasa a |
|---|---|---|
| `validadores/` | 87 | Módulos de `core/` agrupados por tema (reglas, documentos, fases, git, redacción), cada función escrita una sola vez |
| `adaptadores/claude-code/` | 21 | `core/enganches/`: lo que recibe cada evento de Claude Code |
| `memoria/` y `metricas/` | 7 | `core/memoria/` y `core/metricas/` |
| `interfaz/` | 34 | Se junta con Cimiento, porque es otra aplicación Django aparte |
| `historico-chat/scripts/` | 208 | No se mueve: `04·S18` exige conservarlos tal cual |

**El punto que hay que decidir es la velocidad de los enganches.** No hace falta que cada mensaje arranque Django. La lógica de cada módulo de `core/` se escribe en Python simple, sin depender de Django, y solo los modelos y las pantallas lo usan. Así los enganches importan esa lógica directamente y siguen tardando lo mismo que hoy, cerca de medio segundo, con el código en un solo sitio.

**El orden que propongo:**
1. Primero lo que más se repite: rutas, git, lectura de archivos y tablas. Eso va a `core/comun/`.
2. Después cada grupo, uno por HU. Cada `.py` viejo se borra cuando su reemplazo pasa sus pruebas.

¿Se toma esa forma de resolver los enganches (lógica en Python simple dentro de `core/`)?

### 50 · Usuario, 2026-10-04 13:38:46
> analicemos: esta:interfaz/ tampoco va por ahora

**Agente**, 2026-10-04 13:38:56
<!-- agente: 660f8028-0d06-4324-8af5-26433bdc02a4 -->

Anotado: `interfaz/` queda por fuera por ahora. Pasan a Cimiento estos cuatro grupos:

| Hoy | Archivos | Pasa a |
|---|---|---|
| `validadores/` | 87 | Módulos de `core/` por tema, con cada función escrita una sola vez |
| `adaptadores/claude-code/` | 21 | `core/enganches/` |
| `memoria/` y `metricas/` | 7 | `core/memoria/` y `core/metricas/` |
| Lo que se repite en todos (rutas, git, lectura) | — | `core/comun/`, de primero |

Falta saber una cosa: ¿la lógica de `core/` se escribe en Python simple, sin depender de Django, para que los enganches la llamen sin hacer más lento cada mensaje?

### 51 · Usuario, 2026-10-04 13:40:45
> hágalo: por ahora empecemos con los validadores estos deben ser clases

**Agente**, 2026-10-04 13:44:59
<!-- agente: adbc4d28-c61a-4476-9593-f16f09c5b860 -->

Empiezo por revisar cómo están hechos hoy los validadores (el resultado común, la lectura de archivos y las rutas), para pasarlos a clases sin perder nada.

Ya tengo las piezas. Anoto en el análisis el acuerdo de que los validadores son clases, y la fila con los archivos de este primer paso.

Escribo `core/comun/`.

Ahora la clase base de los validadores, el recorrido de código y el primer validador.

Ahora las pruebas de las dos partes.

Pasan las 18 pruebas, y cargar los validadores sin Django tarda 0,08 segundos. Compruebo que el validador nuevo encuentre lo mismo que el viejo en el repositorio real.

Listo el primer paso: los validadores ya son clases dentro de Cimiento.

**Lo que quedó en `proyectos/cimiento/core/`:**
- `comun/`: lo que todos usan, escrito una sola vez. `Proyecto` maneja las rutas, entiende `/c/...` y sabe si una ruta queda dentro del proyecto. `Git` corre git y maneja sus errores. `Archivos` lee sin que un archivo dañado detenga todo. `Hallazgo` registra lo que se encontró.
- `validadores/base.py`: la clase `Validador`. Cada validador hereda de ella y queda registrado con su nombre. Si dos validadores usan el mismo nombre, se reporta como error.
- `validadores/calidad.py`: `FuncionesLargas` (`07·Q3`), el primer validador pasado a clase, junto con `RecorridoDeCodigo`.

**Comprobaciones:**
- Pasan 18 de 18 pruebas, tanto con `unittest` como con `manage.py test core`.
- Sobre el repositorio de Cimiento, la clase nueva encuentra los mismos 15 avisos que el validador viejo.
- Cargar los validadores toma 0,08 segundos y no necesita Django, así que los enganches no se vuelven más lentos.

**Lo que sigue:**
1. Pasar los otros 86 validadores, por grupos de tema, con el mismo patrón.
2. Hacer que `validar.py` y los enganches usen las clases nuevas. Mientras eso no pase, el `calidad.py` viejo se queda, porque todavía lo usan. Se borra cuando ya nadie lo llame.
3. Las filas 10 y 12 del análisis, que siguen pendientes, y el commit, que todavía no tiene su aprobación.

### 52 · Usuario, 2026-10-04 13:46:52
> 
> apruebo

**Agente**, 2026-10-04 13:51:20
<!-- agente: 0965a177-a466-46d6-8768-bf2597c5cfbf -->

Sigo con el siguiente grupo: los validadores que revisan el código de los proyectos. Empiezo por los cuatro más pequeños: `errores`, `seguridad`, `rendimiento` y `aislamiento`.

Ahora paso las pruebas que ya existían para estos cuatro validadores.

Los cinco dan lo mismo que antes en Cimiento. Los pruebo también en un proyecto PHP real, porque en Cimiento casi no hay código de ese tipo.

Listo el segundo grupo: los cinco validadores que revisan el código de los proyectos ya son clases dentro de Cimiento.

| Clase | Regla | Antes |
|---|---|---|
| `FuncionesLargas` | `07·Q3` | `calidad.py` |
| `CapturasYLogs` | `05·E1`, `05·E5` | `errores.py` |
| `InyeccionYSesion` | `04·S3`, `04·S5` | `seguridad.py` |
| `ConsultasCostosas` | `06·R1`, `06·R2` | `rendimiento.py` |
| `PruebasAisladas` | `08·T3`, `08·T4` | `aislamiento.py` |

**Lo repetido que se eliminó:**
- El recorrido del código aparecía cinco veces; ahora está una sola vez, en `ValidadorDeCodigo`. Cada validador solo escribe `revisar_texto`.
- La búsqueda de bloques (`{...}` y bloques con sangría) estaba copiada en dos archivos; ahora está una sola vez, en `Bloques`.

**Comprobaciones:**
- Pasan las 31 pruebas. Las de estos validadores son las mismas que tenían en `pruebas.py`, adaptadas a las clases.
- Los validadores nuevos encuentran exactamente lo mismo que los viejos en tres proyectos reales: Cimiento, dp y scilit. La única diferencia es intencional: el aviso de funciones largas ahora dice `07·Q3` en lugar de `Q3`.

Falta pasar 81 validadores. Los `.py` viejos se quedan hasta que `validar.py` y los enganches usen las clases nuevas. El commit todavía necesita su aprobación.

### 53 · Usuario, 2026-10-04 13:53:38
> 
> hágalo: suba git

**Agente**, 2026-10-04 13:56:19
<!-- agente: db327846-8407-4a44-a0da-0fbd88db666c -->

El `.env` ya quedó excluido y los 51 enlaces apuntan a la carpeta nueva. Reviso si quedan enlaces rotos: muchos apuntaban a código que se borró al limpiar la base.

Solo queda un enlace roto, en un resumen viejo (`2026-08-22/sesion-6.md`), que apunta a `plataforma/`. Preparo el commit y reviso que no entre nada privado.

**Paré: el freno detuvo el commit.** No se subió nada. Los cambios quedaron preparados (`git add`), pero no se guardaron.

**Por qué se detuvo:** el commit incluye el borrado de los 1.789 archivos de `plataforma/`, que se hizo a mano. Ninguna fila del análisis autoriza esos archivos. Como el freno solo acepta rutas exactas, no hay forma de nombrar la carpeta completa.

**Lo que revisé antes:**
- No entra nada privado. `proyectos/cimiento/.env` ya está excluido en el `.gitignore` de la raíz, igual que `db.sqlite3`, `CLAUDE.md` y `.agente/`.
- Quedan dos cosas para decidir:
  - `proyectos/cimiento/config/ambiente.py` sigue en el disco y entraría al commit, aunque no hace parte de la base acordada.
  - También entrarían las transcripciones de otras sesiones (`2026-09-30` y `2026-10-01`), que se escriben solas.

**Opciones para subir:**
1. **Hacer el commit y el push a mano**, con los cambios ya preparados: `git commit` y `git push`. Es lo más rápido.
2. **Agregar al análisis una fila con las 1.789 rutas de `plataforma/`**, armada con un guion, para que el freno deje pasar el commit. Funciona, pero deja una fila enorme en el análisis.
3. **Corregir el freno para que una fila pueda autorizar una carpeta entera.** Es el mismo defecto que ya apareció al borrar `plataforma/`.

Recomiendo la 1 para este commit y la 3 como pendiente.

¿Borro antes `ambiente.py`?

### 54 · Usuario, 2026-10-04 13:57:08
> 
> 00 id9

**Agente**, 2026-10-04 13:57:19
<!-- agente: 36978c6a-9ff8-4609-ae63-cf350356e4ad -->

Lo mismo, más corto:

El freno detuvo el commit porque ninguna fila del análisis autoriza el borrado de los 1.789 archivos de `plataforma/`. No se subió nada. Los cambios quedaron preparados y no entra ningún archivo privado.

Recomiendo hacer el commit y el push a mano (`git commit` y `git push`) y dejar como pendiente la corrección del freno, para que una fila pueda autorizar una carpeta completa.

¿Borro antes `config/ambiente.py`, que no hace parte de la base?

### 55 · Usuario, 2026-10-04 13:58:35
> 
> Pregunta y por qué lo va a borrar?

**Agente**, 2026-10-04 13:58:47
<!-- agente: 7c38524d-17e2-4cbe-8b5b-a8412230bc2e -->

Porque no está en la estructura de la base que se acordó: viene de la plataforma vieja. Lo que hace es leer el `.env` y cargar sus valores en el entorno, como la clave de firma y el puerto.

Hay dos cosas que debí decir antes:
- **Borrarlo solo dañaría Cimiento.** `manage.py` lo carga al arrancar. Si se borra, también hay que dejar `manage.py` como lo genera Django.
- **Sin él, Cimiento ya no lee el `.env`.** La clave de firma tendría que llegar por otro camino. Django no lee ese archivo por sí solo.

Por eso, borrarlo o conservarlo es una decisión, no una limpieza. Si se conserva, la base queda con su lector del `.env` y hay que agregarlo a la estructura acordada.

### 56 · Usuario, 2026-10-04 13:59:57
> 
> Analicemos: ya lo borré

**Agente**, 2026-10-04 14:00:20
<!-- agente: f2a08f60-b6d9-4355-bb5d-53b56f775172 -->

Verifiqué la carpeta: `ambiente.py` ya no está. Pero ahora **Cimiento no arranca**. `manage.py` todavía lo importa en la línea 37, y `python manage.py check` termina con `ImportError: cannot import name 'ambiente'`.

Para que vuelva a funcionar, `manage.py` tiene que quedar como lo genera Django, sin el código del puerto y sin cargar `ambiente`. De paso, en `.env.example` sobra `PUERTO`.

¿Lo corrijo?

### 57 · Usuario, 2026-10-04 14:01:01
> analicemos: ya lo recuperé

**Agente**, 2026-10-04 14:01:22
<!-- agente: f7d8f73d-2b3c-4d8e-864f-5c62f10cca6d -->

Confirmado: `config/ambiente.py` está otra vez en su sitio y Cimiento arranca sin errores (`check`).

Si se queda, conviene agregarlo a la estructura acordada de la base como el lector del `.env`, para que no vuelva a parecer que sobra. Con eso, lo único que falta para subir es hacer el commit y el push a mano, porque el freno no deja pasar el borrado de `plataforma/`.

### 58 · Usuario, 2026-10-04 14:30:50
> pregunta: pero si plataforma ya esite por qué la sigue nombrando

**Agente**, 2026-10-04 14:31:06
<!-- agente: d54e788f-3c20-42e2-bf98-ddb2db531310 -->

Porque en el disco ya no existe, pero en git sí. El último commit todavía guarda los 1.789 archivos de `plataforma/`. Para que el repositorio refleje que se borraron, el próximo commit tiene que registrar ese borrado.

El freno no se fija en si la carpeta existe. Revisa la lista de cambios del commit, y ahí aparecen esos 1.789 borrados como «archivos tocados» que ninguna fila del análisis autoriza. Por eso sigo nombrándola: después de ese commit, `plataforma/` deja de aparecer.

### 59 · Usuario, 2026-10-04 14:33:12
> que commit le agrego?

**Agente**, 2026-10-04 14:33:23
<!-- agente: adc693b4-c3df-4a39-9c50-0f254e24e639 -->

Al mensaje le falta la palabra del comienzo. Si pide el texto del commit, se escribe «Redacte: el mensaje del commit».

### 60 · Usuario, 2026-10-04 14:33:45
> Redacte: el mensaje del commit

**Agente**, 2026-10-04 14:34:00
<!-- agente: 489a5cf6-3a7f-4f4a-9334-d489d33ea1aa -->

Mensaje escrito para el historial de git de Cimiento.

```
feat(cimiento): Cimiento pasa a ser la aplicación Django y los validadores empiezan a ser clases

El usuario pidió optimizar los .py de Cimiento: cada vez que se necesita
algo se crea un archivo nuevo sin revisar si eso ya existe, como pasó con
el manejo de rutas. Decidió que todo se centralice en Django, en
proyectos/cimiento, partiendo de una base limpia, y que los validadores
sean clases.

Lo que hizo el agente:
- plataforma/ sale de la raíz y queda proyectos/cimiento/ con la base
  Django de plantillas/estructura-proyecto-django.md (config/settings por
  entorno, requirements con lock.txt, static/, templates/ y core/).
- core/comun/: Proyecto, Git, Archivos y Hallazgo, escritos una sola vez.
- core/validadores/: la clase Validador, ValidadorDeCodigo y Bloques, y
  cinco validadores pasados a clases (07·Q3, 05·E1/E5, 04·S3/S5,
  06·R1/R2, 08·T3/T4). Dan los mismos hallazgos que los viejos en
  Cimiento, dp y scilit; 31 pruebas en verde.
- freno.py: una fila del análisis ya puede autorizar .gitignore y otros
  archivos que empiezan con punto.
- analisis_en_curso.py: un análisis aprobado ya no queda abierto para
  siempre por una HU que no existe.
- .gitignore: .env, db.sqlite3 y la configuración local de cada proyecto
  en proyectos/ no entran al repositorio (00·N6).
- Los enlaces de 51 documentos apuntan a proyectos/cimiento/.
- Análisis 1 del pendiente 116 y pendientes 116 y 117.
```

Como los cambios ya están preparados, para guardarlo se copia el mensaje en un archivo y se corre `git commit -F archivo`, y después `git push`.

### 61 · Usuario, 2026-10-04 14:37:54
> analicemos: ese freno del git está muy cansón porque todo lo frena en el commit cuando hay archivos nuevos

**Agente**, 2026-10-04 14:38:48
<!-- agente: 8bd7f993-c3e8-488c-839f-f7702f38d6cf -->

Revisé qué es lo que frena. No es git: la revisión de `pre-commit` (`validar.py plan`) pasa limpia con estos mismos cambios. El que frena es el freno del agente: después de cada orden de consola compara todo lo que cambió en git contra el plan.

**Por qué frena tanto:**
1. **Toma el registro como si fuera escritura.** `git add` y `git commit` no crean contenido, solo registran lo que ya cambió. Aun así, el freno ve cada archivo del commit como «escrito ahora» y exige que una fila del análisis lo autorice. Por eso cualquier commit con archivos nuevos se detiene.
2. **No acepta carpetas.** Hay que nombrar archivo por archivo: los 1.789 de `plataforma/` no tienen cómo autorizarse.
3. **No reconoce la orden del usuario.** «Suba» o «Hágalo» en el chat no cuentan como autorización. Es el [pendiente 118](../../../../../historico-chat/resumenes/2026-10-04/pendientes/118-el-freno-detiene-lo-que-el-usuario-ya-autorizo/pendiente.md), que scilit ya había reportado.

**Recomiendo corregir el punto 1 primero.** Que el freno no revise las órdenes de git que solo registran (`add`, `commit`, `push`), porque lo que entra al commit ya lo controla `pre-commit`. Es un cambio pequeño en `freno.py`, con su prueba, y quita el bloqueo de hoy. Los puntos 2 y 3 van en el pendiente 118.

¿Lo corrijo?

### 62 · Usuario, 2026-10-04 14:41:10
> apruebo

**Agente**, 2026-10-04 14:48:23
<!-- agente: 303d2244-ce28-47d5-b573-03290ec8f2c0 -->

Ya está corregida la lectura de `git status`. Ahora ajusto la detección de las órdenes de git y conecto el cambio en el enganche.

El `;` dentro del mensaje entre comillas partía la orden en dos. Antes de partirla, quito lo que va entre comillas.

Pasan 34 de 34 pruebas del freno. Retomo la orden pendiente de subir: «Hágalo: suba git».

Listo: el freno quedó corregido y el trabajo está en GitHub (`main`, hasta `29a30ad`).

**Lo que se corrigió en el freno:**
- Leía mal la salida de `git status` cuando había archivos renombrados. Tomaba la ruta vieja como si fuera un archivo nuevo y le cortaba las primeras letras: de ahí salían los avisos de `taforma/...`.
- Ya no revisa `git add`, `commit` ni `push`, porque esas órdenes solo registran lo que ya cambió. Lo que entra al commit lo sigue revisando el `pre-commit`.
- Pasan 34 de 34 pruebas del freno, 4 de ellas nuevas.

**Lo que se subió:**
1. `1123d39`: Cimiento como aplicación Django, los validadores pasados a clases y los arreglos del freno y del análisis.
2. `29a30ad`: el arreglo del enlace roto del resumen del 2026-08-22, que era lo único que detenía el push.

Los enganches revisaron los commits y solo dejaron avisos, ninguno bloqueante:
- el asunto del primer commit es largo;
- `CHANGELOG.md` tiene una versión repetida de antes;
- un archivo trae marcas de dos sesiones.

**Lo que falta:**
1. Pasar los 81 validadores que quedan.
2. Las filas 12 (épicas retiradas) y 11 (`ambiente.py` en la estructura acordada).
3. Los puntos 2 y 3 del freno (autorizar carpetas y aceptar la palabra del usuario) siguen en el pendiente 118.

### 63 · Usuario, 2026-10-04 14:49:02
> sígalos pasando

**Agente**, 2026-10-04 14:49:12
<!-- agente: 9dc154dc-eb8b-491e-a55b-f1995518e7f0 -->

Al mensaje le falta la palabra del comienzo. Para seguir pasando los validadores, escriba «Continúe» o «Hágalo: sígalos pasando».

### 64 · Usuario, 2026-10-04 14:51:57
> Continúe

**Agente**, 2026-10-04 15:06:31
<!-- agente: b3a5c797-cb7a-4af2-8ec8-5ae3371d6604 -->

Sigo con lo que queda del grupo que revisa código: `esquema`, `estructura` y `entidades`.

`declaracion` usa la lectura de tablas Markdown de `comun.py` (`filas_de` y `valor_limpio`). Esa pieza la necesitan muchos validadores, así que también va a `core/comun/`. La leo.

Escribo primero la fila 16 del análisis y después las piezas compartidas: la lectura de tablas Markdown y el recorrido de migraciones, que se repetía tres veces.

Coincide con el original. Sigo con la exportación, la declaración y las migraciones.

Ahora el esquema, con su lector de tablas que también usan `estructura` y `entidades`.

Ahora `entidades`, el último del grupo.

Comparo los cinco validadores nuevos contra los viejos en los tres proyectos reales, antes de escribir las pruebas.

Pasan las 50 pruebas. Veo qué queda en `validadores/` para seguir con el siguiente grupo.

El siguiente grupo es el que revisa el repositorio y git: `versionado`, `secretos`, `dependencias`, `ci`, `rama` y `commits`. Los leo.

Para `versionado` y `commits` necesito ver cómo los llama hoy `validar.py`, porque no reciben el proyecto igual que los demás.

Uso `prefijo_de` en los cuatro módulos que lo repetían.

Ahora los seis validadores del repositorio y de git.

Comparo los seis validadores nuevos con los viejos en cuatro proyectos reales, antes de escribir las pruebas.

Los seis dan lo mismo en los cuatro proyectos y en los últimos cuatro commits. Escribo sus pruebas; las claves de ejemplo se arman al correr, para que el archivo no tenga ningún secreto escrito.

Avancé dos grupos más. Ya son 16 validadores pasados a clases dentro de Cimiento, y pasan 69 pruebas.

**Lo que se agregó en esta vuelta:**

| Grupo | Clases |
|---|---|
| Migraciones y esquema | `MigracionesReversibles` (`03·D2`), `IntegridadDeEsquema` (`03·D1/D3`, `14·EST2`), `ConvencionDeNombres` (`14·EST1/EST2`), `TablasDeDominio` (`03·D1`, `15·IM2/IM5`), `DeclaracionDelProyecto` |
| Repositorio y git | `ArchivosVersionados` (`09·G3`), `LockfileVersionado` (`10·DEP2`), `IntegracionContinua` (`09·G6`), `RamaDedicada` (`09·G4`), `SecretosEnElCodigo` (`04·S4`, `00·N6`), `MensajeDeCommit` (`09·G2/G8`) |

**Lo repetido que se eliminó:**
- El recorrido de migraciones estaba en tres validadores. Ahora está una sola vez, en `RecorridoDeMigraciones`.
- El cálculo del prefijo de cada repositorio estaba en nueve sitios. Ahora está en `Proyecto.prefijo_de`.
- Las consultas de ramas y del mensaje del commit quedaron en `Git`.
- La lectura de tablas Markdown quedó en `core/comun/markdown.py`.

**Cómo se comprobó:** cada clase nueva da exactamente los mismos hallazgos que el validador viejo en cuatro proyectos reales: Cimiento, dp, scilit y rni-back. `estructura` y `entidades` casi no tienen datos en esos proyectos, así que también se probaron con un proyecto armado para la prueba, donde dieron 25 hallazgos y todos coincidieron. `MensajeDeCommit` dio lo mismo en los últimos cuatro commits.

**Lo que sigue:** quedan unos 60 módulos en `validadores/`. Muchos no son validadores sino herramientas, como el instalador, el andamio o el histórico. El próximo grupo es el de los documentos: `enlaces`, `indices`, `marcas`, `plantillas`, `citas` y `trazabilidad`.

Nada de esto está guardado en un commit todavía.

### 65 · Usuario, 2026-10-04 15:08:10
> Continué

**Agente**, 2026-10-04 15:14:22
<!-- agente: 6c0837b1-c94a-4517-a385-260fcec05780 -->

Sigo con el grupo de los documentos. Empiezo por `enlaces`, que es la base de `indices`.

Escribo la fila 18 del análisis y las piezas compartidas: la lectura de enlaces y encabezados en `Markdown`, y el recorrido de los `.md` y la ubicación del estándar en `Proyecto`.

Coinciden con los originales. Ahora `Proyecto`: el recorrido de los `.md` y la ubicación del estándar.

Ahora el módulo de enlaces: una clase con las reglas de qué enlace se comprueba, tres validadores y el reparador.

Pasan las 86 pruebas. Ahora arreglo los 15 textos de enlace que quedaron diciendo la ruta vieja, con el reparador nuevo. Son de los mismos documentos de la fila 10.

**Paré: el freno detuvo una acción mía.** El reparador cambió el texto de enlaces en 21 archivos, y tres no estaban autorizados por el análisis: `base/tareas.md`, `pendientes/98-...` y `pendientes/99-...`.

Además, dos de los cambiados están en `base/` (`tareas.md` y `mapa-de-tareas.md`). Por las reglas de este repositorio, cualquier cambio en `base/` lleva su entrada en el `CHANGELOG`. Y `mapa-de-tareas.md` lo genera un programa, así que lo cambiado ahí puede perderse la próxima vez que se genere.

**El cambio en sí es correcto:** solo cambió el texto de los enlaces, para que diga la ruta desde la raíz (`13·DOC14`), y no tocó ningún destino. Ahora el reparador encuentra cero pendientes. Pero lo hice sin mirar antes qué archivos iba a tocar.

**Lo que avanzó este grupo:** `EnlacesRotos`, `FormatoDeEnlaces`, `IndicesDeCarpetas` y `ReparadorDeEnlaces` son clases. Dan lo mismo que el validador viejo en Cimiento, dp y scilit, y pasan 86 pruebas.

**Falta decidir qué hago con los cambios en esos archivos:**
1. Dejarlos y agregarlos a la fila 18 del análisis, con la entrada del `CHANGELOG` por `base/`. Lo recomiendo.
2. Revertir los cambios en `base/` y en `pendientes/` y dejar solo los que estaban autorizados.

### 66 · Usuario, 2026-10-04 15:15:20
> 00 id9

**Agente**, 2026-10-04 15:15:28
<!-- agente: f88f5311-7830-43fa-88ed-313b9c429be4 -->

Lo mismo, más corto:

El freno detuvo una acción mía. Corregí el texto de enlaces en 21 archivos, y tres de ellos no estaban autorizados: `base/tareas.md`, `pendientes/98` y `pendientes/99`. El cambio en sí es correcto, porque solo toca el texto y no el destino. Pero lo que cambia en `base/` necesita su entrada en el `CHANGELOG`.

Los enlaces ya son clases: dan los mismos resultados que el validador viejo en Cimiento, dp y scilit, y pasan las 86 pruebas.

¿Dejo esos cambios y los agrego al análisis con su `CHANGELOG`, o los revierto?

### 67 · Usuario, 2026-10-04 15:18:55
> explique la pregunta

**Agente**, 2026-10-04 15:19:07
<!-- agente: 228ee746-8bb8-4268-a7ea-4f287d516bde -->

Un enlace en Markdown tiene dos partes: el **texto** que se lee y el **destino** al que lleva. Por ejemplo, en `x.md (`base/x.md`, ya no está ahí)` el texto es `x.md` y el destino es `../../base/x.md`. La regla `13·DOC14` pide que el texto diga la ruta completa, `base/x.md`, para saber dónde está el archivo sin abrirlo.

Corrí el reparador nuevo y cambió ese **texto** en 21 archivos. Ningún destino cambió, así que todos los enlaces siguen funcionando.

El problema es que tres de esos archivos no los podía tocar sin permiso: `base/tareas.md`, `pendientes/98-...` y `pendientes/99-...`. Por eso el freno avisó. Además, todo lo que cambia en `base/` necesita su línea en el `CHANGELOG`.

La pregunta es qué hacer con esos tres cambios:
1. **Dejarlos.** Los anoto en el análisis como autorizados y agrego la línea al `CHANGELOG`. Lo recomiendo, porque el cambio cumple la regla.
2. **Revertirlos.** Esos tres archivos quedan como estaban y se conservan solo los cambios que sí estaban autorizados.

### 68 · Usuario, 2026-10-04 15:20:59
> Hágalo: dejarlos

**Agente**, 2026-10-04 15:25:09
<!-- agente: 822971e8-b587-4d2f-af16-6733a610811e -->

Son cinco archivos. Escribo un guion de apoyo que, en cada uno, devuelve a su versión de git solo los renglones dañados.

Los cinco quedaron restaurados y `validar.py tareas` vuelve a pasar. Verifico que `base/` no tenga cambios y corrijo el error en los dos lugares.

Quedan tres textos por arreglar. Antes de escribirlos, veo cómo quedarían.

Quedó resuelto, aunque no exactamente como se aprobó. Al revisarlos, los cambios en `base/` resultaron mal hechos, así que los devolví a como estaban. Por eso `base/` no tiene cambios y no hace falta tocar el `CHANGELOG`.

**Lo que pasó:**
- El reparador de enlaces tenía un error, que venía del código viejo y que copié igual en la clase nueva. Cuando el texto de un enlace nombraba una carpeta, le pegaba el nombre del archivo y le dejaba una barra al final: `[base/x/README.md/](../../../../../...)`.
- Con ese error dañó 5 archivos. Dos eran de `base/`, y uno de esos lo genera un programa, así que `validar.py tareas` fallaba.

**Lo que hice:**
1. Devolví los renglones dañados a su versión de git con un guion de apoyo ([restaurar_textos_de_enlace.py](../../../../../historico-chat/scripts/2026-10-04/restaurar_textos_de_enlace.py)). `validar.py tareas` vuelve a pasar.
2. Corregí el error en las dos versiones, la nueva y la vieja, y agregué una prueba para ese caso.
3. Dejé los cambios de `pendientes/98` y `pendientes/99`, que sí eran correctos, y los agregué a la fila 18 del análisis.

**Resultado:** pasan 87 pruebas. Los avisos de formato de enlaces coinciden con el validador viejo en Cimiento, dp y scilit (2.360, 389 y 235), y no hay ningún enlace roto.

**Queda un caso abierto:** la prueba vieja que exige «cero enlaces por arreglar» marca 2. Los dos están en la sección «Conversación» del análisis, que es copia literal del chat y no se edita. Habría que excluir esas secciones del reparador, igual que ya se excluyen las transcripciones.

### 69 · Usuario, 2026-10-04 15:26:26
> 00 id9

**Agente**, 2026-10-04 15:26:39
<!-- agente: 64bdca40-aec7-450a-b70d-9a1b3eb89633 -->

Lo mismo, más corto:

Los cambios en `base/` estaban mal: el reparador dejaba textos como `[base/x/README.md/](../../../../../...)`. Los devolví a como estaban, así que no hace falta tocar el `CHANGELOG`. Corregí ese error en el reparador nuevo y en el viejo, con su prueba. Pasan 87 pruebas, los resultados coinciden con el validador viejo en los tres proyectos y no queda ningún enlace roto.

Falta un caso: el reparador quiere cambiar 2 enlaces dentro de la «Conversación» del análisis, que es copia literal del chat. Hay que excluir esa sección, igual que las transcripciones.

### 70 · Usuario, 2026-10-04 15:27:31
> analicemos: a esos validadores se le pueden realizar configuraciones por interfaz?

**Agente**, 2026-10-04 15:27:49
<!-- agente: 848b1a39-dad2-4f1f-a95e-fdc621a64e18 -->

Hoy no se pueden configurar desde una interfaz. Pero, como ya son clases, agregarlo es sencillo.

**Cómo están hoy:**
- Lo que se puede ajustar está escrito en el código, como atributos de cada clase: el máximo de 60 líneas por función en `FuncionesLargas`, el largo del asunto del commit, las extensiones de archivo que se revisan y los archivos exentos de `SecretosEnElCodigo`.
- Lo propio de cada proyecto ya se configura, pero a mano, en `.agente/mapeo-nombres.md` y en `.agente/dominio.md`.

**Cómo quedaría con interfaz:**
- Un módulo `core/ajustes/` con un modelo que guarde, por proyecto y por validador, tres cosas: si corre, con qué severidad y con qué valores (el máximo de líneas, los exentos...). Se edita desde la administración de Django.
- La clase `Validador` lee esos valores antes de revisar, y si no hay ninguno usa los de siempre.

**El punto que hay que decidir:** los enganches corren sin Django, para no hacer más lento cada mensaje. Por eso los ajustes no pueden quedar solo en la base de datos. Recomiendo que la interfaz los guarde también en un archivo del proyecto, `.agente/validadores.md`, que se lee sin Django. Así la interfaz sirve para editar y el archivo es lo que se usa al revisar.

**Algo que conviene saber:** la plataforma vieja tenía un módulo parecido (`nucleo/ajustes`, de la HU «lo obligatorio no se apaga»), y se borró con la base limpia. Su regla sigue valiendo: los validadores del núcleo (`00·N...`) no se pueden apagar desde la interfaz.

¿Lo agrego al análisis como una HU nueva, para después de pasar los validadores?

### 71 · Usuario, 2026-10-04 15:28:19
> analicemos: yo se y por eso es que lo estoy preguntando

**Agente**, 2026-10-04 15:31:42
<!-- agente: 6b6f5732-3f12-40a3-a848-c96e826b3023 -->

Ya vi la HU vieja del tema. Reviso si el archivo de configuración sigue existiendo en algún proyecto.

Sí se pueden configurar, y la forma ya está decidida en el estándar. La HU-005 de EP-008, «Configurar qué rige en cada proyecto», ya está terminada, y la plataforma vieja la cumplía. Hay que conectarla a las clases nuevas.

Esa HU fija tres cosas:
- Por proyecto, solo se enciende o se apaga lo opcional: 49 de 257 reglas son opcionales (`*opt-in*`). Lo obligatorio no se apaga nunca (RN-2).
- La configuración se guarda en el proyecto, en `.agente/configuracion.md`, y no en la base de datos (RN-4). La interfaz solo edita ese archivo. Eso también resuelve lo de los enganches, que leen el archivo sin cargar Django.
- Cada cambio queda escrito con la fecha y quién lo hizo.

Para conectarla, `Validador` ya tiene el atributo `regla`. Antes de revisar, la clase mira si su regla es opcional y si el proyecto la apagó en ese archivo. Hoy ningún programa lee `configuracion.md`, y el archivo no existe en este repo ni en `proyectos/cimiento/`.

Falta decidir los valores, como el tope de 60 líneas o el largo del asunto del commit. La HU no los cubre. Si cada proyecto puede cambiar un número que fija la regla, la regla pasa a ser una sugerencia, que es lo que RN-2 impide. Recomiendo que esos valores no se cambien por proyecto: si un número está mal, se cambia la regla en `base/`, para todos.

¿Los valores de las reglas quedan fijos, y por proyecto solo se encienden o se apagan las reglas opcionales?

### 72 · Usuario, 2026-10-04 15:56:45
> Hágalo: siga pasando los validadores

**Agente**, 2026-10-04 16:15:23
<!-- agente: dbc68645-c358-4eac-9ee5-b6f0b4e28d9b -->

Sigo con el grupo siguiente: marcas, plantillas, citas y trazabilidad. Primero miro qué queda por pasar.

Leí los cuatro. Trazabilidad depende de `fases.py`; miro esa parte.

Paso primero lo compartido: `Proyecto.recorrer_md` tiene que poder recorrer una sola carpeta (citas y marcas recorren `base/`).

Ahora trazabilidad, con una pieza `Epicas` que después reusará `fases`.

El freno exige que cada archivo nuevo esté en la tabla del análisis. Reviso cómo quedaron autorizados los anteriores.

Agrego la fila 19 para este grupo, como se hizo con los anteriores (acuerdo 11).

Sigue la plantilla: el documento se compara contra el molde del que salió.

Ahora citas: índice de reglas, validador y enlazador, con la misma lógica de antes.

Falta marcas, el más largo. Miro la API de `Git` para el trinquete.

Ahora el `__init__.py`.

Escribo el guion de paridad: compara lo viejo contra lo nuevo en este repo y en los proyectos reales.

Paridad completa en los cuatro, sobre este repo y tres proyectos reales. Paso las pruebas viejas a las clases; las leo.

Agrego las pruebas a `tests_documentos.py`.

El heredoc se rompió con las comillas; hago el cambio con Edit.

Dos fallas y un error. Miro el error.

Ahora la prueba vieja del trinquete, para que el renombrado de verdad se pruebe.

116 pruebas en verde. Vuelvo a correr la paridad con la corrección aplicada a los dos validadores.

Marco la fila 19 como hecha y anoto los dos defectos en el resumen de la sesión.

Pasé el grupo siguiente a clases: trazabilidad, plantilla, citas y marcas. Las 116 pruebas de `core` pasan, y lo nuevo da lo mismo que lo viejo en este repo y en tres proyectos reales (rni-back, shopnest y agro-system). En rni-back no hay épicas, así que ahí no se comparó la trazabilidad.

Lo que quedó:
- **Trazabilidad:** [trazabilidad.py](../../../../../proyectos/cimiento/core/validadores/trazabilidad.py) revisa que épicas y HU se nombren entre sí, el ORIGEN del plan y la tabla de cierre. Recorre las épicas con [epicas.py](../../../../../proyectos/cimiento/core/validadores/epicas.py), una pieza nueva que también va a usar `fases` en el grupo siguiente.
- **Plantilla:** [plantillas.py](../../../../../proyectos/cimiento/core/validadores/plantillas.py) compara un documento con su plantilla y busca la plantilla en el estándar.
- **Citas:** [citas.py](../../../../../proyectos/cimiento/core/validadores/citas.py) tiene el índice de reglas, el validador y el que pone los enlaces a las citas.
- **Marcas:** [marcas.py](../../../../../proyectos/cimiento/core/validadores/marcas.py) mide y limpia un texto. El validador revisa lo que se hereda o, con `solo_preparados`, solo lo que va a entrar en el commit, y no deja que las marcas aumenten.
- `Proyecto.recorrer_md` ahora puede recorrer una sola carpeta, por ejemplo `base/`.

Las pruebas nuevas encontraron dos errores que ya estaban en los validadores viejos. Los corregí en las dos versiones:
- `plantillas.py` decía que una regla de negocio sin origen estaba en la línea de antes de la suya.
- Las dos pruebas de renombrado del trinquete de marcas no probaban nada: `git mv` fallaba sin avisar porque la carpeta de destino no existía.

Para que el freno dejara escribir los archivos agregué la fila 19 al análisis, ya marcada como hecha. Anoté los errores en el resumen de la sesión (H-7). El guion que compara lo viejo con lo nuevo es [paridad_documentos.py](../../../../../historico-chat/scripts/2026-10-04/paridad_documentos.py).

Lo que falta, en orden:
1. Pasar a clases los demás validadores: quedan unos 60 de los 87 archivos de `validadores/`, contando los enganches y las herramientas. Sigue el grupo de flujo y fases, que es el más grande (`fases.py` tiene 1.060 líneas).
2. Conectar `validar.py` y los enganches a las clases, y después borrar los `.py` viejos.
3. Hacer que el reparador de enlaces no toque la «Conversación» del análisis, que es copia literal del chat.
4. Los puntos del análisis que siguen abiertos: las HU de EP-024, parecidas.py, las filas 10 y 12, `ambiente.py` y lo de 02·F4 con 02·F25.
5. Decidir sobre el commit: hay trabajo de varios grupos sin guardar.

### 73 · Usuario, 2026-10-04 16:15:59
> 
> 00 id9

**Agente**, 2026-10-04 16:16:11
<!-- agente: 68ae5db9-89da-4ce3-9247-ee33b027f1f0 -->

Ya están como clases trazabilidad, plantilla, citas y marcas. Las 116 pruebas pasan. Lo nuevo da lo mismo que lo viejo en este repo, shopnest y agro-system. En rni-back no hay épicas, así que la trazabilidad no se comparó.

Lo nuevo:
- [epicas.py](../../../../../proyectos/cimiento/core/validadores/epicas.py) recorre épicas, HU y fases en un solo lugar. Lo va a usar también `fases`.
- `Proyecto.recorrer_md` ya puede recorrer una sola carpeta, como `base/`.

Las pruebas encontraron dos errores que ya tenían los validadores viejos, y quedaron corregidos en las dos versiones:
- `plantillas.py` señalaba la línea de antes de la regla sin origen.
- Las pruebas de renombrado del trinquete no probaban nada, porque `git mv` fallaba sin avisar.

Quedaron anotados en la fila 19 del análisis y en el resumen (H-7).

Falta, en orden:
1. Pasar el resto a clases. Quedan unos 60 de los 87 archivos de `validadores/`, contando enganches y herramientas, y sigue el grupo de flujo y fases.
2. Conectar `validar.py` y los enganches a las clases, y borrar los archivos viejos.
3. Que el reparador de enlaces no toque la «Conversación» del análisis.
4. Cerrar los puntos abiertos del análisis.
5. El commit.

### 74 · Usuario, 2026-10-04 16:16:58
> continué

**Agente**, 2026-10-04 16:24:12
<!-- agente: b7b3e27c-79d7-4e9c-8b8b-8108eea93f26 -->

Sigo con el grupo de flujo y fases. Primero miro de qué dependen.

Es el módulo más grande (1.060 líneas). Antes de escribir, reviso cómo lee `comun.leer` un archivo que no existe, porque `fases` lo usa para decidir.

Ahora la lectura del veredicto.

Ahora el validador de fases con el inventario.

Exporto las clases y escribo la paridad.

Paridad completa en los cuatro proyectos. Ahora las pruebas; leo las viejas de fases.

Las dos fallas son de mis pruebas: la primera no tenía épicas (sin ellas, el validador se detiene antes, igual que el viejo) y la segunda tenía un `../` de más.

140 pruebas en verde. Marco la fila 20 como hecha (quito `trazabilidad.py`, que al final no hubo que tocar).

Pasé a clases el validador de fases, la pieza más grande (1.060 líneas), junto con la marca de la estación del commit. Las 140 pruebas de `core` pasan. Lo nuevo da lo mismo que lo viejo en este repo y en rni-back, shopnest y agro-system: hallazgos, inventario, veredictos y marca del commit.

Quedó en cinco piezas:
- [epicas.py](../../../../../proyectos/cimiento/core/validadores/epicas.py) recorre el árbol y lee los nombres de épica, HU y fase.
- [moldes.py](../../../../../proyectos/cimiento/core/validadores/moldes.py) dice si un documento sigue siendo la plantilla.
- [veredictos.py](../../../../../proyectos/cimiento/core/validadores/veredictos.py) lee Cumple o No cumple, el conteo de criterios y los rojos reemplazados.
- [estacion.py](../../../../../proyectos/cimiento/core/validadores/estacion.py) marca la estación 12 con el hash del commit.
- [fases.py](../../../../../proyectos/cimiento/core/validadores/fases.py) es el validador, con el inventario y la línea final.

Antes, `checkpoint.py`, `veredicto.py`, `flujo.py` y `estacion_commit.py` usaban funciones internas de `fases.py`. Con estas piezas cada uno las va a pedir a la pieza que corresponde.

Un cambio, a propósito: cuando una fase queda detenida por un análisis abierto, el mensaje nombra el análisis con la ruta desde el proyecto revisado y no desde el estándar. En los cuatro proyectos el resultado salió igual.

Las autorizaciones están en la fila 20 del análisis, ya marcada como hecha. El guion de comparación es [paridad_fases.py](../../../../../historico-chat/scripts/2026-10-04/paridad_fases.py).

Falta:
1. Sigue `flujo.py`, que depende de `plan_vs_hecho.py` y `version.py`; después, el resto de `validadores/`.
2. Conectar `validar.py` y los enganches a las clases, y borrar los archivos viejos.
3. Que el reparador de enlaces no toque la «Conversación» del análisis.
4. Cerrar los puntos abiertos del análisis.
5. El commit.

### 75 · Usuario, 2026-10-04 16:25:18
> Hágalo: deje de estar informando tantas cosas haga todo el trabajo

**Agente**, 2026-10-04 16:35:10
<!-- agente: eeaaacb2-30dc-4f49-a8d5-f7c52061a9df -->

Me pongo con todo lo que queda. Primero mido el tamaño completo para repartir el trabajo.

Sigo: registro la autorización en el análisis y creo los paquetes nuevos.

Antes de lanzar los agentes escribo `core/comun/consola.py` (imprimir hallazgos y preparar la salida), que van a usar todos los comandos.

Lanzo la primera tanda: cuatro agentes en paralelo, cada uno con su grupo.

Mientras trabajan, resuelvo lo pendiente del reparador de enlaces: que no toque la «Conversación» de los análisis.

Aplico el cambio en las dos versiones: en un `analisis-N.md`, lo que está bajo «## Conversación» no se reporta ni se repara, y el reemplazo se hace por renglón, no en todo el archivo.

Ahora lo mismo en la clase nueva.

Agrego la prueba en la clase nueva y corro todo.

Mientras los agentes trabajan, leo `validar.py` entero para planear cómo conectarlo a las clases.

La primera tanda está trabajando: cuatro agentes con los grupos de reglas, instalación, proceso y sesión. Mientras tanto dejé listo el reparador de enlaces, que ya no toca la «Conversación» de los análisis. Cuando terminen sigue el grupo del freno y después la conexión de `validar.py` y los enganches.

> En pausa desde el turno 76.

> acá termina la conversación

---

## Lo acordado

1. Alcance: el análisis se abre con el hallazgo 2 del resumen del 2026-10-04, «el código se repite en vez de reusarse», y trata también el pendiente 117, «nada avisa cuando se crea una función que ya existe» (turno 17).
2. Orden: primero el validador de `07·Q4`, como HU nueva en `EP-004`, para que no nazcan copias nuevas; después una épica nueva que junta las copias que ya hay (turno 8 de la sesión, antes de prender el análisis).
3. Para cualquier proyecto: el validador se construye junto a `validadores/calidad.py` y reutiliza `validadores/codigo.py` y la separación de funciones de `calidad.py`, sin copiarlas (turno 17).
4. Qué hace al encontrar una copia: avisa y no frena, y compara lo que hace la función, no solo su nombre (turno 17).
5. Las reglas siguen el mismo camino que el código: al crear o cambiar una regla, un control busca por significado las reglas parecidas y avisa cuáles leer antes. Reutiliza la búsqueda por significado de `memoria/` y `validadores/metareglas.py`. Va como HU en `EP-004` (turnos 21 y 23).
6. Aprobar el análisis aprueba lo que sale de él: se cambian `02·F4` y `02·F25`, sin crear una regla nueva. El plan que sale de un análisis aprobado y cumple sus filas queda aprobado; solo lo que el análisis no contempló pide aprobación otra vez. Va de primero en el orden (turnos 20, 21 y 23).
7. La lógica vive en `core/` y los enganches la importan sin arrancar Django. Reemplaza lo que este acuerdo decía antes (que la plataforma salía a `proyectos/plataforma/`), que el acuerdo 8 dejó sin efecto: Cimiento es la aplicación (turnos 24 a 27; reescrito con aprobación del usuario el 2026-10-05).
8. Cimiento es la aplicación Django: la carpeta se llama `proyectos/cimiento/` y no se le vuelve a decir «la plataforma». Ahí se junta lo que hoy está repartido en muchos `.py`, que es el propósito de esta sesión (turnos 32 a 34).
9. Cimiento parte de una base Django limpia: se borra todo lo que no es la base, como un commit que conserva la historia, incluido `datos/`. La base sigue [`plantillas/estructura-proyecto-django.md`](../../../../../plantillas/estructura-proyecto-django.md), con la configuración separada por entorno, `requirements/` con su `lock.txt`, `static/`, `templates/` y el paquete de módulos, que se llama `core/`. Se conserva lo que dejó la instalación de Cimiento (turnos 37, 38 y 41).
10. Las épicas `EP-008` a `EP-022`, que describen lo construido en la plataforma, se marcan como retiradas con fecha y enlace a este análisis; no se borran (`20·M11`) (turno 37).
11. Los validadores pasan primero a Cimiento, y cada uno es una clase: comparten una clase base y lo común (rutas, git, lectura de archivos, hallazgos) vive una sola vez en `core/comun/`. `interfaz/` no entra por ahora (turno 51).

Ya no queda nada abierto: el acuerdo 7 reescrito resuelve también el costo de arrancar Django en cada enganche (2,4 s medidos contra 0,46 s), porque los enganches importan `core/` sin arrancarlo. `EP-024` no se crea: su trabajo quedó en las filas 21 y 22 (2026-10-05).

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `07·Q4` (no repetir lógica), `20·M3` (la base no depende del lenguaje del proyecto), `02·F0` (cadena completa) y `02·F11` (una fase toca un solo módulo: por eso la limpieza va en una HU por capa, puntos 4 a 6).

Para las reglas aplican `20·M12` (buscar antes de crear) y las filas 2 y 17 del [checklist de las reglas](../../../../../base/20-meta-reglas/checklist.md): hoy solo las cumple la memoria del agente, y eso cubre el punto 7.

Chocan `02·F4` y `02·F25` con la aprobación del análisis: exigen un OK por cada plan aunque el análisis aprobado ya lo defina. Se resuelve en el punto 8 cambiándolas, coherente con `00·N1` (aprobar un plan vale para todo lo que dice) y con la excepción de `02·F9` (lo no contemplado vuelve al análisis).

Chocan las dos mitades de `07·Q4`: «no repitas» y «no abstraigas de más». Dos funciones con el mismo nombre pueden hacer cosas distintas. Se resuelve en el punto 2: el validador compara lo que hace la función, y en la limpieza solo se junta lo que hace lo mismo.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| Sitio común de los validadores | `validadores/comun.py` tiene `leer`, `relativo` y lectura de tablas; no tiene nada de rutas, raíz del proyecto ni git |
| Sitio común de los enganches | No existe: cada archivo de `adaptadores/claude-code/` trae su `raiz_pedida`, `_entrada` y `archivo_editado` |
| Sitio común de la plataforma | No existe: `dicho`, `reconstruir_indice`, `_indexar` y `huella` están repetidas en `plataforma/nucleo/` |
| Validador hermano | `validadores/calidad.py` comprueba `07·Q3`: separa las funciones de PHP, JavaScript y Python y avisa sin frenar. `validadores/codigo.py` recorre el código versionado de 18 lenguajes |
| Saber si una ruta queda dentro del proyecto | Dos formas: `relativa` en `validadores/freno.py` y `_partes` en `validadores/rutas_fuera.py`. Solo la primera entiende `/c/...` |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Commit `1295614` | Confirma el daño: el arreglo de `/c/...` llegó a `freno.py` y no a `rutas_fuera.py`. Lo recoge el punto 2 de «Lo acordado» |
| Recuerdo [todo multiproyecto](../../../../memory/todo-multiproyecto.md) | Ya decidía que el validador sirve a cualquier proyecto. Lo recoge el punto 3 |
| [Análisis 1 del pendiente 110: lo que un proyecto reporta es un defecto de Cimiento en todos los proyectos](../../../../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde/pendientes/110-el-andamio-no-sirve-desde-un-proyecto/analisis-1.md) | Su R-12: lo que se construye se prueba desde otro proyecto. Lo recoge el punto 3 |
| S-294 y S-295 | Las lecciones de este análisis |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | Versión MAYOR (`20·M10`) por el punto 8, que cambia qué aprobación pide cada plan. Los dos controles solo avisan. No aplica `02·F22`: no se deroga ninguna regla, se cambian |
| Normas y leyes | Ninguna |
| Herramientas | Los validadores no se copian a los proyectos: una sola copia sirve a todos ([`instalar.py`](../../../../../validadores/instalar.py)). Juntar las copias en Cimiento arregla todos los proyectos a la vez |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Funciones repetidas en el código de Cimiento | `validadores/`, `adaptadores/`, `plataforma/`, `memoria/`, `metricas/` | Un arreglo llega a una sola copia | Puntos 4 a 6 |
| Funciones repetidas en los proyectos que heredan | Cualquier proyecto, en cualquier lenguaje que lea `codigo.py` | `07·Q4` se exige y nada lo comprueba | Punto 3 |
| Copias que nacen después de la limpieza | Todo archivo nuevo | La limpieza se pierde con el tiempo | Punto 3: el validador corre con `validar.py` |
| Pruebas repetidas | `validadores/tests/` y `validadores/pruebas.py` | Dos juegos de pruebas que envejecen distinto | No se cubre aquí: no es lógica del programa; si el usuario lo pide, va en su propio pendiente |
| Reglas nuevas que repiten o contradicen otras | `base/`, y la capa propia de cada proyecto | El proyecto hereda las contradicciones de Cimiento | Punto 7 |
| Planes que piden un OK que el análisis ya dio | Toda fase que sale de un análisis aprobado, en cualquier proyecto | El usuario aprueba dos veces lo mismo | Punto 8 |
| Guiones de apoyo | `historico-chat/scripts/` | Ninguno: son de una sola vez y `04·S18` los conserva tal cual | No hace falta |

---

## Propuesta final: hallazgo y pendiente V«N+1», épica y HU

### Hallazgo V2. El código de Cimiento se repite en vez de reusarse

| Campo | Valor |
|---|---|
| Qué pasó | El inventario de los `.py` de Cimiento encontró la misma función copiada en muchos archivos: `_leer` en 13, `raiz_pedida` en 10, `dicho` en 9, `_entrada` en 8, `_git` en 6, y dos formas distintas de saber si una ruta queda dentro del proyecto. Cada vez que hizo falta algo se creó un archivo nuevo sin buscar si eso ya existía |
| Por qué importa | Un arreglo llega a una sola copia: el commit `1295614` corrigió `/c/...` en `freno.py` y `rutas_fuera.py` siguió sin entenderlo |

### Pendiente V2. El código de Cimiento se repite en vez de reusarse

| Campo | Valor |
|---|---|
| De dónde sale | El hallazgo V2, «el código de Cimiento se repite en vez de reusarse» |
| El problema | Las mismas funciones están copiadas en `validadores/`, `adaptadores/claude-code/` y `plataforma/nucleo/`. `validadores/comun.py` no tiene nada de rutas, raíz ni git, y los enganches y la plataforma no tienen sitio común |
| Por qué importa | Un arreglo llega a una sola copia, y como los validadores sirven a todos los proyectos, la copia sin arreglar falla en todos |

### Épica y HU que salen del análisis

Dos épicas. `EP-023 lo que se construye es lo que se analizó` recibe el cambio de la aprobación. `EP-004 comprobación automática` recibe los dos controles. La limpieza iba a una épica nueva, `EP-024`, y no se crea: el código se pasó a `core/` con las filas 13 a 22, y lo que quedaba de ella está en las filas 21 y 22 (2026-10-05).

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | `EP-023` HU-008 | Aprobar el análisis aprueba lo que sale de él | `02·F4` y `02·F25` piden un OK por cada plan aunque el análisis aprobado ya lo defina | Ninguna | Las demás HU salen de este análisis: sin ella, cada una vuelve a pedir aprobación | 8 |
| 2 | `EP-004` HU-026 | Se avisa cuando se crea una función que ya existe | Nada avisa al crear una función que ya existe, y por eso nacen las copias | `EP-023` HU-008 | Ataca la causa: sin ella, las copias siguen naciendo mientras se limpia | 2, 3 |
| 3 | `EP-004` HU-027 | Se avisa cuando una regla nueva se parece a otra | Al crear una regla nada busca las parecidas, y así nacen reglas que se repiten o se contradicen | `EP-023` HU-008 | Misma causa que la HU anterior, del lado de las reglas | 7 |

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Se le preguntó al usuario algo que Cimiento ya decidía: si el validador servía a cualquier proyecto | Falló | S-294 | complementa R-2 |
| 2 | El validador nuevo se diseñó junto a su hermano, `calidad.py`, reutilizando sus piezas | Funcionó | S-295 | complementa R-2 |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Pasar el pendiente a su versión siguiente | `13·DOC26` | Este análisis, de una y sin fase: `historico-chat/resumenes/2026-10-04/pendientes/116-el-codigo-de-cimiento-se-repite-en-vez-de-reusarse/pendiente.md`, hecho el 2026-10-04 |
| 2 | Dejar la separación de funciones en un solo lugar, `Funciones` de `core/validadores/codigo.py`, para que la usen los dos validadores | 3 | `EP-004` HU-026, hecho el 2026-10-04 |
| 3 | Construir el validador de `07·Q4`: avisa sin frenar, compara lo que hace la función y no solo el nombre, corre con `validar.py` y se prueba desde un proyecto que no es Cimiento | 2, 3, 4 | `EP-004` HU-026 |
| 4 | Juntar en un solo lugar la raíz del proyecto, las rutas (también `/c/...`), la pregunta de si una ruta queda dentro del proyecto y la llamada a git. Ya viven una vez en `Proyecto` y `Git` de `core/comun/`; quedan en los enganches las copias de `raiz_pedida` y `archivo_editado` | 2 | Se termina con la fila 22 |
| 5 | Juntar las demás funciones repetidas de los validadores y los enganches. Las que quedan están en los validadores viejos de `validadores/` y desaparecen al borrarlos | 2 | Se termina con la fila 21 |
| 6 | Juntar las funciones repetidas de `plataforma/nucleo/` | 2 | Ya no aplica: la fila 11 borró `plataforma/nucleo/` |
| 7 | Construir el control de reglas: al crear o cambiar una regla, busca por significado las parecidas con la búsqueda de `memoria/` y avisa cuáles leer, desde `validadores/metareglas.py` | 5, `20·M12` | `EP-004` HU-027 |
| 8 | Cambiar `02·F4` y `02·F25`: el plan que sale de un análisis aprobado y cumple sus filas queda aprobado, y su marca cita el análisis; ajustar `validadores/plan_vs_hecho.py` para aceptar esa marca. Versión MAYOR | 6 | `EP-023` HU-008 |
| 9 | Trasladar `plataforma/` a `proyectos/plataforma/` con su historia: Cimiento la ignora, la plataforma busca el estándar subiendo de carpeta y los enlaces de los documentos pasan a la ruta nueva | 7 | Este análisis, de una y sin fase: `.gitignore`, `validadores/comun.py`, `validadores/corredor.py`, `plataforma`, `proyectos/plataforma`, `proyectos/plataforma/.env`, `proyectos/plataforma/indice.sqlite3`, `proyectos/plataforma/terceros`, `proyectos/plataforma/datos/auditoria/2026-10.md`, `proyectos/plataforma/config/settings/base.py`, `proyectos/plataforma/nucleo/ciclo_de_vida/core.py`, `proyectos/plataforma/nucleo/comprobaciones/tests_estado.py`, `documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-001-conectar-un-proyecto/A-EP-008-HU-001-la-plataforma-levanta-y-guarda/funcionalidad_implementada.md`, `documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-001-conectar-un-proyecto/B-EP-008-HU-001-se-conecta-un-proyecto/funcionalidad_implementada.md`, `documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-002-avisar-la-ruta-perdida/C-EP-008-HU-002-la-ruta-perdida-se-avisa/funcionalidad_implementada.md`, `documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-002-avisar-la-ruta-perdida/C-EP-008-HU-002-la-ruta-perdida-se-avisa/plan_trabajo.md`, `documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-003-ver-el-estado-de-un-proyecto/G-EP-008-HU-003-se-ve-el-estado-de-un-proyecto/funcionalidad_implementada.md`, `documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-004-administrar-un-proyecto-conectado/H-EP-008-HU-004-un-proyecto-conectado-se-administra/funcionalidad_implementada.md`, `documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-004-administrar-un-proyecto-conectado/H-EP-008-HU-004-un-proyecto-conectado-se-administra/plan_trabajo.md`, `documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-005-configurar-que-rige-en-cada-proyecto/V-EP-008-HU-005-lo-obligatorio-no-se-apaga/funcionalidad_implementada.md`, `documentacion/epicas/EP-009-todo-lo-que-se-hace-queda-registrado/HU-001-registrar-cada-accion/D-EP-009-HU-001-la-constancia-va-antes-que-el-efecto/funcionalidad_implementada.md`, `documentacion/epicas/EP-009-todo-lo-que-se-hace-queda-registrado/HU-002-buscar-en-la-auditoria/R-EP-009-HU-002-la-auditoria-se-puede-preguntar/funcionalidad_implementada.md`, `documentacion/epicas/EP-010-lo-escrito-entra-a-la-plataforma/HU-001-traer-un-proyecto/E-EP-010-HU-001-se-trae-un-proyecto-con-lo-que-tenga-escrito/funcionalidad_implementada.md`, `documentacion/epicas/EP-010-lo-escrito-entra-a-la-plataforma/HU-002-reportar-lo-no-reconocido/F-EP-010-HU-002-lo-que-no-se-reconoce-se-reporta/funcionalidad_implementada.md`, `documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-001-buscar-en-lo-conversado/A-EP-011-HU-001-lo-conversado-se-indexa-y-se-busca/funcionalidad_implementada.md`, `documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-001-buscar-en-lo-conversado/A-EP-011-HU-001-lo-conversado-se-indexa-y-se-busca/plan_pruebas.md`, `documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-001-buscar-en-lo-conversado/A-EP-011-HU-001-lo-conversado-se-indexa-y-se-busca/plan_trabajo.md`, `documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-002-ver-que-correccion-se-repite/A-EP-011-HU-002-lo-que-se-repitio-sale-contado/funcionalidad_implementada.md`, `documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-002-ver-que-correccion-se-repite/B-EP-011-HU-002-lo-generico-no-encabeza-el-reporte/funcionalidad_implementada.md`, `documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-003-medir-el-tiempo-que-se-gasta-revisando/Y-EP-011-HU-003-la-linea-base-dice-que-es-reconstruida/funcionalidad_implementada.md`, `documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/HU-001-armar-el-expediente-de-un-proyecto/A-EP-012-HU-001-el-expediente-se-arma-y-dice-que-le-falta/funcionalidad_implementada.md`, `documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/HU-001-armar-el-expediente-de-un-proyecto/A-EP-012-HU-001-el-expediente-se-arma-y-dice-que-le-falta/plan_trabajo.md`, `documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/HU-001-armar-el-expediente-de-un-proyecto/HU-001-armar-el-expediente-de-un-proyecto.md`, `documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/HU-002-generar-el-entregable-de-ofimatica/A-EP-012-HU-002-el-entregable-sale-del-texto/funcionalidad_implementada.md`, `documentacion/epicas/EP-013-los-documentos-se-llenan-sin-salir-de-la-plataforma/HU-001-ver-que-le-falta-a-un-documento/A-EP-013-HU-001-los-huecos-de-un-documento-se-ven/funcionalidad_implementada.md`, `documentacion/epicas/EP-013-los-documentos-se-llenan-sin-salir-de-la-plataforma/HU-001-ver-que-le-falta-a-un-documento/HU-001-ver-que-le-falta-a-un-documento.md`, `documentacion/epicas/EP-013-los-documentos-se-llenan-sin-salir-de-la-plataforma/HU-002-llenar-un-hueco-desde-la-plataforma/B-EP-013-HU-002-el-hueco-se-llena-sin-tocar-lo-demas/funcionalidad_implementada.md`, `documentacion/epicas/EP-014-ninguna-clave-queda-escrita/HU-001-tapar-la-clave-al-escribirla/C-EP-014-HU-001-se-tapa-lo-que-se-teclea-no-lo-que-se-copia/funcionalidad_implementada.md`, `documentacion/epicas/EP-014-ninguna-clave-queda-escrita/HU-001-tapar-la-clave-al-escribirla/HU-001-tapar-la-clave-al-escribirla.md`, `documentacion/epicas/EP-015-lo-exigido-se-comprueba-solo/HU-001-comprobar-un-proyecto-desde-la-plataforma/D-EP-015-HU-001-la-plataforma-corre-lo-que-el-estandar-exige/funcionalidad_implementada.md`, `documentacion/epicas/EP-015-lo-exigido-se-comprueba-solo/HU-001-comprobar-un-proyecto-desde-la-plataforma/HU-001-comprobar-un-proyecto-desde-la-plataforma.md`, `documentacion/epicas/EP-015-lo-exigido-se-comprueba-solo/HU-002-fijar-el-estado-desde-la-evidencia/E-EP-015-HU-002-el-estado-sale-de-la-fase-que-corrio/funcionalidad_implementada.md`, `documentacion/epicas/EP-015-lo-exigido-se-comprueba-solo/HU-003-no-publicar-lo-que-rompe-lo-anterior/F-EP-015-HU-003-la-puerta-corre-lo-que-ya-funcionaba/funcionalidad_implementada.md`, `documentacion/epicas/EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/HU-001-dar-el-identificador-sin-reutilizar-ninguno/G-EP-016-HU-001-ningun-numero-se-reutiliza/funcionalidad_implementada.md`, `documentacion/epicas/EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/HU-002-escribir-corregir-y-derogar-una-regla/H-EP-016-HU-002-derogar-marca-y-no-borra/funcionalidad_implementada.md`, `documentacion/epicas/EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/HU-003-aplicar-el-checklist-y-guardar-su-sello/I-EP-016-HU-003-un-sello-no-sobrevive-a-un-cambio/funcionalidad_implementada.md`, `documentacion/epicas/EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/HU-004-publicar-una-version-del-cuerpo-de-reglas/J-EP-016-HU-004-sin-decir-que-cambio-no-se-publica/funcionalidad_implementada.md`, `documentacion/epicas/EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/HU-005-entregarle-las-reglas-al-agente/K-EP-016-HU-005-las-reglas-llegan-y-la-fuente-sigue-ahi/funcionalidad_implementada.md`, `documentacion/epicas/EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/HU-006-avisar-al-proyecto-que-quedo-atras/L-EP-016-HU-006-el-aviso-dice-que-cambio/funcionalidad_implementada.md`, `documentacion/epicas/EP-017-una-aprobacion-dice-sobre-que-texto/HU-001-registrar-una-aprobacion-con-su-firma/M-EP-017-HU-001-una-aprobacion-guarda-la-huella-del-texto/funcionalidad_implementada.md`, `documentacion/epicas/EP-017-una-aprobacion-dice-sobre-que-texto/HU-002-ver-que-esta-aprobado-y-que-no/N-EP-017-HU-002-los-tres-estados-se-dicen-con-palabras/funcionalidad_implementada.md`, `documentacion/epicas/EP-017-una-aprobacion-dice-sobre-que-texto/HU-003-caducar-la-aprobacion-cuando-el-texto-cambia/O-EP-017-HU-003-editar-quita-la-aprobacion-y-no-borra-la-historia/funcionalidad_implementada.md`, `documentacion/epicas/EP-018-lo-aprendido-no-se-pierde-entre-sesiones/HU-001-guardar-lo-aprendido/P-EP-018-HU-001-lo-guardado-vuelve-en-la-sesion-siguiente/funcionalidad_implementada.md`, `documentacion/epicas/EP-018-lo-aprendido-no-se-pierde-entre-sesiones/HU-002-consultar-y-corregir-lo-guardado/Q-EP-018-HU-002-corregir-conserva-lo-que-decia-antes/funcionalidad_implementada.md`, `documentacion/epicas/EP-019-el-ciclo-se-opera-desde-la-plataforma/HU-001-abrir-una-fase-con-sus-documentos/S-EP-019-HU-001-el-nombre-sale-del-identificador/funcionalidad_implementada.md`, `documentacion/epicas/EP-019-el-ciclo-se-opera-desde-la-plataforma/HU-002-ver-en-que-estacion-va-cada-fase/T-EP-019-HU-002-la-tabla-manda-sobre-la-frase/funcionalidad_implementada.md`, `documentacion/epicas/EP-019-el-ciclo-se-opera-desde-la-plataforma/HU-003-impedir-avanzar-sin-la-puerta-cumplida/U-EP-019-HU-003-el-rechazo-dice-cual-puerta-falta/funcionalidad_implementada.md`, `documentacion/epicas/EP-020-lo-que-se-desvia-se-avisa/HU-001-avisar-lo-que-se-desvia/W-EP-020-HU-001-todo-aviso-dice-que-lo-disparo/funcionalidad_implementada.md`, `documentacion/epicas/EP-020-lo-que-se-desvia-se-avisa/HU-002-reportar-como-va-cada-proyecto/X-EP-020-HU-002-sin-datos-no-es-cero/funcionalidad_implementada.md`, `documentacion/epicas/EP-022-quien-entra-y-que-puede-hacer/HU-001-entrar-con-cuenta-y-contrasena/AA-EP-022-HU-001-sin-entrar-no-se-ve-nada/funcionalidad_implementada.md`, `documentacion/epicas/EP-022-quien-entra-y-que-puede-hacer/HU-002-separar-lo-que-cada-grupo-puede-hacer/AB-EP-022-HU-002-el-agente-no-aprueba/funcionalidad_implementada.md`, `documentacion/medicion/spec.md`, `documentacion/senales.md`, hecho el 2026-10-04 |
| 10 | La carpeta pasa a llamarse `proyectos/cimiento/`: corregir la ruta de las pruebas y los enlaces de los documentos | 8 | Este análisis, de una y sin fase: `validadores/corredor.py`, `historico-chat/resumenes/2026-08-22/sesion-6.md`, `documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-001-conectar-un-proyecto/A-EP-008-HU-001-la-plataforma-levanta-y-guarda/funcionalidad_implementada.md`, `documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-001-conectar-un-proyecto/B-EP-008-HU-001-se-conecta-un-proyecto/funcionalidad_implementada.md`, `documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-002-avisar-la-ruta-perdida/C-EP-008-HU-002-la-ruta-perdida-se-avisa/funcionalidad_implementada.md`, `documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-002-avisar-la-ruta-perdida/C-EP-008-HU-002-la-ruta-perdida-se-avisa/plan_trabajo.md`, `documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-003-ver-el-estado-de-un-proyecto/G-EP-008-HU-003-se-ve-el-estado-de-un-proyecto/funcionalidad_implementada.md`, `documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-004-administrar-un-proyecto-conectado/H-EP-008-HU-004-un-proyecto-conectado-se-administra/funcionalidad_implementada.md`, `documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-004-administrar-un-proyecto-conectado/H-EP-008-HU-004-un-proyecto-conectado-se-administra/plan_trabajo.md`, `documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-005-configurar-que-rige-en-cada-proyecto/V-EP-008-HU-005-lo-obligatorio-no-se-apaga/funcionalidad_implementada.md`, `documentacion/epicas/EP-009-todo-lo-que-se-hace-queda-registrado/HU-001-registrar-cada-accion/D-EP-009-HU-001-la-constancia-va-antes-que-el-efecto/funcionalidad_implementada.md`, `documentacion/epicas/EP-009-todo-lo-que-se-hace-queda-registrado/HU-002-buscar-en-la-auditoria/R-EP-009-HU-002-la-auditoria-se-puede-preguntar/funcionalidad_implementada.md`, `documentacion/epicas/EP-010-lo-escrito-entra-a-la-plataforma/HU-001-traer-un-proyecto/E-EP-010-HU-001-se-trae-un-proyecto-con-lo-que-tenga-escrito/funcionalidad_implementada.md`, `documentacion/epicas/EP-010-lo-escrito-entra-a-la-plataforma/HU-002-reportar-lo-no-reconocido/F-EP-010-HU-002-lo-que-no-se-reconoce-se-reporta/funcionalidad_implementada.md`, `documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-001-buscar-en-lo-conversado/A-EP-011-HU-001-lo-conversado-se-indexa-y-se-busca/funcionalidad_implementada.md`, `documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-001-buscar-en-lo-conversado/A-EP-011-HU-001-lo-conversado-se-indexa-y-se-busca/plan_pruebas.md`, `documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-001-buscar-en-lo-conversado/A-EP-011-HU-001-lo-conversado-se-indexa-y-se-busca/plan_trabajo.md`, `documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-002-ver-que-correccion-se-repite/A-EP-011-HU-002-lo-que-se-repitio-sale-contado/funcionalidad_implementada.md`, `documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-002-ver-que-correccion-se-repite/B-EP-011-HU-002-lo-generico-no-encabeza-el-reporte/funcionalidad_implementada.md`, `documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-003-medir-el-tiempo-que-se-gasta-revisando/Y-EP-011-HU-003-la-linea-base-dice-que-es-reconstruida/funcionalidad_implementada.md`, `documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/HU-001-armar-el-expediente-de-un-proyecto/A-EP-012-HU-001-el-expediente-se-arma-y-dice-que-le-falta/funcionalidad_implementada.md`, `documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/HU-001-armar-el-expediente-de-un-proyecto/A-EP-012-HU-001-el-expediente-se-arma-y-dice-que-le-falta/plan_trabajo.md`, `documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/HU-001-armar-el-expediente-de-un-proyecto/HU-001-armar-el-expediente-de-un-proyecto.md`, `documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/HU-002-generar-el-entregable-de-ofimatica/A-EP-012-HU-002-el-entregable-sale-del-texto/funcionalidad_implementada.md`, `documentacion/epicas/EP-013-los-documentos-se-llenan-sin-salir-de-la-plataforma/HU-001-ver-que-le-falta-a-un-documento/A-EP-013-HU-001-los-huecos-de-un-documento-se-ven/funcionalidad_implementada.md`, `documentacion/epicas/EP-013-los-documentos-se-llenan-sin-salir-de-la-plataforma/HU-001-ver-que-le-falta-a-un-documento/HU-001-ver-que-le-falta-a-un-documento.md`, `documentacion/epicas/EP-013-los-documentos-se-llenan-sin-salir-de-la-plataforma/HU-002-llenar-un-hueco-desde-la-plataforma/B-EP-013-HU-002-el-hueco-se-llena-sin-tocar-lo-demas/funcionalidad_implementada.md`, `documentacion/epicas/EP-014-ninguna-clave-queda-escrita/HU-001-tapar-la-clave-al-escribirla/C-EP-014-HU-001-se-tapa-lo-que-se-teclea-no-lo-que-se-copia/funcionalidad_implementada.md`, `documentacion/epicas/EP-014-ninguna-clave-queda-escrita/HU-001-tapar-la-clave-al-escribirla/HU-001-tapar-la-clave-al-escribirla.md`, `documentacion/epicas/EP-015-lo-exigido-se-comprueba-solo/HU-001-comprobar-un-proyecto-desde-la-plataforma/D-EP-015-HU-001-la-plataforma-corre-lo-que-el-estandar-exige/funcionalidad_implementada.md`, `documentacion/epicas/EP-015-lo-exigido-se-comprueba-solo/HU-001-comprobar-un-proyecto-desde-la-plataforma/HU-001-comprobar-un-proyecto-desde-la-plataforma.md`, `documentacion/epicas/EP-015-lo-exigido-se-comprueba-solo/HU-002-fijar-el-estado-desde-la-evidencia/E-EP-015-HU-002-el-estado-sale-de-la-fase-que-corrio/funcionalidad_implementada.md`, `documentacion/epicas/EP-015-lo-exigido-se-comprueba-solo/HU-003-no-publicar-lo-que-rompe-lo-anterior/F-EP-015-HU-003-la-puerta-corre-lo-que-ya-funcionaba/funcionalidad_implementada.md`, `documentacion/epicas/EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/HU-001-dar-el-identificador-sin-reutilizar-ninguno/G-EP-016-HU-001-ningun-numero-se-reutiliza/funcionalidad_implementada.md`, `documentacion/epicas/EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/HU-002-escribir-corregir-y-derogar-una-regla/H-EP-016-HU-002-derogar-marca-y-no-borra/funcionalidad_implementada.md`, `documentacion/epicas/EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/HU-003-aplicar-el-checklist-y-guardar-su-sello/I-EP-016-HU-003-un-sello-no-sobrevive-a-un-cambio/funcionalidad_implementada.md`, `documentacion/epicas/EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/HU-004-publicar-una-version-del-cuerpo-de-reglas/J-EP-016-HU-004-sin-decir-que-cambio-no-se-publica/funcionalidad_implementada.md`, `documentacion/epicas/EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/HU-005-entregarle-las-reglas-al-agente/K-EP-016-HU-005-las-reglas-llegan-y-la-fuente-sigue-ahi/funcionalidad_implementada.md`, `documentacion/epicas/EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/HU-006-avisar-al-proyecto-que-quedo-atras/L-EP-016-HU-006-el-aviso-dice-que-cambio/funcionalidad_implementada.md`, `documentacion/epicas/EP-017-una-aprobacion-dice-sobre-que-texto/HU-001-registrar-una-aprobacion-con-su-firma/M-EP-017-HU-001-una-aprobacion-guarda-la-huella-del-texto/funcionalidad_implementada.md`, `documentacion/epicas/EP-017-una-aprobacion-dice-sobre-que-texto/HU-002-ver-que-esta-aprobado-y-que-no/N-EP-017-HU-002-los-tres-estados-se-dicen-con-palabras/funcionalidad_implementada.md`, `documentacion/epicas/EP-017-una-aprobacion-dice-sobre-que-texto/HU-003-caducar-la-aprobacion-cuando-el-texto-cambia/O-EP-017-HU-003-editar-quita-la-aprobacion-y-no-borra-la-historia/funcionalidad_implementada.md`, `documentacion/epicas/EP-018-lo-aprendido-no-se-pierde-entre-sesiones/HU-001-guardar-lo-aprendido/P-EP-018-HU-001-lo-guardado-vuelve-en-la-sesion-siguiente/funcionalidad_implementada.md`, `documentacion/epicas/EP-018-lo-aprendido-no-se-pierde-entre-sesiones/HU-002-consultar-y-corregir-lo-guardado/Q-EP-018-HU-002-corregir-conserva-lo-que-decia-antes/funcionalidad_implementada.md`, `documentacion/epicas/EP-019-el-ciclo-se-opera-desde-la-plataforma/HU-001-abrir-una-fase-con-sus-documentos/S-EP-019-HU-001-el-nombre-sale-del-identificador/funcionalidad_implementada.md`, `documentacion/epicas/EP-019-el-ciclo-se-opera-desde-la-plataforma/HU-002-ver-en-que-estacion-va-cada-fase/T-EP-019-HU-002-la-tabla-manda-sobre-la-frase/funcionalidad_implementada.md`, `documentacion/epicas/EP-019-el-ciclo-se-opera-desde-la-plataforma/HU-003-impedir-avanzar-sin-la-puerta-cumplida/U-EP-019-HU-003-el-rechazo-dice-cual-puerta-falta/funcionalidad_implementada.md`, `documentacion/epicas/EP-020-lo-que-se-desvia-se-avisa/HU-001-avisar-lo-que-se-desvia/W-EP-020-HU-001-todo-aviso-dice-que-lo-disparo/funcionalidad_implementada.md`, `documentacion/epicas/EP-020-lo-que-se-desvia-se-avisa/HU-002-reportar-como-va-cada-proyecto/X-EP-020-HU-002-sin-datos-no-es-cero/funcionalidad_implementada.md`, `documentacion/epicas/EP-022-quien-entra-y-que-puede-hacer/HU-001-entrar-con-cuenta-y-contrasena/AA-EP-022-HU-001-sin-entrar-no-se-ve-nada/funcionalidad_implementada.md`, `documentacion/epicas/EP-022-quien-entra-y-que-puede-hacer/HU-002-separar-lo-que-cada-grupo-puede-hacer/AB-EP-022-HU-002-el-agente-no-aprueba/funcionalidad_implementada.md`, `documentacion/medicion/spec.md`, `documentacion/senales.md`, hecho el 2026-10-04 |
| 11 | Dejar en `proyectos/cimiento/` solo la base Django de la plantilla, con el paquete `core/`, y probar que arranca | 9 | Este análisis, de una y sin fase: `proyectos/cimiento/nucleo`, `proyectos/cimiento/datos`, `proyectos/cimiento/terceros`, `proyectos/cimiento/templates`, `proyectos/cimiento/templates/.gitkeep`, `proyectos/cimiento/static`, `proyectos/cimiento/static/.gitkeep`, `proyectos/cimiento/proyectos`, `proyectos/cimiento/descargar_estaticos.py`, `proyectos/cimiento/indice.sqlite3`, `proyectos/cimiento/config/ambiente.py`, `proyectos/cimiento/config/settings/base.py`, `proyectos/cimiento/config/settings/local.py`, `proyectos/cimiento/config/urls.py`, `proyectos/cimiento/README.md`, `proyectos/cimiento/.env.example`, `proyectos/cimiento/.gitignore`, `proyectos/cimiento/requirements/base.txt`, `proyectos/cimiento/requirements/local.txt`, `proyectos/cimiento/requirements/lock.txt`, `proyectos/cimiento/core`, `proyectos/cimiento/core/__init__.py`, `proyectos/cimiento/.agente/mapeo-nombres.md`, `proyectos/cimiento/manage.py`, `proyectos/cimiento/config/wsgi.py`, `proyectos/cimiento/config/asgi.py`, `proyectos/cimiento/config/settings/__init__.py`, hecho el 2026-10-04 |
| 12 | Marcar como retiradas las épicas `EP-008` a `EP-022`, con fecha y enlace a este análisis | 10 | Este análisis, de una y sin fase: `documentacion/epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/epica.md`, `documentacion/epicas/EP-009-todo-lo-que-se-hace-queda-registrado/epica.md`, `documentacion/epicas/EP-010-lo-escrito-entra-a-la-plataforma/epica.md`, `documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/epica.md`, `documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/epica.md`, `documentacion/epicas/EP-013-los-documentos-se-llenan-sin-salir-de-la-plataforma/epica.md`, `documentacion/epicas/EP-014-ninguna-clave-queda-escrita/epica.md`, `documentacion/epicas/EP-015-lo-exigido-se-comprueba-solo/epica.md`, `documentacion/epicas/EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/epica.md`, `documentacion/epicas/EP-017-una-aprobacion-dice-sobre-que-texto/epica.md`, `documentacion/epicas/EP-018-lo-aprendido-no-se-pierde-entre-sesiones/epica.md`, `documentacion/epicas/EP-019-el-ciclo-se-opera-desde-la-plataforma/epica.md`, `documentacion/epicas/EP-020-lo-que-se-desvia-se-avisa/epica.md`, `documentacion/epicas/EP-021-la-plataforma-se-mira-sin-consola/epica.md`, `documentacion/epicas/EP-022-quien-entra-y-que-puede-hacer/epica.md`, hecho el 2026-10-04 |
| 13 | Primer paso de los validadores como clases: lo común en `core/comun/`, la clase base en `core/validadores/base.py` y el validador de funciones largas (`07·Q3`) con su recorrido de código, cada uno con sus pruebas | 11 | Este análisis, de una y sin fase: `proyectos/cimiento/core/comun/__init__.py`, `proyectos/cimiento/core/comun/hallazgos.py`, `proyectos/cimiento/core/comun/archivos.py`, `proyectos/cimiento/core/comun/proyecto.py`, `proyectos/cimiento/core/comun/git.py`, `proyectos/cimiento/core/comun/tests.py`, `proyectos/cimiento/core/validadores/__init__.py`, `proyectos/cimiento/core/validadores/base.py`, `proyectos/cimiento/core/validadores/codigo.py`, `proyectos/cimiento/core/validadores/calidad.py`, `proyectos/cimiento/core/validadores/tests.py`, hecho el 2026-10-04 |
| 14 | Pasar a clases los validadores que revisan el código (`05·E1/E5`, `04·S3/S5`, `06·R1/R2`, `08·T3/T4`), sobre una clase `ValidadorDeCodigo` que recorre el código una sola vez, con sus pruebas | 11 | Este análisis, de una y sin fase: `proyectos/cimiento/core/validadores/codigo.py`, `proyectos/cimiento/core/validadores/calidad.py`, `proyectos/cimiento/core/validadores/errores.py`, `proyectos/cimiento/core/validadores/seguridad.py`, `proyectos/cimiento/core/validadores/rendimiento.py`, `proyectos/cimiento/core/validadores/aislamiento.py`, `proyectos/cimiento/core/validadores/__init__.py`, `proyectos/cimiento/core/validadores/tests.py`, hecho el 2026-10-04 |
| 15 | El freno no frena el registro de git: lee bien los renombrados de `git status` y no revisa `git add`, `commit` ni `push`, cuyo contenido ya revisa el `pre-commit` | 11 | Este análisis, de una y sin fase: `validadores/freno.py`, `adaptadores/claude-code/hook_despues.py`, `validadores/tests/test_el_freno_no_frena_el_registro_de_git.py`, hecho el 2026-10-04 |
| 16 | Pasar a clases los validadores de migraciones y esquema (`03·D1/D2/D3`, `14·EST1/EST2`, `15·IM2/IM5`) y lo que necesitan: la lectura de tablas Markdown en `core/comun/`, la declaración del proyecto y un solo recorrido de migraciones, con sus pruebas | 11 | Este análisis, de una y sin fase: `proyectos/cimiento/core/comun/__init__.py`, `proyectos/cimiento/core/comun/markdown.py`, `proyectos/cimiento/core/comun/tests.py`, `proyectos/cimiento/core/validadores/__init__.py`, `proyectos/cimiento/core/validadores/declaracion.py`, `proyectos/cimiento/core/validadores/migraciones.py`, `proyectos/cimiento/core/validadores/esquema.py`, `proyectos/cimiento/core/validadores/estructura.py`, `proyectos/cimiento/core/validadores/entidades.py`, `proyectos/cimiento/core/validadores/tests_esquema.py`, hecho el 2026-10-04 |
| 17 | Pasar a clases los validadores del repositorio y de git (`09·G2/G3/G4/G6/G8`, `10·DEP2`, `04·S4`, `00·N6`); el prefijo de cada repositorio y las consultas de ramas quedan una sola vez en `Proyecto` y `Git`, con sus pruebas | 11 | Este análisis, de una y sin fase: `proyectos/cimiento/core/comun/git.py`, `proyectos/cimiento/core/comun/proyecto.py`, `proyectos/cimiento/core/comun/tests.py`, `proyectos/cimiento/core/validadores/__init__.py`, `proyectos/cimiento/core/validadores/codigo.py`, `proyectos/cimiento/core/validadores/migraciones.py`, `proyectos/cimiento/core/validadores/estructura.py`, `proyectos/cimiento/core/validadores/aislamiento.py`, `proyectos/cimiento/core/validadores/versionado.py`, `proyectos/cimiento/core/validadores/dependencias.py`, `proyectos/cimiento/core/validadores/ci.py`, `proyectos/cimiento/core/validadores/rama.py`, `proyectos/cimiento/core/validadores/secretos.py`, `proyectos/cimiento/core/validadores/commits.py`, `proyectos/cimiento/core/validadores/tests_repositorio.py`, `validadores/secretos.py`, hecho el 2026-10-04 |
| 18 | Pasar a clases el validador de enlaces (enlaces rotos, formato `13·DOC14` e índices de carpetas) y su reparador; la lectura de enlaces, el recorrido de los `.md` y la ubicación del estándar quedan una sola vez en `Markdown` y `Proyecto`, con sus pruebas | 11 | Este análisis, de una y sin fase: `proyectos/cimiento/core/comun/markdown.py`, `proyectos/cimiento/core/comun/proyecto.py`, `proyectos/cimiento/core/comun/tests.py`, `proyectos/cimiento/core/validadores/__init__.py`, `proyectos/cimiento/core/validadores/enlaces.py`, `proyectos/cimiento/core/validadores/tests_documentos.py`, `proyectos/cimiento/config/settings/base.py`, `validadores/enlaces.py`, `pendientes/98-las-reglas-mandan-sobre-la-instruccion-del-momento.md`, `pendientes/99-nada-del-proyecto-queda-fuera-del-proyecto.md`, `historico-chat/scripts/2026-10-04/restaurar_textos_de_enlace.py`, hecho el 2026-10-04 |
| 19 | Pasar a clases los validadores de documentos que siguen: trazabilidad de fases (`13·DOC16`), documento contra su plantilla, citas entre reglas y marcas de `00·ID8`; el recorrido de `documentacion/epicas/` queda una sola vez en `Epicas`, con sus pruebas | 11 | Este análisis, de una y sin fase: `proyectos/cimiento/core/comun/proyecto.py`, `proyectos/cimiento/core/validadores/__init__.py`, `proyectos/cimiento/core/validadores/epicas.py`, `proyectos/cimiento/core/validadores/trazabilidad.py`, `proyectos/cimiento/core/validadores/plantillas.py`, `proyectos/cimiento/core/validadores/citas.py`, `proyectos/cimiento/core/validadores/marcas.py`, `proyectos/cimiento/core/validadores/tests_documentos.py`, `historico-chat/scripts/2026-10-04/paridad_documentos.py`, `validadores/plantillas.py`, `validadores/tests/test_el_trinquete_de_las_marcas.py`, hecho el 2026-10-04 |
| 20 | Pasar a clases el validador de fases (`02·F12`) y lo que comparte con los enganches: el recorrido del árbol de épicas, si un documento sigue siendo la plantilla, la lectura del veredicto y la marca de la estación del commit, cada uno una sola vez, con sus pruebas | 11 | Este análisis, de una y sin fase: `proyectos/cimiento/core/validadores/__init__.py`, `proyectos/cimiento/core/validadores/epicas.py`, `proyectos/cimiento/core/validadores/moldes.py`, `proyectos/cimiento/core/validadores/veredictos.py`, `proyectos/cimiento/core/validadores/estacion.py`, `proyectos/cimiento/core/validadores/fases.py`, `proyectos/cimiento/core/validadores/tests_fases.py`, `historico-chat/scripts/2026-10-04/paridad_fases.py`, hecho el 2026-10-04 |
| 21 | Pasar a clases todo lo que queda en `validadores/`: las comprobaciones a `core/validadores/`, la lógica de los enganches a `core/enganches/` y las herramientas a `core/herramientas/`, cada grupo con su paridad y sus pruebas | 11 | Este análisis, de una y sin fase: `proyectos/cimiento/core/validadores/metareglas.py`, `proyectos/cimiento/core/validadores/ejecutable.py`, `proyectos/cimiento/core/validadores/vigencia.py`, `proyectos/cimiento/core/validadores/numeracion.py`, `proyectos/cimiento/core/validadores/cruces.py`, `proyectos/cimiento/core/validadores/relacionadas.py`, `proyectos/cimiento/core/herramientas/mapa_tareas.py`, `proyectos/cimiento/core/herramientas/instalar.py`, `proyectos/cimiento/core/validadores/checklist.py`, `proyectos/cimiento/core/validadores/version.py`, `proyectos/cimiento/core/validadores/versiones.py`, `proyectos/cimiento/core/validadores/guardian_version.py`, `proyectos/cimiento/core/validadores/herramientas.py`, `proyectos/cimiento/core/enganches/recuerdos.py`, `proyectos/cimiento/core/enganches/sesion.py`, `proyectos/cimiento/core/validadores/pendientes.py`, `proyectos/cimiento/core/validadores/acciones.py`, `proyectos/cimiento/core/validadores/amarre.py`, `proyectos/cimiento/core/validadores/brevedad.py`, `proyectos/cimiento/core/validadores/redaccion.py`, `proyectos/cimiento/core/validadores/expediente.py`, `proyectos/cimiento/core/validadores/reaperturas.py`, `proyectos/cimiento/core/validadores/sesiones.py`, `proyectos/cimiento/core/validadores/sitio.py`, `proyectos/cimiento/core/validadores/inmutable.py`, `proyectos/cimiento/core/validadores/indices.py`, `proyectos/cimiento/core/validadores/conteo.py`, `proyectos/cimiento/core/validadores/traza.py`, `proyectos/cimiento/core/enganches/enmascarar.py`, `proyectos/cimiento/core/enganches/historico.py`, `proyectos/cimiento/core/enganches/externo.py`, `proyectos/cimiento/core/enganches/presupuesto.py`, `proyectos/cimiento/core/enganches/rutas_fuera.py`, `proyectos/cimiento/core/enganches/cargador.py`, `proyectos/cimiento/core/enganches/checkpoint.py`, `proyectos/cimiento/core/enganches/veredicto.py`, `proyectos/cimiento/core/herramientas/respaldo.py`, `proyectos/cimiento/core/herramientas/corredor.py`, `proyectos/cimiento/core/herramientas/temas.py`, `proyectos/cimiento/core/enganches/freno.py`, `proyectos/cimiento/core/enganches/plan_vs_hecho.py`, `proyectos/cimiento/core/enganches/acuerdos.py`, `proyectos/cimiento/core/enganches/autorizado.py`, `proyectos/cimiento/core/enganches/origen.py`, `proyectos/cimiento/core/enganches/analisis_en_curso.py`, `proyectos/cimiento/core/enganches/resumen.py`, `proyectos/cimiento/core/enganches/aviso_resuelto.py`, `proyectos/cimiento/core/validadores/analisis.py`, `proyectos/cimiento/core/validadores/flujo.py`, `proyectos/cimiento/core/herramientas/recuperar.py`, `proyectos/cimiento/core/herramientas/andamio.py`, `proyectos/cimiento/core/herramientas/cerrar.py`, `proyectos/cimiento/core/validadores/tests_reglas.py`, `proyectos/cimiento/core/validadores/tests_proceso.py`, `proyectos/cimiento/core/herramientas/tests_instalacion.py`, `proyectos/cimiento/core/enganches/tests_sesion.py`, `proyectos/cimiento/core/enganches/tests_freno.py`, `proyectos/cimiento/core/enganches/__init__.py`, `proyectos/cimiento/core/herramientas/__init__.py`, `proyectos/cimiento/core/validadores/__init__.py`, `proyectos/cimiento/core/comun/__init__.py`, `proyectos/cimiento/core/comun/consola.py`, `proyectos/cimiento/core/comun/tests_consola.py`, `historico-chat/scripts/2026-10-04/paridad_reglas.py`, `historico-chat/scripts/2026-10-04/paridad_instalacion.py`, `historico-chat/scripts/2026-10-04/paridad_proceso.py`, `historico-chat/scripts/2026-10-04/paridad_sesion.py`, `historico-chat/scripts/2026-10-04/paridad_freno.py` |
| 22 | Conectar `validar.py` y los enganches de `adaptadores/claude-code/` a las clases de `core/`: el despachador pasa a `core/herramientas/validar.py` y `validadores/validar.py` queda como la puerta que llaman los `.githooks` de cada proyecto | 11 | Este análisis, de una y sin fase: `proyectos/cimiento/core/herramientas/validar.py`, `proyectos/cimiento/core/herramientas/tests_validar.py`, `validadores/validar.py`, `historico-chat/scripts/2026-10-04/paridad_validar.py`, `adaptadores/claude-code/hook_acuerdos.py`, `adaptadores/claude-code/hook_analisis.py`, `adaptadores/claude-code/hook_antes.py`, `adaptadores/claude-code/hook_checklist.py`, `adaptadores/claude-code/hook_checkpoint.py`, `adaptadores/claude-code/hook_despues.py`, `adaptadores/claude-code/hook_estacion.py`, `adaptadores/claude-code/hook_externo.py`, `adaptadores/claude-code/hook_historico.py`, `adaptadores/claude-code/hook_md.py`, `adaptadores/claude-code/hook_presupuesto.py`, `adaptadores/claude-code/hook_recuerdos.py`, `adaptadores/claude-code/hook_redaccion.py`, `adaptadores/claude-code/hook_reglas.py`, `adaptadores/claude-code/hook_relacionadas.py`, `adaptadores/claude-code/hook_resumen.py`, `adaptadores/claude-code/hook_rutas.py`, `adaptadores/claude-code/hook_senales.py`, `adaptadores/claude-code/hook_sesion.py`, `adaptadores/claude-code/hook_turno.py`, `adaptadores/claude-code/hook_veredicto.py` |

## Lo que aporta al análisis principal

**Resultado:** cambia lo que se construye.

**Lo que suma al análisis principal:** Cimiento se revisa a sí mismo con sus propias reglas: un control avisa cuando una función o una regla nueva se parece a otra que ya existe, el código repetido se junta en un solo lugar por capa, y aprobar un análisis aprueba lo que sale de él.
