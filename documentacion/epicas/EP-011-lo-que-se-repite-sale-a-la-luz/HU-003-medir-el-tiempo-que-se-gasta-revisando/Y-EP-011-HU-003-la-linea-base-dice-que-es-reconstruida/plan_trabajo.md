# Plan de Trabajo — Fase `Y-EP-011-HU-003-la-linea-base-dice-que-es-reconstruida` (módulo Medición)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación. El requisito vive en la HU; las pruebas, en el `plan_pruebas`; lo que quedó hecho, en el `funcionalidad_implementada.md`.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `Y-EP-011-HU-003-la-linea-base-dice-que-es-reconstruida` |
| **Épica** | [EP-011](../../epica.md) |
| **HU** | [HU-003 Medir el tiempo que se gasta revisando](../HU-003-medir-el-tiempo-que-se-gasta-revisando.md), una sola (`F12.1`) |
| **Módulo** | Medición |
| **Especificación del módulo** | [documentacion/medicion/spec.md](../../../../medicion/spec.md) |
| **Fecha apertura** | 2026-09-01 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- 📋 **Ficha de `F-032`:** *«saber si el proyecto cumplió su objetivo, en vez de suponerlo»*.
- ⚠️ **Y su advertencia, que resultó ser el entregable:** *«la medición inicial debió tomarse antes de empezar y no se tomó: sin ella pierde la mitad del valor»*.

> **El usuario autorizó ejecutar sin aprobar paso por paso** el 2026-09-01.

**CA de la HU que cubre esta fase:** los dos, todos ☑.

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** medir cuánto tiempo se gasta revisando lo entregado, sin que el usuario anote nada.

**Y decir, cada vez, que la línea base no es un antes de verdad.** Es la parte de la funcionalidad que más costó, y no es código: es una frase.

**Fuera de alcance:** reconstruir la medición inicial —no se puede, y decirlo es parte del entregable— y medir el tiempo del agente.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo que ya existe y se reutiliza:** el índice de lo conversado, con 67 sesiones y 3720 mensajes.

**Lo verificado:** **3665 de 3720 mensajes tienen hora de reloj**; los 55 restantes dicen «hora no registrada» o «reconstruido a mano». Y todo el histórico cabe en **un solo mes**, así que no hay contra qué comparar.

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/medicion/revision.py` | Crear | Servicio | Los huecos y la comparación |
| `plataforma/nucleo/medicion/management/commands/cuanto_se_revisa.py` | Crear | Consola | La orden |
| `plataforma/nucleo/medicion/tests_revision.py` | Crear | Prueba | Los dos CA |
| `documentacion/medicion/spec.md` | Modificar | Especificación | Su §13 |

**Ninguna entidad y ninguna migración:** se lee el índice que el módulo ya tenía.

### 2.2 Matriz de dependencias del refactor

**Nada existente se toca.** Esta fase solo lee el índice.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican: órdenes de consola.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **El tiempo sale de las horas ya escritas** | Pedirle al usuario que cronometre | Medir no puede costar más que lo que ahorra: está en la ficha |
| **La línea base sale siempre marcada como reconstruida** | Presentarla como el antes | Una que se presente como un antes de verdad hace que la mejora parezca mayor de lo que es |
| **Un hueco mayor a dos horas no se cuenta** | Contarlo | No es revisión: es que se fue. Convertiría un almuerzo en el mejor dato del reporte |
| **Uno menor a tres segundos tampoco** | Contarlo | Es un «si» o un «siga», no una revisión |
| **La mediana, no el promedio** | El promedio | Un solo hueco largo mueve el promedio; acá los huecos largos son lo normal |
| **Con un solo mes no se compara** | Comparar contra sí mismo | Sería inventar una mejora |

### 2.7 Dudas por resolver antes de codificar

Una, y se resolvió mirando: **si existía algún tramo anterior al proyecto en marcha**. No existe.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | Los huecos entre la respuesta y el mensaje siguiente | Servicio | 1,5 h | — | CA-02 | EV-01 |
| T-02 | Descartar los larguísimos y los de un segundo | Servicio | 1 h | T-01 | Transversal | EV-01 |
| T-03 | Juntar por mes, con mediana | Servicio | 1 h | T-02 | CA-01 | EV-01 |
| T-04 | La línea base, marcada como reconstruida | Servicio | 1 h | T-03 | CA-01 | EV-01 |
| T-05 | Negarse a comparar cuando no hay con qué | Servicio | 1 h | T-04 | Transversal | EV-01 |
| T-06 | La orden de consola | Consola | 1 h | T-05 | — | EV-01 |
| T-07 | Las pruebas de los dos CA | Test | 2 h | T-06 | Todos | EV-01 |

**Total estimado:** 8,5 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-03 → T-04 → T-07.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Con dos meses de sesiones | EV-01 | 2026-09-01 | ☑ |
| CA-02 | Midiendo sin agregar ningún dato | EV-01 | 2026-09-01 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas de la fase | `plataforma/nucleo/medicion/tests_revision.py` |

---

## 6. Datos y ambiente de prueba

Sesiones de mentiras con horas puestas a mano, y **la corrida contra el histórico real**: 67 sesiones y 3720 mensajes.

---

## 7. Reversión / rollback  ·  Q11

**Solo lee.** Se quita el archivo y no queda rastro; ninguna sesión del histórico se modifica.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna migración, ninguna dependencia nueva.

---

## 9. Reglas aplicadas  ·  Q13

- Base: `03·DA-01`, y el capítulo [`12`](../../../../../base/12-privacidad-datos.md), porque lo que se mide son conversaciones.
- Producto: las `RN-1` a `RN-5` de la historia.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | **Que la línea base se lea como un antes de verdad** | **Alto: la mejora parecería mayor** | Sale marcada como reconstruida, cada vez que se muestra | Cerrado |
| B-02 | Que un almuerzo se cuente como cuatro horas de lectura | Alto | Se descarta y se cuenta aparte | Cerrado |
| B-03 | Que se invente una hora donde no la hay | Alto | Los 55 mensajes sin hora se dicen aparte | Cerrado |
| B-04 | **Que la medición inicial no exista** | **Alto, y no tiene arreglo** | **Se declara:** no se tomó, y ninguna reconstrucción la reemplaza | Declarado |

---

## 11. Definition of Done

- [x] Los dos CA verificados con evidencia
- [x] Comprobado que la línea base dice que es reconstruida
- [x] Comprobado que con un mes no se compara
- [x] Las dos baterías en verde
- [x] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
