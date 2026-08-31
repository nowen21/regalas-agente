# Plan de Pruebas — Fase `A-EP-005-HU-012-que-cada-regla-del-nucleo-diga-quien-la-hace-cumplir`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase, con qué datos y cuándo se da por aprobado. Lo que se pide vive en la [HU-012](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que **ninguna regla del núcleo puede publicarse sin decir quién la hace cumplir**, que decir «nadie» exige el motivo, que la pieza nombrada existe, y que la pieza construida para las tres reglas de redacción **mide de verdad y no detiene nada**.

### 1.2 Alcance

**Entra:** la comprobación sobre el capítulo `00`, las dos formas de la declaración, la resolución de la pieza contra el disco, la medida del turno (trato, marcas, largo) y el enganche que la deja a la vista.

**No entra:** comprobar que la pieza declarada **haga cumplir** la regla. Eso se lee, y prometerlo sería el número que el lector completa con lo que quiere creer (`S-091`). Tampoco entran las reglas de fuera del capítulo `00`.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | La línea base 18/14 y las dos dudas |
| [HU-012](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md) | Los cuatro CA y las cinco reglas de negocio |
| [pendiente 58](../../../../../pendientes/hecho/nada-hace-cumplir-id9.md) | «Menos es más», siete veces en tres días, anotado siete veces y nunca cumplido |
| `S-091` | Una frase que describe lo que hace un programa se deriva, no se escribe |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| `ejecutable.py` | Que reporte la regla sin declaración, y **solo** esa |
| La declaración de «nadie» | Que valga con motivo y **no** sin él |
| La pieza nombrada | Que se resuelva contra el disco, y que la inventada se reporte |
| `redaccion.py` | Que cuente el trato directo y **no** cuente lo citado ni lo que va en código |
| El umbral de largo | Que salga de `brevedad.HOLGADO` y no de un número propio |
| `hook_redaccion.py` | Que hable cuando hay algo que decir, **calle cuando no**, y nunca rompa el turno |
| El canal del enganche | Que esté declarado en el instalador, que es el único canal (`RN-04`) |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

**Con cuerpos de reglas de verdad**, escritos y borrados por la propia prueba en carpetas temporales. El único caso que corre contra el estándar publicado es el de no regresión.

| Tipo | Por qué |
|---|---|
| **De que no pase** | Una declaración vacía tiene que fallar; si pasa, la exigencia queda de adorno |
| **De partición** | Sin declaración · con pieza · con «nadie» y motivo · con «nadie» sin motivo · con pieza inventada |
| **De silencio** | El aviso que sale en cada turno deja de leerse a la tercera |
| **De conexión** | Que el enganche esté colgado, no solo escrito |
| **De límite** | Una regla derogada, y una que declara dos piezas |
| **De no regresión** | Que las 650 pruebas internas sigan como estaban |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-002 | **«Nadie» sin motivo es la puerta por la que la exigencia se vacía** |
| Crítica | CP-006 | **Si el enganche habla en cada turno, se deja de leer, y quedamos peor que sin él** |
| Alta | CP-001, CP-003 | Que la que falta se reporte y que la pieza inventada no pase |
| Alta | CP-005 | Que lo citado no se cuente: contar una cita convierte el reporte en ruido |
| Media | CP-004, CP-007, CP-008 | Límites, umbral derivado y conexión |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

Los dos archivos de prueba de la fase, y **la batería interna completa** (`python validadores/validar.py internas`), porque la fase toca `metareglas.py`, que es de lo que más cuelga.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Los dos planes, aprobados.
- **La medición previa corrida:** cuántas reglas del núcleo hay y cuántas no tienen quién las ejecute, escrita regla por regla.
- El molde con el sitio de la declaración ya fijado: sin eso, cada regla la escribiría en un sitio distinto.

### 4.2 Criterios de salida

- Los ocho casos ejecutados.
- `validar.py ejecutable` en verde sobre el estándar publicado.
- La batería interna sin fallas nuevas respecto de la línea base.
- El enganche corriendo de punta a punta, con su salida vista.

### 4.3 Criterios de suspensión y reanudación

Se suspende si:

- **La declaración vence el sello del checklist de las dieciocho reglas.** Vencer dieciocho sellos de un golpe es la forma más rápida de que nadie vuelva a mirar uno.
- **La línea nueva hace reprobar la fila 10 a una regla que cabía en el molde.** Sería el estándar castigando a la regla por cumplir lo que él mismo pidió.
- **El enganche agrega marcas de `00·ID8` al capítulo `00`.** El trinquete del `pre-commit` rechazaría el commit, y la fase estaría incumpliendo la regla que viene a hacer cumplir.

**Los tres se midieron antes de dar la fase por buena**, y los tres aparecieron de verdad durante la construcción.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| [CA-01](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#ca-01--una-regla-de-núcleo-sin-forma-de-cumplirse-se-reporta) — la regla sin declaración se reporta | CP-001 | Que **no** pase |
| [CA-02](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#ca-02--no-se-puede-hacer-cumplir-vale-pero-con-motivo) — «nadie» vale con motivo | CP-002 | De partición |
| [CA-03](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#ca-03--la-pieza-declarada-existe) — la pieza declarada existe | CP-003 | De partición |
| Transversal — límites | CP-004 | De límite |
| [CA-04](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#ca-04--id9-queda-con-su-decisión-escrita) — la medida del turno | CP-005 | De partición |
| [CA-04](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#ca-04--id9-queda-con-su-decisión-escrita) — el enganche calla cuando todo está bien | CP-006 | **De silencio** |
| [RNF-01](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#5-requisitos-no-funcionales) · [RNF-02](../HU-012-hacer-cumplir-lo-que-solo-se-recuerda.md#5-requisitos-no-funcionales) | CP-007 | De claridad y determinismo |
| `RN-04` — el canal es el instalador | CP-008 | De conexión |
| Transversal — no regresión | CP-009 | De no regresión |

---

## 6. Casos de prueba

### CP-001 — La regla que no lo dice se reporta, y la que sí, no

- **Precondición:** un `base/00-prueba/` con dos reglas, una con su declaración y otra sin ella.
- **Acción:** correr `ejecutable.validar(raiz)`.
- **Resultado esperado:** un solo hallazgo, de severidad **falla**, que nombra la regla que falta y dice dónde escribir la declaración.
- **Y sobre el estándar de verdad, antes de escribir nada:** las **18** reportadas.

### CP-002 — «Nadie la hace cumplir», con motivo y sin él

- **Precondición:** la misma regla, escrita dos veces.
- **Acción:** con el motivo escrito, y con la declaración a secas.
- **Resultado esperado:** con motivo **no se reporta**; sin motivo **sí**, y el mensaje dice que falta el porqué.
- **Por qué importa:** una casilla marcada sin motivo no es una decisión. Es la puerta por la que las dieciocho reglas se declararían «nadie» en una tarde.

### CP-003 — La pieza declarada existe

- **Precondición:** una regla que declara `validadores/inventado.py`, y otra que declara una pieza real.
- **Acción:** correr la comprobación sobre las dos.
- **Resultado esperado:** la inventada se reporta **nombrándola**; la real no.
- **Y el caso del medio:** decir que alguien la hace cumplir sin nombrar a nadie también se reporta.

### CP-004 — Los dos límites que la historia pide

- **Una regla derogada:** queda fuera. Dejó de regir, y pedirle cuentas es pedírselas a una regla que ya no manda.
- **Una regla con dos piezas:** se revisan las dos, y basta que una no exista para que se reporte.

### CP-005 — Qué se cuenta de un turno, y qué no

| Texto | Se espera |
|---|---|
| «El agente abre la terminal y ejecuta el programa.» | nada |
| «Usted abre la terminal.» | trato directo, `00·ID10` |
| «Después tú lo ejecutas.» | trato directo |
| «El texto dice «usted» y eso es una cita.» | **nada** |
| Un bloque cercado con `usted` adentro | **nada** |
| «El estudio y el atún.» | **nada** |
| Una raya larga como inciso | una marca de `00·ID8` |

**Los cuatro «nada» son el caso importante.** Un reporte que cuenta la cita y la palabra que contiene las letras es un reporte que se ignora.

### CP-006 — El enganche calla cuando todo está bien

- **Precondición:** una transcripción de mentiras con una respuesta limpia, y otra con una sucia.
- **Acción:** pasarle cada una al enganche por la entrada estándar.
- **Resultado esperado:** con la sucia, la línea sale nombrando la regla; con la limpia, **ni una palabra**. En los dos casos termina en 0.
- **Y con basura por la entrada:** termina en 0 igual. Medir no puede costarle el turno a nadie.

### CP-007 — Claridad y determinismo

- **`RNF-01`:** el mensaje nombra la regla, dice qué falta y dónde se escribe.
- **`RNF-02`:** dos corridas seguidas sobre el mismo árbol dan la misma lista.
- **El umbral del largo sale de `brevedad.HOLGADO`**, y la prueba lo compara contra esa constante, no contra un número escrito a mano.

### CP-008 — El canal es el instalador  ·  `RN-04`

- **Acción:** leer la tabla de enganches de `instalar.py`.
- **Resultado esperado:** `hook_redaccion.py` está declarado, en el evento de cierre de turno, y el archivo existe.
- **Por qué se prueba:** el proyecto no puede agregar enganches por su cuenta; lo que agregue lo pisa la siguiente instalación.

### CP-009 — No regresión

- **Acción:** `python validadores/validar.py internas`.
- **Resultado esperado:** ninguna falla nueva respecto de la línea base del día.
- **Lo que se vigila en particular:** `metareglas.py`, que la fase toca, y de la que cuelgan el molde, el sello y el largo del cuerpo de todas las reglas.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes

Carpetas temporales que la propia prueba crea y borra, y el repositorio del estándar tal como está publicado.

### 7.2 Datos de prueba

Cuerpos de reglas inventados, con el molde completo: encabezado, cuerpo, ejemplo y checklist. **Ninguno se parece a una regla real**, para que nadie los lea como si lo fueran.

### 7.3 Usuarios de prueba

No aplica.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Que la pieza declarada haga cumplir la regla.** Las pruebas ven que la ruta exista; que el programa de esa ruta ejecute la exigencia lo decide quien lo lee. Está escrito acá para que la corrida en verde no se lea de más.

**Y que la sesión de verdad se comporte como la transcripción de mentiras.** El enganche se prueba con archivos armados; lo que la herramienta escribe de verdad puede traer formas que la prueba no tiene.

---

## 8. Herramientas

`unittest` de la biblioteca estándar, y `subprocess` para correr el enganche como lo corre la herramienta. Ninguna dependencia nueva.

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | La comprobación pasa una regla sin declaración, o el enganche rompe el turno |
| **Alta** | Se reporta lo que está bien: una cita contada como trato, una pieza real como inexistente |
| **Media** | El mensaje no dice dónde escribir la declaración |

### 9.2 Flujo del defecto

Se anota en el `resultado_pruebas.md`, se arregla en la misma fase si cabe en su alcance, y si no, sale como pendiente con su número.

### 9.3 Contenido mínimo de un reporte

Qué se corrió, con qué entrada, qué salió y qué se esperaba.

### 9.4 Registro

En el `resultado_pruebas.md` de esta fase, caso por caso.

---

## 10. Cronograma

Una jornada, la del 2026-08-31.

---

## 11. Roles y responsabilidades

Una sola persona cumple los roles de dueño de producto, desarrollo y pruebas. Quien aprueba es el usuario.

---

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Antes | Objetivo |
|---|---|---|
| Reglas del núcleo sin declaración | 18 | 0 |
| Reglas del núcleo con pieza que las ejecuta | 2 | se cuenta y se declara, no se fija por meta |
| Pruebas de la fase | 0 | las que cubran los nueve casos |

**La segunda no lleva meta a propósito.** Ponerle una empujaría a declarar piezas que no ejecutan nada, que es exactamente el defecto que la historia persigue.

### 12.2 Dónde se miden

`validar.py ejecutable` imprime las dos cifras al cerrar la corrida.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Que las pruebas se escriban contra lo construido y no contra lo pedido | Cada caso nombra el CA que cubre, y los CA son los de la HU |
| Que una corrida en verde se lea como «el núcleo ya se hace cumplir» | La línea de cierre lo dice de frente: declararlo no es hacerlas cumplir |
| Que el cuerpo de reglas de prueba se parezca demasiado al real | Los identificadores y los títulos son inventados |

---

## 14. Control de versiones

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-08-31 | Ing. José Dúmar Jiménez Ruíz | Creación del plan de pruebas de la fase |

---

## 15. Aprobación

| Rol | Nombre | Aprobación |
|---|---|---|
| Usuario | Ing. José Dúmar Jiménez Ruíz | ☐ |
