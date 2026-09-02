# Plan de Trabajo — Fase `W-EP-020-HU-001-todo-aviso-dice-que-lo-disparo` (módulo Avisos)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación. El requisito vive en la HU; las pruebas, en el `plan_pruebas`; lo que quedó hecho, en el `funcionalidad_implementada.md`.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `W-EP-020-HU-001-todo-aviso-dice-que-lo-disparo` |
| **Épica** | [EP-020](../../epica.md) |
| **HU** | [HU-001 Avisar lo que se desvía](../HU-001-avisar-lo-que-se-desvia.md), una sola (`F12.1`) |
| **Módulo** | Avisos |
| **Especificación del módulo** | [documentacion/avisos/spec.md](../../../../avisos/spec.md) |
| **Fecha apertura** | 2026-09-01 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- 📋 **Ficha de `F-029`:** *«que enterarse no dependa de ir a mirar»*, y su advertencia: *«demasiados avisos se vuelven ruido, y el ruido se ignora completo»*.
- 🩹 **Medido acá el 2026-09-01:** 3 historias escritas sin ninguna fase, y 28 funcionalidades construidas sin verificar. Todo estaba escrito, y nadie lo había leído.

> **El usuario autorizó ejecutar sin aprobar paso por paso** el 2026-09-01.

**CA de la HU que cubre esta fase:** los tres, todos ☑.

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que lo que se salió de lo acordado salga solo, ordenado por lo que más duele.

**El límite lo pone la ficha:** demasiados avisos se ignoran completos. Por eso son tres clases y no quince, y por eso **un aviso que no puede decir qué lo disparó no se emite**.

**Fuera de alcance:** arreglar lo que se avisa, mandarlo por correo, y la pantalla.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo que ya existe y se reutiliza:** la lectura de estaciones de `EP-019`, que dice qué fases están sin cerrar y desde cuándo.

**Lo verificado, y es lo que definió las tres clases:** el repositorio tiene 209 fases, 3 historias sin ninguna fase y 28 funcionalidades construidas sin verificar. **Ninguna deuda tiene fecha de vencimiento**, porque el estándar nunca se la pidió.

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/avisos/core.py` | Crear | Servicio | Las tres clases |
| `plataforma/nucleo/avisos/apps.py` | Crear | Módulo | Nace el módulo |
| `plataforma/nucleo/avisos/management/commands/avisos.py` | Crear | Consola | La orden |
| `plataforma/nucleo/avisos/tests.py` | Crear | Prueba | Los tres CA |
| `plataforma/config/settings/base.py` | Modificar | Configuración | Registrar el módulo |
| `documentacion/avisos/spec.md` | Crear | Especificación | El módulo |

**Ninguna entidad y ninguna migración:** todo aviso se calcula al pedirlo, `DA-01`.

### 2.2 Matriz de dependencias del refactor

**Nada existente se toca.** El módulo lee lo que otros ya escribieron.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican: órdenes de consola.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **Tres clases de aviso, no quince** | Una por cada cosa que puede salir mal | El ruido se ignora completo, y entonces también lo que importaba |
| **Un aviso que no puede decir qué lo disparó no se emite** | Emitirlo igual | Un aviso sin causa obliga a buscarla, y nadie busca |
| **«Vencida» son 30 días sin moverse** | Esperar a que el estándar le ponga fecha a la deuda | Es lo único que el texto sabe. Se declara, para que no se lea como un vencimiento acordado |
| **Lo callado se escribe en el proyecto** | Guardarlo en la base | Una decisión que no viaja con el repositorio se pierde al clonarlo |
| **La fase que no dice desde cuándo no se da por vencida** | Contarla como vencida | No se sabe, y no saber tiene su propio nombre |
| **Cuando recorta, lo dice** | Recortar en silencio | Un tope callado se lee como «eso es todo lo que hay» (`S-113`) |

### 2.7 Dudas por resolver antes de codificar

Una, y hubo que resolverla antes de codificar: **el estándar nunca le puso fecha a una deuda**, así que «vencida» no estaba definida. Se definió acá, y sale escrita en el reporte.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | Las fases detenidas | Servicio | 1 h | — | CA-01 | EV-01 |
| T-02 | Las historias sin fase | Servicio | 1 h | — | CA-02 | EV-01 |
| T-03 | Lo construido sin verificar | Servicio | 1 h | — | CA-02 | EV-01 |
| T-04 | Ordenar por lo que más duele | Servicio | 30 min | T-03 | CA-02 | EV-01 |
| T-05 | Leer lo callado a propósito | Servicio | 1 h | T-04 | CA-03 | EV-01 |
| T-06 | Decir cuando recorta y cuando no hay nada | Servicio | 30 min | T-05 | Transversal | EV-01 |
| T-07 | La orden de consola | Consola | 1 h | T-06 | — | EV-01 |
| T-08 | Las pruebas de los tres CA | Test | 2 h | T-07 | Todos | EV-01 |

**Total estimado:** 8 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-04 → T-05 → T-08.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Con una fase vieja y otra reciente | EV-01 | 2026-09-01 | ☑ |
| CA-02 | Recorriendo los tres tipos de aviso | EV-01 | 2026-09-01 | ☑ |
| CA-03 | Arreglando la causa de uno y callando otro | EV-01 | 2026-09-01 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas de la fase | `plataforma/nucleo/avisos/tests.py` |

---

## 6. Datos y ambiente de prueba

Carpetas temporales con fases, historias e inventarios de mentiras. Y **la corrida contra este repositorio**, que es de solo lectura.

---

## 7. Reversión / rollback  ·  Q11

**Módulo nuevo y de solo lectura.** Se quita y no queda rastro; lo único que escribe es el archivo de avisos callados, y lo escribe el usuario.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna migración, ninguna dependencia nueva.

---

## 9. Reglas aplicadas  ·  Q13

- Base: `03·DA-01` (el texto es la verdad) y el capítulo [`15`](../../../../../base/15-registros-inmutables.md), porque lo callado deja rastro.
- Producto: las `RN-1` a `RN-5` de la historia.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | **Que demasiados avisos se vuelvan ruido** | **Alto: se ignora la lista entera** | Tres clases, y ninguna sin causa ni sin destino | Cerrado |
| B-02 | Que un aviso atendido vuelva | Alto | Se calla por su causa, o a mano con el porqué escrito | Cerrado |
| B-03 | Que «vencida» se lea como un vencimiento acordado | Medio | Sale con su definición, siempre | Cerrado |
| B-04 | Que un recorte callado parezca la lista completa | Medio | Cuando recorta, lo dice | Cerrado |

---

## 11. Definition of Done

- [x] Los tres CA verificados con evidencia
- [x] Comprobado que todo aviso dice qué lo disparó y dónde mirar
- [x] Comprobado que lo atendido no vuelve
- [x] Las dos baterías en verde
- [x] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
