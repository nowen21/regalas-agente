# Plan de Pruebas — Fase `O-EP-017-HU-003-editar-quita-la-aprobacion-y-no-borra-la-historia`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [HU-003](../HU-003-caducar-la-aprobacion-cuando-el-texto-cambia.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que **editar un documento aprobado le quita la aprobación**, que se ve cuánto cambió, y que **la anterior no se borra**.

### 1.2 Alcance

**Entra:** la comparación de huellas, la medida del cambio, la historia y el documento que desaparece.

**No entra:** el diff completo.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las cinco decisiones técnicas |
| [documentacion/aprobaciones/spec.md](../../../../aprobaciones/spec.md) | El módulo |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| La comparación | Sin tocar, con edición, y con el documento borrado |
| La medida del cambio | De más y de menos |
| La historia | **Que la anterior se conserve** |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De estado** | Aprobado antes, caducada después |
| **De que NO pase** | Que caducar borre la historia |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-003 | **Es el caso real que originó la funcionalidad** |
| Crítica | CP-004 | Perder la historia deja el documento como si nadie lo hubiera mirado |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/aprobaciones/` entera, y las dos baterías completas.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- Las fases `M` y `N` cerradas.

### 4.2 Criterios de salida

- Los dos casos ejecutados.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **una aprobación anterior se pierde**. Es la única parte de esta épica que no se puede reconstruir.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01 y CA-02 | CP-003 | De estado |
| CA-03 | CP-004 | Que **no** pase |

---

## 6. Casos de prueba

### CP-003 — Editar quita la aprobación

**El caso que decide la fase.**

| Entrada | Se espera |
|---|---|
| Sin tocar el documento | Sigue aprobado |
| Editando su texto | **Caduca** |
| Editando para agregar | Se dice cuántos caracteres de más |
| Borrando el documento | **También caduca**, y se dice que ya no está |

### CP-004 — La aprobación anterior no se borra

- Al volver a aprobar quedan las dos.
- **La que manda es la última**, y la anterior sigue consultable.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Carpetas temporales con documentos de mentiras.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Un cambio que no cambia lo que el documento dice.** Una aprobación responde por el texto exacto: arreglar una coma la caduca, y está declarado.

---

## 8. Herramientas

El corredor de la plataforma. **Ninguna dependencia nueva.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | Se pierde una aprobación anterior · editar no caduca |
| **Alta** | Un documento borrado sigue aprobado |
| **Media** | No se dice cuánto cambió |

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
| Aprobaciones perdidas al caducar | **Cero** |
| Documentos editados que siguen aprobados | **Cero** |

### 12.2 Dónde se miden

En las pruebas, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Probar solo el caso de editar | Se prueba también borrar el documento |

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
