# Plan de Pruebas — Fase `AB-EP-022-HU-002-el-agente-no-aprueba`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [HU-002](../HU-002-separar-lo-que-cada-grupo-puede-hacer.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que **el agente no aprueba**, que **el rechazo dice qué permiso falta**, y que **una cuenta que no existe se rechaza**.

### 1.2 Alcance

**Entra:** los dos grupos, sus permisos, el rechazo y `aprobar`.

**No entra:** permisos por proyecto.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las decisiones técnicas |
| [documentacion/acceso/spec.md](../../../../acceso/spec.md) | El módulo |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| Los dos grupos | Que sean dos, y con qué permisos |
| El agente | Las cuatro acciones que no puede |
| El rechazo | Que traiga los tres datos |
| `aprobar` | Con cuenta, sin cuenta y con cuenta sin permiso |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De que NO pase** | Que el agente apruebe |
| **De estado después del rechazo** | Que no quede nada a medio guardar |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-004 | **Un agente que aprueba lo que él mismo construyó vuelve la aprobación un trámite** |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/acceso/` entera, y las dos baterías completas.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- La fase `AA` cerrada.

### 4.2 Criterios de salida

- Todos los casos ejecutados.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **una aprobación queda guardada tras un rechazo**.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01 | CP-003 y CP-004 | De permisos |
| CA-02 | CP-004 | De mensaje |
| CA-03 | CP-004 | Que **no** pase |

---

## 6. Casos de prueba

### CP-003 — Los dos grupos y sus permisos

- **Son dos y no cuatro.**
- El usuario puede las cuatro acciones restringidas; el agente, ninguna.
- El agente **sí** puede escribir documentos y abrir fases: es su trabajo.
- Ponerlos al día dos veces seguidas no rompe nada.

### CP-004 — El agente no aprueba

**El caso que decide la fase.**

| Entrada | Se espera |
|---|---|
| El agente intenta aprobar | **No se hace**, y el motivo nombra el permiso, el porqué y el grupo que lo tiene |
| El usuario aprueba | Se hace |
| Un nombre que no es cuenta | **Se rechaza**, diciendo que la constancia diría quién sin probarlo |
| Después de los dos rechazos | **Cero aprobaciones guardadas** |
| El superusuario | Puede, aunque no esté en ningún grupo |

**10 pruebas** cubren estos casos.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Cuentas de mentiras de los dos grupos, en la base de pruebas, y una carpeta temporal como proyecto.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Un agente decidido a saltárselo.** Estos permisos los comprueba la plataforma, no el sistema operativo: quien pueda editar la base o el código puede darse cualquier permiso. Lo que se logra es que saltárselo sea **deliberado y visible**, no un olvido.

---

## 8. Herramientas

El corredor de la plataforma. **Ninguna dependencia nueva.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | El agente aprueba · un rechazo deja algo guardado |
| **Alta** | Se acepta un nombre que no es cuenta |
| **Media** | El rechazo no dice qué permiso falta |

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
| Aprobaciones hechas por el grupo agente | **Cero** |
| Aprobaciones con un nombre que no es cuenta | **Cero** |

### 12.2 Dónde se miden

En las pruebas, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Probar con superusuario | Las pruebas crean cuentas de cada grupo, con los permisos de verdad: entrar con superusuario no comprueba nada sobre permisos |

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
