# Plan de Trabajo — Fase `N-EP-017-HU-002-los-tres-estados-se-dicen-con-palabras` (módulo Aprobaciones)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación. El requisito vive en la HU; las pruebas, en el `plan_pruebas`; lo que quedó hecho, en el `funcionalidad_implementada.md`.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `N-EP-017-HU-002-los-tres-estados-se-dicen-con-palabras` |
| **Épica** | [EP-017](../../epica.md) |
| **HU** | [HU-002 Ver qué está aprobado y qué no](../HU-002-ver-que-esta-aprobado-y-que-no.md), una sola (`F12.1`) |
| **Módulo** | Aprobaciones |
| **Especificación del módulo** | [documentacion/aprobaciones/spec.md](../../../../aprobaciones/spec.md) |
| **Fecha apertura** | 2026-09-01 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- ✨ **Funcionalidad nueva:** `F-016`. Su ficha pide que se diga **con palabras, no solo con color**.

> **El usuario autorizó ejecutar sin aprobar paso por paso** el 2026-09-01.

**CA de la HU que cubre esta fase:** los tres, todos ☑.

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que de cada documento se sepa si está aprobado, si su aprobación caducó, o si nadie lo ha mirado.

**Son tres estados, no dos.** «Caducada» dice que hubo un juicio y que algo lo invalidó; «sin aprobación», que nunca lo hubo. Confundirlas pierde información.

**Fuera de alcance:** la pantalla, y juzgar si algo debería estar aprobado.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo que ya existe y se reutiliza:** la aprobación con su huella, de la fase anterior.

**Lo verificado el 2026-09-01:** la ficha de `F-016` exige decirlo con palabras, y el motivo está escrito ahí: **quien no distingue colores tiene que poder saberlo**.

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/aprobaciones/core.py` | Modificar | Servicio | Los tres estados y sus frases |
| `plataforma/nucleo/aprobaciones/management/commands/aprobaciones.py` | Nuevo | Orden | Mostrarlos |
| `plataforma/nucleo/aprobaciones/tests.py` | Modificar | Prueba | Los tres CA |

**Ninguna entidad nueva y ninguna migración.**

### 2.2 Matriz de dependencias del refactor

`core.py` crece; lo que ya tenía no cambia, y sus pruebas lo comprueban.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **Tres estados, no dos** | Aprobado / no aprobado | «Caducada» y «sin aprobación» son cosas distintas |
| **Cada estado con su frase** | Solo la palabra | Quien no distingue colores tiene que poder saberlo |
| **La frase de caducada dice por qué** | Decir solo que caducó | Lo primero que hay que ver es qué cambió |
| **Un documento sin aprobación aparece** | No listarlo | Un vacío se leería como un error de la consulta |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | Los tres estados, con su frase | Servicio | 1 h | — | CA-01 | EV-01 |
| T-02 | Comparar la huella de lo que hay | Servicio | 1 h | T-01 | CA-01 | EV-01 |
| T-03 | Decir desde cuándo y por quién | Servicio | 1 h | T-02 | CA-02 | EV-01 |
| T-04 | Que lo sin aprobación aparezca | Servicio | 1 h | T-01 | CA-03 | EV-01 |
| T-05 | La orden de consola | Orden | 1 h | T-04 | Todos | EV-02 |
| T-06 | Las pruebas de los tres CA | Test | 2 h | T-05 | Todos | EV-01 |

**Total estimado:** 7 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-05.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Con uno aprobado y uno sin aprobar | EV-01 | 2026-09-01 | ☑ |
| CA-02 | Aprobando y consultando | EV-01 | 2026-09-01 | ☑ |
| CA-03 | Con un documento que nadie aprobó | EV-01 | 2026-09-01 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas del módulo | `plataforma/nucleo/aprobaciones/tests.py` |
| EV-02 | La orden de consola | `resultado_pruebas.md` §2 |

---

## 6. Datos y ambiente de prueba

Carpetas temporales con documentos de mentiras.

---

## 7. Reversión / rollback  ·  Q11

Nada que revertir: esta fase solo lee.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna migración, ninguna dependencia nueva.

---

## 9. Reglas aplicadas  ·  Q13

- Base: [`17`](../../../../../base/17-interfaz.md), por lo de no comunicar solo con color.
- Producto: las `RN-1` a `RN-4` de la historia.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | **Que el estado se comunique solo con color** | **Alto** | Los tres estados tienen su frase, y hay prueba de ello | Cerrado |
| B-02 | Que lo sin aprobación salga vacío | Alto | Aparece con su frase | Cerrado |
| B-03 | Que se confunda caducada con sin aprobación | Medio | Son valores distintos, con frases distintas | Cerrado |

---

## 11. Definition of Done

- [x] Los tres CA verificados con evidencia
- [x] Comprobado que los tres estados tienen su frase
- [x] Las dos baterías en verde
- [x] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
