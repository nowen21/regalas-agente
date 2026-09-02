# Plan de Trabajo — Fase `V-EP-008-HU-005-lo-obligatorio-no-se-apaga` (módulo Proyectos)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación. El requisito vive en la HU; las pruebas, en el `plan_pruebas`; lo que quedó hecho, en el `funcionalidad_implementada.md`.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `V-EP-008-HU-005-lo-obligatorio-no-se-apaga` |
| **Épica** | [EP-008](../../epica.md) |
| **HU** | [HU-005 Configurar qué rige en cada proyecto](../HU-005-configurar-que-rige-en-cada-proyecto.md), una sola (`F12.1`) |
| **Módulo** | Proyectos |
| **Especificación del módulo** | [documentacion/proyectos/spec.md](../../../../proyectos/spec.md) |
| **Fecha apertura** | 2026-09-01 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- 📋 **Ficha de `F-004`:** *«que un proyecto pequeño no cargue con lo que solo necesita uno grande»*, con su exigencia dura: *«lo obligatorio no se puede apagar»*.

> **El usuario autorizó ejecutar sin aprobar paso por paso** el 2026-09-01.

**CA de la HU que cubre esta fase:** los tres, todos ☑.

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que un proyecto pueda encender y apagar las reglas opcionales, y **solo las opcionales**.

**La exigencia dura es la que sostiene todo:** si lo obligatorio se puede apagar, «configurable» quiere decir «el estándar rige cuando conviene», que es no tener estándar.

**Fuera de alcance:** elegir moldes por proyecto —se deja para cuando haya más de uno por documento— y la pantalla.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo que ya existe y se reutiliza:** las marcas que el propio estándar usa para lo opcional: `*opt-in*` en la regla, y `[CAPA 2 · opt-in]` en la cabecera de un capítulo, que rige a todas las suyas.

**Lo verificado, y es lo que salvó la funcionalidad:** de las **257 reglas**, las opcionales son **49**. La primera versión del detector daba **52**, y entre ellas `02·F0`.

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/proyectos/configuracion.py` | Crear | Servicio | Qué es opcional, y qué rige |
| `plataforma/nucleo/proyectos/management/commands/que_rige.py` | Crear | Consola | La orden |
| `plataforma/nucleo/proyectos/tests_configuracion.py` | Crear | Prueba | Los tres CA |
| `documentacion/proyectos/spec.md` | Modificar | Especificación | Su §13 |

**Ninguna entidad y ninguna migración:** la configuración vive en el proyecto, no en la base.

### 2.2 Matriz de dependencias del refactor

**Nada existente se toca.** El módulo Proyectos crece con un archivo nuevo.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican: órdenes de consola.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **Qué es opcional lo dice el estándar** | Guardar acá una lista propia | Una segunda lista envejece en cuanto el estándar marque una regla más |
| **La marca vale donde está escrita** | Buscarla en todo el archivo | Buscarla en el archivo entero contagia a todas las reglas que lo acompañan: dio 52, y una era `02·F0` |
| **Ante la duda, es obligatoria** | Ante la duda, opcional | La respuesta segura es la que no deja apagar nada |
| **La configuración vive en el proyecto** | Guardarla en la base de la plataforma | Un proyecto clonado se quedaría sin ella |
| **De fábrica, lo opcional viene apagado** | Encendido | Encender es una decisión; que quede escrita con fecha y con quién |
| **Cambiar de estado reemplaza la fila** | Agregar una fila cada vez | La historia la guarda el control de versiones, no el archivo |

### 2.7 Dudas por resolver antes de codificar

Ninguna al empezar. **La que apareció fue al mirar la lista nombre por nombre**, y no en el número: sobraba `02·F0`.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | Hallar qué reglas son opcionales, leyendo `base/` | Servicio | 1,5 h | — | CA-01 | EV-01 |
| T-02 | Escribir el estado en el proyecto, con fecha y quién | Servicio | 1,5 h | T-01 | CA-01 | EV-01 |
| T-03 | Rechazar apagar una obligatoria | Servicio | 1 h | T-01 | CA-02 | EV-01 |
| T-04 | Entregar lo de ese proyecto y de ninguno más | Servicio | 1 h | T-02 | CA-03 | EV-01 |
| T-05 | La orden de consola | Consola | 1 h | T-04 | — | EV-01 |
| T-06 | Las pruebas de los tres CA | Test | 2 h | T-05 | Todos | EV-01 |

**Total estimado:** 8 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-03 → T-06. **T-01 es la crítica de verdad**: de esa lista depende qué se puede apagar.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Encendiendo y apagando, y releyendo | EV-01 | 2026-09-01 | ☑ |
| CA-02 | Intentándolo con una obligatoria | EV-01 | 2026-09-01 | ☑ |
| CA-03 | Con dos proyectos a la vez | EV-01 | 2026-09-01 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas de la fase | `plataforma/nucleo/proyectos/tests_configuracion.py` |

---

## 6. Datos y ambiente de prueba

Un estándar de mentiras con tres capítulos —uno obligatorio, uno opt-in entero y uno con una sola regla marcada—, y dos proyectos en carpetas temporales.

---

## 7. Reversión / rollback  ·  Q11

Se quita el archivo del módulo y no queda rastro. **Lo que queda es el `.agente/configuracion.md` de cada proyecto**, que es del proyecto y lo borra su dueño.

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna migración, ninguna dependencia nueva.

---

## 9. Reglas aplicadas  ·  Q13

- Base: el capítulo [`20`](../../../../../base/20-meta-reglas/base.md), que fija cómo se marca una regla opcional, y `03·DA-01`.
- Producto: las `RN-1` a `RN-5` de la historia.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | **Que se marque como opcional algo que no lo es** | **Crítico: se podría apagar el estándar** | La marca vale donde está escrita, y la lista se leyó nombre por nombre | Cerrado |
| B-02 | Que la configuración no viaje con el repositorio | Alto | Vive en el proyecto, en `.agente/` | Cerrado |
| B-03 | Que una regla desconocida se deje apagar | Alto | Ante la duda, es obligatoria | Cerrado |
| B-04 | Que cada opción aleje dos proyectos entre sí | Medio | **Se acepta y se declara:** está en la ficha, y no se resuelve con código | Declarado |

---

## 11. Definition of Done

- [x] Los tres CA verificados con evidencia
- [x] Comprobado que una obligatoria no se apaga
- [x] La lista de opcionales leída nombre por nombre
- [x] Las dos baterías en verde
- [x] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
