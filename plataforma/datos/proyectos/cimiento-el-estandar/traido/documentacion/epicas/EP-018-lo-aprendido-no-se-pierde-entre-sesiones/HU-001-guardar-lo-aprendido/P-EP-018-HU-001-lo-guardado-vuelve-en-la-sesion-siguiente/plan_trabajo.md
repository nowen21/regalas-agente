# Plan de Trabajo — Fase `P-EP-018-HU-001-lo-guardado-vuelve-en-la-sesion-siguiente` (módulo Memoria)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación. El requisito vive en la HU; las pruebas, en el `plan_pruebas`; lo que quedó hecho, en el `funcionalidad_implementada.md`.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `P-EP-018-HU-001-lo-guardado-vuelve-en-la-sesion-siguiente` |
| **Épica** | [EP-018](../../epica.md) |
| **HU** | [HU-001 Guardar lo aprendido](../HU-001-guardar-lo-aprendido.md), una sola (`F12.1`) |
| **Módulo** | Memoria |
| **Especificación del módulo** | [documentacion/memoria/spec.md](../../../../memoria/spec.md) |
| **Fecha apertura** | 2026-09-01 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- 📋 **Ficha de `F-023`:** *«es la mitad del problema original: sin esto, cada sesión vuelve a empezar»*.

> **El usuario autorizó ejecutar sin aprobar paso por paso** el 2026-09-01.

**CA de la HU que cubre esta fase:** los tres, todos ☑.

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** poder guardar un recuerdo y volver a leerlo, sin abrir los archivos a mano.

**Lo que esta fase NO decide es dónde vive la memoria.** Eso ya lo decidió `01·C19`: un archivo del repositorio por recuerdo, con su línea en el índice, y el almacén de la herramienta vacío.

**Fuera de alcance:** decidir qué merece recordarse, y la pantalla.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo que ya existe y se reutiliza:** la carpeta `historico-chat/memory/` con sus recuerdos y su índice.

**Lo verificado:** los recuerdos están ahí y siguen el formato de `01·C19`. No hay que migrar nada.

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/memoria/__init__.py` | Crear | Módulo | Nace |
| `plataforma/nucleo/memoria/core.py` | Crear | Servicio | Leer, buscar y guardar |
| `plataforma/nucleo/memoria/management/commands/memoria.py` | Crear | Consola | La orden |
| `plataforma/nucleo/memoria/tests.py` | Crear | Prueba | Los tres CA |
| `documentacion/memoria/spec.md` | Crear | Especificación | El módulo |

**Ninguna entidad y ninguna migración:** `DA-01`, el texto es la verdad.

### 2.2 Matriz de dependencias del refactor

**Nada existente se toca.** El módulo lee archivos que ya están.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican: órdenes de consola.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **Sin entidad en la base** | Una tabla de recuerdos | Todo lo que responde está en el texto (`DA-01`) |
| **Guardar no pisa** | Sobrescribir | Perder un recuerdo es el peor fallo posible acá |
| **La carpeta y el índice se leen al pedir** | Un caché | Los archivos cambian por fuera, y el caché mentiría |
| **Un tema sin recuerdos se dice con palabras** | Devolver una lista vacía | Un vacío se ve igual que una falla — `S-110` |

### 2.7 Dudas por resolver antes de codificar

Ninguna: el formato lo fija `01·C19`.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | Leer la carpeta y el índice | Servicio | 1 h | — | CA-01 | EV-01 |
| T-02 | Separar vigentes de dados de baja | Servicio | 1 h | T-01 | CA-01 | EV-01 |
| T-03 | Buscar por palabra | Servicio | 1 h | T-01 | CA-03 | EV-01 |
| T-04 | Guardar sin pisar, con su línea de índice | Servicio | 1 h | T-01 | Transversal | EV-01 |
| T-05 | El resumen | Servicio | 30 min | T-02 | CA-02 | EV-01 |
| T-06 | La orden de consola | Consola | 1 h | T-05 | — | EV-01 |
| T-07 | Las pruebas de los tres CA | Test | 2 h | T-06 | Todos | EV-01 |

**Total estimado:** 7,5 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-04 → T-07.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Guardando y volviendo a leer desde cero | EV-01 | 2026-09-01 | ☑ |
| CA-02 | Con dos carpetas de proyecto distintas | EV-01 | 2026-09-01 | ☑ |
| CA-03 | Buscando algo que no existe | EV-01 | 2026-09-01 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas del módulo | `plataforma/nucleo/memoria/tests.py` |

---

## 6. Datos y ambiente de prueba

Carpetas temporales con recuerdos de mentiras. **La carpeta real no se toca al probar** (`08·T4`).

---

## 7. Reversión / rollback  ·  Q11

Módulo nuevo: se quita y no queda rastro. **Ningún archivo de recuerdos se modifica al leer.**

---

## 8. Producción y migración incremental  ·  Q12

**Aditivo puro.** Ninguna migración, ninguna dependencia nueva.

---

## 9. Reglas aplicadas  ·  Q13

- Base: `01·C19` (dónde vive la memoria), `03·DA-01` (el texto es la verdad), el capítulo [`15`](../../../../../base/15-registros-inmutables.md).
- Producto: las `RN-1` a `RN-5` de la historia.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | **Que guardar pise un recuerdo existente** | **Alto: se pierde lo aprendido** | No pisa: avisa, y hay prueba | Cerrado |
| B-02 | Que un tema sin recuerdos se vea como una falla | Medio | Se dice con palabras | Cerrado |
| B-03 | Que un recuerdo equivocado siga rigiendo | Medio | **Se acepta y se declara:** nada lo revisa solo | Declarado |

---

## 11. Definition of Done

- [x] Los tres CA verificados con evidencia
- [x] Comprobado que guardar no pisa
- [x] Las dos baterías en verde
- [x] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
