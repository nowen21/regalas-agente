# Plan de Pruebas — Fase `R-EP-009-HU-002-la-auditoria-se-puede-preguntar`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [HU-002](../HU-002-buscar-en-la-auditoria.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que **la auditoría se puede preguntar**: por proyecto, por fecha y por tipo de acción, con la respuesta medida.

### 1.2 Alcance

**Entra:** los tres filtros, el orden, el aviso de vacío, el aviso de recorte y el tiempo.

**No entra:** la pantalla y exportar.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las cinco decisiones técnicas |
| [documentacion/auditoria/spec.md](../../../../auditoria/spec.md) | El módulo |
| [`S-110`](../../../../senales.md) | Por qué un vacío tiene que decirse |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| Los tres filtros | Juntos y por separado |
| El rango de fechas | **Que el último día entre completo** |
| El aviso de vacío | Que se distinga de una falla |
| El tiempo | Que venga medido en la respuesta |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De borde** | El último día del rango es donde se pierde lo más reciente |
| **De mensaje** | Un vacío se ve igual que una falla |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-002 | **Perder el último día es perder justo lo que se está buscando** |
| Alta | CP-003 | Un vacío mudo hace desconfiar del registro entero |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/auditoria/` entera, y las dos baterías completas.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- La fase `D` cerrada, con la auditoría registrando.

### 4.2 Criterios de salida

- Los cuatro casos ejecutados.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **una búsqueda modifica algún registro**. La auditoría es de solo lectura desde acá.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01 | CP-001 | De filtro |
| Transversal | CP-002 | De borde |
| CA-02 | CP-003 | De mensaje |
| CA-03 | CP-004 | De tiempo |

---

## 6. Casos de prueba

### CP-001 — Los tres filtros

- Por proyecto, por rango de fechas y por tipo de acción, juntos y por separado.
- Lo hallado sale **de lo más reciente a lo más viejo**.
- Los tipos de acción disponibles salen **de lo registrado**, no de una lista fija.

### CP-002 — El último día entra completo

**El caso de borde que decide la fase.**

- Un registro hecho a las once de la noche del día del `hasta` **entra en el resultado**.
- Se comprueba con la hora pegada al texto de la fecha.

### CP-003 — Sin coincidencias se dice

- Una búsqueda que no encuentra nada **responde con una frase**.
- Se distingue de una consulta que falló.

### CP-004 — El tiempo viene medido

- La respuesta trae **cuántos** y **en cuántos segundos**.
- Si el resultado se recortó, **lo dice**.

**14 pruebas** cubren estos cuatro casos.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Registros de mentiras en la base de pruebas, de varios proyectos y varias fechas.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Un año de registros de verdad.** El CA-03 pide menos de un segundo con ese volumen; la prueba mide con lo que hay, y **el número que sale es el que se escribe**, no una promesa. Cuando la auditoría real acumule un año, el número habrá que volverlo a medir.

---

## 8. Herramientas

El corredor de la plataforma. **Ninguna dependencia nueva.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | Se pierde el último día del rango · una búsqueda modifica un registro |
| **Alta** | Un vacío no se distingue de una falla |
| **Media** | El recorte no se avisa |

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
| Registros perdidos por el borde del rango | **Cero** |
| Recortes en silencio | **Cero** |
| Tiempos supuestos en vez de medidos | **Cero** |

### 12.2 Dónde se miden

En las pruebas, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Probar el rango solo por el medio | Se prueba el registro de las once de la noche del último día |
| Dar el tiempo por bueno sin medirlo | La respuesta trae los segundos, y se escriben |

---

## 14. Control de versiones

| Fecha | Autor | Cambio |
|---|---|---|
| 2026-09-01 | Ing. José Dúmar Jiménez Ruíz | Creación del plan de pruebas de la fase |

---

## 15. Aprobación

| Rol | Nombre | Aprobación |
|---|---|---|
| Usuario | Ing. José Dúmar Jiménez Ruíz | ☑ Autorizada el 2026-09-01 |
