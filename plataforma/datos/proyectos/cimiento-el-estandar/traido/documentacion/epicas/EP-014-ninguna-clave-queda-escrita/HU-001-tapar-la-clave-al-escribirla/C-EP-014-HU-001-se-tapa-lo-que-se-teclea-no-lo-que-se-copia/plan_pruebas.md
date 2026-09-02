# Plan de Pruebas — Fase `C-EP-014-HU-001-se-tapa-lo-que-se-teclea-no-lo-que-se-copia`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [HU-001](../HU-001-tapar-la-clave-al-escribirla.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que **lo que se teclea se tapa y lo que se copia no**, que se dice cuántas se taparon, y que sin enmascarador no se escribe nada.

### 1.2 Alcance

**Entra:** el puente que tapa, el camino que llena un hueco, el conteo sin tocar y la orden que avisa.

**No entra:** reconocer formas de credencial, que vive en el estándar y tiene sus propias pruebas allá.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las cinco decisiones, y la medición que fijó el alcance |
| [documentacion/seguridad/spec.md](../../../../seguridad/spec.md) | La §5.1: qué camino tapa y cuál no |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| El puente | Clave con comillas, sin comillas, y texto limpio |
| El nombre de la variable | Que quede intacto |
| El camino que llena | Que tape, y que diga cuántas |
| Lo importado | **Que no cambie** |
| El conteo | Que encuentre y ordene, sin tocar |
| La falta del enmascarador | Que reviente |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De que NO pase** | Es la mitad de esta fase: que no se altere lo importado, y que no se escriba sin tapar |
| De partición | Con comillas, sin comillas, y lo que solo parece clave |
| **Sobre lo real** | Los 1 002 documentos guardados, que es donde apareció el límite |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-003 | **Tapar no se deshace.** Alterar lo importado corrompe documentos sin vuelta |
| Crítica | CP-005 | Escribir sin tapar es el daño que todo esto viene a evitar |
| Alta | CP-001, CP-002 | Que tape, y que lo diga |
| Media | CP-004 | El aviso |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/seguridad/` y `plataforma/nucleo/ciclo_de_vida/`, y las dos baterías completas.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- La medición hecha: qué caminos tapan y qué pasaría si taparan todos.
- La especificación del módulo, con su §5.1.

### 4.2 Criterios de salida

- Los cinco casos ejecutados.
- **La orden corrida sobre los 1 002 documentos**, con su número escrito.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **alguna prueba altera un documento que no debía**. Tapar no se deshace, y un defecto ahí no se arregla volviendo a correr.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01 — la clave tecleada se tapa | CP-001 | De sistema |
| CA-02 — se dice cuántas | CP-002 | De sistema |
| CA-03 — lo importado no se altera | CP-003 | Que **no** pase |
| CA-04 — lo que no se tapa se dice | CP-004 | De conteo |
| CA-05 — sin enmascarador no se escribe | CP-005 | Que **no** pase |

---

## 6. Casos de prueba

### CP-001 — Una clave tecleada al llenar queda tapada

- Llenar un hueco con una clave entre comillas: en el archivo está el nombre y **no** está la clave.
- Lo mismo sin comillas.
- Un texto sin claves se escribe **idéntico**.

### CP-002 — Se dice cuántas se taparon

- Al llenar con una clave, vuelve el número uno.
- Al llenar con texto limpio, vuelve cero.
- **Tapar en silencio deja al usuario creyendo que escribió otra cosa.**

### CP-003 — Lo importado no se altera

**El caso que decide la fase.**

- Un documento con una clave de ejemplo escrita se guarda **tal cual**.
- Leerlo devuelve el texto con la clave de ejemplo adentro, intacta.
- Revisarlo lo encuentra **sin tocarlo**.

### CP-004 — Lo que no se tapa se dice

- Se listan cuáles y cuántos fragmentos, de más a menos.
- Un proyecto limpio no devuelve nada.
- **Sobre los 1 002 documentos reales:** el número queda escrito, sea el que sea.

### CP-005 — Sin enmascarador no se escribe

- Con la ruta de validadores apuntando a una carpeta que no existe, tapar **revienta**.
- No devuelve el texto tal cual. Es el caso de «que NO pase» que más protege.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Carpetas temporales y **claves inventadas**, nunca una real ([`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)). Para el conteo, los documentos guardados de este repositorio, que solo se leen.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Si el reconocedor reconoce todo lo que hay que reconocer.** Eso se prueba en el estándar, donde vive la lista de formas. Acá se prueba que la plataforma lo use y lo use donde debe.

---

## 8. Herramientas

El corredor de la plataforma y el enmascarador del estándar. **Ninguna dependencia nueva.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | Se altera un documento importado · se escribe sin tapar |
| **Alta** | Una clave tecleada llega al archivo · el nombre de la variable se tapa |
| **Media** | El aviso no sale |

### 9.2 Flujo · 9.3 Contenido mínimo · 9.4 Registro

En el `resultado_pruebas.md` de esta fase.

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
| Claves que llegan a un archivo por el camino que teclea | **Cero** |
| Documentos importados alterados | **Cero** |
| Documentos con apariencia de credencial, dichos | Todos, con su número |
| Dependencias nuevas | **Cero** |

### 12.2 Dónde se miden

Sobre los documentos reales, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Usar una clave real en una prueba | Solo inventadas, y el propio tapador las trata igual |
| Dar por bueno que tapa sin comprobar dónde | Se comprueba camino por camino, y los seis quedan declarados |

---

## 14. Control de versiones

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-09-01 | Ing. José Dúmar Jiménez Ruíz | Creación del plan de pruebas de la fase |

---

## 15. Aprobación

| Rol | Nombre | Aprobación |
|---|---|---|
| Usuario | Ing. José Dúmar Jiménez Ruíz | ☑ Autorizada la épica entera el 2026-09-01 |
