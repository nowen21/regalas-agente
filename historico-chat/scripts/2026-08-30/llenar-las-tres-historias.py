# -*- coding: utf-8 -*-
"""Llena las tres historias que levanto el andamio, con lo que dice su pendiente.

El andamio deja el molde con sus marcadores; el contenido sale de los pendientes
91, 92 y 93, que son los que el usuario aprobo el 2026-08-30.
"""
import io
import os

RAIZ = r"c:\Ing. Jose\ia\agente"
EPICAS = os.path.join(RAIZ, "documentacion", "epicas")

CABECERA = u"""# {id} — {titulo}

> Historia de usuario del estándar. Nace del [pendiente {pend}](../../../../pendientes/{pend_archivo}), aprobado por el usuario el 2026-08-30.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| **ID** | {id} |
| **Épica / Feature** | [{ep} — {ep_titulo}](../epica.md) |
| **Módulo / Componente** | {modulo} |
| **Tipo** | Técnica |
| **Prioridad** | {prioridad} |
| **Estimación** | {estimacion} |
| **Sprint** | Sin asignar |
| **Solicitante** | El usuario |
| **Responsable** | El agente |
| **Estado** | Pendiente |

---

## 2. Narrativa

**Como** {como}
**quiero** {quiero}
**para** {para}.

---

## 3. Contexto y descripción

{contexto}

### 3.1 Reglas de negocio

{reglas}

### 3.2 Supuestos

{supuestos}

### 3.3 Fuera de alcance

{fuera}

---

## 4. Criterios de aceptación

{criterios}

### Criterios de aceptación transversales

{transversales}

---

## 5. Requisitos no funcionales

| ID | Categoría | Requisito |
|---|---|---|
{rnf}

---

## 6. Diseño y referencias

{diseno}

---

## 7. Tareas técnicas derivadas

{tareas}

---

## 8. Fases que la implementan

> **Trazabilidad hacia abajo.** Se completa a medida que la HU se descompone en fases (`02·F12.2`: al menos una). El enlace se escribe en los dos lados.

| Fase (`02·F12.6`) | CA que cubre | Depende de | Plan de trabajo | Plan de pruebas | Resultado | Estado |
|---|---|---|---|---|---|---|
| Sin abrir todavía | — | — | — | — | — | Sin empezar |

**Qué documento responde qué**, para no buscar en el que no es:

| Pregunta | Documento |
|---|---|
| Qué se pide y cuándo se da por aceptado | Esta HU |
| Qué se va a hacer, en qué orden y sobre qué archivos | `plan_trabajo.md` de la fase |
| Con qué casos se comprueba cada CA | `plan_pruebas.md` de la fase |
| Qué se ejecutó, con qué resultado, y si el CA quedó cumplido | `resultado_pruebas.md` de la fase |
| En qué estación va y qué la tiene detenida | `estado-fase.md` de la fase |
| Qué quedó hecho al final | `funcionalidad_implementada.md` de la fase |

---

## 9. Dependencias y riesgos

| Tipo | Descripción | Impacto |
|---|---|---|
{riesgos}

---

## 10. Definition of Ready (DoR)

- [x] Narrativa clara con rol, acción y beneficio
- [x] Criterios de aceptación definidos y testeables
- [x] Reglas de negocio documentadas
- [x] Diseño / mockup disponible: no aplica, no hay interfaz
- [x] Dependencias identificadas y desbloqueadas
- [ ] Estimada por el equipo
- [x] Cumple criterios INVEST

## 11. Definition of Done (DoD)

- [ ] Código implementado y en rama principal
- [ ] Pruebas unitarias e integración pasando
- [ ] Code review aprobado
- [ ] Todos los criterios de aceptación verificados
- [ ] Requisitos no funcionales validados
- [ ] Documentación técnica actualizada
- [ ] Desplegada: no aplica, no hay ambiente
- [ ] Aceptada por el usuario

---

## 12. Validación INVEST

| Criterio | ✅ | Observación |
|---|:--:|---|
| **I**ndependiente | ☑ | {invest_i} |
| **N**egociable | ☑ | {invest_n} |
| **V**aliosa | ☑ | {invest_v} |
| **E**stimable | ☑ | {invest_e} |
| **S**mall (pequeña) | ☑ | {invest_s} |
| **T**esteable | ☑ | {invest_t} |

---

## 13. Bitácora

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-30 | El agente | Se crea la historia a partir del pendiente {pend}, aprobado por el usuario |
"""

HISTORIAS = [
 dict(
  epica="EP-004-comprobacion-automatica", ep="EP-004",
  ep_titulo=u"Comprobación automática de lo que no admite discusión",
  carpeta="HU-024-el-validador-dice-que-no-comprueba",
  id="HU-024", pend="91",
  pend_archivo="91-el-validador-de-marcas-no-dice-que-no-comprueba.md",
  titulo=u"El validador dice sobre qué corrió y qué no comprueba",
  modulo=u"Programas de comprobación",
  prioridad=u"Must", estimacion=u"2 puntos",
  como=u"quien corre un validador antes de entregar un documento",
  quiero=u"que su salida diga sobre qué carpetas corrió y qué partes de la norma no cuenta",
  para=u"no leer un cero como si fuera un aprobado",
  contexto=u"""`validar.py marcas` recorre `base/` y `plantillas/`. Sobre `documentacion/` devuelve cero **porque no mira**, no porque esté limpio, y la salida no distingue una cosa de la otra.

El programa tampoco cuenta todo lo que la norma pide: cubre las marcas mecánicas y deja para la lectura las que hay que juzgar. Su «0 en 0 archivos» tampoco lo dice.

**Ya cobró.** El 2026-08-30 el agente corrió el comando sobre veinticinco documentos nuevos, obtuvo cero, y escribió en el cuerpo de un commit que el validador no reportaba ninguna línea de esos archivos. El enganche del commit, que sí lee lo que entra al índice, encontró trece avisos en esos mismos archivos. La afirmación falsa quedó publicada.""",
  reglas=u"""- Un validador que no dice sobre qué corrió no entrega un veredicto: entrega un número que el lector completa con lo que quiere creer.
- Decir qué **no** se comprobó no es una disculpa: es parte del resultado.
- Ampliar el alcance del recorrido es una decisión aparte, y no la reemplaza esta historia.""",
  supuestos=u"""- La salida la lee una persona, no otro programa: se escribe en palabras, no en códigos.
- El alcance actual del recorrido se conserva mientras no se decida otra cosa.""",
  fuera=u"""- **Ampliar el recorrido a `documentacion/`.** Es más trabajo y produciría ruido de entrada, porque esa carpeta arrastra deuda vieja.
- Construir la comprobación de las marcas que hoy se leen a mano.""",
  criterios=u"""### CA-01 — La salida nombra sobre qué corrió

```gherkin
Dado que el validador de marcas termina su corrida
Cuando imprime su resultado
Entonces la salida nombra las carpetas que recorrió
Y quien la lee puede saber si su archivo estaba entre ellas
```

**Cómo validarlo:**
1. Desde la raíz del repositorio, correr `python validadores/validar.py marcas`.
2. Leer la salida completa → resultado esperado: aparece una línea que nombra las carpetas recorridas.
3. Comprobar que un archivo de `documentacion/` no está cubierto por esa lista, y que la salida lo deja claro.
- **Aprobado cuando:** la salida nombra las carpetas y no hay que abrir el código para saber cuáles son.

### CA-02 — La salida nombra qué partes de la norma no cuenta

```gherkin
Dado que el validador cubre unas marcas y deja otras para la lectura
Cuando termina su corrida
Entonces la salida dice qué partes no contó
Y dice que esas se leen
```

**Cómo validarlo:**
1. Correr `python validadores/validar.py marcas` sobre un árbol sin ninguna marca mecánica.
2. Leer la salida → resultado esperado: además del cero, aparece qué quedó sin contar.
3. Comprobar que lo nombrado coincide con lo que el programa de verdad no mira.
- **Aprobado cuando:** un cero no se puede leer como «cumple la norma entera».

### CA-03 — Un recorrido sin archivos lo dice, y no dice «limpio»

```gherkin
Dado que se corre el validador sobre una carpeta sin ningún archivo que mirar
Cuando termina
Entonces dice que no encontró nada que revisar
Y no dice que esté limpio
```

**Cómo validarlo:**
1. Crear una carpeta temporal vacía.
2. Correr el validador con esa carpeta como raíz → resultado esperado: un mensaje de que no había nada que mirar.
3. Comprobar que el texto no afirma limpieza.
- **Aprobado cuando:** los dos ceros, el de «no encontré nada» y el de «no hay marcas», se distinguen leyendo.""",
  transversales=u"""- [x] **Errores** — un archivo que no se puede leer no tumba la corrida, y se dice cuál fue.
- [x] **No regresión** — la suite del validador queda verde, y ningún conteo cambia.""",
  rnf=u"""| RNF-01 | **Rendimiento** | La salida nueva no agrega ninguna pasada sobre el árbol: se arma con lo que la corrida ya sabe |
| RNF-02 | **Trazabilidad** | Lo que la salida diga que no cuenta tiene que coincidir con lo que el programa no mira, y eso se prueba |""",
  diseno=u"""- **Documento funcional:** el [pendiente 91](../../../../pendientes/91-el-validador-de-marcas-no-dice-que-no-comprueba.md).
- **Programa afectado:** `validadores/marcas.py` y su entrada en `validadores/validar.py`.
- **La norma que se comprueba:** el anexo de marcas de generación automática.""",
  tareas=u"""- [ ] Programa: que la corrida sepa qué carpetas recorrió y las imprima
- [ ] Programa: que imprima qué partes de la norma no cuenta
- [ ] Programa: distinguir «no había nada que mirar» de «no hay marcas»
- [ ] Pruebas: un caso por cada uno de los tres criterios
- [ ] Documentación: cerrar el pendiente 91""",
  riesgos=u"""| Riesgo | Que la salida se vuelva tan larga que nadie la lea | Se dice en una línea, al final, y solo lo que cambia la lectura del número |
| Riesgo | Que lo declarado y lo que el programa mira se separen con el tiempo | El CA-02 lo prueba: lo declarado sale de lo que el programa recorre, no de un texto escrito aparte |""",
  invest_i=u"No depende de ninguna otra historia abierta",
  invest_n=u"Qué se nombra y con qué palabras es discutible",
  invest_v=u"Evita el defecto que ya publicó una afirmación falsa",
  invest_e=u"Tres criterios, un solo programa",
  invest_s=u"Una fase",
  invest_t=u"Los tres criterios se comprueban corriendo el comando",
 ),
 dict(
  epica="EP-004-comprobacion-automatica", ep="EP-004",
  ep_titulo=u"Comprobación automática de lo que no admite discusión",
  carpeta="HU-025-los-caracteres-de-control-invisibles-se-cuentan",
  id="HU-025", pend="92",
  pend_archivo="92-hay-caracteres-de-control-invisibles-en-26-documentos.md",
  titulo=u"Los caracteres de control invisibles se cuentan y se quitan",
  modulo=u"Programas de comprobación",
  prioridad=u"Should", estimacion=u"2 puntos",
  como=u"quien lee un documento del proyecto",
  quiero=u"que ningún carácter de control se cuele dentro de un archivo de texto",
  para=u"que una tabla no se rompa sin que nadie lo vea",
  contexto=u"""Al ir a agregar una fila a la tabla de fases de una historia, la fila que ya estaba empezaba con un carácter de control en vez de con la barra de la tabla. Esa fila **no se renderiza como fila**: en cualquier visor desaparece del cuadro y queda como un párrafo suelto debajo.

Buscándolo aparece en **26 archivos**, trece de ellos en `documentacion/`.

El programa que cuenta las marcas invisibles ya conoce siete caracteres —el espacio duro, el de ancho cero, el guion suave y cuatro más— y los limpia. Ninguno de control está en esa lista.""",
  reglas=u"""- Un carácter que no se ve leyendo y que rompe el documento es exactamente lo que un programa debe cazar: una persona no puede.
- Lo que la lista del anexo diga y lo que el programa cuente tienen que ser lo mismo.
- Limpiar los archivos que ya lo traen va en su propio commit, sin mezclarse con otro trabajo.""",
  supuestos=u"""- Los caracteres de control dentro de un bloque de código pueden ser legítimos y no se tocan.
- El salto de línea y el tabulador no son el problema.""",
  fuera=u"""- **Averiguar de dónde salieron.** Nadie sabe qué los metió, y saberlo no es condición para limpiarlos.
- Los caracteres invisibles que ya se cuentan, que siguen igual.""",
  criterios=u"""### CA-01 — El carácter de control se reporta, con su archivo y su línea

```gherkin
Dado un archivo de texto con un carácter de control dentro
Cuando se corre el validador de marcas
Entonces lo reporta nombrando el archivo, la línea y qué carácter es
```

**Cómo validarlo:**
1. Crear una carpeta temporal con un archivo que traiga un carácter de control en medio de una línea.
2. Correr el validador de marcas sobre esa carpeta → resultado esperado: un hallazgo que nombra el archivo, la línea y el carácter.
3. Comprobar que el nombre del carácter se entiende sin conocer la tabla de códigos.
- **Aprobado cuando:** el hallazgo dice dónde está y qué es, sin que haya que buscarlo a mano.

### CA-02 — El árbol queda en cero

```gherkin
Dado que 26 archivos del repositorio traen un carácter de control
Cuando se limpian
Entonces la búsqueda no devuelve ninguno
Y el texto que se ve no cambió
```

**Cómo validarlo:**
1. Antes de limpiar, contar cuántos archivos lo traen y anotar el número.
2. Limpiar, y volver a contar → resultado esperado: cero.
3. Comparar un archivo antes y después → resultado esperado: la única diferencia es el carácter que no se veía.
- **Aprobado cuando:** la cuenta queda en cero y ninguna palabra del texto cambió.

### CA-03 — Lo legítimo no se toca

```gherkin
Dado un archivo con un tabulador dentro de un bloque de código
Cuando se corre el validador
Entonces no lo reporta
```

**Cómo validarlo:**
1. Crear un archivo con un bloque de código que use tabulador para alinear.
2. Correr el validador → resultado esperado: ningún hallazgo por ese tabulador.
- **Aprobado cuando:** el caso legítimo pasa sin reclamo.""",
  transversales=u"""- [x] **Límites** — el archivo vacío y el que no se puede decodificar tienen comportamiento definido.
- [x] **No regresión** — los siete caracteres que ya se contaban se siguen contando igual.""",
  rnf=u"""| RNF-01 | **Rendimiento** | La comprobación nueva no agrega ninguna pasada: va en la misma lectura del archivo |
| RNF-02 | **Trazabilidad** | La lista del anexo y la del programa dicen lo mismo, y eso se prueba |""",
  diseno=u"""- **Documento funcional:** el [pendiente 92](../../../../pendientes/92-hay-caracteres-de-control-invisibles-en-26-documentos.md).
- **Programa afectado:** `validadores/marcas.py`.
- **La norma que se amplía:** la lista de marcas invisibles del anexo de generación automática.""",
  tareas=u"""- [ ] Programa: contar los caracteres de control, y decidir si se barre el rango entero o solo los que aparecieron
- [ ] Programa: que la limpieza los quite
- [ ] Norma: agregar la fila al anexo, para que la lista y el programa digan lo mismo
- [ ] Limpieza: los 26 archivos, en su propio commit
- [ ] Pruebas: un caso por criterio, incluido el legítimo que no se toca""",
  riesgos=u"""| Riesgo | Que la limpieza cambie texto visible | El CA-02 compara el antes y el después: la única diferencia permitida es el carácter invisible |
| Riesgo | Que se limpien archivos de otras sesiones en curso | Se comprueba el registro de sesiones antes de tocar, como se hizo con los enlaces el 2026-08-30 |""",
  invest_i=u"No depende de ninguna otra historia",
  invest_n=u"Si se barre el rango entero o solo lo que apareció, se discute",
  invest_v=u"Hoy una historia muestra una fase menos de las que tiene",
  invest_e=u"Un programa y una limpieza contada",
  invest_s=u"Una fase, y la limpieza en su commit",
  invest_t=u"La cuenta antes y después es el criterio",
 ),
 dict(
  epica="EP-001-cuerpo-de-reglas-heredable", ep="EP-001",
  ep_titulo=u"Cuerpo de reglas heredable",
  carpeta="HU-037-la-norma-de-redaccion-del-agente",
  id="HU-037", pend="93",
  pend_archivo="93-la-norma-de-redaccion-vive-dentro-de-dos-plantillas.md",
  titulo=u"La norma de redacción del agente vive en el cuerpo de reglas",
  modulo=u"Cuerpo de reglas",
  prioridad=u"Should", estimacion=u"3 puntos",
  como=u"agente que entrega documentos en cualquier proyecto",
  quiero=u"una regla del cuerpo de reglas que fije variedad del idioma, persona y forma verbal",
  para=u"que la exigencia no dependa de qué plantilla se esté llenando",
  contexto=u"""El usuario pidió que un documento se redactara en español colombiano, en tercera persona y en infinitivo. **No hubo regla del cuerpo de reglas que citar.**

Esa exigencia solo está escrita dentro de dos plantillas, como su regla 11: la del manual de usuario y la del manual de instalación. Dice, palabra por palabra, que las acciones van en infinitivo, las explicaciones en tercera persona, y que el impersonal con «se» no sirve para las acciones.

**El estándar ya sabe que le falta.** El anexo de marcas de generación automática lo dice en su cierre: la norma del idioma «necesita su propia regla, y todavía no existe».""",
  reglas=u"""- La variedad del idioma sale del proyecto, no se fija en uno solo: ya hay una regla que dice que se habla el idioma del proyecto, y esta la concreta.
- Una norma que rige lo que el agente entrega no puede vivir dentro de un documento modelo: ahí solo la hereda quien llene ese modelo.
- Al cerrarse, las dos plantillas citan la regla en vez de repetirla.""",
  supuestos=u"""- La regla se escribe por el procedimiento del capítulo de meta-reglas, con su checklist aplicado y su versión.
- Lo que hoy dicen las dos plantillas es correcto: lo que cambia es dónde vive.""",
  fuera=u"""- **La ortografía y la gramática.** El anexo las nombra como pendientes suyas y son otra regla: una cosa es cómo se conjuga y otra si el texto está bien escrito.
- El texto que ve el usuario final de un producto, que ya tiene su regla.""",
  criterios=u"""### CA-01 — La regla existe, con su identificador y su checklist

```gherkin
Dado que la norma de redacción no está en el cuerpo de reglas
Cuando se escribe la regla por el procedimiento del capítulo de meta-reglas
Entonces existe con su identificador, su ejemplo y su checklist aplicado
Y el validador de meta-reglas no reclama nada
```

**Cómo validarlo:**
1. Abrir el capítulo donde quedó la regla y leer su cuerpo → resultado esperado: una sola exigencia, con su ejemplo de lo incorrecto y lo correcto.
2. Correr `python validadores/validar.py metareglas` → resultado esperado: sin incumplimientos.
3. Comprobar que aparece clasificada en el registro de reglas comprobables, diciendo qué mitad no lo es.
- **Aprobado cuando:** la regla está escrita, clasificada y el validador la acepta.

### CA-02 — Las dos plantillas la citan en vez de repetirla

```gherkin
Dado que la norma estaba escrita dentro de dos plantillas
Cuando la regla existe en el cuerpo de reglas
Entonces las dos plantillas la citan con su enlace
Y ninguna repite su texto
```

**Cómo validarlo:**
1. Buscar en las dos plantillas el texto de la regla 11 → resultado esperado: ya no está el texto completo.
2. Comprobar que en su lugar hay una cita con enlace a la regla nueva.
3. Correr el validador de coherencia → resultado esperado: el enlace resuelve.
- **Aprobado cuando:** la norma está en un solo sitio y las plantillas apuntan a él.

### CA-03 — La regla dice el idioma del proyecto, no uno fijo

```gherkin
Dado un proyecto que no trabaja en español
Cuando se aplica la regla
Entonces exige la variedad del idioma que ese proyecto declara
Y no exige español colombiano
```

**Cómo validarlo:**
1. Leer el cuerpo de la regla → resultado esperado: nombra el idioma del proyecto, no uno concreto.
2. Comprobar que se sostiene sobre la regla que ya fija el idioma del proyecto.
- **Aprobado cuando:** la regla sirve a un proyecto en cualquier idioma.""",
  transversales=u"""- [x] **No regresión** — el validador de meta-reglas y el de coherencia quedan sin fallas.
- [x] **Trazabilidad** — la regla queda clasificada, diciendo qué se puede comprobar con un programa y qué no.""",
  rnf=u"""| RNF-01 | **Trazabilidad** | La regla nueva se versiona y se registra, como cualquier cambio del cuerpo de reglas |
| RNF-02 | **Compatibilidad** | Un proyecto que ya tenga documentos escritos no queda obligado a reescribirlos: la regla rige lo que se entrega de aquí en adelante |""",
  diseno=u"""- **Documento funcional:** el [pendiente 93](../../../../pendientes/93-la-norma-de-redaccion-vive-dentro-de-dos-plantillas.md).
- **Documentos afectados:** el capítulo donde quede la regla, las dos plantillas de manual, y el registro de reglas comprobables.""",
  tareas=u"""- [ ] Decidir el alcance con el usuario: si rige para todo documento o solo para los que lee alguien de fuera del oficio
- [ ] Escribir la regla, con su checklist aplicado
- [ ] Clasificarla en el registro de comprobables
- [ ] Cambiar las dos plantillas para que la citen
- [ ] Versionar y registrar el cambio
- [ ] Cerrar el pendiente 93""",
  riesgos=u"""| Dependencia | La decisión de alcance es del usuario y bloquea la redacción | Alto |
| Riesgo | Que la regla quede fijada a un idioma y no sirva a otros proyectos | El CA-03 lo comprueba |
| Riesgo | Que se escriba como norma de estilo y termine siendo discutible en cada documento | Se escribe con una sola exigencia y su ejemplo, como cualquier regla |""",
  invest_i=u"Depende de una decisión del usuario, no de otra historia",
  invest_n=u"El alcance es justamente lo que se negocia",
  invest_v=u"Hoy la convención se copia a mano de una plantilla, y lo copiado a mano se copia distinto",
  invest_e=u"Una regla, dos plantillas y un registro",
  invest_s=u"Una fase",
  invest_t=u"Los tres criterios se comprueban leyendo y corriendo dos validadores",
 ),
]

for h in HISTORIAS:
    ruta = os.path.join(EPICAS, h["epica"], h["carpeta"], h["carpeta"] + ".md")
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(CABECERA.format(**h))
    print("llenada:", h["id"])
