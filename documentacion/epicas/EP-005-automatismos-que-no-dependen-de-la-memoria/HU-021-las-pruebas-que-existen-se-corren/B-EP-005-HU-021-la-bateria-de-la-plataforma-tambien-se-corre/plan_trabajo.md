# Plan de Trabajo — Fase «B-EP-005-HU-021-la-bateria-de-la-plataforma-tambien-se-corre» (módulo «Pruebas»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-005-HU-021-la-bateria-de-la-plataforma-tambien-se-corre` |
| **Épica** | [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/epica.md](../../epica.md) |
| **HU** | [documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-021-las-pruebas-que-existen-se-corren/HU-021-las-pruebas-que-existen-se-corren.md](../HU-021-las-pruebas-que-existen-se-corren.md) — **una sola** (`F12.1`) |
| **Módulo** | Pruebas |
| **Especificación del módulo** | La HU citada arriba (`02·F19`) |
| **Fecha apertura** | 2026-08-31 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- 📝 **Modifica fase(s):** completa lo que la fase `A` dejó a medias sin saberlo. Aquella puso a correr las 650 pruebas de `validadores/tests/` y dio el trabajo por hecho; **este repositorio tiene dos baterías**, y la otra —las 187 de la plataforma— siguió sin que nada la corriera.

**CA de la HU que cubre esta fase:**

| CA de `HU-021` que cierra esta fase | Estado |
|---|---|
| [CA-01 — La carpeta se corre con una orden, y es la documentada](../HU-021-las-pruebas-que-existen-se-corren.md#ca-01--la-carpeta-se-corre-con-una-orden-y-es-la-documentada) | ☐ |
| [CA-02 — Cero pruebas no pasa por verde](../HU-021-las-pruebas-que-existen-se-corren.md#ca-02--cero-pruebas-no-pasa-por-verde) | ☐ |
| [CA-03 — Se puede pedir un subconjunto](../HU-021-las-pruebas-que-existen-se-corren.md#ca-03--se-puede-pedir-un-subconjunto) | ☐ |

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que la orden que corre las pruebas del estándar corra **las dos baterías** de este repositorio, y que no tener la segunda se diga en vez de saltarse en silencio.

**El caso que lo pide, medido hoy.** La subida a `37.1.0` de la mañana puso en rojo dos de las 187 pruebas de la plataforma. Nadie lo supo hasta la tarde, y solo porque hubo que abrir una fase que tocaba esa carpeta. Es `S-097`.

| Lo medido | Antes | Después |
|---|---|---|
| Pruebas que corre `validar.py internas` | 724 | 724 **más 187** |
| Baterías del repositorio que nada ejecuta | 1 de 2 | 0 de 2 |

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | La orden corre las dos, y dice cuántas de cada una | Funcional | Media |
| CA-02 | Cero pruebas de la plataforma es rojo | **Que NO pase** | Baja |
| CA-03 | Pedir un subconjunto no arrastra la otra batería | Funcional | Baja |

**Fuera de alcance:**

- Fundir las dos baterías en una. Son de dos productos y las corre distinto marco; juntarlas escondería cuál se cayó.
- Correr la batería de la plataforma en el `pre-commit`. La corrida completa ya tiene su sitio, que es el reclamo del `pre-push`.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `validadores/corredor.py` | Modificar | Corredor | `correr_la_plataforma`, y su entrada en `validar` |
| `validadores/tests/test_la_bateria_de_la_plataforma_se_corre.py` | Nuevo | Prueba | Los tres CA |

### 2.2 Matriz de dependencias del refactor

| Archivo a refactorizar | Cambio de contrato | Archivos que dependen | Dónde rompe |
|---|---|---|---|
| `corredor.validar` | El resumen agrega una cifra al final | `validar.py internas`, `test_las_pruebas_que_existen_se_corren.py` | No rompen: el texto viejo sigue completo y solo se le suma |

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| Se le pide a la plataforma **por su punto de entrada** | Cargar sus archivos de prueba desde acá con `unittest` | Su marco arma la base de prueba y descubre las aplicaciones; cargarlos a mano daría un número que nadie más obtiene, y encima distinto |
| **No tener plataforma es aviso, no falla** | Reportarlo como falla | Un proyecto que hereda el estándar no tiene plataforma. Sería un rojo permanente, y un rojo que siempre está se apaga |
| Las dos cifras se dicen **aparte** | Sumarlas en un total | Un solo número escondería cuál de las dos se cayó |
| La otra batería entra **solo en la corrida entera** | Correrla también con `--solo` | Pedir un subconjunto es lo que hace cumplible `02·F5`; arrastrar 187 pruebas ajenas a una fase que toca dos archivos vuelve esa orden un peaje |
| Se acepta que la batería de la plataforma corra **dos veces** en la corrida completa | Que la prueba de integración se salte cuando corre dentro de la batería | Son dos cosas distintas: una es el producto y la otra lo comprueba. Cuesta medio minuto sobre diez, y esconderlo con una condición dejaría la integración sin prueba propia |

### 2.7 Dudas por resolver antes de codificar

Ninguna abierta.

---

## 3. Desglose de tareas por criterio de aceptación

### [CA-01](../HU-021-las-pruebas-que-existen-se-corren.md#ca-01--la-carpeta-se-corre-con-una-orden-y-es-la-documentada) — La orden corre las dos

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `correr_la_plataforma`: le pide por su punto de entrada y lee cuántas corrieron | Corredor | 2 h | — | EV-01 |
| T-02 | Entra en `validar`, con su cifra aparte en el resumen | Corredor | 1 h | T-01 | EV-01 |

### [CA-02](../HU-021-las-pruebas-que-existen-se-corren.md#ca-02--cero-pruebas-no-pasa-por-verde) — Cero pruebas es rojo

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-03 | Cero pruebas de la plataforma: falla. No tenerla: aviso | Corredor | 1 h | T-01 | EV-01 |

### [CA-03](../HU-021-las-pruebas-que-existen-se-corren.md#ca-03--se-puede-pedir-un-subconjunto) — El subconjunto no arrastra la otra

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-04 | Con `--solo`, la otra batería no corre | Corredor | 1 h | T-02 | EV-01 |
| T-05 | Las nueve pruebas de la fase | Test | 2 h | T-04 | EV-01 |
| T-06 | Sabotaje: una prueba de la plataforma en rojo tiene que cazarse | Test | 1 h | T-02 | EV-02 |

**Total estimado:** 8 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-04 → T-05. T-03 y T-06 cuelgan de T-01 y T-02.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| [CA-01](../HU-021-las-pruebas-que-existen-se-corren.md#ca-01--la-carpeta-se-corre-con-una-orden-y-es-la-documentada) | La corrida completa, con las dos cifras | EV-01, EV-03 | | ☐ |
| [CA-02](../HU-021-las-pruebas-que-existen-se-corren.md#ca-02--cero-pruebas-no-pasa-por-verde) | Punto de entrada que no corre nada, y repositorio sin plataforma | EV-01 | | ☐ |
| [CA-03](../HU-021-las-pruebas-que-existen-se-corren.md#ca-03--se-puede-pedir-un-subconjunto) | `--solo` sobre un repositorio chico | EV-01 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las nueve pruebas de la fase | `resultado_pruebas.md` §2 |
| EV-02 | El sabotaje | `resultado_pruebas.md` §2 |
| EV-03 | La corrida completa, con las dos cifras | `resultado_pruebas.md` §2 |

---

## 6. Datos y ambiente de prueba

Repositorios de mentiras que la propia prueba crea y borra, y este repositorio para la corrida de verdad. Ningún dato real.

---

## 7. Reversión / rollback  ·  Q11

Todo versionado. La pieza nueva es aditiva: si se quita, la corrida vuelve a mirar una sola batería.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo, y con una consecuencia buena para quien hereda.** Un proyecto sin plataforma recibe un aviso nuevo que dice que no la tiene. No es una falla, así que no le rompe nada.

---

## 9. Reglas del estándar aplicadas  ·  Q13

- Base: [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`08·T5`](../../../../../base/08-pruebas.md#t5--corre-la-suite-completa-antes-de-cerrar).
- Proyecto: no aplica.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que la corrida completa se vuelva más lenta y alguien la apague | Alto — es el patrón que ya apareció cuatro veces acá | Medio minuto sobre diez. Y la otra batería no entra en el subconjunto, que es la orden del día a día | Cerrado |
| B-02 | Que un proyecto que hereda vea una falla que no le corresponde | Alto | No tener plataforma es **aviso**, nunca falla | Cerrado |

---

## 11. Definition of Done

- [ ] Los tres CA verificados con evidencia
- [ ] Las nueve pruebas en verde
- [ ] El sabotaje comprobado
- [ ] La corrida completa diciendo las dos cifras
- [ ] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
