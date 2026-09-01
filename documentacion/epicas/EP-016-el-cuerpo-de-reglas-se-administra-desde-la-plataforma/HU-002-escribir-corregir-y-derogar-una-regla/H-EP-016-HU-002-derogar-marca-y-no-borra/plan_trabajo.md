# Plan de Trabajo — Fase `H-EP-016-HU-002-derogar-marca-y-no-borra` (módulo Reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación. El requisito vive en la HU; las pruebas, en el `plan_pruebas`; lo que quedó hecho, en el `funcionalidad_implementada.md`.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `H-EP-016-HU-002-derogar-marca-y-no-borra` |
| **Épica** | [EP-016](../../epica.md) |
| **HU** | [HU-002 Escribir, corregir y derogar una regla](../HU-002-escribir-corregir-y-derogar-una-regla.md) — **una sola** (`F12.1`) |
| **Módulo** | Reglas |
| **Especificación del módulo** | [documentacion/reglas/spec.md](../../../../reglas/spec.md) |
| **Fecha apertura** | 2026-09-01 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- ✨ **Funcionalidad nueva:** `F-005`, la que la ficha llama lo difícil de la épica.

> **El usuario autorizó ejecutar sin aprobar paso por paso** el 2026-09-01.

**CA de la HU que cubre esta fase:** los tres, todos ☑.

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que una regla se escriba y se derogue desde la plataforma, sin borrar nada y viendo antes las que hablan de lo mismo.

**Lo difícil no es escribir.** Lo dice la ficha: *«escribir la regla es lo fácil; lo que cuesta es que no repita ni contradiga a otra»*. Con 248 vigentes, nadie las tiene todas en la cabeza.

**Y hay un límite que se declara antes de construir:** la plataforma **no detecta contradicciones**. Pone al lado las que hablan de lo mismo. Llamarlo detector sería peor que no tenerlo.

**Fuera de alcance:** el checklist y su sello, que es `F-007`.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo que ya existe y se reutiliza:**

| Pieza | Qué aporta |
|---|---|
| `reglas/numeracion.py` | El identificador, de la fase anterior |
| `reglas/catalogo.py` | El puente hacia el lector del estándar |
| `nucleo/auditoria/` | El registro de lo que se escribe |
| `nucleo/ciclo_de_vida/` | Puede llenar los huecos con que nace la regla |

**Lo verificado el 2026-09-01:**

| Qué se comprobó | Resultado |
|---|---|
| El formato canónico de una regla | Encabezado, cuerpo de una exigencia, y ejemplo INCORRECTO/CORRECTO |
| La marca de derogación | `[DEROGADA en <versión> → ver <a dónde>]`, en el encabezado |
| Reglas vigentes contra las que comparar | **248** |
| Reglas blindadas | **9** |

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/reglas/redaccion.py` | Nuevo | Servicio | Escribir y derogar |
| `plataforma/nucleo/reglas/parecidas.py` | Nuevo | Servicio | Las que hablan de lo mismo |
| `plataforma/nucleo/reglas/management/commands/nueva_regla.py` | Nuevo | Orden | Escribir |
| `plataforma/nucleo/reglas/management/commands/derogar_regla.py` | Nuevo | Orden | Derogar |
| `plataforma/nucleo/reglas/tests_redaccion.py` | Nuevo | Prueba | Los tres CA |
| `documentacion/reglas/spec.md` | Modificar | Especificación | Su §13, para nombrar la fase |

**Ninguna entidad y ninguna migración.**

### 2.2 Matriz de dependencias del refactor

`numeracion.py` y `catalogo.py` no se tocan: esta fase los usa.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **Se muestran las parecidas, y se dice que no detecta contradicciones** | Llamarlo detector | Quien confía en un detector deja de mirar, y las que se le escapan pasan sin revisar |
| **La regla nace con sus huecos puestos** | Nacer vacía | Una regla incompleta que no se nota se publica incompleta |
| **Derogar reescribe el encabezado y conserva el texto** | Mover la regla a otro sitio | Lo que se mueve se pierde de vista; lo que se marca se sigue leyendo donde estaba |
| **Una blindada no se deroga desde acá** | Dejarlo pasar | Sostienen a las demás, y derogarlas por una orden de consola es demasiado fácil |
| **Sin `--igual-la-escribo` no se escribe nada** | Escribir de una | La orden sirve primero para mirar; escribir es la segunda intención |
| **Las palabras vacías se declaran en el código** | Una lista genérica de otro idioma | Las que sobran acá son las del vocabulario de las reglas: «regla», «debe», «queda» |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | El molde canónico, con sus huecos | Servicio | 1 h | — | CA-01 | EV-01 |
| T-02 | Escribir la regla, pidiendo el identificador antes | Servicio | 2 h | T-01 | CA-01 | EV-01 |
| T-03 | Derogar: marcar y conservar | Servicio | 2 h | — | CA-02 | EV-01 |
| T-04 | Impedir derogar una blindada o una ya derogada | Servicio | 1 h | T-03 | CA-02 | EV-01 |
| T-05 | Las reglas que hablan de lo mismo | Servicio | 2 h | — | CA-03 | EV-01 |
| T-06 | El aviso de lo que eso no puede decir | Servicio | 1 h | T-05 | CA-03 | EV-01 |
| T-07 | Las dos órdenes de consola | Orden | 2 h | T-02, T-03 | Todos | EV-02 |
| T-08 | Las pruebas de los tres CA | Test | 2 h | T-07 | Todos | EV-01 |
| T-09 | **Correrlo sobre el cuerpo de reglas real** | Medición | 1 h | T-07 | CA-03 | EV-02 |

**Total estimado:** 14 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-07 → T-09. T-03 y T-05 van en paralelo.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Escribiendo una en un cuerpo de prueba, y leyendo el archivo | EV-01 | 2026-09-01 | ☑ |
| CA-02 | Derogando una y leyendo el archivo entero | EV-01 | 2026-09-01 | ☑ |
| CA-03 | **Con el título de una regla que ya existe, sobre el cuerpo real** | EV-01, EV-02 | 2026-09-01 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas de escribir y derogar | `plataforma/nucleo/reglas/tests_redaccion.py` |
| EV-02 | La corrida sobre el cuerpo real | `resultado_pruebas.md` §1 |

---

## 6. Datos y ambiente de prueba

Un cuerpo de reglas de mentiras para escribir y derogar, y **el cuerpo real solo para mirar** las parecidas. Ninguna regla real se toca.

---

## 7. Reversión / rollback  ·  Q11

Lo que esta fase escriba queda en archivos versionados. **En las pruebas nunca escribe sobre el cuerpo real.**

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna migración, ninguna dependencia nueva.

---

## 9. Reglas aplicadas  ·  Q13

- Base: [`20·M11`](../../../../../base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md) y [`20·M5`](../../../../../base/20-meta-reglas/reglas/M5-toda-regla-se-escribe-en-el-mismo-formato.md), que son las que mandan acá.
- Producto: las `RN-1` a `RN-6` de la historia.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | **Que alguien crea que detecta contradicciones** | **Alto — deja de mirar** | El aviso lo dice cada vez, incluso cuando no encuentra nada | Cerrado por diseño |
| B-02 | Que derogar pierda el texto | **Alto — no se deshace** | El `CA-02` lee el archivo entero después | Cerrado |
| B-03 | Que se derogue una blindada | Alto | Está impedido, y se dice por qué | Cerrado |
| B-04 | Que la lista de parecidas se llene de coincidencias sin sentido | Medio | Palabras vacías declaradas, y un mínimo de dos en común | Abierto hasta T-09 |

---

## 11. Definition of Done

- [x] Los tres CA verificados con evidencia
- [x] Corrido sobre el cuerpo de reglas real
- [x] Comprobado que derogar conserva el texto
- [x] Las dos baterías en verde
- [x] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
