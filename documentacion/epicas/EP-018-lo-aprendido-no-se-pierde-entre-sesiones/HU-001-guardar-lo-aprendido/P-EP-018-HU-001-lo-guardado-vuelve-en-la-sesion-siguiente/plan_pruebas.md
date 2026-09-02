# Plan de Pruebas — Fase `P-EP-018-HU-001-lo-guardado-vuelve-en-la-sesion-siguiente`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [HU-001](../HU-001-guardar-lo-aprendido.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que **lo guardado se recupera**, que **guardar no pisa**, y que **un tema sin recuerdos se dice** en vez de inventarse.

### 1.2 Alcance

**Entra:** listar, separar vigentes, buscar, guardar y el resumen.

**No entra:** corregir y dar de baja, que van en la fase `Q`.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las cuatro decisiones técnicas |
| [documentacion/memoria/spec.md](../../../../memoria/spec.md) | El módulo |
| `01·C19` | Dónde vive la memoria |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| Listar | Todos, y solo los vigentes |
| Buscar | Con coincidencias y sin ellas |
| Guardar | Nuevo, y con un nombre que ya existe |
| El resumen | Que los números cuadren |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De ida y vuelta** | Guardar y volver a leer desde cero es el criterio central |
| **De que NO pase** | Que guardar pise un recuerdo existente |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-002 | **Perder un recuerdo es el único fallo irreparable de este módulo** |
| Alta | CP-001 | Si no vuelve, el módulo no sirve para nada |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/memoria/` entera, y las dos baterías completas.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- La carpeta `historico-chat/memory/` existe, con el formato de `01·C19`.

### 4.2 Criterios de salida

- Los tres casos ejecutados.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **una prueba escribe en la carpeta real de recuerdos**. Se reanuda cuando todas trabajen sobre carpetas temporales.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01 | CP-001 | De ida y vuelta |
| CA-02 | CP-001 | De aislamiento |
| CA-03 | CP-003 | De mensaje |
| Transversal | CP-002 | Que **no** pase |

---

## 6. Casos de prueba

### CP-001 — Lo guardado vuelve, y no se mezcla

| Entrada | Se espera |
|---|---|
| Un recuerdo guardado, y se relee desde cero | Está, con su título y su cuerpo |
| Dos carpetas de proyecto distintas | Ninguno se cruza |
| Un recuerdo dado de baja | No sale entre los vigentes |

### CP-002 — Guardar no pisa

**El caso que decide la fase.**

- Guardar con un nombre que ya existe **avisa y deja el archivo como estaba**.
- Se comprueba leyendo el contenido anterior después del intento.

### CP-003 — Un tema sin recuerdos se dice

- Buscar una palabra que no está **responde con una frase**, no con un vacío.

**6 pruebas** cubren estos tres casos.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Carpetas temporales con recuerdos de mentiras. **Ninguna prueba toca `historico-chat/memory/`.**

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Un recuerdo que dejó de ser cierto.** Las pruebas comprueban que se guarda y se recupera; **ninguna comprueba que lo guardado siga siendo verdad**, y nada lo revisa solo. Está declarado.

---

## 8. Herramientas

El corredor de la plataforma. **Ninguna dependencia nueva.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | Se pierde un recuerdo · guardar pisa |
| **Alta** | Lo guardado no vuelve · se mezclan dos proyectos |
| **Media** | Un tema vacío no se distingue de una falla |

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
| Recuerdos perdidos | **Cero** |
| Archivos de la carpeta real modificados al probar | **Cero** |

### 12.2 Dónde se miden

En las pruebas, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Probar sobre la carpeta real | Todas usan carpetas temporales, y se comprueba |

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
