# Plan de Pruebas — Fase `M-EP-017-HU-001-una-aprobacion-guarda-la-huella-del-texto`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [HU-001](../HU-001-registrar-una-aprobacion-con-su-firma.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que una aprobación guarda **quién, cuándo y sobre qué texto**, que se puede consultar después, y que **no se aprueba lo que no existe**.

### 1.2 Alcance

**Entra:** la entidad, aprobar, rechazar lo que no existe, el registro en la auditoría y la consulta de la historia.

**No entra:** el estado de aprobación, que es la fase siguiente.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las cinco decisiones técnicas |
| [documentacion/aprobaciones/spec.md](../../../../aprobaciones/spec.md) | La §5: por qué esta sí guarda |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| La aprobación | Que traiga quién, cuándo, huella y tamaño |
| La huella | **Que sea la del texto aprobado** |
| Lo que no existe | Documento y proyecto |
| La auditoría | Que quede el registro |
| La historia | Que se pueda consultar |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De contenido** | Que la huella sea la del texto, no otra cosa |
| **De que NO pase** | Firmar en blanco es el peor error posible acá |
| De trazabilidad | Que aprobar quede registrado |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-002 | **Aprobar lo que no existe sería firmar en blanco** |
| Crítica | CP-001 | Sin la huella correcta, la aprobación no dice nada |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/aprobaciones/` entera, y las dos baterías completas.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- La especificación del módulo, con su §5.
- Medidas las 21 marcas escritas a mano.

### 4.2 Criterios de salida

- Los dos casos ejecutados.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **se guarda una aprobación sin huella**. Sería repetir lo que ya se hace a mano, con más pasos.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01 y CA-02 | CP-001 | De contenido |
| CA-03 | CP-002 | Que **no** pase |

---

## 6. Casos de prueba

### CP-001 — Se registra quién aprobó y sobre qué

- Queda quién, cuándo, la huella y el tamaño.
- **La huella es la del texto aprobado**, comparada contra el texto exacto.
- Se puede consultar después.
- Aprobar queda en la auditoría.

### CP-002 — No se aprueba lo que no existe

**El caso que decide la fase.**

| Entrada | Se espera |
|---|---|
| Un documento que no está | Se rechaza |
| El mismo | **No queda nada registrado** |
| Un proyecto que no está registrado | Se rechaza |

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Carpetas temporales con documentos de mentiras. **Ningún documento real se aprueba.**

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Que quien aprueba sea quien dice ser.** No se comprueba, y está declarado en la especificación.

---

## 8. Herramientas

El corredor de la plataforma y la librería estándar. **Ninguna dependencia nueva.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | Se guarda una aprobación sin huella · se aprueba lo que no existe |
| **Alta** | Un intento fallido deja registro |
| **Media** | No queda en la auditoría |

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
| Aprobaciones guardadas sin huella | **Cero** |
| Aprobaciones de documentos que no existen | **Cero** |
| Documentos reales aprobados al probar | **Cero** |

### 12.2 Dónde se miden

En las pruebas, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Aprobar un documento real al probar | Se usan carpetas temporales |
| Dar por buena la huella sin compararla | Se compara contra el texto exacto |

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
