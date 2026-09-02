# Plan de Pruebas — Fase `A-EP-011-HU-002-lo-que-se-repitio-sale-contado`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-002-ver-que-correccion-se-repite/HU-002-ver-que-correccion-se-repite.md](../HU-002-ver-que-correccion-se-repite.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que lo repetido sale contado, agrupado y con sus sesiones; que **lo mismo dicho distinto cuenta como uno**; y que sin nada repetido se dice, en vez de rellenar.

### 1.2 Alcance

**Entra:** qué cuenta como corrección, cómo se agrupa, el orden, el período, los dos silencios, y que el reporte no se lea como una lista de tareas.

**No entra:** escribir la regla que resuelve el patrón, ni la pantalla.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las seis decisiones, y el caso real medido antes de escribirlo |
| [documentacion/medicion/spec.md](../../../../medicion/spec.md) | La `RN-6`: qué cuenta como corrección |
| [documentacion/epicas/EP-011-lo-que-se-repite-sale-a-la-luz/HU-001-buscar-en-lo-conversado/A-EP-011-HU-001-lo-conversado-se-indexa-y-se-busca/funcionalidad_implementada.md](../../HU-001-buscar-en-lo-conversado/A-EP-011-HU-001-lo-conversado-se-indexa-y-se-busca/funcionalidad_implementada.md) | Lo que dejó indexado la fase anterior |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| Qué cuenta como corrección | Confirmación, pedido, lo muy corto, y **lo que pegó la herramienta** |
| La agrupación | Tres formas del caso real como una · que no se agrupe en cadena |
| El orden y el período | Lo más repetido primero · el período recorta · dos corridas iguales |
| Los dos silencios | «Nada se repitió» contra «no había nada que mirar» |
| Quién habló | Que lo que dijo el agente no cuente |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **Sobre el caso real** | El `CA-03` lo pide con nombre propio: las tres formas de «español colombiano» |
| **De que NO pase** | Que lo dicho una sola vez entre al reporte, y que el agente cuente como usuario |
| **De ruido** | Lo que el editor pega al mensaje no lo escribió una persona |
| **De determinismo** | Dos corridas sobre lo mismo dan la misma lista |
| **De no regresión** | Las dos baterías del repositorio |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-002 | **Es el criterio que la HU llama «lo difícil»**, y sin él el reporte cuenta tres cosas donde hay una |
| Crítica | CP-005 | Un reporte que siempre tiene filas deja de leerse |
| Alta | CP-001, CP-003 | Qué cuenta, y el orden |
| Media | CP-004, CP-006 | El período y el determinismo |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/medicion/` entera, y las dos baterías completas por la no regresión.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Los dos planes, aprobados, y la `RN-6` decidida.
- Lo conversado ya indexado: 3 720 mensajes.

### 4.2 Criterios de salida

- Los seis casos ejecutados.
- El reporte corrido sobre lo indexado de verdad, y **escrito** en el resultado.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **el reporte se llena de ruido de la herramienta**. Un reporte cuyas primeras filas no las escribió una persona no mide lo que dice medir, y es peor que no tenerlo: da la sensación de estar mirando.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| `RN-6` — qué cuenta como corrección | CP-001 | De partición |
| CA-03 — lo mismo dicho distinto | CP-002 | **Sobre el caso real** |
| CA-01 — orden · CA-02 — cuántas y dónde | CP-003 | De sistema |
| CA-01 — período | CP-004 | De partición |
| CA-04 — sin nada repetido | CP-005 | Que **no** pase |
| Determinismo | CP-006 | De repetición |

---

## 6. Casos de prueba

### CP-001 — Qué cuenta como corrección

| Entrada | Se espera |
|---|---|
| «si», «Sí», «hágale», «listo», «OK», «siga» | **no** cuenta |
| «recuerde que todo va en español colombiano» | cuenta |
| «no eso» | **no** cuenta: no alcanza para agrupar |
| Un mensaje que es solo un bloque del editor | **no** cuenta |
| Un mensaje con un bloque del editor y una frase | cuenta **solo la frase** |

### CP-002 — Lo mismo dicho distinto cuenta como uno

- **Precondición:** las tres formas del caso real, en dos sesiones distintas.
- **Resultado esperado:** **una fila**, con tres veces y dos sesiones.
- **Y no se agrupa en cadena:** dos correcciones sobre otro tema salen en su propia fila, no en la misma.

### CP-003 — Ordenado, con cuántas veces y dónde

- **Resultado esperado:** lo más repetido primero, y cada fila con su cuenta y sus sesiones.

### CP-004 — El período recorta

- **Acción:** pedir desde una fecha.
- **Resultado esperado:** lo de antes no sale.

### CP-005 — Sin nada repetido se dice

- **Precondición:** una conversación donde nada se repitió.
- **Resultado esperado:** lista vacía, **y la cuenta de correcciones distinta de cero**. Los dos silencios se distinguen.
- **Y con nada indexado:** las dos en cero, y el reporte dice otra cosa.
- **Y una sesión de puras confirmaciones:** cero correcciones.

### CP-006 — Dos corridas dan la misma lista

- **Por qué:** un reporte que cambia de orden entre corridas no se puede revisar.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes

La base de prueba de la plataforma, con conversaciones que la propia prueba escribe. El `CA-03` se comprueba además **sobre lo indexado de verdad**.

### 7.2 Datos de prueba

Las tres formas del caso real, y mensajes inventados para el resto.

### 7.3 Usuarios de prueba

No aplica.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Si el reporte sirve.** La HU lo dice: *«si no nace una regla nueva, no sirvió»*. Eso no lo mide ninguna prueba; se mide leyendo lo que salió, y decidiendo. Queda como el riesgo `B-02` del plan.

---

## 8. Herramientas

El corredor de la plataforma. **Ninguna dependencia nueva, y ese es un requisito**: agrupar tenía que salir sin instalar nada ni salir a la red.

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | El reporte cuenta como dicho por la persona lo que escribió la herramienta |
| **Alta** | Tres formas de lo mismo salen como tres filas |
| **Media** | Los dos silencios se dicen igual |

### 9.2 Flujo · 9.3 Contenido mínimo · 9.4 Registro

En el `resultado_pruebas.md` de esta fase, con qué se corrió, qué salió y qué se esperaba.

---

## 10. Cronograma

Una jornada, la del 2026-08-31.

---

## 11. Roles y responsabilidades

Una sola persona cumple los roles. Quien aprueba es el usuario.

---

## 12. Métricas e informe

### 12.1 Métricas

| Métrica | Antes | Después |
|---|---|---|
| Formas de saber qué se repitió | ninguna | una orden |
| Filas del reporte que no escribió una persona | 14 de las 14 primeras | 0 |

### 12.2 Dónde se miden

La salida de la orden, escrita en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Probar la agrupación solo con casos inventados | El `CP-002` usa el caso real que la HU nombra |
| Dar por bueno un reporte sin mirarlo | Se corre sobre lo indexado y la salida queda escrita |

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
