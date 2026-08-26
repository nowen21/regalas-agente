# Plan de Trabajo — Fase A-EP-001-HU-014-adoptar-la-guia-del-desarrollo-profesional (módulo Cuerpo de reglas)

**Para qué sirve este documento.** Dice qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba está aceptando el alcance y el costo. El requisito vive en [HU-014](../HU-014-la-guia-de-entrada-del-estandar.md); el detalle de las pruebas, en el `plan_pruebas.md` de esta misma fase; lo que dieron al correrlas, en el `resultado_pruebas.md`; lo que quede hecho, en el documento de cierre.

## 0. Identificación y origen

| Campo | Valor |
|---|---|
| **Fase** (identificador · [`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-001-HU-014-adoptar-la-guia-del-desarrollo-profesional` |
| **Épica** | [EP-001 Cuerpo de reglas heredable y en capas](../../epica.md) |
| **HU** | [HU-014 La guía de entrada del estándar](../HU-014-la-guia-de-entrada-del-estandar.md) — una sola (`F12.1`) |
| **Módulo** | Cuerpo de reglas |
| **Especificación del módulo** | [HU-014](../HU-014-la-guia-de-entrada-del-estandar.md). El entregable es un documento: sus CA son la especificación |
| **Fecha apertura** | 2026-08-21 |
| **Rama** | `main` — el commit lo autoriza el usuario |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)): ✨ **Funcionalidad nueva**, bajada del [pendiente 73](../../../../../pendientes/hecho/la-guia-de-entrada-es-del-estandar.md) por [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md): la guía del desarrollo profesional quedó escrita en el proyecto `matematica` y es doctrina de cualquier proyecto. El usuario eligió bajarlo («73», 2026-08-21) tras el análisis que lo puso después del 74 — decisión suya, registrada acá.

**CA de la HU que cubre esta fase**

| CA de HU-014 | Qué exige | Estado hoy, verificado el 2026-08-21 |
|---|---|---|
| [CA-01](../HU-014-la-guia-de-entrada-del-estandar.md#ca-01--la-guía-existe-en-el-estándar-completa-y-enlazada-al-cuerpo-normativo) | La guía en `base/`, con 10 pasos y 9 cualidades enlazados al cuerpo normativo, sin restos del proyecto de origen | No existe: en `base/` no hay documento de entrada; el material está en el adjunto `73-adjunto-guia-desarrollo-profesional.md` (borrado al cerrar el pendiente, como este ordenaba; el historial de git lo conserva) |
| [CA-02](../HU-014-la-guia-de-entrada-del-estandar.md#ca-02--la-guía-llega-a-los-herederos-y-se-encuentra-sin-saber-que-existe) | Viaja con `base/`, nombrada desde su README y el mapa, sin engordar el arranque | No aplica todavía: depende del CA-01 |

---

## 1. Objetivo y alcance  ·  `F14` Q4

**Objetivo:** que la guía sea un documento del estándar, heredable y enlazado a las reglas que explica, y que el pendiente 73 cierre con su aviso al proyecto de origen.

**Fuera de alcance:**

- Crear reglas o validadores (RN-03 de la HU). Si al escribir aparece algo que deba ser norma, se pausa y se propone (`02·F20`).
- Reemplazar la copia de `matematica`: es del proyecto de origen, con el aviso de cierre.
- El pendiente 74 y el 75, que tocan zonas vecinas.

---

## 2. Análisis previo — línea base verificada  ·  `F17`

> Verificado contra el repositorio el 2026-08-21.

- El material completo está en el adjunto: 10 pasos, 9 cualidades, la sección «cómo lo modela el estándar» y la frase resumen. Sus partes de origen (tabla «cómo se vivió en este proyecto», rutas de `matematica`) no entran.
- En `base/` no hay documento de entrada; el vecino natural es [`base/glosario.md`](../../../../../base/glosario.md): material de consulta que viaja con la carpeta y que el cargador **no** suma al arranque (carga los archivos numerados).
- El [README de `base/`](../../../../../base/README.md) presenta la carpeta y nombra al glosario: la guía se nombra ahí mismo.
- El [mapa del sitio](../../../../../anatomia/mapa-del-sitio.md) lista qué archivo hace qué: fila nueva.

### 2.1 Archivos que se crean o modifican  ·  `F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `base/guia-de-entrada.md` | Nuevo | Cuerpo de reglas | La guía, reescrita desde el adjunto con sus enlaces |
| [`base/README.md`](../../../../../base/README.md) | Modificar | Cuerpo de reglas | La nombra como puerta de entrada, junto al glosario |
| [`anatomia/mapa-del-sitio.md`](../../../../../anatomia/mapa-del-sitio.md) | Modificar | Anatomía | Su fila |
| [`CHANGELOG.md`](../../../../../CHANGELOG.md) · [`VERSION`](../../../../../VERSION) | Modificar | Versionado | Entrada MENOR; `VERSION` se lee un instante antes (`20·M18`) |
| [`pendientes/73-la-guia-…`](../../../../../pendientes/hecho/la-guia-de-entrada-es-del-estandar.md) | Mover | Backlog | A `hecho/` con `cerrar.py`, con su aviso de vuelta a `matematica` |
| `pendientes/73-adjunto-guia-desarrollo-profesional.md` | Borrar | Backlog | El propio pendiente lo ordena: «el adjunto se borra al cerrar». Su fila del índice sale con él |
| [`pendientes/README.md`](../../../../../pendientes/README.md) | Modificar | Backlog | Filas del 73 y del adjunto |
| [`HU-014](../HU-014-la-guia-de-entrada-del-estandar.md) | Modificar | Documentación | §7 al cerrar; bitácora |
| Documentos de esta fase | Llenar | Documentación | resultado, estado, cierre |

> **Ninguna regla se toca.** La guía cita; no re-enuncia ni cambia exigencias.

### 2.2 Matriz de dependencias del refactor  ·  `F17`

Ninguna: no cambia contrato de código ni texto de regla.

### 2.3 Rutas / endpoints  ·  `F14` Q6 · 2.4 Punto de entrada  ·  Q7 · 2.5 Permisos  ·  Q8

No aplica API ni permisos. Punto de entrada: el README de `base/` y el mapa del sitio; el lector llega por ahí, no por el arranque.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación |
|---|---|---|
| `base/guia-de-entrada.md`, junto al glosario | `anatomia/` (opción del pendiente) | `anatomia/` no viaja a los herederos; lo heredable vive en `base/`. El pendiente ya descartó la plantilla-copia por multiplicar versiones |
| Fuera del arranque del cargador | Sumarla a los archivos que se cargan al abrir | El arranque va en 68 de 90 KB; la guía es de consulta, como el glosario, no regla que rige cada frase |
| Subida MENOR | MAYOR | Documento aditivo: nadie al día tiene que hacer nada |

### 2.7 Dudas por resolver antes de ejecutar

Ninguna: el material está completo y la decisión de sitio queda en este plan, que se aprueba.

---

## 3. Desglose de tareas por criterio de aceptación

### CA-01 — La guía existe, completa y enlazada

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-01 | Escribir `base/guia-de-entrada.md` desde el adjunto: 10 pasos con su enlace a las reglas de flujo, 9 cualidades con su enlace a capítulos y patrones, sin restos del origen | `base/guia-de-entrada.md` | 2,5 |

### CA-02 — Llega a los herederos y se encuentra

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-02 | Nombrarla en el README de `base/` y en el mapa del sitio | README · mapa | 0,5 |

### Cierre

| # | Tarea | Archivo | Horas |
|---|---|---|---|
| T-03 | Ejecutar los casos y registrar el resultado | `resultado_pruebas.md` | 1,0 |
| T-04 | Versionar (MENOR) | CHANGELOG · VERSION | 0,5 |
| T-05 | Cerrar: pendiente 73 a `hecho/` con aviso a `matematica`, borrar el adjunto, cierre de fase y HU | backlog + fase | 1,0 |

**Total: 5 tareas · 5,5 horas.**

---

## 4. Secuencia de ejecución

T-01 → T-02 → T-03 → T-04 → T-05, sin paralelos.

> Solo se tocan los archivos declarados en §2.1 ([`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md)).

---

## 5. Verificación de criterios de aceptación  ·  `F14` Q10

| CA | Método de verificación | Evidencia |
|---|---|---|
| CA-01 | Conteo (10 y 9), recorrido de enlaces y comparación contra el adjunto | CP-001 |
| CA-02 | El documento dentro de `base/`, nombrado en README y mapa; el arranque sin crecer | CP-002 |

---

## 6. Datos y ambiente de prueba

Este repositorio. Las pruebas son de lectura y comparación; `validar.py estandar` comprueba los enlaces. Ningún dato real.

---

## 7. Reversión / rollback  ·  `F14` Q11

`git revert` del commit de la fase. El adjunto borrado vuelve del historial si hiciera falta.

---

## 8. Producción y migración incremental  ·  `F14` Q12 · `F10`

Los herederos reciben la guía con `base/` en su próxima instalación, avisados por el desfase de versión. `matematica` además recibe el aviso de vuelta de `cerrar.py` para reemplazar su copia por el puntero.

---

## 9. Reglas del estándar aplicadas  ·  `F14` Q13

[`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md), [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md), [`02·F23`](../../../../../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md), [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md), [`13·DOC14`](../../../../../base/13-documentacion/reglas/DOC14-enlaza-cada-md-con-ruta-legible-y-destino-relativo.md), [`20·M3`](../../../../../base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md), [`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md), [`20·M13`](../../../../../base/20-meta-reglas/reglas/M13-lo-que-no-es-regla-del-estandar-tiene-su-propio-sitio.md), [`20·M17`](../../../../../base/20-meta-reglas/reglas/M17-la-entrada-del-registro-abre-en-castellano-llano.md), [`20·M18`](../../../../../base/20-meta-reglas/reglas/M18-lo-compartido-se-lee-un-instante-antes-de-escribirlo.md).

---

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| R-01 | Que la guía re-enuncie normas y diverja del cuerpo | Dos textos que envejecen distinto | RN-02: cada punto enlaza a su regla; la exigencia vive solo allá | Mitigado por diseño |
| R-02 | Que el trinquete de marcas frene el documento nuevo | Rechaza el commit | Se escribe sin rayas nuevas ni tipografía de máquina, como quedó aprendido hoy | Abierto |

---

## 11. Definition of Done

- [ ] `base/guia-de-entrada.md` publicado, con CP-001 y CP-002 aprobados.
- [ ] README de `base/` y mapa del sitio al día.
- [ ] Versión MENOR subida; pendiente 73 en `hecho/` con su aviso; adjunto borrado.
- [ ] `validar.py estandar` y `pendientes` sin fallas nuevas.
- [ ] Aprobado por el usuario antes del commit.

---

## 12. Seguimiento diario

No aplica: el avance en vivo va en el `estado-fase.md`.

---

## 13. Cierre

No se escribe acá: vive en el `funcionalidad_implementada.md` de esta fase. Este plan se queda como se aprobó.
