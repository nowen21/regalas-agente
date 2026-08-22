# Resultado de Pruebas — Fase A-EP-001-HU-004-retrodocumentar-la-conducta-de-la-ia   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-001-HU-004-retrodocumentar-la-conducta-de-la-ia` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-17 |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente |

**Lo que hace especial a esta fase:** los tres criterios son sobre **cómo se comporta el agente**, y la única evidencia honesta es cómo se comportó de verdad. Esta jornada da los tres casos, y dos de ellos son incumplimientos.

---

## 1. Ejecución caso por caso

### CA-01 · Una pregunta se responde, no se ejecuta

Está cubierto por dos reglas, y las dos con nombre: [`01·C13`](../../../../../base/01-conducta.md#c13--preguntas-de-análisis-van-en-chat-abierto-no-en-formulario-cerrado) y [`01·C17`](../../../../../base/01-conducta.md#c17--ante-un-pedido-que-admite-dos-lecturas-reformula-antes-de-mover-nada).

**Caso real de hoy.** El usuario preguntó «¿qué aporta esto?» sobre un párrafo. La respuesta fue una respuesta: qué comunicaba ese lugar, qué comunicaba el párrafo, y una propuesta. **No se tocó el archivo hasta que el usuario lo pidió.** Toda la sesión salió de esa pregunta bien entendida.

**Y hay un contraejemplo, también de hoy, que vale más que el ejemplo.** Cuando el usuario dijo «siga», el agente lo tomó como orden de continuar y **no** como autorización para commitear, y lo dijo cada vez. Distinguir las dos cosas es exactamente este criterio.

**Resultado del criterio: Cumple.**

### CA-02 · Lo que se detecta mal se corrige sin preguntar

Está en el recuerdo [corregir el defecto que uno mismo detecta](../../../../../historico-chat/memory/corregir-el-defecto-que-uno-mismo-detecta.md).

**Caso real de hoy, y es un incumplimiento parcial.** El agente detectó que el molde del planteamiento copiaba la cadena de `02·F0` con una versión desactualizada. **No lo corrigió en el momento**: lo anotó como hallazgo H-7 y esperó a que la fase C lo tomara. Fue lo correcto, porque tocar un molde sube versión y eso pide su cadena, pero muestra el límite del criterio: **«sin preguntar» no significa «sin procedimiento»**.

En cambio sí se corrigieron sin preguntar, y bien: el marcador `«…»` roto en 24 sitios, las seis líneas donde la coma quedó donde iban dos puntos, y la expectativa mal contada de una prueba.

**Resultado del criterio: Cumple**, con el matiz de arriba escrito.

### CA-03 · Lo entregado no se lee como escrito por una máquina

Existe la regla, [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md), existe la lista cerrada de marcas, y existe el programa que cuenta las mecánicas.

**Y hoy se incumplió, de la forma más útil posible: la vio el usuario.** El planteamiento reconstruido salió con **33 marcas** y el agente no había corrido el validador que existe justo para eso. Lo señaló el usuario, no el programa.

Eso destapó lo demás: el recuento era más ancho que la regla y contaba 9 000 marcas que no lo eran, y los moldes del ciclo pasaron de 197 a 0. Está en los hallazgos H-3, H-5 y H-8 del [resumen de la sesión](../../../../../historico-chat/resumenes/2026-08-22/sesion-2.md).

**Resultado del criterio: Cumple** como regla, **con un incumplimiento medido el mismo día**. Lo que falla no es la regla ni el programa: es que nadie corre el programa antes de entregar.

---

## 2. Defectos encontrados

| ID | Severidad | Qué pasó | Estado |
|---|---|---|---|
| D-01 | **Alta** | Nada obliga a correr el recuento de marcas **antes de entregar un documento**. La regla existe, el programa existe, y el enganche solo mira lo que entra al commit. Un documento que se muestra en el chat y nunca se commitea no pasa por ningún filtro | **Abierto** |
| D-02 | Media | El CA-02 se lee como «corrige de una», y hay correcciones que exigen su cadena porque suben versión. El criterio no distingue, y el agente tuvo que decidirlo sobre la marcha | **Abierto** |

---

## 3. Veredicto por criterio de aceptación

| CA | Cómo se comprobó | Concepto |
|---|---|---|
| CA-01, la pregunta se responde | `01·C13` y `01·C17`, y dos casos reales de hoy, uno de ellos un contraejemplo | Cumple |
| CA-02, lo detectado mal se corrige sin preguntar | El recuerdo, tres correcciones hechas y una diferida con motivo | Cumple |
| CA-03, no se lee como máquina | `00·ID8` con su lista y su programa, y un incumplimiento del mismo día | Cumple |

---

## 4. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios están cubiertos por reglas con nombre, y los tres tienen evidencia de conducta real y no de lectura. Que dos de esos casos sean incumplimientos **no los invalida**: el criterio pide que la conducta esté exigida y sea observable, y lo es tanto cuando se cumple como cuando no.

**Lo que esta fase deja como deuda** es el D-01, que es el que explica el incumplimiento del CA-03: no hay quién recuerde correr el programa antes de entregar.

---

## 5. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Las reglas de conducta | `base/01-conducta.md`, 27 reglas |
| EV-02 | Los casos reales | Hallazgos H-1, H-3, H-4, H-7 y H-8 del resumen de esta sesión |
| EV-03 | El incumplimiento del CA-03 | 33 marcas en un documento entregado, señaladas por el usuario |

---

## 6. Ciclos anteriores

Ninguno.
