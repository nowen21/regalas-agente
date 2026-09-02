# Plan de Pruebas — Fase `N-EP-017-HU-002-los-tres-estados-se-dicen-con-palabras`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [HU-002](../HU-002-ver-que-esta-aprobado-y-que-no.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que los tres estados se distinguen, **que se dicen con palabras**, y que un documento sin aprobación aparece así y no vacío.

### 1.2 Alcance

**Entra:** los tres estados, sus frases, y la lista de varios documentos.

**No entra:** la pantalla.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las cuatro decisiones técnicas |
| [documentacion/aprobaciones/spec.md](../../../../aprobaciones/spec.md) | La §5.1: los tres estados |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| Los tres estados | Que cada uno salga cuando toca |
| Sus frases | **Que existan las tres** |
| La de caducada | Que diga por qué |
| Lo sin aprobación | Que aparezca, no que falte |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De partición** | Los tres estados, cada uno |
| **De accesibilidad** | Que la palabra exista, no solo el valor |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-005 | **Quien no distingue colores tiene que poder saberlo** |
| Alta | CP-005 (sin aprobación) | Un vacío se leería como un fallo de la consulta |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/aprobaciones/` entera, y las dos baterías completas.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- La fase anterior cerrada, con la aprobación y su huella.

### 4.2 Criterios de salida

- El caso ejecutado, con sus cuatro comprobaciones.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **algún estado no tiene frase**. Sin ella, el estado solo se puede leer si se ve el color.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01, CA-02 y CA-03 | CP-005 | De partición |

---

## 6. Casos de prueba

### CP-005 — Los tres estados se dicen con palabras

| Entrada | Se espera |
|---|---|
| Un documento sin aprobación | Sale, y dice que nadie lo ha aprobado |
| Los tres estados | **Cada uno con su frase** |
| La frase de caducada | Dice que el documento cambió |
| Varios documentos a la vez | Todos salen, cada uno con el suyo |

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Carpetas temporales con documentos de mentiras.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Si las frases se entienden.** Que existan se prueba; que sirvan lo dice quien las lea.

---

## 8. Herramientas

El corredor de la plataforma. **Ninguna dependencia nueva.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | Un estado sin frase |
| **Alta** | Lo sin aprobación no aparece |
| **Media** | La frase de caducada no dice por qué |

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
| Estados sin frase | **Cero** |
| Documentos sin aprobación que salen vacíos | **Cero** |

### 12.2 Dónde se miden

En las pruebas, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Probar solo el estado aprobado | Se prueban los tres |

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
