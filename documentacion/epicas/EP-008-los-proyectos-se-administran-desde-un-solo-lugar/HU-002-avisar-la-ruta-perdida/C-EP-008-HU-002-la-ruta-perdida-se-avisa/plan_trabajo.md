# Plan de Trabajo — Fase C-EP-008-HU-002-la-ruta-perdida-se-avisa (módulo Proyectos)   ·   `[CAPA 3]`

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** | `C-EP-008-HU-002-la-ruta-perdida-se-avisa` |
| **Épica** | [EP-008 Los proyectos se administran desde un solo lugar](../../epica.md) |
| **HU** | [HU-002 Avisar cuando la ruta de un proyecto se pierde](../HU-002-avisar-la-ruta-perdida.md), una sola |
| **Módulo** | Proyectos |
| **Especificación** | [documentacion/proyectos/spec.md](../../../../proyectos/spec.md), §6 |
| **Versión del producto** | 1, fase C de ocho |
| **Fecha apertura** | 2026-08-25 |
| **Rama** | Una rama propia de la fase, que se integra al cerrarla |

---

## 1. Objetivo y alcance

**Qué se busca.** Que el usuario no descubra que movió la carpeta de un proyecto el día que necesita trabajar en él.

**Qué entra.** El aviso con la ruta que se buscó, corregir esa ruta, y la medición de que comprobar cincuenta rutas no vuelve lenta la lista.

**Qué no entra.** Buscar la carpeta sola en otro lado, que la historia deja fuera a propósito. Vigilar las rutas todo el tiempo: se comprueban al listar, y ese supuesto está declarado en la historia.

## 2. Análisis previo: línea base verificada

**Esta fase es más corta de lo que parece, y conviene decirlo antes de planearla.** Al revisar el código de las fases B y H apareció que **`CA-01` y `CA-02` ya están casi construidos**, sin que ninguna fase se lo hubiera propuesto:

| Qué pide la historia | Qué hay hoy | Qué falta |
|---|---|---|
| `CA-01` la ruta perdida se marca en la lista | `ruta_viva` en [models.py](../../../../../plataforma/nucleo/proyectos/models.py), y la lista muestra «esa ruta ya no existe» | **El aviso no dice qué ruta se buscó.** La lista la muestra en su columna, pero el aviso en sí no la nombra, y `RN-2` pide que la diga |
| `CA-02` su documentación se sigue viendo | La pantalla del proyecto ya avisa, y su documentación no depende de la ruta | Nada. Falta la prueba que lo fije |
| `CA-03` corregir la ruta quita el aviso | **Nada** | Todo. Es el grueso de la fase |
| Transversal: listar cincuenta proyectos bajo un segundo | Nada medido | La medición |

**Por qué apareció construido.** `ruta_viva` se hizo en la fase B porque el modelo de datos lo pedía como campo calculado, y el aviso de la pantalla salió de la misma fase. Ninguna de las dos estaba pensando en `HU-002`.

**Qué se usa tal cual.** El comprobante de la auditoría, la reescritura de la ficha (`_reescribir_ficha` de la fase H, que ya sabe cambiar un campo y dejar el registro), y la pantalla de confirmación con su lista de «qué NO va a pasar».

### 2.1 Archivos que se crean o modifican

`plataforma/nucleo/proyectos/` y sus plantillas. Se modifica `config/urls.py` si hace falta una ruta nueva.

**Nada de esta fase escribe dentro de la carpeta del proyecto.**

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Por qué |
|---|---|---|
| Corregir la ruta reutiliza `_reescribir_ficha` de la fase H | Escribir otro camino de guardado | Ya sabe reescribir un campo, dejar la constancia antes y registrar el cambio. Otro camino sería otro sitio donde olvidarse de la auditoría |
| La ruta corregida se comprueba igual que al conectar: que exista, y que no la tenga otro | Aceptarla sin comprobar | Corregir no puede ser una puerta de atrás para lo que conectar rechaza. Es lo mismo que se decidió con la versión de reglas en la fase H |
| Corregir la ruta **relee la versión de reglas** del proyecto nuevo | Dejar la versión que tenía | La carpeta cambió: la versión que declara puede ser otra. Dejar la vieja sería afirmar sobre lo que no se leyó |
| El aviso nombra la ruta que se buscó | Decir solo «la ruta no existe» | `RN-2` de la historia. Sin la ruta, el usuario no puede ver si fue un renombre, un movimiento o un disco que no está montado |
| La comprobación de rutas se mide con cincuenta proyectos de mentira | Confiar en que va a ser rápido | El transversal de la historia lo exige contra `RNF-02`, y medir es la única forma de saberlo |

### 2.7 Dudas por resolver antes de escribir

Ninguna. Las tres que podrían serlo ya están resueltas:

| Lo que podría ser duda | Dónde ya está resuelto |
|---|---|
| Cuándo se comprueba la ruta | Al listar. Es el supuesto declarado en la §3.2 de la historia |
| Qué pasa con la documentación de un proyecto con ruta perdida | Se sigue viendo. Es `RN-1` de la historia y `RN-4` de la especificación |
| Si corregir la ruta puede saltarse las comprobaciones de conectar | No. Se decidió lo mismo para la versión de reglas en la fase H, y esta fase sigue ese camino |

## 3. Desglose de tareas

| # | Tarea | Entregable |
|---|---|---|
| 1 | Que el aviso diga qué ruta se buscó | El aviso nombra la ruta, en la lista y en la pantalla del proyecto |
| 2 | Corregir la ruta de un proyecto | Se apunta a otra carpeta, con su confirmación y su registro |
| 3 | Comprobar la ruta nueva como al conectar | Una ruta que no existe o que ya tiene otro proyecto se rechaza |
| 4 | Releer la versión de reglas al corregir la ruta | La versión sale de la carpeta nueva, no de la vieja |
| 5 | Medir que cincuenta proyectos listan bajo un segundo | La medición, con su número escrito |

## 4. Secuencia de ejecución

1 → 2 → 3 → 4 → 5. La 5 va al final porque necesita que la comprobación de rutas esté completa para medir lo que de verdad va a correr.

## 5. Verificación de criterios de aceptación

| Criterio | Cómo se verifica |
|---|---|
| `CA-01` la ruta que dejó de existir se avisa | Se conecta un proyecto, se borra su carpeta, y se mira la lista |
| `CA-02` su documentación se sigue viendo | Con la ruta perdida, se entra al proyecto y se busca su documentación |
| `CA-03` volver a apuntar la ruta quita el aviso | Se corrige a una carpeta que existe, y se comprueba que el aviso desaparece y queda el registro |
| Transversal `RNF-02` | Se listan cincuenta proyectos y se mide |

## 6. Datos y ambiente de prueba

La propia máquina, sin red. Proyectos de mentira creados y borrados por la propia prueba. Para probar la ruta perdida **se borran carpetas de mentira**, nunca ninguna del usuario.

## 7. Reversión

Se descarta la rama de la fase. Lo que escribe son rutas dentro de fichas que ya existen; nada se borra.

## 8. Producción y migración

No aplica: el campo de la ruta ya existe desde la fase B.

## 9. Reglas del estándar aplicadas

| Regla | Cómo se cumple acá |
|---|---|
| `02·F2` sin especificación acordada no hay código | La del módulo Proyectos describe este comportamiento en su §6 |
| `02·F4` el plan va con su plan de pruebas | Se presentan y se aprueban juntos |
| `00·N1` ningún cambio de estado sin aprobación | Corregir la ruta pide confirmación, como los cambios de la fase H |
| `20·M12` buscar antes de crear | Media fase estaba construida, y por eso la sección 2 lo dice antes de planear |
| `01·C7` ante dos lecturas, preguntar | No quedó ninguna duda: las tres candidatas ya estaban resueltas y se comprobó |

## 10. Riesgos y bloqueos

| # | Riesgo | Qué se hace |
|---|---|---|
| 1 | Que comprobar cincuenta rutas haga lenta la lista | Es la tarea 5. Se mide, y si no cabe en el segundo, se decide qué hacer antes de cerrar la fase |
| 2 | Que corregir la ruta se convierta en una forma de saltarse lo que conectar comprueba | Es la tarea 3, y su caso de prueba |
| 3 | Que la fase parezca hecha porque la mitad ya estaba | Lo que estaba se declaró en la sección 2, y el plan de pruebas comprueba **todo** el criterio, no solo lo que se agrega |

## 11. Definition of Done

- ☐ El aviso dice qué ruta se buscó.
- ☐ Se puede corregir la ruta, con confirmación y registro.
- ☐ Una ruta que no existe, o que ya tiene otro proyecto, se rechaza al corregir.
- ☐ Corregir la ruta relee la versión de reglas de la carpeta nueva.
- ☐ La documentación de un proyecto con ruta perdida se sigue viendo.
- ☐ Medido cuánto tarda listar cincuenta proyectos, con el número escrito.

## 12. Seguimiento

El estado vive en [estado-fase.md](estado-fase.md), y se actualiza al cambiar de estación.

## 13. Cierre

La fase cierra cuando los seis puntos de la sección 11 tengan veredicto. Lo que quede sin hacer se declara como deuda en el documento de cierre.

---

**Aprobado por Ing. José Dúmar Jiménez Ruíz, el 2026-08-25.** Se aprueba junto con [plan_pruebas.md](plan_pruebas.md).
