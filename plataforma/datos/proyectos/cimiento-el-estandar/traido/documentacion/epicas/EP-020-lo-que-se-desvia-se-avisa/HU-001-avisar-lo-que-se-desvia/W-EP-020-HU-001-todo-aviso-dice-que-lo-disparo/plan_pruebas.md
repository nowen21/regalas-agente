# Plan de Pruebas — Fase `W-EP-020-HU-001-todo-aviso-dice-que-lo-disparo`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **con qué casos concretos se comprueba** cada criterio de esta fase y cuándo se da por aprobado. Lo que se pide vive en la [HU-001](../HU-001-avisar-lo-que-se-desvia.md); lo que se va a hacer, en el [plan_trabajo.md](plan_trabajo.md).

---

## 1. Introducción

### 1.1 Propósito

Comprobar que **los avisos salen**, que **cada uno dice qué lo disparó y dónde mirar**, y que **lo atendido no vuelve**.

### 1.2 Alcance

**Entra:** las tres clases, el orden, lo callado, el recorte y el cero.

**No entra:** arreglar lo que se avisa, y la pantalla.

### 1.3 Documentos de referencia

| Documento | Para qué |
|---|---|
| [plan_trabajo.md](plan_trabajo.md) | Las decisiones técnicas |
| [documentacion/avisos/spec.md](../../../../avisos/spec.md) | El módulo |

---

## 2. Elementos a probar

| Elemento | Qué se prueba de él |
|---|---|
| Las tres clases | Cada una con su disparador y su destino |
| El orden | Que lo más grave salga primero |
| Lo callado | Por su causa, y a mano |
| El recorte | Que se diga |

---

## 3. Estrategia de pruebas

### 3.1 Niveles y tipos

| Tipo | Por qué |
|---|---|
| **De contenido** | Todo aviso tiene que traer dos datos, y se comprueban los dos |
| **De que NO pase** | Que un aviso atendido vuelva |

### 3.2 Priorización

| Prioridad | Casos | Por qué |
|---|---|---|
| Crítica | CP-002 | **Un aviso que vuelve después de atendido enseña a ignorar la lista entera** |
| Alta | CP-003 | El ruido es el modo en que esta funcionalidad fracasa |

### 3.3 Alcance de la ejecución automatizada  ·  [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

`plataforma/nucleo/avisos/` entera, y las dos baterías completas.

---

## 4. Criterios de entrada y salida

### 4.1 Criterios de entrada

- `EP-019` cerrada: de ahí sale en qué estación va cada fase.

### 4.2 Criterios de salida

- Todos los casos ejecutados.
- Las dos baterías en verde.

### 4.3 Criterios de suspensión y reanudación

Se suspende si **un aviso sale sin decir qué lo disparó**. Es la exigencia que sostiene la funcionalidad entera.

---

## 5. Matriz de trazabilidad

| CA | Caso | Tipo |
|---|---|---|
| CA-01 y CA-02 | CP-001 | De contenido |
| CA-03 | CP-002 | Que **no** pase |
| Transversal | CP-003 | De control del ruido |

---

## 6. Casos de prueba

### CP-001 — Los tres avisos dicen qué y dónde

- Una fase detenida sale **con los días que lleva**.
- Una historia sin fase sale; una con fase, no.
- Lo construido sin verificar sale; **lo que todavía está en «definida», no**.
- **Todo aviso trae qué lo disparó y dónde mirar**, sin excepción.
- Lo más grave sale primero.

### CP-002 — El aviso atendido no vuelve

**El caso que decide la fase.**

- Callado a mano: no sale, y **se dice cuántos están callados a propósito**.
- Arreglada la causa: tampoco sale.
- Sin avisos, **se dice con palabras**.

### CP-003 — El ruido se controla

- Una fase que lleva poco quieta no avisa.
- Los días se pueden cambiar al pedirlo.
- **Una fase terminada no avisa por más vieja que sea.**
- Cuando la lista se recorta, **se dice**.
- **Una fase que no dice desde cuándo no se da por vencida.**

**13 pruebas** cubren estos casos.

---

## 7. Datos y ambientes de prueba

### 7.1 Ambientes · 7.2 Datos · 7.3 Usuarios

Carpetas temporales con fases, historias e inventarios de mentiras. Y **la corrida contra este repositorio**, que es de solo lectura.

### 7.4 Qué NO reproduce el entorno de pruebas  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

**Cuántos avisos son demasiados.** Las pruebas comprueban que el recorte se avise y que las clases sean tres; **ninguna dice a partir de cuántos avisos la gente deja de leer la lista**. Eso se sabe usándolo, y por eso los 30 días se pueden cambiar al pedirlo.

---

## 8. Herramientas

El corredor de la plataforma. **Ninguna dependencia nueva.**

---

## 9. Gestión de defectos

### 9.1 Clasificación por severidad

| Severidad | Qué es acá |
|---|---|
| **Crítica** | Un aviso sale sin decir qué lo disparó · un aviso atendido vuelve |
| **Alta** | Una fase terminada aparece como deuda |
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
| Avisos sin causa o sin destino | **Cero** |
| Avisos atendidos que vuelven | **Cero** |
| Recortes en silencio | **Cero** |

### 12.2 Dónde se miden

En las pruebas, y escrito en el `resultado_pruebas.md`.

---

## 13. Riesgos del proceso de pruebas

| Riesgo | Qué se hace |
|---|---|
| Probar solo que los avisos salgan | La mitad de los casos comprueban que **no** salgan |
| Probar con datos de mentiras nada más | Se corrió contra este repositorio, y ahí apareció lo que nadie veía |

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
