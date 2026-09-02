# Plan de Trabajo — Fase `M-EP-017-HU-001-una-aprobacion-guarda-la-huella-del-texto` (módulo Aprobaciones)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba** cada criterio de aceptación. El requisito vive en la HU; las pruebas, en el `plan_pruebas`; lo que quedó hecho, en el `funcionalidad_implementada.md`.

---

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `M-EP-017-HU-001-una-aprobacion-guarda-la-huella-del-texto` |
| **Épica** | [EP-017](../../epica.md) |
| **HU** | [HU-001 Registrar una aprobación con su firma](../HU-001-registrar-una-aprobacion-con-su-firma.md), una sola (`F12.1`) |
| **Módulo** | Aprobaciones |
| **Especificación del módulo** | [documentacion/aprobaciones/spec.md](../../../../aprobaciones/spec.md) |
| **Fecha apertura** | 2026-09-01 |
| **Rama** | `main` |
| Sprint · Dev · Revisor · QA | No aplica: una sola persona cumple los roles |

**ORIGEN:**

- ✨ **Funcionalidad nueva:** `F-015`. Su ficha dice que **es la pieza que hoy no existe, y de la que se sostiene todo el gobierno**.

> **El usuario autorizó ejecutar sin aprobar paso por paso** el 2026-09-01.

**CA de la HU que cubre esta fase:** los tres, todos ☑.

---

## 1. Objetivo y alcance  ·  Q4

**Objetivo:** que una aprobación diga quién, cuándo y **sobre qué texto exacto**.

**Sin la huella, «aprobado» no dice nada.** El documento pudo cambiar tres veces desde entonces.

**Fuera de alcance:** comprobar quién es quien aprueba, y migrar las 21 marcas escritas a mano.

---

## 2. Análisis previo — línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

**Lo medido el 2026-09-01:**

| Qué se midió | Resultado |
|---|---|
| Documentos con aprobación escrita a mano | **21** |
| De esas, cuántas dicen sobre qué texto | **Ninguna** |
| Módulos de la plataforma con entidad propia | 1, y este es el segundo |

**Por qué esta sí guarda.** Los demás módulos calculan al pedir porque su respuesta está en el texto. Esta no: **el texto no sabe quién lo aprobó**.

### 2.1 Archivos que se crean o modifican  ·  Q9

| Archivo | Tipo | Capa | Nota |
|---|---|---|---|
| `plataforma/nucleo/aprobaciones/models.py` | Nuevo | Modelo | La aprobación, con su huella |
| `plataforma/nucleo/aprobaciones/core.py` | Nuevo | Servicio | Aprobar y consultar |
| `plataforma/nucleo/aprobaciones/apps.py` | Nuevo | Config | |
| `plataforma/nucleo/aprobaciones/migrations/0001_initial.py` | Nuevo | Modelo | Lo genera Django |
| `plataforma/nucleo/aprobaciones/management/commands/aprobar.py` | Nuevo | Orden | Aprobar |
| `plataforma/nucleo/aprobaciones/tests.py` | Nuevo | Prueba | Los tres CA |
| `plataforma/config/settings/base.py` | Modificar | Config | La aplicación en la lista |
| `documentacion/aprobaciones/spec.md` | Nuevo | Especificación | Módulo nuevo |

### 2.2 Matriz de dependencias del refactor

No aplica: todo es nuevo. Usa la auditoría y no la modifica.

### 2.3 Rutas · 2.4 UI · 2.5 Permisos

No aplican.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| **La aprobación se guarda en la base** | Escribirla en el documento | Es lo que se hace hoy, y no dice sobre qué texto |
| **Se guarda la huella del texto** | Solo quién y cuándo | Sin ella no se puede responder si lo aprobado sigue siendo lo que hay |
| **No se aprueba lo que no existe** | Aceptarlo | Sería firmar en blanco: cuando aparezca diría que ya se aprobó |
| **Se guarda también el tamaño** | Solo la huella | Permite decir cuánto cambió, no solo que cambió |
| **Cada aprobación se agrega** | Reemplazar la anterior | Es la historia de qué se autorizó |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

---

## 3. Desglose de tareas

| ID | Tarea | Capa | Est. | Depende de | CA | Ev. |
|---|---|---|:--:|---|---|---|
| T-01 | La entidad, con su huella y su tamaño | Modelo | 2 h | — | CA-01 | EV-01 |
| T-02 | Aprobar, leyendo el texto que hay | Servicio | 2 h | T-01 | CA-01 | EV-01 |
| T-03 | Rechazar lo que no existe | Servicio | 1 h | T-02 | CA-03 | EV-01 |
| T-04 | Registrar en la auditoría | Servicio | 1 h | T-02 | — | EV-01 |
| T-05 | Consultar la historia | Servicio | 1 h | T-01 | CA-02 | EV-01 |
| T-06 | La orden de consola | Orden | 1 h | T-03 | Todos | EV-02 |
| T-07 | Las pruebas de los tres CA | Test | 2 h | T-06 | Todos | EV-01 |

**Total estimado:** 10 h

---

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 → T-02 → T-03 → T-06.

---

## 5. Verificación de criterios de aceptación  ·  Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Aprobando y mirando la huella guardada | EV-01 | 2026-09-01 | ☑ |
| CA-02 | Consultando la historia después | EV-01 | 2026-09-01 | ☑ |
| CA-03 | Con una ruta inventada y con un proyecto que no existe | EV-01 | 2026-09-01 | ☑ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Las pruebas del módulo | `plataforma/nucleo/aprobaciones/tests.py` |
| EV-02 | La orden de consola | `resultado_pruebas.md` §2 |

---

## 6. Datos y ambiente de prueba

Carpetas temporales con documentos de mentiras. **Ningún documento real se aprueba al probar.**

---

## 7. Reversión / rollback  ·  Q11

Una tabla nueva, sin datos previos. El código está versionado.

---

## 8. Producción y migración incremental  ·  Q12

**Una migración**, la de la tabla nueva. Ninguna dependencia nueva.

---

## 9. Reglas aplicadas  ·  Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), y el capítulo [`15`](../../../../../base/15-registros-inmutables.md) por lo de que nada se borra.
- Producto: `DA-08`, y las `RN-1` a `RN-4` de la historia.

---

## 10. Riesgos y bloqueos

| ID | Riesgo / Bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | **Que se apruebe sin huella** | **Alto** | Sin huella no se guarda: va en la misma escritura | Cerrado |
| B-02 | Firmar en blanco un documento que no existe | Alto | Está impedido, y hay prueba de que no queda registro | Cerrado |
| B-03 | Que una aprobación se pise al volver a aprobar | Medio | Cada una se agrega | Cerrado |

---

## 11. Definition of Done

- [x] Los tres CA verificados con evidencia
- [x] Comprobado que la huella es la del texto aprobado
- [x] Comprobado que un intento fallido no deja registro
- [x] Las dos baterías en verde
- [x] Señales registradas
- [ ] Aceptada por el usuario

---

## 12. Seguimiento diario

No aplica.

---

## 13. Cierre

**No se escribe acá.** El cierre vive en el `funcionalidad_implementada.md`.
