# Plan de Trabajo — Fase `Q-EP-018-HU-002-corregir-conserva-lo-que-decia-antes` (módulo Memoria)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación. El requisito vive en la HU; las pruebas, en el `plan_pruebas`; lo que quedó hecho, en el `funcionalidad_implementada.md`.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `Q-EP-018-HU-002-corregir-conserva-lo-que-decia-antes` |
| **Épica** | [EP-018](../../epica.md) |
| **HU** | [HU-002 Consultar y corregir lo guardado](../HU-002-consultar-y-corregir-lo-guardado.md), una sola (`F12.1`) |
| **Módulo** | Memoria |
| **Especificación del módulo** | [documentacion/memoria/spec.md](../../../../memoria/spec.md) |
| **Fecha apertura** | 2026-09-01 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- 📋 **Ficha de `F-024`:** *«es un problema de confianza antes que de comodidad: hoy solo el agente ve lo que recuerda»*.

> **El usuario autorizó ejecutar sin aprobar paso por paso** el 2026-09-01.

**CA de la HU que cubre esta fase:** los tres, todos ☑.

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que el usuario pueda corregir un recuerdo y darlo de baja, sin perder qué decía antes.

**Fuera de alcance:** la pantalla, y revisar solo si un recuerdo sigue siendo cierto.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo que ya existe y se reutiliza:** todo lo que dejó la fase `P` — leer, buscar y guardar.

**Lo verificado:** los recuerdos de la carpeta real siguen el formato de `01·C19`, y la marca de baja se puede poner sin romper ninguno.

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/memoria/core.py` | Modificar | Servicio | Corregir y dar de baja |
| `plataforma/nucleo/memoria/management/commands/memoria.py` | Modificar | Consola | Las dos acciones nuevas |
| `plataforma/nucleo/memoria/tests.py` | Modificar | Prueba | Los tres CA |
| `documentacion/memoria/spec.md` | Modificar | Especificación | Su §13 |

**Ninguna entidad y ninguna migración.**

### 2.2 Matriz de dependencias del refactor

`core.py` crece; lo de la fase `P` no cambia, y sus 6 pruebas lo comprueban.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **Corregir deja lo anterior debajo, marcado** | Reemplazar el texto | Un recuerdo corregido cuenta dos cosas, y las dos sirven |
| **Dar de baja marca, no borra** | Borrar el archivo | Lo mismo que hace el estándar con las reglas derogadas (`20·M11`) |
| **La marca va al principio del cuerpo** | Al final, o en el nombre del archivo | Quien abre el archivo tiene que verla antes de leerlo |
| **Lo dado de baja sale de lo vigente, no del listado** | Esconderlo | El usuario tiene que poder verlo para saber que existió |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | Corregir conservando lo anterior | Servicio | 1,5 h | — | CA-02 | EV-01 |
| T-02 | Dar de baja con su marca | Servicio | 1 h | — | CA-03 | EV-01 |
| T-03 | Que lo de baja salga de lo vigente | Servicio | 30 min | T-02 | CA-03 | EV-01 |
| T-04 | Las dos acciones en la consola | Consola | 1 h | T-03 | — | EV-01 |
| T-05 | Las pruebas de los tres CA | Test | 2 h | T-04 | Todos | EV-01 |

**Total estimado:** 6 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-05.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Buscando algo que está y algo que no | EV-01 | 2026-09-01 | ☑ |
| CA-02 | Corrigiendo y leyendo el archivo | EV-01 | 2026-09-01 | ☑ |
| CA-03 | Dando de baja y pidiendo las dos listas | EV-01 | 2026-09-01 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas del módulo | `plataforma/nucleo/memoria/tests.py` |

---

## 6. Datos y ambiente de prueba

Carpetas temporales con recuerdos de mentiras. **La carpeta real no se toca al probar** (`08·T4`).

---

## 7. Reversión / rollback  ·  Q11

**Nada que revertir en los datos:** esta fase no borra ningún archivo, y ese es su punto.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna migración, ninguna dependencia nueva.

---

## 9. Reglas aplicadas  ·  Q13

- Base: `01·C19`, `03·DA-01`, el capítulo [`15`](../../../../../base/15-registros-inmutables.md), y `20·M11` por analogía.
- Producto: las `RN-1` a `RN-4` de la historia.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | **Que corregir borre lo que decía antes** | **Alto: se pierde por qué cambió** | Queda debajo, marcado, y hay prueba | Cerrado |
| B-02 | **Que dar de baja borre el archivo** | **Alto** | Solo le pone la marca, y hay prueba de que el archivo queda | Cerrado |
| B-03 | Que un recuerdo corregido se vuelva ilegible de tanto historial | Bajo | **Se acepta:** un recuerdo con muchas correcciones es una señal de que hacía falta | Declarado |

---

## 11. Definition of Done

- [x] Los tres CA verificados con evidencia
- [x] Comprobado que corregir conserva lo anterior
- [x] Comprobado que dar de baja no borra
- [x] Las dos baterías en verde
- [x] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
