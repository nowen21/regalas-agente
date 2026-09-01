# Plan de Pruebas — Fase `A-EP-013-HU-001-los-huecos-de-un-documento-se-ven`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [HU-001](../HU-001-ver-que-le-falta-a-un-documento.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que de un documento del ciclo se sabe **qué molde sigue** y **cuántos huecos le faltan**, que las tres clases de hueco se tratan distinto, y que lo que no se reconoce se dice.

### 1.2 Alcance

**Entra:** la tabla de moldes, la búsqueda de la marca, su clasificación, la ubicación de cada hueco y las cuentas separadas.

**No entra:** escribir en el documento, la pantalla, y juzgar lo ya escrito.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las cinco decisiones técnicas, y por qué la tabla se declara |
| [documentacion/ciclo-de-vida/spec.md](../../../../ciclo-de-vida/spec.md) | Las tres clases (§5.1) y la tabla de moldes (§5.2) |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| La tabla de moldes | Los 17 con molde, y **los cinco que no son directos** |
| Los dos tipos sin molde | Que se digan como reconocidos y sin molde |
| La marca | Que se encuentre donde está y **no donde no está** |
| Las tres clases | Cierto, posible y de instalación, cada una en su lista |
| La ubicación | Línea y contexto de cada hueco |
| Las cuentas | La del usuario y la de instalación, aparte |
| El tipo desconocido | Que lo diga |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De conteo** | Es el `CA-02`, y se mide contando sobre los documentos reales |
| **De clasificación** | Las tres clases son la decisión de diseño de esta fase |
| De borde | Una marca dentro de un bloque de código · dos marcas en la misma línea · una marca partida entre dos líneas |
| **De que NO pase** | Que se cuente lo que no es un hueco, y que un tipo sin molde reciba el parecido |
| **Sobre lo real** | Los documentos de este repositorio, que es donde el marcado deja de ser de mentiras |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-002 | **La cuenta es lo que la historia entrega.** Una cuenta inflada ya pasó una vez: 559 en vez de 31 |
| Crítica | CP-004 | Sin apartar la marca de instalación, el usuario recibe 134 preguntas que no le tocan |
| Crítica | CP-003 | **Es lo que la medición cambió**: contar los de nombre daría por incompleto un documento bien escrito |
| Alta | CP-001 | El molde de cada tipo |
| Media | CP-005, CP-006 | El tipo desconocido y que nada se modifique |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/ciclo_de_vida/` entera, y las dos baterías completas.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Los dos planes, aprobados.
- La especificación del módulo, aprobada el 2026-09-01, con su §5.1 y su §5.2.

### 4.2 Criterios de salida

- Los seis casos ejecutados.
- **La cuenta de huecos de este repositorio, escrita**, sea la que sea.
- Comprobado que la cuenta del expediente y esta no se contradicen.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **la cuenta sobre lo real resulta absurda**: si de 762 documentos salen decenas de miles de huecos, la marca no está diciendo lo que se cree y hay que volver a la §5.1 antes de seguir.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01 — el molde del tipo | CP-001 | De sistema |
| CA-02 — la cuenta y la ubicación | CP-002 | **De conteo** |
| CA-03 — solo el cierto cuenta | CP-003 | De clasificación |
| CA-04 — la clase que no se pregunta | CP-004 | De partición |
| CA-05 — el tipo desconocido | CP-005 | Que **no** pase |
| Transversal — mirar no modifica | CP-006 | Que **no** pase |

---

## 6. Casos de prueba

### CP-001 — Se dice qué molde sigue el documento

- Un `plan_trabajo.md` da el molde del plan de trabajo, y un `epica.md` el de la épica.
- **Los cinco que no son directos:** señales, decisiones de arquitectura y etapa del ciclo dan su molde de fuera de `ciclo-vida-proyectos/`; el índice y el registro de versión salen **reconocidos y sin molde**.
- Un `README.md` dentro de una carpeta de etapa da el molde de la etapa, no el del índice.

### CP-002 — Se listan los huecos, con cuántos son y dónde

| Entrada | Se espera |
|---|---|
| Un documento con tres huecos | Tres, cada uno con su línea |
| Dos huecos en la misma línea | Dos, distinguibles |
| Una marca dentro de un bloque de código | **No se cuenta**: ahí es un ejemplo, no un hueco |
| Un documento sin huecos | Lo dice, en vez de una lista vacía |

**Y sobre los documentos reales:** se cuentan los huecos de este repositorio. El número queda escrito, sea el que sea, y se compara contra contar la marca a mano sobre los mismos archivos.

### CP-003 — Solo el hueco cierto entra en la cuenta

- Un documento con un `«…»` y una marca con nombre que también está en su molde: la cuenta dice **uno**.
- El de nombre sale en la lista de posibles, con su línea.
- **Sobre las 130 historias reales:** la cuenta de ciertos **no incluye** ninguna de las 75 marcas del molde, y **coincide con la que da el módulo Expediente**.

### CP-004 — Lo que llena la instalación no se cuenta como pendiente

- Un documento con `«RUTA-ESTANDAR»`: esa marca **no entra** en la cuenta del usuario.
- **Y aparece en la cuenta de instalación**, con su número.
- Sobre `plantillas/`, donde son 134: la cuenta del usuario baja en 134 y la de instalación sube en 134. Ninguna desaparece.

### CP-005 — Un documento de tipo desconocido lo dice

- Un archivo de nombre inventado dentro de `documentacion/`: se dice que no se le conoce el tipo.
- **Y no se le aplica el molde de otro.** Es el caso de «que NO pase».

### CP-006 — Mirar no modifica nada

- Retrato de los archivos antes y después de pedir qué les falta.
- **Ninguno cambia**, ni en contenido ni en fecha de modificación.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Carpetas temporales con documentos escritos por la prueba, y los documentos reales de este repositorio para la medición. No aplican usuarios.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Si la lista de huecos sirve para llenarlos.** Se comprueba que la cuenta es correcta y que cada hueco se ubica; que el contexto mostrado alcance para saber qué escribir lo dice quien lo use, y eso llega con la `HU-002`.

**Y no se prueba con proyectos ajenos.** El único proyecto conectado es este repositorio.

---

## 8. Herramientas

El corredor de la plataforma y la librería estándar. **Ninguna dependencia nueva.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | La cuenta cuenta lo que no es un hueco · un tipo recibe el molde de otro |
| **Alta** | Una clase de hueco se trata como otra · un hueco se ubica mal |
| **Media** | Un documento sin huecos devuelve una lista vacía sin decirlo |

### 9.2 Flujo · 9.3 Contenido mínimo · 9.4 Registro

En el `resultado_pruebas.md` de esta fase, con qué se corrió, qué salió y qué se esperaba.

---

## 10. Cronograma

Una jornada, la del 2026-09-01.

---

## 11. Roles y responsabilidades

Una sola persona cumple los roles. Quien aprueba es el usuario.

---

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Objetivo |
|---|---|
| Huecos contados en este repositorio | **El número escrito**, y comparado con contarlo a mano |
| Marcas contadas que no eran huecos | Cero |
| Tipos sin molde asignado a la fuerza | Cero |
| Dependencias nuevas | **Cero** |

### 12.2 Dónde se miden

Sobre los documentos reales, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Probar solo con documentos inventados | Se mide sobre los documentos reales de este repositorio |
| Dar por buena la cuenta sin contrastarla | Se compara contra contar la marca a mano sobre los mismos archivos |
| Que esta cuenta y la del expediente digan cosas distintas | Se corren las dos y se explica la diferencia con números |

---

## 14. Control de versiones

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-09-01 | Ing. José Dúmar Jiménez Ruíz | Creación del plan de pruebas de la fase |

---

## 15. Aprobación

| Rol | Nombre | Aprobación |
|---|---|---|
| Usuario | Ing. José Dúmar Jiménez Ruíz | ☐ |
