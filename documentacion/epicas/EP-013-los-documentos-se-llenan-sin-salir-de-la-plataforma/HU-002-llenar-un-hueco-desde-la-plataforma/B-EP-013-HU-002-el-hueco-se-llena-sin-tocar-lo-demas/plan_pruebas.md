# Plan de Pruebas — Fase `B-EP-013-HU-002-el-hueco-se-llena-sin-tocar-lo-demas`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [HU-002](../HU-002-llenar-un-hueco-desde-la-plataforma.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que un hueco se llena, que lo escrito queda en el archivo del proyecto, y sobre todo que **nada más cambia**.

### 1.2 Alcance

**Entra:** reemplazar el hueco, guardar sin dejar el archivo a medias, detectar el cambio ajeno, registrar, y volver a traer el documento.

**No entra:** redactar libre, crear documentos, y la pantalla.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las siete decisiones técnicas, y por qué se escribe en el original |
| [documentacion/ciclo-de-vida/spec.md](../../../../ciclo-de-vida/spec.md) | Las `RN-1` a `RN-7` y la §6 |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| El reemplazo | Que ponga el texto donde va, y **solo ahí** |
| El guardado | Que no deje el archivo a medias |
| La huella | Que detecte el cambio ajeno |
| La ubicación | Que un documento movido no se escriba a ciegas |
| El registro | Que quede quién, cuándo, qué documento y qué hueco |
| La copia | Que no se separe del original |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De comparación entera** | Es el `CA-02`, y solo se comprueba mirando el archivo completo |
| **De que NO pase** | Escribir encima de un cambio ajeno · escribir en el hueco equivocado · dejar el archivo a medias |
| De borde | El primer hueco · el último · dos iguales en la misma línea · un hueco dentro de una tabla |
| **Sobre lo real** | Un documento de este repositorio, llenado de punta a punta |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-002 | **Si guardar reformatea, el editor gana y nadie usa la plataforma** |
| Crítica | CP-004 | Escribir encima de un cambio ajeno pierde trabajo de otro |
| Crítica | CP-006 | Escribir en el hueco equivocado daña el documento en silencio |
| Alta | CP-001, CP-003 | Que quede escrito, y que la cuenta baje |
| Media | CP-005 | El registro |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/ciclo_de_vida/` entera, y las dos baterías completas.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Los dos planes, aprobados.
- La `HU-001` cerrada: sin saber dónde está el hueco no hay dónde escribir.
- Dónde se escribe, decidido: en el archivo original.

### 4.2 Criterios de salida

- Los seis casos ejecutados.
- **Un documento real llenado de punta a punta**, con el archivo comparado entero.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **el archivo cambia fuera del hueco**, aunque sea en un espacio o en un salto de línea. Un guardado que reformatea obliga a revisar el documento entero cada vez, y entonces la funcionalidad no sirve para lo que se hizo.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01 — queda en el archivo | CP-001 | De sistema |
| CA-02 — nada más cambia | CP-002 | **De comparación entera** |
| CA-03 — la cuenta baja | CP-003 | De conteo |
| CA-04 — el cambio ajeno no se pisa | CP-004 | Que **no** pase |
| CA-05 — queda registrado | CP-005 | De trazabilidad |
| Transversal — el hueco equivocado | CP-006 | Que **no** pase |

---

## 6. Casos de prueba

### CP-001 — Se llena un hueco y queda en el archivo

- Lo escrito aparece en el **archivo original del proyecto**, no solo en la copia.
- El archivo se abre y se lee **sin la plataforma**.
- La copia de `datos/` queda con lo mismo: se vuelve a traer el documento.

### CP-002 — Lo que no es el hueco no cambia

**El caso que decide la fase.**

| Entrada | Se espera |
|---|---|
| Un documento largo, con tablas | Solo cambia el hueco |
| Un documento con saltos de línea al final | Los mismos saltos, antes y después |
| Un hueco dentro de una celda de tabla | La tabla no se reacomoda |
| El primer y el último hueco del archivo | Ninguno de los dos corre el resto |

Se compara **el archivo entero, carácter por carácter**, con el hueco descontado.

### CP-003 — La cuenta de huecos baja

- Un documento con N huecos, tras llenar uno, queda con N menos uno.
- **Ni en más ni en menos:** llenar uno no puede hacer desaparecer otro.

### CP-004 — Si el archivo cambió por fuera, se avisa

- Leer, cambiar el archivo por fuera, y guardar: **avisa y no escribe**.
- El cambio de afuera sigue ahí, entero.
- Es el caso de «que NO pase» de esta fase.

### CP-005 — Queda registrado

- Tras llenar, la auditoría dice quién, cuándo, qué documento y qué hueco.
- **El registro va antes del efecto**, como en el resto de la plataforma.
- Un intento que no escribió no deja registro de un cambio que no hubo.

### CP-006 — No se escribe en el hueco equivocado

- Un hueco cuya línea ya no dice lo mismo: **no se escribe**, se avisa.
- Dos huecos iguales en la misma línea: se llena el que se pidió, no el otro.
- Un documento sin huecos no se puede llenar, y lo dice.
- Llenar con texto vacío no hace nada: borrar la marca sin poner nada deja el documento peor, porque ya no se ve que falta.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Carpetas temporales para las pruebas automáticas, y **un documento real de este repositorio** para el caso de punta a punta. Está versionado: si algo sale mal, el control de versiones lo devuelve.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Si llenar así es cómodo.** Se comprueba que lo escrito queda bien y que nada más cambia; que valga la pena frente a abrir el editor lo dice quien lo use, y esa es la pregunta que la ficha de `F-014` deja advertida.

**Y no se prueba con un proyecto ajeno.** El único conectado es este repositorio, y **esta es la primera fase que escribe en él**.

---

## 8. Herramientas

El corredor de la plataforma y la librería estándar. **Ninguna dependencia nueva.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | El archivo cambia fuera del hueco · se escribe encima de un cambio ajeno · el archivo queda a medias |
| **Alta** | Se escribe en el hueco equivocado · la cuenta no baja |
| **Media** | El registro no dice qué hueco fue |

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
| Caracteres que cambian fuera del hueco | **Cero**, y el número escrito |
| Huecos llenados en el documento de punta a punta | Todos los que tenía |
| Cambios ajenos pisados | **Cero** |
| Dependencias nuevas | **Cero** |

### 12.2 Dónde se miden

Sobre el archivo real, comparado entero, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Probar solo con documentos cortos e inventados | Se llena un documento real, largo y con tablas |
| Dar por bueno «se ve igual» sin comparar | Se compara carácter por carácter, y el número va escrito |
| Probar la escritura sobre un archivo sin versionar | Se usa uno versionado, para que haya vuelta atrás |

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
