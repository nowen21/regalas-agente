# Pendiente · Inventario y riesgo de las acciones del agente

**Estado:** cerrado 2026-08-18 · anotado 2026-08-13.

| | |
|---|---|
| **Historia de usuario** | [EP-001 · HU-012 — Inventario de las acciones del agente y su riesgo](../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-012-inventario-de-acciones-y-riesgo/HU-012-inventario-de-acciones-y-riesgo.md) — el inventario es un anexo del núcleo, y el núcleo es cuerpo de reglas |

Escribir la lista de **todo lo que el agente puede hacer** y clasificar cada cosa por qué tan difícil es deshacerla. A partir de esa lista, decir qué necesita aprobación de una persona y qué no.

## El problema

Nadie ha hecho esa lista. Las reglas cubren los casos que alguien recordó: el [núcleo blindado](../../base/00-nucleo-blindado.md) protege datos reales (`N4`), commit y push (`N2`), secretos (`N6`) y las operaciones masivas (`N5`). Son los casos que dolieron. Lo que nunca se hizo fue sentarse a enumerar qué más puede hacer el agente y preguntarse por cada cosa qué pasa si sale mal.

De ahí salen dos consecuencias.

**La primera:** hay acciones sin clasificar. Borrar un archivo que no está en git, reescribir un archivo de configuración de la máquina, correr un script del proyecto que sale a la red. Ninguna aparece en `N1` a `N6` por su nombre, así que caen en la regla general `N1` (ningún cambio de estado sin aprobación explícita) junto con cambiarle una coma a un README.

**La segunda, que es la grave:** un control que trata igual todo lo que toca se termina relajando de una sola vez. Cuando la misma exigencia cubre el cambio de coma y el borrado de la base, lo que ocurre en la práctica es que se aprueba en bloque, y entonces también quedó aprobado el borrado. La rigidez pareja no protege más, protege menos.

## De dónde sale

De los apuntes del diplomado, módulo 2, nota de clase sobre la administración de la IA. Dos frases de ahí:

> Sin inventario no hay nada más.

> Un modelo que ordena un catálogo y uno que niega un crédito no pueden tener el mismo control.

Y de la diapositiva de sistemas autónomos: mientras la máquina sugiere, el error lo filtra una persona; cuando la máquina ejecuta, el error ya ocurrió. El agente de este repo ejecuta.

## Qué habría que construir

**1. El inventario.** Un anexo del capítulo `00 · Núcleo blindado` con la lista de clases de acción: leer, escribir un archivo del repo, borrar, correr un comando local, correr algo que sale a la red, tocar git, tocar datos, tocar la máquina fuera del repo, escribir en el histórico y en la memoria. La lista se hace una vez y se revisa cuando aparece una herramienta nueva.

**2. La clasificación, por lo que cuesta deshacer.** Tres clases bastan:

| Clase | Qué significa | Qué exige |
|---|---|---|
| Se deshace sola | El repo la revierte: editar un archivo versionado, crear uno nuevo. | Nada. Se avisa en el reporte de lo hecho. |
| Se deshace con trabajo | Hay cómo volver atrás pero cuesta: reescribir muchos archivos, tocar la rama, borrar algo versionado. | Se anuncia antes y se hace de una en una, no en bloque. |
| No se deshace | Push, datos reales, algo fuera del repo, cualquier cosa que salga de la máquina. | Aprobación explícita de esa acción concreta, no de un plan que la contenga. |

**3. La consecuencia sobre `N1`.** Hoy `N1` exige aprobación para todo cambio de estado y deja una excepción: un plan aprobado se ejecuta seguido. Con el inventario, esa excepción se puede escribir bien: un plan aprobado cubre lo de las dos primeras clases y nunca lo de la tercera.

## Por qué conviene hacerlo antes que otros

Es barato (es una lista y una tabla, no un programa) y desbloquea cosas: el ítem 15 del [pendiente 09](autonomia-sin-ia.md) (respaldo antes de operación irreversible) hoy no sabe contra qué lista comparar, y esta es esa lista. El [pendiente 12](patron-ia.md) necesita la misma tabla de riesgo para los modelos de un proyecto, así que se escribe una vez y se usa dos veces.

## El límite

La clasificación la escribe una persona, y decidir en qué clase cae una acción nueva es criterio. Lo que un programa puede hacer después es comparar: esta acción está en la lista, esta no. Una acción que no está en el inventario se trata como de la tercera clase hasta que alguien la clasifique, que es la única forma segura de que la lista incompleta no se vuelva un permiso.


---

# Cómo cerró — 2026-08-18

**Las tres piezas que pedía, construidas.** Fase [`A-EP-001-HU-012`](../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-012-inventario-de-acciones-y-riesgo/A-EP-001-HU-012-inventario-de-acciones-y-riesgo/README.md), plan aprobado por el usuario antes de tocar nada.

| Lo que pedía | Cómo quedó |
|---|---|
| **1 · El inventario** | [`base/00-identidad-y-rol/acciones-y-riesgo.md`](../../base/00-identidad-y-rol/acciones-y-riesgo.md) — **12 clases** |
| **2 · La clasificación por lo que cuesta deshacer** | Tres niveles, como proponía: 3 se deshacen solas · 4 con trabajo · **5 no se deshacen** |
| **3 · La consecuencia sobre `N1`** | Escrita: un plan aprobado cubre los dos primeros niveles y **nunca el tercero** |

## La frase del pendiente que resultó ser el criterio de diseño

> *La rigidez pareja no protege más, protege menos.*

Quedó escrita en el anexo, y es lo que decide `CP-006`: si el nivel más bajo y el más alto exigen lo mismo, **la fase falla aunque todo lo demás pase**. Sin diferencia de exigencia, el inventario es decoración.

## Lo que el pendiente no había previsto

**Tres acciones que nombraba como «sin clasificar» resultaron ser del nivel más alto**, no del medio:

- **Borrar un archivo no versionado** — no hay de dónde recuperarlo.
- **Correr algo que sale a la red** — ya salió de la máquina.
- **Escribir fuera del repositorio** — se rompe algo que el usuario usa en paralelo.

Las tres caían hasta hoy en `N1`, junto con cambiarle una coma a un README.

## El núcleo no se tocó

`N1` a `N6` siguen letra por letra. **La lista los organiza, no los reemplaza**, y hay una prueba que compara su texto contra lo guardado — que **cazó un cambio real** mientras se construía.

## Lo que queda, y es otra fase

**Aplicar la clasificación a los enganches**: que el que corre antes de una acción sepa de qué nivel es. No lo cubre ningún criterio de esta historia, así que no se hizo acá.
