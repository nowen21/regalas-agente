# Plan de Trabajo — Fase «A-EP-012-HU-002-el-entregable-sale-del-texto» (módulo «Expediente»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación antes de darlo por cumplido. El requisito vive en la HU; el detalle de las pruebas, en el `plan_pruebas` de esta misma fase; lo que quedó hecho, en el `funcionalidad_implementada.md` del cierre.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-012-HU-002-el-entregable-sale-del-texto` |
| **Épica** | [documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/epica.md](../../epica.md) |
| **HU** | [documentacion/epicas/EP-012-el-expediente-se-entrega-el-mismo-dia/HU-002-generar-el-entregable-de-ofimatica/HU-002-generar-el-entregable-de-ofimatica.md](../HU-002-generar-el-entregable-de-ofimatica.md) — **una sola** (`F12.1`) |
| **Módulo** | Expediente |
| **Especificación del módulo** | [documentacion/expediente/spec.md](../../../../expediente/spec.md), aprobada el 2026-08-31 |
| **Fecha apertura** | 2026-08-31 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- ✨ **Funcionalidad nueva:** `F-026`, la segunda obligatoria de la versión 2 y lo que esa versión promete como valor.

**CA de la HU que cubre esta fase:**

| CA de `HU-002` que cierra esta fase | Estado |
|---|---|
| [CA-01 — Un expediente completo se genera con todas sus secciones](../HU-002-generar-el-entregable-de-ofimatica.md#ca-01--un-expediente-completo-se-genera-con-todas-sus-secciones) | ☐ |
| [CA-02 — Las listas y las tablas salen como listas y tablas](../HU-002-generar-el-entregable-de-ofimatica.md#ca-02--las-listas-y-las-tablas-salen-como-listas-y-tablas) | ☐ |
| [CA-03 — Generar dos veces da el mismo resultado](../HU-002-generar-el-entregable-de-ofimatica.md#ca-03--generar-dos-veces-da-el-mismo-resultado) | ☐ |
| [CA-04 — Con espacios sin llenar, avisa antes de generar](../HU-002-generar-el-entregable-de-ofimatica.md#ca-04--con-espacios-sin-llenar-avisa-antes-de-generar) | ☐ |

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que el expediente se convierta en un archivo que el cliente abre, generado desde el texto, sin escribir una línea a mano.

**La decisión que gobierna la fase, tomada antes de empezar.** Se generó **con la librería estándar y nada más**. Al abrir la fase se encontró que `markdown` ya está instalado en esta máquina, aunque no es dependencia declarada de la plataforma; se le dijo al usuario y **mantuvo la decisión**, por un motivo escrito: el entregable es lo único que sale hacia un tercero, y `CA-03` exige que dos corridas den el mismo archivo. Con una biblioteca de por medio, una actualización cambia lo que el cliente ve sin que nadie lo pida.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Todas las secciones, en orden | Funcional | Media |
| CA-02 | **Sin marcas del origen a la vista** | Funcional | **Alta** |
| CA-03 | Dos corridas, un archivo | Funcional | Media |
| CA-04 | Avisa y no impide | Funcional | Baja |

**Fuera de alcance:**

- Recibir cambios hechos encima del entregable. Es la pérdida que `DA-09` declara.
- Elegir la plantilla visual del cliente.
- Pantalla.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo que ya existe:** el expediente armado por la fase anterior — 762 documentos de este repositorio, con sus tres listas —, el almacén que guarda con constancia, y la auditoría que la emite.

**Lo que hay que convertir, contado sobre lo real:** los documentos usan encabezados, tablas, listas, negrita, código, enlaces, citas y bloques cercados. **Casi toda tabla lleva listas adentro**, escritas con un separador porque una celda no tiene renglones.

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/expediente/marcado.py` | Nuevo | Servicio | El convertidor, con la librería estándar |
| `plataforma/nucleo/expediente/entregable.py` | Nuevo | Servicio | Arma el archivo y lo guarda con constancia |
| `plataforma/nucleo/expediente/management/commands/generar_entregable.py` | Nuevo | Orden | Pedirlo desde la consola |
| `plataforma/nucleo/expediente/tests_entregable.py` | Nuevo | Prueba | Los cuatro CA |

### 2.2 Matriz de dependencias del refactor

No aplica: todo es nuevo. Lee el expediente y escribe un archivo propio.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **Con la librería estándar** | Declarar una biblioteca de conversión | Decisión del usuario, mantenida al saber que ya estaba instalada. Una actualización cambiaría lo que el cliente ve |
| **Se convierte lo que los documentos usan, no un lenguaje entero** | Cubrirlo todo | Convertir todo sería rehacer lo que ya existe; convertir lo que se usa se puede comprobar |
| **Lo que no se reconoce se deja como texto, escapado** | Adivinar la etiqueta | Un convertidor que adivina produce un documento que se ve bien y dice otra cosa |
| **La fecha de generación no va dentro del archivo** | Ponerla en el pie | Haría distintos dos archivos idénticos, y `CA-03` no se podría comprobar más que de palabra. Cuándo se generó vive en la auditoría |
| **Lo que falta va dentro del archivo**, no solo en la consola | Dejarlo en la salida de la orden | Quien lo recibe tiene que ver lo mismo que vio quien lo generó |
| **Nada que salga a la red en el archivo** | Fuentes o estilos de un servidor | Un entregable que necesita internet para verse bien no es un entregable |

### 2.7 Dudas por resolver antes de codificar

Ninguna abierta: la de con qué se genera se resolvió antes de abrir la fase.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | El convertidor: encabezados, párrafos, listas, citas, código | Servicio | 3 h | — | CA-01 | EV-01 |
| T-02 | **Tablas, y listas dentro de una celda** | Servicio | 3 h | T-01 | CA-02 | EV-01 |
| T-03 | La envoltura del archivo, sin nada de la red | Servicio | 2 h | T-02 | CA-01 | EV-01 |
| T-04 | El índice del entregable, y lo que falta adentro | Servicio | 2 h | T-03 | CA-04 | EV-01 |
| T-05 | Guardar con constancia y registrar en la auditoría | Servicio | 1 h | T-03 | — | EV-01 |
| T-06 | La orden de consola, con los avisos antes de la ruta | Orden | 1 h | T-05 | CA-04 | EV-02 |
| T-07 | Las pruebas de los cuatro CA | Test | 3 h | T-06 | Todos | EV-01 |
| T-08 | Generarlo sobre este repositorio y **contar las marcas que quedaron** | Medición | 2 h | T-06 | CA-02 | EV-02 |

**Total estimado:** 17 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-05 → T-06 → T-08.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| [CA-01](../HU-002-generar-el-entregable-de-ofimatica.md#ca-01--un-expediente-completo-se-genera-con-todas-sus-secciones) | Contar los documentos del archivo contra el expediente | EV-01, EV-02 | | ☐ |
| [CA-02](../HU-002-generar-el-entregable-de-ofimatica.md#ca-02--las-listas-y-las-tablas-salen-como-listas-y-tablas) | **Contar las marcas del origen que quedaron a la vista**, sobre el archivo real | EV-02 | | ☐ |
| [CA-03](../HU-002-generar-el-entregable-de-ofimatica.md#ca-03--generar-dos-veces-da-el-mismo-resultado) | Generar dos veces y comparar | EV-01 | | ☐ |
| [CA-04](../HU-002-generar-el-entregable-de-ofimatica.md#ca-04--con-espacios-sin-llenar-avisa-antes-de-generar) | Un expediente con huecos | EV-01 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas del entregable | `plataforma/nucleo/expediente/tests_entregable.py` |
| EV-02 | El entregable de este repositorio, medido | `resultado_pruebas.md` §2 |

---

## 6. Datos y ambiente de prueba

Documentos de mentiras que la prueba escribe, y **el expediente real** para la medición del `CA-02`. El módulo escribe un solo archivo, en la carpeta de datos.

---

## 7. Reversión / rollback  ·  Q11

El entregable **se rehace**: borrarlo no pierde nada. El código está versionado.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna migración, ninguna dependencia nueva.

---

## 9. Reglas aplicadas  ·  Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F19`](../../../../../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md), [`04·S2`](../../../../../base/04-seguridad.md) al escapar lo que viene del texto.
- Producto: `DA-09`, y `RN-6` de la especificación del módulo.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que el formato se rompa en listas y tablas | **Alto — es el riesgo que la HU nombra** | Se prueba con documentos reales y se **cuenta** cuántas marcas quedaron | Abierto hasta T-08 |
| B-02 | Que el convertidor invente una etiqueta y el documento diga otra cosa | Alto | Lo que no se reconoce se escapa y se deja como texto | Cerrado |
| B-03 | Que dos corridas difieran por la fecha | Medio | La fecha no va dentro del archivo | Cerrado |

---

## 11. Definition of Done

- [ ] Los cuatro CA verificados con evidencia
- [ ] El entregable de este repositorio generado, **con las marcas contadas**
- [ ] Dos corridas comparadas
- [ ] Las dos baterías en verde
- [ ] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
