# Plan de Trabajo — Fase `Z-EP-021-HU-001-lo-vacio-se-dice` (módulo Avisos, Ciclo de vida, Comprobaciones, Aprobaciones y Memoria)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación. El requisito vive en la HU; las pruebas, en el `plan_pruebas`; lo que quedó hecho, en el `funcionalidad_implementada.md`.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `Z-EP-021-HU-001-lo-vacio-se-dice` |
| **Épica** | [EP-021](../../epica.md) |
| **HU** | [HU-001 Ver el estado sin abrir la consola](../HU-001-ver-el-estado-sin-abrir-la-consola.md), una sola (`F12.1`) |
| **Módulo** | Avisos, Ciclo de vida, Comprobaciones, Aprobaciones y Memoria |
| **Especificación del módulo** | [documentacion/avisos/spec.md](../../../../avisos/spec.md) |
| **Fecha apertura** | 2026-09-01 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- 💬 **Una pregunta del usuario:** «qué sigue».
- 📋 **Y cuatro fichas que lo piden por escrito:** `F-012`, `F-024`, `F-029` y `F-030` dicen «Pantalla y lógica» en su casilla de qué necesita construirse. La lógica estaba; la pantalla no.

> **El usuario autorizó ejecutar sin aprobar paso por paso** el 2026-09-01.

**CA de la HU que cubre esta fase:** los tres, todos ☑.

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que lo que la plataforma ya sabe se pueda mirar sin abrir una consola.

**Son pantallas de solo mirar.** Aprobar, corregir un recuerdo o abrir una fase son cambios de estado, y `00·N1` los quiere con su confirmación: siguen por consola.

**Fuera de alcance:** cambiar algo desde la pantalla, y los seis módulos que siguen sin ella: Auditoría, Medición, Expediente, Reglas, Seguridad y Almacén.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo verificado antes de empezar:** el repositorio tiene **trece módulos** y solo **dos con pantalla de verdad** —Proyectos e Importación—. El tercero con `views.py` es Almacén, y su única vista es la que responde si la plataforma está viva.

**Y cinco especificaciones decían «sin pantalla todavía»**, que dejó de ser cierto al cerrar esta fase.

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/avisos/views.py` | Crear | Vista | El tablero |
| `plataforma/nucleo/ciclo_de_vida/views.py` | Crear | Vista | Las fases |
| `plataforma/nucleo/comprobaciones/views.py` | Crear | Vista | Las funcionalidades |
| `plataforma/nucleo/aprobaciones/views.py` | Crear | Vista | Las aprobaciones |
| `plataforma/nucleo/memoria/views.py` | Crear | Vista | La memoria |
| `plataforma/templates/…` | Crear | Plantilla | Cinco, una por pantalla |
| `plataforma/config/urls.py` | Modificar | Rutas | Las cinco, **antes de la comodín** |
| `plataforma/templates/base.html` y `proyectos/uno.html` | Modificar | Plantilla | Los enlaces |
| Las cinco `spec.md` | Modificar | Especificación | Su §7 dejó de ser cierta |

**Ninguna entidad y ninguna migración:** las pantallas no guardan; muestran lo que los módulos calculan.

### 2.2 Matriz de dependencias del refactor

**Ninguna lógica se movió ni se duplicó.** Las cinco vistas llaman a funciones que ya existían y estaban probadas.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican: órdenes de consola.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **Las vistas piden, no calculan** | Calcular en la vista lo que hace falta mostrar | Lógica en dos lugares es lógica que un día dirá dos cosas |
| **Solo mirar; nada se cambia desde la pantalla** | Botones de aprobar, corregir, abrir | Son cambios de estado, y `00·N1` los quiere con confirmación. Hacerlos ahora sería media confirmación |
| **Las rutas nuevas van antes de la comodín** | Ponerlas al final | `proyecto/<id>/<que>/` se traga cualquier segmento: puestas después, ninguna respondería |
| **Las advertencias van impresas con los datos** | Dejarlas en la especificación | Una advertencia que vive en otro archivo no se lee |
| **Nada sale a la red** | Traer estilos o tipografías de afuera | La plataforma tiene que servir sin conexión |

### 2.7 Dudas por resolver antes de codificar

Una: **cuántas pantallas.** Se resolvió por lo que las fichas piden por escrito —cuatro— más la de comprobaciones, que es la que responde si algo está verificado. Los otros seis módulos quedan declarados sin pantalla.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | El tablero, con los avisos y el reporte | Vista | 1,5 h | — | CA-01 | EV-01 |
| T-02 | Las fases, con su estación y su puerta | Vista | 1,5 h | — | CA-01 | EV-01 |
| T-03 | Las funcionalidades, con su porqué | Vista | 1 h | — | CA-01 | EV-01 |
| T-04 | Las aprobaciones y la memoria | Vista | 1,5 h | — | CA-01 | EV-01 |
| T-05 | El caso vacío de cada una | Plantilla | 1,5 h | T-04 | CA-02 | EV-01 |
| T-06 | Que ninguna escriba cero donde no se sabe | Plantilla | 1 h | T-05 | CA-03 | EV-01 |
| T-07 | Las rutas y los enlaces | Rutas | 1 h | T-06 | CA-01 | EV-01 |
| T-08 | Las pruebas de los tres CA | Test | 2 h | T-07 | Todos | EV-01 |
| T-09 | Las cinco §7 de las especificaciones | Documentación | 1 h | T-08 | — | — |

**Total estimado:** 12 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-05 → T-06 → T-08. **Lo que costó no fue mostrar: fue el caso vacío**, que son cinco casos distintos y cada uno se dice distinto.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Pidiendo las cinco y mirando los enlaces | EV-01 | 2026-09-02 | ☑ |
| CA-02 | Con un proyecto recién conectado, sin nada escrito | EV-01 | 2026-09-02 | ☑ |
| CA-03 | Con un proyecto sin datos y una fase sin fecha | EV-01 | 2026-09-02 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas de la fase | `plataforma/nucleo/avisos/tests_pantallas.py` |

---

## 6. Datos y ambiente de prueba

Un proyecto de mentiras en una carpeta temporal, y el cliente de pruebas de Django pidiendo las cinco direcciones.

---

## 7. Reversión / rollback  ·  Q11

**Cinco vistas y cinco plantillas.** Se quitan sus rutas y la plataforma queda como estaba; ninguna escribe nada.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna migración, ninguna dependencia nueva.

---

## 9. Reglas aplicadas  ·  Q13

- Base: `00·N1` (ningún cambio de estado sin aprobación) y el `RNF-03` del producto, que pide servir sin conexión.
- Producto: las `RN-1` a `RN-6` de la historia.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | **Que una pantalla vacía se lea como una falla de la plataforma** | **Alto: se desconfía de todo lo demás** | Cada una dice que está vacía y por qué, con prueba propia | Cerrado |
| B-02 | **Que una pantalla dé a entender que muestra todo** | Alto | Cada una dice qué deja por fuera | Cerrado |
| B-03 | Que un «no se sabe» salga como cero | Alto | Sale «sin datos» o «no lo dice» | Cerrado |
| B-04 | Que la ruta comodín se trague las nuevas | Alto | Van antes, y hay prueba de que las cinco responden | Cerrado |
| B-05 | Que seis módulos se queden sin pantalla y nadie lo note | Medio | **Se declara** en la épica y en la historia | Declarado |

---

## 11. Definition of Done

- [x] Los tres CA verificados con evidencia
- [x] Comprobado que lo vacío se dice
- [x] Comprobado que ninguna escribe cero donde no se sabe
- [x] Las cinco §7 puestas al día
- [x] Las dos baterías en verde
- [x] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
