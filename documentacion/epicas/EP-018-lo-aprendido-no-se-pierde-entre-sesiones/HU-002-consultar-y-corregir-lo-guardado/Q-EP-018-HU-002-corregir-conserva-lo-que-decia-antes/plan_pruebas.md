# Plan de Pruebas — Fase `Q-EP-018-HU-002-corregir-conserva-lo-que-decia-antes`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [HU-002](../HU-002-consultar-y-corregir-lo-guardado.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que **corregir conserva lo que decía antes** y que **dar de baja no borra**.

### 1.2 Alcance

**Entra:** buscar, corregir, dar de baja y el resumen.

**No entra:** la pantalla.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las cuatro decisiones técnicas |
| [documentacion/memoria/spec.md](../../../../memoria/spec.md) | El módulo |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| Buscar | Con coincidencias y sin ellas |
| Corregir | **Que quede el texto nuevo y el anterior** |
| Dar de baja | Que el archivo siga, y salga de lo vigente |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De contenido** | Se lee el archivo después de corregir |
| **De que NO pase** | Que dar de baja borre el archivo |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-005 | **Corregir sin conservar deja la corrección sin explicación** |
| Crítica | CP-006 | Borrar un recuerdo es irreparable |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/memoria/` entera, y las dos baterías completas.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- La fase `P` cerrada.

### 4.2 Criterios de salida

- Los tres casos ejecutados.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **un archivo de recuerdo desaparece** en cualquier prueba.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01 | CP-004 | De búsqueda |
| CA-02 | CP-005 | De contenido |
| CA-03 | CP-006 | Que **no** pase |

---

## 6. Casos de prueba

### CP-004 — Se busca por palabra

- Sale lo que la trae, en el título o en el cuerpo.
- Lo que no está **se dice con palabras**.

### CP-005 — Corregir conserva lo que decía antes

**El caso que decide la fase.**

| Entrada | Se espera |
|---|---|
| Un recuerdo corregido | El texto nuevo está |
| El mismo archivo | **Y debajo, marcado, el texto anterior** |
| Dos correcciones seguidas | Las dos versiones anteriores quedan |

### CP-006 — Dar de baja no borra

- El archivo **sigue estando** después.
- **No sale entre los vigentes**, y sí entre todos.
- El resumen cuenta bien los tres números.

**10 pruebas** cubren estos tres casos.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Carpetas temporales con recuerdos de mentiras. **Ninguna prueba toca `historico-chat/memory/`.**

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Un recuerdo con años de correcciones encima.** Las pruebas corrigen dos veces; un recuerdo real puede acumular más, y volverse pesado de leer. Está declarado y se acepta: **muchas correcciones son la señal de que ese recuerdo hacía falta**.

---

## 8. Herramientas

El corredor de la plataforma. **Ninguna dependencia nueva.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | Se borra un archivo · corregir pierde lo anterior |
| **Alta** | Un recuerdo de baja sigue saliendo entre los vigentes |
| **Media** | El resumen no cuadra |

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
| Archivos de recuerdo borrados | **Cero** |
| Correcciones que pierden lo anterior | **Cero** |

### 12.2 Dónde se miden

En las pruebas, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Probar solo que la corrección se ve | Se lee el archivo entero, y se comprueba que lo anterior está |

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
